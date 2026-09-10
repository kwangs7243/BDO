<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 연금 숙련도 효과

## Identity

- slug: "alchemy-mastery-effects"
- name_ko: "연금 숙련도 효과"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "연금 숙련도는 최대 결과물, 일반·특수·희귀 추가 결과, 황실 납품 추가 이익에 각각 영향을 준다."
- purpose: "숙련도 3000 수치를 효과별로 분리한다."

## Requirements

### `alchemy-mastery-effects.max-result`

- seed_key: "alchemy-mastery-effects.max-result"
- kind: "stat"
- requirement_level: "required"
- title: "최대 결과물 획득 확률"
- description: "최대 결과물 획득 확률의 현재 규칙이다."
- structured_value:

```json
{
  "mastery": 3000,
  "percent": 62.5
}
```

### `alchemy-mastery-effects.normal-extra`

- seed_key: "alchemy-mastery-effects.normal-extra"
- kind: "stat"
- requirement_level: "required"
- title: "일반 결과물 추가 획득 확률"
- description: "일반 결과물 추가 획득 확률의 현재 규칙이다."
- structured_value:

```json
{
  "mastery": 3000,
  "percent": 3.83
}
```

### `alchemy-mastery-effects.special-extra`

- seed_key: "alchemy-mastery-effects.special-extra"
- kind: "stat"
- requirement_level: "required"
- title: "특수 결과물 추가 획득 확률"
- description: "특수 결과물 추가 획득 확률의 현재 규칙이다."
- structured_value:

```json
{
  "mastery": 3000,
  "percent": 2.98
}
```

### `alchemy-mastery-effects.rare-extra`

- seed_key: "alchemy-mastery-effects.rare-extra"
- kind: "stat"
- requirement_level: "required"
- title: "희귀 결과물 추가 획득 확률"
- description: "희귀 결과물 추가 획득 확률의 현재 규칙이다."
- structured_value:

```json
{
  "mastery": 3000,
  "percent": 0.36
}
```

### `alchemy-mastery-effects.imperial-profit`

- seed_key: "alchemy-mastery-effects.imperial-profit"
- kind: "stat"
- requirement_level: "required"
- title: "황실 연금 납품 추가 이익"
- description: "황실 연금 납품 추가 이익의 현재 규칙이다."
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

### `alchemy-mastery-effects.foundation`

- seed_key: "alchemy-mastery-effects.foundation"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-mastery-foundation"
- content_name_ko: "생활 숙련도 기반"
- content_category: "life"
- note: "생활 숙련도 공통 기반의 연금별 효과다."
- order_no: 1
- relative_path: "../contents/life-mastery-foundation.md"
### `alchemy-onboarding-strategy.mastery`

- seed_key: "alchemy-onboarding-strategy.mastery"
- direction: "incoming"
- relation_type: "related"
- content_slug: "alchemy-onboarding-strategy"
- content_name_ko: "연금 입문 전략"
- content_category: "life"
- note: null
- order_no: 2
- relative_path: "../contents/alchemy-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `alchemy-mastery-effects.claim.values::life-mastery-prione-2025-01-08`

- evidence_seed_key: "alchemy-mastery-effects.claim.values::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-mastery-effects"
- claim_key: "requirements:alchemy-mastery-effects"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
