<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 일꾼 숙소

## Identity

- slug: "worker-lodging"
- name_ko: "일꾼 숙소"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "각 마을·영지는 숙소 없이 일꾼 1명을 고용할 수 있고 추가 숙소가 일꾼 수용량을 늘린다."
- purpose: "일꾼 기본 수용량과 숙소 확장을 과도한 집별 일반화 없이 설명한다."

## Requirements

### `worker-lodging.capacity`

- seed_key: "worker-lodging.capacity"
- kind: "other"
- requirement_level: "required"
- title: "일꾼 수용량"
- description: "기본 한 명과 추가 숙소 효과를 기록한다."
- structured_value:

```json
{
  "additional_lodging_increases_capacity": true,
  "base_workers_without_lodging_per_town_or_territory": 1,
  "exact_capacity_depends_on_house": true
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

### `worker-lodging.housing`

- seed_key: "worker-lodging.housing"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "housing-life-economy"
- content_name_ko: "집과 생활 경제"
- content_category: "life"
- note: "숙소는 집의 용도 중 하나다."
- order_no: 1
- relative_path: "../contents/housing-life-economy.md"
### `worker-lodging.worker`

- seed_key: "worker-lodging.worker"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "worker-current-system"
- content_name_ko: "일꾼 현재 시스템"
- content_category: "life"
- note: "숙소가 추가 일꾼 고용 수용량을 연다."
- order_no: 2
- relative_path: "../contents/worker-current-system.md"

## Evidence and Sources

### Current evidence

### `worker-lodging.claim.current::house-guide`

- evidence_seed_key: "worker-lodging.claim.current::house-guide"
- source_id: "house-guide"
- title: "집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=92"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-lodging"
- claim_key: "requirement:worker-lodging.capacity"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `worker-lodging.claim.current::worker-guide`

- evidence_seed_key: "worker-lodging.claim.current::worker-guide"
- source_id: "worker-guide"
- title: "일꾼"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=95"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-lodging"
- claim_key: "requirement:worker-lodging.capacity"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
