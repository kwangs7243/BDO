<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 베이스 소스

## Identity

- key: "base-sauce"
- name_ko: "베이스 소스"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

### `red-sauce.ingredient.base-sauce.option.base-sauce`

- recipe_slug: "red-sauce"
- recipe_name_ko: "레드소스"
- process_type: "cooking"
- slot_seed_key: "red-sauce.ingredient.base-sauce"
- slot_label: "베이스 소스"
- slot_order_no: 1
- option_seed_key: "red-sauce.ingredient.base-sauce.option.base-sauce"
- option_order_no: 1
- required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/red-sauce.md"

### `white-sauce.ingredient.base-sauce.option.base-sauce`

- recipe_slug: "white-sauce"
- recipe_name_ko: "화이트소스"
- process_type: "cooking"
- slot_seed_key: "white-sauce.ingredient.base-sauce"
- slot_label: "베이스 소스"
- slot_order_no: 1
- option_seed_key: "white-sauce.ingredient.base-sauce.option.base-sauce"
- option_order_no: 1
- required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/white-sauce.md"

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
