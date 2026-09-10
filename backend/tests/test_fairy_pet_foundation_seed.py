from __future__ import annotations

import json
import shutil
from collections import Counter
from datetime import datetime
from pathlib import Path

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import Session

from app.checklists import get_current_checklists
from app.content import get_content_detail
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
    Reward,
    ScheduleRule,
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
FIXED_NOW = datetime(2026, 9, 7, 12, tzinfo=KST)
V19J_CONTENT_SLUGS = {
    "fairy-current-system",
    "pet-current-system",
    "pet-fifth-generation",
    "fairy-pet-setup-strategy",
}
V19J_SOURCE_IDS = {
    "fairy-guide-current",
    "fairy-probability-guide-current",
    "fairy-continuous-care-update-2025-09-17",
    "fairy-continuous-care-introduction-2022-08-10",
    "fairy-appearance-skill-update-2026-08-19",
    "pet-guide-current",
    "pet-fifth-generation-guide-current",
    "fairy-beginner-strategy-2026-08-20",
    "pet-exchange-decisions-2026-06-04",
}


def _seed_rows() -> tuple[list[dict], list[dict]]:
    sources = json.loads((DATA_DIR / "seed_sources.json").read_text(encoding="utf-8"))
    contents = json.loads((DATA_DIR / "seed_contents.json").read_text(encoding="utf-8"))
    return sources, contents


def _content_row(slug: str) -> dict:
    return next(row for row in _seed_rows()[1] if row["slug"] == slug)


def _requirement_map(slug: str) -> dict[str, dict]:
    return {
        row["seed_key"].removeprefix(f"{slug}."): row
        for row in _content_row(slug)["requirements"]
    }


def _role_counts(contents: list[dict]) -> Counter[str]:
    return Counter(
        structured["knowledge_role"]
        for content in contents
        for requirement in content.get("requirements", [])
        if isinstance((structured := requirement.get("structured_value")), dict)
        and structured.get("knowledge_role") in {"fact", "strategy", "measurement"}
    )


def _orm_content(session: Session, slug: str) -> Content:
    content = session.scalar(select(Content).where(Content.slug == slug))
    assert content is not None
    return content


def test_v19j_seed_identity_counts_references_and_roles() -> None:
    sources, contents = _seed_rows()
    source_ids = [row["id"] for row in sources]
    source_urls = [row["url"] for row in sources]
    slugs = [row["slug"] for row in contents]

    assert len(sources) >= 177
    assert len(contents) >= 274
    assert sum(len(row.get("relations", [])) for row in contents) >= 490
    assert len(source_ids) == len(set(source_ids))
    assert len(source_urls) == len(set(source_urls))
    assert len(slugs) == len(set(slugs))
    assert V19J_SOURCE_IDS <= set(source_ids)
    assert V19J_CONTENT_SLUGS <= set(slugs)
    assert all(row.get("status", "active") == "active" for row in contents)

    referenced_sources = {
        source_id
        for content in contents
        for evidence in content.get("evidence", [])
        for source_id in evidence.get("source_ids", [])
    }
    relation_targets = {
        relation["to_content_slug"]
        for content in contents
        for relation in content.get("relations", [])
    }
    assert referenced_sources <= set(source_ids)
    assert relation_targets <= set(slugs)
    role_counts = _role_counts(contents)
    assert role_counts["fact"] >= 220
    assert role_counts["strategy"] >= 63
    assert role_counts["measurement"] >= 11


def test_v19j_sources_separate_official_and_community_scope() -> None:
    sources, _ = _seed_rows()
    by_id = {row["id"]: row for row in sources}

    official_ids = V19J_SOURCE_IDS - {
        "fairy-beginner-strategy-2026-08-20",
        "pet-exchange-decisions-2026-06-04",
    }
    assert all(by_id[source_id]["source_type"].startswith("official_") for source_id in official_ids)
    assert by_id["fairy-beginner-strategy-2026-08-20"]["source_type"] == "community_strategy"
    assert by_id["pet-exchange-decisions-2026-06-04"]["source_type"] == "community_strategy"
    assert by_id["fairy-continuous-care-update-2025-09-17"]["published_at"] == "2025-09-17"
    assert by_id["fairy-appearance-skill-update-2026-08-19"]["published_at"] == "2026-08-19"
    assert "채택하지 않음" in by_id["pet-exchange-decisions-2026-06-04"]["notes"]

    probability = by_id["fairy-probability-guide-current"]
    assert probability["id"] == "fairy-probability-guide-current"
    assert probability["url"] == "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=338"
    assert probability["title"] == "요정 기술 습득 / 날개 돋이 확률"
    assert "전체 확률 matrix는 seed하지 않는다" in probability["notes"]
    assert "아낌없는 손길 V 효과 문구 20개" in probability["notes"]
    assert "current 등록 가능 수 근거로 사용하지 않는다" in probability["notes"]

    serialized = json.dumps([_content_row(slug) for slug in V19J_CONTENT_SLUGS], ensure_ascii=False)
    for excluded in ("discount_rate", "current_pearl_price", "cash_cost", "event_reward", "event_fairy_box"):
        assert excluded not in serialized


