<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 우유

## Identity

- key: "milk"
- name_ko: "우유"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

### `sute-tea.ingredient.milk.option.milk`

- recipe_slug: "sute-tea"
- recipe_name_ko: "수테차"
- process_type: "cooking"
- slot_seed_key: "sute-tea.ingredient.milk"
- slot_label: "우유"
- slot_order_no: 2
- option_seed_key: "sute-tea.ingredient.milk.option.milk"
- option_order_no: 1
- required_quantity: 3.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/sute-tea.md"

### `white-sauce.ingredient.milk.option.milk`

- recipe_slug: "white-sauce"
- recipe_name_ko: "화이트소스"
- process_type: "cooking"
- slot_seed_key: "white-sauce.ingredient.milk"
- slot_label: "우유"
- slot_order_no: 3
- option_seed_key: "white-sauce.ingredient.milk.option.milk"
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
