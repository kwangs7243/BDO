<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 꿈결 환상마

## Identity

- slug: "mythical-dream-horse"
- name_ko: "꿈결 환상마"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "같은 종류의 30레벨 암수 환상마와 꿈을 부르는 향로 1개로 꿈결 아두아나트·디네·둠에 도전한다."
- purpose: "꿈결 환상마 도전 확률·실패 누적·향로 제작 규칙을 기록한다."

## Requirements

### `mythical-dream-horse.attempt`

- seed_key: "mythical-dream-horse.attempt"
- kind: "other"
- requirement_level: "required"
- title: "몽상 조건과 확률"
- description: "몽상 조건과 확률의 현재 규칙이다."
- structured_value:

```json
{
  "applies_to_other_types": true,
  "base_success_percent": 3,
  "failure_increment_percentage_points": 0.2,
  "failure_stack_scope": "family",
  "mythical_censer": 1,
  "on_failure": {
    "censer_consumed": true,
    "horses_retained": true
  },
  "on_success": {
    "gender": null,
    "market_registration": false
  },
  "parents": {
    "female_level": 30,
    "male_level": 30,
    "same_type": true
  }
}
```

### `mythical-dream-horse.types`

- seed_key: "mythical-dream-horse.types"
- kind: "other"
- requirement_level: "required"
- title: "꿈결 환상마 종류"
- description: "꿈결 환상마 종류의 현재 규칙이다."
- structured_value:

```json
{
  "types": [
    "mythical_arduanatt",
    "mythical_dine",
    "mythical_doom"
  ]
}
```

### `mythical-dream-horse.censer`

- seed_key: "mythical-dream-horse.censer"
- kind: "item"
- requirement_level: "required"
- title: "꿈을 부르는 향로 제작"
- description: "꿈을 부르는 향로 제작의 현재 규칙이다."
- structured_value:

```json
{
  "fire_horn": 10,
  "flame_powder": 10,
  "mythical_feather": 10,
  "mythical_powder": 10,
  "old_moon_censer": 1
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

### `mythical-dream-horse.materials`

- seed_key: "mythical-dream-horse.materials"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "dream-horse-material-routines"
- content_name_ko: "꿈결 환상마 재료 루틴"
- content_category: "life"
- note: "꿈을 부르는 향로 재료 루틴과 연결된다."
- order_no: 1
- relative_path: "../contents/dream-horse-material-routines.md"
### `training-onboarding-strategy.mythical`

- seed_key: "training-onboarding-strategy.mythical"
- direction: "incoming"
- relation_type: "related"
- content_slug: "training-onboarding-strategy"
- content_name_ko: "조련 입문 운영 전략"
- content_category: "life"
- note: "꿈결 환상마 progression"
- order_no: 8
- relative_path: "../contents/training-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `mythical-dream-horse.claim.current::mythical-horse-guide`

- evidence_seed_key: "mythical-dream-horse.claim.current::mythical-horse-guide"
- source_id: "mythical-horse-guide"
- title: "꿈결 환상마(몽상)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=355"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "mythical-dream-horse"
- claim_key: "requirements:mythical-dream-horse"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `mythical-dream-horse.claim.legacy-doom::mythical-horse-guide`

- evidence_seed_key: "mythical-dream-horse.claim.legacy-doom::mythical-horse-guide"
- source_id: "mythical-horse-guide"
- title: "꿈결 환상마(몽상)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=355"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "mythical-dream-horse"
- claim_key: "legacy:mythical-doom-unavailable"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: false
- is_active: false