def test_v19j_fairy_acquisition_grades_and_growth() -> None:
    requirements = _requirement_map("fairy-current-system")
    acquisition = requirements["acquisition"]["structured_value"]
    grades = requirements["grades"]["structured_value"]["grades"]
    growth = requirements["growth"]["structured_value"]

    assert acquisition["minimum_level"] == 53
    assert acquisition["recommended_quest"] == "[모험 지원] 요정, 신비스러운 동행"
    assert acquisition["petal_exchange"] == {
        "item": "레이라의 꽃잎",
        "amount": 2,
        "result": "봉인된 요정의 날개",
        "result_amount": 1,
    }
    assert grades == [
        {"grade": "희미한", "max_level": 10},
        {"grade": "선명한", "max_level": 20},
        {"grade": "영롱한", "max_level": 30},
        {"grade": "찬란한", "max_level": 50},
    ]
    assert growth["full_experience_table_in_scope"] is False
    assert {"오네테아 흑벌꿀주", "달콤한 벌꿀주"} <= set(growth["growth_resources"])


def test_v19j_fairy_lifecycle_current_capacity_and_appearance() -> None:
    requirements = _requirement_map("fairy-current-system")
    wing = requirements["wing-upgrade"]["structured_value"]
    rebirth = requirements["rebirth"]["structured_value"]
    skill_change = requirements["skill-change"]["structured_value"]
    skills = requirements["major-skills"]["structured_value"]
    appearance = requirements["appearance-skill-separation"]["structured_value"]

    assert wing["learned_skills_reset_on_success"] is True
    assert wing["retry_after_failure_requires_rebirth"] is True
    assert rebirth["growth_rebirth"]["resets_skills"] is True
    assert rebirth["personality_rebirth"]["changes_personality"] is True
    assert skill_change["orbs_equal_learned_skill_count"] is True
    assert skill_change["guaranteed_target_skill"] is False
    assert skills["continuous_care_capacity"] == {"I": 5, "II": 8, "III": 12, "IV": 16, "V": 25}
    assert skills["continuous_care_capacity"]["V"] != 30
    assert appearance == {
        "knowledge_role": "fact",
        "effective_at": "2026-08-19",
        "appearance_selected_separately": True,
        "skill_selected_separately": True,
        "skill_must_be_owned": True,
        "appearance_determines_skill": False,
    }
    evidence = {
        row["entity_seed_key"]: row for row in _content_row("fairy-current-system")["evidence"]
    }
    assert evidence["fairy-current-system.major-skills"]["source_ids"] == [
        "fairy-guide-current",
        "fairy-continuous-care-introduction-2022-08-10",
        "fairy-continuous-care-update-2025-09-17",
    ]
    assert (
        "fairy-probability-guide-current"
        not in evidence["fairy-current-system.major-skills"]["source_ids"]
    )
    assert "fairy-probability-guide-current" in evidence["fairy-current-system.wing-upgrade"]["source_ids"]
    assert "fairy-probability-guide-current" in evidence["fairy-current-system.skill-change"]["source_ids"]


def test_v19j_pet_current_actions_hunger_specialty_and_exchange() -> None:
    requirements = _requirement_map("pet-current-system")
    action = requirements["action-mode"]["structured_value"]
    hunger = requirements["hunger"]["structured_value"]
    specialty = requirements["specialty"]["structured_value"]
    exchange = requirements["exchange"]["structured_value"]

    assert action["modes"] == ["신중함", "보통", "기민함"]
    assert action["faster_mode_increases_hunger_use"] is True
    assert hunger["zero_hunger_stops_loot"] is True
    assert hunger["zero_hunger_disables_specialty"] is True
    assert specialty["separate_from_skills"] is True
    assert "자동 낚시 시간 감소" in specialty["non_stacking_specialties"]
    assert exchange["max_registered_pets"] == 5
    assert exchange["max_result_generation"] == 4
    assert exchange["same_exchange_type_required"] is True
    assert exchange["full_probability_matrix_in_scope"] is False


