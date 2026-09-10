<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# [데키아 II] 잿빛 숲

## Identity

- slug: "dehkia-ash-ii"
- name_ko: "[데키아 II] 잿빛 숲"
- category: "combat"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "very_high"

## Overview

- summary: "데키아의 등불 2단계 사냥터."
- purpose: "데키아 고단계 전리품 획득"

## Requirements

### `dehkia-ash-ii.current-stats`

- seed_key: "dehkia-ash-ii.current-stats"
- kind: "stat"
- requirement_level: "recommended"
- title: "현재 권장 수치"
- description: "표기 공격력 345, 공격력 상한 1540."
- structured_value:

```json
{
  "ap_cap": 1540,
  "knowledge_role": "fact",
  "sheet_ap_recommended": 345
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

### `dehkia-ash-ii.attack-cap`

- seed_key: "dehkia-ash-ii.attack-cap"
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

### `dehkia-ash-ii.claim.current-stats::combat-system-rework-2025-07-23`

- evidence_seed_key: "dehkia-ash-ii.claim.current-stats::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "dehkia-ash-ii.current-stats"
- claim_key: "requirement:current-stats"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
