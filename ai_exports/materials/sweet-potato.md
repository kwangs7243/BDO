<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 고구마

## Identity

- key: "sweet-potato"
- name_ko: "고구마"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

- None

## Ingredient Group Memberships

### `ingredient-group.grain.member.sweet-potato`

- group_key: "grain"
- group_name_ko: "곡물"
- member_seed_key: "ingredient-group.grain.member.sweet-potato"
- member_order_no: 4
- group_verification_status: "verified"
- group_last_verified_at: "2026-09-11"

#### Evidence and Sources

### `ingredient-group.grain.membership::cooking-guide`

- evidence_seed_key: "ingredient-group.grain.membership::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "ingredient_group"
- entity_id: "grain"
- claim_key: "members"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "2026-09-11 공식 current 요리 가이드의 대체품 목록을 재확인했다. 그룹 소속은 전역 수량 환산을 뜻하지 않는다."
- active: true
- is_active: true

## Ingredient Group Candidate Recipe Usages

### `beer.ingredient.grain.option.grain`

- usage_semantics: "ingredient_group_candidate"
- group_key: "grain"
- group_name_ko: "곡물"
- group_verification_status: "verified"
- group_last_verified_at: "2026-09-11"
- recipe_slug: "beer"
- recipe_name_ko: "맥주"
- process_type: "cooking"
- slot_seed_key: "beer.ingredient.grain"
- slot_label: "곡물"
- slot_order_no: 1
- option_seed_key: "beer.ingredient.grain.option.grain"
- option_order_no: 1
- group_required_quantity: 5.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/beer.md"

### `omelet.ingredient.grain.option.grain`

- usage_semantics: "ingredient_group_candidate"
- group_key: "grain"
- group_name_ko: "곡물"
- group_verification_status: "verified"
- group_last_verified_at: "2026-09-11"
- recipe_slug: "omelet"
- recipe_name_ko: "오믈렛"
- process_type: "cooking"
- slot_seed_key: "omelet.ingredient.grain"
- slot_label: "곡물"
- slot_order_no: 1
- option_seed_key: "omelet.ingredient.grain.option.grain"
- option_order_no: 1
- group_required_quantity: 5.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/omelet.md"

### `vinegar.ingredient.grain.option.grain`

- usage_semantics: "ingredient_group_candidate"
- group_key: "grain"
- group_name_ko: "곡물"
- group_verification_status: "verified"
- group_last_verified_at: "2026-09-11"
- recipe_slug: "vinegar"
- recipe_name_ko: "식초"
- process_type: "cooking"
- slot_seed_key: "vinegar.ingredient.grain"
- slot_label: "곡물"
- slot_order_no: 1
- option_seed_key: "vinegar.ingredient.grain.option.grain"
- option_order_no: 1
- group_required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/vinegar.md"

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
