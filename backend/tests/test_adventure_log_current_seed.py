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
FIXED_NOW = datetime(2026, 9, 8, 16, 0, tzinfo=KST)
NEW_SOURCE_IDS = {
    "emma-bartali-log-update-2026-07-29",
    "justin-bartali-log-update-2025-11-19",
}
NEW_CONTENT_SLUGS = {
    "rulupee-travel-log",
    "lamute-gang-adventure-log",
    "caphras-record",
    "fughar-success-era",
    "herald-journal",
    "pavino-greko-miscellany",
    "deve-encyclopedia",
    "alustin-alchemy-journal",
    "dorin-morgrim-secret-journal",
    "morning-land-boss-codex",
    "morning-land-story-codex",
    "adventurer-strange-scenery",
    "justin-bartali-adventure-log",
    "emma-bartali-record-log",
}
V19L_CONTENT_SLUGS = NEW_CONTENT_SLUGS | {
    "adventure-log-foundation",
    "igor-bartali-adventure-log",
    "book-of-margahan",
}


def seed_rows() -> tuple[list[dict], list[dict]]:
    return (
        json.loads((DATA / "seed_sources.json").read_text(encoding="utf-8")),
        json.loads((DATA / "seed_contents.json").read_text(encoding="utf-8")),
    )


def requirement(session: Session, seed_key: str) -> ContentRequirement:
    row = session.scalar(
        select(ContentRequirement).where(ContentRequirement.seed_key == seed_key)
    )
    assert row is not None
    return row


def reward(session: Session, seed_key: str) -> Reward:
    row = session.scalar(select(Reward).where(Reward.seed_key == seed_key))
    assert row is not None
    return row


def relations(session: Session, slug: str) -> set[tuple[str, str]]:
    return {
        (row.relation_type, row.to_content.slug)
        for row in session.scalars(
            select(ContentRelation)
            .join(Content, Content.id == ContentRelation.from_content_id)
            .where(Content.slug == slug, ContentRelation.active.is_(True))
        )
    }


def test_v19l_counts_references_and_identity_uniqueness() -> None:
    sources, contents = seed_rows()
    source_ids = {row["id"] for row in sources}
    slugs = {row["slug"] for row in contents}
    roles = Counter(
        requirement["structured_value"].get("knowledge_role")
        for content in contents
        for requirement in content.get("requirements", [])
        if isinstance(requirement.get("structured_value"), dict)
    )
    assert len(sources) >= 182
    assert len(contents) >= 294
    assert sum(len(row.get("relations", [])) for row in contents) >= 521
    assert roles["fact"] >= 279
    assert roles["strategy"] >= 63
    assert roles["measurement"] >= 11
    assert len(source_ids) == len(sources)
    assert len({row["url"] for row in sources}) == len(sources)
    assert len(slugs) == len(contents)
    assert NEW_SOURCE_IDS <= source_ids
    assert NEW_CONTENT_SLUGS <= slugs
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


def test_adventure_log_foundation_matches_current_bookshelf(session: Session) -> None:
    structure = requirement(
        session, "adventure-log-foundation.current-structure"
    ).structured_value
    assert (structure["listed_group_count"], structure["non_event_group_count"]) == (10, 9)
    assert structure["event_group_count"] == 1
    assert structure["groups"] == [
        "이고르 바탈리의 모험일지",
        "까마귀 상단의 기록일지",
        "그믐달 상단의 행동일지",
        "샤카투 상단의 수집일지",
        "이벤트 모험일지",
        "우두머리 도감 : 아침의 나라",
        "아침의 나라 이야기 도감 : 동해도/황해도 편",
        "어느 모험가의 낯선 풍경",
        "저스틴 바탈리의 모험일지",
        "올비아 아카데미 성장일지",
    ]
    source = session.get(Source, "adventure-log-bookshelf-guide")
    assert source is not None
    assert source.url.endswith("Wiki?wikiNo=313")
    assert source.title == "모험일지 책장"


