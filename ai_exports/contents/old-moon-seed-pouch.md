<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 클로의 그믐달 씨앗 주머니

## Identity

- slug: "old-moon-seed-pouch"
- name_ko: "클로의 그믐달 씨앗 주머니"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "씨앗류 아이템을 최대 50개 보관하며, 현재는 씨앗을 캐릭터 가방으로 옮긴 뒤 울타리에 심어야 한다."
- purpose: "씨앗 주머니의 현재 동작과 적용 연기된 직접 심기를 분리한다."

## Requirements

### `old-moon-seed-pouch.capacity`

- seed_key: "old-moon-seed-pouch.capacity"
- kind: "item"
- requirement_level: "required"
- title: "보관 용량"
- description: "씨앗류 아이템을 최대 50개 보관한다."
- structured_value:

```json
{
  "capacity_items": 50
}
```

### `old-moon-seed-pouch.acquisition`

- seed_key: "old-moon-seed-pouch.acquisition"
- kind: "quest"
- requirement_level: "required"
- title: "획득"
- description: "재배 숙련 1 이상일 때 가문당 1회 흑정령 의뢰로 획득한다."
- structured_value:

```json
{
  "family_limit": 1,
  "minimum_farming_level": "Skilled 1",
  "quest": "[재배] 클로의 그믐달 씨앗 주머니"
}
```

### `old-moon-seed-pouch.current-planting`

- seed_key: "old-moon-seed-pouch.current-planting"
- kind: "other"
- requirement_level: "required"
- title: "현재 심기 동작"
- description: "주머니 속 씨앗은 캐릭터 일반 가방으로 이동한 뒤 울타리에 심는다."
- structured_value:

```json
{
  "direct_planting_current": false,
  "must_transfer_to_character_inventory": true
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `old-moon-seed-pouch.announced`

- seed_key: "old-moon-seed-pouch.announced"
- section_type: "notes"
- title: "ANNOUNCED BUT NOT CONFIRMED LIVE"
- order_no: 1

#### body_markdown

주머니 내부 씨앗 직접 심기는 canonical 현재 mechanic이 아니다. 후속 KR Live source가 생기면 다시 검증한다.

## Related Contents

### `old-moon-seed-pouch.seeds`

- seed_key: "old-moon-seed-pouch.seeds"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "farming-seeds-harvest-breeding"
- content_name_ko: "재배 씨앗·수확·품종개량"
- content_category: "life"
- note: "씨앗 보관"
- order_no: 1
- relative_path: "../contents/farming-seeds-harvest-breeding.md"
### `farming-seeds-harvest-breeding.pouch`

- seed_key: "farming-seeds-harvest-breeding.pouch"
- direction: "incoming"
- relation_type: "related"
- content_slug: "farming-seeds-harvest-breeding"
- content_name_ko: "재배 씨앗·수확·품종개량"
- content_category: "life"
- note: "씨앗 보관"
- order_no: 3
- relative_path: "../contents/farming-seeds-harvest-breeding.md"
### `farming-onboarding-strategy.pouch`

- seed_key: "farming-onboarding-strategy.pouch"
- direction: "incoming"
- relation_type: "related"
- content_slug: "farming-onboarding-strategy"
- content_name_ko: "재배 입문 전략"
- content_category: "life"
- note: null
- order_no: 4
- relative_path: "../contents/farming-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `old-moon-seed-pouch.summary::farming-overhaul-2026-06-04`

- evidence_seed_key: "old-moon-seed-pouch.summary::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "old-moon-seed-pouch"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "50개 보관과 현재 이동 후 심기"
- active: true
- is_active: true

### `old-moon-seed-pouch.summary::old-moon-seed-pouch-2025-07-09`

- evidence_seed_key: "old-moon-seed-pouch.summary::old-moon-seed-pouch-2025-07-09"
- source_id: "old-moon-seed-pouch-2025-07-09"
- title: "7월 9일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14224"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-09"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "old-moon-seed-pouch"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "50개 보관과 현재 이동 후 심기"
- active: true
- is_active: true

### `old-moon-seed-pouch.requirement.acquisition::old-moon-seed-pouch-2025-07-09`

- evidence_seed_key: "old-moon-seed-pouch.requirement.acquisition::old-moon-seed-pouch-2025-07-09"
- source_id: "old-moon-seed-pouch-2025-07-09"
- title: "7월 9일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14224"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-09"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "old-moon-seed-pouch.acquisition"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "숙련 1·가문당 1회"
- active: true
- is_active: true

### `old-moon-seed-pouch.requirement.capacity::old-moon-seed-pouch-2025-07-09`

- evidence_seed_key: "old-moon-seed-pouch.requirement.capacity::old-moon-seed-pouch-2025-07-09"
- source_id: "old-moon-seed-pouch-2025-07-09"
- title: "7월 9일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14224"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-09"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "old-moon-seed-pouch.capacity"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "최대 50개"
- active: true
- is_active: true

### `old-moon-seed-pouch.requirement.current-planting::farming-overhaul-2026-06-04`

- evidence_seed_key: "old-moon-seed-pouch.requirement.current-planting::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "old-moon-seed-pouch.current-planting"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일반 가방 이동 후 심기"
- active: true
- is_active: true

### `old-moon-seed-pouch.requirement.current-planting::old-moon-seed-pouch-2025-07-09`

- evidence_seed_key: "old-moon-seed-pouch.requirement.current-planting::old-moon-seed-pouch-2025-07-09"
- source_id: "old-moon-seed-pouch-2025-07-09"
- title: "7월 9일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14224"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-09"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "old-moon-seed-pouch.current-planting"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일반 가방 이동 후 심기"
- active: true
- is_active: true

### Historical / inactive evidence

### `old-moon-seed-pouch.requirement.planned-direct-planting::farming-overhaul-2026-06-04`

- evidence_seed_key: "old-moon-seed-pouch.requirement.planned-direct-planting::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "old-moon-seed-pouch.planned-direct-planting"
- claim_key: "structured_value"
- verification_status: "needs_review"
- last_verified_at: "2026-09-03"
- evidence_note: "직접 심기 계획은 적용 연기"
- active: false
- is_active: false
