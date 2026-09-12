<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 프랭크 샌드위치

## Identity

- slug: "frank-sandwich"
- process_type: "cooking"
- summary: "요리 1회 시도 기준 프랭크 샌드위치 배합. 양배추 2는 vegetable group으로 일반화하지 않는다."
- verification_status: "verified"
- last_verified_at: "2026-09-11"

## Result

- material_key: "frank-sandwich"
- name_ko: "프랭크 샌드위치"
- unit: "개"

## Recipe Requirement

- required_skill_tier: "professional"
- required_skill_level: 1

## Ingredient Slots

### 소시지

- seed_key: "frank-sandwich.ingredient.sausage"
- order_no: 1
- notes: null

#### frank-sandwich.ingredient.sausage.option.grilled-sausage

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "grilled-sausage"
- name_ko: "구운 소시지"
- unit: "개"

#### frank-sandwich.ingredient.sausage.option.smoked-sausage

- target_type: "material"
- required_quantity: 1.0
- order_no: 2
- notes: null
- material_key: "smoked-sausage"
- name_ko: "훈연 소시지"
- unit: "개"

### 부드러운 빵

- seed_key: "frank-sandwich.ingredient.soft-bread"
- order_no: 2
- notes: null

#### frank-sandwich.ingredient.soft-bread.option.soft-bread

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "soft-bread"
- name_ko: "부드러운 빵"
- unit: "개"

### 양배추

- seed_key: "frank-sandwich.ingredient.cabbage"
- order_no: 3
- notes: null

#### frank-sandwich.ingredient.cabbage.option.cabbage

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "cabbage"
- name_ko: "양배추"
- unit: "개"

### 레드소스

- seed_key: "frank-sandwich.ingredient.red-sauce"
- order_no: 4
- notes: null

#### frank-sandwich.ingredient.red-sauce.option.red-sauce

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "red-sauce"
- name_ko: "레드소스"
- unit: "개"


## Substitution Semantics

- Ingredient quantities are per one recipe attempt.
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

#### `grilled-sausage -> frank-sandwich`

- producer_recipe_slug: "grilled-sausage"
- producer_recipe_name_ko: "구운 소시지"
- producer_process_type: "cooking"
- producer_verification_status: "verified"
- consumer_recipe_slug: "frank-sandwich"
- consumer_recipe_name_ko: "프랭크 샌드위치"
- consumer_process_type: "cooking"
- consumer_verification_status: "verified"
- material_key: "grilled-sausage"
- material_name_ko: "구운 소시지"
- unit: "개"
- required_quantity: 2.0
- consumer_slot_seed_key: "frank-sandwich.ingredient.sausage"
- consumer_option_seed_key: "frank-sandwich.ingredient.sausage.option.grilled-sausage"
- is_alternative: true
- relative_path: "../recipes/grilled-sausage.md"

#### `red-sauce -> frank-sandwich`

- producer_recipe_slug: "red-sauce"
- producer_recipe_name_ko: "레드소스"
- producer_process_type: "cooking"
- producer_verification_status: "verified"
- consumer_recipe_slug: "frank-sandwich"
- consumer_recipe_name_ko: "프랭크 샌드위치"
- consumer_process_type: "cooking"
- consumer_verification_status: "verified"
- material_key: "red-sauce"
- material_name_ko: "레드소스"
- unit: "개"
- required_quantity: 1.0
- consumer_slot_seed_key: "frank-sandwich.ingredient.red-sauce"
- consumer_option_seed_key: "frank-sandwich.ingredient.red-sauce.option.red-sauce"
- is_alternative: false
- relative_path: "../recipes/red-sauce.md"

### Downstream Consumers

- None

## Evidence and Sources

### Current evidence

### `recipe.frank-sandwich.formula::codex-frank-sandwich-360`

- evidence_seed_key: "recipe.frank-sandwich.formula::codex-frank-sandwich-360"
- source_id: "codex-frank-sandwich-360"
- title: "프랭크 샌드위치"
- url: "https://bdocodex.com/kr/recipe/360/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "frank-sandwich"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet의 지정 Source에서 1회 배합을 교차확인했다."
- active: true
- is_active: true

### `recipe.frank-sandwich.formula::codex-frank-sandwich-smoked-361`

- evidence_seed_key: "recipe.frank-sandwich.formula::codex-frank-sandwich-smoked-361"
- source_id: "codex-frank-sandwich-smoked-361"
- title: "프랭크 샌드위치"
- url: "https://bdocodex.com/kr/recipe/361/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "frank-sandwich"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet의 지정 Source에서 1회 배합을 교차확인했다."
- active: true
- is_active: true

### `recipe.frank-sandwich.formula::weingchicken-frank-sandwich-375`

- evidence_seed_key: "recipe.frank-sandwich.formula::weingchicken-frank-sandwich-375"
- source_id: "weingchicken-frank-sandwich-375"
- title: "프랭크 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/375"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "frank-sandwich"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet의 지정 Source에서 1회 배합을 교차확인했다."
- active: true
- is_active: true

### `recipe.frank-sandwich.attempt::cooking-guide`

- evidence_seed_key: "recipe.frank-sandwich.attempt::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "frank-sandwich"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "공식 current 요리 가이드의 1회분 투입 의미만 연결한다."
- active: true
- is_active: true

### `recipe.frank-sandwich.skill::codex-frank-sandwich-360`

