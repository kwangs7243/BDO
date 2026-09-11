from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.knowledge import get_knowledge_recipe
from app.models import Recipe
from app.schemas import (
    KnowledgeRecipeDependenciesOut,
    KnowledgeRecipeDependencyEdgeOut,
    KnowledgeRecipeOut,
)


def _upstream_sort_key(edge: KnowledgeRecipeDependencyEdgeOut) -> tuple:
    return (
        edge.consumer_slot_order_no,
        edge.consumer_option_order_no,
        edge.producer_recipe_slug,
        edge.consumer_recipe_slug,
    )


def _downstream_sort_key(edge: KnowledgeRecipeDependencyEdgeOut) -> tuple:
    return (
        edge.consumer_recipe_slug,
        edge.consumer_slot_order_no,
        edge.consumer_option_order_no,
        edge.producer_recipe_slug,
    )


def build_recipe_dependency_index(
    recipes: list[KnowledgeRecipeOut],
) -> dict[str, KnowledgeRecipeDependenciesOut]:
    """Derive direct Recipe edges from explicit shared Material identities."""

    ordered_recipes = sorted(recipes, key=lambda recipe: recipe.slug)
    producers_by_material: dict[str, list[KnowledgeRecipeOut]] = {}
    upstream: dict[str, list[KnowledgeRecipeDependencyEdgeOut]] = {}
    downstream: dict[str, list[KnowledgeRecipeDependencyEdgeOut]] = {}

    for recipe in ordered_recipes:
        producers_by_material.setdefault(recipe.result_material_key, []).append(recipe)
        upstream[recipe.slug] = []
        downstream[recipe.slug] = []

    for consumer in ordered_recipes:
        for slot in consumer.ingredient_slots:
            is_alternative = len(slot.options) > 1
            for option in slot.options:
                if (
                    option.target_type != "material"
                    or option.material_key is None
                    or option.material_name_ko is None
                    or option.unit is None
                ):
                    continue
                for producer in producers_by_material.get(option.material_key, []):
                    edge = KnowledgeRecipeDependencyEdgeOut(
                        producer_recipe_slug=producer.slug,
                        producer_recipe_name_ko=producer.name_ko,
                        producer_verification_status=producer.verification_status,
                        consumer_recipe_slug=consumer.slug,
                        consumer_recipe_name_ko=consumer.name_ko,
                        consumer_verification_status=consumer.verification_status,
                        material_key=option.material_key,
                        material_name_ko=option.material_name_ko,
                        unit=option.unit,
                        consumer_slot_seed_key=slot.seed_key,
                        consumer_slot_label=slot.label,
                        consumer_option_seed_key=option.seed_key,
                        required_quantity=option.required_quantity,
                        consumer_slot_order_no=slot.order_no,
                        consumer_option_order_no=option.order_no,
                        is_alternative=is_alternative,
                    )
                    upstream[consumer.slug].append(edge)
                    downstream[producer.slug].append(edge)

    return {
        recipe.slug: KnowledgeRecipeDependenciesOut(
            recipe_slug=recipe.slug,
            recipe_name_ko=recipe.name_ko,
            process_type=recipe.process_type,
            result_material_key=recipe.result_material_key,
            result_material_name_ko=recipe.result_material_name_ko,
            direct_upstream=sorted(upstream[recipe.slug], key=_upstream_sort_key),
            direct_downstream=sorted(downstream[recipe.slug], key=_downstream_sort_key),
        )
        for recipe in ordered_recipes
    }


def get_recipe_dependencies(
    session: Session,
    slug: str,
) -> KnowledgeRecipeDependenciesOut | None:
    """Return the canonical direct dependency projection without personal state."""

    recipes: list[KnowledgeRecipeOut] = []
    for recipe_slug in session.scalars(
        select(Recipe.slug).where(Recipe.active.is_(True)).order_by(Recipe.slug)
    ):
        recipe = get_knowledge_recipe(session, recipe_slug)
        if recipe is None:
            raise RuntimeError(f"Canonical Recipe disappeared during projection: {recipe_slug}")
        recipes.append(recipe)
    return build_recipe_dependency_index(recipes).get(slug)
