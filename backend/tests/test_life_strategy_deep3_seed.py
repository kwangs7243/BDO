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
V19F_SOURCE_IDS = {
    "imperial-delivery-guide",
    "golden-seal-guide",
    "cooking-imperial-strategy-2025-01-30",
    "alchemy-imperial-strategy-2024-11-09",
    "cooking-imperial-direction-2025-12-25",
    "alchemy-node-strategy-2025-10-28",
}
V19F_CONTENT_SLUGS = {
    "cooking-onboarding-strategy",
    "alchemy-onboarding-strategy",
}
COMMUNITY_SOURCE_IDS = {
    "cooking-imperial-strategy-2025-01-30",
    "alchemy-imperial-strategy-2024-11-09",
    "cooking-imperial-direction-2025-12-25",
    "alchemy-node-strategy-2025-10-28",
}
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


def _explicit_role_counts(contents: list[dict]) -> Counter[str]:
    return Counter(
        structured["knowledge_role"]
        for content in contents
        for requirement in content.get("requirements", [])
        if isinstance((structured := requirement.get("structured_value")), dict)
        and structured.get("knowledge_role") in {"fact", "strategy", "measurement"}
    )


def test_v19f_seed_identity_sources_roles_and_references() -> None:
    sources, contents = _seed_rows()
    source_ids = [row["id"] for row in sources]
    source_urls = [row["url"] for row in sources]
    content_slugs = [row["slug"] for row in contents]

    assert len([row for row in sources if row["id"] in V19F_SOURCE_IDS]) == 6
    assert len([row for row in contents if row["slug"] in V19F_CONTENT_SLUGS]) == 2
    assert len(source_ids) == len(set(source_ids))
    assert len(source_urls) == len(set(source_urls))
    assert len(content_slugs) == len(set(content_slugs))
    assert all(
        next(row for row in sources if row["id"] == source_id)["source_type"]
        == "community_strategy"
        for source_id in COMMUNITY_SOURCE_IDS
    )
    assert {
        next(row for row in sources if row["id"] == source_id)["source_type"]
        for source_id in V19F_SOURCE_IDS - COMMUNITY_SOURCE_IDS
    } == {"official_guide"}

    referenced = {
        source_id
        for content in contents
        for evidence in content.get("evidence", [])
        for source_id in evidence.get("source_ids", [])
    }
    assert referenced <= set(source_ids)
    assert _explicit_role_counts(contents) == {
        "fact": 194,
        "strategy": 41,
        "measurement": 11,
    }


def test_v19f_current_fact_audit_keeps_existing_canonical_owners() -> None:
    cooking = _content_row("cooking-current-system")
    cooking_mass = _content_row("cooking-mass-production")
    delicacy = _content_row("witch-delicacy")
    imperial = _content_row("imperial-crafting-delivery-daily")
    alchemy = _content_row("alchemy-current-system")
    alchemy_imperial = _content_row("alchemy-imperial-current")
    alchemy_stone = _content_row("alchemy-stone-current-progression")

    assert {row["seed_key"] for row in cooking["requirements"]} == {
        "cooking-current-system.setup",
        "cooking-current-system.minimum-time",
    }
    assert {row["seed_key"] for row in cooking_mass["requirements"]} == {
        "cooking-mass-production.trigger",
        "cooking-mass-production.batch",
    }
    assert {row["seed_key"] for row in delicacy["requirements"]} == {
        "witch-delicacy.origin",
        "witch-delicacy.exchange",
    }
    assert {row["seed_key"] for row in imperial["requirements"]} == {
        "imperial-crafting-delivery-daily.personal-limit",
        "imperial-crafting-delivery-daily.independent-pools",
        "imperial-crafting-delivery-daily.server-stock",
    }
    assert {row["seed_key"] for row in alchemy["requirements"]} == {
        "alchemy-current-system.setup",
        "alchemy-current-system.quantity",
        "alchemy-current-system.categories",
    }
    assert alchemy_imperial["evidence"][0]["source_ids"] == [
        "ocean-iliya-consolidation-2025-05-14"
    ]
    assert {
        "alchemy-stone-current-progression.stages",
        "alchemy-stone-current-progression.rules",
        "alchemy-stone-current-progression.essence",
    } == {row["seed_key"] for row in alchemy_stone["requirements"]}


def test_v19f_seed_keys_claim_coverage_and_static_scope() -> None:
    for slug in V19F_CONTENT_SLUGS:
        content = _content_row(slug)
        assert content["status"] == "active"
        assert content["last_verified_at"] == "2026-09-06"
        assert all(
            row["structured_value"]["knowledge_role"] == "strategy"
            for row in content["requirements"]
        )
        assert content["rewards"] == []
        assert content["schedules"] == []
        assert content["checklists"] == []

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
        assert {
            row.get("entity_seed_key", slug) for row in content["evidence"]
        } == expected_entities

        serialized = json.dumps(content, ensure_ascii=False).lower()
        for forbidden in (
            "silver/hour",
            "현재 거래소 가격",
            "현재 최저가",
            "현재 최고가",
            "guaranteed best",
            "숙련도 +20",
            "최대 소지 무게 +30lt",
        ):
            assert forbidden not in serialized


