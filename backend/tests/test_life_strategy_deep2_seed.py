from __future__ import annotations

import json
import shutil
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
V19E_SOURCE_IDS = {
    "farming-market-prep-2026-05-29",
    "processing-mass-recipes-2026-07-22",
    "farming-purpose-strategy-2025-09-15",
    "farming-onboarding-strategy-2025-09-21",
    "processing-route-strategy-2026-01-21",
}
V19E_CONTENT_SLUGS = {
    "farming-onboarding-strategy",
    "processing-onboarding-strategy",
}
COMMUNITY_SOURCE_TYPES = {"community_strategy", "community_discussion"}
FIXED_NOW = datetime(2026, 9, 6, 12, tzinfo=KST)


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


def test_v19e_seed_identity_sources_and_references() -> None:
    sources, contents = _seed_rows()
    source_ids = [row["id"] for row in sources]
    source_urls = [row["url"] for row in sources]
    content_slugs = [row["slug"] for row in contents]

    assert len([row for row in sources if row["id"] in V19E_SOURCE_IDS]) == 5
    assert len([row for row in contents if row["slug"] in V19E_CONTENT_SLUGS]) == 2
    assert len(source_ids) == len(set(source_ids))
    assert len(source_urls) == len(set(source_urls))
    assert len(content_slugs) == len(set(content_slugs))

    referenced = {
        source_id
        for content in contents
        for evidence in content.get("evidence", [])
        for source_id in evidence.get("source_ids", [])
    }
    assert referenced <= set(source_ids)
    assert {
        row["source_type"]
        for row in sources
        if row["id"] in V19E_SOURCE_IDS
    } == {"official_patch", "community_strategy"}


def test_v19e_farming_fact_audit_keeps_latest_official_chain() -> None:
    current = _content_row("farming-current-cycle")
    bird_damage = next(
        row for row in current["requirements"] if row["seed_key"].endswith("bird-damage")
    )
    evidence = next(
        row
        for row in current["evidence"]
        if row["seed_key"].endswith("requirement.bird-damage")
    )

    assert bird_damage["structured_value"] == {
        "knowledge_role": "fact",
        "health_reduction_percent_approx": 0.25,
        "previous_percent_approx": 4.16,
        "effective_from": "2026-06-10",
    }
    assert evidence["source_ids"] == ["grind-profit-update-2026-06-10"]
    assert evidence["verification_status"] == "verified"

    strategy = _content_row("farming-onboarding-strategy")
    current_rules = next(
        row for row in strategy["sections"] if row["seed_key"].endswith("current-rules")
    )
    assert "2026-05-29" in current_rules["body_markdown"]
    assert "06-04" in current_rules["body_markdown"]
    assert "06-10" in current_rules["body_markdown"]
    assert "06-17" in current_rules["body_markdown"]


def test_v19e_seed_keys_claim_coverage_and_strategy_scope() -> None:
    for slug in V19E_CONTENT_SLUGS:
        content = _content_row(slug)
        assert content["status"] == "active"
        assert content["last_verified_at"] == "2026-09-06"
        assert all(
            row["structured_value"]["knowledge_role"] == "strategy"
            for row in content["requirements"]
        )
        assert "schedules" in content and content["schedules"] == []
        assert "checklists" in content and content["checklists"] == []
        assert "rewards" in content and content["rewards"] == []

        nested = [
            *content["requirements"],
            *content["steps"],
            *content["sections"],
            *content["relations"],
            *content["evidence"],
        ]
        keys = [row["seed_key"] for row in nested]
        assert all(key.startswith(f"{slug}.") for key in keys)
        assert len(keys) == len(set(keys))

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

        serialized = json.dumps(content, ensure_ascii=False).lower()
        for forbidden in (
            "silver/hour",
            "current market price",
            "guaranteed best",
        ):
            assert forbidden not in serialized


def test_farming_onboarding_semantics_and_relations(session: Session) -> None:
    content = _orm_content(session, "farming-onboarding-strategy")
    purpose = next(row for row in content.requirements if row.seed_key.endswith("purpose-choice"))
    action = next(row for row in content.requirements if row.seed_key.endswith("harvest-or-breed"))
    location = next(row for row in content.requirements if row.seed_key.endswith("location-context"))

    assert purpose.structured_value["single_default_goal"] is False
    assert purpose.structured_value["universal_best_crop"] is False
    assert action.structured_value["mixed_cycle_supported"] is True
    assert action.structured_value["universal_best_action"] is False
    assert location.structured_value["universal_best_location"] is False
    assert len(content.steps) == 8
    assert {
        "farming-current-cycle",
        "farming-fences",
        "farming-seeds-harvest-breeding",
        "old-moon-seed-pouch",
        "farming-moles",
        "worker-current-system",
    } <= _relation_targets(content)


