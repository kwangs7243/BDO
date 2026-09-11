<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 소금

## Identity

- key: "salt"
- name_ko: "소금"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

### `dressing.ingredient.salt.option.salt`

- recipe_slug: "dressing"
- recipe_name_ko: "드레싱"
- process_type: "cooking"
- slot_seed_key: "dressing.ingredient.salt"
- slot_label: "소금"
- slot_order_no: 4
- option_seed_key: "dressing.ingredient.salt.option.salt"
- option_order_no: 1
- required_quantity: 2.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/dressing.md"

### `grilled-bird-meat.ingredient.salt.option.salt`

- recipe_slug: "grilled-bird-meat"
- recipe_name_ko: "새구이"
- process_type: "cooking"
- slot_seed_key: "grilled-bird-meat.ingredient.salt"
- slot_label: "소금"
- slot_order_no: 4
- option_seed_key: "grilled-bird-meat.ingredient.salt.option.salt"
- option_order_no: 1
- required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/grilled-bird-meat.md"

### `grilled-sausage.ingredient.salt.option.salt`

- recipe_slug: "grilled-sausage"
- recipe_name_ko: "구운 소시지"
- process_type: "cooking"
- slot_seed_key: "grilled-sausage.ingredient.salt"
- slot_label: "소금"
- slot_order_no: 3
- option_seed_key: "grilled-sausage.ingredient.salt.option.salt"
- option_order_no: 1
- required_quantity: 2.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/grilled-sausage.md"

### `omelet.ingredient.salt.option.salt`

- recipe_slug: "omelet"
- recipe_name_ko: "오믈렛"
- process_type: "cooking"
- slot_seed_key: "omelet.ingredient.salt"
- slot_label: "소금"
- slot_order_no: 4
- option_seed_key: "omelet.ingredient.salt.option.salt"
- option_order_no: 1
- required_quantity: 2.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/omelet.md"

### `steak.ingredient.salt.option.salt`

- recipe_slug: "steak"
- recipe_name_ko: "스테이크"
- process_type: "cooking"
- slot_seed_key: "steak.ingredient.salt"
- slot_label: "소금"
- slot_order_no: 4
- option_seed_key: "steak.ingredient.salt.option.salt"
- option_order_no: 1
- required_quantity: 2.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/steak.md"

### `sute-tea.ingredient.salt.option.salt`

- recipe_slug: "sute-tea"
- recipe_name_ko: "수테차"
- process_type: "cooking"
- slot_seed_key: "sute-tea.ingredient.salt"
- slot_label: "소금"
- slot_order_no: 3
- option_seed_key: "sute-tea.ingredient.salt.option.salt"
- option_order_no: 1
- required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/sute-tea.md"

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
