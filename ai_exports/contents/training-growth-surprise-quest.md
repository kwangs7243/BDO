<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 조련 성장 깜짝 의뢰

## Identity

- slug: "training-growth-surprise-quest"
- name_ko: "조련 성장 깜짝 의뢰"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "야생마 포획 또는 6세대 이상 말·환상마·황실 보마 납품 때 확률로 발생하며 같은 조련 성장 의뢰는 하나만 진행한다."
- purpose: "조련 성장 깜짝 의뢰의 현재 발생 조건과 선택 보상을 기록한다."

## Requirements

### `training-growth-surprise-quest.rules`

- seed_key: "training-growth-surprise-quest.rules"
- kind: "quest"
- requirement_level: "required"
- title: "발생 및 동시 진행 규칙"
- description: "발생 및 동시 진행 규칙의 현재 규칙이다."
- structured_value:

```json
{
  "daily_limit": null,
  "other_life_domains_can_coexist": true,
  "probabilistic": true,
  "same_domain_concurrent_limit": 1,
  "trigger_one_of": [
    "capture_one_wild_horse",
    "imperial_delivery_generation_6_or_higher",
    "imperial_delivery_dream_horse",
    "imperial_delivery_imperial_steed"
  ]
}
```

### `training-growth-surprise-quest.rewards`

- seed_key: "training-growth-surprise-quest.rewards"
- kind: "quest"
- requirement_level: "required"
- title: "보상"
- description: "보상의 현재 규칙이다."
- structured_value:

```json
{
  "choose_one": {
    "fierce_sprint_elixir": 1,
    "stonetail_wind_meal": 1
  },
  "talk_to_black_spirit": {
    "elixir_of_training": 1
  }
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

### `training-onboarding-strategy.growth-quest`

- seed_key: "training-onboarding-strategy.growth-quest"
- direction: "incoming"
- relation_type: "related"
- content_slug: "training-onboarding-strategy"
- content_name_ko: "조련 입문 운영 전략"
- content_category: "life"
- note: "조련 성장 깜짝 의뢰"
- order_no: 9
- relative_path: "../contents/training-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `training-growth-surprise-quest.claim.current::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "training-growth-surprise-quest.claim.current::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "training-growth-surprise-quest"
- claim_key: "requirements:training-growth-surprise-quest"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
