from __future__ import annotations

import json
from pathlib import Path

from sqlalchemy import select

from app.models import Content, ContentRelation, ContentRequirement, Evidence


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


def test_v16i_seed_json_is_unique_and_expected_rows_exist() -> None:
    sources = json.loads((DATA_DIR / "seed_sources.json").read_text(encoding="utf-8"))
    contents = json.loads((DATA_DIR / "seed_contents.json").read_text(encoding="utf-8"))
    source_ids = [row["id"] for row in sources]
    source_urls = [row["url"] for row in sources]
    slugs = [row["slug"] for row in contents]

    expected_sources = {
        "contribution-guide",
        "node-guide",
        "farming-overhaul-2026-06-04",
        "worker-guide",
        "worker-overhaul-2023-05-24",
        "worker-convenience-2025-01-22",
        "work-management-guide",
        "house-guide",
        "crafting-guide",
        "storage-guide",
        "silver-unification-history",
        "magnus-storage-history",
        "magnus-guide",
        "remote-storage-sale-history",
        "royal-workshop-history",
        "royal-workshop-2024-11-20",
    }
    expected_contents = {
        "contribution-economy-foundation",
        "node-network-current-system",
        "production-node-current-system",
        "production-node-2026-overhaul",
        "worker-current-system",
        "worker-races-grades",
        "worker-growth-promotion",
        "worker-skills-luck",
        "worker-special-delivery",
        "worker-stamina-auto-recovery",
        "worker-market",
        "housing-life-economy",
        "worker-lodging",
        "workshop-crafting-logistics",
        "storage-current-system",
        "storage-transport",
        "magnus-remote-storage",
        "family-silver-unification",
        "royal-workshop-current-system",
        "royal-workshop-worker-effects",
    }

    assert len(source_ids) == len(set(source_ids))
    assert len(source_urls) == len(set(source_urls))
    assert len(slugs) == len(set(slugs))
    assert expected_sources <= set(source_ids)
    assert expected_contents <= set(slugs)


def test_contribution_and_node_network_current_rules(session) -> None:
    contribution = _requirement(session, "contribution-economy-foundation.uses")
    node_types = _requirement(session, "node-network-current-system.types")
    remote = _requirement(session, "node-network-current-system.value-pack-remote")
    penalties = _requirement(session, "node-network-current-system.disconnected-penalties")

    assert contribution["family_shared"] is True
    assert contribution["region_restricted"] is False
    assert node_types["distinct"] is True
    assert node_types["production_type_count"] == 7
    assert remote["value_pack_required"] is True
    assert remote["energy_per_node"] == 10
    assert remote["free_remote_investment"] is False
    assert penalties == {
        "transport_available": True,
        "transport_fee_multiplier": 3,
        "trade_sale_base_price_percent": 30,
    }


def test_production_node_unlock_and_destination_are_separate(session) -> None:
    unlock = _requirement(session, "production-node-current-system.unlock")
    worker = _requirement(session, "production-node-current-system.worker-network")
    destination = _requirement(session, "production-node-current-system.output-destination")

    assert unlock == {
        "parent_exploration_node_invested": True,
        "production_node_invested": True,
    }
    assert worker["connected_network_required"] is True
    assert worker["remote_town_worker_allowed_when_connected"] is True
    assert destination["special_delivery"] is True
    assert destination["destination_town_storage_selectable"] is True
    assert destination["default_town_storage_only"] is False


def test_2026_node_cp_changes_are_current_and_old_claim_is_inactive(session) -> None:
    value = _requirement(session, "production-node-2026-overhaul.cp-changes")
    current = {row["node"]: row["current_cp"] for row in value["rows"]}

    assert value["effective_date"] == "2026-06-04"
    assert value["current_row_count"] == 13
    assert current["플로린 관문"] == 1
    assert current["티티움 계곡"] == 1
    assert current["라이칼 폭포 - 채집"] == 1
    assert current["쿠니드의 쉼터 - 채집"] == 1
    old = _evidence(
        session,
        "production-node-2026-overhaul.claim.legacy-cp"
        "::farming-overhaul-2026-06-04",
    )
    assert old.verification_status == "superseded" and not old.active