def test_igor_and_margahan_current_rewards_keep_stable_semantics(session: Session) -> None:
    assert requirement(
        session, "igor-bartali-adventure-log.volume-count"
    ).structured_value["volume_count"] == 15
    assert (
        reward(session, "igor-bartali-adventure-log.reward.family-ap").amount,
        reward(session, "igor-bartali-adventure-log.reward.family-dp").amount,
    ) == (6, 6)
    current = requirement(
        session, "igor-bartali-adventure-log.current-consolidation"
    ).structured_value
    assert current["effective_date"] == "2025-07-23"
    legacy = requirement(session, "igor-bartali-adventure-log.legacy-rewards")
    assert legacy.active is False
    legacy_evidence = list(
        session.scalars(select(Evidence).where(Evidence.entity_id == legacy.seed_key))
    )
    assert legacy_evidence
    assert all(not row.active and row.verification_status == "superseded" for row in legacy_evidence)
    effect = requirement(session, "book-of-margahan.agris-enhancement").structured_value
    assert effect["does_not_unlock_agris"] is True
    assert (
        effect["agris_point_cap_increase"],
        effect["daily_recovery_increase"],
        effect["trash_loot_bonus_percentage_point_increase"],
    ) == (50_000, 5_000, 50)


def test_current_catalog_unlocks_rewards_and_identity_boundaries(session: Session) -> None:
    levels = {
        "rulupee-travel-log": 55,
        "lamute-gang-adventure-log": 55,
        "caphras-record": 55,
        "fughar-success-era": 55,
        "herald-journal": 58,
        "pavino-greko-miscellany": 58,
        "deve-encyclopedia": 57,
        "alustin-alchemy-journal": 57,
        "dorin-morgrim-secret-journal": 57,
        "adventurer-strange-scenery": 11,
        "justin-bartali-adventure-log": 60,
    }
    for slug, level in levels.items():
        assert requirement(session, f"{slug}.unlock").structured_value["minimum_level"] == level
        assert ("part_of", "adventure-log-foundation") in relations(session, slug)
    justin_requirement = requirement(session, "justin-bartali-adventure-log.unlock")
    justin = justin_requirement.structured_value
    assert justin["starting_quest"] == "[저스틴의 모험] 집 떠난 탕아"
    assert justin["completion_quest"] == "[모험일지] 저스틴 바탈리의 모험일지"
    assert (justin["entry_count"], justin["entry_range"]) == (17, "I-XVII")
    assert "17권" not in justin_requirement.description

    justin_source = session.get(Source, "justin-bartali-log-update-2025-11-19")
    assert justin_source is not None
    assert justin_source.url == (
        "https://www.kr.playblackdesert.com/ko-KR/News/Detail?"
        "countryType=ko-KR&groupContentNo=14803"
    )
    assert justin_source.title == "11월 19일(수) 업데이트 안내"
    unlock_sources = {
        row.source_id
        for row in session.scalars(
            select(Evidence).where(
                Evidence.entity_id == "justin-bartali-adventure-log.unlock",
                Evidence.active.is_(True),
            )
        )
    }
    assert "justin-bartali-log-update-2025-11-19" in unlock_sources

    justin_rewards = {
        row.seed_key: row
        for row in session.scalars(
            select(Reward)
            .join(Content)
            .where(Content.slug == "justin-bartali-adventure-log", Reward.active.is_(True))
        )
    }
    assert {
        seed_key: row.amount for seed_key, row in justin_rewards.items()
    } == {
        "justin-bartali-adventure-log.reward.item-collection-scroll": 12,
        "justin-bartali-adventure-log.reward.florin-secret-book": 9,
        "justin-bartali-adventure-log.reward.intermediate-titles": 7,
        "justin-bartali-adventure-log.reward.sealed-combat-book": 1,
        "justin-bartali-adventure-log.reward.sealed-life-book": 1,
        "justin-bartali-adventure-log.reward.cron-stone": 300,
        "justin-bartali-adventure-log.reward.final-title": 1,
        "justin-bartali-adventure-log.reward.warranty": 1,
    }
    assert justin_rewards[
        "justin-bartali-adventure-log.reward.intermediate-titles"
    ].notes == (
        "고소공포증, 숨은 그림 찾기, 투견, 역마살, 이몸등장, 덜덜 떠는, "
        "바람에 펄럭이는"
    )
    assert justin_rewards[
        "justin-bartali-adventure-log.reward.sealed-combat-book"
    ].notes == "지속 기간 7일"
    assert justin_rewards[
        "justin-bartali-adventure-log.reward.sealed-life-book"
    ].notes == "지속 기간 7일"
    assert justin_rewards[
        "justin-bartali-adventure-log.reward.final-title"
    ].name == "칭호: 집 나간 자식"
    assert justin_rewards[
        "justin-bartali-adventure-log.reward.warranty"
    ].name == "저스틴 바탈리의 보증서"
    for row in justin_rewards.values():
        evidence = list(
            session.scalars(
                select(Evidence).where(
                    Evidence.entity_id == row.seed_key,
                    Evidence.claim_key == "reward",
                    Evidence.active.is_(True),
                )
            )
        )
        assert {item.source_id for item in evidence} == {
            "justin-bartali-log-update-2025-11-19"
        }
        assert all(item.verification_status == "verified" for item in evidence)

    for slug in ("morning-land-boss-codex", "morning-land-story-codex"):
        assert requirement(session, f"{slug}.unlock").structured_value[
            "unlock_condition"
        ] == "none_listed"

    assert reward(session, "herald-journal.reward.valks-cry").amount == 50
    assert reward(session, "pavino-greko-miscellany.reward.gold-bar-1kg").amount == 7
    assert reward(
        session, "dorin-morgrim-secret-journal.reward.item-collection-scroll"
    ).amount == 27
    assert reward(session, "morning-land-boss-codex.reward.hongik-ember").amount == 220
    assert reward(session, "adventurer-strange-scenery.reward.primordial-ember").amount == 15

    boss = requirement(session, "morning-land-boss-codex.identity").structured_value
    story = requirement(session, "morning-land-story-codex.identity").structured_value
    assert boss["journal_kind"] == "boss_codex"
    assert boss["same_as_black_shrine_weekly"] is False
    assert story["journal_kind"] == "story_replay_archive"
    assert story["standard_stat_progression"] is False
    assert ("related", "black-shrine-donghae-current-system") in relations(
        session, "morning-land-boss-codex"
    )
    assert ("related", "main-quest-morning-land") in relations(
        session, "morning-land-story-codex"
    )


