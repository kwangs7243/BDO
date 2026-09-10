<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 금돼지굴

## Identity

- slug: "golden-pig-cave"
- name_ko: "금돼지굴"
- category: "combat"
- status: "active"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "very_high"

## Overview

- summary: "태초의 결정을 사용해 제한 시간 동안 진행하는 상시 사냥터."
- purpose: "금돼지굴 전리품 획득"

## Requirements

### `golden-pig-cave.current-stats`

- seed_key: "golden-pig-cave.current-stats"
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

### `golden-pig-cave.entry-session`

- seed_key: "golden-pig-cave.entry-session"
- kind: "item"
- requirement_level: "required"
- title: "입장과 세션 규칙"
- description: "문식에게 태초의 결정 1개를 사용하며 세션은 25분이다."
- structured_value:

```json
{
  "death_penalties_apply": true,
  "ejection_conditions_exist": true,
  "entry_item": "태초의 결정",
  "entry_item_amount": 1,
  "knowledge_role": "fact",
  "npc": "문식",
  "session_minutes": 25
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

### `golden-pig-cave.attack-cap`

- seed_key: "golden-pig-cave.attack-cap"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-zone-attack-cap"
- content_name_ko: "사냥터 공격력 제한"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/grind-zone-attack-cap.md"
### `golden-pig-cave.lucky`

- seed_key: "golden-pig-cave.lucky"
- direction: "outgoing"
- relation_type: "alternative"
- content_slug: "lucky-golden-pig-cave"
- content_name_ko: "행운의 금돼지굴"
- content_category: "combat"
- note: null
- order_no: 2
- relative_path: "../contents/lucky-golden-pig-cave.md"
### `lucky-golden-pig-cave.standard`

- seed_key: "lucky-golden-pig-cave.standard"
- direction: "incoming"
- relation_type: "alternative"
- content_slug: "lucky-golden-pig-cave"
- content_name_ko: "행운의 금돼지굴"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/lucky-golden-pig-cave.md"

## Evidence and Sources

### Current evidence

### `golden-pig-cave.claim.current-stats::combat-system-rework-2025-07-23`

- evidence_seed_key: "golden-pig-cave.claim.current-stats::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "golden-pig-cave.current-stats"
- claim_key: "requirement:current-stats"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `golden-pig-cave.claim.entry-session::v17b-provided-measurement-pack-2026-09-04`

- evidence_seed_key: "golden-pig-cave.claim.entry-session::v17b-provided-measurement-pack-2026-09-04"
- source_id: "v17b-provided-measurement-pack-2026-09-04"
- title: "V1.7B Grind Spot Deep Pack - provided measurement records"
- url: "attachment://b902d37c-2b3b-4e3e-b4f3-7c1ccf094a0c/pasted-text.txt"
- publisher: "User-provided research pack"
- source_type: "community_measurement"
- published_at: "2026-09-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "golden-pig-cave.entry-session"
- claim_key: "requirement:entry-session"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `golden-pig-cave.claim.legacy-release-stats::v17b-provided-measurement-pack-2026-09-04`

- evidence_seed_key: "golden-pig-cave.claim.legacy-release-stats::v17b-provided-measurement-pack-2026-09-04"
- source_id: "v17b-provided-measurement-pack-2026-09-04"
- title: "V1.7B Grind Spot Deep Pack - provided measurement records"
- url: "attachment://b902d37c-2b3b-4e3e-b4f3-7c1ccf094a0c/pasted-text.txt"
- publisher: "User-provided research pack"
- source_type: "community_measurement"
- published_at: "2026-09-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "golden-pig-cave.legacy-release-stats"
- claim_key: "requirement:legacy-release-stats"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
