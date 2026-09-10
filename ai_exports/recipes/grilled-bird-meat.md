<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 새구이

## Identity

- slug: "grilled-bird-meat"
- process_type: "cooking"
- summary: "요리 1회 시도에 필요한 재료 정의. 정확한 현행 제작식의 공식 검증은 추가 확인이 필요하다."
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"

## Result

- material_key: "grilled-bird-meat"
- name_ko: "새구이"
- unit: "개"

## Cooking Requirement

- required_skill_tier: "beginner"
- required_skill_level: 1

## Ingredient Slots

### 새고기

- seed_key: "grilled-bird-meat.ingredient.bird-meat"
- order_no: 1
- notes: null

#### grilled-bird-meat.ingredient.bird-meat.option.bird-meat

- target_type: "ingredient_group"
- required_quantity: 2.0
- order_no: 1
- notes: null
- group: "bird-meat"
- name_ko: "새고기"
- verification_status: "verified"
- last_verified_at: "2026-09-10"

Allowed current members:

- kuku-bird-meat / 쿠쿠새 고기 (개)
- flamingo-meat / 홍학 고기 (개)
- chicken-meat / 닭고기 (개)

### 오일

- seed_key: "grilled-bird-meat.ingredient.oil"
- order_no: 2
- notes: null

#### grilled-bird-meat.ingredient.oil.option.deep-frying-oil

- target_type: "material"
- required_quantity: 6.0
- order_no: 1
- notes: null
- material_key: "deep-frying-oil"
- name_ko: "튀김용 오일"
- unit: "개"

#### grilled-bird-meat.ingredient.oil.option.cottonseed-oil

- target_type: "material"
- required_quantity: 6.0
- order_no: 2
- notes: null
- material_key: "cottonseed-oil"
- name_ko: "면실유"
- unit: "개"

### 조리용 와인

- seed_key: "grilled-bird-meat.ingredient.cooking-wine"
- order_no: 3
- notes: null

#### grilled-bird-meat.ingredient.cooking-wine.option.cooking-wine

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "cooking-wine"
- name_ko: "조리용 와인"
- unit: "개"

### 소금

- seed_key: "grilled-bird-meat.ingredient.salt"
- order_no: 4
- notes: null

#### grilled-bird-meat.ingredient.salt.option.salt

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "salt"
- name_ko: "소금"
- unit: "개"


## Substitution Semantics

- Ingredient quantities are per one cooking attempt.
- All active slots are required (AND).
- Options inside one slot are alternatives (OR); select one allowed material.
- IngredientGroup membership does not define a global quantity conversion.
- required_quantity belongs to this Recipe option.
- Mixed option consumption is not inferred.
- Result quantity is not guaranteed by this Recipe definition.
- High-quality/special multipliers and yield probabilities are not defined.

## Evidence and Sources

### Current evidence

### `ingredient-group.bird-meat.membership::cooking-guide`

- evidence_seed_key: "ingredient-group.bird-meat.membership::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "ingredient_group"
- entity_id: "bird-meat"
- claim_key: "members"
- verification_status: "verified"
- last_verified_at: "2026-09-10"
- evidence_note: "공식 current 요리 가이드 대체품 목록의 구성원. 그룹 소속은 전역 수량 환산을 뜻하지 않는다."
- active: true
- is_active: true

### `recipe.grilled-bird-meat.formula::codex-grilled-bird-meat-9492`

- evidence_seed_key: "recipe.grilled-bird-meat.formula::codex-grilled-bird-meat-9492"
- source_id: "codex-grilled-bird-meat-9492"
- title: "새구이"
- url: "https://bdocodex.com/kr/item/9492/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "grilled-bird-meat"
- claim_key: "ingredients"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "과거 공식/커뮤니티 및 DB 보조 자료를 보존한다. current KR first-party exact formula를 검증한 것으로 승격하지 않는다."
- active: true
- is_active: true

### `recipe.grilled-bird-meat.attempt::cooking-guide`

- evidence_seed_key: "recipe.grilled-bird-meat.attempt::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "recipe"
- entity_id: "grilled-bird-meat"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-10"
- evidence_note: "재료는 한 번 요리할 분량이며 대량 요리는 10회분 재료를 소비한다."
- active: true
- is_active: true