def test_emma_chapters_rewards_and_known_issue_are_separate(session: Session) -> None:
    identity = requirement(session, "emma-bartali-record-log.identity").structured_value
    chapters = requirement(
        session, "emma-bartali-record-log.chapter-prerequisites"
    ).structured_value["chapter_prerequisites"]
    assert identity["bookshelf_group"] == "올비아 아카데미 성장일지"
    assert (identity["chapter_count"], identity["support_range"]) == (13, "동(V)-풍(VIII)")
    assert set(chapters) == {str(number) for number in range(1, 14)}
    assert "이고르 바탈리" in chapters["1"]
    assert "구미호" in chapters["8"]
    assert "비형랑" in chapters["12"]

    expected = {
        "emma-bartali-record-log.reward.ancient-hammer-pen": 10,
        "emma-bartali-record-log.reward.ancient-black-stone-pen": 2,
        "emma-bartali-record-log.reward.ancient-hammer-hex": 10,
        "emma-bartali-record-log.reward.ancient-black-stone-hex": 2,
        "emma-bartali-record-log.reward.ancient-black-stone-sep": 2,
        "emma-bartali-record-log.reward.dawn-essence": 100,
    }
    assert {key: reward(session, key).amount for key in expected} == expected
    issue = session.scalar(
        select(Evidence).where(
            Evidence.entity_id == "emma-bartali-record-log.section.known-issue"
        )
    )
    assert issue is not None
    assert (issue.verification_status, issue.source_id) == (
        "needs_review",
        "known-issues-current-2026-09-04",
    )
    assert ("related", "igor-bartali-adventure-log") in relations(
        session, "emma-bartali-record-log"
    )


