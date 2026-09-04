from __future__ import annotations

import json
from pathlib import Path

from sqlalchemy import select

from app.models import Content, ContentRequirement, Evidence, ScheduleRule


DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def _content(session, slug: str) -> Content:
    return session.scalar(select(Content).where(Content.slug == slug))


def _requirement(session, seed_key: str) -> ContentRequirement:
    return session.scalar(
        select(ContentRequirement).where(ContentRequirement.seed_key == seed_key)
    )


def test_family_life_levels_are_summed_and_share_guru_caps(session) -> None:
    scope = _requirement(session, "life-family-levels.family-scope").structured_value
    aggregation = _requirement(
        session, "life-family-levels.exp-aggregation"
    ).structured_value
    caps = _requirement(session, "life-family-levels.progression-cap").structured_value

    assert scope["scope"] == "family"
    assert scope["skill_count"] == 11
    assert aggregation["aggregation"] == "sum_all_characters"
    assert aggregation["disallowed_interpretation"] == "highest_character_only"
    assert caps["max_progression_level"] == "Guru 100"
    assert caps["mastery_growth_cap_by_level"] == "Guru 50"
    assert caps["guru_51_to_100_additional_effect"] is False


def test_life_mastery_uses_current_cap_and_guru_50_total(session) -> None:
    cap = _requirement(session, "life-mastery-foundation.effective-cap").structured_value
    levels = _requirement(
        session, "life-mastery-foundation.level-breakpoints"
    ).structured_value

    assert cap == {"maximum_effective_mastery": 3000}
    assert {row["level"]: row["mastery"] for row in levels["breakpoints"]}[
        "Guru 50"
    ] == 800
    assert levels["guru_51_to_100_additional_mastery"] == 0

    legacy = session.scalar(
        select(Evidence).where(
            Evidence.seed_key
            == "life-mastery-foundation.legacy.cap-2000::life-mastery-prione-2025-01-08"
        )
    )
    assert legacy.verification_status == "superseded"
    assert legacy.active is False


def test_life_exp_and_mastery_are_distinct_stats(session) -> None:
    values = _requirement(
        session, "life-mastery-foundation.stat-distinction"
    ).structured_value

    assert values["life_exp_bonus"] == "level_progression"
    assert values["life_mastery"] == "activity_specific_effects"
    assert values["same_stat"] is False
    buffs = _requirement(
        session, "life-mastery-foundation.common-buff-taxonomy"
    ).structured_value
    assert "life_exp" in buffs["categories"]
    assert "life_mastery" in buffs["categories"]
    assert buffs["event_buffs_included"] is False


def test_integrated_life_gear_separates_global_and_category_slots(session) -> None:
    family = _requirement(session, "life-common-gear.family-wide").structured_value
    global_slots = _requirement(
        session, "life-common-gear.global-slots"
    ).structured_value
    category_slots = _requirement(
        session, "life-common-gear.category-slots"
    ).structured_value
    concurrent = _requirement(
        session, "life-common-gear.combat-life-concurrent"
    ).structured_value

    assert family["scope"] == "family"
    assert family["same_effects_all_characters"] is True
    assert global_slots["slots"] == ["생활 액세서리", "생활 연금석", "청명의 보주"]
    assert global_slots["per_life_category_copies"] is False
    assert "채집 도구" in category_slots["gathering"]
    assert concurrent["combat_and_life_equipment_simultaneous"] is True
    assert concurrent["remove_combat_gear_for_life"] is False


def test_floamos_is_fixed_and_daily_exchange_has_reset_rule(session) -> None:
    properties = _requirement(session, "floamos-accessories.properties").structured_value
    acquisition = _requirement(
        session, "floamos-accessories.family-acquisition"
    ).structured_value
    exchange = _requirement(
        session, "floamos-accessories.daily-exchange"
    ).structured_value
    schedule = session.scalar(
        select(ScheduleRule).where(
            ScheduleRule.seed_key == "floamos-accessories.exchange-reset"
        )
    )

    assert properties["enhancement_allowed"] is False
    assert properties["equivalent_stats_to"] == "TRI Manos accessory"
    assert acquisition["family_limit"] == 1
    assert {row["amount"] for row in acquisition["turn_in_one_of"]} == {300}
    assert exchange["daily_limit"] == 1
    assert exchange["inputs"][1] == {"item": "응축된 마력의 검은 결정", "amount": 10}
    assert schedule.rule_type == "quest_reset"
    assert schedule.recurrence_type == "daily"


def test_prione_failure_and_failstack_rules_are_current(session) -> None:
    rules = _requirement(
        session, "prione-accessories.enhancement-rules"
    ).structured_value
    table = _requirement(
        session, "prione-accessories.enhancement-table"
    ).structured_value["rows"]

    assert rules["fixed_success_probability"] is True
    assert rules["failstack_applied"] is False
    assert rules["failstack_consumed_on_success"] is False
    assert rules["destroyed_on_failure"] is False
    assert rules["downgrade_on_failure"] is True
    assert rules["cron_prevents_downgrade"] is True
    assert rules["max_durability_loss_on_failure"] == 10
    assert len(table) == 10
    assert table[0] == {
        "from": "+0", "to": "I", "crystals": 15,
        "success_percent": 25, "cron": 0, "agris": 6,
    }
    assert table[-1]["success_percent"] == 7.5
    assert table[-1]["cron"] == 2810


