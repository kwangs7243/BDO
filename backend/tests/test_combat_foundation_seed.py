from __future__ import annotations

import json
from pathlib import Path

from sqlalchemy import select

from app.models import Content, ContentRelation, ContentRequirement, ContentSection, Evidence, Source
from app.seed import import_seed


DATA_DIR = Path(__file__).resolve().parents[2] / "data"


V17A_SOURCE_IDS = {
    "combat-stat-bonus-guide",
    "combat-system-rework-2025-07-23",
    "crystal-guide",
    "item-drop-rate-guide",
    "item-drop-applicability-guide",
    "item-drop-benefits-history",
    "agris-fever-guide",
    "church-buff-guide",
    "camp-church-rework-2025-12-30",
    "combat-gear-a-to-j-2026-04-22",
    "hyper-boost-gear-strategy-2026-08-19",
    "softcap-strategy-2025-07-29",
    "grind-selection-strategy-2025-11-18",
    "combat-guide-index-2026-02-28",
}

V17A_CONTENT_SLUGS = {
    "combat-stat-foundation",
    "sheet-vs-final-stats",
    "sheet-ap-bonus-table",
    "sheet-dp-bonus-table",
    "monster-extra-ap",
    "race-extra-ap",
    "accuracy-evasion-current-system",
    "special-attack-system",
    "grind-zone-attack-cap",
    "grind-zone-recommendation-system",
    "combat-crystal-system",
    "pve-crystal-strategy",
    "combat-artifacts",
    "combat-lightstones",
    "pve-lightstone-strategy",
    "combat-buff-foundation",
    "church-buff-current",
    "camp-combat-buffs",
    "combat-food-elixir-perfume",
    "item-drop-rate-system",
    "loot-scroll-system",
    "item-drop-rate-cap",
    "ecology-family-drop-bonus",
    "agris-fever",
    "combat-gear-progression-strategy",
    "grind-setup-strategy-foundation",
}


def _requirement(session, seed_key: str) -> dict:
    row = session.scalar(
        select(ContentRequirement).where(ContentRequirement.seed_key == seed_key)
    )
    assert row is not None
    return row.structured_value


def _evidence(session, seed_key: str, source_id: str) -> Evidence:
    row = session.scalar(
        select(Evidence).where(Evidence.seed_key == f"{seed_key}::{source_id}")
    )
    assert row is not None
    return row


def test_v17a_seed_json_is_unique_and_expected_rows_exist() -> None:
    sources = json.loads((DATA_DIR / "seed_sources.json").read_text(encoding="utf-8"))
    contents = json.loads((DATA_DIR / "seed_contents.json").read_text(encoding="utf-8"))
    source_ids = [row["id"] for row in sources]
    source_urls = [row["url"] for row in sources]
    slugs = [row["slug"] for row in contents]

    assert len(source_ids) == len(set(source_ids))
    assert len(source_urls) == len(set(source_urls))
    assert len(slugs) == len(set(slugs))
    assert len(sources) >= 112
    assert len(contents) >= 166
    assert V17A_SOURCE_IDS <= set(source_ids)
    assert V17A_CONTENT_SLUGS <= set(slugs)


def test_ap_bonus_table_current_boundaries(session) -> None:
    value = _requirement(session, "sheet-ap-bonus-table.current")
    bonus = value["bonus_ap_breakpoints"]
    monster = value["monster_extra_ap_benchmarks"]
    formulas = value["monster_extra_ap_formula"]

    assert bonus["309"] == 200
    assert bonus["401"] == 249
    assert bonus["449"] == 297
    assert monster == {"309": 0, "310": 8, "400": 728, "401": 744, "450": 1528}
    assert formulas[0] == {"sheet_ap_min": 100, "sheet_ap_max": 309, "formula": "0"}
    assert formulas[1]["formula"] == "(sheet_ap - 309) * 8"
    assert formulas[2]["formula"] == "728 + (sheet_ap - 400) * 16"


def test_dp_bonus_table_current_boundaries(session) -> None:
    value = _requirement(session, "sheet-dp-bonus-table.current")
    rate = value["damage_reduction_rate_breakpoints"]
    flat = value["flat_damage_reduction_breakpoints"]

    assert rate["401"] == 30
    assert flat["400"] == 81
    assert flat["481"] == 91
    assert flat["486"] == 92
    assert flat["531"] == 101
    assert 89 not in flat.values()


