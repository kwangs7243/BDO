<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 구운 소시지

## Identity

- slug: "grilled-sausage"
- process_type: "cooking"
- summary: "요리 1회 시도 기준 구운 소시지 배합. 훈연 소시지 proc·결과량은 포함하지 않는다."
- verification_status: "verified"
- last_verified_at: "2026-09-11"

## Result

- material_key: "grilled-sausage"
- name_ko: "구운 소시지"
- unit: "개"

## Cooking Requirement

- required_skill_tier: "beginner"
- required_skill_level: 6

## Ingredient Slots

### 고기

- seed_key: "grilled-sausage.ingredient.meat"
- order_no: 1
- notes: null

#### grilled-sausage.ingredient.meat.option.meat

- target_type: "ingredient_group"
- required_quantity: 6.0
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

### 양파

- seed_key: "grilled-sausage.ingredient.onion"
- order_no: 2
- notes: null

#### grilled-sausage.ingredient.onion.option.onion

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "onion"
- name_ko: "양파"
- unit: "개"

### 소금

- seed_key: "grilled-sausage.ingredient.salt"
- order_no: 3
- notes: null

#### grilled-sausage.ingredient.salt.option.salt

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "salt"
- name_ko: "소금"
- unit: "개"

### 후추

- seed_key: "grilled-sausage.ingredient.pepper"
- order_no: 4
- notes: null

#### grilled-sausage.ingredient.pepper.option.pepper

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "pepper"
- name_ko: "후추"
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

### `recipe.grilled-sausage.formula::codex-grilled-sausage-9427`

- evidence_seed_key: "recipe.grilled-sausage.formula::codex-grilled-sausage-9427"
- source_id: "codex-grilled-sausage-9427"
- title: "구운 소시지"
- url: "https://bdocodex.com/kr/item/9427/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "grilled-sausage"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet의 지정 Source에서 1회 배합을 교차확인했다."
- active: true
- is_active: true

### `recipe.grilled-sausage.formula::weingchicken-grilled-sausage-19`

- evidence_seed_key: "recipe.grilled-sausage.formula::weingchicken-grilled-sausage-19"
- source_id: "weingchicken-grilled-sausage-19"
- title: "구운 소시지 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/19"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "grilled-sausage"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet의 지정 Source에서 1회 배합을 교차확인했다."
- active: true
- is_active: true

### `recipe.grilled-sausage.attempt::cooking-guide`

- evidence_seed_key: "recipe.grilled-sausage.attempt::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "grilled-sausage"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "공식 current 요리 가이드의 1회분 투입 의미만 연결한다."
- active: true
- is_active: true

### `recipe.grilled-sausage.skill::codex-grilled-sausage-9427`

- evidence_seed_key: "recipe.grilled-sausage.skill::codex-grilled-sausage-9427"
- source_id: "codex-grilled-sausage-9427"
- title: "구운 소시지"
- url: "https://bdocodex.com/kr/item/9427/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "grilled-sausage"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet에서 허용한 Source만 required skill 근거로 연결한다."
- active: true
- is_active: true

### `recipe.grilled-sausage.skill::weingchicken-grilled-sausage-19`

- evidence_seed_key: "recipe.grilled-sausage.skill::weingchicken-grilled-sausage-19"
- source_id: "weingchicken-grilled-sausage-19"
- title: "구운 소시지 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/19"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "grilled-sausage"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet에서 허용한 Source만 required skill 근거로 연결한다."
- active: true
- is_active: true

### `recipe.grilled-sausage.ingredient.meat.option.meat.quantity::codex-grilled-sausage-9427`

- evidence_seed_key: "recipe.grilled-sausage.ingredient.meat.option.meat.quantity::codex-grilled-sausage-9427"
- source_id: "codex-grilled-sausage-9427"
- title: "구운 소시지"
- url: "https://bdocodex.com/kr/item/9427/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-sausage.ingredient.meat.option.meat"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.grilled-sausage.ingredient.meat.option.meat.quantity::weingchicken-grilled-sausage-19`

- evidence_seed_key: "recipe.grilled-sausage.ingredient.meat.option.meat.quantity::weingchicken-grilled-sausage-19"
- source_id: "weingchicken-grilled-sausage-19"
- title: "구운 소시지 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/19"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-sausage.ingredient.meat.option.meat"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.grilled-sausage.ingredient.onion.option.onion.quantity::codex-grilled-sausage-9427`

- evidence_seed_key: "recipe.grilled-sausage.ingredient.onion.option.onion.quantity::codex-grilled-sausage-9427"
- source_id: "codex-grilled-sausage-9427"
- title: "구운 소시지"
- url: "https://bdocodex.com/kr/item/9427/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-sausage.ingredient.onion.option.onion"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.grilled-sausage.ingredient.onion.option.onion.quantity::weingchicken-grilled-sausage-19`

- evidence_seed_key: "recipe.grilled-sausage.ingredient.onion.option.onion.quantity::weingchicken-grilled-sausage-19"
- source_id: "weingchicken-grilled-sausage-19"
- title: "구운 소시지 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/19"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-sausage.ingredient.onion.option.onion"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.grilled-sausage.ingredient.pepper.option.pepper.quantity::codex-grilled-sausage-9427`

- evidence_seed_key: "recipe.grilled-sausage.ingredient.pepper.option.pepper.quantity::codex-grilled-sausage-9427"
- source_id: "codex-grilled-sausage-9427"
- title: "구운 소시지"
- url: "https://bdocodex.com/kr/item/9427/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-sausage.ingredient.pepper.option.pepper"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.grilled-sausage.ingredient.pepper.option.pepper.quantity::weingchicken-grilled-sausage-19`

- evidence_seed_key: "recipe.grilled-sausage.ingredient.pepper.option.pepper.quantity::weingchicken-grilled-sausage-19"
- source_id: "weingchicken-grilled-sausage-19"
- title: "구운 소시지 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/19"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-sausage.ingredient.pepper.option.pepper"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.grilled-sausage.ingredient.salt.option.salt.quantity::codex-grilled-sausage-9427`

- evidence_seed_key: "recipe.grilled-sausage.ingredient.salt.option.salt.quantity::codex-grilled-sausage-9427"
- source_id: "codex-grilled-sausage-9427"
- title: "구운 소시지"
- url: "https://bdocodex.com/kr/item/9427/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-sausage.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.grilled-sausage.ingredient.salt.option.salt.quantity::weingchicken-grilled-sausage-19`

- evidence_seed_key: "recipe.grilled-sausage.ingredient.salt.option.salt.quantity::weingchicken-grilled-sausage-19"
- source_id: "weingchicken-grilled-sausage-19"
- title: "구운 소시지 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/19"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "grilled-sausage.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
