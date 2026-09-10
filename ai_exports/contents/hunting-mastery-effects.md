<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 수렵 숙련도 효과

## Identity

- slug: "hunting-mastery-effects"
- name_ko: "수렵 숙련도 효과"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "수렵 숙련도는 수렵 몬스터 도축 시 채집물 획득 수량 증가에 영향을 준다."
- purpose: "숙련도 2000과 3000의 수렵 채집물 증가율을 기록한다."

## Requirements

### `hunting-mastery-effects.yield`

- seed_key: "hunting-mastery-effects.yield"
- kind: "stat"
- requirement_level: "required"
- title: "수렵 채집물 획득 수량 증가"
- description: "수렵 채집물 획득 수량 증가의 현재 규칙이다."
- structured_value:

```json
{
  "rows": [
    {
      "increase_percent": 300,
      "mastery": 2000
    },
    {
      "increase_percent": 375,
      "mastery": 3000
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

### `hunting-mastery-effects.foundation`

- seed_key: "hunting-mastery-effects.foundation"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-mastery-foundation"
- content_name_ko: "생활 숙련도 기반"
- content_category: "life"
- note: "생활 숙련도 공통 기반의 수렵별 효과다."
- order_no: 1
- relative_path: "../contents/life-mastery-foundation.md"

## Evidence and Sources

### Current evidence

### `hunting-mastery-effects.claim.values::life-mastery-prione-2025-01-08`

- evidence_seed_key: "hunting-mastery-effects.claim.values::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "hunting-mastery-effects"
- claim_key: "requirement:hunting-mastery-effects.yield"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
