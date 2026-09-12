<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 증류수

## Identity

- key: "distilled-water"
- name_ko: "증류수"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

### `clear-liquid-reagent.ingredient.water.option.distilled-water`

- recipe_slug: "clear-liquid-reagent"
- recipe_name_ko: "맑은 액체 시약"
- process_type: "alchemy"
- slot_seed_key: "clear-liquid-reagent.ingredient.water"
- slot_label: "물"
- slot_order_no: 1
- option_seed_key: "clear-liquid-reagent.ingredient.water.option.distilled-water"
- option_order_no: 2
- required_quantity: 1.0
- is_alternative: true
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-12"
- relative_path: "../recipes/clear-liquid-reagent.md"

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
