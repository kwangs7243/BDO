<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 마그누스 원격 창고

## Identity

- slug: "magnus-remote-storage"
- name_ko: "마그누스 원격 창고"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "마그누스 진행 후 창고지기·메이드로 다른 지역 창고와 캐릭터 가방 사이를 원격 이용하되 특정 아이템은 이동할 수 없다."
- purpose: "마그누스 원격 접근·제한·2025 타 마을 판매 기능을 일반 수송과 구분한다."

## Requirements

### `magnus-remote-storage.unlock`

- seed_key: "magnus-remote-storage.unlock"
- kind: "quest"
- requirement_level: "required"
- title: "원격 창고 해금"
- description: "도움의 대가와 대상 지역 심연의 혈관 지식·지도 조건을 적용한다."
- structured_value:

```json
{
  "access": [
    "storage_keeper",
    "storage_maid"
  ],
  "knowledge_required": [
    "도움의 대가",
    "target_region_abyssal_vein"
  ],
  "magnus_progress_required": true,
  "target_town_map_discovered_required": true
}
```

### `magnus-remote-storage.restrictions`

- seed_key: "magnus-remote-storage.restrictions"
- kind: "item"
- requirement_level: "required"
- title: "원격 이동 제한"
- description: "원격 창고로 이동할 수 없는 품목군을 기록한다."
- structured_value:

```json
{
  "restricted_item_classes": [
    "trade_goods",
    "barter_goods",
    "treasure_items",
    "ornette_or_odores_spirit_essence_and_lower_potions"
  ]
}
```

### `magnus-remote-storage.remote-sale`

- seed_key: "magnus-remote-storage.remote-sale"
- kind: "other"
- requirement_level: "required"
- title: "타 마을 창고 판매·거래소 이동"
- description: "마그누스 전체 의뢰 완료 후 다른 마을 창고 품목의 지정 기능을 지원한다."
- structured_value:

```json
{
  "all_items_freely_movable": false,
  "full_magnus_questline_required": true,
  "move_to_central_market_storage": true,
  "remote_movement_restrictions_still_apply": true,
  "remote_town_storage_item_sale": true
}
```

### `magnus-remote-storage.distinction`

- seed_key: "magnus-remote-storage.distinction"
- kind: "other"
- requirement_level: "required"
- title: "일반 수송과 구분"
- description: "일반 창고 수송의 package·경로 시간·미연결 비용과 같은 시스템이 아니다."
- structured_value:

```json
{
  "same_as_production_special_delivery": false,
  "same_as_storage_transport": false,
  "same_as_workshop_material_logistics": false
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

### `magnus-remote-storage.storage`

- seed_key: "magnus-remote-storage.storage"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "storage-current-system"
- content_name_ko: "창고 현재 시스템"
- content_category: "life"
- note: "마그누스 진행으로 다른 지역 아이템 창고를 원격 이용한다."
- order_no: 1
- relative_path: "../contents/storage-current-system.md"
### `magnus-remote-storage.transport`

- seed_key: "magnus-remote-storage.transport"
- direction: "outgoing"
- relation_type: "alternative"
- content_slug: "storage-transport"
- content_name_ko: "일반 창고 수송"
- content_category: "life"
- note: "제한 품목을 제외한 원격 입출고는 일반 수송과 다른 접근 수단이다."
- order_no: 2
- relative_path: "../contents/storage-transport.md"
### `content-unlock-foundation.magnus-storage`

- seed_key: "content-unlock-foundation.magnus-storage"
- direction: "incoming"
- relation_type: "related"
- content_slug: "content-unlock-foundation"
- content_name_ko: "콘텐츠 해금 기반"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/content-unlock-foundation.md"
### `family-convenience-unlock-foundation.remote-storage`

- seed_key: "family-convenience-unlock-foundation.remote-storage"
- direction: "incoming"
- relation_type: "related"
- content_slug: "family-convenience-unlock-foundation"
- content_name_ko: "가문 편의 기능 해금"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/family-convenience-unlock-foundation.md"
### `magnus-progression.remote-storage`

- seed_key: "magnus-progression.remote-storage"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "magnus-progression"
- content_name_ko: "마그누스 전체 진행"
- content_category: "progression"
- note: null
- order_no: 3
- relative_path: "../contents/magnus-progression.md"
### `storage-transport.magnus`

- seed_key: "storage-transport.magnus"
- direction: "incoming"
- relation_type: "related"
- content_slug: "storage-transport"
- content_name_ko: "일반 창고 수송"
- content_category: "life"
- note: "시간이 드는 일반 수송과 마그누스 원격 입출고는 별개다."
- order_no: 3
- relative_path: "../contents/storage-transport.md"

## Evidence and Sources

### Current evidence

### `magnus-remote-storage.claim.current::magnus-guide`

- evidence_seed_key: "magnus-remote-storage.claim.current::magnus-guide"
- source_id: "magnus-guide"
- title: "어비스 원 : 마그누스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=305"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "magnus-remote-storage"
- claim_key: "requirements:magnus-remote-storage"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `magnus-remote-storage.claim.current::magnus-storage-history`

- evidence_seed_key: "magnus-remote-storage.claim.current::magnus-storage-history"
- source_id: "magnus-storage-history"
- title: "다른 지역 창고 이용 가능"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=9720"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "magnus-remote-storage"
- claim_key: "requirements:magnus-remote-storage"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `magnus-remote-storage.claim.current::remote-storage-sale-history`

- evidence_seed_key: "magnus-remote-storage.claim.current::remote-storage-sale-history"
- source_id: "remote-storage-sale-history"
- title: "다른 마을 창고 아이템 판매"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13871"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "magnus-remote-storage"
- claim_key: "requirements:magnus-remote-storage"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
