from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError
from sqlalchemy import func, select

from app.ai_export import build_ai_exports
from app.database import get_session
from app.knowledge import get_knowledge_material, get_knowledge_recipe, search_knowledge
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
from app.recipe_dependencies import get_recipe_dependencies
from app.recipe_seed import RecipeSeed
from app.seed import import_seed


DATA = Path(__file__).resolve().parents[2] / "data"
ALCHEMY_SLUGS = {
    "clear-liquid-reagent",
    "pure-powder-reagent",
    "defense-elixir",
    "concentration-elixir",
}


def _formula(session, slug: str) -> list[list[tuple[str, float]]]:
    recipe = get_knowledge_recipe(session, slug)
    assert recipe is not None
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


def _source_ids(session, evidence_seed_key: str) -> set[str]:
    prefix = f"{evidence_seed_key}::"
    return set(
        session.scalars(
            select(Evidence.source_id).where(
                Evidence.seed_key.startswith(prefix),
                Evidence.active.is_(True),
            )
        )
    )


def _client(session) -> TestClient:
    app.dependency_overrides[get_session] = lambda: session
    return TestClient(app)


def test_v19x_catalog_counts_and_exact_alchemy_formulas(session) -> None:
    expected_counts = {
        Material: 91,
        IngredientGroup: 7,
        IngredientGroupMember: 35,
        Recipe: 19,
        RecipeIngredientSlot: 76,
        RecipeIngredientOption: 87,
    }
    for model, count in expected_counts.items():
        assert session.scalar(
            select(func.count()).select_from(model).where(model.active.is_(True))
        ) == count
    assert session.scalar(select(func.count()).select_from(Source)) == 221

    expected = {
        "clear-liquid-reagent": [
            [("purified-water", 1), ("distilled-water", 1)],
            [("salt", 1)],
            [("dawn-herb", 1)],
            [("wild-grass", 1), ("weed", 1)],
        ],
        "pure-powder-reagent": [
            [("purified-water", 1)],
            [("sugar", 1)],
            [("silver-azalea", 1)],
            [("wild-grass", 1), ("weed", 1)],
        ],
        "defense-elixir": [
            [("clear-liquid-reagent", 1)],
            [("ash-sap", 6)],
            [("pig-blood", 5)],
            [("purified-water", 3)],
        ],
        "concentration-elixir": [
            [("clear-liquid-reagent", 1)],
            [("cloud-mushroom", 3)],
            [("bear-blood", 3)],
            [("wild-grass", 2), ("weed", 8)],
        ],
    }
    for slug, formula in expected.items():
        recipe = get_knowledge_recipe(session, slug)
        assert recipe is not None
        assert recipe.process_type == "alchemy"
        assert (recipe.required_skill_tier, recipe.required_skill_level) == (
            "beginner",
            1,
        )
        assert recipe.verification_status == "verified"
        assert recipe.last_verified_at.isoformat() == "2026-09-12"
        assert _formula(session, slug) == formula


def test_alchemy_evidence_counts_and_pure_powder_source_boundary(session) -> None:
    evidence = list(
        session.scalars(
            select(Evidence).where(
                Evidence.entity_type.in_(
                    {
                        "ingredient_group",
                        "recipe",
                        "recipe_ingredient_option",
                    }
                ),
                Evidence.active.is_(True),
            )
        )
    )
    assert len(evidence) == 292
    assert all(row.verification_status == "verified" for row in evidence)

    pure_rows = [
        row
        for row in evidence
        if row.entity_id.startswith("pure-powder-reagent")
    ]
    advanced_claims = {
        row.claim_key
        for row in pure_rows
        if row.source_id == "alchemy-advanced-guide"
    }
    assert advanced_claims == {"required_skill"}
    assert "alchemy-advanced-guide" not in _source_ids(
        session, "recipe.pure-powder-reagent.formula"
    )
    assert all(
        row.source_id != "alchemy-advanced-guide"
        for row in pure_rows
        if row.claim_key == "required_quantity"
    )


