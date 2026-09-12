<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 향이 좋은 차

## Identity

- slug: "tea-with-fine-scent"
- process_type: "cooking"
- summary: "요리 1회 시도 기준 향이 좋은 차 배합. 요리용 생수 7 또는 정제수 3을 별도 option으로 보존한다."
- verification_status: "verified"
- last_verified_at: "2026-09-11"

## Result

- material_key: "tea-with-fine-scent"
- name_ko: "향이 좋은 차"
- unit: "개"

## Recipe Requirement

- required_skill_tier: "apprentice"
- required_skill_level: 1

## Ingredient Slots

### 꽃

- seed_key: "tea-with-fine-scent.ingredient.flower"
- order_no: 1
- notes: null

#### tea-with-fine-scent.ingredient.flower.option.flower

- target_type: "ingredient_group"
- required_quantity: 4.0
- order_no: 1
- notes: null
- group: "flower"
- name_ko: "꽃"
- verification_status: "verified"
- last_verified_at: "2026-09-11"

Allowed current members:

- rose / 장미꽃 (개)
- tulip / 튤립 (개)
- sunflower / 해바라기 (개)

### 과일

- seed_key: "tea-with-fine-scent.ingredient.fruit"
- order_no: 2
- notes: null

#### tea-with-fine-scent.ingredient.fruit.option.fruit

- target_type: "ingredient_group"
- required_quantity: 4.0
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

### 물

- seed_key: "tea-with-fine-scent.ingredient.water"
- order_no: 3
- notes: null

#### tea-with-fine-scent.ingredient.water.option.mineral-water

- target_type: "material"
- required_quantity: 7.0
- order_no: 1
- notes: null
- material_key: "mineral-water"
- name_ko: "요리용 생수"
- unit: "개"

#### tea-with-fine-scent.ingredient.water.option.purified-water

- target_type: "material"
- required_quantity: 3.0
- order_no: 2
- notes: null
- material_key: "purified-water"
- name_ko: "정제수"
- unit: "개"

### 식용벌꿀

- seed_key: "tea-with-fine-scent.ingredient.edible-honey"
- order_no: 4
- notes: null

#### tea-with-fine-scent.ingredient.edible-honey.option.edible-honey

- target_type: "material"
- required_quantity: 3.0
- order_no: 1
- notes: null
- material_key: "edible-honey"
- name_ko: "식용벌꿀"
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

#### `tea-with-fine-scent -> sute-tea`

- producer_recipe_slug: "tea-with-fine-scent"
- producer_recipe_name_ko: "향이 좋은 차"
- producer_process_type: "cooking"
- producer_verification_status: "verified"
- consumer_recipe_slug: "sute-tea"
- consumer_recipe_name_ko: "수테차"
- consumer_process_type: "cooking"
- consumer_verification_status: "verified"
- material_key: "tea-with-fine-scent"
- material_name_ko: "향이 좋은 차"
- unit: "개"
- required_quantity: 2.0
- consumer_slot_seed_key: "sute-tea.ingredient.tea"
- consumer_option_seed_key: "sute-tea.ingredient.tea.option.tea-with-fine-scent"
- is_alternative: true
- relative_path: "../recipes/sute-tea.md"

## Evidence and Sources

### Current evidence

### `ingredient-group.flower.membership::cooking-guide`

- evidence_seed_key: "ingredient-group.flower.membership::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "ingredient_group"
- entity_id: "flower"
- claim_key: "members"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "공식 current 요리 가이드의 대체품 목록 근거. Group membership은 global quantity conversion을 의미하지 않으며 Recipe마다 대체재 필요 수량이 다를 수 있다."
- active: true
- is_active: true

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

### `recipe.tea-with-fine-scent.formula::codex-tea-with-fine-scent-9270`

- evidence_seed_key: "recipe.tea-with-fine-scent.formula::codex-tea-with-fine-scent-9270"
- source_id: "codex-tea-with-fine-scent-9270"
- title: "향이 좋은 차"
- url: "https://bdocodex.com/kr/item/9270/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "tea-with-fine-scent"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "기본 배합과 정제수 3 대안을 지정된 세 Recipe DB에서 검증했다. 물 option별 수량을 하나의 global group 수량으로 축약하지 않는다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.formula::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.tea-with-fine-scent.formula::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "tea-with-fine-scent"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "기본 배합과 정제수 3 대안을 지정된 세 Recipe DB에서 검증했다. 물 option별 수량을 하나의 global group 수량으로 축약하지 않는다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.formula::weingchicken-tea-with-fine-scent-218`