- evidence_seed_key: "recipe.frank-sandwich.skill::codex-frank-sandwich-360"
- source_id: "codex-frank-sandwich-360"
- title: "프랭크 샌드위치"
- url: "https://bdocodex.com/kr/recipe/360/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "frank-sandwich"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet에서 허용한 Source만 required skill 근거로 연결한다."
- active: true
- is_active: true

### `recipe.frank-sandwich.skill::weingchicken-frank-sandwich-375`

- evidence_seed_key: "recipe.frank-sandwich.skill::weingchicken-frank-sandwich-375"
- source_id: "weingchicken-frank-sandwich-375"
- title: "프랭크 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/375"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "frank-sandwich"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet에서 허용한 Source만 required skill 근거로 연결한다."
- active: true
- is_active: true

### `recipe.frank-sandwich.ingredient.cabbage.option.cabbage.quantity::codex-frank-sandwich-360`

- evidence_seed_key: "recipe.frank-sandwich.ingredient.cabbage.option.cabbage.quantity::codex-frank-sandwich-360"
- source_id: "codex-frank-sandwich-360"
- title: "프랭크 샌드위치"
- url: "https://bdocodex.com/kr/recipe/360/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "frank-sandwich.ingredient.cabbage.option.cabbage"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.frank-sandwich.ingredient.cabbage.option.cabbage.quantity::weingchicken-frank-sandwich-375`

- evidence_seed_key: "recipe.frank-sandwich.ingredient.cabbage.option.cabbage.quantity::weingchicken-frank-sandwich-375"
- source_id: "weingchicken-frank-sandwich-375"
- title: "프랭크 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/375"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "frank-sandwich.ingredient.cabbage.option.cabbage"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.frank-sandwich.ingredient.red-sauce.option.red-sauce.quantity::codex-frank-sandwich-360`

- evidence_seed_key: "recipe.frank-sandwich.ingredient.red-sauce.option.red-sauce.quantity::codex-frank-sandwich-360"
- source_id: "codex-frank-sandwich-360"
- title: "프랭크 샌드위치"
- url: "https://bdocodex.com/kr/recipe/360/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "frank-sandwich.ingredient.red-sauce.option.red-sauce"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.frank-sandwich.ingredient.red-sauce.option.red-sauce.quantity::weingchicken-frank-sandwich-375`

- evidence_seed_key: "recipe.frank-sandwich.ingredient.red-sauce.option.red-sauce.quantity::weingchicken-frank-sandwich-375"
- source_id: "weingchicken-frank-sandwich-375"
- title: "프랭크 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/375"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "frank-sandwich.ingredient.red-sauce.option.red-sauce"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.frank-sandwich.ingredient.sausage.option.grilled-sausage.quantity::codex-frank-sandwich-360`

- evidence_seed_key: "recipe.frank-sandwich.ingredient.sausage.option.grilled-sausage.quantity::codex-frank-sandwich-360"
- source_id: "codex-frank-sandwich-360"
- title: "프랭크 샌드위치"
- url: "https://bdocodex.com/kr/recipe/360/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "frank-sandwich.ingredient.sausage.option.grilled-sausage"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.frank-sandwich.ingredient.sausage.option.grilled-sausage.quantity::weingchicken-frank-sandwich-375`

- evidence_seed_key: "recipe.frank-sandwich.ingredient.sausage.option.grilled-sausage.quantity::weingchicken-frank-sandwich-375"
- source_id: "weingchicken-frank-sandwich-375"
- title: "프랭크 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/375"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "frank-sandwich.ingredient.sausage.option.grilled-sausage"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.frank-sandwich.ingredient.sausage.option.smoked-sausage.quantity::codex-frank-sandwich-smoked-361`

- evidence_seed_key: "recipe.frank-sandwich.ingredient.sausage.option.smoked-sausage.quantity::codex-frank-sandwich-smoked-361"
- source_id: "codex-frank-sandwich-smoked-361"
- title: "프랭크 샌드위치"
- url: "https://bdocodex.com/kr/recipe/361/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "frank-sandwich.ingredient.sausage.option.smoked-sausage"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.frank-sandwich.ingredient.sausage.option.smoked-sausage.quantity::weingchicken-frank-sandwich-375`

- evidence_seed_key: "recipe.frank-sandwich.ingredient.sausage.option.smoked-sausage.quantity::weingchicken-frank-sandwich-375"
- source_id: "weingchicken-frank-sandwich-375"
- title: "프랭크 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/375"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "frank-sandwich.ingredient.sausage.option.smoked-sausage"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.frank-sandwich.ingredient.soft-bread.option.soft-bread.quantity::codex-frank-sandwich-360`

- evidence_seed_key: "recipe.frank-sandwich.ingredient.soft-bread.option.soft-bread.quantity::codex-frank-sandwich-360"
- source_id: "codex-frank-sandwich-360"
- title: "프랭크 샌드위치"
- url: "https://bdocodex.com/kr/recipe/360/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "frank-sandwich.ingredient.soft-bread.option.soft-bread"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.frank-sandwich.ingredient.soft-bread.option.soft-bread.quantity::weingchicken-frank-sandwich-375`

- evidence_seed_key: "recipe.frank-sandwich.ingredient.soft-bread.option.soft-bread.quantity::weingchicken-frank-sandwich-375"
- source_id: "weingchicken-frank-sandwich-375"
- title: "프랭크 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/375"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "frank-sandwich.ingredient.soft-bread.option.soft-bread"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
