<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 미트 샌드위치

## Identity

- slug: "meat-sandwich"
- process_type: "cooking"
- summary: "요리 1회 시도 기준 미트 샌드위치 배합. 기존 meat·vegetable IngredientGroup을 재사용한다."
- verification_status: "verified"
- last_verified_at: "2026-09-11"

## Result

- material_key: "meat-sandwich"
- name_ko: "미트 샌드위치"
- unit: "개"

## Cooking Requirement

- required_skill_tier: "apprentice"
- required_skill_level: 6

## Ingredient Slots

### 고기

- seed_key: "meat-sandwich.ingredient.meat"
- order_no: 1
- notes: null

#### meat-sandwich.ingredient.meat.option.meat

- target_type: "ingredient_group"
- required_quantity: 7.0
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

### 부드러운 빵

- seed_key: "meat-sandwich.ingredient.soft-bread"
- order_no: 2
- notes: null

#### meat-sandwich.ingredient.soft-bread.option.soft-bread

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "soft-bread"
- name_ko: "부드러운 빵"
- unit: "개"

### 채소

- seed_key: "meat-sandwich.ingredient.vegetable"
- order_no: 3
- notes: null

#### meat-sandwich.ingredient.vegetable.option.vegetable

- target_type: "ingredient_group"
- required_quantity: 6.0
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

### 치즈

- seed_key: "meat-sandwich.ingredient.cheese"
- order_no: 4
- notes: null

#### meat-sandwich.ingredient.cheese.option.cheese

- target_type: "material"
- required_quantity: 3.0
- order_no: 1
- notes: null
- material_key: "cheese"
- name_ko: "치즈"
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

### `recipe.meat-sandwich.formula::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.meat-sandwich.formula::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "meat-sandwich"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet의 지정 Source에서 1회 배합을 교차확인했다."
- active: true
- is_active: true

### `recipe.meat-sandwich.formula::weingchicken-meat-sandwich-228`

- evidence_seed_key: "recipe.meat-sandwich.formula::weingchicken-meat-sandwich-228"
- source_id: "weingchicken-meat-sandwich-228"
- title: "미트 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/228"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "meat-sandwich"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet의 지정 Source에서 1회 배합을 교차확인했다."
- active: true
- is_active: true

### `recipe.meat-sandwich.attempt::cooking-guide`

- evidence_seed_key: "recipe.meat-sandwich.attempt::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "meat-sandwich"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "공식 current 요리 가이드의 1회분 투입 의미만 연결한다."
- active: true
- is_active: true

### `recipe.meat-sandwich.skill::weingchicken-meat-sandwich-228`

- evidence_seed_key: "recipe.meat-sandwich.skill::weingchicken-meat-sandwich-228"
- source_id: "weingchicken-meat-sandwich-228"
- title: "미트 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/228"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "meat-sandwich"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "Research Packet에서 허용한 Source만 required skill 근거로 연결한다."
- active: true
- is_active: true

### `recipe.meat-sandwich.ingredient.cheese.option.cheese.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.meat-sandwich.ingredient.cheese.option.cheese.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "meat-sandwich.ingredient.cheese.option.cheese"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.meat-sandwich.ingredient.cheese.option.cheese.quantity::weingchicken-meat-sandwich-228`

- evidence_seed_key: "recipe.meat-sandwich.ingredient.cheese.option.cheese.quantity::weingchicken-meat-sandwich-228"
- source_id: "weingchicken-meat-sandwich-228"
- title: "미트 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/228"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "meat-sandwich.ingredient.cheese.option.cheese"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.meat-sandwich.ingredient.meat.option.meat.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.meat-sandwich.ingredient.meat.option.meat.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "meat-sandwich.ingredient.meat.option.meat"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.meat-sandwich.ingredient.meat.option.meat.quantity::weingchicken-meat-sandwich-228`

- evidence_seed_key: "recipe.meat-sandwich.ingredient.meat.option.meat.quantity::weingchicken-meat-sandwich-228"
- source_id: "weingchicken-meat-sandwich-228"
- title: "미트 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/228"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "meat-sandwich.ingredient.meat.option.meat"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.meat-sandwich.ingredient.soft-bread.option.soft-bread.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.meat-sandwich.ingredient.soft-bread.option.soft-bread.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "meat-sandwich.ingredient.soft-bread.option.soft-bread"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.meat-sandwich.ingredient.soft-bread.option.soft-bread.quantity::weingchicken-meat-sandwich-228`

- evidence_seed_key: "recipe.meat-sandwich.ingredient.soft-bread.option.soft-bread.quantity::weingchicken-meat-sandwich-228"
- source_id: "weingchicken-meat-sandwich-228"
- title: "미트 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/228"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "meat-sandwich.ingredient.soft-bread.option.soft-bread"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.meat-sandwich.ingredient.vegetable.option.vegetable.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.meat-sandwich.ingredient.vegetable.option.vegetable.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "meat-sandwich.ingredient.vegetable.option.vegetable"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### `recipe.meat-sandwich.ingredient.vegetable.option.vegetable.quantity::weingchicken-meat-sandwich-228`

- evidence_seed_key: "recipe.meat-sandwich.ingredient.vegetable.option.vegetable.quantity::weingchicken-meat-sandwich-228"
- source_id: "weingchicken-meat-sandwich-228"
- title: "미트 샌드위치 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/228"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T20:16:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "meat-sandwich.ingredient.vegetable.option.vegetable"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "해당 Recipe option의 1회 필요 수량으로만 사용하며 전역 환산을 만들지 않는다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
