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
V19G_SOURCE_IDS = {
    "barter-accessibility-2026-05-20",
    "barter-scheduler-strategy-2026-06-06",
    "sailing-academy-community-2026-06-14",
}
V19G_CONTENT_SLUGS = {
    "sailing-onboarding-strategy",
    "barter-onboarding-strategy",
}
COMMUNITY_SOURCE_IDS = {
    "barter-scheduler-strategy-2026-06-06",
    "sailing-academy-community-2026-06-14",
}
FIXED_NOW = datetime(2026, 9, 7, 12, tzinfo=KST)
OLD_CROW_PRICES = {
    "deep-sea-tear": 500,
    "cox-combat": 150,
    "brilliant-rock-salt": 500,
    "deep-tide-timber": 100,
    "brilliant-pearl": 500,
    "deep-seaweed": 100,
    "cox-negotiation-upper": 500,
    "tide-timber": 100,
    "brilliant-cobalt": 500,
    "moon-vein-flax": 50,
    "khan-tendon": 500,
    "enhanced-island-plywood": 50,
    "red-undersea-nodule": 250,
    "pure-reef-fragment": 40,
    "khan-scale": 200,
    "moon-scale-plywood": 20,
    "pure-pearl": 250,
}
CURRENT_CROW_PRICES = {
    key: value
    for key, value in (
        ("deep-sea-tear", 400),
        ("cox-combat", 120),
        ("brilliant-rock-salt", 400),
        ("deep-tide-timber", 80),
        ("brilliant-pearl", 400),
        ("deep-seaweed", 80),
        ("cox-negotiation-upper", 400),
        ("tide-timber", 80),
        ("brilliant-cobalt", 400),
        ("moon-vein-flax", 40),
        ("khan-tendon", 400),
        ("enhanced-island-plywood", 40),
        ("red-undersea-nodule", 200),
        ("pure-reef-fragment", 30),
        ("khan-scale", 160),
        ("moon-scale-plywood", 15),
        ("pure-pearl", 200),
    )
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


def test_v19g_seed_identity_sources_roles_and_references() -> None:
    sources, contents = _seed_rows()
    source_ids = [row["id"] for row in sources]
    source_urls = [row["url"] for row in sources]
    content_slugs = [row["slug"] for row in contents]

    assert len(sources) >= 164
    assert len(contents) >= 268
    assert sum(len(row.get("relations", [])) for row in contents) >= 468
    assert len(source_ids) == len(set(source_ids))
    assert len(source_urls) == len(set(source_urls))
    assert len(content_slugs) == len(set(content_slugs))
    assert V19G_SOURCE_IDS <= set(source_ids)
    assert V19G_CONTENT_SLUGS <= set(content_slugs)
    assert all(
        next(row for row in sources if row["id"] == source_id)["source_type"]
        == "community_strategy"
        for source_id in COMMUNITY_SOURCE_IDS
    )
    assert (
        next(
            row
            for row in sources
            if row["id"] == "barter-accessibility-2026-05-20"
        )["source_type"]
        == "official_patch"
    )

    referenced = {
        source_id
        for content in contents
        for evidence in content.get("evidence", [])
        for source_id in evidence.get("source_ids", [])
    }
    assert referenced <= set(source_ids)
    roles = _explicit_role_counts(contents)
    assert roles["fact"] >= 194
    assert roles["strategy"] >= 51
    assert roles["measurement"] >= 11
    assert sum(
        1
        for content in contents
        if content["slug"] in V19G_CONTENT_SLUGS
        for requirement in content.get("requirements", [])
        if requirement.get("structured_value", {}).get("knowledge_role") == "strategy"
    ) == 10


def test_v19g_current_fact_audit_and_route_responsibility() -> None:
    current = _content_row("barter-current-system")
    stages = _content_row("barter-stage-values")
    route = _content_row("barter-route-strategy")
    crow = _content_row("crow-coin-material-shop")

    assert {
        row["seed_key"] for row in current["requirements"]
    } == {
        "barter-current-system.low-tier-output",
        "barter-current-system.parley.crow-coin",
        "barter-current-system.parley.ocean-rares",
        "barter-current-system.transport-disabled",
    }
    assert len(stages["requirements"]) == 8
    assert route["subcategory"] == "community_strategy"
    assert route["requirements"] == []
    assert route["steps"] == []
    assert len(route["sections"]) == 1
    assert route["sections"][0]["seed_key"].endswith("distance-2026-05-31")

    prices = {
        row["seed_key"].removeprefix("crow-coin-material-shop.price."): row["amount"]
        for row in crow["rewards"]
    }
    assert prices == CURRENT_CROW_PRICES
    assert crow["last_verified_at"] == "2026-09-07"
    assert all(
        evidence["source_ids"] == ["barter-accessibility-2026-05-20"]
        for evidence in crow["evidence"]
    )


def test_v19g_seed_keys_claim_coverage_and_static_scope() -> None:
    for slug in V19G_CONTENT_SLUGS:
        content = _content_row(slug)
        assert content["status"] == "active"
        assert content["last_verified_at"] == "2026-09-07"
        assert 4 <= len(content["requirements"]) <= 6
        assert 8 <= len(content["steps"]) <= 11
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
            "crow coin/hour",
            "현재 최적 섬",
            "현재 best route",
            "scheduler score",
            "ocr",
            "외부 executable",
        ):
            assert forbidden not in serialized


