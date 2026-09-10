<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 연금 성장 깜짝 의뢰

## Identity

- slug: "alchemy-growth-surprise-quest"
- name_ko: "연금 성장 깜짝 의뢰"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "연금 중 확률로 발생하며 일일 횟수 제한은 없지만 같은 연금 분야 성장 깜짝 의뢰는 한 번에 하나만 진행한다."
- purpose: "현재 연금 성장 깜짝 의뢰의 규칙과 목표·보상을 구조화한다."

## Requirements

### `alchemy-growth-surprise-quest.rules`

- seed_key: "alchemy-growth-surprise-quest.rules"
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
  "trigger": "probabilistic_during_alchemy"
}
```

### `alchemy-growth-surprise-quest.tiers`

- seed_key: "alchemy-growth-surprise-quest.tiers"
- kind: "quest"
- requirement_level: "required"
- title: "현재 목표와 보상"
- description: "현재 목표와 보상의 현재 규칙이다."
- structured_value:

```json
{
  "targets": [
    "clear_liquid_reagent",
    "pure_powder_reagent",
    "clowns_blood"
  ],
  "tiers": [
    {
      "craft_count": 500,
      "reward_all": {
        "bloody_tree_knot": 2000,
        "monks_branch": 2000,
        "natures_trace": 500,
        "old_tree_bark": 2000,
        "red_tree_lump": 2000,
        "spirit_leaf": 2000
      }
    },
    {
      "base_reward": {
        "natures_trace": 250
      },
      "choose_one": {
        "sap_group_a": {
          "ash_sap": 500,
          "fir_sap": 500,
          "maple_sap": 500,
          "ring_tree_sap": 500,
          "thorn_sap": 500
        },
        "sap_group_b": {
          "birch_sap": 500,
          "cedar_sap": 500,
          "moss_tree_sap": 500,
          "pine_sap": 500
        }
      },
      "craft_count": 100
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

### `alchemy-onboarding-strategy.growth`

- seed_key: "alchemy-onboarding-strategy.growth"
- direction: "incoming"
- relation_type: "related"
- content_slug: "alchemy-onboarding-strategy"
- content_name_ko: "연금 입문 전략"
- content_category: "life"
- note: null
- order_no: 5
- relative_path: "../contents/alchemy-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `alchemy-growth-surprise-quest.claim.current::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "alchemy-growth-surprise-quest.claim.current::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-growth-surprise-quest"
- claim_key: "requirements:alchemy-growth-surprise-quest"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `alchemy-growth-surprise-quest.claim.legacy-dalishain::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "alchemy-growth-surprise-quest.claim.legacy-dalishain::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-growth-surprise-quest"
- claim_key: "legacy:dalishain-simple-test"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: false
- is_active: false