def test_alchemy_options_preserve_or_without_blood_substitution(session) -> None:
    clear = get_knowledge_recipe(session, "clear-liquid-reagent")
    pure = get_knowledge_recipe(session, "pure-powder-reagent")
    defense = get_knowledge_recipe(session, "defense-elixir")
    concentration = get_knowledge_recipe(session, "concentration-elixir")
    assert clear is not None and pure is not None
    assert defense is not None and concentration is not None

    assert [option.material_key for option in clear.ingredient_slots[0].options] == [
        "purified-water",
        "distilled-water",
    ]
    assert [
        option.material_key for option in pure.ingredient_slots[-1].options
    ] == ["wild-grass", "weed"]
    assert all(
        option.target_type == "material"
        for recipe in (defense, concentration)
        for slot in recipe.ingredient_slots
        for option in slot.options
    )
    assert defense.ingredient_slots[2].options[0].material_key == "pig-blood"
    assert concentration.ingredient_slots[2].options[0].material_key == "bear-blood"
    assert all(
        option.ingredient_group is None
        for recipe in (defense, concentration)
        for slot in recipe.ingredient_slots
        for option in slot.options
    )


def test_recipe_process_type_validation_accepts_only_cooking_and_alchemy() -> None:
    base = {
        "slug": "process-validation",
        "name_ko": "공정 검증",
        "result_material_key": "salt",
        "last_verified_at": "2026-09-12",
    }
    for process_type in ("cooking", "alchemy"):
        assert RecipeSeed.model_validate(
            {**base, "process_type": process_type}
        ).process_type == process_type

    unsupported = (
        "processing",
        "simple_alchemy",
        "simple_cooking",
        "heating",
        "grinding",
        "shaking",
        "manufacturing",
        "imperial_alchemy",
    )
    for process_type in unsupported:
        with pytest.raises(ValidationError, match="unsupported Recipe process type"):
            RecipeSeed.model_validate({**base, "process_type": process_type})


@pytest.mark.parametrize(
    ("slug", "expected"),
    [
        (
            "clear-liquid-reagent",
            {
                "purified-water": 10,
                "distilled-water": 10,
                "salt": 10,
                "dawn-herb": 10,
                "wild-grass": 10,
                "weed": 10,
            },
        ),
        (
            "pure-powder-reagent",
            {
                "purified-water": 10,
                "sugar": 10,
                "silver-azalea": 10,
                "wild-grass": 10,
                "weed": 10,
            },
        ),
        (
            "defense-elixir",
            {
                "clear-liquid-reagent": 10,
                "ash-sap": 60,
                "pig-blood": 50,
                "purified-water": 30,
            },
        ),
        (
            "concentration-elixir",
            {
                "clear-liquid-reagent": 10,
                "cloud-mushroom": 30,
                "bear-blood": 30,
                "wild-grass": 20,
                "weed": 80,
            },
        ),
    ],
)
def test_alchemy_stateless_calculation_scales_each_option(
    session, slug: str, expected: dict[str, int]
) -> None:
    client = _client(session)
    try:
        response = client.post(
            f"/api/calculations/recipes/{slug}",
            json={"attempt_count": 10},
        )
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert response.status_code == 200
    payload = response.json()
    assert payload["process_type"] == "alchemy"
    assert {
        option["material_key"]: option["total_required_quantity"]
        for slot in payload["ingredient_slots"]
        for option in slot["options"]
    } == expected
    assert "selected_option" not in payload
    assert "result_quantity" not in payload


def test_existing_cooking_calculation_contract_adds_process_type_only(session) -> None:
    client = _client(session)
    try:
        response = client.post(
            "/api/calculations/recipes/beer",
            json={"attempt_count": 1},
        )
    finally:
        app.dependency_overrides.clear()
        client.close()
    assert response.status_code == 200
    assert response.json()["process_type"] == "cooking"


