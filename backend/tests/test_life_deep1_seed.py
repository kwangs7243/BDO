from __future__ import annotations

import json
from pathlib import Path

from sqlalchemy import select

from app.models import Content, ContentRequirement, Evidence, ScheduleRule


DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def _content(session, slug: str) -> Content:
    row = session.scalar(select(Content).where(Content.slug == slug))
    assert row is not None
    return row


def _requirement(session, seed_key: str) -> ContentRequirement:
    row = session.scalar(
        select(ContentRequirement).where(ContentRequirement.seed_key == seed_key)
    )
    assert row is not None
    return row


def _evidence(session, seed_key: str) -> Evidence:
    row = session.scalar(select(Evidence).where(Evidence.seed_key == seed_key))
    assert row is not None
    return row


def test_v16g_seed_json_and_logical_content_are_unique() -> None:
    sources = json.loads((DATA_DIR / "seed_sources.json").read_text(encoding="utf-8"))
    contents = json.loads((DATA_DIR / "seed_contents.json").read_text(encoding="utf-8"))

    source_ids = [row["id"] for row in sources]
    source_urls = [row["url"] for row in sources]
    slugs = [row["slug"] for row in contents]
    assert len(source_ids) == len(set(source_ids))
    assert len(source_urls) == len(set(source_urls))
    assert len(slugs) == len(set(slugs))
    expected_sources = {
        "gathering-guide",
        "processing-guide",
        "processing-stone-history",
        "life-clothes-2025-08-27",
        "farming-guide",
        "farming-overhaul-2026-06-04",
        "farming-moles-2026-06-17",
        "old-moon-seed-pouch-2025-07-09",
        "fishing-basic-guide",
        "fishing-advanced-guide",
        "fish-freshness-2025-05-21",
        "fishing-improvement-history",
        "mystical-fish-tank-2023-08-02",
        "mystical-fish-tank-rules-2024-08-28",
        "fish-encyclopedia-2025-04-16",
    }
    expected_contents = {
        "gathering-current-system",
        "gathering-tools",
        "gathering-green-artisan-minigames",
        "gathering-special-drops",
        "processing-current-system",
        "mass-processing",
        "processing-stones-and-clothes",
        "farming-current-cycle",
        "farming-fences",
        "farming-seeds-harvest-breeding",
        "farming-moles",
        "old-moon-seed-pouch",
        "fishing-current-system",
        "auto-fishing",
        "fish-freshness-and-trade",
        "imperial-fishing-delivery",
        "mystical-fish-tank",
        "treasure-grade-fish",
        "fishing-encyclopedia-and-weekly-contest",
    }
    assert expected_sources <= set(source_ids)
    assert expected_contents <= set(slugs)


def test_magic_gathering_tool_suppresses_only_mastery_acquisition_probability(session) -> None:
    value = _requirement(session, "gathering-tools.magic").structured_value

    assert value["time_reduction_seconds"] == 11
    assert value["item_acquisition_chance_percent"] == 80
    assert value["mastery_acquisition_probability_applied"] is False
    assert value["mastery_entirely_disabled"] is False


def test_green_artisan_success_failure_and_valtarra_exclusion(session) -> None:
    result = _requirement(
        session, "gathering-green-artisan-minigames.result"
    ).structured_value
    exclusions = _requirement(
        session, "gathering-green-artisan-minigames.exclusions"
    ).structured_value

    assert result["success"] == {"energy": 10, "output_multiplier": 10}
    assert result["failure"] == {"energy": 1, "output": "normal_one_action"}
    assert exclusions["not_multiplied"] == ["발타라의 천안", "발타라의 추억"]


def test_buried_trace_reward_semantics(session) -> None:
    rewards = _requirement(
        session, "gathering-special-drops.buried-trace-rewards"
    ).structured_value["rewards"]
    by_name = {row["item"]: row for row in rewards}

    assert by_name["뾰족한 흑결정 조각"] == {
        "item": "뾰족한 흑결정 조각",
        "min": 15,
        "max": 22,
        "probability_percent": 100,
    }
    assert by_name["고대 정령의 가루"]["probability_percent"] == 50


def test_old_life_alchemy_activation_workflow_remains_inactive(session) -> None:
    stale = session.scalars(
        select(Evidence).where(
            Evidence.seed_key.in_(
                [
                    "life-alchemy-stones.legacy.durability::life-unification-2026-09-02",
                    "life-alchemy-stones.legacy.manual-activation::life-unification-2026-09-02",
                ]
            )
        )
    ).all()

    assert len(stale) == 2
    assert all(row.verification_status == "superseded" and not row.active for row in stale)


