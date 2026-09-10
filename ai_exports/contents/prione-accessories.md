<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 프리오네 액세서리

## Identity

- slug: "prione-accessories"
- name_ko: "프리오네 액세서리"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "강화된 마노스 액세서리를 교환해 획득하며, 고정 확률 강화 실패 시 파괴되지 않고 단계가 하락한다."
- purpose: "프리오네의 교환, 강화 규칙, 단계별 재료와 능력치를 정확히 구조화한다."

## Requirements

### `prione-accessories.exchange`

- seed_key: "prione-accessories.exchange"
- kind: "quest"
- requirement_level: "required"
- title: "마노스 교환"
- description: "가문당 1회 선행 의뢰 후 리아나의 반복 교환 의뢰에는 일일 제한이 없다."
- structured_value:

```json
{
  "exchanges": [
    {
      "input": "TRI Manos",
      "output": "+0 Prione"
    },
    {
      "input": "TET Manos",
      "output": "TRI Prione"
    },
    {
      "input": "PEN Manos",
      "output": "VIII Prione"
    }
  ],
  "npc": "리아나",
  "prerequisite_family_limit": 1,
  "repeated_exchange_daily_limit": null
}
```

### `prione-accessories.enhancement-rules`

- seed_key: "prione-accessories.enhancement-rules"
- kind: "gear"
- requirement_level: "required"
- title: "강화 규칙"
- description: "고정 확률을 사용하며 실패 시 파괴되지 않고 단계가 하락한다. 크론석은 단계 하락을 막고 강화 스택은 적용·소모되지 않는다."
- structured_value:

```json
{
  "agris_essence_scope": "per_slot",
  "cron_prevents_downgrade": true,
  "destroyed_on_failure": false,
  "downgrade_on_failure": true,
  "failstack_applied": false,
  "failstack_consumed_on_success": false,
  "fixed_success_probability": true,
  "material": "응축된 마력의 검은 결정",
  "max_durability_loss_on_failure": 10
}
```

### `prione-accessories.enhancement-table`

- seed_key: "prione-accessories.enhancement-table"
- kind: "gear"
- requirement_level: "required"
- title: "단계별 강화표"
- description: "공식 단계별 결정·확률·크론석·아그리스의 정수 수치다."
- structured_value:

```json
{
  "rows": [
    {
      "agris": 6,
      "cron": 0,
      "crystals": 15,
      "from": "+0",
      "success_percent": 25,
      "to": "I"
    },
    {
      "agris": 8,
      "cron": 360,
      "crystals": 16,
      "from": "I",
      "success_percent": 20,
      "to": "II"
    },
    {
      "agris": 10,
      "cron": 670,
      "crystals": 17,
      "from": "II",
      "success_percent": 15,
      "to": "III"
    },
    {
      "agris": 12,
      "cron": 990,
      "crystals": 18,
      "from": "III",
      "success_percent": 13,
      "to": "IV"
    },
    {
      "agris": 14,
      "cron": 1430,
      "crystals": 19,
      "from": "IV",
      "success_percent": 11,
      "to": "V"
    },
    {
      "agris": 15,
      "cron": 1890,
      "crystals": 20,
      "from": "V",
      "success_percent": 10,
      "to": "VI"
    },
    {
      "agris": 17,
      "cron": 2390,
      "crystals": 21,
      "from": "VI",
      "success_percent": 9,
      "to": "VII"
    },
    {
      "agris": 18,
      "cron": 2690,
      "crystals": 22,
      "from": "VII",
      "success_percent": 8.5,
      "to": "VIII"
    },
    {
      "agris": 19,
      "cron": 2750,
      "crystals": 23,
      "from": "VIII",
      "success_percent": 8,
      "to": "IX"
    },
    {
      "agris": 20,
      "cron": 2810,
      "crystals": 25,
      "from": "IX",
      "success_percent": 7.5,
      "to": "X"
    }
  ]
}
```

### `prione-accessories.stats`

- seed_key: "prione-accessories.stats"
- kind: "gear"
- requirement_level: "required"
- title: "부위별 능력치"
- description: "목걸이·허리띠와 반지·귀걸이의 단계별 숙련도 및 생활 경험치 수치다."
- structured_value:

