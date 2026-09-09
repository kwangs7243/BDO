from __future__ import annotations

import copy
import json
import shutil
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import Session

from app.checklists import get_current_checklists
from app.models import (
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
from app.prompt_bridge import build_context, render_markdown
from app.schemas import PromptMode, PromptRequest
from app.seed import import_seed


DATA = Path(__file__).resolve().parents[2] / "data"
FIXED_NOW = datetime(2026, 9, 9, 17, 0, tzinfo=KST)
NEW_SOURCE_ID = "blood-altar-high-tier-2026-09-09"
NEW_REQUIREMENT_KEY = "blood-altar.high-tier-current"
NEW_REWARD_KEYS = {
    f"blood-altar.reward.stage-{stage}-{kind}"
    for stage in (22, 23, 24)
    for kind in ("weekly", "first-clear")
}


def seed_rows() -> tuple[list[dict], list[dict]]:
    return (
        json.loads((DATA / "seed_sources.json").read_text(encoding="utf-8")),
        json.loads((DATA / "seed_contents.json").read_text(encoding="utf-8")),
    )


def blood_row(contents: list[dict]) -> dict:
    return next(row for row in contents if row["slug"] == "blood-altar")


def requirement(session: Session, seed_key: str) -> ContentRequirement:
    row = session.scalar(
        select(ContentRequirement).where(ContentRequirement.seed_key == seed_key)
    )
    assert row is not None
    return row


def test_v19m_exact_baseline_and_reference_integrity() -> None:
    sources, contents = seed_rows()
    source_ids = {row["id"] for row in sources}
    slugs = {row["slug"] for row in contents}
    roles = Counter(
        requirement["structured_value"].get("knowledge_role")
        for content in contents
        for requirement in content.get("requirements", [])
        if isinstance(requirement.get("structured_value"), dict)
    )

    assert (len(sources), len(contents)) == (183, 294)
    assert sum(len(row.get("relations", [])) for row in contents) == 521
    assert {key: roles[key] for key in ("fact", "strategy", "measurement")} == {
        "fact": 280,
        "strategy": 63,
        "measurement": 11,
    }
    assert len(source_ids) == len(sources)
    assert len({row["url"] for row in sources}) == len(sources)
    assert len(slugs) == len(contents)
    assert all(row.get("status", "active") == "active" for row in contents)
    assert {
        source_id
        for content in contents
        for evidence in content.get("evidence", [])
        for source_id in evidence["source_ids"]
    } <= source_ids
    assert {
        relation["to_content_slug"]
        for content in contents
        for relation in content.get("relations", [])
    } <= slugs


def test_sources_preserve_guide_identity_and_mark_stale_boundaries(session: Session) -> None:
    guide = session.get(Source, "blood-altar-guide")
    patch = session.get(Source, NEW_SOURCE_ID)
    assert guide is not None and patch is not None
    assert guide.url == "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168"
    assert guide.title == "피의 제단"
    assert patch.url.endswith("groupContentNo=16163")
    assert patch.title == "9월 9일(수) 업데이트 안내"

    sources, _ = seed_rows()
    guide_seed = next(row for row in sources if row["id"] == "blood-altar-guide")
    notes = guide_seed["notes"]
    assert all(value in notes for value in ("21단계", "5회", "심연의 환상", "current 근거로 사용하지 않는다"))


def test_current_structure_stats_and_removed_difficulties(session: Session) -> None:
    content = session.scalar(select(Content).where(Content.slug == "blood-altar"))
    assert content is not None and content.status == "active"
    assert content.last_verified_at.isoformat() == "2026-09-09"
    assert "24단계" in content.summary
    assert "주간 입장 제한은 없고" in content.summary
    assert "도전 10회" in content.summary
    assert "최초 클리어 보상" in content.summary
    assert "current 난이도에 포함하지 않는다" in content.summary

    stages = requirement(session, "blood-altar.stages").structured_value
    assert stages == {"stage_count": 24, "highest_clear_persists": True}

    current = requirement(session, NEW_REQUIREMENT_KEY).structured_value
    assert current["knowledge_role"] == "fact"
    assert current["current_stage_cap"] == 24
    assert current["future_high_tiers_possible"] is True
    assert current["removed_effective_date"] == "2026-09-09"
    assert current["removed_difficulties"] == [
        {"key": "abyss_illusion_1", "name": "심연의 환상 1", "current": False},
        {"key": "abyss_illusion_2", "name": "심연의 환상 2", "current": False},
        {"key": "abyss_illusion_3", "name": "심연의 환상 3", "current": False},
    ]
    assert {
        stage: (
            values["recommended_ap"],
            values["recommended_dp"],
            values["recommended_final_ap"],
            values["recommended_final_dp"],
        )
        for stage, values in current["stages"].items()
    } == {
        "22": (405, 465, 2110, 810),
        "23": (410, 470, 2200, 815),
        "24": (415, 475, 2290, 820),
    }


def test_high_tier_reward_table_is_exact_without_invented_probabilities(
    session: Session,
) -> None:
    stages = requirement(session, NEW_REQUIREMENT_KEY).structured_value["stages"]
    expected_ranges = {
        "22": {
            "gold": (4, 5),
            "traces": (25, 30),
            "crystals": (60, 65),
            "black_stones": (125, 130),
        },
        "23": {
            "gold": (5, 5),
            "traces": (26, 31),
            "crystals": (65, 70),
            "black_stones": (130, 135),
        },
        "24": {
            "gold": (5, 6),
            "traces": (27, 32),
            "crystals": (70, 75),
            "black_stones": (135, 140),
        },
    }
    for stage, values in stages.items():
        weekly = values["weekly_reward"]
        chance = {row["name"]: row for row in weekly["chance_based"]}
        guaranteed = {row["name"]: row for row in weekly["quantity_guaranteed"]}
        first = {row["name"]: row for row in values["first_clear_reward"]["guaranteed"]}

        assert chance["금괴 상자"]["amount"] == 14
        assert chance["금괴 상자"]["contents"] == {
            "name": "금괴 1kG",
            "min_amount": 3,
            "max_amount": 10,
            "unit": "개",
        }
        assert {
            name: chance[name]["amount"]
            for name in (
                "발크스의 조언 (+300)",
                "발크스의 조언 (+250)",
                "발크스의 조언 (+200)",
                "영롱한 포식의 기원",
                "영롱한 포식의 정수",
            )
        } == {
            "발크스의 조언 (+300)": 1,
            "발크스의 조언 (+250)": 1,
            "발크스의 조언 (+200)": 1,
            "영롱한 포식의 기원": 4,
            "영롱한 포식의 정수": 9,
        }

        expected = expected_ranges[stage]
        gold = guaranteed["금괴 상자"]
        actual_gold = (
            gold.get("min_amount", gold.get("amount")),
            gold.get("max_amount", gold.get("amount")),
        )
        assert actual_gold == expected["gold"]
        assert (
            guaranteed["자연의 흔적"]["min_amount"],
            guaranteed["자연의 흔적"]["max_amount"],
        ) == expected["traces"]
        assert (
            guaranteed["봉인된 검은 마력의 수정"]["min_amount"],
            guaranteed["봉인된 검은 마력의 수정"]["max_amount"],
        ) == expected["crystals"]
        assert (
            guaranteed["블랙스톤"]["min_amount"],
            guaranteed["블랙스톤"]["max_amount"],
        ) == expected["black_stones"]
        assert guaranteed["영롱한 포식의 기원"]["amount"] == 1
        assert guaranteed["발크스의 조언 (+100)"]["amount"] == 1

        assert first["금괴 상자"]["amount"] == 3
        assert first["영롱한 포식의 기원"]["amount"] == 2
        assert first["발크스의 조언 (+200)"]["amount"] == 1
        assert first[f"피의 제단 : 제{stage}의 환상"]["unit"] == "지식"

    serialized = json.dumps(stages, ensure_ascii=False).lower()
    assert "probability" not in serialized
    assert "percent" not in serialized

    rewards = {
        row.seed_key: row
        for row in session.scalars(
            select(Reward).where(Reward.seed_key.in_(NEW_REWARD_KEYS))
        )
    }
    assert set(rewards) == NEW_REWARD_KEYS
    assert all(row.amount == 1 and row.unit == "묶음" for row in rewards.values())


def test_attempt_schedule_and_claim_level_evidence_remain_distinct(
    session: Session,
) -> None:
    allowance = requirement(session, "blood-altar.challenge-allowance").structured_value
    entry = requirement(session, "blood-altar.entry-limit").structured_value
    weekly = requirement(session, "blood-altar.weekly-reward-rule").structured_value
    assert allowance == {
        "party_challenge_allowance": 10,
        "can_rematch_after_exhaustion": True,
    }
    assert entry == {"weekly_entry_limit": None, "entry_recurrence": "unlimited"}
    assert weekly == {
        "family_weekly_reward_limit": 1,
        "basis": "highest_stage",
        "cumulative": False,
    }

    schedule = session.scalar(
        select(ScheduleRule).where(ScheduleRule.seed_key == "blood-altar.reward-payout")
    )
    assert schedule is not None
    assert schedule.rule_type == "reward_payout"
    assert schedule.recurrence_type == "weekly"
    assert schedule.weekday == 6
    assert schedule.time_local.isoformat() == "00:00:00"
    assert schedule.timezone == "Asia/Seoul"
    assert not list(
        session.scalars(
            select(ScheduleRule).where(
                ScheduleRule.content_id == schedule.content_id,
                ScheduleRule.rule_type.in_(("quest_reset", "attempt_reset")),
                ScheduleRule.active.is_(True),
            )
        )
    )

    current_evidence = list(
        session.scalars(
            select(Evidence).where(
                Evidence.entity_id == NEW_REQUIREMENT_KEY,
                Evidence.active.is_(True),
            )
        )
    )
    assert {(row.source_id, row.claim_key) for row in current_evidence} == {
        (NEW_SOURCE_ID, "description"),
        (NEW_SOURCE_ID, "structured_value"),
    }
    attempt_evidence = list(
        session.scalars(
            select(Evidence).where(
                Evidence.entity_id == "blood-altar.challenge-allowance",
                Evidence.active.is_(True),
            )
        )
    )
    assert {(row.source_id, row.claim_key) for row in attempt_evidence} == {
        ("blood-altar-challenge-2026-07-15", "structured_value")
    }
    stage_evidence = list(
        session.scalars(
            select(Evidence).where(
                Evidence.entity_id == "blood-altar.stages",
                Evidence.active.is_(True),
            )
        )
    )
    assert {
        (row.source_id, row.claim_key) for row in stage_evidence
    } == {
        ("blood-altar-guide", "highest_clear_persists"),
        (NEW_SOURCE_ID, "structured_value"),
    }
    assert all(row.verification_status == "verified" for row in current_evidence + attempt_evidence + stage_evidence)


def test_prompt_bridge_exposes_current_fact_without_reclassifying_removed_modes(
    session: Session,
) -> None:
    for mode in (PromptMode.CONTENT_ONBOARDING, PromptMode.VERIFY_LATEST):
        request = PromptRequest(mode=mode, content_slug="blood-altar", as_of=FIXED_NOW)
        bundle = build_context(session, request, FIXED_NOW)
        assert bundle == build_context(session, request, FIXED_NOW)
        current_claims = [
            fact.claim
            for fact in bundle.canonical_facts
            if fact.claim.startswith("2026-09-09 기준 22단계")
        ]
        assert len(current_claims) == 1
        current_claim = current_claims[0]
        assert all(
            value in current_claim
            for value in (
                "22단계 권장 405/465·최종 2110/810",
                "23단계 권장 410/470·최종 2200/815",
                "24단계 권장 415/475·최종 2290/820",
                "심연의 환상 1~3은 같은 날 삭제",
            )
        )
        assert "21단계" not in current_claim
        assert any("최대 10회" in row for row in bundle.requirements)
        markdown = render_markdown(bundle)
        assert "## VERIFIED_KNOWLEDGE" in markdown
        assert "2026-09-09 기준 22단계" in markdown


def _v19l_baseline_rows() -> tuple[list[dict], list[dict]]:
    sources, contents = seed_rows()
    baseline_sources = [
        copy.deepcopy(row) for row in sources if row["id"] != NEW_SOURCE_ID
    ]
    guide = next(row for row in baseline_sources if row["id"] == "blood-altar-guide")
    guide["notes"] = "주간 최고 기록 기반, 일요일 00시 보상"
    guide.pop("retrieved_at", None)
    guide.pop("region", None)

    baseline_contents = copy.deepcopy(contents)
    blood = blood_row(baseline_contents)
    blood["summary"] = (
        "Lv.56 이상 3인이 도전하는 21단계 콘텐츠. 주간 입장 제한은 없고, "
        "파티당 도전 10회와 일요일 주간 보상 정산을 분리해 관리한다."
    )
    blood["last_verified_at"] = "2026-09-03"
    stage_row = next(
        row for row in blood["requirements"] if row["seed_key"] == "blood-altar.stages"
    )
    stage_row["description"] = "총 21단계이며 최고 클리어 기록은 초기화되지 않는다."
    stage_row["structured_value"]["stage_count"] = 21
    blood["requirements"] = [
        row for row in blood["requirements"] if row["seed_key"] != NEW_REQUIREMENT_KEY
    ]
    blood["rewards"] = [
        row for row in blood["rewards"] if row["seed_key"] not in NEW_REWARD_KEYS
    ]

    restored: list[dict] = []
    restored_keys: set[str] = set()
    for evidence in blood["evidence"]:
        if NEW_SOURCE_ID in evidence["source_ids"]:
            continue
        seed_key = evidence["seed_key"]
        if seed_key == "blood-altar.summary":
            if seed_key in restored_keys:
                continue
            evidence.update(
                claim_key="summary",
                source_ids=[
                    "blood-altar-guide",
                    "blood-altar-challenge-2026-07-15",
                ],
                last_verified_at="2026-09-03",
                note="21단계·3인·무제한 주간 입장과 최신 파티 도전 10회",
            )
        elif seed_key == "blood-altar.requirement.stages":
            if seed_key in restored_keys:
                continue
            evidence.update(
                claim_key="structured_value",
                source_ids=["blood-altar-guide"],
                last_verified_at="2026-09-03",
                note="21단계 및 최고 기록 유지",
            )
        elif seed_key == "blood-altar.section.entry-and-challenge":
            if seed_key in restored_keys:
                continue
            evidence.update(
                claim_key="body",
                source_ids=[
                    "blood-altar-guide",
                    "blood-altar-challenge-2026-07-15",
                ],
                last_verified_at="2026-09-03",
                note="입장과 도전 횟수 분리",
            )
        elif seed_key == "blood-altar.section.payout-warning":
            if seed_key in restored_keys:
                continue
            evidence.update(
                claim_key="body",
                source_ids=["blood-altar-guide"],
                last_verified_at="2026-09-03",
                note="보상 산정과 입장 제한 분리",
            )
        restored.append(evidence)
        restored_keys.add(seed_key)
    blood["evidence"] = restored
    return baseline_sources, baseline_contents


def test_v19l_to_v19m_import_is_idempotent_and_preserves_history(
    tmp_path: Path, monkeypatch
) -> None:
    db_path = tmp_path / "v19m-validation.db"
    database_url = f"sqlite:///{db_path.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", database_url)
    backend_dir = Path(__file__).resolve().parents[1]
    config = Config(str(backend_dir / "alembic.ini"))
    config.set_main_option("script_location", str(backend_dir / "alembic"))
    command.upgrade(config, "20260902_0001")
    command.upgrade(config, "head")

    baseline_sources, baseline_contents = _v19l_baseline_rows()
    assert (len(baseline_sources), len(baseline_contents)) == (182, 294)
    baseline_dir = tmp_path / "v19l-seed"
    baseline_dir.mkdir()
    (baseline_dir / "seed_sources.json").write_text(
        json.dumps(baseline_sources, ensure_ascii=False), encoding="utf-8"
    )
    (baseline_dir / "seed_contents.json").write_text(
        json.dumps(baseline_contents, ensure_ascii=False), encoding="utf-8"
    )
    shutil.copy(DATA / "seed_projects.json", baseline_dir / "seed_projects.json")

    nested_models = (
        ScheduleRule,
        ContentRequirement,
        ContentStep,
        Reward,
        ContentSection,
        ChecklistTemplate,
        ChecklistTemplateItem,
        ContentRelation,
        Evidence,
    )
    canonical_models = (
        Source,
        Content,
        *nested_models,
        Project,
        ProjectStage,
        ProjectStageDependency,
        ProjectMaterial,
        ProjectMaterialSource,
        Material,
    )
    engine = create_engine(database_url)
    with Session(engine, expire_on_commit=False) as session:
        import_seed(session, baseline_dir)
        baseline_content_ids = {
            row.slug: row.id for row in session.scalars(select(Content))
        }
        blood_content = session.scalar(
            select(Content).where(Content.slug == "blood-altar")
        )
        assert blood_content is not None
        baseline_blood_nested = {
            model.__name__: {
                row.seed_key: (row.id, row.active)
                for row in session.scalars(select(model))
                if (getattr(row, "seed_key", "") or "").startswith("blood-altar.")
            }
            for model in nested_models
        }

        get_current_checklists(session, "weekly", FIXED_NOW)
        checklist_state = session.scalar(
            select(ChecklistItemState)
            .join(ChecklistTemplateItem)
            .where(
                ChecklistTemplateItem.seed_key
                == "blood-altar.weekly-record-check.status"
            )
        )
        material = session.scalar(select(Material))
        project_stage = session.scalar(select(ProjectStage))
        assert checklist_state is not None and material is not None and project_stage is not None
        checklist_state.completed = True
        checklist_state.note = "V1.9L checklist history"
        user_content = UserContentState(
            content_id=blood_content.id,
            state="in_progress",
            priority=1,
            note="V1.9L Blood Altar history",
            updated_at=datetime(2026, 9, 9, 8, tzinfo=timezone.utc),
        )
        inventory = UserMaterialInventory(
            material_id=material.id,
            quantity=7,
            note="V1.9L inventory history",
            updated_at=datetime(2026, 9, 9, 8, tzinfo=timezone.utc),
        )
        stage_state = UserProjectStageState(
            stage_id=project_stage.id,
            completed=True,
            completed_at=datetime(2026, 9, 9, 8, tzinfo=timezone.utc),
            note="V1.9L project history",
            updated_at=datetime(2026, 9, 9, 8, tzinfo=timezone.utc),
        )
        session.add_all((user_content, inventory, stage_state))
        session.commit()
        user_ids = (
            checklist_state.id,
            user_content.id,
            inventory.id,
            stage_state.id,
        )

        import_seed(session, DATA)
        first_counts = tuple(
            session.scalar(select(func.count()).select_from(model))
            for model in canonical_models
        )
        new_nested_ids = {
            ContentRequirement.__name__: {
                row.seed_key: row.id
                for row in session.scalars(
                    select(ContentRequirement).where(
                        ContentRequirement.seed_key == NEW_REQUIREMENT_KEY
                    )
                )
            },
            Reward.__name__: {
                row.seed_key: row.id
                for row in session.scalars(
                    select(Reward).where(Reward.seed_key.in_(NEW_REWARD_KEYS))
                )
            },
            Evidence.__name__: {
                row.seed_key: row.id
                for row in session.scalars(
                    select(Evidence).where(Evidence.source_id == NEW_SOURCE_ID)
                )
            },
        }
        assert all(new_nested_ids.values())

        for _ in range(2):
            import_seed(session, DATA)
            assert first_counts == tuple(
                session.scalar(select(func.count()).select_from(model))
                for model in canonical_models
            )

        assert baseline_content_ids == {
            row.slug: row.id
            for row in session.scalars(
                select(Content).where(Content.slug.in_(baseline_content_ids))
            )
        }
        for model in nested_models:
            current = {
                row.seed_key: (row.id, row.active)
                for row in session.scalars(select(model))
                if getattr(row, "seed_key", None)
                in baseline_blood_nested[model.__name__]
            }
            assert current == baseline_blood_nested[model.__name__]
        assert new_nested_ids[ContentRequirement.__name__] == {
            row.seed_key: row.id
            for row in session.scalars(
                select(ContentRequirement).where(
                    ContentRequirement.seed_key == NEW_REQUIREMENT_KEY
                )
            )
        }
        assert new_nested_ids[Reward.__name__] == {
            row.seed_key: row.id
            for row in session.scalars(
                select(Reward).where(Reward.seed_key.in_(NEW_REWARD_KEYS))
            )
        }
        assert new_nested_ids[Evidence.__name__] == {
            row.seed_key: row.id
            for row in session.scalars(
                select(Evidence).where(Evidence.source_id == NEW_SOURCE_ID)
            )
        }
        assert session.get(ChecklistItemState, user_ids[0]).note == "V1.9L checklist history"
        assert session.get(UserContentState, user_ids[1]).note == "V1.9L Blood Altar history"
        assert session.get(UserMaterialInventory, user_ids[2]).note == "V1.9L inventory history"
        assert session.get(UserProjectStageState, user_ids[3]).note == "V1.9L project history"
    engine.dispose()