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

V17C_SOURCE_IDS = {
    "songakshi-high-calamity-2026-07-08",
    "morning-land-boss-balance-2026-02-04",
    "heidel-ball-boss-announcements-2026",
    "known-issues-current-2026-09-04",
    "hwanghae-party-strategy-2026-07-27",
    "hwanghae-party-mode-2026-07-31",
    "hwanghae-hyperboost-party-2026-07-30",
    "black-shrine-party-guide-current",
    "donghae-c8-strategy-2026-06-30",
}

DONGHAE_BOSS_SLUGS = {
    "donghae-shrine-golden-pig-king",
    "donghae-shrine-bari",
    "donghae-shrine-bamboo-legion-lieutenant",
    "donghae-shrine-sangoon",
    "donghae-shrine-gumiho",
    "donghae-shrine-oduksini",
    "donghae-shrine-apex-changui",
    "donghae-shrine-duoksini",
    "donghae-shrine-imoogi",
    "donghae-shrine-songakshi",
}

HWANGHAE_BOSS_SLUGS = {
    "hwanghae-shrine-jigwi",
    "hwanghae-shrine-uturi",
    "hwanghae-shrine-blue-clad-youth",
    "hwanghae-shrine-bulgasal",
    "hwanghae-shrine-dark-bonghwang",
    "hwanghae-shrine-bihyung",
    "hwanghae-shrine-deposed-crown-prince",
}

WORLD_BOSS_SLUGS = {
    "world-boss-kzarka",
    "world-boss-nouver",
    "world-boss-karanda",
    "world-boss-kutum",
    "world-boss-quint",
    "world-boss-muraka",
    "world-boss-offin",
    "world-boss-sangoon",
    "world-boss-golden-pig-king",
    "world-boss-uturi",
    "world-boss-bulgasal",
    "world-boss-black-phoenix",
}

V17C_SYSTEM_SLUGS = {
    "boss-content-taxonomy",
    "black-shrine-donghae-current-system",
    "donghae-light-orb-system",
    "donghae-calamity-8-10",
    "donghae-reward-ranking",
    "donghae-hyperboost-armor-support",
    "donghae-boss-strategy",
    "black-shrine-hwanghae-current-system",
    "hwanghae-aura-system",
    "hwanghae-reward-ranking",
    "hwanghae-party-strategy",
    "hwanghae-current-roster",
    "world-boss-current-system",
    "world-boss-current-roster",
    "world-boss-reward-2025-overhaul",
    "morning-land-world-bosses",
    "boss-guide-conflicts",
}

V17C_CONTENT_SLUGS = (
    V17C_SYSTEM_SLUGS | DONGHAE_BOSS_SLUGS | HWANGHAE_BOSS_SLUGS | WORLD_BOSS_SLUGS
)


def _requirement(session: Session, seed_key: str) -> ContentRequirement:
    row = session.scalar(
        select(ContentRequirement).where(ContentRequirement.seed_key == seed_key)
    )
    assert row is not None
    assert isinstance(row.structured_value, dict)
    return row


def _value(session: Session, seed_key: str) -> dict:
    return _requirement(session, seed_key).structured_value


def test_v17c_seed_rows_are_unique_and_expected_entities_exist() -> None:
    sources = json.loads((DATA_DIR / "seed_sources.json").read_text(encoding="utf-8"))
    contents = json.loads((DATA_DIR / "seed_contents.json").read_text(encoding="utf-8"))
    source_ids = [row["id"] for row in sources]
    source_urls = [row["url"] for row in sources]
    slugs = [row["slug"] for row in contents]

    assert len(source_ids) == len(set(source_ids))
    assert len(source_urls) == len(set(source_urls))
    assert len(slugs) == len(set(slugs))
    assert V17C_SOURCE_IDS <= set(source_ids)
    assert V17C_CONTENT_SLUGS <= set(slugs)
    assert {"garmoth", "vell", "black-shrine-donghae-weekly", "black-shrine-hwanghae-weekly"} <= set(slugs)


