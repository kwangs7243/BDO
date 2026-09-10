<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 저격 수렵

## Identity

- slug: "sniper-hunting"
- name_ko: "저격 수렵"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "저격 수렵은 자세와 조준을 사용하며 희귀 채집물 등급과 고기 추가량은 누적 손상도 구간으로 판정한다."
- purpose: "현재 누적 손상도 보상 구간을 옛 숙련도 전용 구간과 구분한다."

## Requirements

### `sniper-hunting.damage-tiers`

- seed_key: "sniper-hunting.damage-tiers"
- kind: "item"
- requirement_level: "required"
- title: "누적 손상도별 보상"
- description: "누적 손상도별 보상의 현재 규칙이다."
- structured_value:

```json
{
  "mastery_also_applies_separately": true,
  "rows": [
    {
      "damage_percent": "0",
      "meat_bonus_percent": 10,
      "minimum": 1,
      "rare_grade": "upper_or_lower"
    },
    {
      "damage_percent": "1-40",
      "meat_bonus_percent": 10,
      "minimum": 1,
      "rare_grade": "middle_or_lower"
    },
    {
      "damage_percent": "41-80",
      "meat_bonus_percent": 5,
      "minimum": 1,
      "rare_grade": "lower"
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

### `hunting-onboarding-strategy.sniper`

- seed_key: "hunting-onboarding-strategy.sniper"
- direction: "incoming"
- relation_type: "related"
- content_slug: "hunting-onboarding-strategy"
- content_name_ko: "수렵 입문 전략"
- content_category: "life"
- note: "저격 수렵의 별도 조작과 대상을 확인한다."
- order_no: 3
- relative_path: "../contents/hunting-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `sniper-hunting.claim.current::sniper-reward-rework-2023-05-03`

- evidence_seed_key: "sniper-hunting.claim.current::sniper-reward-rework-2023-05-03"
- source_id: "sniper-reward-rework-2023-05-03"
- title: "5월 3일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=10269"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-05-03"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "sniper-hunting"
- claim_key: "requirement:sniper-hunting.damage-tiers"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `sniper-hunting.claim.legacy-mastery-tiers::hunting-guide`

- evidence_seed_key: "sniper-hunting.claim.legacy-mastery-tiers::hunting-guide"
- source_id: "hunting-guide"
- title: "수렵"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "sniper-hunting"
- claim_key: "legacy:rare-reward-only-mastery-250-500-900"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: false
- is_active: false
