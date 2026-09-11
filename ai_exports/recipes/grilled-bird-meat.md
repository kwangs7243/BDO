<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 새구이

## Identity

- slug: "grilled-bird-meat"
- process_type: "cooking"
- summary: "요리 1회 시도에 필요한 재료 정의. 공식 과거 자료와 current game-data를 claim별로 교차검증했다."
- verification_status: "verified"
- last_verified_at: "2026-09-11"

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
- last_verified_at: "2026-09-11"

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

## Direct Recipe Dependencies

- Only explicit Material options create dependency edges.
- IngredientGroup membership is not expanded.
- Dependencies are direct only.
- No recursive quantity propagation is performed.
- No producer output/yield is inferred.

### Upstream Producers

- None

### Downstream Consumers

- None

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

### `recipe.grilled-bird-meat.formula::codex-grilled-bird-meat-9492`

- evidence_seed_key: "recipe.grilled-bird-meat.formula::codex-grilled-bird-meat-9492"
- source_id: "codex-grilled-bird-meat-9492"
- title: "새구이"
- url: "https://bdocodex.com/kr/item/9492/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "grilled-bird-meat"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "current BDO Codex에서 전체 option 구성을 확인했다. 공식 2018 자료는 면실유 대안을 포함하지 않으므로 전체 formula claim의 출처로 확대하지 않는다."
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
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "grilled-bird-meat"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "2026-09-11 공식 current 요리 가이드에서 1회분 투입과 대량 요리의 10회분 소비를 재확인했다."
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
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "grilled-bird-meat"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "요리 초급 1 이상 조건을 2018년 공식 추가 자료와 current BDO Codex에서 교차검증했다."
- active: true
- is_active: true

### `recipe.grilled-bird-meat.skill::cooking-grilled-bird-meat-official-2018`

- evidence_seed_key: "recipe.grilled-bird-meat.skill::cooking-grilled-bird-meat-official-2018"
- source_id: "cooking-grilled-bird-meat-official-2018"
- title: "2018년 7월 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=905"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2018-07-01"
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "grilled-bird-meat"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "요리 초급 1 이상 조건을 2018년 공식 추가 자료와 current BDO Codex에서 교차검증했다."
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
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-bird-meat.ingredient.bird-meat.option.bird-meat"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "새고기 2를 공식 2018 닭고기 배합과 current BDO Codex에서 교차검증했다. 현행 공식 가이드의 새고기 그룹만 적용하며 전역 환산·혼합 사용은 추론하지 않는다."
- active: true
- is_active: true

### `recipe.grilled-bird-meat.ingredient.bird-meat.option.bird-meat.quantity::cooking-grilled-bird-meat-official-2018`

- evidence_seed_key: "recipe.grilled-bird-meat.ingredient.bird-meat.option.bird-meat.quantity::cooking-grilled-bird-meat-official-2018"
- source_id: "cooking-grilled-bird-meat-official-2018"
- title: "2018년 7월 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=905"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2018-07-01"
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-bird-meat.ingredient.bird-meat.option.bird-meat"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "새고기 2를 공식 2018 닭고기 배합과 current BDO Codex에서 교차검증했다. 현행 공식 가이드의 새고기 그룹만 적용하며 전역 환산·혼합 사용은 추론하지 않는다."
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
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-bird-meat.ingredient.cooking-wine.option.cooking-wine"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "조리용 와인 2를 공식 2018 자료와 current BDO Codex에서 교차검증했다. 다른 recipe의 수량으로 일반화하지 않는다."
- active: true
- is_active: true

### `recipe.grilled-bird-meat.ingredient.cooking-wine.option.cooking-wine.quantity::cooking-grilled-bird-meat-official-2018`

- evidence_seed_key: "recipe.grilled-bird-meat.ingredient.cooking-wine.option.cooking-wine.quantity::cooking-grilled-bird-meat-official-2018"
- source_id: "cooking-grilled-bird-meat-official-2018"
- title: "2018년 7월 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=905"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2018-07-01"
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-bird-meat.ingredient.cooking-wine.option.cooking-wine"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "조리용 와인 2를 공식 2018 자료와 current BDO Codex에서 교차검증했다. 다른 recipe의 수량으로 일반화하지 않는다."
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
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-bird-meat.ingredient.oil.option.cottonseed-oil"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "면실유 6 대안은 current BDO Codex에서 확인했다. 공식 2018 자료에는 이 대안이 없으므로 출처로 연결하지 않으며 전역 환산·혼합 사용은 추론하지 않는다."
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
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-bird-meat.ingredient.oil.option.deep-frying-oil"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "튀김용 오일 6을 공식 2018 자료와 current BDO Codex에서 교차검증했다. 다른 recipe의 수량으로 일반화하지 않는다."
- active: true
- is_active: true

### `recipe.grilled-bird-meat.ingredient.oil.option.deep-frying-oil.quantity::cooking-grilled-bird-meat-official-2018`

- evidence_seed_key: "recipe.grilled-bird-meat.ingredient.oil.option.deep-frying-oil.quantity::cooking-grilled-bird-meat-official-2018"
- source_id: "cooking-grilled-bird-meat-official-2018"
- title: "2018년 7월 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=905"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2018-07-01"
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-bird-meat.ingredient.oil.option.deep-frying-oil"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "튀김용 오일 6을 공식 2018 자료와 current BDO Codex에서 교차검증했다. 다른 recipe의 수량으로 일반화하지 않는다."
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
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-bird-meat.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "소금 1을 공식 2018 자료와 current BDO Codex에서 교차검증했다. 다른 recipe의 수량으로 일반화하지 않는다."
- active: true
- is_active: true

### `recipe.grilled-bird-meat.ingredient.salt.option.salt.quantity::cooking-grilled-bird-meat-official-2018`

- evidence_seed_key: "recipe.grilled-bird-meat.ingredient.salt.option.salt.quantity::cooking-grilled-bird-meat-official-2018"
- source_id: "cooking-grilled-bird-meat-official-2018"
- title: "2018년 7월 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=905"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2018-07-01"
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-bird-meat.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "소금 1을 공식 2018 자료와 current BDO Codex에서 교차검증했다. 다른 recipe의 수량으로 일반화하지 않는다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
