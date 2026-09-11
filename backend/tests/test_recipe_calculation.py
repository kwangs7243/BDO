from __future__ import annotations

from datetime import UTC, datetime

from fastapi.testclient import TestClient
import pytest
from sqlalchemy import select

from app.database import get_session
from app.knowledge import get_knowledge_recipe
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
    UserMaterialInventory,
)
from app.recipe_calculations import scale_recipe_requirements


def _client(session):
    def override_session():
        yield session

    app.dependency_overrides[get_session] = override_session
    return TestClient(app)


def _post(session, payload: dict[str, object], slug: str = "beer"):
    client = _client(session)
    try:
        return client.post(f"/api/calculations/recipes/{slug}", json=payload)
    finally:
        app.dependency_overrides.clear()
        client.close()


def _options(payload):
    return [
        option
        for slot in payload["ingredient_slots"]
        for option in slot["options"]
    ]


def _option_map(payload):
    return {
        option["material_key"] or option["ingredient_group"]["key"]: option
        for option in _options(payload)
    }


def _table_snapshot(session, models):
    return {
        model.__tablename__: [
            tuple(row)
            for row in session.execute(
                select(model.__table__).order_by(model.__table__.c.id)
            )
        ]
        for model in models
    }


def _all_keys(value):
    if isinstance(value, dict):
        return set(value) | {
            key
            for child in value.values()
            for key in _all_keys(child)
        }
    if isinstance(value, list):
        return {key for child in value for key in _all_keys(child)}
    return set()


def test_beer_100_attempts_scales_every_option_independently(session) -> None:
    response = _post(session, {"attempt_count": 100})

    assert response.status_code == 200
    payload = response.json()
    assert {
        key: option["total_required_quantity"]
        for key, option in _option_map(payload).items()
    } == {
        "grain": 500,
        "mineral-water": 600,
        "purified-water": 300,
        "leavening-agent": 200,
        "sugar": 100,
    }
    assert payload["recipe_slug"] == "beer"
    assert payload["result_material_key"] == "beer"
    assert payload["attempt_count"] == 100
    assert payload["verification_status"] == "verified"
    assert payload["last_verified_at"] == "2026-09-11"
    assert {"id", "evidence_id", "sources"}.isdisjoint(_all_keys(payload))


@pytest.mark.parametrize(
    ("slug", "attempt_count", "expected"),
    [
        (
            "vinegar",
            7,
            {"grain": 7, "fruit": 7, "leavening-agent": 7, "sugar": 7},
        ),
        (
            "pickled-vegetables",
            3,
            {"vegetable": 24, "vinegar": 12, "leavening-agent": 6, "sugar": 6},
        ),
        (
            "grilled-bird-meat",
            5,
            {
                "bird-meat": 10,
                "deep-frying-oil": 30,
                "cottonseed-oil": 30,
                "cooking-wine": 10,
                "salt": 5,
            },
        ),
    ],
)
def test_recipe_batch_scaling_uses_canonical_per_attempt_quantities(
    session, slug, attempt_count, expected
) -> None:
    response = _post(session, {"attempt_count": attempt_count}, slug=slug)

    assert response.status_code == 200
    assert {
        key: option["total_required_quantity"]
        for key, option in _option_map(response.json()).items()
    } == expected


@pytest.mark.parametrize(
    "slug", ["beer", "vinegar", "pickled-vegetables", "grilled-bird-meat"]
)
def test_one_attempt_equals_each_canonical_option_quantity(session, slug) -> None:
    response = _post(session, {"attempt_count": 1}, slug=slug)

    assert response.status_code == 200
    for option in _options(response.json()):
        assert option["total_required_quantity"] == option["per_attempt_quantity"]


