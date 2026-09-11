<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 레드소스

## Identity

- key: "red-sauce"
- name_ko: "레드소스"
- unit: "개"

## Produced By Recipes

### `red-sauce`

- recipe_slug: "red-sauce"
- recipe_name_ko: "레드소스"
- process_type: "cooking"
- required_skill_tier: "beginner"
- required_skill_level: 1
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- relative_path: "../recipes/red-sauce.md"

## Explicit Recipe Usages

### `frank-sandwich.ingredient.red-sauce.option.red-sauce`

- recipe_slug: "frank-sandwich"
- recipe_name_ko: "프랭크 샌드위치"
- process_type: "cooking"
- slot_seed_key: "frank-sandwich.ingredient.red-sauce"
- slot_label: "레드소스"
- slot_order_no: 4
- option_seed_key: "frank-sandwich.ingredient.red-sauce.option.red-sauce"
- option_order_no: 1
- required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/frank-sandwich.md"

### `steak.ingredient.red-sauce.option.red-sauce`

- recipe_slug: "steak"
- recipe_name_ko: "스테이크"
- process_type: "cooking"
- slot_seed_key: "steak.ingredient.red-sauce"
- slot_label: "레드소스"
- slot_order_no: 3
- option_seed_key: "steak.ingredient.red-sauce.option.red-sauce"
- option_order_no: 1
- required_quantity: 2.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/steak.md"

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
