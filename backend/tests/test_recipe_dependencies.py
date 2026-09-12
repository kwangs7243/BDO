from __future__ import annotations

from datetime import UTC, datetime

from fastapi.testclient import TestClient
from sqlalchemy import func, select

from app.database import get_session
from app.knowledge import get_knowledge_recipe
from app.main import app
from app.models import (
    Evidence,
    Material,
    Recipe,
    RecipeIngredientOption,
    RecipeIngredientSlot,
    UserMaterialInventory,
)
from app.recipe_dependencies import (
    build_recipe_dependency_index,
    get_recipe_dependencies,
)


EXPECTED_EDGES = {
    (
        "vinegar",
        "pickled-vegetables",
        "vinegar",
        "pickled-vegetables.ingredient.vinegar.option.vinegar",
    ): (4.0, False),
    (
        "red-sauce",
        "steak",
        "red-sauce",
        "steak.ingredient.red-sauce.option.red-sauce",
    ): (2.0, False),
    (
        "red-sauce",
        "frank-sandwich",
        "red-sauce",
        "frank-sandwich.ingredient.red-sauce.option.red-sauce",
    ): (1.0, False),
    (
        "tea-with-fine-scent",
        "sute-tea",
        "tea-with-fine-scent",
        "sute-tea.ingredient.tea.option.tea-with-fine-scent",
    ): (2.0, True),
    (
        "grilled-sausage",
        "ham-sandwich",
        "grilled-sausage",
        "ham-sandwich.ingredient.sausage.option.grilled-sausage",
    ): (2.0, True),
    (
        "grilled-sausage",
        "frank-sandwich",
        "grilled-sausage",
        "frank-sandwich.ingredient.sausage.option.grilled-sausage",
    ): (2.0, True),
    (
        "clear-liquid-reagent",
        "defense-elixir",
        "clear-liquid-reagent",
        "defense-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent",
    ): (1.0, False),
    (
        "clear-liquid-reagent",
        "concentration-elixir",
        "clear-liquid-reagent",
        "concentration-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent",
    ): (1.0, False),
}


def _recipes(session):
    rows = []
    for slug in session.scalars(
        select(Recipe.slug).where(Recipe.active.is_(True)).order_by(Recipe.slug)
    ):
        recipe = get_knowledge_recipe(session, slug)
        assert recipe is not None
        rows.append(recipe)
    return rows


def _client(session):
    app.dependency_overrides[get_session] = lambda: session
    return TestClient(app)


def _edge_identity(edge):
    return (
        edge.producer_recipe_slug,
        edge.consumer_recipe_slug,
        edge.material_key,
        edge.consumer_option_seed_key,
    )


def test_current_catalog_has_exact_direct_material_edges(session):
    index = build_recipe_dependency_index(_recipes(session))
    edges = [
        edge
        for dependencies in index.values()
        for edge in dependencies.direct_downstream
    ]

    assert len(index) == 19
    assert len(edges) == 8
    assert {
        _edge_identity(edge): (edge.required_quantity, edge.is_alternative)
        for edge in edges
    } == EXPECTED_EDGES
    assert all(edge.producer_verification_status == "verified" for edge in edges)
    assert all(edge.consumer_verification_status == "verified" for edge in edges)
    assert all(
        edge.producer_process_type == edge.consumer_process_type == "alchemy"
        for edge in edges
        if edge.producer_recipe_slug == "clear-liquid-reagent"
    )


def test_expected_upstream_and_downstream_sets_are_exact(session):
    index = build_recipe_dependency_index(_recipes(session))
    upstream = {
        slug: [edge.producer_recipe_slug for edge in dependencies.direct_upstream]
        for slug, dependencies in index.items()
    }
    downstream = {
        slug: [edge.consumer_recipe_slug for edge in dependencies.direct_downstream]
        for slug, dependencies in index.items()
    }

    assert upstream["pickled-vegetables"] == ["vinegar"]
    assert upstream["steak"] == ["red-sauce"]
    assert upstream["sute-tea"] == ["tea-with-fine-scent"]
    assert upstream["ham-sandwich"] == ["grilled-sausage"]
    assert upstream["frank-sandwich"] == ["grilled-sausage", "red-sauce"]
    assert upstream["defense-elixir"] == ["clear-liquid-reagent"]
    assert upstream["concentration-elixir"] == ["clear-liquid-reagent"]
    assert downstream["vinegar"] == ["pickled-vegetables"]
    assert downstream["red-sauce"] == ["frank-sandwich", "steak"]
    assert downstream["tea-with-fine-scent"] == ["sute-tea"]
    assert downstream["grilled-sausage"] == ["frank-sandwich", "ham-sandwich"]
    assert downstream["clear-liquid-reagent"] == [
        "concentration-elixir",
        "defense-elixir",
    ]

    expected_upstream = {
        "pickled-vegetables",
        "steak",
        "sute-tea",
        "ham-sandwich",
        "frank-sandwich",
        "defense-elixir",
        "concentration-elixir",
    }
    expected_downstream = {
        "vinegar",
        "red-sauce",
        "tea-with-fine-scent",
        "grilled-sausage",
        "clear-liquid-reagent",
    }
    assert all(upstream[slug] == [] for slug in index.keys() - expected_upstream)
    assert all(downstream[slug] == [] for slug in index.keys() - expected_downstream)


