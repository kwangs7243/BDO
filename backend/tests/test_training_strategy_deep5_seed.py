from __future__ import annotations

import json
import shutil
from collections import Counter
from datetime import datetime
from pathlib import Path

from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import Session

from app.checklists import get_current_checklists
from app.content import get_content_detail
from app.database import get_session
from app.main import app
from app.models import (
    ChecklistInstance,
    ChecklistItemState,
    Content,
    ContentRelation,
    ContentRequirement,
    ContentSection,
    ContentStep,
    Evidence,
    Material,
    ProjectMaterialSource,
    Project,
    ProjectMaterial,
    ProjectStage,
    Source,
    UserContentState,
    UserMaterialInventory,
    UserProjectStageState,
)
from app.periods import KST
from app.prompt_bridge import build_context
from app.schemas import PromptKnowledgeRole, PromptMode, PromptRequest
from app.seed import import_seed


DATA_DIR = Path(__file__).resolve().parents[2] / "data"
V19H_SOURCE_ID = "training-beginner-decisions-2026-02-05"
V19H_CONTENT_SLUG = "training-onboarding-strategy"
FERN_EXCHANGE_KEY = "dream-horse-material-routines.fern-training-material-exchange"
FIXED_NOW = datetime(2026, 9, 7, 12, tzinfo=KST)
TRAINING_FACT_SLUGS = {
    "training-current-system",
    "training-mastery-effects",
    "wild-horse-capture",
    "horse-breeding-exchange",
    "horse-imperial-delivery",
    "courser-system",
    "dream-horse-awakening",
    "mythical-dream-horse",
    "training-growth-surprise-quest",
    "dream-horse-material-routines",
}


def _seed_rows() -> tuple[list[dict], list[dict]]:
    sources = json.loads((DATA_DIR / "seed_sources.json").read_text(encoding="utf-8"))
    contents = json.loads((DATA_DIR / "seed_contents.json").read_text(encoding="utf-8"))
    return sources, contents


def _content_row(slug: str) -> dict:
    return next(row for row in _seed_rows()[1] if row["slug"] == slug)


def _orm_content(session: Session, slug: str) -> Content:
    content = session.scalar(select(Content).where(Content.slug == slug))
    assert content is not None
    return content


def _relation_targets(content: Content) -> set[str]:
    return {row.to_content.slug for row in content.outgoing_relations if row.active}


def _client(session: Session) -> TestClient:
    def override_session():
        yield session

    app.dependency_overrides[get_session] = override_session
    return TestClient(app)


def _explicit_role_counts(contents: list[dict]) -> Counter[str]:
    return Counter(
        structured["knowledge_role"]
        for content in contents
        for requirement in content.get("requirements", [])
        if isinstance((structured := requirement.get("structured_value")), dict)
        and structured.get("knowledge_role") in {"fact", "strategy", "measurement"}
    )


def test_v19h_seed_identity_counts_and_references() -> None:
    sources, contents = _seed_rows()
    source_ids = [row["id"] for row in sources]
    source_urls = [row["url"] for row in sources]
    content_slugs = [row["slug"] for row in contents]

    assert len(sources) >= 165
    assert len(contents) >= 269
    assert sum(len(row.get("relations", [])) for row in contents) >= 478
    assert len(source_ids) == len(set(source_ids))
    assert len(source_urls) == len(set(source_urls))
    assert len(content_slugs) == len(set(content_slugs))
    assert V19H_SOURCE_ID in source_ids
    assert V19H_CONTENT_SLUG in content_slugs
    assert all(row.get("status", "active") == "active" for row in contents)

    referenced = {
        source_id
        for content in contents
        for evidence in content.get("evidence", [])
        for source_id in evidence.get("source_ids", [])
    }
    assert referenced <= set(source_ids)
    role_counts = _explicit_role_counts(contents)
    assert role_counts["fact"] >= 195
    assert role_counts["strategy"] >= 57
    assert role_counts["measurement"] >= 11


def test_v19h_source_roles_and_shared_patch_metadata() -> None:
    sources, _ = _seed_rows()
    by_id = {row["id"]: row for row in sources}
    community = by_id[V19H_SOURCE_ID]
    shared_patch = by_id["processing-mass-recipes-2026-07-22"]

    assert community["source_type"] == "community_strategy"
    assert community["published_at"] == "2026-02-05"
    assert community["url"] == "https://www.inven.co.kr/board/black/3583/1995323"
    assert "수치" in community["notes"] and "채택하지 않음" in community["notes"]
    assert shared_patch["source_type"] == "official_patch"
    assert shared_patch["published_at"] == "2026-07-22"
    assert "고비 뿌리" in shared_patch["notes"]