def test_cooking_onboarding_semantics_and_relations(session: Session) -> None:
    content = _orm_content(session, "cooking-onboarding-strategy")
    purpose = next(row for row in content.requirements if row.seed_key.endswith("purpose-choice"))
    recipe = next(row for row in content.requirements if row.seed_key.endswith("recipe-selection"))
    sourcing = next(row for row in content.requirements if row.seed_key.endswith("ingredient-sourcing"))
    session_rule = next(row for row in content.requirements if row.seed_key.endswith("session-bottlenecks"))
    imperial = next(row for row in content.requirements if row.seed_key.endswith("imperial-decision"))

    assert purpose.structured_value["single_default_goal"] is False
    assert recipe.structured_value["universal_best_recipe"] is False
    assert recipe.structured_value["dynamic_market_rank_excluded"] is True
    assert {"production_node_worker", "farming", "gathering", "marketplace"} <= set(
        sourcing.structured_value["supply_routes"]
    )
    assert session_rule.structured_value["mastery_solves_all"] is False
    assert imperial.structured_value["fixed_profit_threshold"] is None
    assert imperial.structured_value["universal_best_box"] is False
    assert len(content.steps) == 9
    assert any(row.seed_key.endswith("run-small-batch") for row in content.steps)
    assert {
        "cooking-current-system",
        "cooking-mastery-effects",
        "cooking-mass-production",
        "witch-delicacy",
        "imperial-crafting-delivery-daily",
        "cooking-growth-surprise-quest",
        "farming-onboarding-strategy",
        "production-node-current-system",
        "storage-current-system",
    } <= _relation_targets(content)


def test_alchemy_onboarding_semantics_and_relations(session: Session) -> None:
    content = _orm_content(session, "alchemy-onboarding-strategy")
    purpose = next(row for row in content.requirements if row.seed_key.endswith("purpose-choice"))
    chain = next(row for row in content.requirements if row.seed_key.endswith("dependency-chain"))
    recipe = next(row for row in content.requirements if row.seed_key.endswith("recipe-validation"))
    sourcing = next(row for row in content.requirements if row.seed_key.endswith("ingredient-sourcing"))
    output = next(
        row for row in content.requirements if row.seed_key.endswith("imperial-and-output-decision")
    )

    assert purpose.structured_value["single_default_goal"] is False
    assert purpose.structured_value["alchemy_stone_growth_separate"] is True
    assert chain.structured_value["reverse_chain"] == [
        "final_product",
        "alchemy_intermediate",
        "blood_oil_reagent_trace_sap_plant",
        "acquisition_route",
    ]
    assert chain.structured_value["full_recipe_catalog"] is False
    assert recipe.structured_value["failure_may_consume_materials"] is True
    assert recipe.structured_value["first_batch"] == "small"
    assert sourcing.structured_value["universal_bottleneck_material"] is False
    assert output.structured_value["fixed_margin_threshold"] is None
    assert output.structured_value["universal_best_product"] is False
    assert output.structured_value["alchemy_stone_progression_is_advanced_path"] is True
    assert len(content.steps) == 10
    assert {
        "alchemy-current-system",
        "alchemy-mastery-effects",
        "alchemy-products-and-byproducts",
        "alchemy-imperial-current",
        "alchemy-growth-surprise-quest",
        "gathering-onboarding-strategy",
        "farming-onboarding-strategy",
        "production-node-current-system",
        "storage-current-system",
        "alchemy-stone-current-progression",
    } <= _relation_targets(content)


def test_v19f_evidence_keeps_official_and_community_roles_separate(session: Session) -> None:
    for slug in V19F_CONTENT_SLUGS:
        content = _orm_content(session, slug)
        entity_ids = {
            slug,
            *(row.seed_key for row in content.requirements),
            *(row.seed_key for row in content.steps),
            *(row.seed_key for row in content.sections),
        }
        evidence = list(session.scalars(select(Evidence).where(Evidence.entity_id.in_(entity_ids))))
        source_types = {row.source.source_type for row in evidence}
        assert "official_guide" in source_types
        assert "community_strategy" in source_types
        assert all(row.active and row.verification_status == "verified" for row in evidence)


