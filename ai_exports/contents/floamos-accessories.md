<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 플로아모스 액세서리

## Identity

- slug: "floamos-accessories"
- name_ko: "플로아모스 액세서리"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "강화할 수 없고 고(III) 마노스와 동일한 능력치를 가지며, 가문당 1회 획득 후 일일 1회 부위 교환이 가능하다."
- purpose: "플로아모스의 상시 획득과 부위 변경 규칙을 기록한다."

## Requirements

### `floamos-accessories.properties`

- seed_key: "floamos-accessories.properties"
- kind: "gear"
- requirement_level: "required"
- title: "아이템 특징"
- description: "4개 부위가 있으며 강화할 수 없고 고(III) 마노스와 동일 능력치 및 마노스 세트 효과를 적용받는다."
- structured_value:

```json
{
  "counts_for_manos_set_effect": true,
  "enhancement_allowed": false,
  "equivalent_stats_to": "TRI Manos accessory",
  "slots": [
    "목걸이",
    "허리띠",
    "반지",
    "귀걸이"
  ]
}
```

### `floamos-accessories.family-acquisition`

- seed_key: "floamos-accessories.family-acquisition"
- kind: "quest"
- requirement_level: "required"
- title: "가문당 1회 획득"
- description: "리아나에게 부산물 3종 중 한 종류 300개를 건네고 플로아모스 4종 중 하나를 선택한다."
- structured_value:

```json
{
  "choose_one_slot": true,
  "family_limit": 1,
  "npc": "리아나",
  "turn_in_one_of": [
    {
      "amount": 300,
      "item": "요정의 숨결"
    },
    {
      "amount": 300,
      "item": "마녀의 별미"
    },
    {
      "amount": 300,
      "item": "미지의 촉매"
    }
  ]
}
```

### `floamos-accessories.daily-exchange`

- seed_key: "floamos-accessories.daily-exchange"
- kind: "quest"
- requirement_level: "required"
- title: "부위 변경"
- description: "기존 플로아모스와 응축된 마력의 검은 결정 10개를 건네고 다른 부위 하나를 선택한다."
- structured_value:

```json
{
  "choose_one_slot": true,
  "daily_limit": 1,
  "inputs": [
    {
      "amount": 1,
      "item": "플로아모스 액세서리"
    },
    {
      "amount": 10,
      "item": "응축된 마력의 검은 결정"
    }
  ],
  "npc": "리아나"
}
```

## Steps

- None

## Schedules

### `floamos-accessories.exchange-reset`

- seed_key: "floamos-accessories.exchange-reset"
- rule_type: "quest_reset"
- recurrence_type: "daily"
- weekday: null
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "플로아모스 부위 변경 의뢰: 가문당 매일 1회"

## Rewards

- None

## Sections

- None

## Related Contents

### `floamos-accessories.accessory-progression`

- seed_key: "floamos-accessories.accessory-progression"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "life-accessory-progression"
- content_name_ko: "생활 액세서리 진행 체계"
- content_category: "life"
- note: "생활 액세서리 진행 체계의 고정형 선택지다."
- order_no: 1
- relative_path: "../contents/life-accessory-progression.md"
### `life-accessory-progression.floamos`

- seed_key: "life-accessory-progression.floamos"
- direction: "incoming"
- relation_type: "related"
- content_slug: "life-accessory-progression"
- content_name_ko: "생활 액세서리 진행 체계"
- content_category: "life"
- note: "고(III) 마노스와 동일 능력치의 강화 불가 액세서리"
- order_no: 1
- relative_path: "../contents/life-accessory-progression.md"

## Evidence and Sources

### Current evidence

### `floamos-accessories.summary::floamos-2023-02-15`

- evidence_seed_key: "floamos-accessories.summary::floamos-2023-02-15"
- source_id: "floamos-2023-02-15"
- title: "2월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=9834"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-02-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "floamos-accessories"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "상시 획득·부위 변경·현재 장착 가능 재확인"
- active: true
- is_active: true

### `floamos-accessories.summary::life-unification-2026-09-02`

- evidence_seed_key: "floamos-accessories.summary::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "floamos-accessories"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "상시 획득·부위 변경·현재 장착 가능 재확인"
- active: true
- is_active: true

### `floamos-accessories.requirement.daily-exchange::floamos-2023-02-15`

- evidence_seed_key: "floamos-accessories.requirement.daily-exchange::floamos-2023-02-15"
- source_id: "floamos-2023-02-15"
- title: "2월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=9834"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-02-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "floamos-accessories.daily-exchange"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "기존 액세서리와 결정 10개로 일일 1회 변경"
- active: true
- is_active: true

### `floamos-accessories.requirement.family-acquisition::floamos-2023-02-15`

- evidence_seed_key: "floamos-accessories.requirement.family-acquisition::floamos-2023-02-15"
- source_id: "floamos-2023-02-15"
- title: "2월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=9834"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-02-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "floamos-accessories.family-acquisition"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "가문당 1회 부산물 300개 선택 납품"
- active: true
- is_active: true

### `floamos-accessories.requirement.properties::floamos-2023-02-15`

- evidence_seed_key: "floamos-accessories.requirement.properties::floamos-2023-02-15"
- source_id: "floamos-2023-02-15"
- title: "2월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=9834"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-02-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "floamos-accessories.properties"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "4종, 강화 불가, TRI 마노스 동일 능력치"
- active: true
- is_active: true

### `floamos-accessories.requirement.properties::life-unification-2026-09-02`

- evidence_seed_key: "floamos-accessories.requirement.properties::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "floamos-accessories.properties"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "4종, 강화 불가, TRI 마노스 동일 능력치"
- active: true
- is_active: true

### `floamos-accessories.schedule.exchange-reset::floamos-2023-02-15`

- evidence_seed_key: "floamos-accessories.schedule.exchange-reset::floamos-2023-02-15"
- source_id: "floamos-2023-02-15"
- title: "2월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=9834"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-02-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "floamos-accessories.exchange-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일일 1회 부위 변경"
- active: true
- is_active: true

### Historical / inactive evidence

- None
