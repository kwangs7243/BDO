<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 부드러운 빵

## Identity

- key: "soft-bread"
- name_ko: "부드러운 빵"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

### `frank-sandwich.ingredient.soft-bread.option.soft-bread`

- recipe_slug: "frank-sandwich"
- recipe_name_ko: "프랭크 샌드위치"
- process_type: "cooking"
- slot_seed_key: "frank-sandwich.ingredient.soft-bread"
- slot_label: "부드러운 빵"
- slot_order_no: 2
- option_seed_key: "frank-sandwich.ingredient.soft-bread.option.soft-bread"
- option_order_no: 1
- required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/frank-sandwich.md"

### `ham-sandwich.ingredient.soft-bread.option.soft-bread`

- recipe_slug: "ham-sandwich"
- recipe_name_ko: "햄 샌드위치"
- process_type: "cooking"
- slot_seed_key: "ham-sandwich.ingredient.soft-bread"
- slot_label: "부드러운 빵"
- slot_order_no: 2
- option_seed_key: "ham-sandwich.ingredient.soft-bread.option.soft-bread"
- option_order_no: 1
- required_quantity: 2.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/ham-sandwich.md"

### `meat-sandwich.ingredient.soft-bread.option.soft-bread`

- recipe_slug: "meat-sandwich"
- recipe_name_ko: "미트 샌드위치"
- process_type: "cooking"
- slot_seed_key: "meat-sandwich.ingredient.soft-bread"
- slot_label: "부드러운 빵"
- slot_order_no: 2
- option_seed_key: "meat-sandwich.ingredient.soft-bread.option.soft-bread"
- option_order_no: 1
- required_quantity: 1.0
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