def test_life_api_discovers_v19f_after_current_facts(session: Session) -> None:
    client = _client(session)
    try:
        for skill, current_slug, strategy_slug in (
            ("cooking", "cooking-current-system", "cooking-onboarding-strategy"),
            ("alchemy", "alchemy-current-system", "alchemy-onboarding-strategy"),
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


def test_v19f_prompt_emits_strategy_role_for_supported_claims(session: Session) -> None:
    for slug in V19F_CONTENT_SLUGS:
        detail = get_content_detail(session, slug, FIXED_NOW)
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
                PromptRequest(mode=mode, content_slug=slug, as_of=FIXED_NOW),
                FIXED_NOW,
            )
            knowledge = {
                item.claim: item
                for item in [*bundle.canonical_facts, *bundle.open_questions_or_conflicts]
            }
            assert expected <= set(knowledge)
            assert all(
                knowledge[claim_text].knowledge_role == PromptKnowledgeRole.STRATEGY
                for claim_text in expected
            )
            assert not bundle.open_questions_or_conflicts


def test_v19f_temp_db_import_is_idempotent_and_preserves_user_history(
    tmp_path, monkeypatch
) -> None:
    db_path = tmp_path / "v19f-validation.db"
    database_url = f"sqlite:///{db_path.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", database_url)

    backend_dir = Path(__file__).resolve().parents[1]
    config = Config(str(backend_dir / "alembic.ini"))
    config.set_main_option("script_location", str(backend_dir / "alembic"))
    command.upgrade(config, "20260902_0001")
    command.upgrade(config, "head")

    source_rows, content_rows = _seed_rows()
    baseline_contents = [
        row for row in content_rows if row["slug"] not in V19F_CONTENT_SLUGS
    ]
    baseline_references = {
        source_id
        for content in baseline_contents
        for evidence in content.get("evidence", [])
        for source_id in evidence.get("source_ids", [])
    }
    baseline_sources = [
        row
        for row in source_rows
        if row["id"] not in V19F_SOURCE_IDS or row["id"] in baseline_references
    ]

    baseline_dir = tmp_path / "v19e-seed"
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
    )
    engine = create_engine(database_url)
    with Session(engine, expire_on_commit=False) as db_session:
        import_seed(db_session, baseline_dir)
        existing = _orm_content(db_session, "cooking-current-system")
        existing_requirement = db_session.scalar(
            select(ContentRequirement).where(
                ContentRequirement.seed_key == "cooking-current-system.setup"
            )
        )
        archived_evidence = db_session.scalar(
            select(Evidence).where(Evidence.active.is_(False)).order_by(Evidence.id)
        )
        assert existing_requirement is not None and archived_evidence is not None
        stable_ids = (existing.id, existing_requirement.id)
        archived_marker = (
            archived_evidence.id,
            archived_evidence.verification_status,
            archived_evidence.source_id,
        )

        get_current_checklists(db_session, "weekly", FIXED_NOW)
        checklist_state = db_session.scalar(select(ChecklistItemState))
        material = db_session.scalar(select(Material).where(Material.key == "moon-vein-flax"))
        stage = db_session.scalar(select(ProjectStage).order_by(ProjectStage.order_no))
        assert checklist_state is not None and material is not None and stage is not None
        checklist_state.completed = True
        checklist_state.note = "V1.9F checklist marker"
        user_state = UserContentState(
            content_id=existing.id,
            state="in_progress",
            priority=1,
            note="V1.9F content marker",
            updated_at=FIXED_NOW,
        )
        inventory = UserMaterialInventory(
            material_id=material.id,
            quantity=19,
            note="V1.9F inventory marker",
            updated_at=FIXED_NOW,
        )
        stage_state = UserProjectStageState(
            stage_id=stage.id,
            completed=True,
            completed_at=FIXED_NOW,
            note="V1.9F stage marker",
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
                select(Content).where(Content.slug.in_(V19F_CONTENT_SLUGS))
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
                select(Content).where(Content.slug.in_(V19F_CONTENT_SLUGS))
            )
        }
        assert stable_ids == (
            _orm_content(db_session, "cooking-current-system").id,
            db_session.scalar(
                select(ContentRequirement.id).where(
                    ContentRequirement.seed_key == "cooking-current-system.setup"
                )
            ),
        )
        archived_after = db_session.get(Evidence, archived_marker[0])
        assert archived_after is not None
        assert (
            archived_after.verification_status,
            archived_after.source_id,
        ) == archived_marker[1:]
        assert db_session.scalar(select(func.count()).select_from(ChecklistInstance)) == history_ids[0]
        assert db_session.get(ChecklistItemState, history_ids[1]).note == "V1.9F checklist marker"
        assert db_session.get(UserContentState, history_ids[2]).note == "V1.9F content marker"
        assert db_session.get(UserMaterialInventory, history_ids[3]).note == "V1.9F inventory marker"
        assert db_session.get(UserProjectStageState, history_ids[4]).note == "V1.9F stage marker"