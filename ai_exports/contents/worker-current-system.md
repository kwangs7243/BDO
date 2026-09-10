<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 일꾼 현재 시스템

## Identity

- slug: "worker-current-system"
- name_ko: "일꾼 현재 시스템"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "일꾼은 작업 감독관에게 고용해 생산 거점·공방·텃밭에 보내며 작업 반복은 최대 50,000회지만 행동력이 실제 횟수를 제한한다."
- purpose: "일꾼 고용과 작업 범위를 현재 규칙으로 설명한다."

## Requirements

### `worker-current-system.hiring`

- seed_key: "worker-current-system.hiring"
- kind: "other"
- requirement_level: "required"
- title: "일꾼 확인과 고용"
- description: "일꾼을 한 번 확인하거나 다시 볼 때마다 기운 5를 소모한다."
- structured_value:

```json
{
  "continuous_view_supported": true,
  "energy_per_reroll": 5,
  "energy_per_view": 5
}
```

### `worker-current-system.remote-hiring`

- seed_key: "worker-current-system.remote-hiring"
- kind: "knowledge"
- requirement_level: "required"
- title: "다른 마을 일꾼 고용"
- description: "현재 위치와 다른 마을 일꾼도 해당 작업 감독관 지식이 있으면 고용할 수 있다."
- structured_value:

```json
{
  "active": true,
  "character_presence_in_town_required": false,
  "select_affiliated_town_first": true,
  "worker_supervisor_knowledge_required": true
}
```

### `worker-current-system.work-scope`

- seed_key: "worker-current-system.work-scope"
- kind: "other"
- requirement_level: "required"
- title: "작업 범위"
- description: "일꾼의 대표 작업과 반복 한도를 구분한다."
- structured_value:

```json
{
  "activities": [
    "production_node",
    "workshop_crafting",
    "farm_management"
  ],
  "actual_repeat_limited_by_stamina": true,
  "max_repeat": 50000
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

### `worker-current-system.production`

- seed_key: "worker-current-system.production"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "production-node-current-system"
- content_name_ko: "생산 거점 현재 시스템"
- content_category: "life"
- note: "생산 거점 작업에 일꾼을 보낸다."
- order_no: 1
- relative_path: "../contents/production-node-current-system.md"
### `worker-current-system.workshop`

- seed_key: "worker-current-system.workshop"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "workshop-crafting-logistics"
- content_name_ko: "공방 제작 물류"
- content_category: "life"
- note: "공방 제작에 일꾼을 사용한다."
- order_no: 2
- relative_path: "../contents/workshop-crafting-logistics.md"
### `worker-current-system.farming`

- seed_key: "worker-current-system.farming"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "farming-current-cycle"
- content_name_ko: "재배 현재 주기"
- content_category: "life"
- note: "텃밭 관리에도 일꾼을 사용할 수 있다."
- order_no: 3
- relative_path: "../contents/farming-current-cycle.md"
### `royal-workshop-current-system.workers`

- seed_key: "royal-workshop-current-system.workers"
- direction: "incoming"
- relation_type: "related"
- content_slug: "royal-workshop-current-system"
- content_name_ko: "왕실 공방 현재 시스템"
- content_category: "life"
- note: "육조거리 일꾼을 사용하지만 적용 능력치는 왕실 공방 전용 규칙을 따른다."
- order_no: 2
- relative_path: "../contents/royal-workshop-current-system.md"
### `worker-lodging.worker`

- seed_key: "worker-lodging.worker"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "worker-lodging"
- content_name_ko: "일꾼 숙소"
- content_category: "life"
- note: "숙소가 추가 일꾼 고용 수용량을 연다."
- order_no: 2
- relative_path: "../contents/worker-lodging.md"
### `workshop-crafting-logistics.worker`

- seed_key: "workshop-crafting-logistics.worker"
- direction: "incoming"
- relation_type: "related"
- content_slug: "workshop-crafting-logistics"
- content_name_ko: "공방 제작 물류"
- content_category: "life"
- note: "일꾼을 선택해 공방 제작을 수행한다."
- order_no: 2
- relative_path: "../contents/workshop-crafting-logistics.md"
### `farming-onboarding-strategy.workers`

- seed_key: "farming-onboarding-strategy.workers"
- direction: "incoming"
- relation_type: "related"
- content_slug: "farming-onboarding-strategy"
- content_name_ko: "재배 입문 전략"
- content_category: "life"
- note: null
- order_no: 6
- relative_path: "../contents/farming-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `worker-current-system.claim.current::worker-convenience-2025-01-22`

- evidence_seed_key: "worker-current-system.claim.current::worker-convenience-2025-01-22"
- source_id: "worker-convenience-2025-01-22"
- title: "1월 22일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13457"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-22"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-current-system"
- claim_key: "requirements:worker-current-system"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `worker-current-system.claim.current::worker-guide`

- evidence_seed_key: "worker-current-system.claim.current::worker-guide"
- source_id: "worker-guide"
- title: "일꾼"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=95"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-current-system"
- claim_key: "requirements:worker-current-system"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