- evidence_seed_key: "recipe.tea-with-fine-scent.formula::weingchicken-tea-with-fine-scent-218"
- source_id: "weingchicken-tea-with-fine-scent-218"
- title: "향이 좋은 차 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/218"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "tea-with-fine-scent"
- claim_key: "ingredients"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "기본 배합과 정제수 3 대안을 지정된 세 Recipe DB에서 검증했다. 물 option별 수량을 하나의 global group 수량으로 축약하지 않는다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.attempt::cooking-guide`

- evidence_seed_key: "recipe.tea-with-fine-scent.attempt::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "tea-with-fine-scent"
- claim_key: "per_attempt"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "공식 current 요리 가이드의 1회분 투입 의미만 연결한다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.skill::codex-tea-with-fine-scent-9270`

- evidence_seed_key: "recipe.tea-with-fine-scent.skill::codex-tea-with-fine-scent-9270"
- source_id: "codex-tea-with-fine-scent-9270"
- title: "향이 좋은 차"
- url: "https://bdocodex.com/kr/item/9270/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "tea-with-fine-scent"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "요리 견습 1 조건을 두 지정 Recipe Source에서 확인했다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.skill::weingchicken-tea-with-fine-scent-218`

- evidence_seed_key: "recipe.tea-with-fine-scent.skill::weingchicken-tea-with-fine-scent-218"
- source_id: "weingchicken-tea-with-fine-scent-218"
- title: "향이 좋은 차 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/218"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe"
- entity_id: "tea-with-fine-scent"
- claim_key: "required_skill"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "요리 견습 1 조건을 두 지정 Recipe Source에서 확인했다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.ingredient.edible-honey.option.edible-honey.quantity::codex-tea-with-fine-scent-9270`

- evidence_seed_key: "recipe.tea-with-fine-scent.ingredient.edible-honey.option.edible-honey.quantity::codex-tea-with-fine-scent-9270"
- source_id: "codex-tea-with-fine-scent-9270"
- title: "향이 좋은 차"
- url: "https://bdocodex.com/kr/item/9270/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "tea-with-fine-scent.ingredient.edible-honey.option.edible-honey"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "향이 좋은 차 1회당 식용벌꿀 3개를 교차확인했다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.ingredient.edible-honey.option.edible-honey.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.tea-with-fine-scent.ingredient.edible-honey.option.edible-honey.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "tea-with-fine-scent.ingredient.edible-honey.option.edible-honey"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "향이 좋은 차 1회당 식용벌꿀 3개를 교차확인했다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.ingredient.edible-honey.option.edible-honey.quantity::weingchicken-tea-with-fine-scent-218`

- evidence_seed_key: "recipe.tea-with-fine-scent.ingredient.edible-honey.option.edible-honey.quantity::weingchicken-tea-with-fine-scent-218"
- source_id: "weingchicken-tea-with-fine-scent-218"
- title: "향이 좋은 차 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/218"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "tea-with-fine-scent.ingredient.edible-honey.option.edible-honey"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "향이 좋은 차 1회당 식용벌꿀 3개를 교차확인했다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.ingredient.flower.option.flower.quantity::codex-tea-with-fine-scent-9270`

- evidence_seed_key: "recipe.tea-with-fine-scent.ingredient.flower.option.flower.quantity::codex-tea-with-fine-scent-9270"
- source_id: "codex-tea-with-fine-scent-9270"
- title: "향이 좋은 차"
- url: "https://bdocodex.com/kr/item/9270/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "tea-with-fine-scent.ingredient.flower.option.flower"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "향이 좋은 차 1회당 공식 current flower group 4개를 교차확인했다. 전역 품질 환산은 적용하지 않는다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.ingredient.flower.option.flower.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.tea-with-fine-scent.ingredient.flower.option.flower.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "tea-with-fine-scent.ingredient.flower.option.flower"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "향이 좋은 차 1회당 공식 current flower group 4개를 교차확인했다. 전역 품질 환산은 적용하지 않는다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.ingredient.flower.option.flower.quantity::weingchicken-tea-with-fine-scent-218`

- evidence_seed_key: "recipe.tea-with-fine-scent.ingredient.flower.option.flower.quantity::weingchicken-tea-with-fine-scent-218"
- source_id: "weingchicken-tea-with-fine-scent-218"
- title: "향이 좋은 차 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/218"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "tea-with-fine-scent.ingredient.flower.option.flower"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "향이 좋은 차 1회당 공식 current flower group 4개를 교차확인했다. 전역 품질 환산은 적용하지 않는다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.ingredient.fruit.option.fruit.quantity::codex-tea-with-fine-scent-9270`