def test_sailing_onboarding_semantics_and_relations(session: Session) -> None:
    content = _orm_content(session, "sailing-onboarding-strategy")
    requirements = {row.seed_key.rsplit(".", 1)[-1]: row for row in content.requirements}
    purpose = requirements["purpose-choice"]
    readiness = requirements["departure-readiness"]
    carrack = requirements["carrack-choice"]
    sailor = requirements["sailor-investment"]
    first = requirements["first-voyage-scope"]

    assert purpose.structured_value["single_default_goal"] is False
    assert {
        "barter_logistics",
        "carrack_progression",
        "ocean_hunting",
        "oquilla_routines",
        "panokseon_or_advanced_ship",
        "ocean_exploration",
    } == set(purpose.structured_value["goals"])
    assert {
        "ship_food",
        "cannon_ammo",
        "ship_durability",
        "sailor_health",
        "crew_slots",
        "cargo_weight",
        "inventory_plan",
        "repair_or_supply_need",
        "return_port",
    } == set(readiness.structured_value["dimensions"])
    assert carrack.structured_value["universal_best_carrack"] is False
    assert sailor.structured_value["universal_best_crew"] is False
    assert first.structured_value["first_session"] == "one_short_goal"
    assert len(content.steps) == 9
    assert any(row.seed_key.endswith("return-and-organize") for row in content.steps)
    assert {
        "carrack-types",
        "sailor-hiring-growth",
        "sailor-role-slots",
        "sailor-health-food",
        "ocean-consumables",
        "carrack-upgrade-materials",
        "sea-crystals",
        "carrack-advance",
    } <= _relation_targets(content)


def test_barter_onboarding_semantics_and_relations(session: Session) -> None:
    content = _orm_content(session, "barter-onboarding-strategy")
    requirements = {row.seed_key.rsplit(".", 1)[-1]: row for row in content.requirements}
    purpose = requirements["purpose-choice"]
    route = requirements["current-list-decision"]
    stock = requirements["stage-stock"]
    cargo = requirements["cargo-storage"]
    higher = requirements["higher-tier-transition"]

    assert purpose.structured_value["single_default_goal"] is False
    assert {
        "silver_sale",
        "crow_coin",
        "carrack_material",
        "stockpile_for_future_routes",
        "daily_or_weekly_objective",
        "general_progression",
    } == set(purpose.structured_value["goals"])
    assert route.structured_value["dynamic_route_excluded"] is True
    assert route.structured_value["universal_best_route"] is False
    assert route.structured_value["runtime_optimizer"] is False
    assert {"current_list", "cargo_weight", "owned_trade_goods", "return_storage"} <= set(
        route.structured_value["dimensions"]
    )
    assert stock.structured_value["fixed_stock_targets"] is None
    assert {
        "departure_stock",
        "intermediate_stock",
        "return_cargo",
        "overflow",
        "next_cycle_reserve",
    } == set(cargo.structured_value["inventory_buckets"])
    assert higher.structured_value["beginner_default"] is False
    assert len(content.steps) == 11
    assert {
        "barter-current-system",
        "barter-stage-values",
        "barter-route-strategy",
        "barter-tier6-routes",
        "barter-tier7-routes",
        "crow-coin-material-shop",
        "carrack-advance",
        "storage-current-system",
    } <= _relation_targets(content)


