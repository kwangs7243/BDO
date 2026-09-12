<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 맑은 액체 시약

## Identity

- slug: "clear-liquid-reagent"
- process_type: "alchemy"
- summary: "연금 1회 시도 기준 맑은 액체 시약의 완전 배합. 감소 투입 성공 확률과 결과 수량은 모델링하지 않는다."
- verification_status: "verified"
- last_verified_at: "2026-09-12"

## Result

- material_key: "clear-liquid-reagent"
- name_ko: "맑은 액체 시약"
- unit: "개"

## Recipe Requirement

- required_skill_tier: "beginner"
- required_skill_level: 1

## Ingredient Slots

### 물

- seed_key: "clear-liquid-reagent.ingredient.water"
- order_no: 1
- notes: null

#### clear-liquid-reagent.ingredient.water.option.purified-water

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "purified-water"
- name_ko: "정제수"
- unit: "개"

#### clear-liquid-reagent.ingredient.water.option.distilled-water

- target_type: "material"
- required_quantity: 1.0
- order_no: 2
- notes: null
- material_key: "distilled-water"
- name_ko: "증류수"
- unit: "개"

### 소금

- seed_key: "clear-liquid-reagent.ingredient.salt"
- order_no: 2
- notes: null

#### clear-liquid-reagent.ingredient.salt.option.salt

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "salt"
- name_ko: "소금"
- unit: "개"

### 여명초

- seed_key: "clear-liquid-reagent.ingredient.dawn-herb"
- order_no: 3
- notes: null

#### clear-liquid-reagent.ingredient.dawn-herb.option.dawn-herb

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "dawn-herb"
- name_ko: "여명초"
- unit: "개"

### 야생 약초

- seed_key: "clear-liquid-reagent.ingredient.wild-herb"
- order_no: 4
- notes: null

#### clear-liquid-reagent.ingredient.wild-herb.option.wild-grass

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "wild-grass"
- name_ko: "야생 들풀"
- unit: "개"

#### clear-liquid-reagent.ingredient.wild-herb.option.weed

- target_type: "material"
- required_quantity: 1.0
- order_no: 2
- notes: null
- material_key: "weed"
- name_ko: "잡초"
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
- required_quantity is the canonical full formulation quantity for one attempt.
- Reduced-input probabilistic success is not modeled.
- Output quantity and special-result probability are not modeled.
- Alchemy level/mastery output effects are not modeled.

## Direct Recipe Dependencies

- Only explicit Material options create dependency edges.
- IngredientGroup membership is not expanded.
- Dependencies are direct only.
- No recursive quantity propagation is performed.
- No producer output/yield is inferred.

### Upstream Producers

- None

### Downstream Consumers

#### `clear-liquid-reagent -> concentration-elixir`

- producer_recipe_slug: "clear-liquid-reagent"
- producer_recipe_name_ko: "맑은 액체 시약"
- producer_process_type: "alchemy"
- producer_verification_status: "verified"
- consumer_recipe_slug: "concentration-elixir"
- consumer_recipe_name_ko: "집중의 비약"
- consumer_process_type: "alchemy"
- consumer_verification_status: "verified"
- material_key: "clear-liquid-reagent"
- material_name_ko: "맑은 액체 시약"
- unit: "개"
- required_quantity: 1.0
- consumer_slot_seed_key: "concentration-elixir.ingredient.clear-liquid-reagent"
- consumer_option_seed_key: "concentration-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent"
- is_alternative: false
- relative_path: "../recipes/concentration-elixir.md"

#### `clear-liquid-reagent -> defense-elixir`

- producer_recipe_slug: "clear-liquid-reagent"
- producer_recipe_name_ko: "맑은 액체 시약"
- producer_process_type: "alchemy"
- producer_verification_status: "verified"
- consumer_recipe_slug: "defense-elixir"
- consumer_recipe_name_ko: "방어의 비약"
- consumer_process_type: "alchemy"
- consumer_verification_status: "verified"
- material_key: "clear-liquid-reagent"
- material_name_ko: "맑은 액체 시약"
- unit: "개"
- required_quantity: 1.0
- consumer_slot_seed_key: "defense-elixir.ingredient.clear-liquid-reagent"
- consumer_option_seed_key: "defense-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent"
- is_alternative: false
- relative_path: "../recipes/defense-elixir.md"

## Evidence and Sources

### Current evidence

### `recipe.clear-liquid-reagent.formula::alchemy-guide`

- evidence_seed_key: "recipe.clear-liquid-reagent.formula::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "clear-liquid-reagent"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.formula::codex-clear-liquid-reagent-47`

- evidence_seed_key: "recipe.clear-liquid-reagent.formula::codex-clear-liquid-reagent-47"
- source_id: "codex-clear-liquid-reagent-47"
- title: "맑은 액체 시약"
- url: "https://bdocodex.com/kr/recipe/47/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "clear-liquid-reagent"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.formula::codex-clear-liquid-reagent-648`

- evidence_seed_key: "recipe.clear-liquid-reagent.formula::codex-clear-liquid-reagent-648"
- source_id: "codex-clear-liquid-reagent-648"
- title: "맑은 액체 시약"
- url: "https://bdocodex.com/kr/recipe/648/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "clear-liquid-reagent"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.formula::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.clear-liquid-reagent.formula::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "clear-liquid-reagent"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.attempt::alchemy-basic-guide`

