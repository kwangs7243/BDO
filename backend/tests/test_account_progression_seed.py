from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import Session

from app.checklists import get_current_checklists
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
    Reward,
    ScheduleRule,
    Source,
    UserContentState,
)
from app.periods import KST
from app.seed import import_seed


DATA_DIR = Path(__file__).resolve().parents[2] / "data"

V17D_SOURCE_IDS = {
    "adventure-log-bookshelf-guide",
    "new-adventurer-main-quest-guide",
    "quest-system-guide",
    "morning-land-main-quest-guide",
    "jordaine-saga-update-2024-02-07",
    "family-stat-quest-history",
    "hyperboost-progression-2026",
    "morning-land-launch-2023-03-29",
}

V17D_CONTENT_SLUGS = {
    "account-progression-foundation",
    "main-quest-progression-foundation",
    "content-unlock-foundation",
    "permanent-family-reward-foundation",
    "permanent-stat-progression",
    "family-convenience-unlock-foundation",
    "adventure-log-foundation",
    "magnus-progression",
    "igor-bartali-adventure-log",
    "book-of-margahan",
    "main-quest-balenos",
    "main-quest-jordaine-saga",
    "main-quest-mediah",
    "main-quest-valencia",
    "main-quest-kamasylvia",
    "main-quest-drieghan",
    "main-quest-odyllita",
    "main-quest-morning-land",
    "main-quest-mountain-of-eternal-winter",
    "kamasylvia-family-defense-quest",
    "odyllita-family-attack-quest",
}


def _requirement(session: Session, seed_key: str) -> ContentRequirement:
    row = session.scalar(select(ContentRequirement).where(ContentRequirement.seed_key == seed_key))
    assert row is not None
    assert isinstance(row.structured_value, dict)
    return row


def _value(session: Session, seed_key: str) -> dict:
    return _requirement(session, seed_key).structured_value


def _reward(session: Session, seed_key: str) -> Reward:
    row = session.scalar(select(Reward).where(Reward.seed_key == seed_key))
    assert row is not None
    return row


def _relations(session: Session, slug: str) -> set[tuple[str, str]]:
    content = session.scalar(select(Content).where(Content.slug == slug))
    assert content is not None
    rows = session.execute(
        select(ContentRelation.relation_type, Content.slug)
        .join(Content, Content.id == ContentRelation.to_content_id)
        .where(ContentRelation.from_content_id == content.id, ContentRelation.active.is_(True))
    )
    return set(rows)


def test_v17d_seed_rows_are_unique_and_expected_entities_exist() -> None:
    sources = json.loads((DATA_DIR / "seed_sources.json").read_text(encoding="utf-8"))
    contents = json.loads((DATA_DIR / "seed_contents.json").read_text(encoding="utf-8"))
    source_ids = [row["id"] for row in sources]
    source_urls = [row["url"].lower() for row in sources]
    slugs = [row["slug"] for row in contents]

    assert len(source_ids) == len(set(source_ids))
    assert len(source_urls) == len(set(source_urls))
    assert len(slugs) == len(set(slugs))
    assert V17D_SOURCE_IDS <= set(source_ids)
    assert V17D_CONTENT_SLUGS <= set(slugs)
    assert 15 <= len(V17D_CONTENT_SLUGS) <= 30
    assert {"magnus-remote-storage", "agris-fever", "black-shrine-donghae-weekly"} <= set(slugs)

    new_rows = [row for row in contents if row["slug"] in V17D_CONTENT_SLUGS]
    nested_keys = [
        nested["seed_key"]
        for row in new_rows
        for collection in ("requirements", "steps", "rewards", "relations", "evidence")
        for nested in row.get(collection, [])
    ]
    assert len(nested_keys) == len(set(nested_keys))
    assert {
        source_id
        for row in new_rows
        for claim in row.get("evidence", [])
        for source_id in claim["source_ids"]
    } <= set(source_ids)
    assert {
        relation["to_content_slug"]
        for row in new_rows
        for relation in row.get("relations", [])
    } <= set(slugs)


