<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 레드소스

## Identity

- slug: "red-sauce"
- process_type: "cooking"
- summary: "요리 1회 시도 기준 레드소스 배합. 요리용 생수 2 또는 정제수 1을 별도 option으로 보존한다."
- verification_status: "verified"
- last_verified_at: "2026-09-11"

## Result

- material_key: "red-sauce"
- name_ko: "레드소스"
- unit: "개"

## Recipe Requirement

- required_skill_tier: "beginner"
- required_skill_level: 1

## Ingredient Slots

### 베이스 소스

- seed_key: "red-sauce.ingredient.base-sauce"
- order_no: 1
- notes: null

#### red-sauce.ingredient.base-sauce.option.base-sauce

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "base-sauce"
- name_ko: "베이스 소스"
- unit: "개"

### 고기

- seed_key: "red-sauce.ingredient.meat"
- order_no: 2
- notes: null

#### red-sauce.ingredient.meat.option.meat

- target_type: "ingredient_group"
- required_quantity: 1.0
- order_no: 1
- notes: null
- group: "meat"
- name_ko: "고기"
- verification_status: "verified"
- last_verified_at: "2026-09-11"

Allowed current members:

- deer-meat / 사슴 고기 (개)
- sheep-meat / 양 고기 (개)
- fox-meat / 여우 고기 (개)
- rhino-meat / 코뿔소 고기 (개)
- pork / 돼지 고기 (개)
- beef / 소 고기 (개)
- raccoon-meat / 너구리 고기 (개)
- weasel-meat / 족제비 고기 (개)
- bear-meat / 곰 고기 (개)
- wolf-meat / 늑대 고기 (개)

### 물

- seed_key: "red-sauce.ingredient.water"
- order_no: 3
- notes: null

#### red-sauce.ingredient.water.option.mineral-water

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "mineral-water"
- name_ko: "요리용 생수"
- unit: "개"

#### red-sauce.ingredient.water.option.purified-water

- target_type: "material"
- required_quantity: 1.0
- order_no: 2
- notes: null
- material_key: "purified-water"
- name_ko: "정제수"
- unit: "개"

### 설탕

- seed_key: "red-sauce.ingredient.sugar"
- order_no: 4
- notes: null

#### red-sauce.ingredient.sugar.option.sugar

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "sugar"
- name_ko: "설탕"
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

- None

### Downstream Consumers

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
- relative_path: "../recipes/frank-sandwich.md"

#### `red-sauce -> steak`

- producer_recipe_slug: "red-sauce"
- producer_recipe_name_ko: "레드소스"
- producer_process_type: "cooking"
- producer_verification_status: "verified"
- consumer_recipe_slug: "steak"
- consumer_recipe_name_ko: "스테이크"
- consumer_process_type: "cooking"
- consumer_verification_status: "verified"
- material_key: "red-sauce"
- material_name_ko: "레드소스"
- unit: "개"
- required_quantity: 2.0
- consumer_slot_seed_key: "steak.ingredient.red-sauce"
- consumer_option_seed_key: "steak.ingredient.red-sauce.option.red-sauce"
- is_alternative: false
- relative_path: "../recipes/steak.md"

## Evidence and Sources

### Current evidence

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

### `recipe.red-sauce.formula::codex-red-sauce-9004`

- evidence_seed_key: "recipe.red-sauce.formula::codex-red-sauce-9004"
- source_id: "codex-red-sauce-9004"
- title: "레드소스"
- url: "https://bdocodex.com/kr/item/9004/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "red-sauce"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "기본 배합과 정제수 1 대안을 지정된 세 Recipe DB에서 검증했다. 물 option별 수량을 하나의 global group 수량으로 축약하지 않는다."
- active: true
- is_active: true

### `recipe.red-sauce.formula::codex-red-sauce-purified-546`

- evidence_seed_key: "recipe.red-sauce.formula::codex-red-sauce-purified-546"
- source_id: "codex-red-sauce-purified-546"
- title: "레드소스"
- url: "https://bdocodex.com/kr/recipe/546/?sl=1"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "red-sauce"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "기본 배합과 정제수 1 대안을 지정된 세 Recipe DB에서 검증했다. 물 option별 수량을 하나의 global group 수량으로 축약하지 않는다."
- active: true
- is_active: true

### `recipe.red-sauce.formula::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.red-sauce.formula::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "red-sauce"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "기본 배합과 정제수 1 대안을 지정된 세 Recipe DB에서 검증했다. 물 option별 수량을 하나의 global group 수량으로 축약하지 않는다."
- active: true
- is_active: true

### `recipe.red-sauce.attempt::cooking-guide`