def test_v19j_fifth_generation_training_captain_and_lock() -> None:
    requirements = _requirement_map("pet-fifth-generation")
    training = requirements["training"]["structured_value"]
    lock = requirements["exchange-lock"]["structured_value"]
    captain = requirements["captain"]["structured_value"]
    effects = requirements["captain-effects"]["structured_value"]
    non_captain = requirements["non-captain"]["structured_value"]

    assert (training["from_generation"], training["to_generation"]) == (4, 5)
    assert training["recipe"] == {"성장의 시약": 10, "마력의 파편": 40, "상급 가벼운 깃털": 800}
    assert lock["exchange_after_training"] is False
    assert lock["plan_skills_before_training"] is True
    assert captain["captain_limit"] == 1
    assert effects["summoned_pet_loot_time_reduction_percent"] == 15
    assert effects["captain_unique_skill_level_increase"] == 1
    assert effects["specialty_increase"] is False
    assert non_captain["non_captain_fifth_generation_matches_generation"] == 4
    assert non_captain["all_pets_need_fifth_generation"] is False


def test_v19j_strategy_is_conditional_and_not_universal() -> None:
    content = _content_row("fairy-pet-setup-strategy")
    requirements = _requirement_map("fairy-pet-setup-strategy")

    assert all(row["structured_value"]["knowledge_role"] == "strategy" for row in requirements.values())
    assert requirements["fairy-priority"]["structured_value"]["universal_best_skill_set"] is False
    assert requirements["fairy-priority"]["structured_value"]["skill_priority_depends_on_activity"] is True
    assert requirements["fairy-stop-condition"]["structured_value"]["beginner_can_stop_early"] is True
    assert requirements["fairy-reroll-budget"]["structured_value"]["paid_reroll_required"] is False
    assert requirements["pet-purpose"]["structured_value"]["universal_best_pet"] is False
    assert requirements["pet-purpose"]["structured_value"]["universal_best_group"] is False
    assert requirements["pet-fifth-generation-plan"]["structured_value"]["all_pets_need_fifth_generation"] is False
    assert requirements["pet-fifth-generation-plan"]["structured_value"]["exchange_before_fifth_generation_when_needed"] is True
    assert content["rewards"] == []
    assert content["schedules"] == []
    assert content["checklists"] == []


def test_v19j_evidence_and_prompt_preserve_fact_strategy_roles(session: Session) -> None:
    for slug in V19J_CONTENT_SLUGS:
        detail = get_content_detail(session, slug, FIXED_NOW)
        expected = {
            detail.summary,
            detail.purpose,
            *(row.description for row in detail.requirements),
            *(f"{row.title}: {row.description}" for row in detail.steps),
            *(f"{row.title}: {row.body_markdown}" for row in detail.sections),
        }
        expected_role = (
            PromptKnowledgeRole.STRATEGY
            if slug == "fairy-pet-setup-strategy"
            else PromptKnowledgeRole.FACT
        )
        for mode in (PromptMode.CONTENT_ONBOARDING, PromptMode.NEXT_ACTION, PromptMode.VERIFY_LATEST):
            bundle = build_context(
                session,
                PromptRequest(mode=mode, content_slug=slug, as_of=FIXED_NOW),
                FIXED_NOW,
            )
            facts = {item.claim: item for item in bundle.canonical_facts}
            assert expected <= set(facts)
            assert all(facts[claim].knowledge_role == expected_role for claim in expected)
            assert not bundle.open_questions_or_conflicts

    fairy_bundle = build_context(
        session,
        PromptRequest(
            mode=PromptMode.VERIFY_LATEST,
            content_slug="fairy-current-system",
            as_of=FIXED_NOW,
        ),
        FIXED_NOW,
    )
    serialized = "\n".join(item.claim for item in fairy_bundle.canonical_facts)
    assert "V=30" not in serialized
    assert "7·10·15·20·30" not in serialized


