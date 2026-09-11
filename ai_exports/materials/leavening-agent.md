<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 발효제

## Identity

- key: "leavening-agent"
- name_ko: "발효제"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

### `beer.ingredient.leavening-agent.option.leavening-agent`

- recipe_slug: "beer"
- recipe_name_ko: "맥주"
- process_type: "cooking"
- slot_seed_key: "beer.ingredient.leavening-agent"
- slot_label: "발효제"
- slot_order_no: 3
- option_seed_key: "beer.ingredient.leavening-agent.option.leavening-agent"
- option_order_no: 1
- required_quantity: 2.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/beer.md"

### `pickled-vegetables.ingredient.leavening-agent.option.leavening-agent`

- recipe_slug: "pickled-vegetables"
- recipe_name_ko: "채소 절임"
- process_type: "cooking"
- slot_seed_key: "pickled-vegetables.ingredient.leavening-agent"
- slot_label: "발효제"
- slot_order_no: 3
- option_seed_key: "pickled-vegetables.ingredient.leavening-agent.option.leavening-agent"
- option_order_no: 1
- required_quantity: 2.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/pickled-vegetables.md"

### `vinegar.ingredient.leavening-agent.option.leavening-agent`

- recipe_slug: "vinegar"
- recipe_name_ko: "식초"
- process_type: "cooking"
- slot_seed_key: "vinegar.ingredient.leavening-agent"
- slot_label: "발효제"
- slot_order_no: 3
- option_seed_key: "vinegar.ingredient.leavening-agent.option.leavening-agent"
- option_order_no: 1
- required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/vinegar.md"

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
