<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 조련 숙련도 효과

## Identity

- slug: "training-mastery-effects"
- name_ko: "조련 숙련도 효과"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "조련 숙련도 3000은 포획 확률·탑승물 경험치·높은 세대 획득 확률에 각각 기여한다."
- purpose: "숙련도 효과를 절대 성공률이 아닌 증가 효과로 구분한다."

## Requirements

### `training-mastery-effects.capture`

- seed_key: "training-mastery-effects.capture"
- kind: "stat"
- requirement_level: "required"
- title: "야생마 포획 확률 증가"
- description: "야생마 포획 확률 증가의 현재 규칙이다."
- structured_value:

```json
{
  "absolute_probability": false,
  "increase_percent": 43.75,
  "mastery": 3000
}
```

### `training-mastery-effects.mount-exp`

- seed_key: "training-mastery-effects.mount-exp"
- kind: "stat"
- requirement_level: "required"
- title: "탑승물 경험치 증가"
- description: "탑승물 경험치 증가의 현재 규칙이다."
- structured_value:

```json
{
  "increase_percent": 93.75,
  "mastery": 3000
}
```

### `training-mastery-effects.generation`

- seed_key: "training-mastery-effects.generation"
- kind: "stat"
- requirement_level: "required"
- title: "높은 세대 획득 확률 증가"
- description: "높은 세대 획득 확률 증가의 현재 규칙이다."
- structured_value:

```json
{
  "absolute_probability": false,
  "increase_percent": 13,
  "mastery": 3000
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

### `training-mastery-effects.foundation`

- seed_key: "training-mastery-effects.foundation"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-mastery-foundation"
- content_name_ko: "생활 숙련도 기반"
- content_category: "life"
- note: "생활 숙련도 공통 기반의 조련별 효과다."
- order_no: 1
- relative_path: "../contents/life-mastery-foundation.md"
### `training-onboarding-strategy.mastery`

- seed_key: "training-onboarding-strategy.mastery"
- direction: "incoming"
- relation_type: "related"
- content_slug: "training-onboarding-strategy"
- content_name_ko: "조련 입문 운영 전략"
- content_category: "life"
- note: "포획·탑승물 경험치·세대 확률의 숙련도 FACT"
- order_no: 2
- relative_path: "../contents/training-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `training-mastery-effects.claim.values::life-mastery-prione-2025-01-08`

- evidence_seed_key: "training-mastery-effects.claim.values::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "training-mastery-effects"
- claim_key: "requirements:training-mastery-effects"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