```json
{
  "necklace_and_belt": [
    {
      "level": "+0",
      "life_exp_percent": 8,
      "mastery": 75
    },
    {
      "level": "I",
      "life_exp_percent": 8,
      "mastery": 85
    },
    {
      "level": "II",
      "life_exp_percent": 8,
      "mastery": 95
    },
    {
      "level": "III",
      "life_exp_percent": 10,
      "mastery": 105
    },
    {
      "level": "IV",
      "life_exp_percent": 10,
      "mastery": 115
    },
    {
      "level": "V",
      "life_exp_percent": 10,
      "mastery": 130
    },
    {
      "level": "VI",
      "life_exp_percent": 12,
      "mastery": 150
    },
    {
      "level": "VII",
      "life_exp_percent": 12,
      "mastery": 175
    },
    {
      "level": "VIII",
      "life_exp_percent": 12,
      "mastery": 200
    },
    {
      "level": "IX",
      "life_exp_percent": 12,
      "mastery": 225
    },
    {
      "level": "X",
      "life_exp_percent": 12,
      "mastery": 250
    }
  ],
  "ring_and_earring": [
    {
      "level": "+0",
      "life_exp_percent": 8,
      "mastery": 65
    },
    {
      "level": "I",
      "life_exp_percent": 8,
      "mastery": 70
    },
    {
      "level": "II",
      "life_exp_percent": 8,
      "mastery": 80
    },
    {
      "level": "III",
      "life_exp_percent": 10,
      "mastery": 90
    },
    {
      "level": "IV",
      "life_exp_percent": 10,
      "mastery": 100
    },
    {
      "level": "V",
      "life_exp_percent": 10,
      "mastery": 110
    },
    {
      "level": "VI",
      "life_exp_percent": 12,
      "mastery": 125
    },
    {
      "level": "VII",
      "life_exp_percent": 12,
      "mastery": 150
    },
    {
      "level": "VIII",
      "life_exp_percent": 12,
      "mastery": 175
    },
    {
      "level": "IX",
      "life_exp_percent": 12,
      "mastery": 200
    },
    {
      "level": "X",
      "life_exp_percent": 12,
      "mastery": 225
    }
  ]
}
```

### `prione-accessories.set-effects`

- seed_key: "prione-accessories.set-effects"
- kind: "gear"
- requirement_level: "required"
- title: "세트 효과"
- description: "마노스와 혼용할 때 마노스 세트 효과를 공유하며 프리오네 2개마다 생활 경험치 5% 효과를 추가 적용한다."
- structured_value:

```json
{
  "additional_life_exp_percent": 5,
  "prione_every_n_items": 2,
  "shares_manos_set_when_mixed": true
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `prione-accessories.failure-warning`

- seed_key: "prione-accessories.failure-warning"
- section_type: "common_mistakes"
- title: "마노스 강화와 다름"
- order_no: 1

#### body_markdown

프리오네는 실패해도 액세서리가 파괴되지 않는다. 일반 강화 확률 증가 수치가 성공 확률을 높이지 않으며 성공해도 현재 수치를 소모하지 않는다.

## Related Contents

### `prione-accessories.accessory-progression`

- seed_key: "prione-accessories.accessory-progression"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "life-accessory-progression"
- content_name_ko: "생활 액세서리 진행 체계"
- content_category: "life"
- note: "강화된 마노스를 공식 교환 경로로 사용하는 상위 생활 액세서리다."
- order_no: 1
- relative_path: "../contents/life-accessory-progression.md"
### `life-accessory-progression.prione`

- seed_key: "life-accessory-progression.prione"
- direction: "incoming"
- relation_type: "related"
- content_slug: "life-accessory-progression"
- content_name_ko: "생활 액세서리 진행 체계"
- content_category: "life"
- note: "강화된 마노스를 통해 교환하는 상위 액세서리"
- order_no: 2
- relative_path: "../contents/life-accessory-progression.md"

## Evidence and Sources

### Current evidence

### `prione-accessories.summary::life-mastery-prione-2025-01-08`

- evidence_seed_key: "prione-accessories.summary::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "prione-accessories"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "프리오네 획득과 강화 핵심"
- active: true
- is_active: true

### `prione-accessories.requirement.enhancement-rules::life-mastery-prione-2025-01-08`

- evidence_seed_key: "prione-accessories.requirement.enhancement-rules::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "prione-accessories.enhancement-rules"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "고정 확률·하락·비파괴·크론·스택"
- active: true
- is_active: true

### `prione-accessories.requirement.enhancement-table::life-mastery-prione-2025-01-08`

- evidence_seed_key: "prione-accessories.requirement.enhancement-table::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "prione-accessories.enhancement-table"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "10단계 공식 강화표"
- active: true
- is_active: true

### `prione-accessories.requirement.exchange::life-mastery-prione-2025-01-08`

- evidence_seed_key: "prione-accessories.requirement.exchange::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "prione-accessories.exchange"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "마노스 단계별 교환과 반복 제한"
- active: true
- is_active: true

### `prione-accessories.requirement.set-effects::life-mastery-prione-2025-01-08`

- evidence_seed_key: "prione-accessories.requirement.set-effects::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "prione-accessories.set-effects"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "마노스 혼용과 프리오네 2개 세트"
- active: true
- is_active: true

### `prione-accessories.requirement.stats::life-mastery-prione-2025-01-08`

- evidence_seed_key: "prione-accessories.requirement.stats::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "prione-accessories.stats"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "부위별 단계 능력치"
- active: true
- is_active: true

### Historical / inactive evidence

- None
