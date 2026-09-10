<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 심청의 신묘한 어항

## Identity

- slug: "mystical-fish-tank"
- name_ko: "심청의 신묘한 어항"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "물고기 50마리를 보관하고 가격 보증기간을 5배로 늘리며, 캐릭터 가방에 있으면 낚은 물고기가 우선 보관된다."
- purpose: "어항의 보관·보증기간 효과와 2025-02-05 획득 조건 변경을 기록한다."

## Requirements

### `mystical-fish-tank.storage`

- seed_key: "mystical-fish-tank.storage"
- kind: "item"
- requirement_level: "required"
- title: "물고기 전용 보관"
- description: "심청의 신묘한 어항은 물고기 최대 50마리용 가방이다."
- structured_value:

```json
{
  "auto_store_when_in_character_inventory": true,
  "capacity_fish": 50
}
```

### `mystical-fish-tank.duration`

- seed_key: "mystical-fish-tank.duration"
- kind: "stat"
- requirement_level: "required"
- title: "가격 보증기간"
- description: "어항 안에서는 물고기 가격 보증기간이 일반 보관보다 5배 길다."
- structured_value:

```json
{
  "guarantee_duration_multiplier": 5
}
```

### `mystical-fish-tank.acquisition`

- seed_key: "mystical-fish-tank.acquisition"
- kind: "quest"
- requirement_level: "required"
- title: "현재 획득 조건"
- description: "의뢰의 물고기 낚기 조건은 유지되지만 오색 빛깔 조개 아이템 요구는 제거됐다."
- structured_value:

```json
{
  "fishing_objectives_remain": true,
  "iridescent_shells_required": false,
  "shell_amount": 0
}
```

### `mystical-fish-tank.restrictions`

- seed_key: "mystical-fish-tank.restrictions"
- kind: "other"
- requirement_level: "required"
- title: "보관 제한"
- description: "캐릭터 소지 무게를 초과한 상태에서는 물고기를 보관할 수 없으며 물고기가 든 어항은 이동 제한이 있다."
- structured_value:

```json
{
  "filled_tank_remote_storage_transfer": false,
  "store_when_over_weight_limit": false
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

### `mystical-fish-tank.auto`

- seed_key: "mystical-fish-tank.auto"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "auto-fishing"
- content_name_ko: "일반 자동 낚시"
- content_category: "life"
- note: "일반 자동 낚시 결과 보관"
- order_no: 1
- relative_path: "../contents/auto-fishing.md"
### `mystical-fish-tank.freshness`

- seed_key: "mystical-fish-tank.freshness"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "fish-freshness-and-trade"
- content_name_ko: "물고기 신선도와 무역"
- content_category: "life"
- note: "가격 보증기간 5배"
- order_no: 2
- relative_path: "../contents/fish-freshness-and-trade.md"
### `mystical-fish-tank.imperial`

- seed_key: "mystical-fish-tank.imperial"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "imperial-fishing-delivery"
- content_name_ko: "황실 낚시 납품"
- content_category: "life"
- note: "보관한 납품 가능 물고기 판매"
- order_no: 3
- relative_path: "../contents/imperial-fishing-delivery.md"
### `auto-fishing.tank`

- seed_key: "auto-fishing.tank"
- direction: "incoming"
- relation_type: "related"
- content_slug: "auto-fishing"
- content_name_ko: "일반 자동 낚시"
- content_category: "life"
- note: "가방 내 어항 자동 보관"
- order_no: 3
- relative_path: "../contents/auto-fishing.md"
### `fish-freshness-and-trade.tank`

- seed_key: "fish-freshness-and-trade.tank"
- direction: "incoming"
- relation_type: "related"
- content_slug: "fish-freshness-and-trade"
- content_name_ko: "물고기 신선도와 무역"
- content_category: "life"
- note: "어항의 5배 보증기간"
- order_no: 3
- relative_path: "../contents/fish-freshness-and-trade.md"
### `fishing-onboarding-strategy.fish-tank`

- seed_key: "fishing-onboarding-strategy.fish-tank"
- direction: "incoming"
- relation_type: "related"
- content_slug: "fishing-onboarding-strategy"
- content_name_ko: "낚시 입문 전략"
- content_category: "life"
- note: "장기 보관 관련 진행도를 확인한다."
- order_no: 6
- relative_path: "../contents/fishing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `mystical-fish-tank.summary::mystical-fish-tank-rules-2024-08-28`

- evidence_seed_key: "mystical-fish-tank.summary::mystical-fish-tank-rules-2024-08-28"
- source_id: "mystical-fish-tank-rules-2024-08-28"
- title: "8월 28일(수) 펄 상점 패키지 및 신규 상품 소개"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12739"
- publisher: "Pearl Abyss"
- source_type: "official_notice"
- published_at: "2024-08-28"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "mystical-fish-tank"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보관·5배와 획득 변경"
- active: true
- is_active: true

### `mystical-fish-tank.summary::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "mystical-fish-tank.summary::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "mystical-fish-tank"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보관·5배와 획득 변경"
- active: true
- is_active: true

