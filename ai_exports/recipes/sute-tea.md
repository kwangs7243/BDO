<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 수테차

## Identity

- slug: "sute-tea"
- process_type: "cooking"
- summary: "요리 1회 시도 기준 수테차 배합. 향이 좋은 차 2 또는 향이 진한 차 1을 Recipe 내부 OR option으로 보존한다."
- verification_status: "verified"
- last_verified_at: "2026-09-11"

## Result

- material_key: "sute-tea"
- name_ko: "수테차"
- unit: "개"

## Cooking Requirement

- required_skill_tier: "skilled"
- required_skill_level: 1

## Ingredient Slots

### 차

- seed_key: "sute-tea.ingredient.tea"
- order_no: 1
- notes: null

#### sute-tea.ingredient.tea.option.tea-with-fine-scent

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "tea-with-fine-scent"
- name_ko: "향이 좋은 차"
- unit: "개"

#### sute-tea.ingredient.tea.option.tea-with-strong-scent

- target_type: "material"
- required_quantity: 1.0
- order_no: 2
- notes: null
- material_key: "tea-with-strong-scent"
- name_ko: "향이 진한 차"
- unit: "개"

### 우유

- seed_key: "sute-tea.ingredient.milk"
- order_no: 2
- notes: null

#### sute-tea.ingredient.milk.option.milk

- target_type: "material"
- required_quantity: 3.0
- order_no: 1
- notes: null
- material_key: "milk"
- name_ko: "우유"
- unit: "개"

### 소금

- seed_key: "sute-tea.ingredient.salt"
- order_no: 3
- notes: null

#### sute-tea.ingredient.salt.option.salt

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "salt"
- name_ko: "소금"
- unit: "개"

### 버터

- seed_key: "sute-tea.ingredient.butter"
- order_no: 4
- notes: null

#### sute-tea.ingredient.butter.option.butter

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "butter"
- name_ko: "버터"
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

#### `tea-with-fine-scent -> sute-tea`

- producer_recipe_slug: "tea-with-fine-scent"
- producer_recipe_name_ko: "향이 좋은 차"
- producer_verification_status: "verified"
- consumer_recipe_slug: "sute-tea"
- consumer_recipe_name_ko: "수테차"
- consumer_verification_status: "verified"
- material_key: "tea-with-fine-scent"
- material_name_ko: "향이 좋은 차"
- unit: "개"
- required_quantity: 2.0
- consumer_slot_seed_key: "sute-tea.ingredient.tea"
- consumer_option_seed_key: "sute-tea.ingredient.tea.option.tea-with-fine-scent"
- is_alternative: true
- relative_path: "../recipes/tea-with-fine-scent.md"

### Downstream Consumers

- None

## Evidence and Sources

### Current evidence

### `recipe.sute-tea.formula::codex-sute-tea-117`

- evidence_seed_key: "recipe.sute-tea.formula::codex-sute-tea-117"
- source_id: "codex-sute-tea-117"
- title: "수테차"
- url: "https://bdocodex.com/kr/recipe/117/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "sute-tea"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet의 지정 Source에서 1회 배합을 교차확인했다."
- active: true
- is_active: true

### `recipe.sute-tea.formula::codex-sute-tea-special-560`

- evidence_seed_key: "recipe.sute-tea.formula::codex-sute-tea-special-560"
- source_id: "codex-sute-tea-special-560"
- title: "수테차"
- url: "https://bdocodex.com/kr/recipe/560/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "sute-tea"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet의 지정 Source에서 1회 배합을 교차확인했다."
- active: true
- is_active: true

### `recipe.sute-tea.formula::weingchicken-healthy-sute-tea-222`

- evidence_seed_key: "recipe.sute-tea.formula::weingchicken-healthy-sute-tea-222"
- source_id: "weingchicken-healthy-sute-tea-222"
- title: "몸에 좋은 수테차 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/222"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "sute-tea"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet의 지정 Source에서 1회 배합을 교차확인했다."
- active: true
- is_active: true

### `recipe.sute-tea.attempt::cooking-guide`

- evidence_seed_key: "recipe.sute-tea.attempt::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "sute-tea"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "공식 current 요리 가이드의 1회분 투입 의미만 연결한다."
- active: true
- is_active: true

### `recipe.sute-tea.skill::codex-sute-tea-117`

- evidence_seed_key: "recipe.sute-tea.skill::codex-sute-tea-117"
- source_id: "codex-sute-tea-117"
- title: "수테차"
- url: "https://bdocodex.com/kr/recipe/117/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "sute-tea"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet에서 허용한 Source만 required skill 근거로 연결한다."
- active: true
- is_active: true

### `recipe.sute-tea.ingredient.butter.option.butter.quantity::codex-sute-tea-117`

- evidence_seed_key: "recipe.sute-tea.ingredient.butter.option.butter.quantity::codex-sute-tea-117"
- source_id: "codex-sute-tea-117"
- title: "수테차"
- url: "https://bdocodex.com/kr/recipe/117/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "sute-tea.ingredient.butter.option.butter"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.sute-tea.ingredient.butter.option.butter.quantity::codex-sute-tea-special-560`