def test_account_foundations_form_hierarchy_and_reuse_existing_content(session: Session) -> None:
    root_children = {
        "main-quest-progression-foundation",
        "content-unlock-foundation",
        "permanent-family-reward-foundation",
        "family-convenience-unlock-foundation",
        "adventure-log-foundation",
    }
    for slug in root_children:
        assert ("part_of", "account-progression-foundation") in _relations(session, slug)

    existing_targets = {
        target
        for slug in V17D_CONTENT_SLUGS
        for _, target in _relations(session, slug)
        if target not in V17D_CONTENT_SLUGS
    }
    assert {
        "energy-foundation",
        "contribution-economy-foundation",
        "ecology-family-drop-bonus",
        "combat-gear-progression-strategy",
        "life-family-levels",
        "magnus-remote-storage",
        "family-silver-unification",
        "storage-current-system",
        "agris-fever",
        "black-shrine-donghae-weekly",
        "grind-zone-recommendation-system",
        "carrack-advance",
        "panokseon",
        "barter-current-system",
    } <= existing_targets


def test_magnus_tracks_large_checkpoints_and_reuses_unlock_targets(session: Session) -> None:
    start = _value(session, "magnus-progression.start")
    completion = _value(session, "magnus-progression.completion")
    assert start["start_quest"] == "[마그누스] 추억의 벨리아"
    assert len(start["alternative_entry_paths"]) == 3
    assert completion == {
        "knowledge_role": "fact",
        "completion_quest": "[마그누스] 도움의 대가",
        "scope": "family",
    }
    steps = list(session.scalars(select(ContentStep).where(ContentStep.seed_key.like("magnus-progression.step.%"))))
    assert [row.phase for row in sorted(steps, key=lambda row: row.order_no)] == ["unlock", "first_time", "reward"]
    reward = _reward(session, "magnus-progression.reward.pen-boss-armor")
    assert (reward.reward_type, reward.amount, reward.unit, reward.is_choice) == ("quest_reward", 1, "개", True)
    relations = _relations(session, "magnus-progression")
    assert ("unlocks", "magnus-remote-storage") in relations
    assert ("unlocks", "main-quest-morning-land") in relations


def test_adventure_log_current_and_superseded_rules_are_separate(session: Session) -> None:
    current = _value(session, "igor-bartali-adventure-log.current-consolidation")
    legacy = _requirement(session, "igor-bartali-adventure-log.legacy-rewards")
    foundation_legacy = _requirement(session, "adventure-log-foundation.legacy-stat-distribution")
    assert current["effective_date"] == "2025-07-23"
    assert {"AP", "DP", "accuracy", "evasion", "max_hp"} <= set(current["consolidated_stats"])
    assert legacy.active is False and legacy.structured_value["knowledge_role"] == "historical"
    assert foundation_legacy.active is False
    legacy_evidence = list(session.scalars(select(Evidence).where(Evidence.entity_id.in_({legacy.seed_key, foundation_legacy.seed_key}))))
    assert legacy_evidence and all(row.verification_status == "superseded" and not row.active for row in legacy_evidence)
    assert (_reward(session, "igor-bartali-adventure-log.reward.family-ap").amount,
            _reward(session, "igor-bartali-adventure-log.reward.family-dp").amount) == (6, 6)


def test_book_of_margahan_enhances_but_does_not_unlock_agris(session: Session) -> None:
    effect = _value(session, "book-of-margahan.agris-enhancement")
    assert effect["does_not_unlock_agris"] is True
    assert (effect["agris_point_cap_increase"], effect["daily_recovery_increase"]) == (50_000, 5_000)
    assert effect["trash_loot_bonus_percentage_point_increase"] == 50
    rewards = {
        row.seed_key: (row.amount, row.unit)
        for row in session.scalars(select(Reward).where(Reward.seed_key.like("book-of-margahan.reward.%")))
    }
    assert rewards == {
        "book-of-margahan.reward.point-cap": (50_000, "point"),
        "book-of-margahan.reward.daily-recovery": (5_000, "point_per_day"),
        "book-of-margahan.reward.trash-bonus": (50, "percentage_point"),
    }
    relations = _relations(session, "book-of-margahan")
    assert ("related", "agris-fever") in relations
    assert ("unlocks", "agris-fever") not in relations


