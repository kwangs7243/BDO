<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 올리브 오일

## Identity

- key: "olive-oil"
- name_ko: "올리브 오일"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

### `dressing.ingredient.olive-oil.option.olive-oil`

- recipe_slug: "dressing"
- recipe_name_ko: "드레싱"
- process_type: "cooking"
- slot_seed_key: "dressing.ingredient.olive-oil"
- slot_label: "올리브 오일"
- slot_order_no: 2
- option_seed_key: "dressing.ingredient.olive-oil.option.olive-oil"
- option_order_no: 1
- required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/dressing.md"

### `omelet.ingredient.olive-oil.option.olive-oil`

- recipe_slug: "omelet"
- recipe_name_ko: "오믈렛"
- process_type: "cooking"
- slot_seed_key: "omelet.ingredient.olive-oil"
- slot_label: "올리브 오일"
- slot_order_no: 2
- option_seed_key: "omelet.ingredient.olive-oil.option.olive-oil"
- option_order_no: 1
- required_quantity: 2.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/omelet.md"

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
