<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 아침의 나라 월드 우두머리

## Identity

- slug: "morning-land-world-bosses"
- name_ko: "아침의 나라 월드 우두머리"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "open_world"
- difficulty: "varies"

## Overview

- summary: "과거 주간 의뢰는 종료됐고 현재는 처치 시 직접 전리품을 획득한다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `morning-land-world-bosses.direct-loot`

- seed_key: "morning-land-world-bosses.direct-loot"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 직접 전리품"
- description: "2025-12-23 이후 아침의 나라 월드 우두머리는 주간 의뢰 대신 직접 전리품을 지급한다."
- structured_value:

```json
{
  "direct_loot_current": true,
  "effective_from": "2025-12-23",
  "knowledge_role": "fact",
  "weekly_quest_required": false
}
```

### `morning-land-world-bosses.hp-2026-02-04`

- seed_key: "morning-land-world-bosses.hp-2026-02-04"
- kind: "knowledge"
- requirement_level: "required"
- title: "생명력 조정"
- description: "불가살·우투리·산군·금돼지왕 생명력이 각각 1.5배로 조정되었다."
- structured_value:

```json
{
  "effective_from": "2026-02-04",
  "hp_multiplier": {
    "Bulgasal": 1.5,
    "Golden Pig King": 1.5,
    "Sangoon": 1.5,
    "Uturi": 1.5
  },
  "knowledge_role": "fact"
}
```

### `morning-land-world-bosses.protection-current`

- seed_key: "morning-land-world-bosses.protection-current"
- kind: "knowledge"
- requirement_level: "required"
- title: "등장 보호 최신 상태"
- description: "크자카의 과거 완전 무적과 불가살·우투리의 등장 무적은 비활성화되고 피해 감소 상태로 바뀌었다."
- structured_value:

```json
{
  "bosses": [
    "Kzarka",
    "Bulgasal",
    "Uturi"
  ],
  "current_state": "damage_reduction",
  "knowledge_role": "fact",
  "old_full_invulnerability_active": false
}
```

### `morning-land-world-bosses.sangoon-location`

- seed_key: "morning-land-world-bosses.sangoon-location"
- kind: "knowledge"
- requirement_level: "required"
- title: "산군 등장 위치 개선"
- description: "산군 월드 우두머리의 재등장 위치가 궁궐과 더 가까운 위치로 조정됐다."
- structured_value:

```json
{
  "boss": "Sangoon",
  "effective_from": "2026-02-04",
  "knowledge_role": "fact",
  "respawn_location_change": "closer_to_palace"
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

### `morning-land-world-bosses.current-system`

- seed_key: "morning-land-world-bosses.current-system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "world-boss-current-system"
- content_name_ko: "월드 우두머리 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-current-system.md"

## Evidence and Sources

### Current evidence

### `morning-land-world-bosses.claim.direct-loot::rare-wild-horses-2025-12-23`

- evidence_seed_key: "morning-land-world-bosses.claim.direct-loot::rare-wild-horses-2025-12-23"
- source_id: "rare-wild-horses-2025-12-23"
- title: "12월 23일(화) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14989"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-23"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "morning-land-world-bosses.direct-loot"
- claim_key: "requirement:direct-loot"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `morning-land-world-bosses.claim.hp-2026-02-04::morning-land-boss-balance-2026-02-04`

- evidence_seed_key: "morning-land-world-bosses.claim.hp-2026-02-04::morning-land-boss-balance-2026-02-04"
- source_id: "morning-land-boss-balance-2026-02-04"
- title: "2월 4일 업데이트 안내 - 아침의 나라 우두머리 조정"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15169"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-02-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "morning-land-world-bosses.hp-2026-02-04"
- claim_key: "requirement:hp-2026-02-04"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `morning-land-world-bosses.claim.protection-current::morning-land-boss-balance-2026-02-04`

- evidence_seed_key: "morning-land-world-bosses.claim.protection-current::morning-land-boss-balance-2026-02-04"
- source_id: "morning-land-boss-balance-2026-02-04"
- title: "2월 4일 업데이트 안내 - 아침의 나라 우두머리 조정"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15169"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-02-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "morning-land-world-bosses.protection-current"
- claim_key: "requirement:protection-current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `morning-land-world-bosses.claim.sangoon-location::morning-land-boss-balance-2026-02-04`

- evidence_seed_key: "morning-land-world-bosses.claim.sangoon-location::morning-land-boss-balance-2026-02-04"
- source_id: "morning-land-boss-balance-2026-02-04"
- title: "2월 4일 업데이트 안내 - 아침의 나라 우두머리 조정"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15169"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-02-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "morning-land-world-bosses.sangoon-location"
- claim_key: "requirement:sangoon-location"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `morning-land-world-bosses.claim.legacy-invulnerability::morning-land-boss-balance-2026-02-04`

- evidence_seed_key: "morning-land-world-bosses.claim.legacy-invulnerability::morning-land-boss-balance-2026-02-04"
- source_id: "morning-land-boss-balance-2026-02-04"
- title: "2월 4일 업데이트 안내 - 아침의 나라 우두머리 조정"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15169"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-02-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "morning-land-world-bosses.legacy-invulnerability"
- claim_key: "requirement:legacy-invulnerability"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false

### `morning-land-world-bosses.claim.legacy-weekly-quests::rare-wild-horses-2025-12-23`

- evidence_seed_key: "morning-land-world-bosses.claim.legacy-weekly-quests::rare-wild-horses-2025-12-23"
- source_id: "rare-wild-horses-2025-12-23"
- title: "12월 23일(화) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14989"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-23"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "morning-land-world-bosses.legacy-weekly-quests"
- claim_key: "requirement:legacy-weekly-quests"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
