<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 아이템 획득 확률 증가 상한

## Identity

- slug: "item-drop-rate-cap"
- name_ko: "아이템 획득 확률 증가 상한"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "현행 전체 아이템 획득 확률 증가 상한과 일반 적용 상한을 구분한다."
- purpose: "과거 300% 전체 상한을 현행 규칙으로 잘못 사용하지 않는다."

## Requirements

### `item-drop-rate-cap.current`

- seed_key: "item-drop-rate-cap.current"
- kind: "stat"
- requirement_level: "required"
- title: "현행 상한"
- description: "전체 상한은 400%이며 일반적으로 적용되는 상한은 300%다."
- structured_value:

```json
{
  "content_exceptions_may_apply": true,
  "knowledge_role": "fact",
  "ordinary_cap_percent": 300,
  "overall_cap_percent": 400
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

### `item-drop-rate-cap.system`

- seed_key: "item-drop-rate-cap.system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "item-drop-rate-system"
- content_name_ko: "아이템 획득 확률 증가 시스템"
- content_category: "combat_pve"
- note: "아이템 획득 확률 증가의 상한 규칙이다."
- order_no: 1
- relative_path: "../contents/item-drop-rate-system.md"

## Evidence and Sources

### Current evidence

### `item-drop-rate-cap.claim.current::item-drop-benefits-history`

- evidence_seed_key: "item-drop-rate-cap.claim.current::item-drop-benefits-history"
- source_id: "item-drop-benefits-history"
- title: "아이템 획득 확률 증가 효과 변경 이력"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=8461"
- publisher: "Pearl Abyss"
- source_type: "official_history"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "item-drop-rate-cap.current"
- claim_key: "requirement:item-drop-rate-cap.current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `item-drop-rate-cap.claim.current::item-drop-rate-guide`

- evidence_seed_key: "item-drop-rate-cap.claim.current::item-drop-rate-guide"
- source_id: "item-drop-rate-guide"
- title: "아이템 획득 확률 증가"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=345"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "item-drop-rate-cap.current"
- claim_key: "requirement:item-drop-rate-cap.current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `item-drop-rate-cap.claim.legacy::item-drop-benefits-history`

- evidence_seed_key: "item-drop-rate-cap.claim.legacy::item-drop-benefits-history"
- source_id: "item-drop-benefits-history"
- title: "아이템 획득 확률 증가 효과 변경 이력"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=8461"
- publisher: "Pearl Abyss"
- source_type: "official_history"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "item-drop-rate-cap.legacy"
- claim_key: "legacy:item-drop-overall-cap-300"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