def test_group_members_do_not_create_dependency_edges(session):
    beer = get_knowledge_recipe(session, "beer")
    grilled_sausage = get_knowledge_recipe(session, "grilled-sausage")
    assert beer is not None
    assert grilled_sausage is not None
    meat_slot = next(
        slot
        for slot in grilled_sausage.ingredient_slots
        if slot.options[0].target_type == "ingredient_group"
        and slot.options[0].ingredient_group.key == "meat"
    )
    producer = beer.model_copy(
        update={
            "slug": "beef-producer",
            "name_ko": "합성 소고기 생산식",
            "result_material_key": "beef",
            "result_material_name_ko": "소고기",
        }
    )
    consumer = grilled_sausage.model_copy(
        update={
            "slug": "meat-group-consumer",
            "name_ko": "합성 고기 그룹 소비식",
            "result_material_key": "synthetic-result",
            "result_material_name_ko": "합성 결과물",
            "ingredient_slots": [meat_slot],
        }
    )

    index = build_recipe_dependency_index([producer, consumer])

    assert index["beef-producer"].direct_downstream == []
    assert index["meat-group-consumer"].direct_upstream == []


def test_special_results_and_recursive_ingredients_are_not_inferred(session):
    ham = get_recipe_dependencies(session, "ham-sandwich")
    sute = get_recipe_dependencies(session, "sute-tea")
    frank = get_recipe_dependencies(session, "frank-sandwich")
    assert ham is not None
    assert sute is not None
    assert frank is not None

    assert [edge.producer_recipe_slug for edge in ham.direct_upstream] == [
        "grilled-sausage"
    ]
    assert [edge.material_key for edge in sute.direct_upstream] == [
        "tea-with-fine-scent"
    ]
    assert [edge.producer_recipe_slug for edge in frank.direct_upstream] == [
        "grilled-sausage",
        "red-sauce",
    ]
    assert {
        edge.material_key for edge in ham.direct_upstream + sute.direct_upstream
    }.isdisjoint({"smoked-sausage", "tea-with-strong-scent"})
    assert {
        edge.material_key for edge in frank.direct_upstream
    }.isdisjoint({"meat", "onion", "salt", "pepper", "base-sauce", "sugar"})


def test_builder_is_deterministic_when_input_order_changes(session):
    recipes = _recipes(session)

    forward = build_recipe_dependency_index(recipes)
    reverse = build_recipe_dependency_index(list(reversed(recipes)))

    assert {
        slug: value.model_dump(mode="json") for slug, value in forward.items()
    } == {
        slug: value.model_dump(mode="json") for slug, value in reverse.items()
    }


def test_dependency_api_representative_responses_and_unknown(session):
    client = _client(session)
    try:
        frank = client.get("/api/knowledge/recipes/frank-sandwich/dependencies")
        red_sauce = client.get("/api/knowledge/recipes/red-sauce/dependencies")
        beer = client.get("/api/knowledge/recipes/beer/dependencies")
        missing = client.get("/api/knowledge/recipes/not-a-recipe/dependencies")
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert frank.status_code == 200
    assert [
        edge["producer_recipe_slug"] for edge in frank.json()["direct_upstream"]
    ] == ["grilled-sausage", "red-sauce"]
    assert len(red_sauce.json()["direct_downstream"]) == 2
    assert beer.json()["direct_upstream"] == []
    assert beer.json()["direct_downstream"] == []
    assert missing.status_code == 404
    assert missing.json() == {"detail": "Recipe not found"}


def test_dependency_api_is_independent_of_personal_inventory(session):
    material = session.scalar(select(Material).where(Material.key == "red-sauce"))
    inventory = UserMaterialInventory(
        material_id=material.id,
        quantity=0,
        note="dependency-independent",
        updated_at=datetime(2026, 9, 11, tzinfo=UTC),
    )
    session.add(inventory)
    session.commit()
    client = _client(session)
    try:
        before = client.get("/api/knowledge/recipes/frank-sandwich/dependencies")
        inventory.quantity = 999999
        session.commit()
        after = client.get("/api/knowledge/recipes/frank-sandwich/dependencies")
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert before.status_code == after.status_code == 200
    assert before.json() == after.json()
    session.refresh(inventory)
    assert inventory.quantity == 999999


def test_dependency_get_does_not_mutate_relevant_tables(session):
    models = (
        Recipe,
        RecipeIngredientSlot,
        RecipeIngredientOption,
        Material,
        Evidence,
        UserMaterialInventory,
    )
    before = {
        model: session.scalar(select(func.count()).select_from(model)) for model in models
    }
    client = _client(session)
    try:
        response = client.get("/api/knowledge/recipes/red-sauce/dependencies")
    finally:
        app.dependency_overrides.clear()
        client.close()
    after = {
        model: session.scalar(select(func.count()).select_from(model)) for model in models
    }

    assert response.status_code == 200
    assert after == before
