<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 말 황실 납품

## Identity

- slug: "horse-imperial-delivery"
- name_ko: "말 황실 납품"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "15레벨 이상 말을 황실 납품하면 은화·황금빛 보답 인장-[황실 조련]·망념의 꽃을 얻는다."
- purpose: "황실 말 납품 조건과 핵심 보상을 기록한다."

## Requirements

### `horse-imperial-delivery.level`

- seed_key: "horse-imperial-delivery.level"
- kind: "level"
- requirement_level: "required"
- title: "납품 가능 말 레벨"
- description: "납품 가능 말 레벨의 현재 규칙이다."
- structured_value:

```json
{
  "level": 15
}
```

### `horse-imperial-delivery.rewards`

- seed_key: "horse-imperial-delivery.rewards"
- kind: "item"
- requirement_level: "required"
- title: "핵심 보상"
- description: "핵심 보상의 현재 규칙이다."
- structured_value:

```json
{
  "rewards": [
    "silver",
    "golden_seal_imperial_training",
    "flower_of_oblivion"
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

### `horse-imperial-delivery.dream-materials`

- seed_key: "horse-imperial-delivery.dream-materials"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "dream-horse-material-routines"
- content_name_ko: "꿈결 환상마 재료 루틴"
- content_category: "life"
- note: "망념의 꽃은 환상마·꿈결 환상마 재료 흐름과 연결된다."
- order_no: 1
- relative_path: "../contents/dream-horse-material-routines.md"
### `training-onboarding-strategy.imperial-delivery`

- seed_key: "training-onboarding-strategy.imperial-delivery"
- direction: "incoming"
- relation_type: "related"
- content_slug: "training-onboarding-strategy"
- content_name_ko: "조련 입문 운영 전략"
- content_category: "life"
- note: "황실 말 납품 조건과 보상"
- order_no: 5
- relative_path: "../contents/training-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `horse-imperial-delivery.claim.current::training-guide`

- evidence_seed_key: "horse-imperial-delivery.claim.current::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "horse-imperial-delivery"
- claim_key: "requirements:horse-imperial-delivery"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
