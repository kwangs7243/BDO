<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 순수한 가루 시약

## Identity

- slug: "pure-powder-reagent"
- process_type: "alchemy"
- summary: "연금 1회 시도 기준 순수한 가루 시약의 완전 배합. 공식 고급 가이드의 충돌하는 정확 배합은 근거로 사용하지 않는다."
- verification_status: "verified"
- last_verified_at: "2026-09-12"

## Result

- material_key: "pure-powder-reagent"
- name_ko: "순수한 가루 시약"
- unit: "개"

## Recipe Requirement

- required_skill_tier: "beginner"
- required_skill_level: 1

## Ingredient Slots

### 정제수

- seed_key: "pure-powder-reagent.ingredient.water"
- order_no: 1
- notes: null

#### pure-powder-reagent.ingredient.water.option.purified-water

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "purified-water"
- name_ko: "정제수"
- unit: "개"

### 설탕

- seed_key: "pure-powder-reagent.ingredient.sugar"
- order_no: 2
- notes: null

#### pure-powder-reagent.ingredient.sugar.option.sugar

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "sugar"
- name_ko: "설탕"
- unit: "개"

### 은빛 철쭉

- seed_key: "pure-powder-reagent.ingredient.silver-azalea"
- order_no: 3
- notes: null

#### pure-powder-reagent.ingredient.silver-azalea.option.silver-azalea

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "silver-azalea"
- name_ko: "은빛 철쭉"
- unit: "개"

### 야생 약초

- seed_key: "pure-powder-reagent.ingredient.wild-herb"
- order_no: 4
- notes: null

#### pure-powder-reagent.ingredient.wild-herb.option.wild-grass

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "wild-grass"
- name_ko: "야생 들풀"
- unit: "개"

#### pure-powder-reagent.ingredient.wild-herb.option.weed

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

- None

## Evidence and Sources

### Current evidence

### `recipe.pure-powder-reagent.formula::codex-pure-powder-reagent-469`

- evidence_seed_key: "recipe.pure-powder-reagent.formula::codex-pure-powder-reagent-469"
- source_id: "codex-pure-powder-reagent-469"
- title: "순수한 가루 시약"
- url: "https://bdocodex.com/kr/recipe/469/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "pure-powder-reagent"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.formula::codex-pure-powder-reagent-48`

- evidence_seed_key: "recipe.pure-powder-reagent.formula::codex-pure-powder-reagent-48"
- source_id: "codex-pure-powder-reagent-48"
- title: "순수한 가루 시약"
- url: "https://bdocodex.com/kr/recipe/48/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "pure-powder-reagent"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.formula::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.pure-powder-reagent.formula::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "pure-powder-reagent"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.attempt::alchemy-basic-guide`

- evidence_seed_key: "recipe.pure-powder-reagent.attempt::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "pure-powder-reagent"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.skill::alchemy-guide`

- evidence_seed_key: "recipe.pure-powder-reagent.skill::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "pure-powder-reagent"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.skill::codex-pure-powder-reagent-469`

- evidence_seed_key: "recipe.pure-powder-reagent.skill::codex-pure-powder-reagent-469"
- source_id: "codex-pure-powder-reagent-469"
- title: "순수한 가루 시약"
- url: "https://bdocodex.com/kr/recipe/469/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "pure-powder-reagent"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.skill::codex-pure-powder-reagent-48`

- evidence_seed_key: "recipe.pure-powder-reagent.skill::codex-pure-powder-reagent-48"
- source_id: "codex-pure-powder-reagent-48"
- title: "순수한 가루 시약"
- url: "https://bdocodex.com/kr/recipe/48/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "pure-powder-reagent"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.ingredient.silver-azalea.option.silver-azalea.quantity::codex-pure-powder-reagent-469`

- evidence_seed_key: "recipe.pure-powder-reagent.ingredient.silver-azalea.option.silver-azalea.quantity::codex-pure-powder-reagent-469"
- source_id: "codex-pure-powder-reagent-469"
- title: "순수한 가루 시약"
- url: "https://bdocodex.com/kr/recipe/469/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "pure-powder-reagent.ingredient.silver-azalea.option.silver-azalea"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.ingredient.silver-azalea.option.silver-azalea.quantity::codex-pure-powder-reagent-48`

