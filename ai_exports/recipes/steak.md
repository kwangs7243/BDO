<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 스테이크

## Identity

- slug: "steak"
- process_type: "cooking"
- summary: "요리 1회 시도 기준 스테이크 배합. V1.9T의 레드소스 Material identity를 재사용한다."
- verification_status: "verified"
- last_verified_at: "2026-09-11"

## Result

- material_key: "steak"
- name_ko: "스테이크"
- unit: "개"

## Cooking Requirement

- required_skill_tier: "apprentice"
- required_skill_level: 1

## Ingredient Slots

### 고기

- seed_key: "steak.ingredient.meat"
- order_no: 1
- notes: null

#### steak.ingredient.meat.option.meat

- target_type: "ingredient_group"
- required_quantity: 8.0
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

### 마늘

- seed_key: "steak.ingredient.garlic"
- order_no: 2
- notes: null

#### steak.ingredient.garlic.option.garlic

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "garlic"
- name_ko: "마늘"
- unit: "개"

### 레드소스

- seed_key: "steak.ingredient.red-sauce"
- order_no: 3
- notes: null

#### steak.ingredient.red-sauce.option.red-sauce

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "red-sauce"
- name_ko: "레드소스"
- unit: "개"

### 소금

- seed_key: "steak.ingredient.salt"
- order_no: 4
- notes: null

#### steak.ingredient.salt.option.salt

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "salt"
- name_ko: "소금"
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

#### `red-sauce -> steak`

- producer_recipe_slug: "red-sauce"
- producer_recipe_name_ko: "레드소스"
- producer_verification_status: "verified"
- consumer_recipe_slug: "steak"
- consumer_recipe_name_ko: "스테이크"
- consumer_verification_status: "verified"
- material_key: "red-sauce"
- material_name_ko: "레드소스"
- unit: "개"
- required_quantity: 2.0
- consumer_slot_seed_key: "steak.ingredient.red-sauce"
- consumer_option_seed_key: "steak.ingredient.red-sauce.option.red-sauce"
- is_alternative: false
- relative_path: "../recipes/red-sauce.md"

### Downstream Consumers

- None

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

### `recipe.steak.formula::codex-steak-9401`

- evidence_seed_key: "recipe.steak.formula::codex-steak-9401"
- source_id: "codex-steak-9401"
- title: "스테이크"
- url: "https://bdocodex.com/kr/item/9401/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "steak"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet의 지정 Source에서 1회 배합을 교차확인했다."
- active: true
- is_active: true

### `recipe.steak.formula::weingchicken-steak-312`

- evidence_seed_key: "recipe.steak.formula::weingchicken-steak-312"
- source_id: "weingchicken-steak-312"
- title: "스테이크 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/312"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "steak"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet의 지정 Source에서 1회 배합을 교차확인했다."
- active: true
- is_active: true

### `recipe.steak.attempt::cooking-guide`

- evidence_seed_key: "recipe.steak.attempt::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "steak"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "공식 current 요리 가이드의 1회분 투입 의미만 연결한다."
- active: true
- is_active: true

### `recipe.steak.skill::codex-steak-9401`

- evidence_seed_key: "recipe.steak.skill::codex-steak-9401"
- source_id: "codex-steak-9401"
- title: "스테이크"
- url: "https://bdocodex.com/kr/item/9401/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "steak"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet에서 허용한 Source만 required skill 근거로 연결한다."
- active: true
- is_active: true

### `recipe.steak.skill::weingchicken-steak-312`

- evidence_seed_key: "recipe.steak.skill::weingchicken-steak-312"
- source_id: "weingchicken-steak-312"
- title: "스테이크 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/312"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "steak"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet에서 허용한 Source만 required skill 근거로 연결한다."
- active: true
- is_active: true

### `recipe.steak.ingredient.garlic.option.garlic.quantity::codex-steak-9401`

- evidence_seed_key: "recipe.steak.ingredient.garlic.option.garlic.quantity::codex-steak-9401"
- source_id: "codex-steak-9401"
- title: "스테이크"
- url: "https://bdocodex.com/kr/item/9401/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "steak.ingredient.garlic.option.garlic"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.steak.ingredient.garlic.option.garlic.quantity::weingchicken-steak-312`

- evidence_seed_key: "recipe.steak.ingredient.garlic.option.garlic.quantity::weingchicken-steak-312"
- source_id: "weingchicken-steak-312"
- title: "스테이크 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/312"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "steak.ingredient.garlic.option.garlic"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.steak.ingredient.meat.option.meat.quantity::codex-steak-9401`

- evidence_seed_key: "recipe.steak.ingredient.meat.option.meat.quantity::codex-steak-9401"
- source_id: "codex-steak-9401"
- title: "스테이크"
- url: "https://bdocodex.com/kr/item/9401/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "steak.ingredient.meat.option.meat"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.steak.ingredient.meat.option.meat.quantity::weingchicken-steak-312`

- evidence_seed_key: "recipe.steak.ingredient.meat.option.meat.quantity::weingchicken-steak-312"
- source_id: "weingchicken-steak-312"
- title: "스테이크 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/312"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "steak.ingredient.meat.option.meat"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.steak.ingredient.red-sauce.option.red-sauce.quantity::codex-steak-9401`

- evidence_seed_key: "recipe.steak.ingredient.red-sauce.option.red-sauce.quantity::codex-steak-9401"
- source_id: "codex-steak-9401"
- title: "스테이크"
- url: "https://bdocodex.com/kr/item/9401/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "steak.ingredient.red-sauce.option.red-sauce"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.steak.ingredient.red-sauce.option.red-sauce.quantity::weingchicken-steak-312`

- evidence_seed_key: "recipe.steak.ingredient.red-sauce.option.red-sauce.quantity::weingchicken-steak-312"
- source_id: "weingchicken-steak-312"
- title: "스테이크 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/312"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "steak.ingredient.red-sauce.option.red-sauce"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.steak.ingredient.salt.option.salt.quantity::codex-steak-9401`

- evidence_seed_key: "recipe.steak.ingredient.salt.option.salt.quantity::codex-steak-9401"
- source_id: "codex-steak-9401"
- title: "스테이크"
- url: "https://bdocodex.com/kr/item/9401/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "steak.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.steak.ingredient.salt.option.salt.quantity::weingchicken-steak-312`

- evidence_seed_key: "recipe.steak.ingredient.salt.option.salt.quantity::weingchicken-steak-312"
- source_id: "weingchicken-steak-312"
- title: "스테이크 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/312"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "steak.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