def test_processing_base_success_and_integrated_stone_are_current(session) -> None:
    base = _requirement(
        session, "processing-current-system.base-success"
    ).structured_value
    stone = _requirement(
        session, "processing-stones-and-clothes.integrated-stone"
    ).structured_value

    assert base == {"base_success_percent": 70, "globally_increased_above_70": False}
    assert stone["integrated"] is True
    assert stone["old_six_separate_stones_required"] is False
    assert len(stone["methods"]) == 6


def test_mass_processing_and_current_clothes(session) -> None:
    rows = _requirement(session, "mass-processing.breakpoints").structured_value[
        "breakpoints"
    ]
    amounts = {row["mastery"]: row["cycles"] for row in rows}
    clothes = _requirement(
        session, "processing-stones-and-clothes.current-clothes"
    ).structured_value
    success = _requirement(
        session, "processing-stones-and-clothes.success-table"
    ).structured_value["rows"]

    assert amounts[2000] == 250
    assert amounts[3000] == 315
    assert clothes["progression"] == ["로기아", "카르타", "마노스"]
    assert clothes["silver_embroidered_craftsman_clothes_active"] is False
    assert success[-1] == {
        "enhancement": "V",
        "Manos": 40,
        "Karta": 33,
        "Loggia": 28,
    }


def test_legacy_processing_progressions_are_superseded(session) -> None:
    stale = session.scalars(
        select(Evidence).where(
            Evidence.seed_key.in_(
                [
                    "processing-stones-and-clothes.legacy.separate-stones::processing-stone-history",
                    "processing-stones-and-clothes.legacy.silver-clothes::life-clothes-2025-08-27",
                ]
            )
        )
    ).all()

    assert len(stale) == 2
    assert all(row.verification_status == "superseded" and not row.active for row in stale)


def test_farming_growth_moisture_and_deleted_fertilizers(session) -> None:
    growth = _requirement(
        session, "farming-current-cycle.growth-time"
    ).structured_value
    moisture = _requirement(
        session, "farming-current-cycle.moisture"
    ).structured_value
    fertilizers = _requirement(
        session, "farming-current-cycle.fertilizers"
    ).structured_value

    assert growth == {
        "suitable_hours": 20,
        "unsuitable_hours": 21,
        "very_unsuitable_hours": 22,
    }
    assert moisture["rate_relative_to_previous"] == 0.2
    assert fertilizers["active_usable_item_count"] == 0
    assert len(fertilizers["deleted"]) == 3


def test_farming_output_multipliers_and_fence_removal(session) -> None:
    output = _requirement(
        session, "farming-seeds-harvest-breeding.output-overhaul"
    ).structured_value
    removal = _requirement(
        session, "farming-fences.inactivity-removal"
    ).structured_value
    old = _evidence(
        session,
        "farming-fences.legacy.inactivity-14-days::farming-overhaul-2026-06-04",
    )

    assert output["guaranteed_items_quantity_multiplier"] == 5
    assert output["probabilistic_items"] == {
        "probability_multiplier": 2,
        "quantity_multiplier": 2.5,
    }
    assert output["designated_special_crops"]["quantity_multiplier"] == 3
    assert removal["current_days"] == 28
    assert removal["legacy_active"] is False
    assert old.verification_status == "superseded" and not old.active


def test_mole_latest_evidence_takes_precedence_without_absolute_inference(session) -> None:
    latest = _requirement(
        session, "farming-moles.latest-adjustment"
    ).structured_value
    old = _evidence(
        session,
        "farming-moles.legacy.june-04-reward::farming-overhaul-2026-06-04",
    )

    assert latest["latest_evidence_date"] == "2026-06-17"
    assert latest["state"] == "increased"
    assert latest["absolute_counts"] is None
    assert len(latest["blush_leaf_relative_increase_percent"]) == 5
    assert old.verification_status == "superseded" and not old.active


