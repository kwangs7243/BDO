<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 오믈렛

## Identity

- slug: "omelet"
- process_type: "cooking"
- summary: "요리 1회 시도 기준 오믈렛 배합. 기존 공식 current grain IngredientGroup을 재사용한다."
- verification_status: "verified"
- last_verified_at: "2026-09-11"

## Result

- material_key: "omelet"
- name_ko: "오믈렛"
- unit: "개"

## Recipe Requirement

- required_skill_tier: "apprentice"
- required_skill_level: 1

## Ingredient Slots

### 곡물

- seed_key: "omelet.ingredient.grain"
- order_no: 1
- notes: null

#### omelet.ingredient.grain.option.grain

- target_type: "ingredient_group"
- required_quantity: 5.0
- order_no: 1
- notes: null
- group: "grain"
- name_ko: "곡물"
- verification_status: "verified"
- last_verified_at: "2026-09-11"

Allowed current members:

- wheat / 밀 (개)
- barley / 보리 (개)
- potato / 감자 (개)
- sweet-potato / 고구마 (개)
- corn / 옥수수 (개)

### 올리브 오일

- seed_key: "omelet.ingredient.olive-oil"
- order_no: 2
- notes: null

#### omelet.ingredient.olive-oil.option.olive-oil

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "olive-oil"
- name_ko: "올리브 오일"
- unit: "개"

### 달걀

- seed_key: "omelet.ingredient.egg"
- order_no: 3
- notes: null

#### omelet.ingredient.egg.option.egg

- target_type: "material"
- required_quantity: 5.0
- order_no: 1
- notes: null
- material_key: "egg"
- name_ko: "달걀"
- unit: "개"

### 소금

- seed_key: "omelet.ingredient.salt"
- order_no: 4
- notes: null

#### omelet.ingredient.salt.option.salt

- target_type: "material"
- required_quantity: 2.0
- order_no: 1
- notes: null
- material_key: "salt"
- name_ko: "소금"
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

### `ingredient-group.grain.membership::cooking-guide`

- evidence_seed_key: "ingredient-group.grain.membership::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "ingredient_group"
- entity_id: "grain"
- claim_key: "members"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "2026-09-11 공식 current 요리 가이드의 대체품 목록을 재확인했다. 그룹 소속은 전역 수량 환산을 뜻하지 않는다."
- active: true
- is_active: true

### `recipe.omelet.formula::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.omelet.formula::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "omelet"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "위잉치킨 제작노트와 인벤 Recipe DB에서 기본 배합을 교차확인했다. 공식 current 가이드는 exact formula 근거로 사용하지 않는다."
- active: true
- is_active: true

### `recipe.omelet.formula::weingchicken-omelet-335`

- evidence_seed_key: "recipe.omelet.formula::weingchicken-omelet-335"
- source_id: "weingchicken-omelet-335"
- title: "오믈렛 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/335"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "omelet"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "위잉치킨 제작노트와 인벤 Recipe DB에서 기본 배합을 교차확인했다. 공식 current 가이드는 exact formula 근거로 사용하지 않는다."
- active: true
- is_active: true

### `recipe.omelet.attempt::cooking-guide`

- evidence_seed_key: "recipe.omelet.attempt::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "omelet"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "공식 current 요리 가이드의 1회분 투입 의미만 연결한다."
- active: true
- is_active: true

### `recipe.omelet.skill::weingchicken-omelet-335`

- evidence_seed_key: "recipe.omelet.skill::weingchicken-omelet-335"
- source_id: "weingchicken-omelet-335"
- title: "오믈렛 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/335"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "omelet"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "요리 견습 1 조건을 지정된 Recipe Source에서 확인했다."
- active: true
- is_active: true

### `recipe.omelet.ingredient.egg.option.egg.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.omelet.ingredient.egg.option.egg.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "omelet.ingredient.egg.option.egg"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "오믈렛 1회당 달걀 5개를 교차확인했다."
- active: true
- is_active: true

### `recipe.omelet.ingredient.egg.option.egg.quantity::weingchicken-omelet-335`

- evidence_seed_key: "recipe.omelet.ingredient.egg.option.egg.quantity::weingchicken-omelet-335"
- source_id: "weingchicken-omelet-335"
- title: "오믈렛 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/335"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "omelet.ingredient.egg.option.egg"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "오믈렛 1회당 달걀 5개를 교차확인했다."
- active: true
- is_active: true

### `recipe.omelet.ingredient.grain.option.grain.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.omelet.ingredient.grain.option.grain.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "omelet.ingredient.grain.option.grain"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "오믈렛 1회당 공식 current grain group 5개를 교차확인했다. 전역 품질 환산은 적용하지 않는다."
- active: true
- is_active: true

### `recipe.omelet.ingredient.grain.option.grain.quantity::weingchicken-omelet-335`

- evidence_seed_key: "recipe.omelet.ingredient.grain.option.grain.quantity::weingchicken-omelet-335"
- source_id: "weingchicken-omelet-335"
- title: "오믈렛 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/335"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "omelet.ingredient.grain.option.grain"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "오믈렛 1회당 공식 current grain group 5개를 교차확인했다. 전역 품질 환산은 적용하지 않는다."
- active: true
- is_active: true

### `recipe.omelet.ingredient.olive-oil.option.olive-oil.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.omelet.ingredient.olive-oil.option.olive-oil.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "omelet.ingredient.olive-oil.option.olive-oil"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "오믈렛 1회당 올리브 오일 2개를 교차확인했다."
- active: true
- is_active: true

### `recipe.omelet.ingredient.olive-oil.option.olive-oil.quantity::weingchicken-omelet-335`

- evidence_seed_key: "recipe.omelet.ingredient.olive-oil.option.olive-oil.quantity::weingchicken-omelet-335"
- source_id: "weingchicken-omelet-335"
- title: "오믈렛 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/335"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "omelet.ingredient.olive-oil.option.olive-oil"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "오믈렛 1회당 올리브 오일 2개를 교차확인했다."
- active: true
- is_active: true

### `recipe.omelet.ingredient.salt.option.salt.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.omelet.ingredient.salt.option.salt.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "omelet.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "오믈렛 1회당 소금 2개를 교차확인했다."
- active: true
- is_active: true

### `recipe.omelet.ingredient.salt.option.salt.quantity::weingchicken-omelet-335`

- evidence_seed_key: "recipe.omelet.ingredient.salt.option.salt.quantity::weingchicken-omelet-335"
- source_id: "weingchicken-omelet-335"
- title: "오믈렛 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/335"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "omelet.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "오믈렛 1회당 소금 2개를 교차확인했다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
