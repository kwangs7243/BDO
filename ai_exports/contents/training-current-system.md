<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 조련 현재 시스템

## Identity

- slug: "training-current-system"
- name_ko: "조련 현재 시스템"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "조련은 야생마 포획·말 성장·교배와 교환·황실 납품·준마와 환상마 성장으로 이어지는 생활 분야다."
- purpose: "현재 조련 콘텐츠의 경계를 연결한다."

## Requirements

### `training-current-system.scope`

- seed_key: "training-current-system.scope"
- kind: "other"
- requirement_level: "required"
- title: "조련 범위"
- description: "조련 범위의 현재 규칙이다."
- structured_value:

```json
{
  "activities": [
    "wild_horse_capture",
    "mount_growth",
    "breeding",
    "exchange",
    "imperial_delivery",
    "courser",
    "dream_horse",
    "mythical_dream_horse"
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

### `training-onboarding-strategy.current-system`

- seed_key: "training-onboarding-strategy.current-system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "training-onboarding-strategy"
- content_name_ko: "조련 입문 운영 전략"
- content_category: "life"
- note: "조련 활동 범위와 현재 시스템"
- order_no: 1
- relative_path: "../contents/training-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `training-current-system.claim.summary::training-guide`

- evidence_seed_key: "training-current-system.claim.summary::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "training-current-system"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
