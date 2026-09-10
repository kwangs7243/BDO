<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# [데키아] 미루목 유적지

## Identity

- slug: "dehkia-miru"
- name_ko: "[데키아] 미루목 유적지"
- category: "combat"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "party"
- difficulty: "very_high"

## Overview

- summary: "3인 파티용 데키아 미루목 유적지."
- purpose: "데키아 유물과 데보레카 허리띠 계열 획득"

## Requirements

### `dehkia-miru.current-stats`

- seed_key: "dehkia-miru.current-stats"
- kind: "stat"
- requirement_level: "recommended"
- title: "현재 권장 수치"
- description: "표기 공격력 350/방어력 427, 최종 공격력 1565/방어력 615, 공격력 상한 1595."
- structured_value:

```json
{
  "ap_cap": 1595,
  "final_ap_recommended": 1565,
  "final_dp_recommended": 615,
  "knowledge_role": "fact",
  "party_size": 3,
  "sheet_ap_recommended": 350,
  "sheet_dp_recommended": 427
}
```

### `dehkia-miru.loot`

- seed_key: "dehkia-miru.loot"
- kind: "item"
- requirement_level: "optional"
- title: "잡동사니와 주요 전리품"
- description: "잠식된 나무 조각 가격과 주요 전리품."
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
  "trash_item": "잠식된 나무 조각",
  "trash_npc_price": 101500
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

### `dehkia-miru.attack-cap`

- seed_key: "dehkia-miru.attack-cap"
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

### `dehkia-miru.claim.flow::dehkia-flow-update-2026-01-28`

- evidence_seed_key: "dehkia-miru.claim.flow::dehkia-flow-update-2026-01-28"
- source_id: "dehkia-flow-update-2026-01-28"
- title: "1월 28일(수) 업데이트 안내 - 데키아 사냥터 흐름 개선"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15136"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-01-28"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "dehkia-miru"
- claim_key: "patch:flow"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `dehkia-miru.claim.current-stats::dehkia-party-spots-2026-01-14`

- evidence_seed_key: "dehkia-miru.claim.current-stats::dehkia-party-spots-2026-01-14"
- source_id: "dehkia-party-spots-2026-01-14"
- title: "1월 14일(수) 업데이트 안내 - 데키아의 등불 파티 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15070"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-01-14"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "dehkia-miru.current-stats"
- claim_key: "requirement:current-stats"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `dehkia-miru.claim.loot::dehkia-party-spots-2026-01-14`

- evidence_seed_key: "dehkia-miru.claim.loot::dehkia-party-spots-2026-01-14"
- source_id: "dehkia-party-spots-2026-01-14"
- title: "1월 14일(수) 업데이트 안내 - 데키아의 등불 파티 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15070"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-01-14"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "dehkia-miru.loot"
- claim_key: "requirement:loot"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