### `recipe.grilled-bird-meat.skill::codex-grilled-bird-meat-9492`

- evidence_seed_key: "recipe.grilled-bird-meat.skill::codex-grilled-bird-meat-9492"
- source_id: "codex-grilled-bird-meat-9492"
- title: "새구이"
- url: "https://bdocodex.com/kr/item/9492/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "grilled-bird-meat"
- claim_key: "required_skill"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "현재 first-party 제작 조건의 추가 검증 필요."
- active: true
- is_active: true

### `recipe.grilled-bird-meat.ingredient.bird-meat.option.bird-meat.quantity::codex-grilled-bird-meat-9492`

- evidence_seed_key: "recipe.grilled-bird-meat.ingredient.bird-meat.option.bird-meat.quantity::codex-grilled-bird-meat-9492"
- source_id: "codex-grilled-bird-meat-9492"
- title: "새구이"
- url: "https://bdocodex.com/kr/item/9492/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-bird-meat.ingredient.bird-meat.option.bird-meat"
- claim_key: "required_quantity"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "해당 Recipe option의 수량이다. 다른 recipe 또는 품질 등급에 대한 전역 환산·혼합 재료 사용은 추론하지 않는다."
- active: true
- is_active: true

### `recipe.grilled-bird-meat.ingredient.cooking-wine.option.cooking-wine.quantity::codex-grilled-bird-meat-9492`

- evidence_seed_key: "recipe.grilled-bird-meat.ingredient.cooking-wine.option.cooking-wine.quantity::codex-grilled-bird-meat-9492"
- source_id: "codex-grilled-bird-meat-9492"
- title: "새구이"
- url: "https://bdocodex.com/kr/item/9492/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-bird-meat.ingredient.cooking-wine.option.cooking-wine"
- claim_key: "required_quantity"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "해당 Recipe option의 수량이다. 다른 recipe 또는 품질 등급에 대한 전역 환산·혼합 재료 사용은 추론하지 않는다."
- active: true
- is_active: true

### `recipe.grilled-bird-meat.ingredient.oil.option.cottonseed-oil.quantity::codex-grilled-bird-meat-9492`

- evidence_seed_key: "recipe.grilled-bird-meat.ingredient.oil.option.cottonseed-oil.quantity::codex-grilled-bird-meat-9492"
- source_id: "codex-grilled-bird-meat-9492"
- title: "새구이"
- url: "https://bdocodex.com/kr/item/9492/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-bird-meat.ingredient.oil.option.cottonseed-oil"
- claim_key: "required_quantity"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "해당 Recipe option의 수량이다. 다른 recipe 또는 품질 등급에 대한 전역 환산·혼합 재료 사용은 추론하지 않는다."
- active: true
- is_active: true

### `recipe.grilled-bird-meat.ingredient.oil.option.deep-frying-oil.quantity::codex-grilled-bird-meat-9492`

- evidence_seed_key: "recipe.grilled-bird-meat.ingredient.oil.option.deep-frying-oil.quantity::codex-grilled-bird-meat-9492"
- source_id: "codex-grilled-bird-meat-9492"
- title: "새구이"
- url: "https://bdocodex.com/kr/item/9492/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-bird-meat.ingredient.oil.option.deep-frying-oil"
- claim_key: "required_quantity"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "해당 Recipe option의 수량이다. 다른 recipe 또는 품질 등급에 대한 전역 환산·혼합 재료 사용은 추론하지 않는다."
- active: true
- is_active: true

### `recipe.grilled-bird-meat.ingredient.salt.option.salt.quantity::codex-grilled-bird-meat-9492`

- evidence_seed_key: "recipe.grilled-bird-meat.ingredient.salt.option.salt.quantity::codex-grilled-bird-meat-9492"
- source_id: "codex-grilled-bird-meat-9492"
- title: "새구이"
- url: "https://bdocodex.com/kr/item/9492/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-bird-meat.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "해당 Recipe option의 수량이다. 다른 recipe 또는 품질 등급에 대한 전역 환산·혼합 재료 사용은 추론하지 않는다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
