from __future__ import annotations

import json
from pathlib import Path

from sqlalchemy import select

from app.models import Content, ContentRequirement, Evidence


DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def _requirement(session, seed_key: str) -> dict:
    row = session.scalar(
        select(ContentRequirement).where(ContentRequirement.seed_key == seed_key)
    )
    assert row is not None
    return row.structured_value


def _evidence(session, seed_key: str) -> Evidence:
    row = session.scalar(select(Evidence).where(Evidence.seed_key == seed_key))
    assert row is not None
    return row


def test_v16h_seed_json_is_unique_and_complete() -> None:
    sources = json.loads((DATA_DIR / "seed_sources.json").read_text(encoding="utf-8"))
    contents = json.loads((DATA_DIR / "seed_contents.json").read_text(encoding="utf-8"))
    expected = {
        "cooking-current-system", "cooking-mastery-effects",
        "cooking-mass-production", "witch-delicacy",
        "cooking-growth-surprise-quest", "alchemy-current-system",
        "alchemy-mastery-effects", "alchemy-products-and-byproducts",
        "alchemy-growth-surprise-quest", "alchemy-imperial-current",
        "alchemy-stone-current-progression", "alchemy-stone-growth",
        "training-current-system", "training-mastery-effects",
        "wild-horse-capture", "horse-breeding-exchange",
        "horse-imperial-delivery", "courser-system",
        "dream-horse-awakening", "mythical-dream-horse",
        "training-growth-surprise-quest", "hunting-current-system",
        "hunting-mastery-effects", "hunting-firearms", "sniper-hunting",
        "marni-sniper-rifle", "group-hunting-whale-khalk",
        "hunting-growth-surprise-quest",
    }
    expected_sources = {
        "alchemy-basic-guide",
        "alchemy-guide",
        "alchemy-stone-guide",
        "alchemy-products-2024-03-20",
        "training-guide",
        "dream-horse-awakening-guide",
        "rare-wild-horses-2025-12-23",
        "hunting-guide",
        "hunting-enhancement-guide",
        "sniper-reward-rework-2023-05-03",
        "marni-sniper-crafting-2026-03-25",
        "marni-sniper-enhancement-2026-04-01",
    }

    assert len(sources) == len({row["id"] for row in sources})
    assert len(sources) == len({row["url"] for row in sources})
    assert len(contents) == len({row["slug"] for row in contents})
    assert expected_sources <= {row["id"] for row in sources}
    assert expected <= {row["slug"] for row in contents}


def test_cooking_minimum_time_and_mass_cooking(session) -> None:
    minimum = _requirement(session, "cooking-current-system.minimum-time")
    trigger = _requirement(session, "cooking-mass-production.trigger")
    batch = _requirement(session, "cooking-mass-production.batch")

    assert minimum["seconds"] == 1
    assert trigger["continuous_crafts"] == 10
    assert batch == {
        "ingredient_crafts_consumed": 10,
        "result_crafts_produced": 10,
        "utensil_durability_consumed": 1,
    }


def test_cooking_mastery_and_surprise_history(session) -> None:
    assert _requirement(session, "cooking-mastery-effects.mass-at-3000")["percent"] == 100
    assert _requirement(session, "cooking-mastery-effects.max-base-result")["percent"] == 76.45
    assert _requirement(session, "cooking-growth-surprise-quest.rules")["daily_limit"] is None
    stale = _evidence(
        session,
        "cooking-growth-surprise-quest.claim.legacy-pickled-soldiers"
        "::ocean-iliya-consolidation-2025-05-14",
    )
    assert stale.verification_status == "superseded" and not stale.active


def test_existing_imperial_delivery_content_remains_active(session) -> None:
    content = session.scalar(
        select(Content).where(Content.slug == "imperial-crafting-delivery-daily")
    )
    assert content is not None and content.status == "active"


def test_alchemy_mastery_values_are_separate(session) -> None:
    values = {
        "max": _requirement(session, "alchemy-mastery-effects.max-result")["percent"],
        "normal": _requirement(session, "alchemy-mastery-effects.normal-extra")["percent"],
        "special": _requirement(session, "alchemy-mastery-effects.special-extra")["percent"],
        "rare": _requirement(session, "alchemy-mastery-effects.rare-extra")["percent"],
    }
    assert values == {"max": 62.5, "normal": 3.83, "special": 2.98, "rare": 0.36}


def test_alchemy_stone_current_progression_and_failure_rules(session) -> None:
    stages = _requirement(session, "alchemy-stone-current-progression.stages")
    rules = _requirement(session, "alchemy-stone-current-progression.rules")

    assert [row["name"] for row in stages["stages"]] == [
        "imperfect", "sturdy", "sharp", "resplendent", "splendid", "shining"
    ]
    assert stages["removed"] == ["rough", "polished"]
    assert rules["failure_downgrade"] is False
    assert rules["failure_destruction"] is False
    assert rules["ancient_anvil_per_type"] == ["destruction", "protection", "life"]


def test_alchemy_stone_growth_table_and_essence(session) -> None:
    essence = _requirement(session, "alchemy-stone-current-progression.essence")
    table = _requirement(session, "alchemy-stone-growth.table")

    assert "growth" in essence["uses"]
    assert table["polish_percent"] == 150
    assert table["rows"][0]["success_percent"] == 55.055
    assert table["rows"][-1] == {
        "from": "splendid", "to": "shining", "success_percent": 0.4005,
        "ancient_anvil": 250, "full_sky_essence": 30,
    }


