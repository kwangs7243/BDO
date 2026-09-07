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
CONTENT_SLUG = "last-gladiius-weekly"
NEW_SOURCE_IDS = {
    "gladius-foundation-2025-05-28",
    "gladius-quest-flow-2025-06-04",
    "gladius-mechanics-2025-10-22",
}
GLADIUS_SOURCE_IDS = {
    *NEW_SOURCE_IDS,
    "combat-system-rework-2025-07-23",
    "gladius-2026",
    "gladius-balance-2026",
    "ator-reset-patch",
}
FIXED_NOW = datetime(2026, 9, 7, 12, tzinfo=KST)


def _seed_rows() -> tuple[list[dict], list[dict]]:
    sources = json.loads((DATA_DIR / "seed_sources.json").read_text(encoding="utf-8"))
    contents = json.loads((DATA_DIR / "seed_contents.json").read_text(encoding="utf-8"))
    return sources, contents


def _content_row() -> dict:
    return next(row for row in _seed_rows()[1] if row["slug"] == CONTENT_SLUG)


def _explicit_role_counts(contents: list[dict]) -> Counter[str]:
    return Counter(
        structured["knowledge_role"]
        for content in contents
        for requirement in content.get("requirements", [])
        if isinstance((structured := requirement.get("structured_value")), dict)
        and structured.get("knowledge_role") in {"fact", "strategy", "measurement"}
    )


def _orm_content(session: Session, slug: str = CONTENT_SLUG) -> Content:
    content = session.scalar(select(Content).where(Content.slug == slug))
    assert content is not None
    return content


def test_v19i_seed_identity_counts_and_references() -> None:
    sources, contents = _seed_rows()
    source_ids = [row["id"] for row in sources]
    source_urls = [row["url"] for row in sources]
    slugs = [row["slug"] for row in contents]

    assert len(sources) >= 168
    assert len(contents) >= 270
    assert sum(len(row.get("relations", [])) for row in contents) >= 480
    assert len(source_ids) == len(set(source_ids))
    assert len(source_urls) == len(set(source_urls))
    assert len(slugs) == len(set(slugs))
    assert GLADIUS_SOURCE_IDS <= set(source_ids)
    assert CONTENT_SLUG in slugs
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
    role_counts = _explicit_role_counts(contents)
    assert role_counts["fact"] >= 200
    assert role_counts["strategy"] >= 57
    assert role_counts["measurement"] >= 11


def test_v19i_source_chain_is_official_and_domain_neutral() -> None:
    sources, _ = _seed_rows()
    by_id = {row["id"]: row for row in sources}

    assert all(by_id[source_id]["source_type"] == "official_patch" for source_id in GLADIUS_SOURCE_IDS)
    assert by_id["gladius-foundation-2025-05-28"]["published_at"] == "2025-05-28"
    assert by_id["gladius-quest-flow-2025-06-04"]["published_at"] == "2025-06-04"
    assert by_id["combat-system-rework-2025-07-23"]["published_at"] == "2025-07-23"
    assert by_id["gladius-mechanics-2025-10-22"]["published_at"] == "2025-10-22"
    assert by_id["gladius-2026"]["published_at"] == "2026-01-28"
    assert by_id["gladius-balance-2026"]["published_at"] == "2026-06-24"
    assert by_id["combat-system-rework-2025-07-23"]["title"].startswith("7월 23일(수) 업데이트 안내")
    assert "사냥터" not in by_id["combat-system-rework-2025-07-23"]["title"]