def test_v19g_evidence_keeps_official_and_community_roles_separate(
    session: Session,
) -> None:
    for slug in V19G_CONTENT_SLUGS:
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
        assert "community_strategy" in source_types
        assert source_types & {"official_guide", "official_patch"}
        assert all(row.active and row.verification_status == "verified" for row in evidence)


def test_life_api_discovers_v19g_without_promoting_advanced_route(
    session: Session,
) -> None:
    client = _client(session)
    try:
        sailing = client.get("/api/life/sailing")
        barter = client.get("/api/life/barter")
        assert sailing.status_code == barter.status_code == 200
        sailing_payload = sailing.json()
        barter_payload = barter.json()
        assert [row["slug"] for row in sailing_payload["getting_started"]][:3] == [
            "carrack-types",
            "sailing-onboarding-strategy",
            "sailor-hiring-growth",
        ]
        assert [row["slug"] for row in barter_payload["getting_started"]][:2] == [
            "barter-current-system",
            "barter-onboarding-strategy",
        ]
        assert "barter-route-strategy" in {
            row["slug"] for row in barter_payload["advanced_contents"]
        }
        assert "barter-route-strategy" not in {
            row["slug"] for row in barter_payload["getting_started"]
        }
    finally:
        app.dependency_overrides.clear()
        client.close()


def test_v19g_prompt_emits_strategy_role_for_supported_claims(
    session: Session,
) -> None:
    for slug in V19G_CONTENT_SLUGS:
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


