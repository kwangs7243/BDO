<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 생산 거점 현재 시스템

## Identity

- slug: "production-node-current-system"
- name_ko: "생산 거점 현재 시스템"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "선행 탐험 거점과 생산 거점에 투자하고 연결된 일꾼을 보내 자원을 생산하며, 특송으로 결과 창고를 선택할 수 있다."
- purpose: "생산 거점의 해금·일꾼 연결·결과물 목적지 규칙을 설명한다."

## Requirements

### `production-node-current-system.unlock`

- seed_key: "production-node-current-system.unlock"
- kind: "other"
- requirement_level: "required"
- title: "생산 거점 해금"
- description: "선행 탐험 거점과 생산 거점 자체에 필요한 공헌도 투자가 완료되어야 한다."
- structured_value:

```json
{
  "parent_exploration_node_invested": true,
  "production_node_invested": true
}
```

### `production-node-current-system.worker-network`

- seed_key: "production-node-current-system.worker-network"
- kind: "other"
- requirement_level: "required"
- title: "일꾼 네트워크"
- description: "멀리 있는 다른 마을 일꾼은 연결된 거점 네트워크를 통해 작업할 수 있다."
- structured_value:

```json
{
  "connected_network_required": true,
  "remote_town_worker_allowed_when_connected": true
}
```

### `production-node-current-system.output-destination`

- seed_key: "production-node-current-system.output-destination"
- kind: "other"
- requirement_level: "required"
- title: "생산 결과물 목적지"
- description: "특송을 가진 일꾼은 작업 시작 시 결과물을 받을 마을 창고를 선택한다."
- structured_value:

```json
{
  "default_town_storage_only": false,
  "destination_town_storage_selectable": true,
  "special_delivery": true
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

### `production-node-current-system.special-delivery`

- seed_key: "production-node-current-system.special-delivery"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "worker-special-delivery"
- content_name_ko: "일꾼 특송"
- content_category: "life"
- note: "생산 결과 창고 선택은 일꾼 특송 기능이다."
- order_no: 1
- relative_path: "../contents/worker-special-delivery.md"
### `production-node-current-system.processing`

- seed_key: "production-node-current-system.processing"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "processing-current-system"
- content_name_ko: "가공 현재 시스템"
- content_category: "life"
- note: "생산 거점 재료는 가공 콘텐츠로 이어진다."
- order_no: 2
- relative_path: "../contents/processing-current-system.md"
### `production-node-current-system.cooking`

- seed_key: "production-node-current-system.cooking"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "cooking-current-system"
- content_name_ko: "요리 현재 시스템"
- content_category: "life"
- note: "생산 거점 재료는 요리 콘텐츠로 이어진다."
- order_no: 3
- relative_path: "../contents/cooking-current-system.md"
### `production-node-current-system.alchemy`

- seed_key: "production-node-current-system.alchemy"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "alchemy-current-system"
- content_name_ko: "연금 현재 시스템"
- content_category: "life"
- note: "생산 거점 재료는 연금 콘텐츠로 이어진다."
- order_no: 4
- relative_path: "../contents/alchemy-current-system.md"
### `node-network-current-system.production`

- seed_key: "node-network-current-system.production"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "node-network-current-system"
- content_name_ko: "거점 네트워크 현재 시스템"
- content_category: "life"
- note: "탐험 거점 연결은 생산 거점 작업의 기반이다."
- order_no: 1
- relative_path: "../contents/node-network-current-system.md"
### `production-node-2026-overhaul.current-system`

- seed_key: "production-node-2026-overhaul.current-system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "production-node-2026-overhaul"
- content_name_ko: "2026 생산 거점 개편"
- content_category: "life"
- note: "현재 생산 거점 시스템의 공헌도·산출물 표다."
- order_no: 1
- relative_path: "../contents/production-node-2026-overhaul.md"
### `worker-current-system.production`

- seed_key: "worker-current-system.production"
- direction: "incoming"
- relation_type: "related"
- content_slug: "worker-current-system"
- content_name_ko: "일꾼 현재 시스템"
- content_category: "life"
- note: "생산 거점 작업에 일꾼을 보낸다."
- order_no: 1
- relative_path: "../contents/worker-current-system.md"
### `worker-special-delivery.production`

- seed_key: "worker-special-delivery.production"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "worker-special-delivery"
- content_name_ko: "일꾼 특송"
- content_category: "life"
- note: "특송은 생산거점 결과물 물류다."
- order_no: 1
- relative_path: "../contents/worker-special-delivery.md"
### `alchemy-onboarding-strategy.production-nodes`

- seed_key: "alchemy-onboarding-strategy.production-nodes"
- direction: "incoming"
- relation_type: "related"
- content_slug: "alchemy-onboarding-strategy"
- content_name_ko: "연금 입문 전략"
- content_category: "life"
- note: null
- order_no: 8
- relative_path: "../contents/alchemy-onboarding-strategy.md"
### `cooking-onboarding-strategy.production-nodes`

- seed_key: "cooking-onboarding-strategy.production-nodes"
- direction: "incoming"
- relation_type: "related"
- content_slug: "cooking-onboarding-strategy"
- content_name_ko: "요리 입문 전략"
- content_category: "life"
- note: null
- order_no: 8
- relative_path: "../contents/cooking-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `production-node-current-system.claim.current::node-guide`

- evidence_seed_key: "production-node-current-system.claim.current::node-guide"
- source_id: "node-guide"
- title: "거점"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=25"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "production-node-current-system"
- claim_key: "requirements:production-node-current-system"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `production-node-current-system.claim.current::worker-convenience-2025-01-22`

- evidence_seed_key: "production-node-current-system.claim.current::worker-convenience-2025-01-22"
- source_id: "worker-convenience-2025-01-22"
- title: "1월 22일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13457"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-22"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "production-node-current-system"
- claim_key: "requirements:production-node-current-system"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `production-node-current-system.claim.current::worker-guide`

- evidence_seed_key: "production-node-current-system.claim.current::worker-guide"
- source_id: "worker-guide"
- title: "일꾼"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=95"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "production-node-current-system"
- claim_key: "requirements:production-node-current-system"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
