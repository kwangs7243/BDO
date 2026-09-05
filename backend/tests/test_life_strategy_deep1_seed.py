from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import Session

from app.checklists import get_current_checklists
from app.database import get_session
from app.life import get_life_skill
from app.main import app
from app.models import (
    ChecklistInstance,
    ChecklistItemState,
    ChecklistTemplate,
    ChecklistTemplateItem,
    Content,
    ContentRelation,
    ContentRequirement,
    ContentSection,
    ContentStep,
    Evidence,
    Material,
    Project,
    ProjectMaterial,
    ProjectMaterialSource,
    ProjectStage,
    ProjectStageDependency,
    Reward,
    ScheduleRule,
    Source,
    UserContentState,
    UserMaterialInventory,
    UserProjectStageState,
)
from app.periods import KST
from app.prompt_bridge import build_context
from app.schemas import PromptMode, PromptRequest
from app.seed import import_seed


DATA_DIR = Path(__file__).resolve().parents[2] / "data"
V19C_SOURCE_IDS = {
    "gathering-location-strategy-2026-05-24",
    "fishing-onboarding-strategy-2024-12-05",
    "fishing-afk-bottlenecks-2025-03-11",
    "hunting-lion-strategy-2024-10-15",
    "hunting-shadow-lion-strategy-2026-06-21",
}
V19C_CONTENT_SLUGS = {
    "gathering-onboarding-strategy",
    "fishing-onboarding-strategy",
    "hunting-onboarding-strategy",
}
COMMUNITY_SOURCE_TYPES = {"community_strategy", "community_discussion"}
FIXED_NOW = datetime(2026, 9, 6, 12, tzinfo=KST)


def _seed_rows() -> tuple[list[dict], list[dict]]:
    sources = json.loads((DATA_DIR / "seed_sources.json").read_text(encoding="utf-8"))
    contents = json.loads((DATA_DIR / "seed_contents.json").read_text(encoding="utf-8"))
    return sources, contents


def _content_row(slug: str) -> dict:
    _, contents = _seed_rows()
    return next(row for row in contents if row["slug"] == slug)


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


def test_v19c_seed_identity_source_references_and_status() -> None:
    sources, contents = _seed_rows()
    source_ids = [row["id"] for row in sources]
    content_slugs = [row["slug"] for row in contents]
    new_sources = [row for row in sources if row["id"] in V19C_SOURCE_IDS]
    new_contents = [row for row in contents if row["slug"] in V19C_CONTENT_SLUGS]

    assert len(new_sources) == len(V19C_SOURCE_IDS)
    assert len(new_contents) == len(V19C_CONTENT_SLUGS)
    assert len(source_ids) == len(set(source_ids))
    assert len(content_slugs) == len(set(content_slugs))
    for source in new_sources:
        assert source["url"] and [row["url"] for row in sources].count(source["url"]) == 1
        assert source["source_type"] in COMMUNITY_SOURCE_TYPES
        assert source["publisher"] != "Pearl Abyss"
    for content in new_contents:
        assert content["status"] == "active"
        assert content["last_verified_at"] == "2026-09-06"
        for claim in content["evidence"]:
            assert set(claim["source_ids"]) <= set(source_ids)


def test_v19c_seed_keys_and_claim_coverage() -> None:
    for slug in V19C_CONTENT_SLUGS:
        content = _content_row(slug)
        children = [
            *content["requirements"],
            *content["steps"],
            *content["sections"],
            *content["relations"],
            *content["evidence"],
        ]
        assert all(row["seed_key"].startswith(f"{slug}.") for row in children)
        assert len([row["seed_key"] for row in children]) == len(
            {row["seed_key"] for row in children}
        )

        expected_entities = {
            slug,
            *(row["seed_key"] for row in content["requirements"]),
            *(row["seed_key"] for row in content["steps"]),
            *(row["seed_key"] for row in content["sections"]),
        }
        claimed_entities = {
            row.get("entity_seed_key", slug) for row in content["evidence"]
        }
        assert claimed_entities == expected_entities


