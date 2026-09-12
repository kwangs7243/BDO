<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 집중의 비약

## Identity

- slug: "concentration-elixir"
- process_type: "alchemy"
- summary: "연금 1회 시도 기준 집중의 비약의 완전 배합. 야생 들풀 2와 잡초 8은 Recipe 내부 OR option이다."
- verification_status: "verified"
- last_verified_at: "2026-09-12"

## Result

- material_key: "concentration-elixir"
- name_ko: "집중의 비약"
- unit: "개"

## Recipe Requirement

- required_skill_tier: "beginner"
- required_skill_level: 1

## Ingredient Slots

### 맑은 액체 시약

- seed_key: "concentration-elixir.ingredient.clear-liquid-reagent"
- order_no: 1
- notes: null

#### concentration-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "clear-liquid-reagent"
- name_ko: "맑은 액체 시약"
- unit: "개"

### 구름 버섯

- seed_key: "concentration-elixir.ingredient.cloud-mushroom"
- order_no: 2
- notes: null

#### concentration-elixir.ingredient.cloud-mushroom.option.cloud-mushroom

- target_type: "material"
- required_quantity: 3.0
- order_no: 1
- notes: null
- material_key: "cloud-mushroom"
- name_ko: "구름 버섯"
- unit: "개"

### 곰 피

- seed_key: "concentration-elixir.ingredient.bear-blood"
- order_no: 3
- notes: null

#### concentration-elixir.ingredient.bear-blood.option.bear-blood

- target_type: "material"
- required_quantity: 3.0
- order_no: 1
- notes: null
- material_key: "bear-blood"
- name_ko: "곰 피"
- unit: "개"

### 야생 약초

- seed_key: "concentration-elixir.ingredient.wild-herb"
- order_no: 4
- notes: null

#### concentration-elixir.ingredient.wild-herb.option.wild-grass

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "wild-grass"
- name_ko: "야생 들풀"
- unit: "개"

#### concentration-elixir.ingredient.wild-herb.option.weed

- target_type: "material"
- required_quantity: 8.0
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
- relative_path: "../recipes/clear-liquid-reagent.md"

### Downstream Consumers

- None

## Evidence and Sources

### Current evidence

### `recipe.concentration-elixir.formula::alchemy-guide`

- evidence_seed_key: "recipe.concentration-elixir.formula::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "concentration-elixir"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.formula::codex-concentration-elixir-19`

- evidence_seed_key: "recipe.concentration-elixir.formula::codex-concentration-elixir-19"
- source_id: "codex-concentration-elixir-19"
- title: "집중의 비약"
- url: "https://bdocodex.com/kr/recipe/19/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "concentration-elixir"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.formula::codex-concentration-elixir-473`

- evidence_seed_key: "recipe.concentration-elixir.formula::codex-concentration-elixir-473"
- source_id: "codex-concentration-elixir-473"
- title: "집중의 비약"
- url: "https://bdocodex.com/kr/recipe/473/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "concentration-elixir"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.formula::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.concentration-elixir.formula::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "concentration-elixir"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.attempt::alchemy-basic-guide`

- evidence_seed_key: "recipe.concentration-elixir.attempt::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "concentration-elixir"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.skill::codex-concentration-elixir-19`

- evidence_seed_key: "recipe.concentration-elixir.skill::codex-concentration-elixir-19"
- source_id: "codex-concentration-elixir-19"
- title: "집중의 비약"
- url: "https://bdocodex.com/kr/recipe/19/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "concentration-elixir"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.skill::codex-concentration-elixir-473`

- evidence_seed_key: "recipe.concentration-elixir.skill::codex-concentration-elixir-473"
- source_id: "codex-concentration-elixir-473"
- title: "집중의 비약"
- url: "https://bdocodex.com/kr/recipe/473/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "concentration-elixir"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.ingredient.bear-blood.option.bear-blood.quantity::alchemy-guide`

- evidence_seed_key: "recipe.concentration-elixir.ingredient.bear-blood.option.bear-blood.quantity::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "concentration-elixir.ingredient.bear-blood.option.bear-blood"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.ingredient.bear-blood.option.bear-blood.quantity::codex-concentration-elixir-19`

- evidence_seed_key: "recipe.concentration-elixir.ingredient.bear-blood.option.bear-blood.quantity::codex-concentration-elixir-19"
- source_id: "codex-concentration-elixir-19"
- title: "집중의 비약"
- url: "https://bdocodex.com/kr/recipe/19/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "concentration-elixir.ingredient.bear-blood.option.bear-blood"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.ingredient.bear-blood.option.bear-blood.quantity::codex-concentration-elixir-473`

