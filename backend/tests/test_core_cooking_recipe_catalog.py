from __future__ import annotations

import json
from pathlib import Path

from fastapi.testclient import TestClient
import pytest
from sqlalchemy import func, select

from app.database import get_session
from app.main import app
from app.models import (
    Evidence,
    IngredientGroup,
    IngredientGroupMember,
    Material,
    Recipe,
    RecipeIngredientOption,
    RecipeIngredientSlot,
    Source,
)
from app.knowledge import get_knowledge_recipe


DATA = Path(__file__).resolve().parents[2] / "data"

NEW_SOURCE_METADATA = {
    "weingchicken-dressing-56": (
        "https://apps.weingchicken.com/bd/makings/56",
        "드레싱 - 검은사막 제작노트",
        "위잉치킨",
    ),
    "codex-red-sauce-9004": (
        "https://bdocodex.com/kr/item/9004/",
        "레드소스",
        "BDO Codex",
    ),
    "codex-red-sauce-purified-546": (
        "https://bdocodex.com/kr/recipe/546/?sl=1",
        "레드소스",
        "BDO Codex",
    ),
    "weingchicken-white-sauce-152": (
        "https://apps.weingchicken.com/bd/makings/152",
        "화이트소스 - 검은사막 제작노트",
        "위잉치킨",
    ),
    "codex-tea-with-fine-scent-9270": (
        "https://bdocodex.com/kr/item/9270/",
        "향이 좋은 차",
        "BDO Codex",
    ),
    "weingchicken-tea-with-fine-scent-218": (
        "https://apps.weingchicken.com/bd/makings/218",
        "향이 좋은 차 - 검은사막 제작노트",
        "위잉치킨",
    ),
    "weingchicken-omelet-335": (
        "https://apps.weingchicken.com/bd/makings/335",
        "오믈렛 - 검은사막 제작노트",
        "위잉치킨",
    ),
    "inven-cooking-recipe-db": (
        "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r",
        "요리 · 연금 DB",
        "검은사막 인벤",
    ),
}

NEW_FORMULAS = {
    "dressing": [
        [("egg", 1)],
        [("olive-oil", 1)],
        [("water", 1)],
        [("salt", 2)],
    ],
    "red-sauce": [
        [("base-sauce", 1)],
        [("meat", 1)],
        [("mineral-water", 2), ("purified-water", 1)],
        [("sugar", 2)],
    ],
    "white-sauce": [
        [("base-sauce", 1)],
        [("fruit", 1)],
        [("milk", 1)],
        [("cooking-wine", 2)],
    ],
    "tea-with-fine-scent": [
        [("flower", 4)],
        [("fruit", 4)],
        [("mineral-water", 7), ("purified-water", 3)],
        [("edible-honey", 3)],
    ],
    "omelet": [
        [("grain", 5)],
        [("olive-oil", 2)],
        [("egg", 5)],
        [("salt", 2)],
    ],
}

TEN_ATTEMPT_TOTALS = {
    "dressing": {
        "egg": 10,
        "olive-oil": 10,
        "water": 10,
        "salt": 20,
    },
    "red-sauce": {
        "base-sauce": 10,
        "meat": 10,
        "mineral-water": 20,
        "purified-water": 10,
        "sugar": 20,
    },
    "white-sauce": {
        "base-sauce": 10,
        "fruit": 10,
        "milk": 10,
        "cooking-wine": 20,
    },
    "tea-with-fine-scent": {
        "flower": 40,
        "fruit": 40,
        "mineral-water": 70,
        "purified-water": 30,
        "edible-honey": 30,
    },
    "omelet": {
        "grain": 50,
        "olive-oil": 20,
        "egg": 50,
        "salt": 20,
    },
}


def _recipe_formula(recipe):
    return [
        [
            (
                option.material_key or option.ingredient_group.key,
                option.required_quantity,
            )
            for option in slot.options
        ]
        for slot in recipe.ingredient_slots
    ]


def _source_ids(session, claim_seed_key: str) -> set[str]:
    return set(
        session.scalars(
            select(Evidence.source_id).where(
                Evidence.seed_key.like(f"{claim_seed_key}::%"),
                Evidence.active.is_(True),
            )
        )
    )


def _all_keys(value) -> set[str]:
    if isinstance(value, dict):
        return set(value) | {
            key for child in value.values() for key in _all_keys(child)
        }
    if isinstance(value, list):
        return {key for child in value for key in _all_keys(child)}
    return set()


def test_v19t_exact_canonical_and_evidence_counts(session) -> None:
    expected_counts = {
        Material: 64,
        IngredientGroup: 7,
        IngredientGroupMember: 35,
        Recipe: 9,
        RecipeIngredientSlot: 36,
        RecipeIngredientOption: 40,
    }
    for model, expected in expected_counts.items():
        actual = session.scalar(
            select(func.count()).select_from(model).where(model.active.is_(True))
        )
        assert actual >= expected
    assert session.scalar(select(func.count()).select_from(Source)) >= 199

    catalog = json.loads((DATA / "seed_recipes.json").read_text(encoding="utf-8"))
    claims = [
        claim
        for owner in [*catalog["ingredient_groups"], *catalog["recipes"]]
        for claim in owner["evidence"]
    ]
    assert len(claims) == len({claim["seed_key"] for claim in claims})
    assert len(claims) >= 74

    domain_types = {
        "ingredient_group",
        "recipe",
        "recipe_ingredient_slot",
        "recipe_ingredient_option",
    }
    evidence = list(
        session.scalars(
            select(Evidence).where(
                Evidence.entity_type.in_(domain_types),
                Evidence.active.is_(True),
            )
        )
    )
    assert len(evidence) >= 115
    assert all(row.verification_status == "verified" for row in evidence)
    assert not any(row.verification_status == "needs_review" for row in evidence)
    assert all(
        get_knowledge_recipe(session, slug).verification_status == "verified"
        for slug in NEW_FORMULAS
    )