def test_all_active_v19l_fact_claims_have_official_evidence(session: Session) -> None:
    contents = list(
        session.scalars(select(Content).where(Content.slug.in_(V19L_CONTENT_SLUGS)))
    )
    assert len(contents) == len(V19L_CONTENT_SLUGS)
    for content in contents:
        for claim_key in ("summary", "purpose"):
            evidence = list(
                session.scalars(
                    select(Evidence).where(
                        Evidence.entity_id == content.slug,
                        Evidence.claim_key == claim_key,
                        Evidence.active.is_(True),
                    )
                )
            )
            assert evidence, (content.slug, claim_key)
            assert all(row.verification_status == "verified" for row in evidence)
            assert all(row.source.source_type.startswith("official") for row in evidence)

    for model, claim_key in (
        (ContentRequirement, "description"),
        (ContentStep, "description"),
        (Reward, "reward"),
    ):
        rows = list(
            session.scalars(
                select(model)
                .join(Content)
                .where(Content.slug.in_(V19L_CONTENT_SLUGS), model.active.is_(True))
            )
        )
        assert rows
        for row in rows:
            evidence = list(
                session.scalars(
                    select(Evidence).where(
                        Evidence.entity_id == row.seed_key,
                        Evidence.claim_key == claim_key,
                        Evidence.active.is_(True),
                    )
                )
            )
            assert evidence, row.seed_key
            assert all(item.verification_status == "verified" for item in evidence)
            assert all(item.source.source_type.startswith("official") for item in evidence)


def test_emma_content_api_and_prompt_bridge_use_existing_boundary(session: Session) -> None:
    emma = session.scalar(select(Content).where(Content.slug == "emma-bartali-record-log"))
    assert emma is not None
    state = UserContentState(
        content_id=emma.id,
        state="in_progress",
        priority=1,
        note="8장 조건 확인 중",
        updated_at=datetime(2026, 9, 8, 7, tzinfo=timezone.utc),
    )
    session.add(state)
    session.commit()
    detail = get_content_detail(session, emma.slug, FIXED_NOW)
    assert detail is not None
    assert detail.user_state.note == "8장 조건 확인 중"
    assert any(source.id == "emma-bartali-log-update-2026-07-29" for source in detail.sources)

    for mode in (
        PromptMode.CONTENT_ONBOARDING,
        PromptMode.NEXT_ACTION,
        PromptMode.VERIFY_LATEST,
    ):
        request = PromptRequest(mode=mode, content_slug=emma.slug, as_of=FIXED_NOW)
        first = build_context(session, request, FIXED_NOW)
        assert first == build_context(session, request, FIXED_NOW)
        assert any("13개 장" in fact.claim for fact in first.canonical_facts)
        assert all(fact.knowledge_role.value == "fact" for fact in first.canonical_facts)
        assert any("아레하자 마을" in fact.claim for fact in first.open_questions_or_conflicts)
        assert "note: 8장 조건 확인 중" in first.user_state
        markdown = render_markdown(first)
        assert "## VERIFIED_KNOWLEDGE" in markdown
        assert "## OPEN_QUESTIONS_OR_CONFLICTS" in markdown


