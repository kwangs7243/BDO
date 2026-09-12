<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 방어의 비약

## Identity

- slug: "defense-elixir"
- process_type: "alchemy"
- summary: "연금 1회 시도 기준 방어의 비약의 완전 배합. 혈액 재료의 자동 대체 관계는 만들지 않는다."
- verification_status: "verified"
- last_verified_at: "2026-09-12"

## Result

- material_key: "defense-elixir"
- name_ko: "방어의 비약"
- unit: "개"

## Recipe Requirement

- required_skill_tier: "beginner"
- required_skill_level: 1

## Ingredient Slots

### 맑은 액체 시약

- seed_key: "defense-elixir.ingredient.clear-liquid-reagent"
- order_no: 1
- notes: null

#### defense-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "clear-liquid-reagent"
- name_ko: "맑은 액체 시약"
- unit: "개"

### 물푸레나무 수액

- seed_key: "defense-elixir.ingredient.ash-sap"
- order_no: 2
- notes: null

#### defense-elixir.ingredient.ash-sap.option.ash-sap

- target_type: "material"
- required_quantity: 6.0
- order_no: 1
- notes: null
- material_key: "ash-sap"
- name_ko: "물푸레나무 수액"
- unit: "개"

### 돼지 피

- seed_key: "defense-elixir.ingredient.pig-blood"
- order_no: 3
- notes: null

#### defense-elixir.ingredient.pig-blood.option.pig-blood

- target_type: "material"
- required_quantity: 5.0
- order_no: 1
- notes: null
- material_key: "pig-blood"
- name_ko: "돼지 피"
- unit: "개"

### 정제수

- seed_key: "defense-elixir.ingredient.purified-water"
- order_no: 4
- notes: null

#### defense-elixir.ingredient.purified-water.option.purified-water

- target_type: "material"
- required_quantity: 3.0
- order_no: 1
- notes: null
- material_key: "purified-water"
- name_ko: "정제수"
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
- relative_path: "../recipes/clear-liquid-reagent.md"

### Downstream Consumers

- None

## Evidence and Sources

### Current evidence

### `recipe.defense-elixir.formula::alchemy-advanced-guide`

- evidence_seed_key: "recipe.defense-elixir.formula::alchemy-advanced-guide"
- source_id: "alchemy-advanced-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100&utm_source=chatgpt.com"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "defense-elixir"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.defense-elixir.formula::codex-defense-elixir-27`

- evidence_seed_key: "recipe.defense-elixir.formula::codex-defense-elixir-27"
- source_id: "codex-defense-elixir-27"
- title: "방어의 비약"
- url: "https://bdocodex.com/kr/recipe/27/?utm_source=chatgpt.com"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "defense-elixir"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.defense-elixir.formula::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.defense-elixir.formula::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "defense-elixir"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.defense-elixir.attempt::alchemy-basic-guide`

- evidence_seed_key: "recipe.defense-elixir.attempt::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "defense-elixir"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.defense-elixir.skill::codex-defense-elixir-27`

- evidence_seed_key: "recipe.defense-elixir.skill::codex-defense-elixir-27"
- source_id: "codex-defense-elixir-27"
- title: "방어의 비약"
- url: "https://bdocodex.com/kr/recipe/27/?utm_source=chatgpt.com"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "defense-elixir"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.defense-elixir.ingredient.ash-sap.option.ash-sap.quantity::alchemy-advanced-guide`

- evidence_seed_key: "recipe.defense-elixir.ingredient.ash-sap.option.ash-sap.quantity::alchemy-advanced-guide"
- source_id: "alchemy-advanced-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100&utm_source=chatgpt.com"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "defense-elixir.ingredient.ash-sap.option.ash-sap"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.defense-elixir.ingredient.ash-sap.option.ash-sap.quantity::codex-defense-elixir-27`

- evidence_seed_key: "recipe.defense-elixir.ingredient.ash-sap.option.ash-sap.quantity::codex-defense-elixir-27"
- source_id: "codex-defense-elixir-27"
- title: "방어의 비약"
- url: "https://bdocodex.com/kr/recipe/27/?utm_source=chatgpt.com"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "defense-elixir.ingredient.ash-sap.option.ash-sap"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.defense-elixir.ingredient.ash-sap.option.ash-sap.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.defense-elixir.ingredient.ash-sap.option.ash-sap.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "defense-elixir.ingredient.ash-sap.option.ash-sap"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.defense-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent.quantity::alchemy-advanced-guide`

- evidence_seed_key: "recipe.defense-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent.quantity::alchemy-advanced-guide"
- source_id: "alchemy-advanced-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100&utm_source=chatgpt.com"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "defense-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.defense-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent.quantity::codex-defense-elixir-27`

- evidence_seed_key: "recipe.defense-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent.quantity::codex-defense-elixir-27"
- source_id: "codex-defense-elixir-27"
- title: "방어의 비약"
- url: "https://bdocodex.com/kr/recipe/27/?utm_source=chatgpt.com"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "defense-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.defense-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.defense-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "defense-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.defense-elixir.ingredient.pig-blood.option.pig-blood.quantity::alchemy-advanced-guide`

- evidence_seed_key: "recipe.defense-elixir.ingredient.pig-blood.option.pig-blood.quantity::alchemy-advanced-guide"
- source_id: "alchemy-advanced-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100&utm_source=chatgpt.com"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "defense-elixir.ingredient.pig-blood.option.pig-blood"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.defense-elixir.ingredient.pig-blood.option.pig-blood.quantity::codex-defense-elixir-27`

- evidence_seed_key: "recipe.defense-elixir.ingredient.pig-blood.option.pig-blood.quantity::codex-defense-elixir-27"
- source_id: "codex-defense-elixir-27"
- title: "방어의 비약"
- url: "https://bdocodex.com/kr/recipe/27/?utm_source=chatgpt.com"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "defense-elixir.ingredient.pig-blood.option.pig-blood"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.defense-elixir.ingredient.pig-blood.option.pig-blood.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.defense-elixir.ingredient.pig-blood.option.pig-blood.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "defense-elixir.ingredient.pig-blood.option.pig-blood"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.defense-elixir.ingredient.purified-water.option.purified-water.quantity::alchemy-advanced-guide`

- evidence_seed_key: "recipe.defense-elixir.ingredient.purified-water.option.purified-water.quantity::alchemy-advanced-guide"
- source_id: "alchemy-advanced-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100&utm_source=chatgpt.com"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "defense-elixir.ingredient.purified-water.option.purified-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.defense-elixir.ingredient.purified-water.option.purified-water.quantity::codex-defense-elixir-27`

- evidence_seed_key: "recipe.defense-elixir.ingredient.purified-water.option.purified-water.quantity::codex-defense-elixir-27"
- source_id: "codex-defense-elixir-27"
- title: "방어의 비약"
- url: "https://bdocodex.com/kr/recipe/27/?utm_source=chatgpt.com"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "defense-elixir.ingredient.purified-water.option.purified-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.defense-elixir.ingredient.purified-water.option.purified-water.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.defense-elixir.ingredient.purified-water.option.purified-water.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "defense-elixir.ingredient.purified-water.option.purified-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
