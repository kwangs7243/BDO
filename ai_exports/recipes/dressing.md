<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 드레싱

## Identity

- slug: "dressing"
- process_type: "cooking"
- summary: "요리 1회 시도 기준 드레싱 배합. 물 대안은 이 Recipe에서 두 재료 모두 1개다."
- verification_status: "verified"
- last_verified_at: "2026-09-11"

## Result

- material_key: "dressing"
- name_ko: "드레싱"
- unit: "개"

## Cooking Requirement

- required_skill_tier: "beginner"
- required_skill_level: 1

## Ingredient Slots

### 달걀

- seed_key: "dressing.ingredient.egg"
- order_no: 1
- notes: null

#### dressing.ingredient.egg.option.egg

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "egg"
- name_ko: "달걀"
- unit: "개"

### 올리브 오일

- seed_key: "dressing.ingredient.olive-oil"
- order_no: 2
- notes: null

#### dressing.ingredient.olive-oil.option.olive-oil

- target_type: "material"
- required_quantity: 1.0
- order_no: 1
- notes: null
- material_key: "olive-oil"
- name_ko: "올리브 오일"
- unit: "개"

### 물

- seed_key: "dressing.ingredient.water"
- order_no: 3
- notes: null

#### dressing.ingredient.water.option.water

- target_type: "ingredient_group"
- required_quantity: 1.0
- order_no: 1
- notes: "이 Recipe에서는 요리용 생수와 정제수 모두 1개로 확인되어 water group을 사용한다."
- group: "water"
- name_ko: "물"
- verification_status: "verified"
- last_verified_at: "2026-09-11"

Allowed current members:

- mineral-water / 요리용 생수 (개)
- purified-water / 정제수 (개)

### 소금

- seed_key: "dressing.ingredient.salt"
- order_no: 4
- notes: null

#### dressing.ingredient.salt.option.salt

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

- None

### Downstream Consumers

- None

## Evidence and Sources

### Current evidence

### `ingredient-group.water.membership::cooking-guide`

- evidence_seed_key: "ingredient-group.water.membership::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "ingredient_group"
- entity_id: "water"
- claim_key: "members"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "공식 current 요리 가이드의 대체품 목록 근거. Group membership은 global quantity conversion을 의미하지 않으며 Recipe마다 대체재 필요 수량이 다를 수 있다."
- active: true
- is_active: true

### `recipe.dressing.formula::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.dressing.formula::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "dressing"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "위잉치킨 제작노트와 인벤 Recipe DB에서 기본 배합을 교차확인했다. 공식 current 가이드는 exact formula 근거로 사용하지 않는다."
- active: true
- is_active: true

### `recipe.dressing.formula::weingchicken-dressing-56`

- evidence_seed_key: "recipe.dressing.formula::weingchicken-dressing-56"
- source_id: "weingchicken-dressing-56"
- title: "드레싱 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/56"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "dressing"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "위잉치킨 제작노트와 인벤 Recipe DB에서 기본 배합을 교차확인했다. 공식 current 가이드는 exact formula 근거로 사용하지 않는다."
- active: true
- is_active: true

### `recipe.dressing.attempt::cooking-guide`

- evidence_seed_key: "recipe.dressing.attempt::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "dressing"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "공식 current 요리 가이드의 1회분 투입 의미만 연결한다."
- active: true
- is_active: true

### `recipe.dressing.skill::weingchicken-dressing-56`

- evidence_seed_key: "recipe.dressing.skill::weingchicken-dressing-56"
- source_id: "weingchicken-dressing-56"
- title: "드레싱 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/56"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "dressing"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "요리 초급 1 조건을 지정된 Recipe Source에서 확인했다."
- active: true
- is_active: true

### `recipe.dressing.ingredient.egg.option.egg.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.dressing.ingredient.egg.option.egg.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "dressing.ingredient.egg.option.egg"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "드레싱 1회당 달걀 1개를 교차확인했다."
- active: true
- is_active: true

### `recipe.dressing.ingredient.egg.option.egg.quantity::weingchicken-dressing-56`

- evidence_seed_key: "recipe.dressing.ingredient.egg.option.egg.quantity::weingchicken-dressing-56"
- source_id: "weingchicken-dressing-56"
- title: "드레싱 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/56"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "dressing.ingredient.egg.option.egg"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "드레싱 1회당 달걀 1개를 교차확인했다."
- active: true
- is_active: true

### `recipe.dressing.ingredient.olive-oil.option.olive-oil.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.dressing.ingredient.olive-oil.option.olive-oil.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "dressing.ingredient.olive-oil.option.olive-oil"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "드레싱 1회당 올리브 오일 1개를 교차확인했다."
- active: true
- is_active: true

### `recipe.dressing.ingredient.olive-oil.option.olive-oil.quantity::weingchicken-dressing-56`

- evidence_seed_key: "recipe.dressing.ingredient.olive-oil.option.olive-oil.quantity::weingchicken-dressing-56"
- source_id: "weingchicken-dressing-56"
- title: "드레싱 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/56"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "dressing.ingredient.olive-oil.option.olive-oil"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "드레싱 1회당 올리브 오일 1개를 교차확인했다."
- active: true
- is_active: true

### `recipe.dressing.ingredient.salt.option.salt.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.dressing.ingredient.salt.option.salt.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "dressing.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "드레싱 1회당 소금 2개를 교차확인했다."
- active: true
- is_active: true

### `recipe.dressing.ingredient.salt.option.salt.quantity::weingchicken-dressing-56`

- evidence_seed_key: "recipe.dressing.ingredient.salt.option.salt.quantity::weingchicken-dressing-56"
- source_id: "weingchicken-dressing-56"
- title: "드레싱 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/56"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "dressing.ingredient.salt.option.salt"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "드레싱 1회당 소금 2개를 교차확인했다."
- active: true
- is_active: true

### `recipe.dressing.ingredient.water.option.water.quantity::weingchicken-dressing-56`

- evidence_seed_key: "recipe.dressing.ingredient.water.option.water.quantity::weingchicken-dressing-56"
- source_id: "weingchicken-dressing-56"
- title: "드레싱 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/56"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "dressing.ingredient.water.option.water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "드레싱에서는 요리용 생수와 정제수가 모두 1개임을 확인했다. 다른 Recipe의 물 수량으로 일반화하지 않는다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