def test_processing_onboarding_semantics_and_relations(session: Session) -> None:
    content = _orm_content(session, "processing-onboarding-strategy")
    mode = next(row for row in content.requirements if row.seed_key.endswith("normal-or-mass"))
    route = next(row for row in content.requirements if row.seed_key.endswith("route-validation"))
    bottlenecks = next(
        row for row in content.requirements if row.seed_key.endswith("session-bottlenecks")
    )

    assert mode.structured_value["fixed_quantity_threshold"] is None
    assert mode.structured_value["universal_best_mode"] is False
    assert route.structured_value["recipe_catalog_static"] is False
    assert {"weight", "inventory_space", "storage_space"} <= set(
        bottlenecks.structured_value["bottlenecks"]
    )
    assert len(content.steps) == 8
    assert {
        "processing-current-system",
        "mass-processing",
        "processing-stones-and-clothes",
        "life-common-gear",
        "life-mastery-foundation",
        "storage-current-system",
    } <= _relation_targets(content)
    known_issue = next(
        row for row in content.sections if row.seed_key.endswith("current-known-issue")
    )
    assert "2026-09-06" in known_issue.body_markdown
    assert "09-09" in known_issue.body_markdown


def test_v19e_evidence_keeps_official_and_community_roles_separate(session: Session) -> None:
    for slug in V19E_CONTENT_SLUGS:
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
        assert any(source_type.startswith("official_") for source_type in source_types)
        assert source_types & COMMUNITY_SOURCE_TYPES
        assert all(row.active and row.verification_status == "verified" for row in evidence)


def test_life_api_discovers_v19e_after_current_facts(session: Session) -> None:
    client = _client(session)
    try:
        for skill, current_slug, strategy_slug in (
            ("farming", "farming-current-cycle", "farming-onboarding-strategy"),
            ("processing", "processing-current-system", "processing-onboarding-strategy"),
        ):
            response = client.get(f"/api/life/{skill}")
            assert response.status_code == 200
            payload = response.json()
            getting_started = [row["slug"] for row in payload["getting_started"]]
            assert getting_started[:2] == [current_slug, strategy_slug]
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
            assert len(all_slugs) == len(set(all_slugs))
    finally:
        app.dependency_overrides.clear()
        client.close()


def test_v19e_prompt_emits_strategy_role_for_supported_claims(session: Session) -> None:
    for slug in V19E_CONTENT_SLUGS:
        detail = get_content_detail(session, slug, FIXED_NOW)
        bundle = build_context(
            session,
            PromptRequest(
                mode=PromptMode.CONTENT_ONBOARDING,
                content_slug=slug,
                as_of=FIXED_NOW,
            ),
            FIXED_NOW,
        )
        knowledge = {
            item.claim: item
            for item in [*bundle.canonical_facts, *bundle.open_questions_or_conflicts]
        }
        expected = {
            detail.summary,
            detail.purpose,
            *(row.description for row in detail.requirements),
            *(f"{row.title}: {row.description}" for row in detail.steps),
            *(f"{row.title}: {row.body_markdown}" for row in detail.sections),
        }
        assert expected <= set(knowledge)
        assert all(
            knowledge[claim].knowledge_role == PromptKnowledgeRole.STRATEGY
            for claim in expected
        )
        assert not bundle.open_questions_or_conflicts

        for mode in (PromptMode.NEXT_ACTION, PromptMode.VERIFY_LATEST):
            followup = build_context(
                session,
                PromptRequest(mode=mode, content_slug=slug, as_of=FIXED_NOW),
                FIXED_NOW,
            )
            assert followup.canonical_facts
            assert not followup.open_questions_or_conflicts
            assert all(
                item.knowledge_role == PromptKnowledgeRole.STRATEGY
                for item in followup.canonical_facts
            )


