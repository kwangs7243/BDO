<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 재배 울타리

## Identity

- slug: "farming-fences"
- name_ko: "재배 울타리"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "울타리는 종류별 공헌도와 작물 칸 수가 다르며, 2026-06-04 이후 28일 이상 재배 활동이 없으면 철거된다."
- purpose: "현재 울타리 종류·비용·칸과 자동 철거 기준을 구조화한다."

## Requirements

### `farming-fences.types`

- seed_key: "farming-fences.types"
- kind: "gear"
- requirement_level: "required"
- title: "울타리 종류"
- description: "현재 가이드의 대표 울타리, 공헌도와 작물 칸 수다."
- structured_value:

```json
{
  "fences": [
    {
      "acquisition": "quest",
      "contribution": 0,
      "crop_slots": 1,
      "name": "엉성한 울타리"
    },
    {
      "acquisition": "rental",
      "contribution": 3,
      "crop_slots": 4,
      "name": "작은 울타리"
    },
    {
      "acquisition": "rental",
      "contribution": 6,
      "crop_slots": 7,
      "name": "평범한 울타리"
    },
    {
      "acquisition": "rental",
      "contribution": 10,
      "crop_slots": 10,
      "name": "단단한 울타리"
    },
    {
      "acquisition": "rental",
      "contribution": 10,
      "crop_slots": 10,
      "minimum_farming_level": "Master 1",
      "name": "그믐달 울타리"
    }
  ]
}
```

### `farming-fences.old-moon`

- seed_key: "farming-fences.old-moon"
- kind: "level"
- requirement_level: "required"
- title: "그믐달 울타리 조건"
- description: "그믐달 울타리는 재배 명장 1 이상부터 설치·이용할 수 있다."
- structured_value:

```json
{
  "contribution": 10,
  "crop_slots": 10,
  "minimum_farming_level": "Master 1",
  "smaller_than_sturdy_fence": true
}
```

### `farming-fences.inactivity-removal`

- seed_key: "farming-fences.inactivity-removal"
- kind: "other"
- requirement_level: "required"
- title: "미사용 자동 철거"
- description: "28일 이상 재배 활동이 없으면 자동 철거되고 울타리는 설치 영지 대표 마을 창고로 이동한다."
- structured_value:

```json
{
  "current_days": 28,
  "destination": "representative_town_storage_of_installed_territory",
  "legacy_active": false,
  "legacy_days": 14
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

### `farming-fences.cycle`

- seed_key: "farming-fences.cycle"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "farming-current-cycle"
- content_name_ko: "재배 현재 주기"
- content_category: "life"
- note: "재배 주기의 공간"
- order_no: 1
- relative_path: "../contents/farming-current-cycle.md"
### `farming-current-cycle.fences`

- seed_key: "farming-current-cycle.fences"
- direction: "incoming"
- relation_type: "related"
- content_slug: "farming-current-cycle"
- content_name_ko: "재배 현재 주기"
- content_category: "life"
- note: "재배 울타리"
- order_no: 1
- relative_path: "../contents/farming-current-cycle.md"
### `farming-onboarding-strategy.fences`

- seed_key: "farming-onboarding-strategy.fences"
- direction: "incoming"
- relation_type: "related"
- content_slug: "farming-onboarding-strategy"
- content_name_ko: "재배 입문 전략"
- content_category: "life"
- note: null
- order_no: 2
- relative_path: "../contents/farming-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `farming-fences.summary::farming-guide`

- evidence_seed_key: "farming-fences.summary::farming-guide"
- source_id: "farming-guide"
- title: "재배"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=94"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "farming-fences"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "울타리와 28일 철거"
- active: true
- is_active: true

### `farming-fences.summary::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-fences.summary::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "farming-fences"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "울타리와 28일 철거"
- active: true
- is_active: true

### `farming-fences.requirement.inactivity-removal::farming-guide`

- evidence_seed_key: "farming-fences.requirement.inactivity-removal::farming-guide"
- source_id: "farming-guide"
- title: "재배"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=94"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-fences.inactivity-removal"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "현재 28일 철거"
- active: true
- is_active: true

### `farming-fences.requirement.inactivity-removal::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-fences.requirement.inactivity-removal::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-fences.inactivity-removal"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "현재 28일 철거"
- active: true
- is_active: true

### `farming-fences.requirement.old-moon::farming-guide`

- evidence_seed_key: "farming-fences.requirement.old-moon::farming-guide"
- source_id: "farming-guide"
- title: "재배"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=94"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-fences.old-moon"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "그믐달 울타리 조건"
- active: true
- is_active: true

### `farming-fences.requirement.types::farming-guide`

- evidence_seed_key: "farming-fences.requirement.types::farming-guide"
- source_id: "farming-guide"
- title: "재배"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=94"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-fences.types"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "종류·공헌도·칸"
- active: true
- is_active: true

### Historical / inactive evidence

### `farming-fences.legacy.inactivity-14-days::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-fences.legacy.inactivity-14-days::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "farming-fences"
- claim_key: "legacy.inactivity_removal_days"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "기존 14일 기준은 28일로 대체"
- active: false
- is_active: false