def test_alchemy_search_dependency_and_material_projections(session) -> None:
    results = search_knowledge(session, "맑은 액체 시약", limit=50)
    assert (results[0].resource_type, results[0].slug) == (
        "material",
        "clear-liquid-reagent",
    )
    recipe_result = next(
        item
        for item in results
        if item.resource_type == "recipe"
        and item.slug == "clear-liquid-reagent"
    )
    assert recipe_result.category == "alchemy"

    dependencies = get_recipe_dependencies(session, "clear-liquid-reagent")
    assert dependencies is not None
    assert dependencies.direct_upstream == []
    assert [
        (edge.consumer_recipe_slug, edge.required_quantity)
        for edge in dependencies.direct_downstream
    ] == [("concentration-elixir", 1), ("defense-elixir", 1)]
    assert all(
        edge.producer_process_type == edge.consumer_process_type == "alchemy"
        for edge in dependencies.direct_downstream
    )

    material = get_knowledge_material(session, "clear-liquid-reagent")
    assert material is not None
    assert [
        (item.recipe_slug, item.process_type)
        for item in material.produced_by_recipes
    ] == [("clear-liquid-reagent", "alchemy")]
    assert [
        (item.recipe_slug, item.required_quantity, item.process_type)
        for item in material.explicit_recipe_usages
    ] == [
        ("concentration-elixir", 1, "alchemy"),
        ("defense-elixir", 1, "alchemy"),
    ]


def test_alchemy_calculation_is_personal_state_independent_and_read_only(session) -> None:
    material = session.scalar(
        select(Material).where(Material.key == "clear-liquid-reagent")
    )
    assert material is not None
    client = _client(session)
    try:
        before = client.post(
            "/api/calculations/recipes/defense-elixir",
            json={"attempt_count": 10},
        ).json()
        session.add(
            UserMaterialInventory(
                material_id=material.id,
                quantity=999999,
                note="must not affect alchemy calculation",
                updated_at=datetime(2026, 9, 12, tzinfo=UTC),
            )
        )
        session.commit()
        table_counts = {
            model: session.scalar(select(func.count()).select_from(model))
            for model in (
                Material,
                Recipe,
                RecipeIngredientSlot,
                RecipeIngredientOption,
                Evidence,
                UserMaterialInventory,
            )
        }
        after = client.post(
            "/api/calculations/recipes/defense-elixir",
            json={"attempt_count": 10},
        ).json()
        assert {
            model: session.scalar(select(func.count()).select_from(model))
            for model in table_counts
        } == table_counts
    finally:
        app.dependency_overrides.clear()
        client.close()
    assert after == before


def test_v19x_reimport_preserves_numeric_ids_and_is_idempotent(session) -> None:
    def identities():
        return {
            "materials": {
                row.key: row.id
                for row in session.scalars(
                    select(Material).where(Material.key.in_(ALCHEMY_SLUGS))
                )
            },
            "recipes": {
                row.slug: row.id
                for row in session.scalars(
                    select(Recipe).where(Recipe.slug.in_(ALCHEMY_SLUGS))
                )
            },
            "slots": {
                row.seed_key: row.id
                for row in session.scalars(
                    select(RecipeIngredientSlot).where(
                        RecipeIngredientSlot.seed_key.startswith(
                            "clear-liquid-reagent."
                        )
                    )
                )
            },
            "options": {
                row.seed_key: row.id
                for row in session.scalars(
                    select(RecipeIngredientOption).where(
                        RecipeIngredientOption.seed_key.startswith(
                            "clear-liquid-reagent."
                        )
                    )
                )
            },
            "evidence": {
                row.seed_key: row.id
                for row in session.scalars(
                    select(Evidence).where(
                        Evidence.seed_key.startswith(
                            "recipe.clear-liquid-reagent."
                        )
                    )
                )
            },
        }

    before = identities()
    import_seed(session, DATA)
    import_seed(session, DATA)
    assert identities() == before


def test_alchemy_ai_export_is_generic_and_declares_model_boundaries(session) -> None:
    exports = build_ai_exports(session)
    manifest = __import__("json").loads(exports["manifest.json"])
    assert manifest["schema_version"] == 3
    assert (
        manifest["content_count"],
        manifest["project_count"],
        manifest["recipe_count"],
        manifest["material_count"],
        len(exports),
    ) == (294, 1, 19, 91, 407)

    page = exports["recipes/clear-liquid-reagent.md"]
    assert "## Recipe Requirement" in page
    assert "## Cooking Requirement" not in page
    for text in (
        "required_quantity is the canonical full formulation quantity for one attempt.",
        "Reduced-input probabilistic success is not modeled.",
        "Output quantity and special-result probability are not modeled.",
        "Alchemy level/mastery output effects are not modeled.",
        'producer_process_type: "alchemy"',
        'consumer_process_type: "alchemy"',
    ):
        assert text in page
    assert "one cooking attempt" not in page
