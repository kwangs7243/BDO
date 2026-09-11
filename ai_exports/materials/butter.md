<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 버터

## Identity

- key: "butter"
- name_ko: "버터"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

### `sute-tea.ingredient.butter.option.butter`

- recipe_slug: "sute-tea"
- recipe_name_ko: "수테차"
- process_type: "cooking"
- slot_seed_key: "sute-tea.ingredient.butter"
- slot_label: "버터"
- slot_order_no: 4
- option_seed_key: "sute-tea.ingredient.butter.option.butter"
- option_order_no: 1
- required_quantity: 2.0
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
