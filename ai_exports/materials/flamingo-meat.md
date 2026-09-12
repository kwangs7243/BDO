<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 홍학 고기

## Identity

- key: "flamingo-meat"
- name_ko: "홍학 고기"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

- None

## Ingredient Group Memberships

### `ingredient-group.bird-meat.member.flamingo-meat`

- group_key: "bird-meat"
- group_name_ko: "새고기"
- member_seed_key: "ingredient-group.bird-meat.member.flamingo-meat"
- member_order_no: 2
- group_verification_status: "verified"
- group_last_verified_at: "2026-09-11"

#### Evidence and Sources

### `ingredient-group.bird-meat.membership::cooking-guide`

- evidence_seed_key: "ingredient-group.bird-meat.membership::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "ingredient_group"
- entity_id: "bird-meat"
- claim_key: "members"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "2026-09-11 공식 current 요리 가이드의 대체품 목록을 재확인했다. 그룹 소속은 전역 수량 환산을 뜻하지 않는다."
- active: true
- is_active: true

## Ingredient Group Candidate Recipe Usages

### `grilled-bird-meat.ingredient.bird-meat.option.bird-meat`

- usage_semantics: "ingredient_group_candidate"
- group_key: "bird-meat"
- group_name_ko: "새고기"
- group_verification_status: "verified"
- group_last_verified_at: "2026-09-11"
- recipe_slug: "grilled-bird-meat"
- recipe_name_ko: "새구이"
- process_type: "cooking"
- slot_seed_key: "grilled-bird-meat.ingredient.bird-meat"
- slot_label: "새고기"
- slot_order_no: 1
- option_seed_key: "grilled-bird-meat.ingredient.bird-meat.option.bird-meat"
- option_order_no: 1
- group_required_quantity: 2.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/grilled-bird-meat.md"

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
