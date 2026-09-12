<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 식용벌꿀

## Identity

- key: "edible-honey"
- name_ko: "식용벌꿀"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

### `tea-with-fine-scent.ingredient.edible-honey.option.edible-honey`

- recipe_slug: "tea-with-fine-scent"
- recipe_name_ko: "향이 좋은 차"
- process_type: "cooking"
- slot_seed_key: "tea-with-fine-scent.ingredient.edible-honey"
- slot_label: "식용벌꿀"
- slot_order_no: 4
- option_seed_key: "tea-with-fine-scent.ingredient.edible-honey.option.edible-honey"
- option_order_no: 1
- required_quantity: 3.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/tea-with-fine-scent.md"

## Ingredient Group Memberships

- None

## Ingredient Group Candidate Recipe Usages

- None

## Project Requirements

- None

## Semantics

- Material identity itself has no invented aggregate verification status.
- Explicit Material usage and IngredientGroup candidate usage are different.
- Group membership does not mean the material is mandatory.
- Group required_quantity belongs to the Recipe group option.
- Project acquisition sources are scoped to that ProjectMaterial requirement.
- No personal inventory is included.
- No market price or profitability is included.
