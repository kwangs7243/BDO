<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 요리 성장 깜짝 의뢰

## Identity

- slug: "cooking-growth-surprise-quest"
- name_ko: "요리 성장 깜짝 의뢰"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "요리 중 확률로 발생하며 일일 횟수 제한은 없지만 같은 요리 분야 성장 깜짝 의뢰는 한 번에 하나만 진행한다."
- purpose: "현재 요리 성장 깜짝 의뢰의 동시 진행 규칙과 목표·보상을 구조화한다."

## Requirements

### `cooking-growth-surprise-quest.rules`

- seed_key: "cooking-growth-surprise-quest.rules"
- kind: "quest"
- requirement_level: "required"
- title: "발생 및 동시 진행 규칙"
- description: "발생 및 동시 진행 규칙의 현재 규칙이다."
- structured_value:

```json
{
  "daily_limit": null,
  "other_life_domains_can_coexist": true,
  "same_domain_concurrent_limit": 1,
  "trigger": "probabilistic_during_cooking"
}
```

### `cooking-growth-surprise-quest.tiers`

- seed_key: "cooking-growth-surprise-quest.tiers"
- kind: "quest"
- requirement_level: "required"
- title: "현재 목표와 보상"
- description: "현재 목표와 보상의 현재 규칙이다."
- structured_value:

```json
{
  "targets": [
    "beer",
    "grilled_bird_meat",
    "pickled_vegetables"
  ],
  "tiers": [
    {
      "craft_count": 5000,
      "reward_all": {
        "egg": 5000,
        "milk": 2000,
        "special_garlic": 2000,
        "special_hot_pepper": 2000,
        "special_onion": 2000,
        "special_pepper": 2000
      }
    },
    {
      "craft_count": 2000,
      "reward_all": {
        "egg": 2500,
        "high_quality_garlic": 1000,
        "high_quality_hot_pepper": 1000,
        "high_quality_onion": 1000,
        "high_quality_pepper": 1000,
        "milk": 1000
      }
    },
    {
      "choose_one": {
        "egg": 2500,
        "high_quality_garlic": 1000,
        "high_quality_hot_pepper": 1000,
        "high_quality_onion": 1000,
        "high_quality_pepper": 1000,
        "milk": 1000
      },
      "craft_count": 1000
    }
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

### `cooking-onboarding-strategy.growth`

- seed_key: "cooking-onboarding-strategy.growth"
- direction: "incoming"
- relation_type: "related"
- content_slug: "cooking-onboarding-strategy"
- content_name_ko: "요리 입문 전략"
- content_category: "life"
- note: null
- order_no: 6
- relative_path: "../contents/cooking-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `cooking-growth-surprise-quest.claim.tiers::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "cooking-growth-surprise-quest.claim.tiers::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "cooking-growth-surprise-quest"
- claim_key: "requirement:cooking-growth-surprise-quest.tiers"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### `cooking-growth-surprise-quest.claim.summary::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "cooking-growth-surprise-quest.claim.summary::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "cooking-growth-surprise-quest"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `cooking-growth-surprise-quest.claim.legacy-pickled-soldiers::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "cooking-growth-surprise-quest.claim.legacy-pickled-soldiers::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "cooking-growth-surprise-quest"
- claim_key: "legacy:surprise-cooking-for-heidel-soldiers-pickled-vegetables"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: false
- is_active: false
