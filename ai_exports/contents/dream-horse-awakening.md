<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 환상마 각성

## Identity

- slug: "dream-horse-awakening"
- name_ko: "환상마 각성"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "30레벨 8세대 준마를 기술·기품·체력 합계 200%까지 훈련하고 크로그달로의 근원석 1개로 각성한다."
- purpose: "환상마 각성의 현재 훈련·재료·실패 규칙을 기록한다."

## Requirements

### `dream-horse-awakening.eligibility`

- seed_key: "dream-horse-awakening.eligibility"
- kind: "level"
- requirement_level: "required"
- title: "각성 대상"
- description: "각성 대상의 현재 규칙이다."
- structured_value:

```json
{
  "courser": true,
  "generation": 8,
  "level": 30
}
```

### `dream-horse-awakening.training`

- seed_key: "dream-horse-awakening.training"
- kind: "other"
- requirement_level: "required"
- title: "준마 훈련"
- description: "준마 훈련의 현재 규칙이다."
- structured_value:

```json
{
  "categories": [
    "skill",
    "elegance",
    "strength"
  ],
  "each_max_percent": 180,
  "per_item_over_100_percent": 0.5,
  "total_percent": 200
}
```

### `dream-horse-awakening.attempt`

- seed_key: "dream-horse-awakening.attempt"
- kind: "other"
- requirement_level: "required"
- title: "각성 시도"
- description: "각성 시도의 현재 규칙이다."
- structured_value:

```json
{
  "base_success_percent": null,
  "krogdalos_origin_stone": 1,
  "on_failure": {
    "success_chance_increases": true,
    "training_reset_without_cron": true,
    "with_cron_training_loss_percent": 50
  }
}
```

### `dream-horse-awakening.types`

- seed_key: "dream-horse-awakening.types"
- kind: "other"
- requirement_level: "required"
- title: "환상마 종류"
- description: "환상마 종류의 현재 규칙이다."
- structured_value:

```json
{
  "exclusive_location": false,
  "guide_locations": [
    "Gula",
    "Hyacinth",
    "Melrubi"
  ],
  "types": [
    "arduanatt",
    "dine",
    "doom"
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

### `dream-horse-awakening.materials`

- seed_key: "dream-horse-awakening.materials"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "dream-horse-material-routines"
- content_name_ko: "꿈결 환상마 재료 루틴"
- content_category: "life"
- note: "환상마 훈련 재료 루틴과 연결된다."
- order_no: 1
- relative_path: "../contents/dream-horse-material-routines.md"
### `courser-system.awakening`

- seed_key: "courser-system.awakening"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "courser-system"
- content_name_ko: "준마 시스템"
- content_category: "life"
- note: "30레벨 8세대 준마가 환상마 각성 대상이다."
- order_no: 1
- relative_path: "../contents/courser-system.md"
### `training-onboarding-strategy.dream-awakening`

- seed_key: "training-onboarding-strategy.dream-awakening"
- direction: "incoming"
- relation_type: "related"
- content_slug: "training-onboarding-strategy"
- content_name_ko: "조련 입문 운영 전략"
- content_category: "life"
- note: "환상마 각성 조건과 재료"
- order_no: 7
- relative_path: "../contents/training-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `dream-horse-awakening.claim.current::dream-horse-awakening-guide`

- evidence_seed_key: "dream-horse-awakening.claim.current::dream-horse-awakening-guide"
- source_id: "dream-horse-awakening-guide"
- title: "환상마 각성 확률 증가 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=350"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "dream-horse-awakening"
- claim_key: "requirements:dream-horse-awakening"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
