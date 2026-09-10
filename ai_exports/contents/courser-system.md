<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 준마 시스템

## Identity

- slug: "courser-system"
- name_ko: "준마 시스템"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "8세대 말이 돌진·드리프트·전력 질주·순간 가속·측면 이동·연: 순간 가속·속: 측면 이동을 모두 익히면 준마가 된다."
- purpose: "8세대 준마 판정 기술과 환상마 도전 조건을 기록한다."

## Requirements

### `courser-system.tier8-skills`

- seed_key: "courser-system.tier8-skills"
- kind: "other"
- requirement_level: "required"
- title: "8세대 준마 필수 기술"
- description: "8세대 준마 필수 기술의 현재 규칙이다."
- structured_value:

```json
{
  "skills": [
    "charge",
    "drift",
    "sprint",
    "instant_accel",
    "sideways",
    "s_instant_accel",
    "s_sideways"
  ]
}
```

### `courser-system.dream-eligibility`

- seed_key: "courser-system.dream-eligibility"
- kind: "level"
- requirement_level: "required"
- title: "환상마 각성 도전 조건"
- description: "환상마 각성 도전 조건의 현재 규칙이다."
- structured_value:

```json
{
  "courser": true,
  "generation": 8,
  "level": 30
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

### `courser-system.awakening`

- seed_key: "courser-system.awakening"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "dream-horse-awakening"
- content_name_ko: "환상마 각성"
- content_category: "life"
- note: "30레벨 8세대 준마가 환상마 각성 대상이다."
- order_no: 1
- relative_path: "../contents/dream-horse-awakening.md"
### `training-onboarding-strategy.courser`

- seed_key: "training-onboarding-strategy.courser"
- direction: "incoming"
- relation_type: "related"
- content_slug: "training-onboarding-strategy"
- content_name_ko: "조련 입문 운영 전략"
- content_category: "life"
- note: "준마 판정과 상위 진행"
- order_no: 6
- relative_path: "../contents/training-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `courser-system.claim.current::training-guide`

- evidence_seed_key: "courser-system.claim.current::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "courser-system"
- claim_key: "requirements:courser-system"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