def _v19k_baseline_rows() -> tuple[list[dict], list[dict]]:
    sources, contents = seed_rows()
    baseline_sources = [
        copy.deepcopy(row) for row in sources if row["id"] not in NEW_SOURCE_IDS
    ]
    bookshelf = next(
        row for row in baseline_sources if row["id"] == "adventure-log-bookshelf-guide"
    )
    bookshelf.update(
        title="Adventure Log Bookshelf",
        retrieved_at="2026-09-04T12:00:00+09:00",
        notes="Current adventure-log unlock conditions and family-wide reward structure",
    )
    known = next(
        row for row in baseline_sources if row["id"] == "known-issues-current-2026-09-04"
    )
    known.update(
        title="현재 확인 중인 현상",
        retrieved_at="2026-09-06T12:00:00+09:00",
    )
    known.pop("notes", None)

    baseline_contents = [
        copy.deepcopy(row) for row in contents if row["slug"] not in NEW_CONTENT_SLUGS
    ]
    by_slug = {row["slug"]: row for row in baseline_contents}
    foundation = by_slug["adventure-log-foundation"]
    foundation.update(
        summary="책장 해금 조건과 가문 공통 영구 보상을 대표 일지 단위로 추적하는 기반이다.",
        purpose="모든 권·장을 나열하지 않고 해금과 완료 상태를 대표 콘텐츠로 관리한다.",
        last_verified_at="2026-09-04",
    )
    current = next(
        row for row in foundation["requirements"]
        if row["seed_key"] == "adventure-log-foundation.current-structure"
    )
    current["description"] = "모험일지 책장에는 11개 주제가 있으며 각 일지는 조건 충족 뒤 순차적으로 열린다."
    current["structured_value"] = {
        "knowledge_role": "fact",
        "topic_count": 11,
        "unlock_pattern": "condition_then_sequential",
    }
    foundation["evidence"] = [
        row
        for row in foundation["evidence"]
        if row["seed_key"]
        not in {
            "adventure-log-foundation.claim.summary",
            "adventure-log-foundation.claim.purpose",
        }
    ]
    for row in foundation["evidence"]:
        row["last_verified_at"] = "2026-09-04"
        if row["seed_key"].endswith("current-structure"):
            row["claim_key"] = "requirement:current-structure"
        else:
            row["claim_key"] = "requirement:legacy-stat-distribution"
            row["source_ids"] = ["pit-weekly-2025"]

    igor = by_slug["igor-bartali-adventure-log"]
    igor.update(
        summary="현재 핵심 가문 능력치 보상이 통합된 대표 모험일지다.",
        purpose="해금 조건, 전체 완료 상태와 현재 영구 공격력·방어력 보상을 추적한다.",
        last_verified_at="2026-09-04",
    )
    igor["requirements"] = [
        row for row in igor["requirements"] if not row["seed_key"].endswith("volume-count")
    ]
    igor["evidence"] = [
        row
        for row in igor["evidence"]
        if row["seed_key"]
        not in {
            "igor-bartali-adventure-log.claim.summary",
            "igor-bartali-adventure-log.claim.purpose",
            "igor-bartali-adventure-log.claim.volume-count",
        }
    ]
    old_claims = {
        "igor-bartali-adventure-log.claim.unlock": ("requirement:unlock", ["adventure-log-bookshelf-guide"]),
        "igor-bartali-adventure-log.claim.consolidation": (
            "requirement:current-consolidation",
            ["pit-weekly-2025", "adventure-log-bookshelf-guide"],
        ),
        "igor-bartali-adventure-log.claim.legacy": ("requirement:legacy-rewards", ["pit-weekly-2025"]),
        "igor-bartali-adventure-log.claim.step-unlock": ("step:unlock", ["adventure-log-bookshelf-guide"]),
        "igor-bartali-adventure-log.claim.step-complete": (
            "step:complete",
            ["adventure-log-bookshelf-guide", "hyperboost-progression-2026"],
        ),
        "igor-bartali-adventure-log.claim.reward-ap": ("reward:family-ap", ["hyperboost-progression-2026"]),
        "igor-bartali-adventure-log.claim.reward-dp": ("reward:family-dp", ["hyperboost-progression-2026"]),
    }
    for row in igor["evidence"]:
        row["claim_key"], row["source_ids"] = old_claims[row["seed_key"]]
        row["last_verified_at"] = "2026-09-04"

    margahan = by_slug["book-of-margahan"]
    margahan["last_verified_at"] = "2026-09-04"
    margahan["evidence"] = [
        row
        for row in margahan["evidence"]
        if row["seed_key"]
        not in {
            "book-of-margahan.claim.summary",
            "book-of-margahan.claim.purpose",
        }
    ]
    old_margahan = {
        "unlock": "requirement:unlock",
        "enhancement": "requirement:agris-enhancement",
        "step-volume-1": "step:volume-1",
        "step-volume-2": "step:volume-2",
        "reward-cap": "reward:point-cap",
        "reward-recovery": "reward:daily-recovery",
        "reward-bonus": "reward:trash-bonus",
    }
    for row in margahan["evidence"]:
        suffix = row["seed_key"].removeprefix("book-of-margahan.claim.")
        row["claim_key"] = old_margahan[suffix]
        row["last_verified_at"] = "2026-09-04"
    return baseline_sources, baseline_contents


