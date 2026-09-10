<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 채소 절임

## Identity

- slug: "pickled-vegetables"
- process_type: "cooking"
- summary: "요리 1회 시도에 필요한 재료 정의. 정확한 현행 제작식의 공식 검증은 추가 확인이 필요하다."
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"

## Result

- material_key: "pickled-vegetables"
- name_ko: "채소 절임"
- unit: "개"

## Cooking Requirement

- required_skill_tier: "apprentice"
- required_skill_level: 1

## Ingredient Slots

### 채소

- seed_key: "pickled-vegetables.ingredient.vegetable"
- order_no: 1
- notes: null

#### pickled-vegetables.ingredient.vegetable.option.vegetable

- target_type: "ingredient_group"
- required_quantity: 8.0
- order_no: 1
- notes: null
- group: "vegetable"
- name_ko: "채소"
- verification_status: "verified"
- last_verified_at: "2026-09-10"

Allowed current members:

- pumpkin / 호박 (개)
- olive / 올리브 (개)
- tomato / 토마토 (개)
- paprika / 파프리카 (개)
- cabbage / 양배추 (개)

### 식초

- seed_key: "pickled-vegetables.ingredient.vinegar"
- order_no: 2
- notes: null

#### pickled-vegetables.ingredient.vinegar.option.vinegar

- target_type: "material"
- required_quantity: 4.0
- order_no: 1
- notes: null
- material_key: "vinegar"
- name_ko: "식초"
- unit: "개"

### 발효제

- seed_key: "pickled-vegetables.ingredient.leavening-agent"
- order_no: 3
- notes: null

#### pickled-vegetables.ingredient.leavening-agent.option.leavening-agent

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "leavening-agent"
- name_ko: "발효제"
- unit: "개"

### 설탕

- seed_key: "pickled-vegetables.ingredient.sugar"
- order_no: 4
- notes: null

#### pickled-vegetables.ingredient.sugar.option.sugar

- target_type: "material"
- required_quantity: 2.0
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

### `ingredient-group.vegetable.membership::cooking-guide`

- evidence_seed_key: "ingredient-group.vegetable.membership::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "ingredient_group"
- entity_id: "vegetable"
- claim_key: "members"
- verification_status: "verified"
- last_verified_at: "2026-09-10"
- evidence_note: "공식 current 요리 가이드 대체품 목록의 구성원. 그룹 소속은 전역 수량 환산을 뜻하지 않는다."
- active: true
- is_active: true

### `recipe.pickled-vegetables.formula::codex-pickled-vegetables-9202`

- evidence_seed_key: "recipe.pickled-vegetables.formula::codex-pickled-vegetables-9202"
- source_id: "codex-pickled-vegetables-9202"
- title: "채소 절임"
- url: "https://bdocodex.com/kr/item/9202/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "pickled-vegetables"
- claim_key: "ingredients"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "과거 공식/커뮤니티 및 DB 보조 자료를 보존한다. current KR first-party exact formula를 검증한 것으로 승격하지 않는다."
- active: true
- is_active: true

### `recipe.pickled-vegetables.formula::cooking-lara-event-2021`

- evidence_seed_key: "recipe.pickled-vegetables.formula::cooking-lara-event-2021"
- source_id: "cooking-lara-event-2021"
- title: "[이벤트] 라라의 부탁을 들어줘!"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=5469"
- publisher: "Pearl Abyss"
- source_type: "official_event"
- published_at: "2021-05-04"
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "pickled-vegetables"
- claim_key: "ingredients"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "과거 공식/커뮤니티 및 DB 보조 자료를 보존한다. current KR first-party exact formula를 검증한 것으로 승격하지 않는다."
- active: true
- is_active: true

### `recipe.pickled-vegetables.formula::cooking-vinegar-community-2020`

- evidence_seed_key: "recipe.pickled-vegetables.formula::cooking-vinegar-community-2020"
- source_id: "cooking-vinegar-community-2020"
- title: "요리와 생활의관계 명장까지 추천요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=26907"
- publisher: "Shy아조씨"
- source_type: "community_guide"
- published_at: "2020-09-24"
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "pickled-vegetables"
- claim_key: "ingredients"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "과거 공식/커뮤니티 및 DB 보조 자료를 보존한다. current KR first-party exact formula를 검증한 것으로 승격하지 않는다."
- active: true
- is_active: true

