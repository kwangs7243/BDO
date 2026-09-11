<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 식초

## Identity

- slug: "vinegar"
- process_type: "cooking"
- summary: "요리 1회 시도에 필요한 재료 정의. community 자료와 current game-data를 claim별로 교차검증했다."
- verification_status: "verified"
- last_verified_at: "2026-09-11"

## Result

- material_key: "vinegar"
- name_ko: "식초"
- unit: "개"

## Cooking Requirement

- required_skill_tier: "beginner"
- required_skill_level: 1

## Ingredient Slots

### 곡물

- seed_key: "vinegar.ingredient.grain"
- order_no: 1
- notes: null

#### vinegar.ingredient.grain.option.grain

- target_type: "ingredient_group"
- required_quantity: 1.0
- order_no: 1
- notes: null
- group: "grain"
- name_ko: "곡물"
- verification_status: "verified"
- last_verified_at: "2026-09-11"

Allowed current members:

- wheat / 밀 (개)
- barley / 보리 (개)
- potato / 감자 (개)
- sweet-potato / 고구마 (개)
- corn / 옥수수 (개)

### 과일

- seed_key: "vinegar.ingredient.fruit"
- order_no: 2
- notes: null

#### vinegar.ingredient.fruit.option.fruit

- target_type: "ingredient_group"
- required_quantity: 1.0
- order_no: 1
- notes: null
- group: "fruit"
- name_ko: "과일"
- verification_status: "verified"
- last_verified_at: "2026-09-11"

Allowed current members:

- grape / 포도 (개)
- strawberry / 딸기 (개)
- apple / 사과 (개)
- cherry / 체리 (개)
- pear / 배 (개)
- banana / 바나나 (개)
- pineapple / 파인애플 (개)

### 발효제

- seed_key: "vinegar.ingredient.leavening-agent"
- order_no: 3
- notes: null

#### vinegar.ingredient.leavening-agent.option.leavening-agent

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "leavening-agent"
- name_ko: "발효제"
- unit: "개"

### 설탕

- seed_key: "vinegar.ingredient.sugar"
- order_no: 4
- notes: null

#### vinegar.ingredient.sugar.option.sugar

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

## Direct Recipe Dependencies

- Only explicit Material options create dependency edges.
- IngredientGroup membership is not expanded.
- Dependencies are direct only.
- No recursive quantity propagation is performed.
- No producer output/yield is inferred.

### Upstream Producers

- None

### Downstream Consumers

#### `vinegar -> pickled-vegetables`

- producer_recipe_slug: "vinegar"
- producer_recipe_name_ko: "식초"
- producer_verification_status: "verified"
- consumer_recipe_slug: "pickled-vegetables"
- consumer_recipe_name_ko: "채소 절임"
- consumer_verification_status: "verified"
- material_key: "vinegar"
- material_name_ko: "식초"
- unit: "개"
- required_quantity: 4.0
- consumer_slot_seed_key: "pickled-vegetables.ingredient.vinegar"
- consumer_option_seed_key: "pickled-vegetables.ingredient.vinegar.option.vinegar"
- is_alternative: false
- relative_path: "../recipes/pickled-vegetables.md"

## Evidence and Sources

### Current evidence

### `ingredient-group.fruit.membership::cooking-guide`

- evidence_seed_key: "ingredient-group.fruit.membership::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "ingredient_group"
- entity_id: "fruit"
- claim_key: "members"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "2026-09-11 공식 current 요리 가이드의 대체품 목록을 재확인했다. 그룹 소속은 전역 수량 환산을 뜻하지 않는다."
- active: true
- is_active: true

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

### `recipe.vinegar.formula::codex-vinegar-9066`

- evidence_seed_key: "recipe.vinegar.formula::codex-vinegar-9066"
- source_id: "codex-vinegar-9066"
- title: "식초"
- url: "https://bdocodex.com/kr/item/9066/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "vinegar"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "community_guide와 current BDO Codex의 exact formula가 일치함을 교차검증했다. 공식 문서만으로 검증했다는 의미는 아니다."
- active: true
- is_active: true