- evidence_seed_key: "recipe.red-sauce.attempt::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "red-sauce"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "공식 current 요리 가이드의 1회분 투입 의미만 연결한다."
- active: true
- is_active: true

### `recipe.red-sauce.skill::codex-red-sauce-9004`

- evidence_seed_key: "recipe.red-sauce.skill::codex-red-sauce-9004"
- source_id: "codex-red-sauce-9004"
- title: "레드소스"
- url: "https://bdocodex.com/kr/item/9004/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "red-sauce"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "요리 초급 1 조건을 지정된 BDO Codex Source에서 확인했다."
- active: true
- is_active: true

### `recipe.red-sauce.ingredient.base-sauce.option.base-sauce.quantity::codex-red-sauce-9004`

- evidence_seed_key: "recipe.red-sauce.ingredient.base-sauce.option.base-sauce.quantity::codex-red-sauce-9004"
- source_id: "codex-red-sauce-9004"
- title: "레드소스"
- url: "https://bdocodex.com/kr/item/9004/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "red-sauce.ingredient.base-sauce.option.base-sauce"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "레드소스 1회당 베이스 소스 1개를 교차확인했다."
- active: true
- is_active: true

### `recipe.red-sauce.ingredient.base-sauce.option.base-sauce.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.red-sauce.ingredient.base-sauce.option.base-sauce.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "red-sauce.ingredient.base-sauce.option.base-sauce"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "레드소스 1회당 베이스 소스 1개를 교차확인했다."
- active: true
- is_active: true

### `recipe.red-sauce.ingredient.meat.option.meat.quantity::codex-red-sauce-9004`

- evidence_seed_key: "recipe.red-sauce.ingredient.meat.option.meat.quantity::codex-red-sauce-9004"
- source_id: "codex-red-sauce-9004"
- title: "레드소스"
- url: "https://bdocodex.com/kr/item/9004/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "red-sauce.ingredient.meat.option.meat"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "레드소스 1회당 공식 current meat group 1개를 교차확인했다. 전역 품질 환산은 적용하지 않는다."
- active: true
- is_active: true

### `recipe.red-sauce.ingredient.meat.option.meat.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.red-sauce.ingredient.meat.option.meat.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "red-sauce.ingredient.meat.option.meat"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "레드소스 1회당 공식 current meat group 1개를 교차확인했다. 전역 품질 환산은 적용하지 않는다."
- active: true
- is_active: true

### `recipe.red-sauce.ingredient.sugar.option.sugar.quantity::codex-red-sauce-9004`

- evidence_seed_key: "recipe.red-sauce.ingredient.sugar.option.sugar.quantity::codex-red-sauce-9004"
- source_id: "codex-red-sauce-9004"
- title: "레드소스"
- url: "https://bdocodex.com/kr/item/9004/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "red-sauce.ingredient.sugar.option.sugar"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "레드소스 1회당 설탕 2개를 교차확인했다."
- active: true
- is_active: true

### `recipe.red-sauce.ingredient.sugar.option.sugar.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.red-sauce.ingredient.sugar.option.sugar.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "red-sauce.ingredient.sugar.option.sugar"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "레드소스 1회당 설탕 2개를 교차확인했다."
- active: true
- is_active: true

### `recipe.red-sauce.ingredient.water.option.mineral-water.quantity::codex-red-sauce-9004`

- evidence_seed_key: "recipe.red-sauce.ingredient.water.option.mineral-water.quantity::codex-red-sauce-9004"
- source_id: "codex-red-sauce-9004"
- title: "레드소스"
- url: "https://bdocodex.com/kr/item/9004/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "red-sauce.ingredient.water.option.mineral-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "레드소스 1회당 요리용 생수 2개를 교차확인했다."
- active: true
- is_active: true

### `recipe.red-sauce.ingredient.water.option.mineral-water.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.red-sauce.ingredient.water.option.mineral-water.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "red-sauce.ingredient.water.option.mineral-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "레드소스 1회당 요리용 생수 2개를 교차확인했다."
- active: true
- is_active: true

### `recipe.red-sauce.ingredient.water.option.purified-water.quantity::codex-red-sauce-purified-546`

- evidence_seed_key: "recipe.red-sauce.ingredient.water.option.purified-water.quantity::codex-red-sauce-purified-546"
- source_id: "codex-red-sauce-purified-546"
- title: "레드소스"
- url: "https://bdocodex.com/kr/recipe/546/?sl=1"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "red-sauce.ingredient.water.option.purified-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "레드소스 1회당 정제수 1개 대안은 전용 Source만 근거로 사용한다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