@pytest.mark.parametrize(
    ("slug", "slot_seed_key", "option_keys", "totals"),
    [
        (
            "beer",
            "beer.ingredient.water",
            ["mineral-water", "purified-water"],
            [600, 300],
        ),
        (
            "grilled-bird-meat",
            "grilled-bird-meat.ingredient.oil",
            ["deep-frying-oil", "cottonseed-oil"],
            [60, 60],
        ),
    ],
)
def test_or_options_are_preserved_in_order_without_selection_or_sum(
    session, slug, slot_seed_key, option_keys, totals
) -> None:
    response = _post(session, {"attempt_count": 100 if slug == "beer" else 10}, slug=slug)
    payload = response.json()
    slot = next(
        item for item in payload["ingredient_slots"] if item["slot_seed_key"] == slot_seed_key
    )

    assert [option["material_key"] for option in slot["options"]] == option_keys
    assert [option["total_required_quantity"] for option in slot["options"]] == totals
    assert "selected_option" not in payload
    assert "combined_quantity" not in slot


@pytest.mark.parametrize(
    ("slug", "group_key", "member_keys"),
    [
        ("beer", "grain", ["wheat", "barley", "potato", "sweet-potato", "corn"]),
        (
            "grilled-bird-meat",
            "bird-meat",
            ["kuku-bird-meat", "flamingo-meat", "chicken-meat"],
        ),
    ],
)
def test_ingredient_group_remains_the_target_without_member_quantities(
    session, slug, group_key, member_keys
) -> None:
    response = _post(session, {"attempt_count": 10}, slug=slug)
    option = _option_map(response.json())[group_key]

    assert option["target_type"] == "ingredient_group"
    assert option["material_key"] is None
    assert option["material_name_ko"] is None
    assert option["unit"] is None
    assert option["ingredient_group"]["key"] == group_key
    assert option["ingredient_group"]["verification_status"] == "verified"
    assert [
        member["material_key"] for member in option["ingredient_group"]["members"]
    ] == member_keys
    assert all(
        {"per_attempt_quantity", "total_required_quantity"}.isdisjoint(member)
        for member in option["ingredient_group"]["members"]
    )


@pytest.mark.parametrize(
    "payload",
    [
        {"attempt_count": 0},
        {"attempt_count": -1},
        {"attempt_count": 1.0},
        {"attempt_count": "1"},
        {"attempt_count": True},
        {"attempt_count": 1, "inventory": []},
    ],
)
def test_attempt_count_is_a_strict_positive_integer(session, payload) -> None:
    assert _post(session, payload).status_code == 422


def test_unknown_recipe_returns_404(session) -> None:
    response = _post(session, {"attempt_count": 1}, slug="not-a-recipe")

    assert response.status_code == 404
    assert response.json() == {"detail": "Recipe not found"}


def test_calculation_is_independent_of_local_material_inventory(session) -> None:
    before = _post(session, {"attempt_count": 100}).json()
    material = session.scalar(select(Material).where(Material.key == "wheat"))
    assert material is not None
    session.add(
        UserMaterialInventory(
            material_id=material.id,
            quantity=999999,
            note="must not affect stateless recipe calculation",
            updated_at=datetime(2026, 9, 11, tzinfo=UTC),
        )
    )
    session.commit()

    assert _post(session, {"attempt_count": 100}).json() == before


def test_calculation_does_not_mutate_canonical_tables(session) -> None:
    models = (
        Material,
        IngredientGroup,
        IngredientGroupMember,
        Recipe,
        RecipeIngredientSlot,
        RecipeIngredientOption,
        Evidence,
        Source,
    )
    before = _table_snapshot(session, models)

    response = _post(session, {"attempt_count": 100})

    assert response.status_code == 200
    assert _table_snapshot(session, models) == before


def test_scaling_is_pure_deterministic_and_does_not_mutate_knowledge_dto(session) -> None:
    recipe = get_knowledge_recipe(session, "beer")
    assert recipe is not None
    before = recipe.model_dump(mode="json")

    first = scale_recipe_requirements(recipe, 25)
    second = scale_recipe_requirements(recipe, 25)

    assert first == second
    assert recipe.model_dump(mode="json") == before
