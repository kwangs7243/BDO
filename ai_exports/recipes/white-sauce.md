<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 화이트소스

## Identity

- slug: "white-sauce"
- process_type: "cooking"
- summary: "요리 1회 시도 기준 화이트소스 배합. 기존 공식 current fruit IngredientGroup을 재사용한다."
- verification_status: "verified"
- last_verified_at: "2026-09-11"

## Result

- material_key: "white-sauce"
- name_ko: "화이트소스"
- unit: "개"

## Cooking Requirement

- required_skill_tier: "beginner"
- required_skill_level: 1

## Ingredient Slots

### 베이스 소스

- seed_key: "white-sauce.ingredient.base-sauce"
- order_no: 1
- notes: null

#### white-sauce.ingredient.base-sauce.option.base-sauce

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "base-sauce"
- name_ko: "베이스 소스"
- unit: "개"

### 과일

- seed_key: "white-sauce.ingredient.fruit"
- order_no: 2
- notes: null

#### white-sauce.ingredient.fruit.option.fruit

- target_type: "ingredient_group"
- required_quantity: 1.0
- order_no: 1
- notes: null
- group: "fruit"
- name_ko: "과일"
- verification_status: "verified"
- last_verified_at: "2026-09-11"

Allowed current members:

- grape / 포도 (개)
- strawberry / 딸기 (개)
- apple / 사과 (개)
- cherry / 체리 (개)
- pear / 배 (개)
- banana / 바나나 (개)
- pineapple / 파인애플 (개)

### 우유

- seed_key: "white-sauce.ingredient.milk"
- order_no: 3
- notes: null

#### white-sauce.ingredient.milk.option.milk

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "milk"
- name_ko: "우유"
- unit: "개"

### 조리용 와인

- seed_key: "white-sauce.ingredient.cooking-wine"
- order_no: 4
- notes: null

#### white-sauce.ingredient.cooking-wine.option.cooking-wine

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "cooking-wine"
- name_ko: "조리용 와인"
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

### `ingredient-group.fruit.membership::cooking-guide`

- evidence_seed_key: "ingredient-group.fruit.membership::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "ingredient_group"
- entity_id: "fruit"
- claim_key: "members"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "2026-09-11 공식 current 요리 가이드의 대체품 목록을 재확인했다. 그룹 소속은 전역 수량 환산을 뜻하지 않는다."
- active: true
- is_active: true

### `recipe.white-sauce.formula::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.white-sauce.formula::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "white-sauce"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "위잉치킨 제작노트와 인벤 Recipe DB에서 기본 배합을 교차확인했다. 공식 current 가이드는 exact formula 근거로 사용하지 않는다."
- active: true
- is_active: true

### `recipe.white-sauce.formula::weingchicken-white-sauce-152`

- evidence_seed_key: "recipe.white-sauce.formula::weingchicken-white-sauce-152"
- source_id: "weingchicken-white-sauce-152"
- title: "화이트소스 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/152"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "white-sauce"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "위잉치킨 제작노트와 인벤 Recipe DB에서 기본 배합을 교차확인했다. 공식 current 가이드는 exact formula 근거로 사용하지 않는다."
- active: true
- is_active: true

### `recipe.white-sauce.attempt::cooking-guide`

- evidence_seed_key: "recipe.white-sauce.attempt::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "white-sauce"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "공식 current 요리 가이드의 1회분 투입 의미만 연결한다."
- active: true
- is_active: true

### `recipe.white-sauce.skill::weingchicken-white-sauce-152`

- evidence_seed_key: "recipe.white-sauce.skill::weingchicken-white-sauce-152"
- source_id: "weingchicken-white-sauce-152"
- title: "화이트소스 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/152"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "white-sauce"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "요리 초급 1 조건을 지정된 Recipe Source에서 확인했다."
- active: true
- is_active: true

### `recipe.white-sauce.ingredient.base-sauce.option.base-sauce.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.white-sauce.ingredient.base-sauce.option.base-sauce.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "white-sauce.ingredient.base-sauce.option.base-sauce"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "화이트소스 1회당 베이스 소스 1개를 교차확인했다."
- active: true
- is_active: true

### `recipe.white-sauce.ingredient.base-sauce.option.base-sauce.quantity::weingchicken-white-sauce-152`

- evidence_seed_key: "recipe.white-sauce.ingredient.base-sauce.option.base-sauce.quantity::weingchicken-white-sauce-152"
- source_id: "weingchicken-white-sauce-152"
- title: "화이트소스 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/152"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "white-sauce.ingredient.base-sauce.option.base-sauce"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "화이트소스 1회당 베이스 소스 1개를 교차확인했다."
- active: true
- is_active: true

### `recipe.white-sauce.ingredient.cooking-wine.option.cooking-wine.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.white-sauce.ingredient.cooking-wine.option.cooking-wine.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "white-sauce.ingredient.cooking-wine.option.cooking-wine"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "화이트소스 1회당 조리용 와인 2개를 교차확인했다."
- active: true
- is_active: true

### `recipe.white-sauce.ingredient.cooking-wine.option.cooking-wine.quantity::weingchicken-white-sauce-152`

- evidence_seed_key: "recipe.white-sauce.ingredient.cooking-wine.option.cooking-wine.quantity::weingchicken-white-sauce-152"
- source_id: "weingchicken-white-sauce-152"
- title: "화이트소스 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/152"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "white-sauce.ingredient.cooking-wine.option.cooking-wine"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "화이트소스 1회당 조리용 와인 2개를 교차확인했다."
- active: true
- is_active: true

### `recipe.white-sauce.ingredient.fruit.option.fruit.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.white-sauce.ingredient.fruit.option.fruit.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "white-sauce.ingredient.fruit.option.fruit"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "화이트소스 1회당 공식 current fruit group 1개를 교차확인했다. 전역 품질 환산은 적용하지 않는다."
- active: true
- is_active: true

### `recipe.white-sauce.ingredient.fruit.option.fruit.quantity::weingchicken-white-sauce-152`

- evidence_seed_key: "recipe.white-sauce.ingredient.fruit.option.fruit.quantity::weingchicken-white-sauce-152"
- source_id: "weingchicken-white-sauce-152"
- title: "화이트소스 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/152"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "white-sauce.ingredient.fruit.option.fruit"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "화이트소스 1회당 공식 current fruit group 1개를 교차확인했다. 전역 품질 환산은 적용하지 않는다."
- active: true
- is_active: true

### `recipe.white-sauce.ingredient.milk.option.milk.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.white-sauce.ingredient.milk.option.milk.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "white-sauce.ingredient.milk.option.milk"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "화이트소스 1회당 우유 1개를 교차확인했다."
- active: true
- is_active: true

### `recipe.white-sauce.ingredient.milk.option.milk.quantity::weingchicken-white-sauce-152`

- evidence_seed_key: "recipe.white-sauce.ingredient.milk.option.milk.quantity::weingchicken-white-sauce-152"
- source_id: "weingchicken-white-sauce-152"
- title: "화이트소스 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/152"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "white-sauce.ingredient.milk.option.milk"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "화이트소스 1회당 우유 1개를 교차확인했다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
