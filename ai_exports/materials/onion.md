<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 양파

## Identity

- key: "onion"
- name_ko: "양파"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

### `grilled-sausage.ingredient.onion.option.onion`

- recipe_slug: "grilled-sausage"
- recipe_name_ko: "구운 소시지"
- process_type: "cooking"
- slot_seed_key: "grilled-sausage.ingredient.onion"
- slot_label: "양파"
- slot_order_no: 2
- option_seed_key: "grilled-sausage.ingredient.onion.option.onion"
- option_order_no: 1
- required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/grilled-sausage.md"

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
