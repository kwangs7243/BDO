<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 수렵 성장 깜짝 의뢰

## Identity

- slug: "hunting-growth-surprise-quest"
- name_ko: "수렵 성장 깜짝 의뢰"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "지정 수렵지에서 확률로 발생하며 일일 제한 없이 같은 수렵 성장 깜짝 의뢰는 하나만 진행한다."
- purpose: "현재 수렵 성장 깜짝 의뢰 대상·보상 범주와 사냥꾼의 새벽 효과를 기록한다."

## Requirements

### `hunting-growth-surprise-quest.rules`

- seed_key: "hunting-growth-surprise-quest.rules"
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
  "trigger": "probabilistic_during_hunting"
}
```

### `hunting-growth-surprise-quest.targets`

- seed_key: "hunting-growth-surprise-quest.targets"
- kind: "quest"
- requirement_level: "required"
- title: "대상과 대표 보상"
- description: "대상과 대표 보상의 현재 규칙이다."
- structured_value:

```json
{
  "multiple_objective_tiers": true,
  "reward_categories": [
    "hunters_dawn",
    "hunters_token",
    "life_materials",
    "black_crystal",
    "condensed_magical_black_crystal"
  ],
  "targets": [
    "feather_wolf_pack",
    "giant_lion_pack",
    "narcion",
    "mountain_of_eternal_winter"
  ]
}
```

### `hunting-growth-surprise-quest.dawn`

- seed_key: "hunting-growth-surprise-quest.dawn"
- kind: "stat"
- requirement_level: "required"
- title: "사냥꾼의 새벽"
- description: "사냥꾼의 새벽의 현재 규칙이다."
- structured_value:

```json
{
  "attack_speed_potential": 2,
  "automatic_on_acquisition": true,
  "critical_hit_potential": 2,
  "duration_minutes": 30,
  "hunting_exp_percent": 15,
  "movement_speed_potential": 2
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

- None

## Evidence and Sources

### Current evidence

### `hunting-growth-surprise-quest.claim.current::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "hunting-growth-surprise-quest.claim.current::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "hunting-growth-surprise-quest"
- claim_key: "requirements:hunting-growth-surprise-quest"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `hunting-growth-surprise-quest.claim.legacy-quests::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "hunting-growth-surprise-quest.claim.legacy-quests::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "hunting-growth-surprise-quest"
- claim_key: "legacy:four-old-hunting-surprise-quests"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: false
- is_active: false