def test_v19t_sources_match_research_packet_without_official_promotion(session) -> None:
    source_seed = {
        row["id"]: row
        for row in json.loads(
            (DATA / "seed_sources.json").read_text(encoding="utf-8")
        )
    }
    assert len({row["url"] for row in source_seed.values()}) == len(source_seed)

    for source_id, (url, title, publisher) in NEW_SOURCE_METADATA.items():
        row = source_seed[source_id]
        assert row == {
            "id": source_id,
            "url": url,
            "title": title,
            "publisher": publisher,
            "source_type": "third_party_database",
            "published_at": None,
            "retrieved_at": "2026-09-11T13:02:00+09:00",
            "region": "KR",
            "notes": row["notes"],
        }
        assert row["notes"]
        assert session.get(Source, source_id).source_type == "third_party_database"


def test_v19t_formulas_skills_and_group_membership(session) -> None:
    apprentice = {"tea-with-fine-scent", "omelet"}
    for slug, expected in NEW_FORMULAS.items():
        recipe = get_knowledge_recipe(session, slug)
        assert recipe is not None
        assert _recipe_formula(recipe) == expected
        assert recipe.required_skill_level == 1
        assert recipe.required_skill_tier == (
            "apprentice" if slug in apprentice else "beginner"
        )
        assert recipe.last_verified_at.isoformat() == "2026-09-11"

    expected_members = {
        "meat": [
            "deer-meat",
            "sheep-meat",
            "fox-meat",
            "rhino-meat",
            "pork",
            "beef",
            "raccoon-meat",
            "weasel-meat",
            "bear-meat",
            "wolf-meat",
        ],
        "flower": ["rose", "tulip", "sunflower"],
        "water": ["mineral-water", "purified-water"],
    }
    groups = {
        group.key: group
        for group in session.scalars(
            select(IngredientGroup).where(IngredientGroup.key.in_(expected_members))
        )
    }
    for key, member_keys in expected_members.items():
        assert [
            member.material.key
            for member in sorted(
                (row for row in groups[key].members if row.active),
                key=lambda row: row.order_no,
            )
        ] == member_keys


def test_v19t_evidence_provenance_boundaries(session) -> None:
    expected_official_claims = {
        "ingredient-group.meat.membership",
        "ingredient-group.flower.membership",
        "ingredient-group.water.membership",
        *{f"recipe.{slug}.attempt" for slug in NEW_FORMULAS},
    }
    official_claims = {
        row.seed_key.split("::", maxsplit=1)[0]
        for row in session.scalars(
            select(Evidence).where(Evidence.source_id == "cooking-guide")
        )
        if row.entity_id in {"meat", "flower", "water"}
        or any(row.entity_id.startswith(slug) for slug in NEW_FORMULAS)
    }
    assert official_claims == expected_official_claims
    assert _source_ids(
        session,
        "recipe.red-sauce.ingredient.water.option.purified-water.quantity",
    ) == {"codex-red-sauce-purified-546"}
    assert _source_ids(
        session,
        "recipe.tea-with-fine-scent.ingredient.water.option.purified-water.quantity",
    ) == {"weingchicken-tea-with-fine-scent-218"}

    forbidden = {
        "conversion_ratio",
        "quantity_multiplier",
        "quality_multiplier",
        "white_equivalent",
        "global_quantity",
    }
    assert forbidden.isdisjoint(IngredientGroup.__table__.columns.keys())
    assert forbidden.isdisjoint(IngredientGroupMember.__table__.columns.keys())
    assert "result_quantity" not in Recipe.__table__.columns


@pytest.mark.parametrize("slug", NEW_FORMULAS)
def test_v19t_read_search_and_ten_attempt_calculation(session, slug) -> None:
    app.dependency_overrides[get_session] = lambda: session
    client = TestClient(app)
    try:
        detail_response = client.get(f"/api/knowledge/recipes/{slug}")
        assert detail_response.status_code == 200
        detail = detail_response.json()
        assert detail["slug"] == slug
        assert detail["verification_status"] == "verified"
        assert {"evidence_id", "owned_quantity"}.isdisjoint(_all_keys(detail))
        assert all(isinstance(source["id"], str) for source in detail["sources"])

        search_response = client.get(
            "/api/knowledge/search",
            params={"q": detail["name_ko"], "limit": 50},
        )
        assert search_response.status_code == 200
        assert ("recipe", slug) in {
            (item["resource_type"], item["slug"]) for item in search_response.json()
        }

        calculation_response = client.post(
            f"/api/calculations/recipes/{slug}",
            json={"attempt_count": 10},
        )
        assert calculation_response.status_code == 200
        calculation = calculation_response.json()
        options = [
            option
            for slot in calculation["ingredient_slots"]
            for option in slot["options"]
        ]
        assert {
            option["material_key"] or option["ingredient_group"]["key"]:
            option["total_required_quantity"]
            for option in options
        } == TEN_ATTEMPT_TOTALS[slug]
        assert "selected_option" not in calculation
        if slug in {"red-sauce", "tea-with-fine-scent"}:
            water = next(
                slot
                for slot in calculation["ingredient_slots"]
                if slot["slot_seed_key"] == f"{slug}.ingredient.water"
            )
            assert len(water["options"]) == 2
            assert "combined_quantity" not in water
    finally:
        app.dependency_overrides.clear()
        client.close()
