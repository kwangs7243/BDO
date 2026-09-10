<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 수렵 장비와 화승총 강화

## Identity

- slug: "hunting-firearms"
- name_ko: "수렵 장비와 화승총 강화"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "수렵 장비는 수렵복·수렵 가방·단계별 화승총·저격총으로 나뉘며 화승총 강화 실패의 하락률은 구간별로 다르다."
- purpose: "수렵 장비 범주와 화승총 강화 하락 규칙을 기록한다."

## Requirements

### `hunting-firearms.categories`

- seed_key: "hunting-firearms.categories"
- kind: "item"
- requirement_level: "required"
- title: "수렵 장비 범주"
- description: "수렵 장비 범주의 현재 규칙이다."
- structured_value:

```json
{
  "clothes": [
    "Loggia",
    "Robaud",
    "Manos"
  ],
  "mastery_bags": [
    "Loggia",
    "Robaud",
    "Manos"
  ],
  "matchlocks": [
    "beginner",
    "apprentice",
    "skilled",
    "professional",
    "artisan",
    "master",
    "solid_master"
  ],
  "sniper_rifles": [
    "sniper_rifle",
    "Marni_sniper_rifle",
    "sturdy_Marni_sniper_rifle"
  ]
}
```

### `hunting-firearms.downgrade`

- seed_key: "hunting-firearms.downgrade"
- kind: "other"
- requirement_level: "required"
- title: "강화 실패 시 하락"
- description: "강화 실패 시 하락의 현재 규칙이다."
- structured_value:

```json
{
  "plus_1_to_6": {
    "downgrade_percent": 0
  },
  "plus_7_to_8": {
    "downgrade_percent": 10,
    "retain_percent": 90
  },
  "plus_8_to_9": {
    "downgrade_percent": 50,
    "retain_percent": 50
  },
  "plus_9_to_10": {
    "downgrade_percent": 100
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

### `marni-sniper-rifle.firearms`

- seed_key: "marni-sniper-rifle.firearms"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "marni-sniper-rifle"
- content_name_ko: "마르니 저격총"
- content_category: "life"
- note: "저격총 장비 계열의 제작·강화 상세다."
- order_no: 1
- relative_path: "../contents/marni-sniper-rifle.md"
### `hunting-onboarding-strategy.firearms`

- seed_key: "hunting-onboarding-strategy.firearms"
- direction: "incoming"
- relation_type: "related"
- content_slug: "hunting-onboarding-strategy"
- content_name_ko: "수렵 입문 전략"
- content_category: "life"
- note: "일반·저격 장비 구분과 현재 장비 규칙을 확인한다."
- order_no: 2
- relative_path: "../contents/hunting-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `hunting-firearms.claim.current::hunting-enhancement-guide`

- evidence_seed_key: "hunting-firearms.claim.current::hunting-enhancement-guide"
- source_id: "hunting-enhancement-guide"
- title: "화승총, 저격총, 낚싯대 및 찌 강화 실패 시 강화 단계 하락 확률 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=435"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "hunting-firearms"
- claim_key: "requirements:hunting-firearms"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### `hunting-firearms.claim.current::hunting-guide`

- evidence_seed_key: "hunting-firearms.claim.current::hunting-guide"
- source_id: "hunting-guide"
- title: "수렵"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "hunting-firearms"
- claim_key: "requirements:hunting-firearms"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
