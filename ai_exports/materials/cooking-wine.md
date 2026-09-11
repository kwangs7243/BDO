<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 조리용 와인

## Identity

- key: "cooking-wine"
- name_ko: "조리용 와인"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

### `grilled-bird-meat.ingredient.cooking-wine.option.cooking-wine`

- recipe_slug: "grilled-bird-meat"
- recipe_name_ko: "새구이"
- process_type: "cooking"
- slot_seed_key: "grilled-bird-meat.ingredient.cooking-wine"
- slot_label: "조리용 와인"
- slot_order_no: 3
- option_seed_key: "grilled-bird-meat.ingredient.cooking-wine.option.cooking-wine"
- option_order_no: 1
- required_quantity: 2.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/grilled-bird-meat.md"

### `white-sauce.ingredient.cooking-wine.option.cooking-wine`

- recipe_slug: "white-sauce"
- recipe_name_ko: "화이트소스"
- process_type: "cooking"
- slot_seed_key: "white-sauce.ingredient.cooking-wine"
- slot_label: "조리용 와인"
- slot_order_no: 4
- option_seed_key: "white-sauce.ingredient.cooking-wine.option.cooking-wine"
- option_order_no: 1
- required_quantity: 2.0
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