def test_v19i_fact_scope_separates_recommendation_and_weekly() -> None:
    content = _content_row()
    requirements = {row["seed_key"].rsplit(".", 1)[-1]: row for row in content["requirements"]}
    boundary = next(row for row in content["sections"] if row["seed_key"].endswith("quest-boundary"))

    assert content["status"] == "active"
    assert content["party_type"] == "solo"
    assert len(requirements) == 5
    assert all(row["structured_value"]["knowledge_role"] == "fact" for row in requirements.values())
    assert requirements["weekly-access"]["structured_value"]["recommended_quest_required"] is False
    assert requirements["weekly-rule"]["structured_value"] == {
        "knowledge_role": "fact",
        "weekly_completion_limit": 1,
        "reset_weekday": 3,
        "reset_time_local": "00:00",
        "timezone": "Asia/Seoul",
    }
    assert "50분" in boundary["body_markdown"]
    assert "추천 의뢰 완료 없이도" in boundary["body_markdown"]
    assert all("추천 의뢰" not in step["title"] for step in content["steps"])


def test_v19i_current_stats_and_mechanics_are_official_backed() -> None:
    content = _content_row()
    requirements = {row["seed_key"].rsplit(".", 1)[-1]: row for row in content["requirements"]}
    evidence = {row["entity_seed_key"]: row for row in content["evidence"]}
    stats = requirements["recommended-stats"]["structured_value"]
    mechanics = requirements["encounter-mechanics"]["structured_value"]

    assert stats == {
        "knowledge_role": "fact",
        "recommended_display_ap": 330,
        "recommended_dp": 420,
        "party_size": 1,
        "elvia_available": False,
    }
    assert mechanics["attack_power_limit"] == 1000
    assert mechanics["above_limit_effect_percent"] == 50
    assert mechanics["black_illusion_spawn_heart_hp_percent"] == [90, 70, 50, 30]
    assert mechanics["heart_defense_reduction_seconds_after_illusion"] == 50
    assert mechanics["ancient_device_light_persists_until_battle_end"] is True
    assert mechanics["all_illusions_defeated_keeps_heart_attackable"] is True
    assert 1300 not in mechanics.values()
    assert evidence[f"{CONTENT_SLUG}.recommended-stats"]["source_ids"] == [
        "gladius-foundation-2025-05-28",
        "gladius-balance-2026",
    ]
    assert evidence[f"{CONTENT_SLUG}.encounter-mechanics"]["source_ids"] == [
        "combat-system-rework-2025-07-23",
        "gladius-mechanics-2025-10-22",
        "gladius-2026",
        "gladius-balance-2026",
    ]


def test_v19i_rewards_reset_relations_and_evidence() -> None:
    content = _content_row()
    rewards = {row["name"]: row for row in content["rewards"]}
    schedule = content["schedules"][0]

    assert len(content["rewards"]) == 10
    assert rewards["글라디우스 : 카이벨라 함"]["amount"] == 1
    assert rewards["마하의 파편"]["amount"] == 35
    assert rewards["자연의 흔적"]["amount"] == 25
    assert rewards["데보레카 액세서리"]["is_choice"] is False
    assert (schedule["rule_type"], schedule["weekday"], schedule["time_local"]) == (
        "quest_reset",
        3,
        "00:00",
    )
    assert {row["to_content_slug"] for row in content["relations"]} == {
        "atoraxxion-weekly",
        "weekly-quest-framework",
    }
    assert len(content["evidence"]) == 31
    assert all(row["verification_status"] == "verified" for row in content["evidence"])
    reset_evidence = next(row for row in content["evidence"] if row["entity_type"] == "schedule_rule")
    assert reset_evidence["source_ids"] == ["ator-reset-patch", "gladius-foundation-2025-05-28"]