def test_alchemy_legacy_claims_are_inactive(session) -> None:
    keys = [
        "alchemy-growth-surprise-quest.claim.legacy-dalishain"
        "::ocean-iliya-consolidation-2025-05-14",
        "alchemy-stone-current-progression.claim.legacy-stages::alchemy-stone-guide",
        "alchemy-stone-current-progression.claim.legacy-failure::alchemy-stone-guide",
    ]
    rows = [_evidence(session, key) for key in keys]
    assert all(row.verification_status == "superseded" and not row.active for row in rows)


def test_imperial_alchemy_uses_current_packaging_values(session) -> None:
    tiers = _requirement(session, "alchemy-imperial-current.table")["tiers"]

    assert ["resurrection_elixir", 18] in tiers["apprentice"]
    assert ["springing_winnie_spirit_elixir", 4] in tiers["professional"]
    assert ["strong_looney_spirit_elixir", 3] in tiers["artisan"]
    assert ["fallen_metal_armor_elixir", 2] in tiers["guru"]


def test_training_mastery_and_imperial_delivery(session) -> None:
    assert _requirement(session, "training-mastery-effects.capture")["increase_percent"] == 43.75
    assert _requirement(session, "training-mastery-effects.mount-exp")["increase_percent"] == 93.75
    assert _requirement(session, "training-mastery-effects.generation")["increase_percent"] == 13
    assert _requirement(session, "horse-imperial-delivery.level")["level"] == 15


def test_courser_and_dream_horse_awaking_requirements(session) -> None:
    skills = _requirement(session, "courser-system.tier8-skills")["skills"]
    eligibility = _requirement(session, "dream-horse-awakening.eligibility")
    training = _requirement(session, "dream-horse-awakening.training")

    assert len(skills) == 7
    assert eligibility == {"generation": 8, "courser": True, "level": 30}
    assert training["total_percent"] == 200
    assert _requirement(session, "dream-horse-awakening.types")["types"] == [
        "arduanatt", "dine", "doom"
    ]


def test_mythical_dream_horse_current_types_and_failure_stack(session) -> None:
    attempt = _requirement(session, "mythical-dream-horse.attempt")
    types = _requirement(session, "mythical-dream-horse.types")["types"]

    assert types == ["mythical_arduanatt", "mythical_dine", "mythical_doom"]
    assert attempt["base_success_percent"] == 3
    assert attempt["failure_increment_percentage_points"] == 0.2
    assert attempt["failure_stack_scope"] == "family"
    stale = _evidence(
        session, "mythical-dream-horse.claim.legacy-doom::mythical-horse-guide"
    )
    assert stale.verification_status == "superseded" and not stale.active


def test_wild_horse_latest_sources_are_attached(session) -> None:
    rare = _evidence(
        session, "wild-horse-capture.claim.rare::rare-wild-horses-2025-12-23"
    )
    population = _evidence(
        session, "wild-horse-capture.claim.generations::blood-altar-challenge-2026-07-15"
    )
    assert rare.active and rare.verification_status == "verified"
    assert population.active and population.verification_status == "verified"


def test_hunting_mastery_and_firearm_downgrade(session) -> None:
    rows = _requirement(session, "hunting-mastery-effects.yield")["rows"]
    downgrade = _requirement(session, "hunting-firearms.downgrade")

    assert {row["mastery"]: row["increase_percent"] for row in rows}[3000] == 375
    assert downgrade["plus_1_to_6"]["downgrade_percent"] == 0
    assert downgrade["plus_7_to_8"]["downgrade_percent"] == 10
    assert downgrade["plus_8_to_9"]["downgrade_percent"] == 50
    assert downgrade["plus_9_to_10"]["downgrade_percent"] == 100


def test_sniper_current_damage_tiers_supersede_old_mastery_only_rule(session) -> None:
    rows = _requirement(session, "sniper-hunting.damage-tiers")["rows"]
    stale = _evidence(
        session,
        "sniper-hunting.claim.legacy-mastery-tiers::hunting-guide",
    )

    assert [row["damage_percent"] for row in rows] == ["0", "1-40", "41-80"]
    assert rows[0]["meat_bonus_percent"] == 10
    assert rows[-1]["meat_bonus_percent"] == 5
    assert stale.verification_status == "superseded" and not stale.active


def test_marni_sniper_crafting_and_enhancement_are_distinct(session) -> None:
    recipe = _requirement(session, "marni-sniper-rifle.recipe")
    enhancement = _requirement(session, "marni-sniper-rifle.enhancement")

    assert recipe["condensed_magical_black_crystal"] == 10
    assert enhancement["material"] == "condensed_magical_black_stone"
    assert enhancement["distinct_from"] == "condensed_magical_black_crystal"
    stale = _evidence(
        session,
        "marni-sniper-rifle.claim.legacy-scorching-sun"
        "::marni-sniper-crafting-2026-03-25",
    )
    assert stale.verification_status == "superseded" and not stale.active


def test_latest_hunting_balance_and_old_surprise_history(session) -> None:
    balance = _requirement(session, "hunting-current-system.balance-2026-09-02")

    assert balance["combat_gear_defense_applies"] is True
    assert balance["morning_light_sniper_hp_increase_percent"] == 10
    assert balance["most_hunting_monster_hp_increase_percent"] == 20
    assert balance["hp_20_percent_exceptions"] == ["라우라우", "산발바닥", "대왕고래"]
    stale = _evidence(
        session,
        "hunting-growth-surprise-quest.claim.legacy-quests"
        "::ocean-iliya-consolidation-2025-05-14",
    )
    assert stale.verification_status == "superseded" and not stale.active