- evidence_seed_key: "recipe.concentration-elixir.ingredient.bear-blood.option.bear-blood.quantity::codex-concentration-elixir-473"
- source_id: "codex-concentration-elixir-473"
- title: "집중의 비약"
- url: "https://bdocodex.com/kr/recipe/473/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "concentration-elixir.ingredient.bear-blood.option.bear-blood"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.ingredient.bear-blood.option.bear-blood.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.concentration-elixir.ingredient.bear-blood.option.bear-blood.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "concentration-elixir.ingredient.bear-blood.option.bear-blood"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent.quantity::alchemy-guide`

- evidence_seed_key: "recipe.concentration-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent.quantity::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "concentration-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent.quantity::codex-concentration-elixir-19`

- evidence_seed_key: "recipe.concentration-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent.quantity::codex-concentration-elixir-19"
- source_id: "codex-concentration-elixir-19"
- title: "집중의 비약"
- url: "https://bdocodex.com/kr/recipe/19/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "concentration-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent.quantity::codex-concentration-elixir-473`

- evidence_seed_key: "recipe.concentration-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent.quantity::codex-concentration-elixir-473"
- source_id: "codex-concentration-elixir-473"
- title: "집중의 비약"
- url: "https://bdocodex.com/kr/recipe/473/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "concentration-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.concentration-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "concentration-elixir.ingredient.clear-liquid-reagent.option.clear-liquid-reagent"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.ingredient.cloud-mushroom.option.cloud-mushroom.quantity::alchemy-guide`

- evidence_seed_key: "recipe.concentration-elixir.ingredient.cloud-mushroom.option.cloud-mushroom.quantity::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "concentration-elixir.ingredient.cloud-mushroom.option.cloud-mushroom"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.ingredient.cloud-mushroom.option.cloud-mushroom.quantity::codex-concentration-elixir-19`

- evidence_seed_key: "recipe.concentration-elixir.ingredient.cloud-mushroom.option.cloud-mushroom.quantity::codex-concentration-elixir-19"
- source_id: "codex-concentration-elixir-19"
- title: "집중의 비약"
- url: "https://bdocodex.com/kr/recipe/19/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "concentration-elixir.ingredient.cloud-mushroom.option.cloud-mushroom"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.ingredient.cloud-mushroom.option.cloud-mushroom.quantity::codex-concentration-elixir-473`

- evidence_seed_key: "recipe.concentration-elixir.ingredient.cloud-mushroom.option.cloud-mushroom.quantity::codex-concentration-elixir-473"
- source_id: "codex-concentration-elixir-473"
- title: "집중의 비약"
- url: "https://bdocodex.com/kr/recipe/473/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "concentration-elixir.ingredient.cloud-mushroom.option.cloud-mushroom"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.ingredient.cloud-mushroom.option.cloud-mushroom.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.concentration-elixir.ingredient.cloud-mushroom.option.cloud-mushroom.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "concentration-elixir.ingredient.cloud-mushroom.option.cloud-mushroom"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.ingredient.wild-herb.option.weed.quantity::alchemy-guide`

- evidence_seed_key: "recipe.concentration-elixir.ingredient.wild-herb.option.weed.quantity::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "concentration-elixir.ingredient.wild-herb.option.weed"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.ingredient.wild-herb.option.weed.quantity::codex-concentration-elixir-473`

- evidence_seed_key: "recipe.concentration-elixir.ingredient.wild-herb.option.weed.quantity::codex-concentration-elixir-473"
- source_id: "codex-concentration-elixir-473"
- title: "집중의 비약"
- url: "https://bdocodex.com/kr/recipe/473/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "concentration-elixir.ingredient.wild-herb.option.weed"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.ingredient.wild-herb.option.wild-grass.quantity::alchemy-guide`

- evidence_seed_key: "recipe.concentration-elixir.ingredient.wild-herb.option.wild-grass.quantity::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "concentration-elixir.ingredient.wild-herb.option.wild-grass"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.ingredient.wild-herb.option.wild-grass.quantity::codex-concentration-elixir-19`

- evidence_seed_key: "recipe.concentration-elixir.ingredient.wild-herb.option.wild-grass.quantity::codex-concentration-elixir-19"
- source_id: "codex-concentration-elixir-19"
- title: "집중의 비약"
- url: "https://bdocodex.com/kr/recipe/19/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "concentration-elixir.ingredient.wild-herb.option.wild-grass"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.concentration-elixir.ingredient.wild-herb.option.wild-grass.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.concentration-elixir.ingredient.wild-herb.option.wild-grass.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "concentration-elixir.ingredient.wild-herb.option.wild-grass"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