def test_v19g_temp_db_import_is_idempotent_and_preserves_history(
    tmp_path, monkeypatch
) -> None:
    db_path = tmp_path / "v19g-validation.db"
    database_url = f"sqlite:///{db_path.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", database_url)

    backend_dir = Path(__file__).resolve().parents[1]
    config = Config(str(backend_dir / "alembic.ini"))
    config.set_main_option("script_location", str(backend_dir / "alembic"))
    command.upgrade(config, "20260902_0001")
    command.upgrade(config, "head")

    source_rows, current_contents = _seed_rows()
    baseline_contents = json.loads(json.dumps(current_contents, ensure_ascii=False))
    baseline_contents = [
        row for row in baseline_contents if row["slug"] not in V19G_CONTENT_SLUGS
    ]
    crow = next(
        row for row in baseline_contents if row["slug"] == "crow-coin-material-shop"
    )
    crow["summary"] = (
        "2024-03-27 공식 패치 기준 까마귀 주화 상점의 현행 증축 재료 구매 가격."
    )
    crow["purpose"] = "구식 가이드 가격 대신 최신 공식 조정 가격으로 증축 비용을 계산한다."
    crow["last_verified_at"] = "2026-09-03"
    for reward in crow["rewards"]:
        key = reward["seed_key"].removeprefix("crow-coin-material-shop.price.")
        reward["amount"] = OLD_CROW_PRICES[key]
        reward["notes"] = "현행 구매 가격"
    crow["sections"][0]["body_markdown"] = (
        "중범선 만들기 가이드에 남아 있는 일부 40·80·400 주화 표기는 현행 가격 "
        "근거로 사용하지 않는다. 이 콘텐츠는 2024-03-27 공식 가격 조정을 정본으로 사용한다."
    )
    for evidence in crow["evidence"]:
        evidence["source_ids"] = ["ocean-barter-rework-2024-03-27"]
        evidence["last_verified_at"] = "2026-09-03"
        evidence["note"] = (
            "현행 구매 가격"
            if evidence["entity_type"] == "reward"
            else crow["sections"][0]["body_markdown"]
        )

    baseline_references = {
        source_id
        for content in baseline_contents
        for evidence in content.get("evidence", [])
        for source_id in evidence.get("source_ids", [])
    }
    baseline_sources = [
        row
        for row in source_rows
        if row["id"] not in V19G_SOURCE_IDS or row["id"] in baseline_references
    ]
    baseline_dir = tmp_path / "v19f-seed"
    baseline_dir.mkdir()
    (baseline_dir / "seed_sources.json").write_text(
        json.dumps(baseline_sources, ensure_ascii=False), encoding="utf-8"
    )
    (baseline_dir / "seed_contents.json").write_text(
        json.dumps(baseline_contents, ensure_ascii=False), encoding="utf-8"
    )
    shutil.copy(DATA_DIR / "seed_projects.json", baseline_dir / "seed_projects.json")
    shutil.copy(DATA_DIR / "seed_materials.json", baseline_dir / "seed_materials.json")

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
        existing = _orm_content(db_session, "crow-coin-material-shop")
        existing_reward = existing.rewards[0]
        existing_evidence = db_session.scalar(
            select(Evidence).where(
                Evidence.seed_key == "crow-coin-material-shop.evidence.price-deep-sea-tear::ocean-barter-rework-2024-03-27"
            )
        )
        archived_evidence = db_session.scalar(
            select(Evidence).where(Evidence.active.is_(False)).order_by(Evidence.id)
        )
        assert existing_evidence is not None and archived_evidence is not None
        stable_ids = (existing.id, existing_reward.id)
        archived_marker = (
            archived_evidence.id,
            archived_evidence.verification_status,
            archived_evidence.source_id,
        )

        get_current_checklists(db_session, "weekly", FIXED_NOW)
        checklist_state = db_session.scalar(select(ChecklistItemState))
        material = db_session.scalar(
            select(Material).where(Material.key == "moon-vein-flax")
        )
        stage = db_session.scalar(select(ProjectStage).order_by(ProjectStage.order_no))
        assert checklist_state is not None and material is not None and stage is not None
        checklist_state.completed = True
        checklist_state.note = "V1.9G checklist marker"
        user_state = UserContentState(
            content_id=existing.id,
            state="in_progress",
            priority=1,
            note="V1.9G content marker",
            updated_at=FIXED_NOW,
        )
        inventory = UserMaterialInventory(
            material_id=material.id,
            quantity=19,
            note="V1.9G inventory marker",
            updated_at=FIXED_NOW,
        )
        stage_state = UserProjectStageState(
            stage_id=stage.id,
            completed=True,
            completed_at=FIXED_NOW,
            note="V1.9G stage marker",
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
                select(Content).where(Content.slug.in_(V19G_CONTENT_SLUGS))
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
                select(Content).where(Content.slug.in_(V19G_CONTENT_SLUGS))
            )
        }
        crow_after = _orm_content(db_session, "crow-coin-material-shop")
        evidence_after = db_session.scalar(
            select(Evidence).where(
                Evidence.seed_key
                == "crow-coin-material-shop.evidence.price-deep-sea-tear::barter-accessibility-2026-05-20"
            )
        )
        old_price_evidence = db_session.get(Evidence, existing_evidence.id)
        assert evidence_after is not None and old_price_evidence is not None
        assert stable_ids == (
            crow_after.id,
            crow_after.rewards[0].id,
        )
        assert crow_after.rewards[0].amount == 400
        assert evidence_after.source.id == "barter-accessibility-2026-05-20"
        assert old_price_evidence.active is False
        assert (
            old_price_evidence.source.id
            == "ocean-barter-rework-2024-03-27"
        )

        archived_after = db_session.get(Evidence, archived_marker[0])
        assert archived_after is not None
        assert (
            archived_after.verification_status,
            archived_after.source_id,
        ) == archived_marker[1:]
        assert (
            db_session.scalar(select(func.count()).select_from(ChecklistInstance))
            == history_ids[0]
        )
        assert db_session.get(ChecklistItemState, history_ids[1]).note == "V1.9G checklist marker"
        assert db_session.get(UserContentState, history_ids[2]).note == "V1.9G content marker"
        assert db_session.get(UserMaterialInventory, history_ids[3]).note == "V1.9G inventory marker"
        assert db_session.get(UserProjectStageState, history_ids[4]).note == "V1.9G stage marker"