def test_v19c_is_strategy_only_and_excludes_dynamic_values() -> None:
    for slug in V19C_CONTENT_SLUGS:
        content = _content_row(slug)
        assert all(
            row["structured_value"]["knowledge_role"] == "strategy"
            for row in content["requirements"]
        )
        assert any(row["section_type"] == "strategy" for row in content["sections"])
        assert "schedules" not in content
        assert "checklists" not in content
        assert "rewards" not in content

        serialized = json.dumps(content, ensure_ascii=False).lower()
        assert "은화/h" not in serialized
        assert "silver/hour" not in serialized
        assert "실시간 거래소" not in serialized
        assert "현재 거래소 가격" not in serialized
        assert "무조건" not in serialized
        assert "최고 채집" not in serialized
        assert "최고 수렵" not in serialized


def test_gathering_onboarding_semantics_and_relations(session: Session) -> None:
    content = _orm_content(session, "gathering-onboarding-strategy")
    purpose = next(row for row in content.requirements if row.seed_key.endswith("purpose-choice"))
    route = next(row for row in content.requirements if row.seed_key.endswith("route-context"))

    assert purpose.structured_value["single_default_goal"] is False
    assert route.structured_value["universal_best_route"] is False
    assert len(content.steps) == 7
    assert {"preparation", "first_time", "maintenance"} == {
        row.phase for row in content.steps
    }
    assert {
        "gathering-current-system",
        "gathering-tools",
        "life-mastery-foundation",
        "energy-foundation",
    } <= _relation_targets(content)
    assert any("목적 기반" in row.title for row in content.sections)


def test_fishing_onboarding_modes_bottlenecks_and_relations(session: Session) -> None:
    content = _orm_content(session, "fishing-onboarding-strategy")
    mode = next(row for row in content.requirements if row.seed_key.endswith("mode-choice"))
    bottlenecks = next(
        row for row in content.requirements if row.seed_key.endswith("session-bottlenecks")
    )

    assert mode.structured_value["modes"] == ["afk", "active", "weekly_contest"]
    assert mode.structured_value["weekly_rotating_target_static"] is False
    assert {"inventory_space", "rod_durability", "discard_setting"} <= set(
        bottlenecks.structured_value["decision_dimensions"]
    )
    assert {
        "fishing-current-system",
        "auto-fishing",
        "fish-freshness-and-trade",
        "fishing-encyclopedia-and-weekly-contest",
    } <= _relation_targets(content)
    assert len(content.steps) == 8


def test_hunting_onboarding_modes_progression_and_relations(session: Session) -> None:
    content = _orm_content(session, "hunting-onboarding-strategy")
    mode = next(row for row in content.requirements if row.seed_key.endswith("mode-choice"))
    target = next(row for row in content.requirements if row.seed_key.endswith("target-context"))

    assert mode.structured_value["modes"] == [
        "individual_matchlock",
        "sniper",
        "cooperative",
    ]
    assert target.structured_value["lion_is_advanced_example"] is True
    assert target.structured_value["universal_best_target"] is False
    assert {
        "hunting-current-system",
        "hunting-firearms",
        "sniper-hunting",
        "life-mastery-foundation",
    } <= _relation_targets(content)
    progression = next(
        row for row in content.sections if row.seed_key.endswith("section.progression")
    )
    assert "상위 단계 사례" in progression.body_markdown


