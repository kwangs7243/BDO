<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 잡초

## Identity

- key: "weed"
- name_ko: "잡초"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

### `clear-liquid-reagent.ingredient.wild-herb.option.weed`

- recipe_slug: "clear-liquid-reagent"
- recipe_name_ko: "맑은 액체 시약"
- process_type: "alchemy"
- slot_seed_key: "clear-liquid-reagent.ingredient.wild-herb"
- slot_label: "야생 약초"
- slot_order_no: 4
- option_seed_key: "clear-liquid-reagent.ingredient.wild-herb.option.weed"
- option_order_no: 2
- required_quantity: 1.0
- is_alternative: true
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-12"
- relative_path: "../recipes/clear-liquid-reagent.md"

### `concentration-elixir.ingredient.wild-herb.option.weed`

- recipe_slug: "concentration-elixir"
- recipe_name_ko: "집중의 비약"
- process_type: "alchemy"
- slot_seed_key: "concentration-elixir.ingredient.wild-herb"
- slot_label: "야생 약초"
- slot_order_no: 4
- option_seed_key: "concentration-elixir.ingredient.wild-herb.option.weed"
- option_order_no: 2
- required_quantity: 8.0
- is_alternative: true
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-12"
- relative_path: "../recipes/concentration-elixir.md"

### `pure-powder-reagent.ingredient.wild-herb.option.weed`

- recipe_slug: "pure-powder-reagent"
- recipe_name_ko: "순수한 가루 시약"
- process_type: "alchemy"
- slot_seed_key: "pure-powder-reagent.ingredient.wild-herb"
- slot_label: "야생 약초"
- slot_order_no: 4
- option_seed_key: "pure-powder-reagent.ingredient.wild-herb.option.weed"
- option_order_no: 2
- required_quantity: 1.0
- is_alternative: true
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-12"
- relative_path: "../recipes/pure-powder-reagent.md"

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