def test_v19i_prompt_keeps_facts_verified_and_discovers_checklist(session: Session) -> None:
    detail = get_content_detail(session, CONTENT_SLUG, FIXED_NOW)
    expected_claims = {
        detail.summary,
        detail.purpose,
        *(row.description for row in detail.requirements),
        *(f"{row.title}: {row.description}" for row in detail.steps),
        *(f"{row.title}: {row.body_markdown}" for row in detail.sections),
    }

    for mode in (PromptMode.CONTENT_ONBOARDING, PromptMode.NEXT_ACTION, PromptMode.VERIFY_LATEST):
        bundle = build_context(
            session,
            PromptRequest(mode=mode, content_slug=CONTENT_SLUG, as_of=FIXED_NOW),
            FIXED_NOW,
        )
        facts = {item.claim: item for item in bundle.canonical_facts}
        assert expected_claims <= set(facts)
        assert all(facts[claim].knowledge_role == PromptKnowledgeRole.FACT for claim in expected_claims)
        assert not bundle.open_questions_or_conflicts
        assert any(source.id == "gladius-balance-2026" for source in bundle.sources)
        assert any(item.seed_key == f"{CONTENT_SLUG}.weekly-reward-check.claimed" for item in detail.checklists[0].items)

    weekly = build_context(
        session,
        PromptRequest(mode=PromptMode.WEEKLY_REVIEW, as_of=FIXED_NOW),
        FIXED_NOW,
    )
    assert any("글라디우스 : 카이벨라 함" in item.label for item in weekly.checklist)


def test_v19i_checklist_uses_thursday_kst_boundary(session: Session) -> None:
    content = _orm_content(session)
    before = get_current_checklists(
        session,
        "weekly",
        datetime(2026, 9, 2, 23, 59, 59, tzinfo=KST),
        content_id=content.id,
    )[0]
    at = get_current_checklists(
        session,
        "weekly",
        datetime(2026, 9, 3, 0, 0, 0, tzinfo=KST),
        content_id=content.id,
    )[0]
    after = get_current_checklists(
        session,
        "weekly",
        datetime(2026, 9, 3, 0, 0, 1, tzinfo=KST),
        content_id=content.id,
    )[0]

    assert before.period_key == "W:2026-08-27T00:00:00+09:00"
    assert at.period_key == "W:2026-09-03T00:00:00+09:00"
    assert after.period_key == at.period_key
    assert at.template_seed_key == f"{CONTENT_SLUG}.weekly-reward-check"
    assert at.items[0].seed_key == f"{CONTENT_SLUG}.weekly-reward-check.claimed"


