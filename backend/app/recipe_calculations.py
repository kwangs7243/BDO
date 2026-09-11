from __future__ import annotations

from sqlalchemy.orm import Session

from app.knowledge import get_knowledge_recipe
from app.schemas import (
    KnowledgeRecipeOut,
    RecipeCalculationIngredientGroupOut,
    RecipeCalculationOptionOut,
    RecipeCalculationOut,
    RecipeCalculationRequest,
    RecipeCalculationSlotOut,
)


def scale_recipe_requirements(
    recipe: KnowledgeRecipeOut,
    attempt_count: int,
) -> RecipeCalculationOut:
    """Scale every canonical option independently without resolving alternatives."""

    slots: list[RecipeCalculationSlotOut] = []
    for slot in recipe.ingredient_slots:
        options: list[RecipeCalculationOptionOut] = []
        for option in slot.options:
            ingredient_group = None
            if option.ingredient_group is not None:
                group = option.ingredient_group
                ingredient_group = RecipeCalculationIngredientGroupOut(
                    key=group.key,
                    name_ko=group.name_ko,
                    verification_status=group.verification_status,
                    last_verified_at=group.last_verified_at,
                    members=group.members,
                )
            options.append(
                RecipeCalculationOptionOut(
                    option_seed_key=option.seed_key,
                    target_type=option.target_type,
                    per_attempt_quantity=option.required_quantity,
                    total_required_quantity=option.required_quantity * attempt_count,
                    order_no=option.order_no,
                    notes=option.notes,
                    material_key=option.material_key,
                    material_name_ko=option.material_name_ko,
                    unit=option.unit,
                    ingredient_group=ingredient_group,
                )
            )
        slots.append(
            RecipeCalculationSlotOut(
                slot_seed_key=slot.seed_key,
                label=slot.label,
                order_no=slot.order_no,
                notes=slot.notes,
                options=options,
            )
        )

    return RecipeCalculationOut(
        recipe_slug=recipe.slug,
        name_ko=recipe.name_ko,
        result_material_key=recipe.result_material_key,
        result_material_name_ko=recipe.result_material_name_ko,
        result_unit=recipe.result_unit,
        attempt_count=attempt_count,
        required_skill_tier=recipe.required_skill_tier,
        required_skill_level=recipe.required_skill_level,
        verification_status=recipe.verification_status,
        last_verified_at=recipe.last_verified_at,
        ingredient_slots=slots,
    )


def calculate_recipe(
    session: Session,
    slug: str,
    request: RecipeCalculationRequest,
) -> RecipeCalculationOut:
    """Resolve canonical Recipe knowledge and calculate without reading user state."""

    recipe = get_knowledge_recipe(session, slug)
    if recipe is None:
        raise LookupError(slug)
    return scale_recipe_requirements(recipe, request.attempt_count)
