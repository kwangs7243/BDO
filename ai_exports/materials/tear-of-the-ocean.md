<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 심해의 눈물

## Identity

- key: "tear-of-the-ocean"
- name_ko: "심해의 눈물"
- unit: "개"

## Produced By Recipes

- None

## Explicit Recipe Usages

- None

## Ingredient Group Memberships

- None

## Ingredient Group Candidate Recipe Usages

- None

## Project Requirements

### `carrack-advance.material.tear-of-the-ocean`

- project_slug: "carrack-advance"
- project_name_ko: "에페리아 중범선 : 점진"
- project_material_seed_key: "carrack-advance.material.tear-of-the-ocean"
- stage_seed_key: "carrack-advance.stage.body-materials"
- stage_name: "점진 본체 재료 준비"
- required_quantity: 42.0
- order_no: 5
- notes: null
- source_entity_type: "content_requirement"
- source_entity_seed_key: "carrack-advance.requirement.body-materials"
- relative_path: "../projects/carrack-advance.md"

#### Scoped Acquisition Sources

### `carrack-advance.material.tear-of-the-ocean.source.young-sea-monster`

- seed_key: "carrack-advance.material.tear-of-the-ocean.source.young-sea-monster"
- content_slug: "oquilla-daily-young-sea-monster-hunter"
- content_name_ko: "[일일] 그믐달 어린 해왕류 사냥꾼"
- quantity_per_completion: 1.0
- notes: null
- order_no: 1
- relative_path: "../contents/oquilla-daily-young-sea-monster-hunter.md"
### `carrack-advance.material.tear-of-the-ocean.source.nineshark`

- seed_key: "carrack-advance.material.tear-of-the-ocean.source.nineshark"
- content_slug: "oquilla-weekly-nineshark-hunter"
- content_name_ko: "[주간] 그믐달 길드의 나인샤크 사냥꾼"
- quantity_per_completion: 2.0
- notes: null
- order_no: 2
- relative_path: "../contents/oquilla-weekly-nineshark-hunter.md"
### `carrack-advance.material.tear-of-the-ocean.source.crow-shop`

- seed_key: "carrack-advance.material.tear-of-the-ocean.source.crow-shop"
- content_slug: "crow-coin-material-shop"
- content_name_ko: "까마귀 주화 증축 재료 상점"
- quantity_per_completion: null
- notes: "교환 가격은 정본 Content에 있으며 1회 획득량으로 환산하지 않는다."
- order_no: 3
- relative_path: "../contents/crow-coin-material-shop.md"

## Semantics

- Material identity itself has no invented aggregate verification status.
- Explicit Material usage and IngredientGroup candidate usage are different.
- Group membership does not mean the material is mandatory.
- Group required_quantity belongs to the Recipe group option.
- Project acquisition sources are scoped to that ProjectMaterial requirement.
- No personal inventory is included.
- No market price or profitability is included.
