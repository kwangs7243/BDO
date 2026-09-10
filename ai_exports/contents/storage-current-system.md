<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 창고 현재 시스템

## Identity

- slug: "storage-current-system"
- name_ko: "창고 현재 시스템"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "아이템 창고는 마을·지역 단위로 분리되고 기본 8칸이며 시간성 아이템은 보관해도 시간이 멈추지 않는다."
- purpose: "아이템 창고와 통합 은화를 구분하고 보관 규칙을 설명한다."

## Requirements

### `storage-current-system.items`

- seed_key: "storage-current-system.items"
- kind: "other"
- requirement_level: "required"
- title: "아이템 창고"
- description: "마을별 아이템 보관과 기본 슬롯을 기록한다."
- structured_value:

```json
{
  "base_slots": 8,
  "scope": "town_or_region",
  "some_character_bound_items_not_storable": true
}
```

### `storage-current-system.house-expansion`

- seed_key: "storage-current-system.house-expansion"
- kind: "other"
- requirement_level: "required"
- title: "창고용 집"
- description: "창고 용도 집으로 슬롯을 늘린다."
- structured_value:

```json
{
  "additional_slots_per_house_storage_stage_general_guide": 3,
  "exact_house_efficiency_varies": true
}
```

### `storage-current-system.timed-items`

- seed_key: "storage-current-system.timed-items"
- kind: "other"
- requirement_level: "required"
- title: "시간성 아이템"
- description: "보관 중에도 가격 보증기간·유효기간이 흐른다."
- structured_value:

```json
{
  "examples": [
    "fish_price_guarantee",
    "expiry_items"
  ],
  "time_stops_in_storage": false
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

### `storage-current-system.housing`

- seed_key: "storage-current-system.housing"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "housing-life-economy"
- content_name_ko: "집과 생활 경제"
- content_category: "life"
- note: "창고는 집의 기본·선택 용도다."
- order_no: 1
- relative_path: "../contents/housing-life-economy.md"
### `storage-current-system.fish-freshness`

- seed_key: "storage-current-system.fish-freshness"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "fish-freshness-and-trade"
- content_name_ko: "물고기 신선도와 무역"
- content_category: "life"
- note: "물고기 가격 보증기간은 창고에서도 계속 흐른다."
- order_no: 2
- relative_path: "../contents/fish-freshness-and-trade.md"
### `storage-current-system.silver`

- seed_key: "storage-current-system.silver"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "family-silver-unification"
- content_name_ko: "가문 통합 은화"
- content_category: "life"
- note: "아이템 창고와 은화 통합 pool은 별도다."
- order_no: 3
- relative_path: "../contents/family-silver-unification.md"
### `family-silver-unification.storage`

- seed_key: "family-silver-unification.storage"
- direction: "incoming"
- relation_type: "related"
- content_slug: "family-silver-unification"
- content_name_ko: "가문 통합 은화"
- content_category: "life"
- note: "창고 아이템 슬롯과 통합 은화 pool은 별도 의미다."
- order_no: 1
- relative_path: "../contents/family-silver-unification.md"
### `magnus-remote-storage.storage`

- seed_key: "magnus-remote-storage.storage"
- direction: "incoming"
- relation_type: "related"
- content_slug: "magnus-remote-storage"
- content_name_ko: "마그누스 원격 창고"
- content_category: "life"
- note: "마그누스 진행으로 다른 지역 아이템 창고를 원격 이용한다."
- order_no: 1
- relative_path: "../contents/magnus-remote-storage.md"
### `family-convenience-unlock-foundation.storage`

- seed_key: "family-convenience-unlock-foundation.storage"
- direction: "incoming"
- relation_type: "related"
- content_slug: "family-convenience-unlock-foundation"
- content_name_ko: "가문 편의 기능 해금"
- content_category: "progression"
- note: null
- order_no: 4
- relative_path: "../contents/family-convenience-unlock-foundation.md"
### `magnus-progression.storage`

- seed_key: "magnus-progression.storage"
- direction: "incoming"
- relation_type: "related"
- content_slug: "magnus-progression"
- content_name_ko: "마그누스 전체 진행"
- content_category: "progression"
- note: null
- order_no: 4
- relative_path: "../contents/magnus-progression.md"
### `processing-onboarding-strategy.storage`

- seed_key: "processing-onboarding-strategy.storage"
- direction: "incoming"
- relation_type: "related"
- content_slug: "processing-onboarding-strategy"
- content_name_ko: "가공 입문 전략"
- content_category: "life"
- note: null
- order_no: 6
- relative_path: "../contents/processing-onboarding-strategy.md"
### `farming-onboarding-strategy.storage`

- seed_key: "farming-onboarding-strategy.storage"
- direction: "incoming"
- relation_type: "related"
- content_slug: "farming-onboarding-strategy"
- content_name_ko: "재배 입문 전략"
- content_category: "life"
- note: null
- order_no: 7
- relative_path: "../contents/farming-onboarding-strategy.md"
### `barter-onboarding-strategy.storage`

- seed_key: "barter-onboarding-strategy.storage"
- direction: "incoming"
- relation_type: "related"
- content_slug: "barter-onboarding-strategy"
- content_name_ko: "물물교환 입문 운영 전략"
- content_category: "ocean_barter"
- note: "출발·중간·귀환 재고"
- order_no: 8
- relative_path: "../contents/barter-onboarding-strategy.md"
### `alchemy-onboarding-strategy.storage`

- seed_key: "alchemy-onboarding-strategy.storage"
- direction: "incoming"
- relation_type: "related"
- content_slug: "alchemy-onboarding-strategy"
- content_name_ko: "연금 입문 전략"
- content_category: "life"
- note: null
- order_no: 9
- relative_path: "../contents/alchemy-onboarding-strategy.md"
### `cooking-onboarding-strategy.storage`

- seed_key: "cooking-onboarding-strategy.storage"
- direction: "incoming"
- relation_type: "related"
- content_slug: "cooking-onboarding-strategy"
- content_name_ko: "요리 입문 전략"
- content_category: "life"
- note: null
- order_no: 9
- relative_path: "../contents/cooking-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `storage-current-system.claim.current::house-guide`

- evidence_seed_key: "storage-current-system.claim.current::house-guide"
- source_id: "house-guide"
- title: "집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=92"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "storage-current-system"
- claim_key: "requirements:storage-current-system"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `storage-current-system.claim.current::storage-guide`

- evidence_seed_key: "storage-current-system.claim.current::storage-guide"
- source_id: "storage-guide"
- title: "창고"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=39"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "storage-current-system"
- claim_key: "requirements:storage-current-system"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
