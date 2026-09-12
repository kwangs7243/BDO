<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 식초

## Identity

- key: "vinegar"
- name_ko: "식초"
- unit: "개"

## Produced By Recipes

### `vinegar`

- recipe_slug: "vinegar"
- recipe_name_ko: "식초"
- process_type: "cooking"
- required_skill_tier: "beginner"
- required_skill_level: 1
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- relative_path: "../recipes/vinegar.md"

## Explicit Recipe Usages

### `pickled-vegetables.ingredient.vinegar.option.vinegar`

- recipe_slug: "pickled-vegetables"
- recipe_name_ko: "채소 절임"
- process_type: "cooking"
- slot_seed_key: "pickled-vegetables.ingredient.vinegar"
- slot_label: "식초"
- slot_order_no: 2
- option_seed_key: "pickled-vegetables.ingredient.vinegar.option.vinegar"
- option_order_no: 1
- required_quantity: 4.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/pickled-vegetables.md"

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