def test_accuracy_race_special_attack_and_zone_cap_rules(session) -> None:
    accuracy = _requirement(session, "accuracy-evasion-current-system.current")
    race = _requirement(session, "race-extra-ap.current")
    special = _requirement(session, "special-attack-system.stacking")
    cap = _requirement(session, "grind-zone-attack-cap.excess")

    assert accuracy["standalone_accuracy_percent"] is False
    assert accuracy["standalone_evasion_percent"] is False
    assert accuracy["legacy_one_percent_converted_to_points"] == 4
    assert race["legacy_pve_reduction_active"] is False
    assert special["different_special_attacks_can_stack"] is True
    assert cap["excess_ap_applied_percent"] == 5


def test_grind_zone_recommendation_uses_final_ap_without_defense(session) -> None:
    value = _requirement(session, "grind-zone-recommendation-system.current")

    assert value["basis"] == "final_ap"
    assert value["range_minus"] == value["range_plus"] == 50
    assert set(value["includes"]) == {"monster_extra_ap", "race_extra_ap"}
    assert value["defense_filter_included"] is False


def test_crystal_artifact_and_lightstone_systems(session) -> None:
    capacity = _requirement(session, "combat-crystal-system.capacity")
    removal = _requirement(session, "combat-crystal-system.removal")
    slots = _requirement(session, "combat-artifacts.slots")
    kabua = _requirement(session, "combat-artifacts.kabua")
    guiding = _requirement(session, "combat-artifacts.guiding")

    assert capacity == {
        "knowledge_role": "fact",
        "crystal_bag_capacity": 50,
        "preset_count": 5,
        "group_limits_apply": True,
    }
    assert removal["extraction_preserves"] is True
    assert removal["direct_removal_destroys"] is True
    assert slots["artifact_slots"] == 2
    assert slots["total_lightstone_sockets"] == 4
    assert (kabua["ap"], kabua["accuracy"], kabua["max_hp"], kabua["max_stamina"]) == (
        7,
        20,
        100,
        75,
    )
    assert (guiding["extra_ap"], guiding["accuracy"], guiding["max_hp"]) == (3, 5, 250)


def test_current_buff_rules_and_legacy_claims(session) -> None:
    church = _requirement(session, "church-buff-current.effects")
    prices = _requirement(session, "church-buff-current.duration-price")
    cron = _requirement(session, "combat-food-elixir-perfume.simple-cron-current")

    assert church == {
        "knowledge_role": "fact",
        "ap": 8,
        "accuracy": 8,
        "damage_reduction": 8,
        "max_hp": 150,
        "combat_exp_percent": 15,
        "skill_exp_percent": 15,
    }
    assert prices["options"] == [
        {"duration_minutes": 120, "silver": 3000000},
        {"duration_minutes": 300, "silver": 10000000},
    ]
    assert cron["back_attack_damage_percent"] == 5
    assert cron["critical_damage_percent"] == 5
    assert cron["down_attack_damage_percent"] is None

    old_church = _evidence(
        session,
        "church-buff-current.claim.legacy-three",
        "camp-church-rework-2025-12-30",
    )
    old_cron = _evidence(
        session,
        "combat-food-elixir-perfume.claim.simple-cron-legacy",
        "combat-system-rework-2025-07-23",
    )
    assert old_church.verification_status == "superseded" and not old_church.active
    assert old_cron.verification_status == "superseded" and not old_cron.active


def test_drop_rate_scroll_caps_and_family_bonuses(session) -> None:
    stages = _requirement(session, "loot-scroll-system.stages")
    caps = _requirement(session, "item-drop-rate-cap.current")
    ecology = _requirement(session, "ecology-family-drop-bonus.ecology")
    fame = _requirement(session, "ecology-family-drop-bonus.family-fame")

    assert stages["same_probability_bonus_between_stages"] is True
    assert stages["exact_probability_bonus_percent"] is None
    assert stages["stages"] == [
        {"stage": 1, "quantity_bonus_percent": 50},
        {"stage": 2, "quantity_bonus_percent": 100},
    ]
    assert caps["overall_cap_percent"] == 400
    assert caps["ordinary_cap_percent"] == 300
    assert ecology["breakpoints"] == {
        "500": 5,
        "1000": 7,
        "1500": 10,
        "2000": 12,
        "3000": 14,
        "4000": 16,
        "5000": 18,
        "6000": 20,
        "7000": 23,
        "8000": 25,
        "9000": 27,
        "10000": 30,
    }
    assert fame == {
        "knowledge_role": "fact",
        "family_fame_threshold": 7000,
        "drop_rate_bonus_percent": 10,
    }