- evidence_seed_key: "recipe.clear-liquid-reagent.attempt::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "clear-liquid-reagent"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.skill::alchemy-guide`

- evidence_seed_key: "recipe.clear-liquid-reagent.skill::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "clear-liquid-reagent"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.skill::codex-clear-liquid-reagent-47`

- evidence_seed_key: "recipe.clear-liquid-reagent.skill::codex-clear-liquid-reagent-47"
- source_id: "codex-clear-liquid-reagent-47"
- title: "맑은 액체 시약"
- url: "https://bdocodex.com/kr/recipe/47/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "clear-liquid-reagent"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.skill::codex-clear-liquid-reagent-648`

- evidence_seed_key: "recipe.clear-liquid-reagent.skill::codex-clear-liquid-reagent-648"
- source_id: "codex-clear-liquid-reagent-648"
- title: "맑은 액체 시약"
- url: "https://bdocodex.com/kr/recipe/648/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "clear-liquid-reagent"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.dawn-herb.option.dawn-herb.quantity::alchemy-guide`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.dawn-herb.option.dawn-herb.quantity::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.dawn-herb.option.dawn-herb"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.dawn-herb.option.dawn-herb.quantity::codex-clear-liquid-reagent-47`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.dawn-herb.option.dawn-herb.quantity::codex-clear-liquid-reagent-47"
- source_id: "codex-clear-liquid-reagent-47"
- title: "맑은 액체 시약"
- url: "https://bdocodex.com/kr/recipe/47/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.dawn-herb.option.dawn-herb"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.dawn-herb.option.dawn-herb.quantity::codex-clear-liquid-reagent-648`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.dawn-herb.option.dawn-herb.quantity::codex-clear-liquid-reagent-648"
- source_id: "codex-clear-liquid-reagent-648"
- title: "맑은 액체 시약"
- url: "https://bdocodex.com/kr/recipe/648/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.dawn-herb.option.dawn-herb"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.dawn-herb.option.dawn-herb.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.dawn-herb.option.dawn-herb.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.dawn-herb.option.dawn-herb"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.salt.option.salt.quantity::alchemy-guide`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.salt.option.salt.quantity::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.salt.option.salt.quantity::codex-clear-liquid-reagent-47`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.salt.option.salt.quantity::codex-clear-liquid-reagent-47"
- source_id: "codex-clear-liquid-reagent-47"
- title: "맑은 액체 시약"
- url: "https://bdocodex.com/kr/recipe/47/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.salt.option.salt.quantity::codex-clear-liquid-reagent-648`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.salt.option.salt.quantity::codex-clear-liquid-reagent-648"
- source_id: "codex-clear-liquid-reagent-648"
- title: "맑은 액체 시약"
- url: "https://bdocodex.com/kr/recipe/648/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.salt.option.salt.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.salt.option.salt.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.water.option.distilled-water.quantity::alchemy-guide`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.water.option.distilled-water.quantity::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.water.option.distilled-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.water.option.purified-water.quantity::alchemy-guide`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.water.option.purified-water.quantity::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.water.option.purified-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.water.option.purified-water.quantity::codex-clear-liquid-reagent-47`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.water.option.purified-water.quantity::codex-clear-liquid-reagent-47"
- source_id: "codex-clear-liquid-reagent-47"
- title: "맑은 액체 시약"
- url: "https://bdocodex.com/kr/recipe/47/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.water.option.purified-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.water.option.purified-water.quantity::codex-clear-liquid-reagent-648`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.water.option.purified-water.quantity::codex-clear-liquid-reagent-648"
- source_id: "codex-clear-liquid-reagent-648"
- title: "맑은 액체 시약"
- url: "https://bdocodex.com/kr/recipe/648/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.water.option.purified-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.water.option.purified-water.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.water.option.purified-water.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.water.option.purified-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.wild-herb.option.weed.quantity::alchemy-guide`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.wild-herb.option.weed.quantity::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.wild-herb.option.weed"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.wild-herb.option.weed.quantity::codex-clear-liquid-reagent-648`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.wild-herb.option.weed.quantity::codex-clear-liquid-reagent-648"
- source_id: "codex-clear-liquid-reagent-648"
- title: "맑은 액체 시약"
- url: "https://bdocodex.com/kr/recipe/648/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.wild-herb.option.weed"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.wild-herb.option.wild-grass.quantity::alchemy-guide`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.wild-herb.option.wild-grass.quantity::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.wild-herb.option.wild-grass"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.wild-herb.option.wild-grass.quantity::codex-clear-liquid-reagent-47`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.wild-herb.option.wild-grass.quantity::codex-clear-liquid-reagent-47"
- source_id: "codex-clear-liquid-reagent-47"
- title: "맑은 액체 시약"
- url: "https://bdocodex.com/kr/recipe/47/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.wild-herb.option.wild-grass"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.clear-liquid-reagent.ingredient.wild-herb.option.wild-grass.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.clear-liquid-reagent.ingredient.wild-herb.option.wild-grass.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "clear-liquid-reagent.ingredient.wild-herb.option.wild-grass"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
