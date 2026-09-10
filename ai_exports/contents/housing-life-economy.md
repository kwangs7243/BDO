<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 집과 생활 경제

## Identity

- slug: "housing-life-economy"
- name_ko: "집과 생활 경제"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "집은 공헌도로 구매하며 용도 미선택 시 기본 창고가 되고 주거지·숙소·공방 등으로 전환할 수 있다."
- purpose: "집 구매·용도 변경·주거지 규칙을 생활 경제 흐름에 연결한다."

## Requirements

### `housing-life-economy.purchase-use`

- seed_key: "housing-life-economy.purchase-use"
- kind: "other"
- requirement_level: "required"
- title: "집 구매와 용도"
- description: "공헌도로 구매하고 선택 가능한 대표 용도를 기록한다."
- structured_value:

```json
{
  "default_when_no_use_selected": "storage",
  "purchase_resource": "contribution",
  "uses": [
    "residence",
    "lodging",
    "storage",
    "refinery",
    "workshop",
    "improvement_workshop",
    "processing_house",
    "manufacturing_house",
    "horse_ranch"
  ]
}
```

### `housing-life-economy.conversion`

- seed_key: "housing-life-economy.conversion"
- kind: "other"
- requirement_level: "required"
- title: "용도 변경"
- description: "언제든 바꿀 수 있지만 시간·은화를 소모하며 변경 중 기능을 쓸 수 없다."
- structured_value:

```json
{
  "available_anytime": true,
  "function_unavailable_during_conversion": true,
  "silver_cost": true,
  "time_cost": true
}
```

### `housing-life-economy.residences`

- seed_key: "housing-life-economy.residences"
- kind: "other"
- requirement_level: "required"
- title: "주거지"
- description: "가문 전체 주거지 상한과 가구 이동을 기록한다."
- structured_value:

```json
{
  "family_max_residences": 5,
  "on_change_from_residence": {
    "installed_furniture_destination": "town_storage"
  }
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

### `housing-life-economy.contribution`

- seed_key: "housing-life-economy.contribution"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "contribution-economy-foundation"
- content_name_ko: "공헌도 경제 기반"
- content_category: "life"
- note: "집 구매에 공헌도를 사용한다."
- order_no: 1
- relative_path: "../contents/contribution-economy-foundation.md"
### `housing-life-economy.cooking`

- seed_key: "housing-life-economy.cooking"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "cooking-current-system"
- content_name_ko: "요리 현재 시스템"
- content_category: "life"
- note: "주거지는 요리 도구 설치 장소다."
- order_no: 2
- relative_path: "../contents/cooking-current-system.md"
### `housing-life-economy.alchemy`

- seed_key: "housing-life-economy.alchemy"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "alchemy-current-system"
- content_name_ko: "연금 현재 시스템"
- content_category: "life"
- note: "주거지는 연금술 도구 설치 장소다."
- order_no: 3
- relative_path: "../contents/alchemy-current-system.md"
### `storage-current-system.housing`

- seed_key: "storage-current-system.housing"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "storage-current-system"
- content_name_ko: "창고 현재 시스템"
- content_category: "life"
- note: "창고는 집의 기본·선택 용도다."
- order_no: 1
- relative_path: "../contents/storage-current-system.md"
### `worker-lodging.housing`

- seed_key: "worker-lodging.housing"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "worker-lodging"
- content_name_ko: "일꾼 숙소"
- content_category: "life"
- note: "숙소는 집의 용도 중 하나다."
- order_no: 1
- relative_path: "../contents/worker-lodging.md"
### `workshop-crafting-logistics.housing`

- seed_key: "workshop-crafting-logistics.housing"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "workshop-crafting-logistics"
- content_name_ko: "공방 제작 물류"
- content_category: "life"
- note: "공방은 집의 용도다."
- order_no: 1
- relative_path: "../contents/workshop-crafting-logistics.md"
### `contribution-economy-foundation.housing`

- seed_key: "contribution-economy-foundation.housing"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "contribution-economy-foundation"
- content_name_ko: "공헌도 경제 기반"
- content_category: "life"
- note: "공헌도로 집을 구매한다."
- order_no: 2
- relative_path: "../contents/contribution-economy-foundation.md"

## Evidence and Sources

### Current evidence

### `housing-life-economy.claim.current::contribution-guide`

- evidence_seed_key: "housing-life-economy.claim.current::contribution-guide"
- source_id: "contribution-guide"
- title: "공헌도"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=24"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "housing-life-economy"
- claim_key: "requirements:housing-life-economy"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `housing-life-economy.claim.current::house-guide`

- evidence_seed_key: "housing-life-economy.claim.current::house-guide"
- source_id: "house-guide"
- title: "집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=92"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "housing-life-economy"
- claim_key: "requirements:housing-life-economy"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