def test_agris_family_recovery_and_scope(session) -> None:
    unlock = _requirement(session, "agris-fever.unlock")
    base = _requirement(session, "agris-fever.base")
    enhanced = _requirement(session, "agris-fever.enhanced")
    scope = _requirement(session, "agris-fever.scope")

    assert unlock["minimum_level"] == 56 and unlock["family_shared"] is True
    assert base["max_points"] == 50000
    assert base["daily_recovery"] == 15000
    assert base["recovery_time"] == "06:00"
    assert base["timezone"] == "Asia/Seoul"
    assert enhanced["max_points"] == 100000
    assert enhanced["daily_recovery"] == 20000
    assert enhanced["trash_loot_quantity_bonus_percent"] == 150
    assert scope["trash_loot_quantity"] is True
    assert scope["rare_drop_probability"] is False


def test_strategy_sources_are_dated_and_not_used_as_numeric_fact_only(session) -> None:
    strategy_ids = {
        "combat-gear-a-to-j-2026-04-22",
        "hyper-boost-gear-strategy-2026-08-19",
        "softcap-strategy-2025-07-29",
        "grind-selection-strategy-2025-11-18",
    }
    for source_id in strategy_ids:
        source = session.get(Source, source_id)
        assert source is not None
        assert source.source_type == "community_strategy"
        assert source.published_at is not None

    for seed_key in (
        "pve-crystal-strategy.context",
        "pve-lightstone-strategy.context",
        "combat-gear-progression-strategy.context",
        "grind-setup-strategy-foundation.checkpoints",
    ):
        value = _requirement(session, seed_key)
        assert value["knowledge_role"] == "strategy"
        assert value["current_as_of"] == "2026-09-04"

    numeric_fact_claims = (
        "sheet-ap-bonus-table.claim.current",
        "sheet-dp-bonus-table.claim.current",
        "grind-zone-recommendation-system.claim.current",
        "combat-artifacts.claim.kabua",
        "church-buff-current.claim.effects",
        "loot-scroll-system.claim.stages",
        "item-drop-rate-cap.claim.current",
        "ecology-family-drop-bonus.claim.ecology",
        "agris-fever.claim.base",
    )
    evidence = session.scalars(
        select(Evidence).where(
            Evidence.seed_key.in_([f"{key}::{source}" for key in numeric_fact_claims for source in V17A_SOURCE_IDS | {"artifact-guide", "blood-altar-challenge-2026-07-15"}])
        )
    ).all()
    assert evidence
    by_claim: dict[str, list[Evidence]] = {}
    for row in evidence:
        by_claim.setdefault(row.seed_key.split("::", 1)[0], []).append(row)
    for claim in numeric_fact_claims:
        assert claim in by_claim
        assert any(session.get(Source, row.source_id).source_type.startswith("official") for row in by_claim[claim])


def test_inactive_historical_claims_are_preserved(session) -> None:
    historical = (
        ("sheet-ap-bonus-table.claim.legacy", "combat-stat-bonus-guide"),
        ("race-extra-ap.claim.legacy-limit", "combat-system-rework-2025-07-23"),
        ("accuracy-evasion-current-system.claim.legacy-percent", "combat-system-rework-2025-07-23"),
        ("church-buff-current.claim.legacy-three", "camp-church-rework-2025-12-30"),
        ("combat-food-elixir-perfume.claim.simple-cron-legacy", "combat-system-rework-2025-07-23"),
        ("item-drop-rate-cap.claim.legacy", "item-drop-benefits-history"),
    )
    for seed_key, source_id in historical:
        row = _evidence(session, seed_key, source_id)
        assert row.verification_status == "superseded"
        assert row.active is False

    event = _evidence(session, "combat-crystal-system.claim.no-break-event", "crystal-guide")
    assert event.verification_status == "needs_review"
    assert event.active is False


def test_v17a_stable_nested_ids_survive_reimport(session) -> None:
    before_content = {
        row.slug: row.id
        for row in session.scalars(select(Content).where(Content.slug.in_(V17A_CONTENT_SLUGS)))
    }
    before_nested = {
        model.__name__: {row.seed_key: row.id for row in session.scalars(select(model)) if row.seed_key}
        for model in (ContentRequirement, ContentSection, ContentRelation, Evidence)
    }

    import_seed(session, DATA_DIR)

    after_content = {
        row.slug: row.id
        for row in session.scalars(select(Content).where(Content.slug.in_(V17A_CONTENT_SLUGS)))
    }
    after_nested = {
        model.__name__: {row.seed_key: row.id for row in session.scalars(select(model)) if row.seed_key}
        for model in (ContentRequirement, ContentSection, ContentRelation, Evidence)
    }
    assert before_content == after_content
    assert before_nested == after_nested