def test_old_moon_seed_pouch_keeps_transfer_before_planting(session) -> None:
    current = _requirement(
        session, "old-moon-seed-pouch.current-planting"
    ).structured_value
    planned_row = _requirement(
        session, "old-moon-seed-pouch.planned-direct-planting"
    )
    planned = planned_row.structured_value
    planned_evidence = _evidence(
        session,
        "old-moon-seed-pouch.requirement.planned-direct-planting::farming-overhaul-2026-06-04",
    )

    assert current["must_transfer_to_character_inventory"] is True
    assert current["direct_planting_current"] is False
    assert planned["direct_planting"] is False
    assert planned["confirmation_status"] == "unconfirmed_live"
    assert planned_row.active is False
    assert planned_evidence.verification_status == "needs_review"
    assert planned_evidence.active is False


def test_fish_freshness_uses_current_durations_and_preserves_history(session) -> None:
    durations = _requirement(
        session, "fish-freshness-and-trade.durations"
    ).structured_value
    old_standard = _evidence(
        session,
        "fish-freshness-and-trade.legacy.standard-24h::fish-freshness-2025-05-21",
    )
    old_odyllita = _evidence(
        session,
        "fish-freshness-and-trade.legacy.odyllita-36h::fish-freshness-2025-05-21",
    )

    assert durations["standard_hours"] == 48
    assert durations["odyllita_hours"] == 60
    assert durations["mountain_of_eternal_winter_hours"] is None
    assert all(
        row.verification_status == "superseded" and not row.active
        for row in (old_standard, old_odyllita)
    )


def test_normal_auto_fishing_timer_is_not_sailor_timer(session) -> None:
    timer = _requirement(session, "auto-fishing.timer").structured_value
    distinct = _requirement(
        session, "auto-fishing.distinct-from-sailor"
    ).structured_value

    assert timer == {"base_completion_seconds": 180, "minimum_seconds": 60}
    assert distinct["same_timer_system_as_carrack_sailor_fishing"] is False
    assert distinct["normal_timer_reductions_apply_to_sailor_system"] is False
    assert _content(session, "carrack-sailor-fishing").status == "active"


def test_fish_tank_and_removed_shell_requirement(session) -> None:
    duration = _requirement(
        session, "mystical-fish-tank.duration"
    ).structured_value
    acquisition = _requirement(
        session, "mystical-fish-tank.acquisition"
    ).structured_value
    legacy = session.scalars(
        select(Evidence).where(
            Evidence.seed_key.like("mystical-fish-tank.legacy.four-shells::%")
        )
    ).all()

    assert duration["guarantee_duration_multiplier"] == 5
    assert acquisition["iridescent_shells_required"] is False
    assert acquisition["shell_amount"] == 0
    assert len(legacy) == 2
    assert all(row.verification_status == "superseded" and not row.active for row in legacy)


def test_imperial_fishing_and_treasure_fish_rules(session) -> None:
    price = _requirement(
        session, "imperial-fishing-delivery.price"
    ).structured_value
    quota = _requirement(
        session, "imperial-fishing-delivery.quota"
    ).structured_value
    treasure = _requirement(
        session, "treasure-grade-fish.imperial"
    ).structured_value
    schedule = session.scalar(
        select(ScheduleRule).where(
            ScheduleRule.seed_key == "imperial-fishing-delivery.quota-refresh"
        )
    )

    assert price["base_price_percent"] == 250
    assert quota["refresh_interval_hours"] == 3
    assert schedule is not None
    assert schedule.rule_type == "stock_refresh"
    assert schedule.recurrence_type == "interval"
    assert treasure["imperial_fishing_delivery_allowed"] is False


def test_fishing_mastery_3000_is_contribution_not_global_final_probability(session) -> None:
    mastery = _requirement(
        session, "fishing-current-system.mastery"
    ).structured_value
    values = {
        row["mastery"]: row["treasure_group_contribution_percent"]
        for row in mastery["breakpoints"]
    }

    assert values[3000] == 6.25
    assert mastery["interpretation"] == "mastery_contribution"
    assert mastery["not_global_final_probability"] is True


def test_weekly_fishing_contest_keeps_reset_settlement_and_payout_distinct(session) -> None:
    schedules = session.scalars(
        select(ScheduleRule).where(
            ScheduleRule.seed_key.like(
                "fishing-encyclopedia-and-weekly-contest.%"
            )
        )
    ).all()
    by_type = {row.rule_type: row for row in schedules}

    assert set(by_type) == {"content_schedule", "record_settlement", "reward_payout"}
    assert by_type["content_schedule"].weekday == 0
    assert by_type["record_settlement"].weekday == 6
    assert by_type["reward_payout"].weekday == 6