def test_2026_production_slots_preserve_duplicate_slots(session) -> None:
    value = _requirement(session, "production-node-2026-overhaul.production-slots")
    slots = value["slots"]

    assert value["slot_count"] == len(slots) == 41
    assert value["deduplicate_identical_outputs"] is False
    by_node = {}
    for row in slots:
        by_node.setdefault(row["node"], []).append(row)

    assert len(by_node["늑대 언덕"]) == 2
    assert by_node["늑대 언덕"][0]["outputs"] == [
        "물푸레 나무 원목",
        "물푸레 나무 수액",
    ]
    assert by_node["노인의 다리"][0]["outputs"] == [
        "자작 나무 원목",
        "자작 나무 수액",
    ]
    assert len(by_node["가모스의 둥지"]) == 2
    assert by_node["가모스의 둥지"][0]["outputs"] == [
        "검은 수정 원석",
        "자연의 흔적",
    ]
    assert len(by_node["낙시온"]) == 2
    assert len(by_node["필라 페"]) == 2
    assert len(by_node["폐허도시 룬"]) == 2
    pilgrim_rows = [row for row in slots if row["node"].startswith("순례자의 성소")]
    assert len(pilgrim_rows) == 4
    assert all(row["outputs"] == ["금광석", "자연의 흔적"] for row in pilgrim_rows)


def test_worker_hiring_remote_access_and_repeat_limit(session) -> None:
    hiring = _requirement(session, "worker-current-system.hiring")
    remote = _requirement(session, "worker-current-system.remote-hiring")
    work = _requirement(session, "worker-current-system.work-scope")

    assert hiring["energy_per_view"] == hiring["energy_per_reroll"] == 5
    assert remote["active"] is True
    assert remote["character_presence_in_town_required"] is False
    assert remote["worker_supervisor_knowledge_required"] is True
    assert work["max_repeat"] == 50000
    assert work["actual_repeat_limited_by_stamina"] is True


def test_worker_race_traits_are_not_universal_final_stats(session) -> None:
    families = _requirement(session, "worker-races-grades.families")

    assert families["goblin_family"]["effects"] == ["work_speed", "movement_speed"]
    assert families["giant_family"]["base_yield_bonus_percent_approx"] == 68.4
    assert families["giant_family"]["not_universal_final_stat"] is True
    assert families["human_family"]["historical_base_luck_increase"] == 3
    assert families["human_family"]["not_universal_final_stat"] is True


def test_worker_growth_promotion_and_skill_reroll(session) -> None:
    growth = _requirement(session, "worker-growth-promotion.level-skills")
    reroll = _requirement(session, "worker-growth-promotion.skill-reroll")
    promotion = _requirement(session, "worker-growth-promotion.promotion")

    assert growth["max_level"] == 40
    assert growth["total_skills_at_level_40"] == 10
    assert reroll["minimum_level"] == 30
    assert reroll["minimum_exp_percent"] == reroll["exp_cost_percent"] == 20
    assert [row["success_percent"] for row in promotion["rows"]] == [90, 70, 50]
    assert promotion["on_success"] == {
        "level_reset": True,
        "learned_skills_reset": True,
    }


def test_worker_special_delivery_current_rule_supersedes_level_40(session) -> None:
    current = _requirement(session, "worker-special-delivery.current-level")
    destination = _requirement(session, "worker-special-delivery.destination")
    old = _evidence(
        session,
        "worker-special-delivery.claim.legacy-level-40::worker-overhaul-2023-05-24",
    )

    assert current == {"all_workers": True, "level": 1, "basic_skill": True}
    assert destination["destination_town_storage_selectable"] is True
    assert destination["changes_workshop_material_source"] is False
    assert old.verification_status == "superseded" and not old.active


def test_worker_stamina_market_and_unresolved_probability(session) -> None:
    automatic = _requirement(session, "worker-stamina-auto-recovery.automatic")
    market = _requirement(session, "worker-market.price-fee")
    unresolved = _requirement(session, "worker-market.unresolved-promotion")

    assert automatic["trigger_at_or_below_stamina"] == 3
    assert automatic["item_source"] == "family_inventory"
    assert automatic["applies_to_farm_workers"] is True
    assert market["sale_fee_percent"] == 30
    assert unresolved == {
        "remaining_promotion_chances": None,
        "verification": "needs_review",
    }


def test_housing_lodging_and_storage_rules(session) -> None:
    housing = _requirement(session, "housing-life-economy.purchase-use")
    residences = _requirement(session, "housing-life-economy.residences")
    lodging = _requirement(session, "worker-lodging.capacity")
    storage = _requirement(session, "storage-current-system.items")
    timed = _requirement(session, "storage-current-system.timed-items")

    assert housing["purchase_resource"] == "contribution"
    assert housing["default_when_no_use_selected"] == "storage"
    assert residences["family_max_residences"] == 5
    assert lodging["base_workers_without_lodging_per_town_or_territory"] == 1
    assert storage["base_slots"] == 8
    assert timed["time_stops_in_storage"] is False


