from __future__ import annotations

import json
from pathlib import Path

from sqlalchemy import select

from app.models import Content, ContentRequirement, Evidence, ScheduleRule


DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def _contents() -> dict[str, dict]:
    rows = json.loads((DATA_DIR / "seed_contents.json").read_text(encoding="utf-8"))
    return {row["slug"]: row for row in rows}


def _requirement(row: dict, seed_key: str) -> dict:
    return next(item for item in row.get("requirements", []) if item["seed_key"] == seed_key)


def _schedule(row: dict, seed_key: str) -> dict:
    return next(item for item in row.get("schedules", []) if item["seed_key"] == seed_key)


def test_black_shrine_uses_sunday_cycle_and_current_attempt_counts() -> None:
    rows = _contents()
    for slug in ("black-shrine-donghae-weekly", "black-shrine-hwanghae-weekly"):
        row = rows[slug]
        attempts = _requirement(row, f"{slug}.attempts")["structured_value"]
        assert attempts["weekly_attempts"] == 5
        reset = _schedule(row, f"{slug}.attempt-reset")
        payout = _schedule(row, f"{slug}.reward-payout")
        assert (reset["weekday"], reset["time_local"]) == (6, "00:00")
        assert payout["weekday"] == 6
        assert all(schedule.get("weekday") != 3 for schedule in row["schedules"])
        reward_text = " ".join(item.get("notes", "") for item in row["rewards"])
        assert "흑정령의 선물함" in reward_text
        assert "누적" in reward_text


def test_blood_altar_separates_entry_challenge_and_reward() -> None:
    row = _contents()["blood-altar"]
    entry = _requirement(row, "blood-altar.entry-limit")["structured_value"]
    challenge = _requirement(row, "blood-altar.challenge-allowance")["structured_value"]
    reward = _requirement(row, "blood-altar.weekly-reward-rule")["structured_value"]
    assert entry["weekly_entry_limit"] is None
    assert challenge["party_challenge_allowance"] == 10
    assert reward == {"family_weekly_reward_limit": 1, "basis": "highest_stage", "cumulative": False}
    payout = _schedule(row, "blood-altar.reward-payout")
    assert (payout["weekday"], payout["time_local"]) == (6, "00:00")
    active_text = json.dumps(row, ensure_ascii=False)
    assert "weekly_entry_limit\": 1" not in active_text


def test_atoraxxion_has_one_current_reward_cycle_without_stale_branches() -> None:
    row = _contents()["atoraxxion-weekly"]
    value = _requirement(row, "atoraxxion-weekly.reward-rule")["structured_value"]
    assert value == {
        "weekly_reward_per_region": 1,
        "separate_season_branch": False,
        "dawn_key_required": False,
    }
    assert len(row["steps"]) == 4


def test_dark_rift_is_six_independent_120_hour_cycles() -> None:
    row = _contents()["dark-rift-cycle"]
    bosses = _requirement(row, "dark-rift-cycle.bosses")["structured_value"]
    assert bosses["boss_count"] == 6
    assert len(bosses["bosses"]) == 6
    respawn = _schedule(row, "dark-rift-cycle.respawn")
    assert respawn["recurrence_type"] == "rolling"
    assert "120시간" in respawn["notes"]
    assert all(schedule.get("weekday") != 3 for schedule in row["schedules"])
    cron = next(item for item in row["rewards"] if item["seed_key"] == "dark-rift-cycle.cron-per-boss")
    assert (cron["amount"], cron["unit"]) == (100, "개/우두머리")


def test_garmoth_reward_cap_and_spawn_are_separate() -> None:
    row = _contents()["garmoth"]
    cap = _requirement(row, "garmoth.weekly-reward-cap")["structured_value"]
    assert cap["weekly_reward_cap"] == 3
    reset = _schedule(row, "garmoth.attempt-reset")
    spawn = _schedule(row, "garmoth.world-boss-spawn")
    assert (reset["weekday"], reset["time_local"]) == (3, "00:00")
    assert (spawn["rule_type"], spawn["recurrence_type"]) == ("spawn", "scheduled")


