<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 전투 수정 시스템

## Identity

- slug: "combat-crystal-system"
- name_ko: "전투 수정 시스템"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "수정 가방·프리셋·그룹 제한과 장착 수정의 제거 방식을 정리한 현행 시스템이다."
- purpose: "수정 구성과 제거 시 손실 위험을 공식 규칙 기준으로 확인한다."

## Requirements

### `combat-crystal-system.capacity`

- seed_key: "combat-crystal-system.capacity"
- kind: "item"
- requirement_level: "required"
- title: "가방과 프리셋"
- description: "수정 가방 기본 보관 한도는 50개이고 수정 프리셋은 5개까지 저장한다."
- structured_value:

```json
{
  "crystal_bag_capacity": 50,
  "group_limits_apply": true,
  "knowledge_role": "fact",
  "preset_count": 5
}
```

### `combat-crystal-system.removal`

- seed_key: "combat-crystal-system.removal"
- kind: "item"
- requirement_level: "required"
- title: "수정 제거"
- description: "추출 도구로 추출하면 수정이 보존되지만 직접 제거하면 파괴된다."
- structured_value:

```json
{
  "direct_removal_destroys": true,
  "extraction_preserves": true,
  "knowledge_role": "fact"
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

### `pve-crystal-strategy.system`

- seed_key: "pve-crystal-strategy.system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "pve-crystal-strategy"
- content_name_ko: "PvE 수정 구성 전략"
- content_category: "combat_pve"
- note: "수정 시스템의 보관·프리셋·제거 규칙이 전제다."
- order_no: 1
- relative_path: "../contents/pve-crystal-strategy.md"

## Evidence and Sources

### Current evidence

### `combat-crystal-system.claim.capacity::crystal-guide`

- evidence_seed_key: "combat-crystal-system.claim.capacity::crystal-guide"
- source_id: "crystal-guide"
- title: "수정 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=310"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-crystal-system.capacity"
- claim_key: "requirement:combat-crystal-system.capacity"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `combat-crystal-system.claim.removal::crystal-guide`

- evidence_seed_key: "combat-crystal-system.claim.removal::crystal-guide"
- source_id: "crystal-guide"
- title: "수정 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=310"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-crystal-system.removal"
- claim_key: "requirement:combat-crystal-system.removal"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `combat-crystal-system.claim.no-break-event::crystal-guide`

- evidence_seed_key: "combat-crystal-system.claim.no-break-event::crystal-guide"
- source_id: "crystal-guide"
- title: "수정 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=310"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-crystal-system.no-break-event"
- claim_key: "temporary:no-crystal-break-event"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
