<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 튤립

## Identity

- key: "tulip"
- name_ko: "튤립"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

- None

## Ingredient Group Memberships

### `ingredient-group.flower.member.tulip`

- group_key: "flower"
- group_name_ko: "꽃"
- member_seed_key: "ingredient-group.flower.member.tulip"
- member_order_no: 2
- group_verification_status: "verified"
- group_last_verified_at: "2026-09-11"

#### Evidence and Sources

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

## Ingredient Group Candidate Recipe Usages

### `tea-with-fine-scent.ingredient.flower.option.flower`

- usage_semantics: "ingredient_group_candidate"
- group_key: "flower"
- group_name_ko: "꽃"
- group_verification_status: "verified"
- group_last_verified_at: "2026-09-11"
- recipe_slug: "tea-with-fine-scent"
- recipe_name_ko: "향이 좋은 차"
- process_type: "cooking"
- slot_seed_key: "tea-with-fine-scent.ingredient.flower"
- slot_label: "꽃"
- slot_order_no: 1
- option_seed_key: "tea-with-fine-scent.ingredient.flower.option.flower"
- option_order_no: 1
- group_required_quantity: 4.0
- is_alternative: false
- recipe_verification_status: "verified"
- recipe_last_verified_at: "2026-09-11"
- relative_path: "../recipes/tea-with-fine-scent.md"

## Project Requirements

- None

## Semantics

- Material identity itself has no invented aggregate verification status.
- Explicit Material usage and IngredientGroup candidate usage are different.
- Group membership does not mean the material is mandatory.
- Group required_quantity belongs to the Recipe group option.
- Project acquisition sources are scoped to that ProjectMaterial requirement.
- No personal inventory is included.
- No market price or profitability is included.