def test_donghae_current_system_and_light_orbs(session: Session) -> None:
    core = _value(session, "black-shrine-donghae-current-system.core")
    payout = _value(session, "black-shrine-donghae-current-system.weekly-payout")
    orb = _value(session, "donghae-light-orb-system.current")
    per_orb = _value(session, "donghae-light-orb-system.per-orb")
    special = _value(session, "donghae-light-orb-system.special-rules")
    legacy = _requirement(session, "donghae-light-orb-system.legacy-max-five")

    assert core["solo"] is True
    assert core["weekly_rewarded_clears"] == 5
    assert core["same_boss_difficulty_retry"] == "unlimited"
    assert (orb["light_orb_active"], orb["max_orbs"]) == (True, 6)
    assert (orb["light_orb_stat_percent"], orb["character_gear_stat_percent"]) == (90, 10)
    assert (per_orb["elemental_ap_per_orb"], per_orb["elemental_dp_per_orb"]) == (50, 100)
    assert (per_orb["extra_points_per_orb"], per_orb["ability_per_point"]) == (3, 3)
    assert (special["elemental_critical_chance_percent"], special["boss_elemental_cc_resistance_percent"]) == (50, 20)
    assert payout == {
        "knowledge_role": "fact",
        "payout_weekday": 6,
        "payout_time": "00:00",
        "timezone": "Asia/Seoul",
        "destination": "Black Spirit Safe",
        "accumulates": True,
        "expires": False,
    }
    assert legacy.active is False and legacy.structured_value["max_orbs"] == 5


def test_donghae_high_calamity_and_hyperboost(session: Session) -> None:
    high = _value(session, "donghae-calamity-8-10.current")
    assert high["light_orb_active"] is False
    assert high["character_gear_stat_percent"] == 100
    assert _value(session, "donghae-calamity-8-10.duoksini-ap")["ap_by_calamity"] == {"8": 365, "9": 375, "10": 385}
    assert _value(session, "donghae-calamity-8-10.songakshi-ap")["ap_by_calamity"] == {"8": 365, "9": 375, "10": 385}
    assert _value(session, "donghae-calamity-8-10.gumiho-current") == {
        "knowledge_role": "fact",
        "boss": "Gumiho",
        "calamity": 8,
        "required_ap": 315,
        "hp_change_percent": -72,
        "ap_change_percent": -69,
        "effective_from": "2026-07-29",
    }

    support = _value(session, "donghae-hyperboost-armor-support.conditions")
    assert support["support_quest_ap_is_distinct_from_boss_entry_ap"] is True
    assert support["entries"] == [
        {"boss": "Golden Pig King", "calamity": 8, "support_quest_ap": 305, "reward": "Labreska's Helmet", "choice": False},
        {"boss": "Golden Pig King", "calamity": 9, "support_quest_ap": 315, "reward": "Ator's Shoes", "choice": True},
        {"boss": "Sangoon", "calamity": 8, "support_quest_ap": 310, "reward": "Fallen God's Armor", "choice": False},
        {"boss": "Gumiho", "calamity": 8, "support_quest_ap": 315, "reward": "Dahn's Gloves", "choice": True},
    ]


def test_hwanghae_current_system_roster_and_rewards(session: Session) -> None:
    core = _value(session, "black-shrine-hwanghae-current-system.core")
    difficulty = _value(session, "black-shrine-hwanghae-current-system.difficulty")
    entry = _value(session, "black-shrine-hwanghae-current-system.entry")
    healing = _value(session, "black-shrine-hwanghae-current-system.healing-buffs")
    roster = _value(session, "hwanghae-current-roster.current")
    old = _requirement(session, "hwanghae-current-roster.legacy-six")

    assert (core["party_size"], core["weekly_rewarded_clears"]) == (5, 5)
    assert core["failed_attempt_consumes_reward_count"] is False
    assert (difficulty["normal_recommended_ap"], difficulty["challenge_recommended_ap"]) == (300, 330)
    assert difficulty["light_orb_active"] is False and difficulty["character_gear_stat_percent"] == 100
    assert (entry["cutscene_skip_votes_required"], entry["party_size"]) == (3, 5)
    assert healing["potions_disabled"] is True
    assert all(healing[key] for key in ("natural_healing_possible", "skill_healing_possible", "content_orb_healing_possible"))
    assert roster["entity_count"] == 7
    assert {row["slug"] for row in roster["entities"]} == HWANGHAE_BOSS_SLUGS
    assert old.active is False and old.structured_value["entity_count"] == 6
    assert _value(session, "hwanghae-reward-ranking.challenge-current")["amount"] == 1


def test_hwanghae_strategy_is_opinion_not_fact_or_measurement(session: Session) -> None:
    strategy_keys = {
        "hwanghae-party-strategy.easy-pug",
        "hwanghae-party-strategy.coordination",
        "hwanghae-party-strategy.organized-party",
        "hwanghae-party-strategy.mechanics",
    }
    rows = [_requirement(session, key) for key in strategy_keys]
    assert all(row.structured_value["knowledge_role"] == "strategy" for row in rows)
    assert all("measurement_grade" not in row.structured_value for row in rows)
    assert _value(session, "hwanghae-party-strategy.easy-pug")["bosses"] == ["Bulgasal", "Jigwi", "Uturi"]
    assert _value(session, "hwanghae-party-strategy.coordination")["bosses"] == ["Bihyung", "Dark Bonghwang"]
    assert _value(session, "hwanghae-party-strategy.organized-party")["bosses"] == ["Deposed Crown Prince", "Blue-clad Youth"]
    evidence = list(session.scalars(select(Evidence).where(Evidence.entity_id.in_(strategy_keys))))
    assert evidence and all(row.verification_status == "needs_review" for row in evidence)
    source_types = {session.get(Source, row.source_id).source_type for row in evidence}
    assert {"community_discussion", "third_party_guide"} <= source_types


