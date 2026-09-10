<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 대량가공

## Identity

- slug: "mass-processing"
- name_ko: "대량가공"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "대량가공은 가공 숙련도와 가공석을 사용하며 숙련도 2000에서 250회, 3000에서 315회 처리한다."
- purpose: "V1.6F 숙련도 3000 기반과 대량가공량 핵심 구간을 연결한다."

## Requirements

### `mass-processing.breakpoints`

- seed_key: "mass-processing.breakpoints"
- kind: "stat"
- requirement_level: "required"
- title: "숙련도별 대량가공량"
- description: "공식 숙련도 표의 핵심 구간이다."
- structured_value:

```json
{
  "breakpoints": [
    {
      "cycles": 10,
      "mastery": 0
    },
    {
      "cycles": 35,
      "mastery": 500
    },
    {
      "cycles": 250,
      "mastery": 2000
    },
    {
      "cycles": 290,
      "mastery": 2500
    },
    {
      "cycles": 300,
      "mastery": 2700
    },
    {
      "cycles": 305,
      "mastery": 2800
    },
    {
      "cycles": 310,
      "mastery": 2900
    },
    {
      "cycles": 315,
      "mastery": 3000
    }
  ],
  "unit": "cycles"
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

### `mass-processing.system`

- seed_key: "mass-processing.system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "processing-current-system"
- content_name_ko: "가공 현재 시스템"
- content_category: "life"
- note: "가공 시스템의 대량 처리"
- order_no: 1
- relative_path: "../contents/processing-current-system.md"
### `mass-processing.mastery`

- seed_key: "mass-processing.mastery"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-mastery-foundation"
- content_name_ko: "생활 숙련도 기반"
- content_category: "life"
- note: "최대 숙련도 3000 재사용"
- order_no: 2
- relative_path: "../contents/life-mastery-foundation.md"
### `mass-processing.stones`

- seed_key: "mass-processing.stones"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "processing-stones-and-clothes"
- content_name_ko: "가공석과 가공복"
- content_category: "life"
- note: "대량가공용 통합 가공석"
- order_no: 3
- relative_path: "../contents/processing-stones-and-clothes.md"
### `processing-stones-and-clothes.mass`

- seed_key: "processing-stones-and-clothes.mass"
- direction: "incoming"
- relation_type: "related"
- content_slug: "processing-stones-and-clothes"
- content_name_ko: "가공석과 가공복"
- content_category: "life"
- note: "가공석은 대량가공과 연결"
- order_no: 1
- relative_path: "../contents/processing-stones-and-clothes.md"
### `processing-current-system.mass`

- seed_key: "processing-current-system.mass"
- direction: "incoming"
- relation_type: "related"
- content_slug: "processing-current-system"
- content_name_ko: "가공 현재 시스템"
- content_category: "life"
- note: "대량가공"
- order_no: 2
- relative_path: "../contents/processing-current-system.md"
### `processing-onboarding-strategy.mass`

- seed_key: "processing-onboarding-strategy.mass"
- direction: "incoming"
- relation_type: "related"
- content_slug: "processing-onboarding-strategy"
- content_name_ko: "가공 입문 전략"
- content_category: "life"
- note: null
- order_no: 2
- relative_path: "../contents/processing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `mass-processing.summary::life-mastery-prione-2025-01-08`

- evidence_seed_key: "mass-processing.summary::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "mass-processing"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "가공 숙련도별 대량가공량"
- active: true
- is_active: true

### `mass-processing.requirement.breakpoints::life-mastery-prione-2025-01-08`

- evidence_seed_key: "mass-processing.requirement.breakpoints::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "mass-processing.breakpoints"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "0~3000 핵심 구간"
- active: true
- is_active: true

### Historical / inactive evidence

- None
