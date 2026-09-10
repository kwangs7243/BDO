<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 일꾼 특송

## Identity

- slug: "worker-special-delivery"
- name_ko: "일꾼 특송"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "2025년 1월 22일 이후 모든 일꾼은 1레벨부터 특송을 기본 보유하며 생산거점 결과물을 받을 마을 창고를 선택할 수 있다."
- purpose: "생산 결과물 목적지 선택을 공방 재료·일반 수송과 구분한다."

## Requirements

### `worker-special-delivery.current-level`

- seed_key: "worker-special-delivery.current-level"
- kind: "level"
- requirement_level: "required"
- title: "현재 특송 습득 레벨"
- description: "모든 일꾼이 1레벨부터 기본 보유한다."
- structured_value:

```json
{
  "all_workers": true,
  "basic_skill": true,
  "level": 1
}
```

### `worker-special-delivery.destination`

- seed_key: "worker-special-delivery.destination"
- kind: "other"
- requirement_level: "required"
- title: "결과물 목적지"
- description: "생산거점 작업 시작 시 결과물을 받을 마을 창고를 선택한다."
- structured_value:

```json
{
  "applies_to": "production_node_output",
  "changes_workshop_material_source": false,
  "destination_town_storage_selectable": true
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

### `worker-special-delivery.production`

- seed_key: "worker-special-delivery.production"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "production-node-current-system"
- content_name_ko: "생산 거점 현재 시스템"
- content_category: "life"
- note: "특송은 생산거점 결과물 물류다."
- order_no: 1
- relative_path: "../contents/production-node-current-system.md"
### `worker-special-delivery.workshop-distinction`

- seed_key: "worker-special-delivery.workshop-distinction"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "workshop-crafting-logistics"
- content_name_ko: "공방 제작 물류"
- content_category: "life"
- note: "공방 재료 창고 규칙과는 별개다."
- order_no: 2
- relative_path: "../contents/workshop-crafting-logistics.md"
### `worker-special-delivery.transport-distinction`

- seed_key: "worker-special-delivery.transport-distinction"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "storage-transport"
- content_name_ko: "일반 창고 수송"
- content_category: "life"
- note: "일반 창고 수송과는 별개다."
- order_no: 3
- relative_path: "../contents/storage-transport.md"
### `production-node-current-system.special-delivery`

- seed_key: "production-node-current-system.special-delivery"
- direction: "incoming"
- relation_type: "related"
- content_slug: "production-node-current-system"
- content_name_ko: "생산 거점 현재 시스템"
- content_category: "life"
- note: "생산 결과 창고 선택은 일꾼 특송 기능이다."
- order_no: 1
- relative_path: "../contents/production-node-current-system.md"
### `storage-transport.special-delivery`

- seed_key: "storage-transport.special-delivery"
- direction: "incoming"
- relation_type: "related"
- content_slug: "storage-transport"
- content_name_ko: "일반 창고 수송"
- content_category: "life"
- note: "일반 town-to-town 수송은 생산 특송과 별개다."
- order_no: 2
- relative_path: "../contents/storage-transport.md"
### `workshop-crafting-logistics.special-delivery`

- seed_key: "workshop-crafting-logistics.special-delivery"
- direction: "incoming"
- relation_type: "related"
- content_slug: "workshop-crafting-logistics"
- content_name_ko: "공방 제작 물류"
- content_category: "life"
- note: "생산 특송과 구분되는 물류다."
- order_no: 3
- relative_path: "../contents/workshop-crafting-logistics.md"

## Evidence and Sources

### Current evidence

### `worker-special-delivery.claim.current::worker-convenience-2025-01-22`

- evidence_seed_key: "worker-special-delivery.claim.current::worker-convenience-2025-01-22"
- source_id: "worker-convenience-2025-01-22"
- title: "1월 22일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13457"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-22"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-special-delivery"
- claim_key: "requirements:worker-special-delivery"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `worker-special-delivery.claim.current::worker-guide`

- evidence_seed_key: "worker-special-delivery.claim.current::worker-guide"
- source_id: "worker-guide"
- title: "일꾼"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=95"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-special-delivery"
- claim_key: "requirements:worker-special-delivery"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `worker-special-delivery.claim.legacy-level-40::worker-convenience-2025-01-22`

- evidence_seed_key: "worker-special-delivery.claim.legacy-level-40::worker-convenience-2025-01-22"
- source_id: "worker-convenience-2025-01-22"
- title: "1월 22일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13457"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-22"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-special-delivery"
- claim_key: "legacy:special-delivery-requires-level-40"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false

### `worker-special-delivery.claim.legacy-level-40::worker-overhaul-2023-05-24`

- evidence_seed_key: "worker-special-delivery.claim.legacy-level-40::worker-overhaul-2023-05-24"
- source_id: "worker-overhaul-2023-05-24"
- title: "5월 24일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=10369"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-05-24"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-special-delivery"
- claim_key: "legacy:special-delivery-requires-level-40"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
