<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 맑은 액체 시약

## Identity

- key: "clear-liquid-reagent"
- name_ko: "맑은 액체 시약"
- unit: "개"

## Produced By Recipes

### `clear-liquid-reagent`

- recipe_slug: "clear-liquid-reagent"
- recipe_name_ko: "맑은 액체 시약"
- process_type: "alchemy"
- required_skill_tier: "beginner"
- required_skill_level: 1
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- relative_path: "../recipes/clear-liquid-reagent.md"

## Explicit Recipe Usages

### `concentration-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent`

- recipe_slug: "concentration-elixir"
- recipe_name_ko: "집중의 비약"
- process_type: "alchemy"
- slot_seed_key: "concentration-elixir.ingredient.clear-liquid-reagent"
- slot_label: "맑은 액체 시약"
- slot_order_no: 1
- option_seed_key: "concentration-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent"
- option_order_no: 1
- required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-12"
- relative_path: "../recipes/concentration-elixir.md"

### `defense-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent`

- recipe_slug: "defense-elixir"
- recipe_name_ko: "방어의 비약"
- process_type: "alchemy"
- slot_seed_key: "defense-elixir.ingredient.clear-liquid-reagent"
- slot_label: "맑은 액체 시약"
- slot_order_no: 1
- option_seed_key: "defense-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent"
- option_order_no: 1
- required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-12"
- relative_path: "../recipes/defense-elixir.md"

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
