<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 왕실 공방 현재 시스템

## Identity

- slug: "royal-workshop-current-system"
- name_ko: "왕실 공방 현재 시스템"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "아침의 나라 서울의 왕실 공방은 공헌도와 육조거리 일꾼·창고를 사용하는 별도 생산·가공 시스템이다."
- purpose: "왕실 공방의 시작 조건, 자원, 생산소 구조와 현재 갱신 규칙을 일반 거점·공방 물류와 구분한다."

## Requirements

### `royal-workshop-current-system.access`

- seed_key: "royal-workshop-current-system.access"
- kind: "other"
- requirement_level: "required"
- title: "위치와 시작"
- description: "메뉴의 생활 항목에서 아침의 나라 서울 왕실 공방을 열고 공헌도 5를 투자해 시작한다."
- structured_value:

```json
{
  "contribution_points": 5,
  "location": "아침의 나라 서울",
  "menu_path": [
    "메뉴(ESC)",
    "생활",
    "왕실 공방"
  ]
}
```

### `royal-workshop-current-system.resources`

- seed_key: "royal-workshop-current-system.resources"
- kind: "other"
- requirement_level: "required"
- title: "사용 자원"
- description: "왕실 공방은 육조거리 소속 일꾼과 육조거리 창고를 사용한다."
- structured_value:

```json
{
  "storage_origin": "육조거리",
  "worker_origin": "육조거리"
}
```

### `royal-workshop-current-system.branches`

- seed_key: "royal-workshop-current-system.branches"
- kind: "other"
- requirement_level: "required"
- title: "거점 분기"
- description: "왕실 공방 거점은 생산 거점과 가공 거점으로 구분한다."
- structured_value:

```json
{
  "branches": [
    "production",
    "processing"
  ]
}
```

### `royal-workshop-current-system.production-workshops`

- seed_key: "royal-workshop-current-system.production-workshops"
- kind: "other"
- requirement_level: "required"
- title: "생산소 공방 구조"
- description: "생산 거점 하나에는 공방 5개가 있고 각 공방은 여러 후보 물품 중 하나를 선택한다."
- structured_value:

```json
{
  "selection_mode": "one_of_candidates_per_workshop",
  "workshops_per_production_node": 5
}
```

### `royal-workshop-current-system.free-refresh`

- seed_key: "royal-workshop-current-system.free-refresh"
- kind: "other"
- requirement_level: "required"
- title: "무료 물품 갱신"
- description: "하루 1회 무료 물품 갱신 횟수를 얻으며 무료 횟수는 최대 1회만 보유한다."
- structured_value:

```json
{
  "free_refresh_grants_per_day": 1,
  "max_free_refreshes_held": 1
}
```

### `royal-workshop-current-system.paid-refresh`

- seed_key: "royal-workshop-current-system.paid-refresh"
- kind: "other"
- requirement_level: "optional"
- title: "추가 물품 갱신"
- description: "추가 갱신 비용은 현재 10펄이며 가격 정책이 바뀔 수 있어 검증 출처와 함께 관리한다."
- structured_value:

```json
{
  "cost": 10,
  "currency": "pearl",
  "policy_may_change": true
}
```

### `royal-workshop-current-system.auto-refresh-current`

- seed_key: "royal-workshop-current-system.auto-refresh-current"
- kind: "other"
- requirement_level: "required"
- title: "현재 자동 갱신 시각"
- description: "왕실 공방 물품은 Asia/Seoul 기준 매일 00:00에 자동 갱신된다."
- structured_value:

```json
{
  "effective_from": "2024-11-20",
  "recurrence_type": "daily",
  "time_local": "00:00:00",
  "timezone": "Asia/Seoul"
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

### `royal-workshop-current-system.node-network`

- seed_key: "royal-workshop-current-system.node-network"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "node-network-current-system"
- content_name_ko: "거점 네트워크 현재 시스템"
- content_category: "life"
- note: "왕실 공방은 일반 거점 네트워크와 구분해 다루는 별도 생활 경제 분기다."
- order_no: 1
- relative_path: "../contents/node-network-current-system.md"
### `royal-workshop-current-system.workers`

- seed_key: "royal-workshop-current-system.workers"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "worker-current-system"
- content_name_ko: "일꾼 현재 시스템"
- content_category: "life"
- note: "육조거리 일꾼을 사용하지만 적용 능력치는 왕실 공방 전용 규칙을 따른다."
- order_no: 2
- relative_path: "../contents/worker-current-system.md"
### `royal-workshop-current-system.worker-effects`

- seed_key: "royal-workshop-current-system.worker-effects"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "royal-workshop-worker-effects"
- content_name_ko: "왕실 공방 일꾼 효과"
- content_category: "life"
- note: "왕실 공방에 적용되는 일꾼 특성과 기술은 별도 콘텐츠에서 정의한다."
- order_no: 3
- relative_path: "../contents/royal-workshop-worker-effects.md"
### `royal-workshop-worker-effects.system`

- seed_key: "royal-workshop-worker-effects.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "royal-workshop-worker-effects"
- content_name_ko: "왕실 공방 일꾼 효과"
- content_category: "life"
- note: "왕실 공방 전용 일꾼 적용 규칙이다."
- order_no: 1
- relative_path: "../contents/royal-workshop-worker-effects.md"

## Evidence and Sources

### Current evidence

### `royal-workshop-current-system.claim.system::royal-workshop-2024-11-20`

- evidence_seed_key: "royal-workshop-current-system.claim.system::royal-workshop-2024-11-20"
- source_id: "royal-workshop-2024-11-20"
- title: "11월 20일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13142"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-11-20"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "royal-workshop-current-system"
- claim_key: "requirements:royal-workshop-current-system"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `royal-workshop-current-system.claim.system::royal-workshop-history`

- evidence_seed_key: "royal-workshop-current-system.claim.system::royal-workshop-history"
- source_id: "royal-workshop-history"
- title: "왕실 공방"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13110"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "royal-workshop-current-system"
- claim_key: "requirements:royal-workshop-current-system"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `royal-workshop-current-system.claim.refresh-current::royal-workshop-2024-11-20`

- evidence_seed_key: "royal-workshop-current-system.claim.refresh-current::royal-workshop-2024-11-20"
- source_id: "royal-workshop-2024-11-20"
- title: "11월 20일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13142"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-11-20"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "royal-workshop-current-system.auto-refresh-current"
- claim_key: "requirement:royal-workshop-current-system.auto-refresh-current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `royal-workshop-current-system.claim.refresh-legacy-0100::royal-workshop-2024-11-20`

- evidence_seed_key: "royal-workshop-current-system.claim.refresh-legacy-0100::royal-workshop-2024-11-20"
- source_id: "royal-workshop-2024-11-20"
- title: "11월 20일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13142"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-11-20"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "royal-workshop-current-system"
- claim_key: "legacy:royal-workshop-auto-refresh-01:00"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false

### `royal-workshop-current-system.claim.refresh-legacy-0100::royal-workshop-history`

- evidence_seed_key: "royal-workshop-current-system.claim.refresh-legacy-0100::royal-workshop-history"
- source_id: "royal-workshop-history"
- title: "왕실 공방"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13110"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "royal-workshop-current-system"
- claim_key: "legacy:royal-workshop-auto-refresh-01:00"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