- evidence_seed_key: "recipe.sute-tea.ingredient.butter.option.butter.quantity::codex-sute-tea-special-560"
- source_id: "codex-sute-tea-special-560"
- title: "수테차"
- url: "https://bdocodex.com/kr/recipe/560/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "sute-tea.ingredient.butter.option.butter"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.sute-tea.ingredient.butter.option.butter.quantity::weingchicken-healthy-sute-tea-222`

- evidence_seed_key: "recipe.sute-tea.ingredient.butter.option.butter.quantity::weingchicken-healthy-sute-tea-222"
- source_id: "weingchicken-healthy-sute-tea-222"
- title: "몸에 좋은 수테차 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/222"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "sute-tea.ingredient.butter.option.butter"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.sute-tea.ingredient.milk.option.milk.quantity::codex-sute-tea-117`

- evidence_seed_key: "recipe.sute-tea.ingredient.milk.option.milk.quantity::codex-sute-tea-117"
- source_id: "codex-sute-tea-117"
- title: "수테차"
- url: "https://bdocodex.com/kr/recipe/117/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "sute-tea.ingredient.milk.option.milk"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.sute-tea.ingredient.milk.option.milk.quantity::codex-sute-tea-special-560`

- evidence_seed_key: "recipe.sute-tea.ingredient.milk.option.milk.quantity::codex-sute-tea-special-560"
- source_id: "codex-sute-tea-special-560"
- title: "수테차"
- url: "https://bdocodex.com/kr/recipe/560/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "sute-tea.ingredient.milk.option.milk"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.sute-tea.ingredient.milk.option.milk.quantity::weingchicken-healthy-sute-tea-222`

- evidence_seed_key: "recipe.sute-tea.ingredient.milk.option.milk.quantity::weingchicken-healthy-sute-tea-222"
- source_id: "weingchicken-healthy-sute-tea-222"
- title: "몸에 좋은 수테차 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/222"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "sute-tea.ingredient.milk.option.milk"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.sute-tea.ingredient.salt.option.salt.quantity::codex-sute-tea-117`

- evidence_seed_key: "recipe.sute-tea.ingredient.salt.option.salt.quantity::codex-sute-tea-117"
- source_id: "codex-sute-tea-117"
- title: "수테차"
- url: "https://bdocodex.com/kr/recipe/117/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "sute-tea.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.sute-tea.ingredient.salt.option.salt.quantity::codex-sute-tea-special-560`

- evidence_seed_key: "recipe.sute-tea.ingredient.salt.option.salt.quantity::codex-sute-tea-special-560"
- source_id: "codex-sute-tea-special-560"
- title: "수테차"
- url: "https://bdocodex.com/kr/recipe/560/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "sute-tea.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.sute-tea.ingredient.salt.option.salt.quantity::weingchicken-healthy-sute-tea-222`

- evidence_seed_key: "recipe.sute-tea.ingredient.salt.option.salt.quantity::weingchicken-healthy-sute-tea-222"
- source_id: "weingchicken-healthy-sute-tea-222"
- title: "몸에 좋은 수테차 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/222"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "sute-tea.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.sute-tea.ingredient.tea.option.tea-with-fine-scent.quantity::codex-sute-tea-117`

- evidence_seed_key: "recipe.sute-tea.ingredient.tea.option.tea-with-fine-scent.quantity::codex-sute-tea-117"
- source_id: "codex-sute-tea-117"
- title: "수테차"
- url: "https://bdocodex.com/kr/recipe/117/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "sute-tea.ingredient.tea.option.tea-with-fine-scent"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.sute-tea.ingredient.tea.option.tea-with-fine-scent.quantity::weingchicken-healthy-sute-tea-222`

- evidence_seed_key: "recipe.sute-tea.ingredient.tea.option.tea-with-fine-scent.quantity::weingchicken-healthy-sute-tea-222"
- source_id: "weingchicken-healthy-sute-tea-222"
- title: "몸에 좋은 수테차 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/222"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "sute-tea.ingredient.tea.option.tea-with-fine-scent"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.sute-tea.ingredient.tea.option.tea-with-strong-scent.quantity::codex-sute-tea-special-560`

- evidence_seed_key: "recipe.sute-tea.ingredient.tea.option.tea-with-strong-scent.quantity::codex-sute-tea-special-560"
- source_id: "codex-sute-tea-special-560"
- title: "수테차"
- url: "https://bdocodex.com/kr/recipe/560/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "sute-tea.ingredient.tea.option.tea-with-strong-scent"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.sute-tea.ingredient.tea.option.tea-with-strong-scent.quantity::weingchicken-healthy-sute-tea-222`

- evidence_seed_key: "recipe.sute-tea.ingredient.tea.option.tea-with-strong-scent.quantity::weingchicken-healthy-sute-tea-222"
- source_id: "weingchicken-healthy-sute-tea-222"
- title: "몸에 좋은 수테차 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/222"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "sute-tea.ingredient.tea.option.tea-with-strong-scent"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