def test_main_quest_checkpoints_and_permanent_family_rewards(session: Session) -> None:
    assert ("alternative", "main-quest-balenos") in _relations(
        session, "main-quest-mountain-of-eternal-winter"
    )
    assert ("prerequisite", "main-quest-balenos") in _relations(
        session, "main-quest-jordaine-saga"
    )
    assert ("prerequisite", "main-quest-jordaine-saga") in _relations(
        session, "main-quest-mediah"
    )
    morning_relations = _relations(session, "main-quest-morning-land")
    assert ("prerequisite", "magnus-progression") in morning_relations
    assert ("unlocks", "black-shrine-donghae-weekly") in morning_relations
    assert _value(session, "main-quest-morning-land.tales")["initial_tale_count"] == 8

    expected = {
        "kamasylvia-family-defense-quest": ("kamasylvia-family-defense-quest.reward.family-dp", 1),
        "odyllita-family-attack-quest": ("odyllita-family-attack-quest.reward.family-ap", 1),
    }
    for slug, (reward_key, amount) in expected.items():
        requirement = _value(session, f"{slug}.unlock")
        assert requirement["scope"] == "family"
        assert requirement["persistence"] == "permanent"
        assert requirement["repeatable"] is False
        reward = _reward(session, reward_key)
        assert (reward.reward_type, reward.amount, reward.unit) == ("fixed_effect", amount, "point")


def test_v17d_fact_claims_have_verified_evidence_and_no_strategy_or_measurement(session: Session) -> None:
    requirements = list(
        session.scalars(
            select(ContentRequirement).join(Content).where(Content.slug.in_(V17D_CONTENT_SLUGS))
        )
    )
    roles = {
        row.structured_value.get("knowledge_role")
        for row in requirements
        if isinstance(row.structured_value, dict)
    }
    assert roles == {"fact", "historical"}
    for row in requirements:
        evidence = list(session.scalars(select(Evidence).where(Evidence.entity_id == row.seed_key)))
        assert evidence
        if row.active and row.structured_value.get("knowledge_role") == "fact":
            assert all(item.active and item.verification_status == "verified" for item in evidence)
        else:
            assert all(not item.active and item.verification_status == "superseded" for item in evidence)

    for model in (ContentStep, Reward):
        rows = list(session.scalars(select(model).join(Content).where(Content.slug.in_(V17D_CONTENT_SLUGS))))
        assert rows
        for row in rows:
            evidence = list(session.scalars(select(Evidence).where(Evidence.entity_id == row.seed_key)))
            assert evidence and all(item.active and item.verification_status == "verified" for item in evidence)

    assert session.scalar(
        select(func.count()).select_from(ScheduleRule).join(Content).where(Content.slug.in_(V17D_CONTENT_SLUGS))
    ) == 0
    assert session.scalar(
        select(func.count()).select_from(ChecklistTemplate).join(Content).where(Content.slug.in_(V17D_CONTENT_SLUGS))
    ) == 0


def test_v17a_b_c_semantic_baseline_remains_available(session: Session) -> None:
    assert _value(session, "agris-fever.base")["max_points"] == 50_000
    assert _value(session, "black-shrine-donghae-current-system.core")["weekly_rewarded_clears"] == 5
    assert _value(session, "world-boss-current-roster.current")["entity_count"] == 14
    assert session.scalar(select(Content).where(Content.slug == "hexe-sanctuary-elvia")) is not None


