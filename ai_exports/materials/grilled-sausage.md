<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 구운 소시지

## Identity

- key: "grilled-sausage"
- name_ko: "구운 소시지"
- unit: "개"

## Produced By Recipes

### `grilled-sausage`

- recipe_slug: "grilled-sausage"
- recipe_name_ko: "구운 소시지"
- process_type: "cooking"
- required_skill_tier: "beginner"
- required_skill_level: 6
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- relative_path: "../recipes/grilled-sausage.md"

## Explicit Recipe Usages

### `frank-sandwich.ingredient.sausage.option.grilled-sausage`

- recipe_slug: "frank-sandwich"
- recipe_name_ko: "프랭크 샌드위치"
- process_type: "cooking"
- slot_seed_key: "frank-sandwich.ingredient.sausage"
- slot_label: "소시지"
- slot_order_no: 1
- option_seed_key: "frank-sandwich.ingredient.sausage.option.grilled-sausage"
- option_order_no: 1
- required_quantity: 2.0
- is_alternative: true
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/frank-sandwich.md"

### `ham-sandwich.ingredient.sausage.option.grilled-sausage`

- recipe_slug: "ham-sandwich"
- recipe_name_ko: "햄 샌드위치"
- process_type: "cooking"
- slot_seed_key: "ham-sandwich.ingredient.sausage"
- slot_label: "소시지"
- slot_order_no: 1
- option_seed_key: "ham-sandwich.ingredient.sausage.option.grilled-sausage"
- option_order_no: 1
- required_quantity: 2.0
- is_alternative: true
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/ham-sandwich.md"

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
