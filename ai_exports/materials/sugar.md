<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 설탕

## Identity

- key: "sugar"
- name_ko: "설탕"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

### `beer.ingredient.sugar.option.sugar`

- recipe_slug: "beer"
- recipe_name_ko: "맥주"
- process_type: "cooking"
- slot_seed_key: "beer.ingredient.sugar"
- slot_label: "설탕"
- slot_order_no: 4
- option_seed_key: "beer.ingredient.sugar.option.sugar"
- option_order_no: 1
- required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/beer.md"

### `pickled-vegetables.ingredient.sugar.option.sugar`

- recipe_slug: "pickled-vegetables"
- recipe_name_ko: "채소 절임"
- process_type: "cooking"
- slot_seed_key: "pickled-vegetables.ingredient.sugar"
- slot_label: "설탕"
- slot_order_no: 4
- option_seed_key: "pickled-vegetables.ingredient.sugar.option.sugar"
- option_order_no: 1
- required_quantity: 2.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/pickled-vegetables.md"

### `pure-powder-reagent.ingredient.sugar.option.sugar`

- recipe_slug: "pure-powder-reagent"
- recipe_name_ko: "순수한 가루 시약"
- process_type: "alchemy"
- slot_seed_key: "pure-powder-reagent.ingredient.sugar"
- slot_label: "설탕"
- slot_order_no: 2
- option_seed_key: "pure-powder-reagent.ingredient.sugar.option.sugar"
- option_order_no: 1
- required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-12"
- relative_path: "../recipes/pure-powder-reagent.md"

### `red-sauce.ingredient.sugar.option.sugar`

- recipe_slug: "red-sauce"
- recipe_name_ko: "레드소스"
- process_type: "cooking"
- slot_seed_key: "red-sauce.ingredient.sugar"
- slot_label: "설탕"
- slot_order_no: 4
- option_seed_key: "red-sauce.ingredient.sugar.option.sugar"
- option_order_no: 1
- required_quantity: 2.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/red-sauce.md"

### `vinegar.ingredient.sugar.option.sugar`

- recipe_slug: "vinegar"
- recipe_name_ko: "식초"
- process_type: "cooking"
- slot_seed_key: "vinegar.ingredient.sugar"
- slot_label: "설탕"
- slot_order_no: 4
- option_seed_key: "vinegar.ingredient.sugar.option.sugar"
- option_order_no: 1
- required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/vinegar.md"

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
