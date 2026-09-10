<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 야생마 포획

## Identity

- slug: "wild-horse-capture"
- name_ko: "야생마 포획"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "현재 야생마는 주로 6~8세대로 등장하며 2026년 7월 주요 지역의 개체 수가 늘었다."
- purpose: "야생마 포획의 현재 세대 범위와 희귀 야생마 특성을 기록한다."

## Requirements

### `wild-horse-capture.generations`

- seed_key: "wild-horse-capture.generations"
- kind: "other"
- requirement_level: "required"
- title: "현재 주요 야생마 세대"
- description: "현재 주요 야생마 세대의 현재 규칙이다."
- structured_value:

```json
{
  "generations": [
    6,
    7,
    8
  ],
  "population_increased_at": "2026-07-15"
}
```

### `wild-horse-capture.rare-male`

- seed_key: "wild-horse-capture.rare-male"
- kind: "other"
- requirement_level: "required"
- title: "희귀 수컷 야생마"
- description: "희귀 수컷 야생마의 현재 규칙이다."
- structured_value:

```json
{
  "generations": [
    6,
    7,
    8
  ],
  "growth_speed_multiplier": 0.4,
  "value_multipliers": [
    10,
    7.5
  ]
}
```

### `wild-horse-capture.rare-female`

- seed_key: "wild-horse-capture.rare-female"
- kind: "other"
- requirement_level: "required"
- title: "희귀 암컷 야생마"
- description: "희귀 암컷 야생마의 현재 규칙이다."
- structured_value:

```json
{
  "generations": [
    7,
    8
  ],
  "growth_speed_multiplier": 0.4,
  "mating_count": 3,
  "value_multipliers": [
    10,
    7.5,
    5
  ]
}
```

### `wild-horse-capture.courser-specialized`

- seed_key: "wild-horse-capture.courser-specialized"
- kind: "other"
- requirement_level: "required"
- title: "8세대 준마 특화 야생마"
- description: "8세대 준마 특화 야생마의 현재 규칙이다."
- structured_value:

```json
{
  "initial_skill_one_of": [
    "sprint",
    "sideways"
  ],
  "some_growth_speed_multiplier": 0.5
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

### `training-onboarding-strategy.capture`

- seed_key: "training-onboarding-strategy.capture"
- direction: "incoming"
- relation_type: "related"
- content_slug: "training-onboarding-strategy"
- content_name_ko: "조련 입문 운영 전략"
- content_category: "life"
- note: "야생마 포획과 2026년 개체 수 변경"
- order_no: 3
- relative_path: "../contents/training-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `wild-horse-capture.claim.generations::blood-altar-challenge-2026-07-15`

- evidence_seed_key: "wild-horse-capture.claim.generations::blood-altar-challenge-2026-07-15"
- source_id: "blood-altar-challenge-2026-07-15"
- title: "7월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15878"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "wild-horse-capture"
- claim_key: "requirement:wild-horse-capture.generations"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### `wild-horse-capture.claim.rare::rare-wild-horses-2025-12-23`

- evidence_seed_key: "wild-horse-capture.claim.rare::rare-wild-horses-2025-12-23"
- source_id: "rare-wild-horses-2025-12-23"
- title: "12월 23일(화) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14989"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-23"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "wild-horse-capture"
- claim_key: "requirements:wild-horse-capture.rare"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
