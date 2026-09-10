<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 요리 숙련도 효과

## Identity

- slug: "cooking-mastery-effects"
- name_ko: "요리 숙련도 효과"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "요리 숙련도는 대량 요리와 결과물 획득 확률, 황실 납품 추가 이익에 각각 영향을 준다."
- purpose: "숙련도 3000 기준 수치를 서로 다른 효과로 구분한다."

## Requirements

### `cooking-mastery-effects.mass-at-3000`

- seed_key: "cooking-mastery-effects.mass-at-3000"
- kind: "stat"
- requirement_level: "required"
- title: "숙련도 3000 대량 요리 발동 확률"
- description: "숙련도 3000 대량 요리 발동 확률의 현재 규칙이다."
- structured_value:

```json
{
  "mastery": 3000,
  "percent": 100
}
```

### `cooking-mastery-effects.max-base-result`

- seed_key: "cooking-mastery-effects.max-base-result"
- kind: "stat"
- requirement_level: "required"
- title: "일반 요리 최대 결과물 획득 확률"
- description: "일반 요리 최대 결과물 획득 확률의 현재 규칙이다."
- structured_value:

```json
{
  "mastery": 3000,
  "percent": 76.45
}
```

### `cooking-mastery-effects.special-acquisition`

- seed_key: "cooking-mastery-effects.special-acquisition"
- kind: "stat"
- requirement_level: "required"
- title: "상위 요리 획득 확률 증가"
- description: "상위 요리 획득 확률 증가의 현재 규칙이다."
- structured_value:

```json
{
  "mastery": 3000,
  "percent": 24.2
}
```

### `cooking-mastery-effects.max-special-result`

- seed_key: "cooking-mastery-effects.max-special-result"
- kind: "stat"
- requirement_level: "required"
- title: "상위 요리 최대 결과물 획득 확률"
- description: "상위 요리 최대 결과물 획득 확률의 현재 규칙이다."
- structured_value:

```json
{
  "mastery": 3000,
  "percent": 76.45
}
```

### `cooking-mastery-effects.imperial-profit`

- seed_key: "cooking-mastery-effects.imperial-profit"
- kind: "stat"
- requirement_level: "required"
- title: "황실 요리 납품 추가 이익"
- description: "황실 요리 납품 추가 이익의 현재 규칙이다."
- structured_value:

```json
{
  "interpretation": "additional_profit_effect",
  "mastery": 3000,
  "percent": 181.25
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

### `cooking-mastery-effects.foundation`

- seed_key: "cooking-mastery-effects.foundation"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-mastery-foundation"
- content_name_ko: "생활 숙련도 기반"
- content_category: "life"
- note: "생활 숙련도 공통 기반의 요리별 효과다."
- order_no: 1
- relative_path: "../contents/life-mastery-foundation.md"
### `cooking-mastery-effects.imperial`

- seed_key: "cooking-mastery-effects.imperial"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "imperial-crafting-delivery-daily"
- content_name_ko: "황실 제작 납품 일일"
- content_category: "life"
- note: "황실 요리 납품 추가 이익 효과와 연결된다."
- order_no: 2
- relative_path: "../contents/imperial-crafting-delivery-daily.md"
### `cooking-onboarding-strategy.mastery`

- seed_key: "cooking-onboarding-strategy.mastery"
- direction: "incoming"
- relation_type: "related"
- content_slug: "cooking-onboarding-strategy"
- content_name_ko: "요리 입문 전략"
- content_category: "life"
- note: null
- order_no: 2
- relative_path: "../contents/cooking-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `cooking-mastery-effects.claim.values::life-mastery-prione-2025-01-08`

- evidence_seed_key: "cooking-mastery-effects.claim.values::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "cooking-mastery-effects"
- claim_key: "requirements:cooking-mastery-effects"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### `cooking-mastery-effects.claim.summary::life-mastery-prione-2025-01-08`

- evidence_seed_key: "cooking-mastery-effects.claim.summary::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "cooking-mastery-effects"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