### `recipe.pickled-vegetables.attempt::cooking-guide`

- evidence_seed_key: "recipe.pickled-vegetables.attempt::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "recipe"
- entity_id: "pickled-vegetables"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-10"
- evidence_note: "재료는 한 번 요리할 분량이며 대량 요리는 10회분 재료를 소비한다."
- active: true
- is_active: true

### `recipe.pickled-vegetables.skill::codex-pickled-vegetables-9202`

- evidence_seed_key: "recipe.pickled-vegetables.skill::codex-pickled-vegetables-9202"
- source_id: "codex-pickled-vegetables-9202"
- title: "채소 절임"
- url: "https://bdocodex.com/kr/item/9202/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "pickled-vegetables"
- claim_key: "required_skill"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "현재 first-party 제작 조건의 추가 검증 필요."
- active: true
- is_active: true

### `recipe.pickled-vegetables.skill::cooking-lara-event-2021`

- evidence_seed_key: "recipe.pickled-vegetables.skill::cooking-lara-event-2021"
- source_id: "cooking-lara-event-2021"
- title: "[이벤트] 라라의 부탁을 들어줘!"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=5469"
- publisher: "Pearl Abyss"
- source_type: "official_event"
- published_at: "2021-05-04"
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "pickled-vegetables"
- claim_key: "required_skill"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "현재 first-party 제작 조건의 추가 검증 필요."
- active: true
- is_active: true

### `recipe.pickled-vegetables.ingredient.leavening-agent.option.leavening-agent.quantity::codex-pickled-vegetables-9202`

- evidence_seed_key: "recipe.pickled-vegetables.ingredient.leavening-agent.option.leavening-agent.quantity::codex-pickled-vegetables-9202"
- source_id: "codex-pickled-vegetables-9202"
- title: "채소 절임"
- url: "https://bdocodex.com/kr/item/9202/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "pickled-vegetables.ingredient.leavening-agent.option.leavening-agent"
- claim_key: "required_quantity"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "해당 Recipe option의 수량이다. 다른 recipe 또는 품질 등급에 대한 전역 환산·혼합 재료 사용은 추론하지 않는다."
- active: true
- is_active: true

### `recipe.pickled-vegetables.ingredient.sugar.option.sugar.quantity::codex-pickled-vegetables-9202`

- evidence_seed_key: "recipe.pickled-vegetables.ingredient.sugar.option.sugar.quantity::codex-pickled-vegetables-9202"
- source_id: "codex-pickled-vegetables-9202"
- title: "채소 절임"
- url: "https://bdocodex.com/kr/item/9202/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "pickled-vegetables.ingredient.sugar.option.sugar"
- claim_key: "required_quantity"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "해당 Recipe option의 수량이다. 다른 recipe 또는 품질 등급에 대한 전역 환산·혼합 재료 사용은 추론하지 않는다."
- active: true
- is_active: true

### `recipe.pickled-vegetables.ingredient.vegetable.option.vegetable.quantity::codex-pickled-vegetables-9202`

- evidence_seed_key: "recipe.pickled-vegetables.ingredient.vegetable.option.vegetable.quantity::codex-pickled-vegetables-9202"
- source_id: "codex-pickled-vegetables-9202"
- title: "채소 절임"
- url: "https://bdocodex.com/kr/item/9202/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "pickled-vegetables.ingredient.vegetable.option.vegetable"
- claim_key: "required_quantity"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "해당 Recipe option의 수량이다. 다른 recipe 또는 품질 등급에 대한 전역 환산·혼합 재료 사용은 추론하지 않는다."
- active: true
- is_active: true

### `recipe.pickled-vegetables.ingredient.vinegar.option.vinegar.quantity::codex-pickled-vegetables-9202`

- evidence_seed_key: "recipe.pickled-vegetables.ingredient.vinegar.option.vinegar.quantity::codex-pickled-vegetables-9202"
- source_id: "codex-pickled-vegetables-9202"
- title: "채소 절임"
- url: "https://bdocodex.com/kr/item/9202/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-10T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "pickled-vegetables.ingredient.vinegar.option.vinegar"
- claim_key: "required_quantity"
- verification_status: "needs_review"
- last_verified_at: "2026-09-10"
- evidence_note: "해당 Recipe option의 수량이다. 다른 recipe 또는 품질 등급에 대한 전역 환산·혼합 재료 사용은 추론하지 않는다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