def test_v19h_current_fact_audits() -> None:
    wild = _content_row("wild-horse-capture")
    generations = next(
        row for row in wild["requirements"] if row["seed_key"].endswith(".generations")
    )
    wild_evidence = next(
        row for row in wild["evidence"] if row["seed_key"].endswith(".claim.generations")
    )
    assert generations["structured_value"]["population_increased_at"] == "2026-07-15"
    assert wild_evidence["source_ids"] == ["blood-altar-challenge-2026-07-15"]

    routines = _content_row("dream-horse-material-routines")
    exchange = next(
        row for row in routines["requirements"] if row["seed_key"] == FERN_EXCHANGE_KEY
    )
    assert routines["last_verified_at"] == "2026-09-07"
    assert exchange["structured_value"]["knowledge_role"] == "fact"
    assert exchange["structured_value"]["input"] == {"item": "고비 뿌리", "amount": 3}
    assert exchange["structured_value"]["choose_one"] == [
        {"item": "돌꼬리 여물", "amount": 1},
        {"item": "바람결 소라해초", "amount": 1},
        {"item": "짙푸른 발굽뿌리", "amount": 1},
    ]
    exchange_evidence = next(
        row
        for row in routines["evidence"]
        if row["entity_seed_key"] == FERN_EXCHANGE_KEY
    )
    assert exchange_evidence["source_ids"] == ["processing-mass-recipes-2026-07-22"]
    assert exchange_evidence["verification_status"] == "verified"

    gear = _content_row("life-common-gear")
    category_slots = next(
        row for row in gear["requirements"] if row["seed_key"].endswith(".category-slots")
    )
    assert category_slots["structured_value"]["training"] == [
        "조련복",
        "마편",
        "조련 유물/광명석",
    ]
    assert gear["last_verified_at"] == "2026-09-03"


def test_v19h_strategy_semantics_and_static_scope() -> None:
    content = _content_row(V19H_CONTENT_SLUG)
    requirements = {
        row["seed_key"].removeprefix(f"{V19H_CONTENT_SLUG}."): row
        for row in content["requirements"]
    }

    assert content["status"] == "active"
    assert content["last_verified_at"] == "2026-09-07"
    assert len(requirements) == 6
    assert len(content["steps"]) == 10
    assert len(content["sections"]) == 3
    assert content["rewards"] == []
    assert content["schedules"] == []
    assert content["checklists"] == []
    assert all(
        row["structured_value"]["knowledge_role"] == "strategy"
        for row in requirements.values()
    )

    purpose = requirements["purpose-choice"]["structured_value"]
    starting = requirements["starting-horse-choice"]["structured_value"]
    capture = requirements["capture-or-owned"]["structured_value"]
    outcome = requirements["outcome-choice"]["structured_value"]
    advanced = requirements["advanced-progression"]["structured_value"]
    mode = requirements["session-mode"]["structured_value"]
    assert purpose["single_default_goal"] is False
    assert purpose["first_session"] == "one_small_training_goal"
    assert starting["universal_best_horse"] is False
    assert capture["universal_best_capture_location"] is False
    assert outcome["fixed_silver_profit"] is None
    assert outcome["fixed_breeding_ev"] is None
    assert advanced["beginner_default"] is False
    assert advanced["universal_priority"] is False
    assert mode["universal_best_training_method"] is False
    assert mode["improvement_per_session"] == 1

    nested = [
        *content["requirements"],
        *content["steps"],
        *content["sections"],
        *content["relations"],
        *content["evidence"],
    ]
    keys = [row["seed_key"] for row in nested]
    assert all(key.startswith(f"{V19H_CONTENT_SLUG}.") for key in keys)
    assert len(keys) == len(set(keys))
    expected_entities = {
        V19H_CONTENT_SLUG,
        *(row["seed_key"] for row in content["requirements"]),
        *(row["seed_key"] for row in content["steps"]),
        *(row["seed_key"] for row in content["sections"]),
    }
    assert {
        row.get("entity_seed_key", V19H_CONTENT_SLUG) for row in content["evidence"]
    } == expected_entities


def test_v19h_relations_preserve_fact_ownership(session: Session) -> None:
    content = _orm_content(session, V19H_CONTENT_SLUG)
    assert _relation_targets(content) == TRAINING_FACT_SLUGS
    assert len(content.requirements) == 6
    assert len(content.steps) == 10
    assert len(content.sections) == 3

    serialized = json.dumps(_content_row(V19H_CONTENT_SLUG), ensure_ascii=False)
    assert "+50%" not in serialized
    assert "2026-09-16" not in serialized
    assert "event_bonus" not in serialized
    assert "market_price" not in serialized
    assert "success_probability" not in serialized