def test_v19e_temp_db_import_is_idempotent_and_preserves_user_history(
    tmp_path, monkeypatch
) -> None:
    db_path = tmp_path / "v19e-validation.db"
    database_url = f"sqlite:///{db_path.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", database_url)

    backend_dir = Path(__file__).resolve().parents[1]
    config = Config(str(backend_dir / "alembic.ini"))
    config.set_main_option("script_location", str(backend_dir / "alembic"))
    command.upgrade(config, "20260902_0001")
    command.upgrade(config, "head")

    source_rows, content_rows = _seed_rows()
    baseline_contents = [
        row for row in content_rows if row["slug"] not in V19E_CONTENT_SLUGS
    ]
    farming = next(
        row for row in baseline_contents if row["slug"] == "farming-current-cycle"
    )
    farming["requirements"] = [
        row
        for row in farming["requirements"]
        if not row["seed_key"].endswith("bird-damage")
    ]
    farming["evidence"] = [
        row
        for row in farming["evidence"]
        if not row["seed_key"].endswith("requirement.bird-damage")
    ]

    baseline_dir = tmp_path / "v19d-seed"
    baseline_dir.mkdir()
    (baseline_dir / "seed_sources.json").write_text(
        json.dumps(
            [row for row in source_rows if row["id"] not in V19E_SOURCE_IDS],
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    (baseline_dir / "seed_contents.json").write_text(
        json.dumps(baseline_contents, ensure_ascii=False),
        encoding="utf-8",
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
    )
    engine = create_engine(database_url)
    with Session(engine, expire_on_commit=False) as db_session:
        import_seed(db_session, baseline_dir)
        existing = _orm_content(db_session, "farming-current-cycle")
        existing_requirement = db_session.scalar(
            select(ContentRequirement).where(
                ContentRequirement.seed_key == "farming-current-cycle.growth-time"
            )
        )
        assert existing_requirement is not None
        stable_ids = (existing.id, existing_requirement.id)

        get_current_checklists(db_session, "weekly", FIXED_NOW)
        checklist_state = db_session.scalar(select(ChecklistItemState))
        material = db_session.scalar(select(Material).where(Material.key == "moon-vein-flax"))
        stage = db_session.scalar(select(ProjectStage).order_by(ProjectStage.order_no))
        assert checklist_state is not None and material is not None and stage is not None
        checklist_state.completed = True
        checklist_state.note = "V1.9E checklist marker"
        user_state = UserContentState(
            content_id=existing.id,
            state="in_progress",
            priority=1,
            note="V1.9E content marker",
            updated_at=FIXED_NOW,
        )
        inventory = UserMaterialInventory(
            material_id=material.id,
            quantity=19,
            note="V1.9E inventory marker",
            updated_at=FIXED_NOW,
        )
        stage_state = UserProjectStageState(
            stage_id=stage.id,
            completed=True,
            completed_at=FIXED_NOW,
            note="V1.9E stage marker",
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
                select(Content).where(Content.slug.in_(V19E_CONTENT_SLUGS))
            )
        }
        bird_damage = db_session.scalar(
            select(ContentRequirement).where(
                ContentRequirement.seed_key == "farming-current-cycle.bird-damage"
            )
        )
        assert bird_damage is not None

        import_seed(db_session, DATA_DIR)
        assert first_counts == tuple(
            db_session.scalar(select(func.count()).select_from(model))
            for model in canonical_models
        )
        assert new_ids == {
            row.slug: row.id
            for row in db_session.scalars(
                select(Content).where(Content.slug.in_(V19E_CONTENT_SLUGS))
            )
        }
        assert stable_ids == (
            _orm_content(db_session, "farming-current-cycle").id,
            db_session.scalar(
                select(ContentRequirement.id).where(
                    ContentRequirement.seed_key == "farming-current-cycle.growth-time"
                )
            ),
        )
        assert (
            db_session.scalar(select(func.count()).select_from(ChecklistInstance))
            == history_ids[0]
        )
        assert db_session.get(ChecklistItemState, history_ids[1]).note == (
            "V1.9E checklist marker"
        )
        assert db_session.get(UserContentState, history_ids[2]).note == (
            "V1.9E content marker"
        )
        assert db_session.get(UserMaterialInventory, history_ids[3]).note == (
            "V1.9E inventory marker"
        )
        assert db_session.get(UserProjectStageState, history_ids[4]).note == (
            "V1.9E stage marker"
        )