def test_four_logistics_mechanics_remain_distinct(session) -> None:
    production = _requirement(session, "production-node-current-system.output-destination")
    workshop = _requirement(session, "workshop-crafting-logistics.material-source")
    workshop_distinction = _requirement(session, "workshop-crafting-logistics.distinction")
    transport = _requirement(session, "storage-transport.network-time")
    packages = _requirement(session, "storage-transport.packages")
    magnus = _requirement(session, "magnus-remote-storage.distinction")

    assert production["destination_town_storage_selectable"] is True
    assert workshop["material_storage"] == "selected_worker_affiliated_town_storage"
    assert workshop["character_inventory_used"] is False
    assert workshop_distinction["production_special_delivery_changes_material_source"] is False
    assert packages["max_packages"] == 40
    assert transport["disconnected_available"] is True
    assert transport["disconnected_fee_multiplier"] == 3
    assert transport["instant"] is False
    assert set(magnus.values()) == {False}


def test_magnus_storage_and_current_silver_rules(session) -> None:
    magnus = _requirement(session, "magnus-remote-storage.remote-sale")
    restrictions = _requirement(session, "magnus-remote-storage.restrictions")
    silver = _requirement(session, "family-silver-unification.current-pool")
    market = _requirement(session, "family-silver-unification.market-separate")

    assert magnus["full_magnus_questline_required"] is True
    assert magnus["remote_town_storage_item_sale"] is True
    assert magnus["move_to_central_market_storage"] is True
    assert len(restrictions["restricted_item_classes"]) == 4
    assert silver["family_unified"] is True
    assert silver["town_specific_balances"] is False
    assert silver["character_specific_balances"] is False
    assert market["central_market_storage_silver_separate"] is True

    stale = [
        _evidence(
            session,
            "family-silver-unification.claim.legacy-town-balance::storage-guide",
        ),
        _evidence(
            session,
            "family-silver-unification.claim.legacy-character-balance::storage-guide",
        ),
    ]
    assert all(row.verification_status == "superseded" and not row.active for row in stale)


def test_royal_workshop_current_rules_and_stale_refresh(session) -> None:
    access = _requirement(session, "royal-workshop-current-system.access")
    resources = _requirement(session, "royal-workshop-current-system.resources")
    workshops = _requirement(session, "royal-workshop-current-system.production-workshops")
    refresh = _requirement(session, "royal-workshop-current-system.auto-refresh-current")
    old = _evidence(
        session,
        "royal-workshop-current-system.claim.refresh-legacy-0100"
        "::royal-workshop-history",
    )

    assert access["contribution_points"] == 5
    assert resources == {"worker_origin": "육조거리", "storage_origin": "육조거리"}
    assert workshops["workshops_per_production_node"] == 5
    assert refresh["time_local"] == "00:00:00"
    assert refresh["timezone"] == "Asia/Seoul"
    assert old.verification_status == "superseded" and not old.active


def test_royal_workshop_worker_effects_are_scoped(session) -> None:
    turtle = _requirement(session, "royal-workshop-worker-effects.production-turtle")
    luck = _requirement(session, "royal-workshop-worker-effects.production-luck")
    frugal = _requirement(session, "royal-workshop-worker-effects.processing-frugal")
    movement = _requirement(session, "royal-workshop-worker-effects.movement-speed")

    assert turtle["branch"] == "production"
    assert turtle["base_yield_bonus_percent"] == 68.4
    assert turtle["applies"] is True
    assert luck["luck_affects_extra_acquisition"] is True
    assert luck["exact_probability"] is None
    assert frugal["skills"] == ["알뜰살뜰 A", "알뜰살뜰 B", "알뜰살뜰 C"]
    assert frugal["return_percent"] == 10
    assert frugal["exact_probability"] is None
    assert movement["affects_royal_workshop_time"] is False


def test_life_economy_relations_link_existing_life_content(session) -> None:
    targets = {
        row.to_content.slug
        for row in session.scalars(
            select(ContentRelation).join(ContentRelation.from_content).where(
                Content.slug.in_(
                    [
                        "production-node-current-system",
                        "housing-life-economy",
                        "workshop-crafting-logistics",
                    ]
                )
            )
        ).all()
        if row.active
    }

    assert {"processing-current-system", "cooking-current-system", "alchemy-current-system"} <= targets
