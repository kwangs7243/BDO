<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 공방 제작 물류

## Identity

- slug: "workshop-crafting-logistics"
- name_ko: "공방 제작 물류"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "공방 제작은 선택한 일꾼 소속 마을 창고의 재료를 사용하며 타 마을 일꾼은 연결된 탐험 거점이 있어야 한다."
- purpose: "공방 재료 출처를 생산거점 특송과 분리한다."

## Requirements

### `workshop-crafting-logistics.categories`

- seed_key: "workshop-crafting-logistics.categories"
- kind: "other"
- requirement_level: "required"
- title: "대표 공방"
- description: "전체 레시피 DB 없이 대표 공방 범주만 기록한다."
- structured_value:

```json
{
  "categories": [
    "무기 단조",
    "갑주 단조",
    "목공예",
    "수공예",
    "도구",
    "대포",
    "가구",
    "세공",
    "마구",
    "가공소",
    "조선소",
    "마차 제작소"
  ],
  "full_recipe_database": false,
  "higher_stage_may_unlock_higher_grade_or_options": true
}
```

### `workshop-crafting-logistics.material-source`

- seed_key: "workshop-crafting-logistics.material-source"
- kind: "item"
- requirement_level: "required"
- title: "제작 재료 출처"
- description: "캐릭터 가방이 아니라 선택한 일꾼 소속 마을 창고에서 재료를 가져간다."
- structured_value:

```json
{
  "character_inventory_used": false,
  "external_worker_requires_connected_exploration_nodes": true,
  "insufficient_storage_space_can_block_start": true,
  "material_storage": "selected_worker_affiliated_town_storage"
}
```

### `workshop-crafting-logistics.distinction`

- seed_key: "workshop-crafting-logistics.distinction"
- kind: "other"
- requirement_level: "required"
- title: "특송과의 구분"
- description: "특송 목적지 선택이 공방 재료 창고를 바꾸지 않는다."
- structured_value:

```json
{
  "production_special_delivery_changes_material_source": false,
  "same_as_magnus_remote_storage": false,
  "same_as_storage_transport": false
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

- None

## Related Contents

### `workshop-crafting-logistics.housing`

- seed_key: "workshop-crafting-logistics.housing"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "housing-life-economy"
- content_name_ko: "집과 생활 경제"
- content_category: "life"
- note: "공방은 집의 용도다."
- order_no: 1
- relative_path: "../contents/housing-life-economy.md"
### `workshop-crafting-logistics.worker`

- seed_key: "workshop-crafting-logistics.worker"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "worker-current-system"
- content_name_ko: "일꾼 현재 시스템"
- content_category: "life"
- note: "일꾼을 선택해 공방 제작을 수행한다."
- order_no: 2
- relative_path: "../contents/worker-current-system.md"
### `workshop-crafting-logistics.special-delivery`

- seed_key: "workshop-crafting-logistics.special-delivery"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "worker-special-delivery"
- content_name_ko: "일꾼 특송"
- content_category: "life"
- note: "생산 특송과 구분되는 물류다."
- order_no: 3
- relative_path: "../contents/worker-special-delivery.md"
### `worker-current-system.workshop`

- seed_key: "worker-current-system.workshop"
- direction: "incoming"
- relation_type: "related"
- content_slug: "worker-current-system"
- content_name_ko: "일꾼 현재 시스템"
- content_category: "life"
- note: "공방 제작에 일꾼을 사용한다."
- order_no: 2
- relative_path: "../contents/worker-current-system.md"
### `worker-special-delivery.workshop-distinction`

- seed_key: "worker-special-delivery.workshop-distinction"
- direction: "incoming"
- relation_type: "related"
- content_slug: "worker-special-delivery"
- content_name_ko: "일꾼 특송"
- content_category: "life"
- note: "공방 재료 창고 규칙과는 별개다."
- order_no: 2
- relative_path: "../contents/worker-special-delivery.md"
### `processing-onboarding-strategy.workshop`

- seed_key: "processing-onboarding-strategy.workshop"
- direction: "incoming"
- relation_type: "related"
- content_slug: "processing-onboarding-strategy"
- content_name_ko: "가공 입문 전략"
- content_category: "life"
- note: null
- order_no: 7
- relative_path: "../contents/processing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `workshop-crafting-logistics.claim.current::crafting-guide`

- evidence_seed_key: "workshop-crafting-logistics.claim.current::crafting-guide"
- source_id: "crafting-guide"
- title: "제작"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=93"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "workshop-crafting-logistics"
- claim_key: "requirements:workshop-crafting-logistics"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `workshop-crafting-logistics.claim.current::work-management-guide`

- evidence_seed_key: "workshop-crafting-logistics.claim.current::work-management-guide"
- source_id: "work-management-guide"
- title: "작업 관리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=96"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "workshop-crafting-logistics"
- claim_key: "requirements:workshop-crafting-logistics"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `workshop-crafting-logistics.claim.current::worker-guide`

- evidence_seed_key: "workshop-crafting-logistics.claim.current::worker-guide"
- source_id: "worker-guide"
- title: "일꾼"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=95"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "workshop-crafting-logistics"
- claim_key: "requirements:workshop-crafting-logistics"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
