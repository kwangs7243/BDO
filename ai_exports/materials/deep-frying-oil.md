<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 튀김용 오일

## Identity

- key: "deep-frying-oil"
- name_ko: "튀김용 오일"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

### `grilled-bird-meat.ingredient.oil.option.deep-frying-oil`

- recipe_slug: "grilled-bird-meat"
- recipe_name_ko: "새구이"
- process_type: "cooking"
- slot_seed_key: "grilled-bird-meat.ingredient.oil"
- slot_label: "오일"
- slot_order_no: 2
- option_seed_key: "grilled-bird-meat.ingredient.oil.option.deep-frying-oil"
- option_order_no: 1
- required_quantity: 6.0
- is_alternative: true
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/grilled-bird-meat.md"

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