- evidence_seed_key: "recipe.tea-with-fine-scent.ingredient.fruit.option.fruit.quantity::codex-tea-with-fine-scent-9270"
- source_id: "codex-tea-with-fine-scent-9270"
- title: "향이 좋은 차"
- url: "https://bdocodex.com/kr/item/9270/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "tea-with-fine-scent.ingredient.fruit.option.fruit"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "향이 좋은 차 1회당 공식 current fruit group 4개를 교차확인했다. 전역 품질 환산은 적용하지 않는다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.ingredient.fruit.option.fruit.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.tea-with-fine-scent.ingredient.fruit.option.fruit.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "tea-with-fine-scent.ingredient.fruit.option.fruit"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "향이 좋은 차 1회당 공식 current fruit group 4개를 교차확인했다. 전역 품질 환산은 적용하지 않는다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.ingredient.fruit.option.fruit.quantity::weingchicken-tea-with-fine-scent-218`

- evidence_seed_key: "recipe.tea-with-fine-scent.ingredient.fruit.option.fruit.quantity::weingchicken-tea-with-fine-scent-218"
- source_id: "weingchicken-tea-with-fine-scent-218"
- title: "향이 좋은 차 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/218"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "tea-with-fine-scent.ingredient.fruit.option.fruit"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "향이 좋은 차 1회당 공식 current fruit group 4개를 교차확인했다. 전역 품질 환산은 적용하지 않는다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.ingredient.water.option.mineral-water.quantity::codex-tea-with-fine-scent-9270`

- evidence_seed_key: "recipe.tea-with-fine-scent.ingredient.water.option.mineral-water.quantity::codex-tea-with-fine-scent-9270"
- source_id: "codex-tea-with-fine-scent-9270"
- title: "향이 좋은 차"
- url: "https://bdocodex.com/kr/item/9270/"
- publisher: "BDO Codex"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "tea-with-fine-scent.ingredient.water.option.mineral-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "향이 좋은 차 1회당 요리용 생수 7개를 교차확인했다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.ingredient.water.option.mineral-water.quantity::inven-cooking-recipe-db`

- evidence_seed_key: "recipe.tea-with-fine-scent.ingredient.water.option.mineral-water.quantity::inven-cooking-recipe-db"
- source_id: "inven-cooking-recipe-db"
- title: "요리 · 연금 DB"
- url: "https://black.inven.co.kr/dataninfo/recipe/?nsrc=r"
- publisher: "검은사막 인벤"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "tea-with-fine-scent.ingredient.water.option.mineral-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "향이 좋은 차 1회당 요리용 생수 7개를 교차확인했다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.ingredient.water.option.mineral-water.quantity::weingchicken-tea-with-fine-scent-218`

- evidence_seed_key: "recipe.tea-with-fine-scent.ingredient.water.option.mineral-water.quantity::weingchicken-tea-with-fine-scent-218"
- source_id: "weingchicken-tea-with-fine-scent-218"
- title: "향이 좋은 차 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/218"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "tea-with-fine-scent.ingredient.water.option.mineral-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "향이 좋은 차 1회당 요리용 생수 7개를 교차확인했다."
- active: true
- is_active: true

### `recipe.tea-with-fine-scent.ingredient.water.option.purified-water.quantity::weingchicken-tea-with-fine-scent-218`

- evidence_seed_key: "recipe.tea-with-fine-scent.ingredient.water.option.purified-water.quantity::weingchicken-tea-with-fine-scent-218"
- source_id: "weingchicken-tea-with-fine-scent-218"
- title: "향이 좋은 차 - 검은사막 제작노트"
- url: "https://apps.weingchicken.com/bd/makings/218"
- publisher: "위잉치킨"
- source_type: "third_party_database"
- published_at: null
- retrieved_at: "2026-09-11T13:02:00+00:00"
- region: "KR"
- entity_type: "recipe_ingredient_option"
- entity_id: "tea-with-fine-scent.ingredient.water.option.purified-water"
- claim_key: "required_quantity"
- verification_status: "verified"
- last_verified_at: "2026-09-11"
- evidence_note: "향이 좋은 차 1회당 정제수 3개 대안은 전용 Source만 근거로 사용하며 7개로 일반화하지 않는다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
