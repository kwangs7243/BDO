<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# [데키아] 가이핀라시아 사원 지상

## Identity

- slug: "dehkia-gyfin-upper"
- name_ko: "[데키아] 가이핀라시아 사원 지상"
- category: "combat"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "party"
- difficulty: "very_high"

## Overview

- summary: "3인 파티용 데키아 가이핀라시아 사원 지상."
- purpose: "데키아 유물과 데보레카 허리띠 계열 획득"

## Requirements

### `dehkia-gyfin-upper.current-stats`

- seed_key: "dehkia-gyfin-upper.current-stats"
- kind: "stat"
- requirement_level: "recommended"
- title: "현재 권장 수치"
- description: "표기 공격력 370/방어력 440, 최종 공격력 1650/방어력 715, 공격력 상한 1680."
- structured_value:

```json
{
  "ap_cap": 1680,
  "final_ap_recommended": 1650,
  "final_dp_recommended": 715,
  "knowledge_role": "fact",
  "party_size": 3,
  "sheet_ap_recommended": 370,
  "sheet_dp_recommended": 440
}
```

### `dehkia-gyfin-upper.loot`

- seed_key: "dehkia-gyfin-upper.loot"
- kind: "item"
- requirement_level: "optional"
- title: "잡동사니와 주요 전리품"
- description: "잠식된 청동 조각 가격과 주요 전리품."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "major_loot": [
    "Dehkia Artifact",
    "Deboreka Belt",
    "Whisper stained by Void",
    "Forgotten Oblivion Box"
  ],
  "trash_item": "잠식된 청동 조각",
  "trash_npc_price": 125900
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

### `dehkia-gyfin-upper.attack-cap`

- seed_key: "dehkia-gyfin-upper.attack-cap"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-zone-attack-cap"
- content_name_ko: "사냥터 공격력 제한"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/grind-zone-attack-cap.md"

## Evidence and Sources

### Current evidence

### `dehkia-gyfin-upper.claim.current-stats::dehkia-party-spots-2026-01-14`

- evidence_seed_key: "dehkia-gyfin-upper.claim.current-stats::dehkia-party-spots-2026-01-14"
- source_id: "dehkia-party-spots-2026-01-14"
- title: "1월 14일(수) 업데이트 안내 - 데키아의 등불 파티 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15070"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-01-14"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "dehkia-gyfin-upper.current-stats"
- claim_key: "requirement:current-stats"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `dehkia-gyfin-upper.claim.loot::dehkia-party-spots-2026-01-14`

- evidence_seed_key: "dehkia-gyfin-upper.claim.loot::dehkia-party-spots-2026-01-14"
- source_id: "dehkia-party-spots-2026-01-14"
- title: "1월 14일(수) 업데이트 안내 - 데키아의 등불 파티 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15070"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-01-14"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "dehkia-gyfin-upper.loot"
- claim_key: "requirement:loot"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