def test_v19c_evidence_keeps_official_and_community_roles_separate(session: Session) -> None:
    for slug in V19C_CONTENT_SLUGS:
        content = _orm_content(session, slug)
        entity_ids = {
            slug,
            *(row.seed_key for row in content.requirements),
            *(row.seed_key for row in content.steps),
            *(row.seed_key for row in content.sections),
        }
        evidence = list(
            session.scalars(select(Evidence).where(Evidence.entity_id.in_(entity_ids)))
        )
        source_types = {row.source.source_type for row in evidence}
        assert "official_guide" in source_types
        assert source_types & COMMUNITY_SOURCE_TYPES
        assert all(row.active and row.verification_status == "verified" for row in evidence)
        assert all(
            row.section_type in {"strategy", "common_mistakes"}
            for row in content.sections
        )


def test_life_api_discovers_v19c_without_duplicate_sections(session: Session) -> None:
    expected = {
        "gathering": "gathering-onboarding-strategy",
        "fishing": "fishing-onboarding-strategy",
        "hunting": "hunting-onboarding-strategy",
    }
    client = _client(session)
    try:
        hub = client.get("/api/life")
        assert hub.status_code == 200
        assert len(hub.json()["skills"]) == 10
        for skill, slug in expected.items():
            response = client.get(f"/api/life/{skill}")
            assert response.status_code == 200
            payload = response.json()
            getting_started = [row["slug"] for row in payload["getting_started"]]
            all_slugs = [
                row["slug"]
                for section in (
                    "foundation_contents",
                    "getting_started",
                    "equipment",
                    "core_systems",
                    "recurring_contents",
                    "advanced_contents",
                    "related_economy",
                )
                for row in payload[section]
            ]
            assert slug in getting_started
            assert len(all_slugs) == len(set(all_slugs))
    finally:
        app.dependency_overrides.clear()
        client.close()


def test_v19c_content_works_with_existing_prompt_modes(session: Session) -> None:
    for slug in V19C_CONTENT_SLUGS:
        onboarding = build_context(
            session,
            PromptRequest(
                mode=PromptMode.CONTENT_ONBOARDING,
                content_slug=slug,
                as_of=FIXED_NOW,
            ),
            FIXED_NOW,
        )
        assert onboarding.canonical_facts
        assert not onboarding.open_questions_or_conflicts
        assert {row.id for row in onboarding.sources} & V19C_SOURCE_IDS

    for mode in (PromptMode.NEXT_ACTION, PromptMode.VERIFY_LATEST):
        bundle = build_context(
            session,
            PromptRequest(
                mode=mode,
                content_slug="gathering-onboarding-strategy",
                as_of=FIXED_NOW,
            ),
            FIXED_NOW,
        )
        assert bundle.sources


def test_v19c_current_system_responsibility_is_not_duplicated(session: Session) -> None:
    for slug in V19C_CONTENT_SLUGS:
        content = _orm_content(session, slug)
        assert all(
            row.structured_value["knowledge_role"] == "strategy"
            for row in content.requirements
        )
        assert any(
            relation.relation_type == "prerequisite"
            and relation.to_content.slug.endswith("-current-system")
            for relation in content.outgoing_relations
        )
        assert not content.schedules
        assert not content.checklist_templates
        assert not content.rewards