def test_v17d_temp_db_migration_import_idempotence_and_history_preservation(
    tmp_path, monkeypatch
) -> None:
    db_path = tmp_path / "v17d-validation.db"
    database_url = f"sqlite:///{db_path.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", database_url)

    backend_dir = Path(__file__).resolve().parents[1]
    alembic_config = Config(str(backend_dir / "alembic.ini"))
    alembic_config.set_main_option("script_location", str(backend_dir / "alembic"))
    command.upgrade(alembic_config, "20260902_0001")
    command.upgrade(alembic_config, "head")

    source_rows = json.loads((DATA_DIR / "seed_sources.json").read_text(encoding="utf-8"))
    content_rows = json.loads((DATA_DIR / "seed_contents.json").read_text(encoding="utf-8"))
    baseline_dir = tmp_path / "v17c-seed"
    baseline_dir.mkdir()
    (baseline_dir / "seed_sources.json").write_text(
        json.dumps([row for row in source_rows if row["id"] not in V17D_SOURCE_IDS], ensure_ascii=False),
        encoding="utf-8",
    )
    (baseline_dir / "seed_contents.json").write_text(
        json.dumps([row for row in content_rows if row["slug"] not in V17D_CONTENT_SLUGS], ensure_ascii=False),
        encoding="utf-8",
    )

    models = (
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
    )
    nested_models = models[2:]
    engine = create_engine(database_url)
    with Session(engine, expire_on_commit=False) as db_session:
        import_seed(db_session, baseline_dir)
        baseline_content_ids = {row.slug: row.id for row in db_session.scalars(select(Content))}
        baseline_nested = {
            model.__name__: {
                row.seed_key: (row.id, row.active)
                for row in db_session.scalars(select(model))
                if getattr(row, "seed_key", None)
            }
            for model in nested_models
        }

        get_current_checklists(db_session, "weekly", datetime(2026, 9, 4, 12, tzinfo=KST))
        item_state = db_session.scalar(select(ChecklistItemState))
        assert item_state is not None
        item_state.completed = True
        item_state.completed_at = datetime(2026, 9, 4, 3, tzinfo=timezone.utc)
        item_state.note = "V1.7D history preservation marker"
        agris = db_session.scalar(select(Content).where(Content.slug == "agris-fever"))
        assert agris is not None
        user_state = UserContentState(
            content_id=agris.id,
            state="in_progress",
            priority=1,
            note="V1.7D user state marker",
            updated_at=datetime(2026, 9, 4, 3, tzinfo=timezone.utc),
        )
        db_session.add(user_state)
        db_session.commit()
        history_ids = (
            db_session.scalar(select(func.count()).select_from(ChecklistInstance)),
            item_state.id,
            user_state.id,
        )

        import_seed(db_session, DATA_DIR)
        first_counts = tuple(db_session.scalar(select(func.count()).select_from(model)) for model in models)
        new_content_ids = {
            row.slug: row.id
            for row in db_session.scalars(select(Content).where(Content.slug.in_(V17D_CONTENT_SLUGS)))
        }
        new_nested = {
            model.__name__: {
                row.seed_key: (row.id, row.active)
                for row in db_session.scalars(select(model))
                if getattr(row, "seed_key", None)
                and row.seed_key.split(".", 1)[0] in V17D_CONTENT_SLUGS
            }
            for model in nested_models
        }

        for _ in range(2):
            import_seed(db_session, DATA_DIR)
            assert first_counts == tuple(
                db_session.scalar(select(func.count()).select_from(model)) for model in models
            )

        assert baseline_content_ids == {
            row.slug: row.id
            for row in db_session.scalars(select(Content).where(Content.slug.in_(baseline_content_ids)))
        }
        assert baseline_nested == {
            model.__name__: {
                row.seed_key: (row.id, row.active)
                for row in db_session.scalars(select(model))
                if getattr(row, "seed_key", None) in baseline_nested[model.__name__]
            }
            for model in nested_models
        }
        assert new_content_ids == {
            row.slug: row.id
            for row in db_session.scalars(select(Content).where(Content.slug.in_(V17D_CONTENT_SLUGS)))
        }
        assert new_nested == {
            model.__name__: {
                row.seed_key: (row.id, row.active)
                for row in db_session.scalars(select(model))
                if getattr(row, "seed_key", None) in new_nested[model.__name__]
            }
            for model in nested_models
        }
        assert all(
            row.status == "active"
            for row in db_session.scalars(select(Content).where(Content.slug.in_(V17D_CONTENT_SLUGS)))
        )
        assert db_session.scalar(select(func.count()).select_from(ChecklistInstance)) == history_ids[0]
        preserved_item = db_session.get(ChecklistItemState, history_ids[1])
        preserved_user = db_session.get(UserContentState, history_ids[2])
        assert preserved_item is not None and preserved_item.completed is True
        assert preserved_item.note == "V1.7D history preservation marker"
        assert preserved_user is not None and preserved_user.note == "V1.7D user state marker"