def test_world_boss_current_rules_roster_and_overhaul(session: Session) -> None:
    core = _value(session, "world-boss-current-system.core")
    despawn = _value(session, "world-boss-current-system.despawn")
    loot = _value(session, "world-boss-current-system.loot")
    roster = _value(session, "world-boss-current-roster.current")
    old_count = _requirement(session, "world-boss-current-roster.guide-fixed-thirteen")
    overhaul = _value(session, "world-boss-reward-2025-overhaul.enhanced-probability")

    assert core["shared_hp_across_servers"] is True and core["max_simultaneous_bosses"] == 2
    assert despawn == {"knowledge_role": "fact", "generic_minutes": 30, "exceptions": {"Quint": 15, "Muraka": 15}}
    assert loot["damage_contribution_matters"] is True and loot["damage_is_only_factor"] is False
    assert roster["entity_count"] == 14
    assert {row["slug"] for row in roster["entities"]} == WORLD_BOSS_SLUGS | {"garmoth", "vell"}
    assert old_count.active is False and old_count.structured_value["consistent_with_enumerated_roster"] is False
    assert overhaul["relative_probability_change_percent"] == 100
    assert overhaul["guaranteed"] is False


def test_morning_land_bosses_black_phoenix_vell_and_garmoth(session: Session) -> None:
    morning = _value(session, "morning-land-world-bosses.direct-loot")
    legacy = _requirement(session, "morning-land-world-bosses.legacy-weekly-quests")
    hp = _value(session, "morning-land-world-bosses.hp-2026-02-04")
    protection = _value(session, "morning-land-world-bosses.protection-current")
    phoenix = _value(session, "world-boss-black-phoenix.current")
    vell = _value(session, "world-boss-current-system.vell")
    garmoth = _value(session, "world-boss-current-system.garmoth")

    assert morning["direct_loot_current"] is True and morning["weekly_quest_required"] is False
    assert legacy.active is False and legacy.structured_value["weekly_quests_active"] is False
    assert hp["hp_multiplier"] == {"Bulgasal": 1.5, "Uturi": 1.5, "Sangoon": 1.5, "Golden Pig King": 1.5}
    assert protection["old_full_invulnerability_active"] is False
    assert phoenix["live"] is True and phoenix["replacement_mechanic"] is True and phoenix["separate_schedule"] is False
    assert vell["spawn_times"] == [{"weekday": 3, "time": "00:15"}, {"weekday": 6, "time": "17:00"}]
    assert vell["cannon_based"] is True and vell["death_penalty"] is False
    assert (garmoth["weekly_reward_max"], garmoth["reset_weekday"], garmoth["reset_time"]) == (3, 3, "00:00")
    assert session.scalar(select(Content).where(Content.slug == "hwanghae-shrine-dark-bonghwang")).id != session.scalar(select(Content).where(Content.slug == "world-boss-black-phoenix")).id


def test_announcements_and_temporary_issue_are_not_current_facts(session: Session) -> None:
    announced = {
        "boss-guide-conflicts.future-donghae-orb-removal",
        "boss-guide-conflicts.future-hwanghae-rework",
        "boss-guide-conflicts.future-laurau",
        "boss-guide-conflicts.future-black-shadow-removal",
    }
    for key in announced:
        row = _requirement(session, key)
        assert row.active is False
        assert row.structured_value["knowledge_role"] == "announced_not_live"
        assert row.structured_value["lifecycle"] == "announced_not_live"

    issue = _requirement(session, "boss-guide-conflicts.gumiho-known-issue")
    assert issue.active is True
    assert issue.structured_value["knowledge_role"] == "temporary_known_issue"
    issue_evidence = session.scalar(select(Evidence).where(Evidence.entity_id == issue.seed_key))
    assert issue_evidence is not None and issue_evidence.verification_status == "needs_review"


