from __future__ import annotations

from datetime import UTC, datetime

from fastapi.testclient import TestClient
from sqlalchemy import func, select

from app.database import get_session
from app.knowledge import get_knowledge_material, list_knowledge_materials, search_knowledge
from app.main import app
from app.models import (
    Evidence,
    IngredientGroup,
    IngredientGroupMember,
    Material,
    Project,
    ProjectMaterial,
    ProjectMaterialSource,
    Recipe,
    RecipeIngredientOption,
    RecipeIngredientSlot,
    UserMaterialInventory,
)


def _client(session):
    def override_session():
        yield session

    app.dependency_overrides[get_session] = override_session
    return TestClient(app)


def test_all_active_materials_are_projected_with_expected_relation_counts(session) -> None:
    materials = list_knowledge_materials(session)

    assert len(materials) == 91
    assert sum(len(item.produced_by_recipes) for item in materials) == 19
    assert sum(len(item.explicit_recipe_usages) for item in materials) == 71
    assert sum(len(item.ingredient_group_memberships) for item in materials) == 35
    assert sum(len(item.group_recipe_usages) for item in materials) == 99
    assert sum(len(item.project_requirements) for item in materials) == 9
    assert sum(
        len(requirement.sources)
        for item in materials
        for requirement in item.project_requirements
    ) == 9
    assert all(not hasattr(item, "verification_status") for item in materials)


def test_red_sauce_projects_producer_and_explicit_recipe_usages(session) -> None:
    material = get_knowledge_material(session, "red-sauce")

    assert material is not None
    assert [item.recipe_slug for item in material.produced_by_recipes] == ["red-sauce"]
    assert {
        item.recipe_slug: item.required_quantity
        for item in material.explicit_recipe_usages
    } == {"steak": 2, "frank-sandwich": 1}
    assert material.ingredient_group_memberships == []
    assert material.group_recipe_usages == []
    assert material.project_requirements == []


def test_beef_group_membership_expands_only_as_candidate_usage(session) -> None:
    material = get_knowledge_material(session, "beef")

    assert material is not None
    assert material.produced_by_recipes == []
    assert material.explicit_recipe_usages == []
    assert [item.group_key for item in material.ingredient_group_memberships] == ["meat"]
    assert material.ingredient_group_memberships[0].sources
    assert {
        item.recipe_slug: item.group_required_quantity
        for item in material.group_recipe_usages
    } == {
        "red-sauce": 1,
        "grilled-sausage": 6,
        "steak": 8,
        "meat-sandwich": 7,
    }
    assert all(
        item.usage_semantics == "ingredient_group_candidate"
        for item in material.group_recipe_usages
    )


def test_mineral_water_keeps_explicit_and_group_candidate_semantics_separate(session) -> None:
    material = get_knowledge_material(session, "mineral-water")

    assert material is not None
    assert {
        item.recipe_slug: item.required_quantity
        for item in material.explicit_recipe_usages
    } == {"beer": 6, "red-sauce": 2, "tea-with-fine-scent": 7}
    assert all(item.is_alternative for item in material.explicit_recipe_usages)
    assert [item.group_key for item in material.ingredient_group_memberships] == ["water"]
    assert [
        (item.recipe_slug, item.group_required_quantity, item.usage_semantics)
        for item in material.group_recipe_usages
    ] == [("dressing", 1, "ingredient_group_candidate")]


def test_smoked_sausage_is_an_explicit_alternative_without_invented_producer(session) -> None:
    material = get_knowledge_material(session, "smoked-sausage")

    assert material is not None
    assert material.produced_by_recipes == []
    assert {
        item.recipe_slug: item.required_quantity
        for item in material.explicit_recipe_usages
    } == {"ham-sandwich": 1, "frank-sandwich": 1}
    assert all(item.is_alternative for item in material.explicit_recipe_usages)


def test_project_material_sources_remain_scoped_to_project_requirement(session) -> None:
    material = get_knowledge_material(session, "moon-vein-flax")

    assert material is not None
    assert material.produced_by_recipes == []
    assert material.explicit_recipe_usages == []
    requirement = material.project_requirements[0]
    assert requirement.project_slug == "carrack-advance"
    assert requirement.stage_seed_key == "carrack-advance.stage.body-materials"
    assert requirement.required_quantity == 180
    assert {
        source.content_slug for source in requirement.sources
    } == {
        "oquilla-daily-young-sea-monster-hunter",
        "crow-coin-material-shop",
    }


def test_material_knowledge_api_404_and_inactive_filter(session) -> None:
    inactive = session.scalar(select(Material).where(Material.key == "red-sauce"))
    assert inactive is not None
    inactive.active = False
    session.flush()

    client = _client(session)
    try:
        missing = client.get("/api/knowledge/materials/not-a-material")
        archived = client.get("/api/knowledge/materials/red-sauce")
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert missing.status_code == 404
    assert missing.json() == {"detail": "Material not found"}
    assert archived.status_code == 404


def test_material_knowledge_is_independent_of_personal_inventory(session) -> None:
    before = get_knowledge_material(session, "moon-vein-flax")
    material = session.scalar(select(Material).where(Material.key == "moon-vein-flax"))
    assert before is not None
    assert material is not None
    session.add(
        UserMaterialInventory(
            material_id=material.id,
            quantity=123,
            note="must not enter canonical material knowledge",
            updated_at=datetime(2026, 9, 12, tzinfo=UTC),
        )
    )
    session.commit()

    after = get_knowledge_material(session, "moon-vein-flax")
    assert after == before
    assert "inventory" not in after.model_dump_json()


def test_material_search_identity_precedes_nested_recipe_and_project_matches(session) -> None:
    moon_flax = search_knowledge(session, "moon-vein-flax", limit=50)
    red_sauce = search_knowledge(session, "red-sauce", limit=50)

    assert moon_flax[0].resource_type == "material"
    assert moon_flax[0].slug == "moon-vein-flax"
    assert moon_flax[0].category == "material"
    assert moon_flax[0].summary is None
    assert moon_flax[0].verification_status is None
    assert any(item.resource_type == "project" for item in moon_flax)
    assert red_sauce[0].resource_type == "material"
    assert any(item.resource_type == "recipe" for item in red_sauce)


def test_material_read_and_search_do_not_mutate_canonical_or_personal_tables(session) -> None:
    models = (
        Material,
        Recipe,
        RecipeIngredientSlot,
        RecipeIngredientOption,
        IngredientGroup,
        IngredientGroupMember,
        Project,
        ProjectMaterial,
        ProjectMaterialSource,
        Evidence,
        UserMaterialInventory,
    )
    before = {
        model.__tablename__: session.scalar(select(func.count()).select_from(model))
        for model in models
    }

    assert get_knowledge_material(session, "red-sauce") is not None
    assert search_knowledge(session, "red-sauce", limit=50)

    after = {
        model.__tablename__: session.scalar(select(func.count()).select_from(model))
        for model in models
    }
    assert after == before