### `mystical-fish-tank.requirement.acquisition::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "mystical-fish-tank.requirement.acquisition::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "mystical-fish-tank.acquisition"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "오색 빛깔 조개 제거"
- active: true
- is_active: true

### `mystical-fish-tank.requirement.duration::fish-freshness-2025-05-21`

- evidence_seed_key: "mystical-fish-tank.requirement.duration::fish-freshness-2025-05-21"
- source_id: "fish-freshness-2025-05-21"
- title: "5월 21일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13995"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-21"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "mystical-fish-tank.duration"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보증기간 5배"
- active: true
- is_active: true

### `mystical-fish-tank.requirement.duration::mystical-fish-tank-rules-2024-08-28`

- evidence_seed_key: "mystical-fish-tank.requirement.duration::mystical-fish-tank-rules-2024-08-28"
- source_id: "mystical-fish-tank-rules-2024-08-28"
- title: "8월 28일(수) 펄 상점 패키지 및 신규 상품 소개"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12739"
- publisher: "Pearl Abyss"
- source_type: "official_notice"
- published_at: "2024-08-28"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "mystical-fish-tank.duration"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보증기간 5배"
- active: true
- is_active: true

### `mystical-fish-tank.requirement.restrictions::mystical-fish-tank-rules-2024-08-28`

- evidence_seed_key: "mystical-fish-tank.requirement.restrictions::mystical-fish-tank-rules-2024-08-28"
- source_id: "mystical-fish-tank-rules-2024-08-28"
- title: "8월 28일(수) 펄 상점 패키지 및 신규 상품 소개"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12739"
- publisher: "Pearl Abyss"
- source_type: "official_notice"
- published_at: "2024-08-28"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "mystical-fish-tank.restrictions"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "무게·이동 제한"
- active: true
- is_active: true

### `mystical-fish-tank.requirement.storage::mystical-fish-tank-rules-2024-08-28`

- evidence_seed_key: "mystical-fish-tank.requirement.storage::mystical-fish-tank-rules-2024-08-28"
- source_id: "mystical-fish-tank-rules-2024-08-28"
- title: "8월 28일(수) 펄 상점 패키지 및 신규 상품 소개"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12739"
- publisher: "Pearl Abyss"
- source_type: "official_notice"
- published_at: "2024-08-28"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "mystical-fish-tank.storage"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "50마리·자동 보관"
- active: true
- is_active: true

### Historical / inactive evidence

### `mystical-fish-tank.legacy.four-shells::mystical-fish-tank-2023-08-02`

- evidence_seed_key: "mystical-fish-tank.legacy.four-shells::mystical-fish-tank-2023-08-02"
- source_id: "mystical-fish-tank-2023-08-02"
- title: "올 여름은 바닷 속 수궁에서 시원하고 즐겁게!"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=10724"
- publisher: "Pearl Abyss"
- source_type: "official_event"
- published_at: "2023-08-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "mystical-fish-tank"
- claim_key: "legacy.iridescent_shells_required"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "오색 빛깔 조개 4개 요구는 제거"
- active: false
- is_active: false

### `mystical-fish-tank.legacy.four-shells::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "mystical-fish-tank.legacy.four-shells::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "mystical-fish-tank"
- claim_key: "legacy.iridescent_shells_required"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "오색 빛깔 조개 4개 요구는 제거"
- active: false
- is_active: false
