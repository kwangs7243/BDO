<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 맥주

## Identity

- slug: "beer"
- process_type: "cooking"
- summary: "요리 1회 시도에 필요한 재료 정의. 정확한 현행 제작식의 공식 검증은 추가 확인이 필요하다."
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"

## Result

- material_key: "beer"
- name_ko: "맥주"
- unit: "개"

## Cooking Requirement

- required_skill_tier: "beginner"
- required_skill_level: 1

## Ingredient Slots

### 곡물

- seed_key: "beer.ingredient.grain"
- order_no: 1
- notes: null

#### beer.ingredient.grain.option.grain

- target_type: "ingredient_group"
- required_quantity: 5.0
- order_no: 1
- notes: null
- group: "grain"
- name_ko: "곡물"
- verification_status: "verified"
- last_verified_at: "2026-09-10"

Allowed current members:

- wheat / 밀 (개)
- barley / 보리 (개)
- potato / 감자 (개)
- sweet-potato / 고구마 (개)
- corn / 옥수수 (개)

### 물

- seed_key: "beer.ingredient.water"
- order_no: 2
- notes: null

#### beer.ingredient.water.option.mineral-water

- target_type: "material"
- required_quantity: 6.0
- order_no: 1
- notes: null
- material_key: "mineral-water"
- name_ko: "요리용 생수"
- unit: "개"

#### beer.ingredient.water.option.purified-water

- target_type: "material"
- required_quantity: 3.0
- order_no: 2
- notes: null
- material_key: "purified-water"
- name_ko: "정제수"
- unit: "개"

### 발효제

- seed_key: "beer.ingredient.leavening-agent"
- order_no: 3
- notes: null

#### beer.ingredient.leavening-agent.option.leavening-agent

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "leavening-agent"
- name_ko: "발효제"
- unit: "개"

### 설탕

- seed_key: "beer.ingredient.sugar"
- order_no: 4
- notes: null

#### beer.ingredient.sugar.option.sugar

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "sugar"
- name_ko: "설탕"
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

### `ingredient-group.grain.membership::cooking-guide`

- evidence_seed_key: "ingredient-group.grain.membership::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "ingredient_group"
- entity_id: "grain"
- claim_key: "members"
- verification_status: "verified"
- last_verified_at: "2026-09-10"
- evidence_note: "공식 current 요리 가이드 대체품 목록의 구성원. 그룹 소속은 전역 수량 환산을 뜻하지 않는다."
- active: true
- is_active: true

### `recipe.beer.formula::codex-beer-9213`

- evidence_seed_key: "recipe.beer.formula::codex-beer-9213"
- source_id: "codex-beer-9213"
- title: "맥주"
- url: "https://bdocodex.com/kr/item/9213/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "beer"
- claim_key: "ingredients"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "과거 공식/커뮤니티 및 DB 보조 자료를 보존한다. current KR first-party exact formula를 검증한 것으로 승격하지 않는다."
- active: true
- is_active: true

### `recipe.beer.formula::cooking-beer-community-2019`

- evidence_seed_key: "recipe.beer.formula::cooking-beer-community-2019"
- source_id: "cooking-beer-community-2019"
- title: "[요리, 채집, 재배] 0부터 세렌디아 정식까지 - 2"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=12232"
- publisher: "삐읏"
- source_type: "community_guide"
- published_at: "2019-11-23"
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "beer"
- claim_key: "ingredients"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "과거 공식/커뮤니티 및 DB 보조 자료를 보존한다. current KR first-party exact formula를 검증한 것으로 승격하지 않는다."
- active: true
- is_active: true

### `recipe.beer.attempt::cooking-guide`

- evidence_seed_key: "recipe.beer.attempt::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "recipe"
- entity_id: "beer"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-10"
- evidence_note: "재료는 한 번 요리할 분량이며 대량 요리는 10회분 재료를 소비한다."
- active: true
- is_active: true

### `recipe.beer.skill::codex-beer-9213`

- evidence_seed_key: "recipe.beer.skill::codex-beer-9213"
- source_id: "codex-beer-9213"
- title: "맥주"
- url: "https://bdocodex.com/kr/item/9213/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "beer"
- claim_key: "required_skill"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "현재 first-party 제작 조건의 추가 검증 필요."
- active: true
- is_active: true

### `recipe.beer.ingredient.grain.option.grain.quantity::codex-beer-9213`

- evidence_seed_key: "recipe.beer.ingredient.grain.option.grain.quantity::codex-beer-9213"
- source_id: "codex-beer-9213"
- title: "맥주"
- url: "https://bdocodex.com/kr/item/9213/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "beer.ingredient.grain.option.grain"
- claim_key: "required_quantity"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "해당 Recipe option의 수량이다. 다른 recipe 또는 품질 등급에 대한 전역 환산·혼합 재료 사용은 추론하지 않는다."
- active: true
- is_active: true

### `recipe.beer.ingredient.leavening-agent.option.leavening-agent.quantity::codex-beer-9213`

- evidence_seed_key: "recipe.beer.ingredient.leavening-agent.option.leavening-agent.quantity::codex-beer-9213"
- source_id: "codex-beer-9213"
- title: "맥주"
- url: "https://bdocodex.com/kr/item/9213/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "beer.ingredient.leavening-agent.option.leavening-agent"
- claim_key: "required_quantity"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "해당 Recipe option의 수량이다. 다른 recipe 또는 품질 등급에 대한 전역 환산·혼합 재료 사용은 추론하지 않는다."
- active: true
- is_active: true

### `recipe.beer.ingredient.sugar.option.sugar.quantity::codex-beer-9213`

- evidence_seed_key: "recipe.beer.ingredient.sugar.option.sugar.quantity::codex-beer-9213"
- source_id: "codex-beer-9213"
- title: "맥주"
- url: "https://bdocodex.com/kr/item/9213/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "beer.ingredient.sugar.option.sugar"
- claim_key: "required_quantity"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "해당 Recipe option의 수량이다. 다른 recipe 또는 품질 등급에 대한 전역 환산·혼합 재료 사용은 추론하지 않는다."
- active: true
- is_active: true

### `recipe.beer.ingredient.water.option.mineral-water.quantity::codex-beer-9213`

- evidence_seed_key: "recipe.beer.ingredient.water.option.mineral-water.quantity::codex-beer-9213"
- source_id: "codex-beer-9213"
- title: "맥주"
- url: "https://bdocodex.com/kr/item/9213/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "beer.ingredient.water.option.mineral-water"
- claim_key: "required_quantity"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "해당 Recipe option의 수량이다. 다른 recipe 또는 품질 등급에 대한 전역 환산·혼합 재료 사용은 추론하지 않는다."
- active: true
- is_active: true

### `recipe.beer.ingredient.water.option.purified-water.quantity::codex-beer-9213`

- evidence_seed_key: "recipe.beer.ingredient.water.option.purified-water.quantity::codex-beer-9213"
- source_id: "codex-beer-9213"
- title: "맥주"
- url: "https://bdocodex.com/kr/item/9213/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "beer.ingredient.water.option.purified-water"
- claim_key: "required_quantity"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "해당 Recipe option의 수량이다. 다른 recipe 또는 품질 등급에 대한 전역 환산·혼합 재료 사용은 추론하지 않는다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