def test_v19k_to_v19l_import_is_idempotent_and_preserves_history(
    tmp_path: Path, monkeypatch
) -> None:
    db_path = tmp_path / "v19l-validation.db"
    database_url = f"sqlite:///{db_path.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", database_url)
    backend_dir = Path(__file__).resolve().parents[1]
    config = Config(str(backend_dir / "alembic.ini"))
    config.set_main_option("script_location", str(backend_dir / "alembic"))
    command.upgrade(config, "20260902_0001")
    command.upgrade(config, "head")

    baseline_sources, baseline_contents = _v19k_baseline_rows()
    assert len(baseline_sources) >= 180
    assert len(baseline_contents) >= 280
    baseline_dir = tmp_path / "v19k-seed"
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
        baseline_nested = {
            model.__name__: {
                row.seed_key: (row.id, row.active)
                for row in session.scalars(select(model))
                if getattr(row, "seed_key", None)
            }
            for model in nested_models
        }

        get_current_checklists(session, "weekly", FIXED_NOW)
        item_state = session.scalar(select(ChecklistItemState))
        igor = session.scalar(
            select(Content).where(Content.slug == "igor-bartali-adventure-log")
        )
        material = session.scalar(select(Material))
        stage = session.scalar(select(ProjectStage))
        assert item_state is not None and igor is not None and material is not None and stage is not None
        item_state.completed = True
        item_state.note = "V1.9L checklist history"
        user_content = UserContentState(
            content_id=igor.id,
            state="in_progress",
            note="V1.9L content history",
            updated_at=datetime(2026, 9, 8, 7, tzinfo=timezone.utc),
        )
        inventory = UserMaterialInventory(
            material_id=material.id,
            quantity=7,
            note="V1.9L inventory history",
            updated_at=datetime(2026, 9, 8, 7, tzinfo=timezone.utc),
        )
        stage_state = UserProjectStageState(
            stage_id=stage.id,
            completed=True,
            completed_at=datetime(2026, 9, 8, 7, tzinfo=timezone.utc),
            note="V1.9L project history",
            updated_at=datetime(2026, 9, 8, 7, tzinfo=timezone.utc),
        )
        session.add_all((user_content, inventory, stage_state))
        session.commit()
        user_ids = (item_state.id, user_content.id, inventory.id, stage_state.id)

        import_seed(session, DATA)
        first_counts = tuple(
            session.scalar(select(func.count()).select_from(model))
            for model in canonical_models
        )
        new_content_ids = {
            row.slug: row.id
            for row in session.scalars(
                select(Content).where(Content.slug.in_(NEW_CONTENT_SLUGS))
            )
        }
        justin_reward_ids = {
            row.seed_key: row.id
            for row in session.scalars(
                select(Reward).where(
                    Reward.seed_key.like("justin-bartali-adventure-log.reward.%")
                )
            )
        }
        assert len(justin_reward_ids) == 8
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
                if getattr(row, "seed_key", None) in baseline_nested[model.__name__]
            }
            assert current == baseline_nested[model.__name__]
        assert new_content_ids == {
            row.slug: row.id
            for row in session.scalars(
                select(Content).where(Content.slug.in_(NEW_CONTENT_SLUGS))
            )
        }
        assert justin_reward_ids == {
            row.seed_key: row.id
            for row in session.scalars(
                select(Reward).where(
                    Reward.seed_key.like("justin-bartali-adventure-log.reward.%")
                )
            )
        }
        assert session.get(ChecklistItemState, user_ids[0]).note == "V1.9L checklist history"
        assert session.get(UserContentState, user_ids[1]).note == "V1.9L content history"
        assert session.get(UserMaterialInventory, user_ids[2]).note == "V1.9L inventory history"
        assert session.get(UserProjectStageState, user_ids[3]).note == "V1.9L project history"
        assert session.scalar(select(func.count()).select_from(ChecklistInstance)) >= 1