def test_v19c_temp_db_migration_import_idempotence_and_user_history_preservation(
    tmp_path, monkeypatch
) -> None:
    db_path = tmp_path / "v19c-validation.db"
    database_url = f"sqlite:///{db_path.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", database_url)

    backend_dir = Path(__file__).resolve().parents[1]
    alembic_config = Config(str(backend_dir / "alembic.ini"))
    alembic_config.set_main_option("script_location", str(backend_dir / "alembic"))
    command.upgrade(alembic_config, "20260902_0001")
    command.upgrade(alembic_config, "head")

    source_rows, content_rows = _seed_rows()
    baseline_dir = tmp_path / "v19b-seed"
    baseline_dir.mkdir()
    (baseline_dir / "seed_sources.json").write_text(
        json.dumps(
            [row for row in source_rows if row["id"] not in V19C_SOURCE_IDS],
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    (baseline_dir / "seed_contents.json").write_text(
        json.dumps(
            [row for row in content_rows if row["slug"] not in V19C_CONTENT_SLUGS],
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    shutil.copy(DATA_DIR / "seed_projects.json", baseline_dir / "seed_projects.json")

    canonical_models = (
        Source,
        Content,
        ScheduleRule,
        ContentRequirement,
        ContentStep,
        Reward,
        ContentSection,
        ChecklistTemplate,
        ChecklistTemplateItem,
        ContentRelation,
        Evidence,
        Project,
        ProjectStage,
        ProjectStageDependency,
        Material,
        ProjectMaterial,
        ProjectMaterialSource,
    )
    engine = create_engine(database_url)
    with Session(engine, expire_on_commit=False) as db_session:
        import_seed(db_session, baseline_dir)
        baseline_content = _orm_content(db_session, "gathering-current-system")
        baseline_requirement = db_session.scalar(
            select(ContentRequirement).where(
                ContentRequirement.seed_key == "gathering-current-system.action-map"
            )
        )
        assert baseline_requirement is not None
        baseline_ids = (baseline_content.id, baseline_requirement.id)
        archived_requirement = db_session.scalar(
            select(ContentRequirement).where(ContentRequirement.active.is_(False))
        )
        assert archived_requirement is not None
        archived_marker = (archived_requirement.id, archived_requirement.seed_key)

        get_current_checklists(db_session, "weekly", FIXED_NOW)
        checklist_state = db_session.scalar(select(ChecklistItemState))
        assert checklist_state is not None
        checklist_state.completed = True
        checklist_state.note = "V1.9C checklist history marker"

        user_state = UserContentState(
            content_id=baseline_content.id,
            state="in_progress",
            priority=1,
            note="V1.9C content state marker",
            updated_at=FIXED_NOW,
        )
        material = db_session.scalar(select(Material).where(Material.key == "moon-vein-flax"))
        stage = db_session.scalar(select(ProjectStage).order_by(ProjectStage.order_no))
        assert material is not None and stage is not None
        inventory = UserMaterialInventory(
            material_id=material.id,
            quantity=37,
            note="V1.9C inventory marker",
            updated_at=FIXED_NOW,
        )
        stage_state = UserProjectStageState(
            stage_id=stage.id,
            completed=True,
            completed_at=FIXED_NOW,
            note="V1.9C project stage marker",
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
        new_ids = {
            row.slug: row.id
            for row in db_session.scalars(
                select(Content).where(Content.slug.in_(V19C_CONTENT_SLUGS))
            )
        }

        import_seed(db_session, DATA_DIR)
        assert first_counts == tuple(
            db_session.scalar(select(func.count()).select_from(model))
            for model in canonical_models
        )
        assert new_ids == {
            row.slug: row.id
            for row in db_session.scalars(
                select(Content).where(Content.slug.in_(V19C_CONTENT_SLUGS))
            )
        }
        assert baseline_ids == (
            _orm_content(db_session, "gathering-current-system").id,
            db_session.scalar(
                select(ContentRequirement.id).where(
                    ContentRequirement.seed_key == "gathering-current-system.action-map"
                )
            ),
        )
        preserved_archived = db_session.get(ContentRequirement, archived_marker[0])
        assert preserved_archived is not None
        assert (preserved_archived.seed_key, preserved_archived.active) == (
            archived_marker[1],
            False,
        )
        assert (
            db_session.scalar(select(func.count()).select_from(ChecklistInstance))
            == history_ids[0]
        )
        assert db_session.get(ChecklistItemState, history_ids[1]).note == (
            "V1.9C checklist history marker"
        )
        assert db_session.get(UserContentState, history_ids[2]).note == (
            "V1.9C content state marker"
        )
        assert db_session.get(UserMaterialInventory, history_ids[3]).note == (
            "V1.9C inventory marker"
        )
        assert db_session.get(UserProjectStageState, history_ids[4]).note == (
            "V1.9C project stage marker"
        )
