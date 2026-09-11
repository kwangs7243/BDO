<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 치즈

## Identity

- key: "cheese"
- name_ko: "치즈"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

### `meat-sandwich.ingredient.cheese.option.cheese`

- recipe_slug: "meat-sandwich"
- recipe_name_ko: "미트 샌드위치"
- process_type: "cooking"
- slot_seed_key: "meat-sandwich.ingredient.cheese"
- slot_label: "치즈"
- slot_order_no: 4
- option_seed_key: "meat-sandwich.ingredient.cheese.option.cheese"
- option_order_no: 1
- required_quantity: 3.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/meat-sandwich.md"

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