def test_v17c_has_no_measurement_claims(session: Session) -> None:
    rows = list(
        session.scalars(
            select(ContentRequirement).join(Content).where(Content.slug.in_(V17C_CONTENT_SLUGS))
        )
    )
    roles = [
        row.structured_value.get("knowledge_role")
        for row in rows
        if isinstance(row.structured_value, dict)
    ]
    assert "fact" in roles and "strategy" in roles
    assert "measurement" not in roles


def test_v17c_temp_db_migration_import_idempotence_and_history_preservation(tmp_path, monkeypatch) -> None:
    db_path = tmp_path / "v17c-validation.db"
    database_url = f"sqlite:///{db_path.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", database_url)

    backend_dir = Path(__file__).resolve().parents[1]
    alembic_config = Config(str(backend_dir / "alembic.ini"))
    alembic_config.set_main_option("script_location", str(backend_dir / "alembic"))
    command.upgrade(alembic_config, "20260902_0001")
    command.upgrade(alembic_config, "head")

    source_rows = json.loads((DATA_DIR / "seed_sources.json").read_text(encoding="utf-8"))
    content_rows = json.loads((DATA_DIR / "seed_contents.json").read_text(encoding="utf-8"))
    baseline_dir = tmp_path / "v17b-seed"
    baseline_dir.mkdir()
    (baseline_dir / "seed_sources.json").write_text(
        json.dumps([row for row in source_rows if row["id"] not in V17C_SOURCE_IDS], ensure_ascii=False),
        encoding="utf-8",
    )
    (baseline_dir / "seed_contents.json").write_text(
        json.dumps([row for row in content_rows if row["slug"] not in V17C_CONTENT_SLUGS], ensure_ascii=False),
        encoding="utf-8",
    )

    models = (
        Source, Content, ScheduleRule, ContentRequirement, ContentStep, Reward,
        ContentSection, ChecklistTemplate, ChecklistTemplateItem, ContentRelation, Evidence,
    )
    engine = create_engine(database_url)
    with Session(engine, expire_on_commit=False) as db_session:
        import_seed(db_session, baseline_dir)
        baseline_content_ids = {row.slug: row.id for row in db_session.scalars(select(Content))}
        baseline_nested_ids = {
            model.__name__: {row.seed_key: (row.id, row.active) for row in db_session.scalars(select(model)) if getattr(row, "seed_key", None)}
            for model in models[2:]
        }
        get_current_checklists(db_session, "weekly", datetime(2026, 9, 4, 12, tzinfo=KST))
        item_state = db_session.scalar(select(ChecklistItemState))
        assert item_state is not None
        item_state.completed = True
        item_state.completed_at = datetime(2026, 9, 4, 3, tzinfo=timezone.utc)
        item_state.note = "V1.7C completion history marker"
        garmoth = db_session.scalar(select(Content).where(Content.slug == "garmoth"))
        user_state = UserContentState(
            content_id=garmoth.id,
            state="in_progress",
            priority=1,
            note="V1.7C user state marker",
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
        first_content_ids = {row.slug: row.id for row in db_session.scalars(select(Content).where(Content.slug.in_(V17C_CONTENT_SLUGS)))}
        first_nested_ids = {
            model.__name__: {row.seed_key: (row.id, row.active) for row in db_session.scalars(select(model)) if getattr(row, "seed_key", None) and row.seed_key.split(".", 1)[0] in V17C_CONTENT_SLUGS}
            for model in models[2:]
        }

        import_seed(db_session, DATA_DIR)
        second_counts = tuple(db_session.scalar(select(func.count()).select_from(model)) for model in models)
        assert first_counts == second_counts
        assert baseline_content_ids == {row.slug: row.id for row in db_session.scalars(select(Content).where(Content.slug.in_(baseline_content_ids)))}
        assert baseline_nested_ids == {
            model.__name__: {row.seed_key: (row.id, row.active) for row in db_session.scalars(select(model)) if getattr(row, "seed_key", None) in baseline_nested_ids[model.__name__]}
            for model in models[2:]
        }
        assert first_content_ids == {row.slug: row.id for row in db_session.scalars(select(Content).where(Content.slug.in_(first_content_ids)))}
        assert first_nested_ids == {
            model.__name__: {row.seed_key: (row.id, row.active) for row in db_session.scalars(select(model)) if getattr(row, "seed_key", None) in first_nested_ids[model.__name__]}
            for model in models[2:]
        }
        assert db_session.scalar(select(func.count()).select_from(ChecklistInstance)) == history_ids[0]
        preserved_item = db_session.get(ChecklistItemState, history_ids[1])
        preserved_user = db_session.get(UserContentState, history_ids[2])
        assert preserved_item is not None and preserved_item.completed is True
        assert preserved_item.note == "V1.7C completion history marker"
        assert preserved_user is not None and preserved_user.note == "V1.7C user state marker"
