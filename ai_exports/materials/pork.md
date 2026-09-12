<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 돼지 고기

## Identity

- key: "pork"
- name_ko: "돼지 고기"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

- None

## Ingredient Group Memberships

### `ingredient-group.meat.member.pork`

- group_key: "meat"
- group_name_ko: "고기"
- member_seed_key: "ingredient-group.meat.member.pork"
- member_order_no: 5
- group_verification_status: "verified"
- group_last_verified_at: "2026-09-11"

#### Evidence and Sources

### `ingredient-group.meat.membership::cooking-guide`

- evidence_seed_key: "ingredient-group.meat.membership::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "ingredient_group"
- entity_id: "meat"
- claim_key: "members"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "공식 current 요리 가이드의 대체품 목록 근거. Group membership은 global quantity conversion을 의미하지 않으며 Recipe마다 대체재 필요 수량이 다를 수 있다."
- active: true
- is_active: true

## Ingredient Group Candidate Recipe Usages

### `grilled-sausage.ingredient.meat.option.meat`

- usage_semantics: "ingredient_group_candidate"
- group_key: "meat"
- group_name_ko: "고기"
- group_verification_status: "verified"
- group_last_verified_at: "2026-09-11"
- recipe_slug: "grilled-sausage"
- recipe_name_ko: "구운 소시지"
- process_type: "cooking"
- slot_seed_key: "grilled-sausage.ingredient.meat"
- slot_label: "고기"
- slot_order_no: 1
- option_seed_key: "grilled-sausage.ingredient.meat.option.meat"
- option_order_no: 1
- group_required_quantity: 6.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/grilled-sausage.md"

### `meat-sandwich.ingredient.meat.option.meat`

- usage_semantics: "ingredient_group_candidate"
- group_key: "meat"
- group_name_ko: "고기"
- group_verification_status: "verified"
- group_last_verified_at: "2026-09-11"
- recipe_slug: "meat-sandwich"
- recipe_name_ko: "미트 샌드위치"
- process_type: "cooking"
- slot_seed_key: "meat-sandwich.ingredient.meat"
- slot_label: "고기"
- slot_order_no: 1
- option_seed_key: "meat-sandwich.ingredient.meat.option.meat"
- option_order_no: 1
- group_required_quantity: 7.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/meat-sandwich.md"

### `red-sauce.ingredient.meat.option.meat`

- usage_semantics: "ingredient_group_candidate"
- group_key: "meat"
- group_name_ko: "고기"
- group_verification_status: "verified"
- group_last_verified_at: "2026-09-11"
- recipe_slug: "red-sauce"
- recipe_name_ko: "레드소스"
- process_type: "cooking"
- slot_seed_key: "red-sauce.ingredient.meat"
- slot_label: "고기"
- slot_order_no: 2
- option_seed_key: "red-sauce.ingredient.meat.option.meat"
- option_order_no: 1
- group_required_quantity: 1.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/red-sauce.md"

### `steak.ingredient.meat.option.meat`

- usage_semantics: "ingredient_group_candidate"
- group_key: "meat"
- group_name_ko: "고기"
- group_verification_status: "verified"
- group_last_verified_at: "2026-09-11"
- recipe_slug: "steak"
- recipe_name_ko: "스테이크"
- process_type: "cooking"
- slot_seed_key: "steak.ingredient.meat"
- slot_label: "고기"
- slot_order_no: 1
- option_seed_key: "steak.ingredient.meat.option.meat"
- option_order_no: 1
- group_required_quantity: 8.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/steak.md"

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
