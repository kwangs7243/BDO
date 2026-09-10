<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 일반 창고 수송

## Identity

- slug: "storage-transport"
- name_ko: "일반 창고 수송"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "발견한 창고 마을 사이에서 최대 40개 package를 비즉시 수송하며 거점 미연결 경로는 수송비가 3배다."
- purpose: "일반 수송의 package·비용·시간을 특송과 마그누스에서 분리한다."

## Requirements

### `storage-transport.route`

- seed_key: "storage-transport.route"
- kind: "other"
- requirement_level: "required"
- title: "수송 경로"
- description: "창고지기나 월드맵에서 발견한 창고 마을을 목적지로 선택한다."
- structured_value:

```json
{
  "access": [
    "storage_keeper",
    "world_map"
  ],
  "destination_requires_discovered_storage_town": true
}
```

### `storage-transport.packages`

- seed_key: "storage-transport.packages"
- kind: "other"
- requirement_level: "required"
- title: "포장 한도"
- description: "총 40 package 한도와 stack 처리를 기록한다."
- structured_value:

```json
{
  "max_packages": 40,
  "non_stackable_items_per_package": 1,
  "stackable_items_auto_split": true
}
```

### `storage-transport.network-time`

- seed_key: "storage-transport.network-time"
- kind: "other"
- requirement_level: "required"
- title: "연결 비용과 시간"
- description: "미연결도 가능하지만 비용이 늘고 즉시 이동하지 않는다."
- structured_value:

```json
{
  "disconnected_available": true,
  "disconnected_fee_multiplier": 3,
  "instant": false,
  "route_time_required": true,
  "transport_modes": [
    "wagon",
    "trade_ship"
  ]
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

### `storage-transport.nodes`

- seed_key: "storage-transport.nodes"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "node-network-current-system"
- content_name_ko: "거점 네트워크 현재 시스템"
- content_category: "life"
- note: "거점 연결 여부가 수송비에 영향을 준다."
- order_no: 1
- relative_path: "../contents/node-network-current-system.md"
### `storage-transport.special-delivery`

- seed_key: "storage-transport.special-delivery"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "worker-special-delivery"
- content_name_ko: "일꾼 특송"
- content_category: "life"
- note: "일반 town-to-town 수송은 생산 특송과 별개다."
- order_no: 2
- relative_path: "../contents/worker-special-delivery.md"
### `storage-transport.magnus`

- seed_key: "storage-transport.magnus"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "magnus-remote-storage"
- content_name_ko: "마그누스 원격 창고"
- content_category: "life"
- note: "시간이 드는 일반 수송과 마그누스 원격 입출고는 별개다."
- order_no: 3
- relative_path: "../contents/magnus-remote-storage.md"
### `magnus-remote-storage.transport`

- seed_key: "magnus-remote-storage.transport"
- direction: "incoming"
- relation_type: "alternative"
- content_slug: "magnus-remote-storage"
- content_name_ko: "마그누스 원격 창고"
- content_category: "life"
- note: "제한 품목을 제외한 원격 입출고는 일반 수송과 다른 접근 수단이다."
- order_no: 2
- relative_path: "../contents/magnus-remote-storage.md"
### `node-network-current-system.transport`

- seed_key: "node-network-current-system.transport"
- direction: "incoming"
- relation_type: "related"
- content_slug: "node-network-current-system"
- content_name_ko: "거점 네트워크 현재 시스템"
- content_category: "life"
- note: "연결 여부가 일반 창고 수송비에 영향을 준다."
- order_no: 2
- relative_path: "../contents/node-network-current-system.md"
### `worker-special-delivery.transport-distinction`

- seed_key: "worker-special-delivery.transport-distinction"
- direction: "incoming"
- relation_type: "related"
- content_slug: "worker-special-delivery"
- content_name_ko: "일꾼 특송"
- content_category: "life"
- note: "일반 창고 수송과는 별개다."
- order_no: 3
- relative_path: "../contents/worker-special-delivery.md"

## Evidence and Sources

### Current evidence

### `storage-transport.claim.current::node-guide`

- evidence_seed_key: "storage-transport.claim.current::node-guide"
- source_id: "node-guide"
- title: "거점"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=25"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "storage-transport"
- claim_key: "requirements:storage-transport"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `storage-transport.claim.current::storage-guide`

- evidence_seed_key: "storage-transport.claim.current::storage-guide"
- source_id: "storage-guide"
- title: "창고"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=39"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "storage-transport"
- claim_key: "requirements:storage-transport"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
