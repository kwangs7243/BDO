<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 햄 샌드위치

## Identity

- slug: "ham-sandwich"
- process_type: "cooking"
- summary: "요리 1회 시도 기준 햄 샌드위치 배합. 구운 소시지 2 또는 훈연 소시지 1을 Recipe 내부 OR option으로 보존한다."
- verification_status: "verified"
- last_verified_at: "2026-09-11"

## Result

- material_key: "ham-sandwich"
- name_ko: "햄 샌드위치"
- unit: "개"

## Cooking Requirement

- required_skill_tier: "skilled"
- required_skill_level: 1

## Ingredient Slots

### 소시지

- seed_key: "ham-sandwich.ingredient.sausage"
- order_no: 1
- notes: null

#### ham-sandwich.ingredient.sausage.option.grilled-sausage

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "grilled-sausage"
- name_ko: "구운 소시지"
- unit: "개"

#### ham-sandwich.ingredient.sausage.option.smoked-sausage

- target_type: "material"
- required_quantity: 1.0
- order_no: 2
- notes: null
- material_key: "smoked-sausage"
- name_ko: "훈연 소시지"
- unit: "개"

### 부드러운 빵

- seed_key: "ham-sandwich.ingredient.soft-bread"
- order_no: 2
- notes: null

#### ham-sandwich.ingredient.soft-bread.option.soft-bread

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "soft-bread"
- name_ko: "부드러운 빵"
- unit: "개"

### 채소

- seed_key: "ham-sandwich.ingredient.vegetable"
- order_no: 3
- notes: null

#### ham-sandwich.ingredient.vegetable.option.vegetable

- target_type: "ingredient_group"
- required_quantity: 5.0
- order_no: 1
- notes: null
- group: "vegetable"
- name_ko: "채소"
- verification_status: "verified"
- last_verified_at: "2026-09-11"

Allowed current members:

- pumpkin / 호박 (개)
- olive / 올리브 (개)
- tomato / 토마토 (개)
- paprika / 파프리카 (개)
- cabbage / 양배추 (개)

### 달걀

- seed_key: "ham-sandwich.ingredient.egg"
- order_no: 4
- notes: null

#### ham-sandwich.ingredient.egg.option.egg

- target_type: "material"
- required_quantity: 4.0
- order_no: 1
- notes: null
- material_key: "egg"
- name_ko: "달걀"
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

#### `grilled-sausage -> ham-sandwich`

- producer_recipe_slug: "grilled-sausage"
- producer_recipe_name_ko: "구운 소시지"
- producer_verification_status: "verified"
- consumer_recipe_slug: "ham-sandwich"
- consumer_recipe_name_ko: "햄 샌드위치"
- consumer_verification_status: "verified"
- material_key: "grilled-sausage"
- material_name_ko: "구운 소시지"
- unit: "개"
- required_quantity: 2.0
- consumer_slot_seed_key: "ham-sandwich.ingredient.sausage"
- consumer_option_seed_key: "ham-sandwich.ingredient.sausage.option.grilled-sausage"
- is_alternative: true
- relative_path: "../recipes/grilled-sausage.md"

### Downstream Consumers

- None

## Evidence and Sources

### Current evidence

### `ingredient-group.vegetable.membership::cooking-guide`

- evidence_seed_key: "ingredient-group.vegetable.membership::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "ingredient_group"
- entity_id: "vegetable"
- claim_key: "members"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "2026-09-11 공식 current 요리 가이드의 대체품 목록을 재확인했다. 그룹 소속은 전역 수량 환산을 뜻하지 않는다."
- active: true
- is_active: true

### `recipe.ham-sandwich.formula::codex-ham-sandwich-136`

- evidence_seed_key: "recipe.ham-sandwich.formula::codex-ham-sandwich-136"
- source_id: "codex-ham-sandwich-136"
- title: "햄 샌드위치"
- url: "https://bdocodex.com/kr/recipe/136/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "ham-sandwich"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet의 지정 Source에서 1회 배합을 교차확인했다."
- active: true
- is_active: true

### `recipe.ham-sandwich.formula::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.ham-sandwich.formula::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "ham-sandwich"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet의 지정 Source에서 1회 배합을 교차확인했다."
- active: true
- is_active: true

### `recipe.ham-sandwich.formula::weingchicken-ham-sandwich-139`

- evidence_seed_key: "recipe.ham-sandwich.formula::weingchicken-ham-sandwich-139"
- source_id: "weingchicken-ham-sandwich-139"
- title: "햄 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/139"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "ham-sandwich"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet의 지정 Source에서 1회 배합을 교차확인했다."
- active: true
- is_active: true

### `recipe.ham-sandwich.attempt::cooking-guide`

- evidence_seed_key: "recipe.ham-sandwich.attempt::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "ham-sandwich"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "공식 current 요리 가이드의 1회분 투입 의미만 연결한다."
- active: true
- is_active: true

### `recipe.ham-sandwich.skill::codex-ham-sandwich-136`

- evidence_seed_key: "recipe.ham-sandwich.skill::codex-ham-sandwich-136"
- source_id: "codex-ham-sandwich-136"
- title: "햄 샌드위치"
- url: "https://bdocodex.com/kr/recipe/136/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "ham-sandwich"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet에서 허용한 Source만 required skill 근거로 연결한다."
- active: true
- is_active: true