def test_current_lightstone_rules_exclude_removed_combinations(session) -> None:
    scope = _requirement(
        session, "life-artifacts-lightstones.category-scope"
    ).structured_value
    combinations = _requirement(
        session, "life-artifacts-lightstones.current-combinations"
    ).structured_value
    activity = _requirement(
        session, "life-artifacts-lightstones.activity-selection"
    ).structured_value

    assert scope["common_effect_scope"] == "equipped_life_category_only"
    assert scope["applies_to_all_life_categories_simultaneously"] is False
    assert combinations["allowed_families"] == ["풀의 광명석", "오색빛 광명석"]
    assert combinations["old_fire_wind_recipes_current"] is False
    assert combinations["deleted_combinations"] == ["송곳니", "대장장이의 축복", "개운한 꿈"]
    assert len(combinations["representative_current_recipes"]) == 10
    assert all(
        all(stone.startswith(("풀의 광명석", "오색빛 광명석")) for stone in row["recipe"])
        for row in combinations["representative_current_recipes"]
    )
    assert activity["selection_basis"] == "actual_activity"
    assert activity["hunting_butchering"]["invalid"] == ["gathering_exp", "gathering_mastery"]


def test_life_alchemy_stones_use_equip_effect_without_durability(session) -> None:
    current = _requirement(
        session, "life-alchemy-stones.current-behavior"
    ).structured_value

    assert current["durability_removed"] is True
    assert current["recharge_required"] is False
    assert current["effect_mode"] == "on_equip"
    assert current["manual_activation_required"] is False

    stale_claims = session.scalars(
        select(Evidence).where(
            Evidence.seed_key.in_(
                [
                    "life-alchemy-stones.legacy.durability::life-unification-2026-09-02",
                    "life-alchemy-stones.legacy.manual-activation::life-unification-2026-09-02",
                ]
            )
        )
    ).all()
    assert len(stale_claims) == 2
    assert all(row.verification_status == "superseded" and not row.active for row in stale_claims)


def test_cheongmyeong_processing_and_enhancement_are_distinct(session) -> None:
    crystal = _requirement(session, "cheongmyeong-orb.crystal-recipe").structured_value
    conversion = _requirement(
        session, "cheongmyeong-orb.reversible-conversion"
    ).structured_value
    enhancement = _requirement(session, "cheongmyeong-orb.enhancement").structured_value

    assert crystal["method"] == "가열하기"
    assert crystal["output"] == {"item": "청명의 결정", "amount": 1}
    assert conversion["method"] == "간이연금"
    assert conversion["reversible"] is True
    assert conversion["heating_for_crystal_to_orb"] is False
    assert enhancement["success_percent"] == 100
    assert [row["crystal_count"] for row in enhancement["rows"]] == [
        1, 1, 1, 1, 1, 1, 6, 6, 6, 6, 20, 20, 20, 20, 20, 20
    ]
    assert enhancement["rows"][-1]["life_exp_percent"] == 90


def test_dawn_crystals_are_removed_and_compensation_is_historical(session) -> None:
    replacement = _requirement(
        session, "cheongmyeong-orb.replacement"
    ).structured_value
    compensation = _requirement(
        session, "cheongmyeong-orb.migration-compensation"
    ).structured_value

    assert replacement["current_equipment"] == "청명의 보주"
    assert replacement["removed_equipment_active_count"] == 0
    assert len(replacement["removed_current_equipment"]) == 3
    assert compensation["historical_only"] is True
    assert compensation["general_acquisition_method"] is False
    assert compensation["compensation"] == [
        {"removed": "진", "crystals": 25},
        {"removed": "본", "crystals": 5},
        {"removed": "원", "crystals": 1},
    ]


def test_energy_separates_family_max_from_character_current(session) -> None:
    pools = _requirement(session, "energy-foundation.pool-scopes").structured_value
    regen = _requirement(
        session, "energy-foundation.natural-regeneration"
    ).structured_value
    gathering = _requirement(
        session, "energy-foundation.gathering-change"
    ).structured_value

    assert pools["base_max_energy"] == 30
    assert pools["maximum_energy_scope"] == "family_shared"
    assert pools["current_energy_scope"] == "per_character"
    assert pools["globally_shared_current_pool"] is False
    assert regen["online"] == {"amount": 1, "minutes": 3}
    assert regen["offline"] == {"amount": 1, "hours": 1}
    assert gathering["no_energy_consumption_chance_increase_percentage_points"] == 10
    assert gathering["maximum_reached_at"] == "Professional 3"
    assert gathering["exact_maximum_percent"] is None


def test_v16f_seed_has_no_unknown_references_or_duplicate_semantic_content() -> None:
    sources = json.loads((DATA_DIR / "seed_sources.json").read_text(encoding="utf-8"))
    contents = json.loads((DATA_DIR / "seed_contents.json").read_text(encoding="utf-8"))
    source_ids = {row["id"] for row in sources}
    content_slugs = {row["slug"] for row in contents}

    assert len(source_ids) == len(sources)
    assert len(content_slugs) == len(contents)
    assert "life-integrated-equipment" not in content_slugs
    assert "life-common-gear" in content_slugs

    for content in contents:
        for claim in content.get("evidence", []):
            assert set(claim["source_ids"]) <= source_ids
            entity_key = claim.get("entity_seed_key", content["slug"])
            assert entity_key == content["slug"] or entity_key.startswith(
                f"{content['slug']}."
            )
        for relation in content.get("relations", []):
            assert relation["to_content_slug"] in content_slugs


def test_existing_v16e_contents_remain_active(session) -> None:
    protected = {
        "carrack-advance",
        "barter-current-system",
        "rinbach-colony",
        "dream-horse-material-routines",
        "imperial-crafting-delivery-daily",
    }

    rows = session.scalars(select(Content).where(Content.slug.in_(protected))).all()
    assert {row.slug for row in rows} == protected
    assert all(row.status == "active" for row in rows)