def test_v19i_temp_db_import_is_idempotent_and_preserves_history(tmp_path, monkeypatch) -> None:
    db_path = tmp_path / "v19i-validation.db"
    database_url = f"sqlite:///{db_path.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", database_url)

    backend_dir = Path(__file__).resolve().parents[1]
    config = Config(str(backend_dir / "alembic.ini"))
    config.set_main_option("script_location", str(backend_dir / "alembic"))
    command.upgrade(config, "20260902_0001")
    command.upgrade(config, "head")

    source_rows, content_rows = _seed_rows()
    first_new_source_index = min(
        index for index, row in enumerate(source_rows) if row["id"] in NEW_SOURCE_IDS
    )
    baseline_sources = json.loads(
        json.dumps(source_rows[:first_new_source_index], ensure_ascii=False)
    )
    baseline_by_id = {row["id"]: row for row in baseline_sources}
    baseline_by_id["gladius-2026"] = {
        "id": "gladius-2026",
        "url": "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15136",
        "title": "1월 28일(수) 업데이트 안내",
        "publisher": "Pearl Abyss",
        "source_type": "official_patch",
        "notes": "최후의 글라디우스 주간 우두머리",
    }
    baseline_by_id["gladius-balance-2026"] = {
        "id": "gladius-balance-2026",
        "url": "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15783",
        "title": "6월 24일(수) 업데이트 안내",
        "publisher": "Pearl Abyss",
        "source_type": "official_patch",
        "notes": "최후의 글라디우스 권장 표기 공격력 330 언급",
    }
    baseline_by_id["combat-system-rework-2025-07-23"] = {
        "id": "combat-system-rework-2025-07-23",
        "url": "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289",
        "title": "2025년 7월 23일 전투 시스템 개편",
        "publisher": "Pearl Abyss",
        "source_type": "official_patch",
        "published_at": "2025-07-23",
        "retrieved_at": "2026-09-04T12:00:00+09:00",
        "region": "KR",
    }
    baseline_sources = list(baseline_by_id.values())
    first_new_content_index = next(
        index for index, row in enumerate(content_rows) if row["slug"] == CONTENT_SLUG
    )
    baseline_contents = content_rows[:first_new_content_index]

    baseline_dir = tmp_path / "v19h-seed"
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
        existing = _orm_content(db_session, "atoraxxion-weekly")
        stable_ids = (
            existing.id,
            {row.seed_key: row.id for row in existing.requirements},
            {row.seed_key: row.id for row in existing.steps},
            {row.seed_key: row.id for row in existing.schedules},
            {row.seed_key: row.id for row in existing.checklist_templates},
        )

        get_current_checklists(db_session, "weekly", FIXED_NOW)
        checklist_state = db_session.scalar(select(ChecklistItemState))
        material = db_session.scalar(select(Material).where(Material.key == "moon-vein-flax"))
        stage = db_session.scalar(select(ProjectStage).order_by(ProjectStage.order_no))
        assert checklist_state is not None and material is not None and stage is not None
        checklist_state.completed = True
        checklist_state.note = "V1.9I checklist marker"
        user_state = UserContentState(
            content_id=existing.id,
            state="in_progress",
            priority=1,
            note="V1.9I content marker",
            updated_at=FIXED_NOW,
        )
        inventory = UserMaterialInventory(
            material_id=material.id,
            quantity=17,
            note="V1.9I inventory marker",
            updated_at=FIXED_NOW,
        )
        stage_state = UserProjectStageState(
            stage_id=stage.id,
            completed=True,
            completed_at=FIXED_NOW,
            note="V1.9I stage marker",
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
        new_content = _orm_content(db_session)
        new_ids = (
            new_content.id,
            {row.seed_key: row.id for row in new_content.requirements},
            {row.seed_key: row.id for row in new_content.steps},
            {row.seed_key: row.id for row in new_content.rewards},
            {row.seed_key: row.id for row in new_content.schedules},
            {row.seed_key: row.id for row in new_content.checklist_templates},
            {
                item.seed_key: item.id
                for template in new_content.checklist_templates
                for item in template.items
            },
        )
        evidence_ids = {
            row.seed_key: row.id
            for row in db_session.scalars(
                select(Evidence).where(Evidence.seed_key.like(f"{CONTENT_SLUG}.claim.%"))
            )
        }

        import_seed(db_session, DATA_DIR)

        assert first_counts == tuple(
            db_session.scalar(select(func.count()).select_from(model))
            for model in canonical_models
        )
        existing_after = _orm_content(db_session, "atoraxxion-weekly")
        assert stable_ids == (
            existing_after.id,
            {row.seed_key: row.id for row in existing_after.requirements},
            {row.seed_key: row.id for row in existing_after.steps},
            {row.seed_key: row.id for row in existing_after.schedules},
            {row.seed_key: row.id for row in existing_after.checklist_templates},
        )
        new_after = _orm_content(db_session)
        assert new_ids == (
            new_after.id,
            {row.seed_key: row.id for row in new_after.requirements},
            {row.seed_key: row.id for row in new_after.steps},
            {row.seed_key: row.id for row in new_after.rewards},
            {row.seed_key: row.id for row in new_after.schedules},
            {row.seed_key: row.id for row in new_after.checklist_templates},
            {
                item.seed_key: item.id
                for template in new_after.checklist_templates
                for item in template.items
            },
        )
        assert evidence_ids == {
            row.seed_key: row.id
            for row in db_session.scalars(
                select(Evidence).where(Evidence.seed_key.like(f"{CONTENT_SLUG}.claim.%"))
            )
        }
        assert db_session.scalar(select(func.count()).select_from(ChecklistInstance)) == history_ids[0]
        assert db_session.get(ChecklistItemState, history_ids[1]).note == "V1.9I checklist marker"
        assert db_session.get(UserContentState, history_ids[2]).note == "V1.9I content marker"
        assert db_session.get(UserMaterialInventory, history_ids[3]).note == "V1.9I inventory marker"
        assert db_session.get(UserProjectStageState, history_ids[4]).note == "V1.9I stage marker"
