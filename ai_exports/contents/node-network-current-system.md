<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 거점 네트워크 현재 시스템

## Identity

- slug: "node-network-current-system"
- name_ko: "거점 네트워크 현재 시스템"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "탐험 거점과 그 위성인 생산 거점을 공헌도로 연결하며, 미연결 상태에서도 수송·무역은 가능하지만 비용과 가격 손해가 있다."
- purpose: "거점 종류·연결 조건·원격 투자·미연결 불이익을 구분한다."

## Requirements

### `node-network-current-system.types`

- seed_key: "node-network-current-system.types"
- kind: "other"
- requirement_level: "required"
- title: "탐험 거점과 생산 거점"
- description: "두 거점 계층과 분류를 구분한다."
- structured_value:

```json
{
  "distinct": true,
  "exploration_types": [
    "중심 마을",
    "마을",
    "무역",
    "관문",
    "위험 지역",
    "연결로"
  ],
  "production_type_count": 7,
  "production_types": [
    "재배",
    "채집",
    "채광",
    "벌목",
    "생산",
    "발굴",
    "특산품"
  ]
}
```

### `node-network-current-system.investment`

- seed_key: "node-network-current-system.investment"
- kind: "knowledge"
- requirement_level: "required"
- title: "탐험 거점 투자 조건"
- description: "일반 탐험 거점은 지식과 투자된 인접 거점이 필요하다."
- structured_value:

```json
{
  "invested_adjacent_node_required": true,
  "region_knowledge_required": true,
  "some_major_towns_available_by_default": true
}
```

### `node-network-current-system.route-helper`

- seed_key: "node-network-current-system.route-helper"
- kind: "other"
- requirement_level: "required"
- title: "거점 바로 연결하기"
- description: "시작·도착 거점을 지정해 최소 공헌도 경로를 안내한다."
- structured_value:

```json
{
  "route_goal": "minimum_contribution",
  "select_start_and_destination": true
}
```

### `node-network-current-system.value-pack-remote`

- seed_key: "node-network-current-system.value-pack-remote"
- kind: "other"
- requirement_level: "required"
- title: "밸류 패키지 원격 투자"
- description: "밸류 패키지 적용 중 관리인 방문 없이 투자할 수 있으나 거점당 기운을 소모한다."
- structured_value:

```json
{
  "energy_per_node": 10,
  "free_remote_investment": false,
  "node_manager_visit_required": false,
  "value_pack_required": true
}
```

### `node-network-current-system.disconnected-penalties`

- seed_key: "node-network-current-system.disconnected-penalties"
- kind: "other"
- requirement_level: "required"
- title: "미연결 불이익"
- description: "미연결이어도 수송·무역은 가능하지만 불이익이 적용된다."
- structured_value:

```json
{
  "trade_sale_base_price_percent": 30,
  "transport_available": true,
  "transport_fee_multiplier": 3
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

### `node-network-current-system.production`

- seed_key: "node-network-current-system.production"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "production-node-current-system"
- content_name_ko: "생산 거점 현재 시스템"
- content_category: "life"
- note: "탐험 거점 연결은 생산 거점 작업의 기반이다."
- order_no: 1
- relative_path: "../contents/production-node-current-system.md"
### `node-network-current-system.transport`

- seed_key: "node-network-current-system.transport"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "storage-transport"
- content_name_ko: "일반 창고 수송"
- content_category: "life"
- note: "연결 여부가 일반 창고 수송비에 영향을 준다."
- order_no: 2
- relative_path: "../contents/storage-transport.md"
### `contribution-economy-foundation.nodes`

- seed_key: "contribution-economy-foundation.nodes"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "contribution-economy-foundation"
- content_name_ko: "공헌도 경제 기반"
- content_category: "life"
- note: "공헌도 투자가 거점 네트워크를 연다."
- order_no: 1
- relative_path: "../contents/contribution-economy-foundation.md"
### `royal-workshop-current-system.node-network`

- seed_key: "royal-workshop-current-system.node-network"
- direction: "incoming"
- relation_type: "related"
- content_slug: "royal-workshop-current-system"
- content_name_ko: "왕실 공방 현재 시스템"
- content_category: "life"
- note: "왕실 공방은 일반 거점 네트워크와 구분해 다루는 별도 생활 경제 분기다."
- order_no: 1
- relative_path: "../contents/royal-workshop-current-system.md"
### `storage-transport.nodes`

- seed_key: "storage-transport.nodes"
- direction: "incoming"
- relation_type: "related"
- content_slug: "storage-transport"
- content_name_ko: "일반 창고 수송"
- content_category: "life"
- note: "거점 연결 여부가 수송비에 영향을 준다."
- order_no: 1
- relative_path: "../contents/storage-transport.md"

## Evidence and Sources

### Current evidence

### `node-network-current-system.claim.current::contribution-guide`

- evidence_seed_key: "node-network-current-system.claim.current::contribution-guide"
- source_id: "contribution-guide"
- title: "공헌도"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=24"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "node-network-current-system"
- claim_key: "requirements:node-network-current-system"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `node-network-current-system.claim.current::node-guide`

- evidence_seed_key: "node-network-current-system.claim.current::node-guide"
- source_id: "node-guide"
- title: "거점"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=25"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "node-network-current-system"
- claim_key: "requirements:node-network-current-system"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