def test_v19h_evidence_keeps_official_and_community_roles_separate(
    session: Session,
) -> None:
    content = _orm_content(session, V19H_CONTENT_SLUG)
    entity_ids = {
        V19H_CONTENT_SLUG,
        *(row.seed_key for row in content.requirements),
        *(row.seed_key for row in content.steps),
        *(row.seed_key for row in content.sections),
    }
    evidence = list(
        session.scalars(select(Evidence).where(Evidence.entity_id.in_(entity_ids)))
    )
    source_types = {row.source.source_type for row in evidence}
    assert {"official_guide", "official_patch", "community_strategy"} <= source_types
    assert all(row.active and row.verification_status == "verified" for row in evidence)

    fern_evidence = session.scalar(
        select(Evidence).where(
            Evidence.seed_key
            == f"dream-horse-material-routines.requirement.fern-training-material-exchange::processing-mass-recipes-2026-07-22"
        )
    )
    assert fern_evidence is not None
    assert fern_evidence.source.source_type == "official_patch"


def test_life_api_discovers_v19h_training_order(session: Session) -> None:
    client = _client(session)
    try:
        response = client.get("/api/life/training")
        assert response.status_code == 200
        payload = response.json()
        assert [row["slug"] for row in payload["getting_started"]][:3] == [
            "training-current-system",
            "training-onboarding-strategy",
            "wild-horse-capture",
        ]
        assert len(client.get("/api/life").json()["skills"]) == 10
    finally:
        app.dependency_overrides.clear()
        client.close()


def test_v19h_prompt_emits_strategy_role_in_existing_modes(session: Session) -> None:
    detail = get_content_detail(session, V19H_CONTENT_SLUG, FIXED_NOW)
    expected = {
        detail.summary,
        detail.purpose,
        *(row.description for row in detail.requirements),
        *(f"{row.title}: {row.description}" for row in detail.steps),
        *(f"{row.title}: {row.body_markdown}" for row in detail.sections),
    }
    for mode in (
        PromptMode.CONTENT_ONBOARDING,
        PromptMode.NEXT_ACTION,
        PromptMode.VERIFY_LATEST,
    ):
        bundle = build_context(
            session,
            PromptRequest(mode=mode, content_slug=V19H_CONTENT_SLUG, as_of=FIXED_NOW),
            FIXED_NOW,
        )
        knowledge = {
            item.claim: item
            for item in [
                *bundle.canonical_facts,
                *bundle.open_questions_or_conflicts,
            ]
        }
        assert expected <= set(knowledge)
        assert all(
            knowledge[text].knowledge_role == PromptKnowledgeRole.STRATEGY
            for text in expected
        )
        assert not bundle.open_questions_or_conflicts