### `recipe.vinegar.formula::cooking-vinegar-community-2020`

- evidence_seed_key: "recipe.vinegar.formula::cooking-vinegar-community-2020"
- source_id: "cooking-vinegar-community-2020"
- title: "요리와 생활의관계 명장까지 추천요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=26907"
- publisher: "Shy아조씨"
- source_type: "community_guide"
- published_at: "2020-09-24"
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "vinegar"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "community_guide와 current BDO Codex의 exact formula가 일치함을 교차검증했다. 공식 문서만으로 검증했다는 의미는 아니다."
- active: true
- is_active: true

### `recipe.vinegar.attempt::cooking-guide`

- evidence_seed_key: "recipe.vinegar.attempt::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "vinegar"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "2026-09-11 공식 current 요리 가이드에서 1회분 투입과 대량 요리의 10회분 소비를 재확인했다."
- active: true
- is_active: true

### `recipe.vinegar.skill::codex-vinegar-9066`

- evidence_seed_key: "recipe.vinegar.skill::codex-vinegar-9066"
- source_id: "codex-vinegar-9066"
- title: "식초"
- url: "https://bdocodex.com/kr/item/9066/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "vinegar"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "요리 초급 1 조건을 current BDO Codex에서 확인하고 전체 formula 교차검증과 함께 canonical current 사용에 충분하다고 판정했다."
- active: true
- is_active: true

### `recipe.vinegar.ingredient.fruit.option.fruit.quantity::codex-vinegar-9066`

- evidence_seed_key: "recipe.vinegar.ingredient.fruit.option.fruit.quantity::codex-vinegar-9066"
- source_id: "codex-vinegar-9066"
- title: "식초"
- url: "https://bdocodex.com/kr/item/9066/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "vinegar.ingredient.fruit.option.fruit"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "과일 1을 community_guide와 current BDO Codex에서 교차검증했다. 현행 공식 가이드의 과일 그룹만 적용하며 전역 환산·혼합 사용은 추론하지 않는다."
- active: true
- is_active: true

### `recipe.vinegar.ingredient.grain.option.grain.quantity::codex-vinegar-9066`

- evidence_seed_key: "recipe.vinegar.ingredient.grain.option.grain.quantity::codex-vinegar-9066"
- source_id: "codex-vinegar-9066"
- title: "식초"
- url: "https://bdocodex.com/kr/item/9066/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "vinegar.ingredient.grain.option.grain"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "곡물 1을 community_guide와 current BDO Codex에서 교차검증했다. 현행 공식 가이드의 곡물 그룹만 적용하며 전역 환산·혼합 사용은 추론하지 않는다."
- active: true
- is_active: true

### `recipe.vinegar.ingredient.leavening-agent.option.leavening-agent.quantity::codex-vinegar-9066`

- evidence_seed_key: "recipe.vinegar.ingredient.leavening-agent.option.leavening-agent.quantity::codex-vinegar-9066"
- source_id: "codex-vinegar-9066"
- title: "식초"
- url: "https://bdocodex.com/kr/item/9066/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "vinegar.ingredient.leavening-agent.option.leavening-agent"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "발효제 1을 community_guide와 current BDO Codex에서 교차검증했다. 다른 recipe의 수량으로 일반화하지 않는다."
- active: true
- is_active: true

### `recipe.vinegar.ingredient.sugar.option.sugar.quantity::codex-vinegar-9066`

- evidence_seed_key: "recipe.vinegar.ingredient.sugar.option.sugar.quantity::codex-vinegar-9066"
- source_id: "codex-vinegar-9066"
- title: "식초"
- url: "https://bdocodex.com/kr/item/9066/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "vinegar.ingredient.sugar.option.sugar"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "설탕 1을 community_guide와 current BDO Codex에서 교차검증했다. 다른 recipe의 수량으로 일반화하지 않는다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