def test_v19j_temp_db_import_is_idempotent_and_preserves_history(tmp_path, monkeypatch) -> None:
    db_path = tmp_path / "v19j-validation.db"
    database_url = f"sqlite:///{db_path.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", database_url)

    backend_dir = Path(__file__).resolve().parents[1]
    config = Config(str(backend_dir / "alembic.ini"))
    config.set_main_option("script_location", str(backend_dir / "alembic"))
    command.upgrade(config, "20260902_0001")
    command.upgrade(config, "head")

    source_rows, content_rows = _seed_rows()
    baseline_sources = [row for row in source_rows if row["id"] not in V19J_SOURCE_IDS]
    baseline_contents = [row for row in content_rows if row["slug"] not in V19J_CONTENT_SLUGS]
    baseline_dir = tmp_path / "v19i-seed"
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
        Reward,
        ContentSection,
        ScheduleRule,
        ChecklistTemplate,
        ChecklistTemplateItem,
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
        existing = _orm_content(db_session, "last-gladiius-weekly")
        stable_ids = (
            existing.id,
            {row.seed_key: row.id for row in existing.requirements},
            {row.seed_key: row.id for row in existing.steps},
            {row.seed_key: row.id for row in existing.sections},
        )

        get_current_checklists(db_session, "weekly", FIXED_NOW)
        checklist_state = db_session.scalar(select(ChecklistItemState))
        material = db_session.scalar(select(Material).where(Material.key == "moon-vein-flax"))
        stage = db_session.scalar(select(ProjectStage).order_by(ProjectStage.order_no))
        assert checklist_state is not None and material is not None and stage is not None
        checklist_state.completed = True
        checklist_state.note = "V1.9J checklist marker"
        user_state = UserContentState(
            content_id=existing.id,
            state="in_progress",
            priority=1,
            note="V1.9J content marker",
            updated_at=FIXED_NOW,
        )
        inventory = UserMaterialInventory(
            material_id=material.id,
            quantity=19,
            note="V1.9J inventory marker",
            updated_at=FIXED_NOW,
        )
        stage_state = UserProjectStageState(
            stage_id=stage.id,
            completed=True,
            completed_at=FIXED_NOW,
            note="V1.9J stage marker",
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
            slug: (
                (content := _orm_content(db_session, slug)).id,
                {row.seed_key: row.id for row in content.requirements},
                {row.seed_key: row.id for row in content.steps},
                {row.seed_key: row.id for row in content.sections},
            )
            for slug in V19J_CONTENT_SLUGS
        }
        evidence_ids = {
            row.seed_key: row.id
            for row in db_session.scalars(
                select(Evidence).where(
                    Evidence.seed_key.like("fairy-current-system.claim.%")
                    | Evidence.seed_key.like("pet-current-system.claim.%")
                    | Evidence.seed_key.like("pet-fifth-generation.claim.%")
                    | Evidence.seed_key.like("fairy-pet-setup-strategy.claim.%")
                )
            )
        }

        import_seed(db_session, DATA_DIR)

        assert first_counts == tuple(
            db_session.scalar(select(func.count()).select_from(model))
            for model in canonical_models
        )
        existing_after = _orm_content(db_session, "last-gladiius-weekly")
        assert stable_ids == (
            existing_after.id,
            {row.seed_key: row.id for row in existing_after.requirements},
            {row.seed_key: row.id for row in existing_after.steps},
            {row.seed_key: row.id for row in existing_after.sections},
        )
        assert new_ids == {
            slug: (
                (content := _orm_content(db_session, slug)).id,
                {row.seed_key: row.id for row in content.requirements},
                {row.seed_key: row.id for row in content.steps},
                {row.seed_key: row.id for row in content.sections},
            )
            for slug in V19J_CONTENT_SLUGS
        }
        assert evidence_ids == {
            row.seed_key: row.id
            for row in db_session.scalars(
                select(Evidence).where(
                    Evidence.seed_key.like("fairy-current-system.claim.%")
                    | Evidence.seed_key.like("pet-current-system.claim.%")
                    | Evidence.seed_key.like("pet-fifth-generation.claim.%")
                    | Evidence.seed_key.like("fairy-pet-setup-strategy.claim.%")
                )
            )
        }
        assert db_session.scalar(select(func.count()).select_from(ChecklistInstance)) == history_ids[0]
        assert db_session.get(ChecklistItemState, history_ids[1]).note == "V1.9J checklist marker"
        assert db_session.get(UserContentState, history_ids[2]).note == "V1.9J content marker"
        assert db_session.get(UserMaterialInventory, history_ids[3]).note == "V1.9J inventory marker"
        assert db_session.get(UserProjectStageState, history_ids[4]).note == "V1.9J stage marker"