- evidence_seed_key: "recipe.pure-powder-reagent.ingredient.silver-azalea.option.silver-azalea.quantity::codex-pure-powder-reagent-48"
- source_id: "codex-pure-powder-reagent-48"
- title: "순수한 가루 시약"
- url: "https://bdocodex.com/kr/recipe/48/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "pure-powder-reagent.ingredient.silver-azalea.option.silver-azalea"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.ingredient.silver-azalea.option.silver-azalea.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.pure-powder-reagent.ingredient.silver-azalea.option.silver-azalea.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "pure-powder-reagent.ingredient.silver-azalea.option.silver-azalea"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.ingredient.sugar.option.sugar.quantity::codex-pure-powder-reagent-469`

- evidence_seed_key: "recipe.pure-powder-reagent.ingredient.sugar.option.sugar.quantity::codex-pure-powder-reagent-469"
- source_id: "codex-pure-powder-reagent-469"
- title: "순수한 가루 시약"
- url: "https://bdocodex.com/kr/recipe/469/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "pure-powder-reagent.ingredient.sugar.option.sugar"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.ingredient.sugar.option.sugar.quantity::codex-pure-powder-reagent-48`

- evidence_seed_key: "recipe.pure-powder-reagent.ingredient.sugar.option.sugar.quantity::codex-pure-powder-reagent-48"
- source_id: "codex-pure-powder-reagent-48"
- title: "순수한 가루 시약"
- url: "https://bdocodex.com/kr/recipe/48/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "pure-powder-reagent.ingredient.sugar.option.sugar"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.ingredient.sugar.option.sugar.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.pure-powder-reagent.ingredient.sugar.option.sugar.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "pure-powder-reagent.ingredient.sugar.option.sugar"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.ingredient.water.option.purified-water.quantity::codex-pure-powder-reagent-469`

- evidence_seed_key: "recipe.pure-powder-reagent.ingredient.water.option.purified-water.quantity::codex-pure-powder-reagent-469"
- source_id: "codex-pure-powder-reagent-469"
- title: "순수한 가루 시약"
- url: "https://bdocodex.com/kr/recipe/469/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "pure-powder-reagent.ingredient.water.option.purified-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.ingredient.water.option.purified-water.quantity::codex-pure-powder-reagent-48`

- evidence_seed_key: "recipe.pure-powder-reagent.ingredient.water.option.purified-water.quantity::codex-pure-powder-reagent-48"
- source_id: "codex-pure-powder-reagent-48"
- title: "순수한 가루 시약"
- url: "https://bdocodex.com/kr/recipe/48/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "pure-powder-reagent.ingredient.water.option.purified-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.ingredient.water.option.purified-water.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.pure-powder-reagent.ingredient.water.option.purified-water.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "pure-powder-reagent.ingredient.water.option.purified-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.ingredient.wild-herb.option.weed.quantity::codex-pure-powder-reagent-469`

- evidence_seed_key: "recipe.pure-powder-reagent.ingredient.wild-herb.option.weed.quantity::codex-pure-powder-reagent-469"
- source_id: "codex-pure-powder-reagent-469"
- title: "순수한 가루 시약"
- url: "https://bdocodex.com/kr/recipe/469/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "pure-powder-reagent.ingredient.wild-herb.option.weed"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.ingredient.wild-herb.option.wild-grass.quantity::codex-pure-powder-reagent-48`

- evidence_seed_key: "recipe.pure-powder-reagent.ingredient.wild-herb.option.wild-grass.quantity::codex-pure-powder-reagent-48"
- source_id: "codex-pure-powder-reagent-48"
- title: "순수한 가루 시약"
- url: "https://bdocodex.com/kr/recipe/48/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "pure-powder-reagent.ingredient.wild-herb.option.wild-grass"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### `recipe.pure-powder-reagent.ingredient.wild-herb.option.wild-grass.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.pure-powder-reagent.ingredient.wild-herb.option.wild-grass.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "pure-powder-reagent.ingredient.wild-herb.option.wild-grass"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-12"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