### `recipe.ham-sandwich.skill::weingchicken-ham-sandwich-139`

- evidence_seed_key: "recipe.ham-sandwich.skill::weingchicken-ham-sandwich-139"
- source_id: "weingchicken-ham-sandwich-139"
- title: "햄 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/139"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "ham-sandwich"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet에서 허용한 Source만 required skill 근거로 연결한다."
- active: true
- is_active: true

### `recipe.ham-sandwich.ingredient.egg.option.egg.quantity::codex-ham-sandwich-136`

- evidence_seed_key: "recipe.ham-sandwich.ingredient.egg.option.egg.quantity::codex-ham-sandwich-136"
- source_id: "codex-ham-sandwich-136"
- title: "햄 샌드위치"
- url: "https://bdocodex.com/kr/recipe/136/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "ham-sandwich.ingredient.egg.option.egg"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.ham-sandwich.ingredient.egg.option.egg.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.ham-sandwich.ingredient.egg.option.egg.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "ham-sandwich.ingredient.egg.option.egg"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.ham-sandwich.ingredient.egg.option.egg.quantity::weingchicken-ham-sandwich-139`

- evidence_seed_key: "recipe.ham-sandwich.ingredient.egg.option.egg.quantity::weingchicken-ham-sandwich-139"
- source_id: "weingchicken-ham-sandwich-139"
- title: "햄 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/139"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "ham-sandwich.ingredient.egg.option.egg"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.ham-sandwich.ingredient.sausage.option.grilled-sausage.quantity::codex-ham-sandwich-136`

- evidence_seed_key: "recipe.ham-sandwich.ingredient.sausage.option.grilled-sausage.quantity::codex-ham-sandwich-136"
- source_id: "codex-ham-sandwich-136"
- title: "햄 샌드위치"
- url: "https://bdocodex.com/kr/recipe/136/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "ham-sandwich.ingredient.sausage.option.grilled-sausage"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.ham-sandwich.ingredient.sausage.option.grilled-sausage.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.ham-sandwich.ingredient.sausage.option.grilled-sausage.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "ham-sandwich.ingredient.sausage.option.grilled-sausage"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.ham-sandwich.ingredient.sausage.option.grilled-sausage.quantity::weingchicken-ham-sandwich-139`

- evidence_seed_key: "recipe.ham-sandwich.ingredient.sausage.option.grilled-sausage.quantity::weingchicken-ham-sandwich-139"
- source_id: "weingchicken-ham-sandwich-139"
- title: "햄 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/139"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "ham-sandwich.ingredient.sausage.option.grilled-sausage"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.ham-sandwich.ingredient.sausage.option.smoked-sausage.quantity::weingchicken-ham-sandwich-139`

- evidence_seed_key: "recipe.ham-sandwich.ingredient.sausage.option.smoked-sausage.quantity::weingchicken-ham-sandwich-139"
- source_id: "weingchicken-ham-sandwich-139"
- title: "햄 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/139"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "ham-sandwich.ingredient.sausage.option.smoked-sausage"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.ham-sandwich.ingredient.soft-bread.option.soft-bread.quantity::codex-ham-sandwich-136`

- evidence_seed_key: "recipe.ham-sandwich.ingredient.soft-bread.option.soft-bread.quantity::codex-ham-sandwich-136"
- source_id: "codex-ham-sandwich-136"
- title: "햄 샌드위치"
- url: "https://bdocodex.com/kr/recipe/136/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "ham-sandwich.ingredient.soft-bread.option.soft-bread"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.ham-sandwich.ingredient.soft-bread.option.soft-bread.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.ham-sandwich.ingredient.soft-bread.option.soft-bread.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "ham-sandwich.ingredient.soft-bread.option.soft-bread"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.ham-sandwich.ingredient.soft-bread.option.soft-bread.quantity::weingchicken-ham-sandwich-139`

- evidence_seed_key: "recipe.ham-sandwich.ingredient.soft-bread.option.soft-bread.quantity::weingchicken-ham-sandwich-139"
- source_id: "weingchicken-ham-sandwich-139"
- title: "햄 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/139"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "ham-sandwich.ingredient.soft-bread.option.soft-bread"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.ham-sandwich.ingredient.vegetable.option.vegetable.quantity::codex-ham-sandwich-136`

- evidence_seed_key: "recipe.ham-sandwich.ingredient.vegetable.option.vegetable.quantity::codex-ham-sandwich-136"
- source_id: "codex-ham-sandwich-136"
- title: "햄 샌드위치"
- url: "https://bdocodex.com/kr/recipe/136/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "ham-sandwich.ingredient.vegetable.option.vegetable"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.ham-sandwich.ingredient.vegetable.option.vegetable.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.ham-sandwich.ingredient.vegetable.option.vegetable.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "ham-sandwich.ingredient.vegetable.option.vegetable"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.ham-sandwich.ingredient.vegetable.option.vegetable.quantity::weingchicken-ham-sandwich-139`

- evidence_seed_key: "recipe.ham-sandwich.ingredient.vegetable.option.vegetable.quantity::weingchicken-ham-sandwich-139"
- source_id: "weingchicken-ham-sandwich-139"
- title: "햄 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/139"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "ham-sandwich.ingredient.vegetable.option.vegetable"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
