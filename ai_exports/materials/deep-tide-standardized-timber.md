<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 짙은 파도빛이 감도는 규격 각목

## Identity

- key: "deep-tide-standardized-timber"
- name_ko: "짙은 파도빛이 감도는 규격 각목"
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

### `carrack-advance.material.deep-tide-standardized-timber`

- project_slug: "carrack-advance"
- project_name_ko: "에페리아 중범선 : 점진"
- project_material_seed_key: "carrack-advance.material.deep-tide-standardized-timber"
- stage_seed_key: "carrack-advance.stage.body-materials"
- stage_name: "점진 본체 재료 준비"
- required_quantity: 144.0
- order_no: 2
- notes: null
- source_entity_type: "content_requirement"
- source_entity_seed_key: "carrack-advance.requirement.body-materials"
- relative_path: "../projects/carrack-advance.md"

#### Scoped Acquisition Sources

### `carrack-advance.material.deep-tide-standardized-timber.source.mutual-benefit`

- seed_key: "carrack-advance.material.deep-tide-standardized-timber.source.mutual-benefit"
- content_slug: "oquilla-daily-mutual-benefit"
- content_name_ko: "[일일] 너도 좋고, 나도 좋고"
- quantity_per_completion: 4.0
- notes: null
- order_no: 1
- relative_path: "../contents/oquilla-daily-mutual-benefit.md"
### `carrack-advance.material.deep-tide-standardized-timber.source.crow-shop`

- seed_key: "carrack-advance.material.deep-tide-standardized-timber.source.crow-shop"
- content_slug: "crow-coin-material-shop"
- content_name_ko: "까마귀 주화 증축 재료 상점"
- quantity_per_completion: null
- notes: "교환 가격은 정본 Content에 있으며 1회 획득량으로 환산하지 않는다."
- order_no: 2
- relative_path: "../contents/crow-coin-material-shop.md"

## Semantics

- Material identity itself has no invented aggregate verification status.
- Explicit Material usage and IngredientGroup candidate usage are different.
- Group membership does not mean the material is mandatory.
- Group required_quantity belongs to the Recipe group option.
- Project acquisition sources are scoped to that ProjectMaterial requirement.
- No personal inventory is included.
- No market price or profitability is included.
