<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 정제수

## Identity

- key: "purified-water"
- name_ko: "정제수"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

### `beer.ingredient.water.option.purified-water`

- recipe_slug: "beer"
- recipe_name_ko: "맥주"
- process_type: "cooking"
- slot_seed_key: "beer.ingredient.water"
- slot_label: "물"
- slot_order_no: 2
- option_seed_key: "beer.ingredient.water.option.purified-water"
- option_order_no: 2
- required_quantity: 3.0
- is_alternative: true
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/beer.md"

### `clear-liquid-reagent.ingredient.water.option.purified-water`

- recipe_slug: "clear-liquid-reagent"
- recipe_name_ko: "맑은 액체 시약"
- process_type: "alchemy"
- slot_seed_key: "clear-liquid-reagent.ingredient.water"
- slot_label: "물"
- slot_order_no: 1
- option_seed_key: "clear-liquid-reagent.ingredient.water.option.purified-water"
- option_order_no: 1
- required_quantity: 1.0
- is_alternative: true
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-12"
- relative_path: "../recipes/clear-liquid-reagent.md"

### `defense-elixir.ingredient.purified-water.option.purified-water`

- recipe_slug: "defense-elixir"
- recipe_name_ko: "방어의 비약"
- process_type: "alchemy"
- slot_seed_key: "defense-elixir.ingredient.purified-water"
- slot_label: "정제수"
- slot_order_no: 4
- option_seed_key: "defense-elixir.ingredient.purified-water.option.purified-water"
- option_order_no: 1
- required_quantity: 3.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-12"
- relative_path: "../recipes/defense-elixir.md"

### `pure-powder-reagent.ingredient.water.option.purified-water`

- recipe_slug: "pure-powder-reagent"
- recipe_name_ko: "순수한 가루 시약"
- process_type: "alchemy"
- slot_seed_key: "pure-powder-reagent.ingredient.water"
- slot_label: "정제수"
- slot_order_no: 1
- option_seed_key: "pure-powder-reagent.ingredient.water.option.purified-water"
- option_order_no: 1
- required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-12"
- relative_path: "../recipes/pure-powder-reagent.md"

### `red-sauce.ingredient.water.option.purified-water`

- recipe_slug: "red-sauce"
- recipe_name_ko: "레드소스"
- process_type: "cooking"
- slot_seed_key: "red-sauce.ingredient.water"
- slot_label: "물"
- slot_order_no: 3
- option_seed_key: "red-sauce.ingredient.water.option.purified-water"
- option_order_no: 2
- required_quantity: 1.0
- is_alternative: true
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/red-sauce.md"

### `tea-with-fine-scent.ingredient.water.option.purified-water`

- recipe_slug: "tea-with-fine-scent"
- recipe_name_ko: "향이 좋은 차"
- process_type: "cooking"
- slot_seed_key: "tea-with-fine-scent.ingredient.water"
- slot_label: "물"
- slot_order_no: 3
- option_seed_key: "tea-with-fine-scent.ingredient.water.option.purified-water"
- option_order_no: 2
- required_quantity: 3.0
- is_alternative: true
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/tea-with-fine-scent.md"

## Ingredient Group Memberships

### `ingredient-group.water.member.purified-water`

- group_key: "water"
- group_name_ko: "물"
- member_seed_key: "ingredient-group.water.member.purified-water"
- member_order_no: 2
- group_verification_status: "verified"
- group_last_verified_at: "2026-09-11"

#### Evidence and Sources

### `ingredient-group.water.membership::cooking-guide`

- evidence_seed_key: "ingredient-group.water.membership::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "ingredient_group"
- entity_id: "water"
- claim_key: "members"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "공식 current 요리 가이드의 대체품 목록 근거. Group membership은 global quantity conversion을 의미하지 않으며 Recipe마다 대체재 필요 수량이 다를 수 있다."
- active: true
- is_active: true

## Ingredient Group Candidate Recipe Usages

### `dressing.ingredient.water.option.water`

- usage_semantics: "ingredient_group_candidate"
- group_key: "water"
- group_name_ko: "물"
- group_verification_status: "verified"
- group_last_verified_at: "2026-09-11"
- recipe_slug: "dressing"
- recipe_name_ko: "드레싱"
- process_type: "cooking"
- slot_seed_key: "dressing.ingredient.water"
- slot_label: "물"
- slot_order_no: 3
- option_seed_key: "dressing.ingredient.water.option.water"
- option_order_no: 1
- group_required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/dressing.md"

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
