<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 연금석 성장 확률과 아그리스

## Identity

- slug: "alchemy-stone-growth"
- name_ko: "연금석 성장 확률과 아그리스"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "연마도 150%에서 단계별 성공 확률·아그리스의 정수·충만한 하늘의 정수 소모량이 정해져 있다."
- purpose: "현재 일반 연금석 성장표를 정확히 보존한다."

## Requirements

### `alchemy-stone-growth.table`

- seed_key: "alchemy-stone-growth.table"
- kind: "other"
- requirement_level: "required"
- title: "연마도 150% 성장표"
- description: "연마도 150% 성장표의 현재 규칙이다."
- structured_value:

```json
{
  "polish_percent": 150,
  "rows": [
    {
      "ancient_anvil": 2,
      "from": "imperfect",
      "full_sky_essence": 2,
      "success_percent": 55.055,
      "to": "sturdy"
    },
    {
      "ancient_anvil": 5,
      "from": "sturdy",
      "full_sky_essence": 3,
      "success_percent": 20.064,
      "to": "sharp"
    },
    {
      "ancient_anvil": 30,
      "from": "sharp",
      "full_sky_essence": 10,
      "success_percent": 3.3158,
      "to": "resplendent"
    },
    {
      "ancient_anvil": 80,
      "from": "resplendent",
      "full_sky_essence": 20,
      "success_percent": 1.2588,
      "to": "splendid"
    },
    {
      "ancient_anvil": 250,
      "from": "splendid",
      "full_sky_essence": 30,
      "success_percent": 0.4005,
      "to": "shining"
    }
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

### `alchemy-stone-growth.progression`

- seed_key: "alchemy-stone-growth.progression"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "alchemy-stone-current-progression"
- content_name_ko: "연금석 현재 성장 체계"
- content_category: "life"
- note: "현재 6단계 성장 체계의 수치표다."
- order_no: 1
- relative_path: "../contents/alchemy-stone-current-progression.md"

## Evidence and Sources

### Current evidence

### `alchemy-stone-growth.claim.table::dark-rift-reward-2026-01-14`

- evidence_seed_key: "alchemy-stone-growth.claim.table::dark-rift-reward-2026-01-14"
- source_id: "dark-rift-reward-2026-01-14"
- title: "1월 14일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15070"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-14"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-stone-growth"
- claim_key: "requirement:alchemy-stone-growth.table"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