def test_no_active_morning_land_world_boss_weekly_content() -> None:
    rows = _contents()
    assert "morning-land-world-boss-weekly" not in rows
    active_text = " ".join(
        json.dumps(row, ensure_ascii=False)
        for row in rows.values()
        if row.get("status", "active") == "active"
    )
    assert "아침의 나라 월드 우두머리 주간 의뢰" not in active_text


def test_edania_is_one_boss_and_thursday_reset() -> None:
    row = _contents()["edania-boss-weekly"]
    assert _requirement(row, "edania-boss-weekly.one-boss")["structured_value"]["weekly_boss_limit"] == 1
    reset = _schedule(row, "edania-boss-weekly.quest-reset")
    assert (reset["weekday"], reset["time_local"]) == (3, "00:00")


def test_infinite_potion_all_six_use_current_targets() -> None:
    row = _contents()["infinite-potion-weeklies"]
    availability = _requirement(row, "infinite-potion-weeklies.availability")["structured_value"]
    assert availability == {"quest_count": 6, "all_available": True, "choose_only_one": False}
    assert [step["description"] for step in row["steps"]] == [
        "나반 초원 몬스터 250마리 및 부드러운 페리의 깃털 250개",
        "숲 로나로스 1,000마리",
        "만샤움 1,000마리",
        "트쉬라 폐허 1,500마리",
        "가크툼 1,500마리",
        "셰레칸의 묘 1,000마리",
    ]


def test_dream_horse_weekly_choice_is_not_double_counted() -> None:
    row = _contents()["dream-horse-material-routines"]
    choice = _requirement(row, "dream-horse-material-routines.fern-weekly-choice")["structured_value"]
    assert choice["mutually_exclusive"] is True
    assert choice["total_reward"] == 50
    assert len(choice["quests"]) == 2


def test_imperial_delivery_has_independent_pools_and_two_clocks() -> None:
    row = _contents()["imperial-crafting-delivery-daily"]
    pools = _requirement(row, "imperial-crafting-delivery-daily.independent-pools")["structured_value"]
    assert pools == {"cooking_pool": "independent", "alchemy_pool": "independent", "combined_quota": False}
    reset = _schedule(row, "imperial-crafting-delivery-daily.personal-reset")
    stock = _schedule(row, "imperial-crafting-delivery-daily.server-stock-refresh")
    assert (reset["recurrence_type"], reset["time_local"]) == ("daily", "00:00")
    assert (stock["rule_type"], stock["recurrence_type"]) == ("stock_refresh", "interval")
    assert _requirement(row, "imperial-crafting-delivery-daily.server-stock")["structured_value"]["refresh_interval_hours"] == 3


def test_imported_routine_semantics_and_superseded_history(session) -> None:
    assert session.scalar(select(Content).where(Content.slug == "dark-rift-cycle")) is not None
    rolling = session.scalar(
        select(ScheduleRule).where(ScheduleRule.seed_key == "dark-rift-cycle.respawn")
    )
    assert (rolling.rule_type, rolling.recurrence_type) == ("respawn", "rolling")
    allowance = session.scalar(
        select(ContentRequirement).where(
            ContentRequirement.seed_key == "blood-altar.challenge-allowance"
        )
    )
    assert allowance.structured_value["party_challenge_allowance"] == 10
    stale = list(
        session.scalars(
            select(Evidence).where(
                Evidence.seed_key.in_(
                    [
                        "blood-altar.history.challenge-five::blood-altar-guide",
                        "black-shrine-donghae-weekly.history.manual-expiry::black-shrine-donghae-guide",
                    ]
                )
            )
        )
    )
    assert len(stale) == 2
    assert all(item.verification_status == "superseded" and not item.active for item in stale)