def test_v19h_temp_db_import_is_idempotent_and_preserves_history(
    tmp_path, monkeypatch
) -> None:
    db_path = tmp_path / "v19h-validation.db"
    database_url = f"sqlite:///{db_path.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", database_url)

    backend_dir = Path(__file__).resolve().parents[1]
    config = Config(str(backend_dir / "alembic.ini"))
    config.set_main_option("script_location", str(backend_dir / "alembic"))
    command.upgrade(config, "20260902_0001")
    command.upgrade(config, "head")

    source_rows, current_contents = _seed_rows()
    baseline_sources = [row for row in source_rows if row["id"] != V19H_SOURCE_ID]
    baseline_contents = json.loads(json.dumps(current_contents, ensure_ascii=False))
    baseline_contents = [
        row for row in baseline_contents if row["slug"] != V19H_CONTENT_SLUG
    ]
    routines = next(
        row for row in baseline_contents if row["slug"] == "dream-horse-material-routines"
    )
    routines["last_verified_at"] = "2026-09-03"
    routines["summary"] = (
        "고비 뿌리와 몽상의 깃털을 얻는 상시 주간·일일 조련 루틴. "
        "이벤트 추가 보상은 포함하지 않는다."
    )
    routines["purpose"] = "꿈결 환상마 몽상 재료를 상시 반복 의뢰로 모은다."
    routines["requirements"] = [
        row for row in routines["requirements"] if row["seed_key"] != FERN_EXCHANGE_KEY
    ]
    routines["evidence"] = [
        row
        for row in routines["evidence"]
        if row.get("entity_seed_key") != FERN_EXCHANGE_KEY
    ]
    summary_evidence = next(
        row for row in routines["evidence"] if row["seed_key"].endswith(".summary")
    )
    summary_evidence["source_ids"] = [
        "mythical-horse-guide",
        "mythical-horse-update-2023-07-12",
    ]
    summary_evidence["last_verified_at"] = "2026-09-03"
    summary_evidence["note"] = "상시 주간·일일 재료 루틴"

    baseline_dir = tmp_path / "v19g-seed"
    baseline_dir.mkdir()
    (baseline_dir / "seed_sources.json").write_text(
        json.dumps(baseline_sources, ensure_ascii=False), encoding="utf-8"
    )
    (baseline_dir / "seed_contents.json").write_text(
        json.dumps(baseline_contents, ensure_ascii=False), encoding="utf-8"
    )
    shutil.copy(DATA_DIR / "seed_projects.json", baseline_dir / "seed_projects.json")

    canonical_models = (
        Source,
        Content,
        ContentRequirement,
        ContentStep,
        ContentSection,
        ContentRelation,
        Evidence,
        Material,
        Project,
        ProjectStage,
        ProjectMaterial,
        ProjectMaterialSource,
    )
    engine = create_engine(database_url)
    with Session(engine, expire_on_commit=False) as db_session:
        import_seed(db_session, baseline_dir)
        existing = _orm_content(db_session, "dream-horse-material-routines")
        existing_requirement_ids = {
            row.seed_key: row.id for row in existing.requirements
        }
        old_summary_evidence = db_session.scalar(
            select(Evidence).where(
                Evidence.seed_key
                == "dream-horse-material-routines.summary::mythical-horse-guide"
            )
        )
        assert old_summary_evidence is not None
        stable_ids = (existing.id, old_summary_evidence.id, existing_requirement_ids)

        get_current_checklists(db_session, "weekly", FIXED_NOW)
        checklist_state = db_session.scalar(select(ChecklistItemState))
        material = db_session.scalar(select(Material).where(Material.key == "moon-vein-flax"))
        stage = db_session.scalar(select(ProjectStage).order_by(ProjectStage.order_no))
        assert checklist_state is not None and material is not None and stage is not None
        checklist_state.completed = True
        checklist_state.note = "V1.9H checklist marker"
        user_state = UserContentState(
            content_id=existing.id,
            state="in_progress",
            priority=1,
            note="V1.9H content marker",
            updated_at=FIXED_NOW,
        )
        inventory = UserMaterialInventory(
            material_id=material.id,
            quantity=23,
            note="V1.9H inventory marker",
            updated_at=FIXED_NOW,
        )
        stage_state = UserProjectStageState(
            stage_id=stage.id,
            completed=True,
            completed_at=FIXED_NOW,
            note="V1.9H stage marker",
            updated_at=FIXED_NOW,
        )
        db_session.add_all([user_state, inventory, stage_state])
        db_session.commit()
        history_ids = (
            db_session.scalar(select(func.count()).select_from(ChecklistInstance)),
            checklist_state.id,
            user_state.id,
            inventory.id,
            stage_state.id,
        )

        import_seed(db_session, DATA_DIR)
        first_counts = tuple(
            db_session.scalar(select(func.count()).select_from(model))
            for model in canonical_models
        )
        new_content = _orm_content(db_session, V19H_CONTENT_SLUG)
        new_content_id = new_content.id
        import_seed(db_session, DATA_DIR)

        assert first_counts == tuple(
            db_session.scalar(select(func.count()).select_from(model))
            for model in canonical_models
        )
        existing_after = _orm_content(db_session, "dream-horse-material-routines")
        assert stable_ids[0] == existing_after.id
        assert stable_ids[2] == {
            row.seed_key: row.id
            for row in existing_after.requirements
            if row.seed_key in stable_ids[2]
        }
        assert db_session.get(Evidence, stable_ids[1]).active is True
        assert _orm_content(db_session, V19H_CONTENT_SLUG).id == new_content_id
        new_requirement = db_session.scalar(
            select(ContentRequirement).where(
                ContentRequirement.seed_key == FERN_EXCHANGE_KEY
            )
        )
        assert new_requirement is not None and new_requirement.active is True
        new_evidence = db_session.scalar(
            select(Evidence).where(
                Evidence.seed_key
                == "dream-horse-material-routines.requirement.fern-training-material-exchange::processing-mass-recipes-2026-07-22"
            )
        )
        assert new_evidence is not None and new_evidence.active is True
        assert (
            db_session.scalar(select(func.count()).select_from(ChecklistInstance))
            == history_ids[0]
        )
        assert db_session.get(ChecklistItemState, history_ids[1]).note == "V1.9H checklist marker"
        assert db_session.get(UserContentState, history_ids[2]).note == "V1.9H content marker"
        assert db_session.get(UserMaterialInventory, history_ids[3]).note == "V1.9H inventory marker"
        assert db_session.get(UserProjectStageState, history_ids[4]).note == "V1.9H stage marker"
