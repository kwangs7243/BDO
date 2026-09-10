<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 님파마레 성

## Identity

- slug: "nymphamare"
- name_ko: "님파마레 성"
- category: "combat"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "very_high"

## Overview

- summary: "에다니아 외부 사냥터 진행 순서의 한 구간."
- purpose: "에다니아 외부 성장 및 전리품 획득"

## Requirements

### `nymphamare.progression`

- seed_key: "nymphamare.progression"
- kind: "stat"
- requirement_level: "recommended"
- title: "외부 진행 순서와 확인된 수치"
- description: "공식 업데이트 히스토리의 외부 진행 순서와 직접 확인된 권장 수치만 저장한다."
- structured_value:

```json
{
  "current_as_of": "2026-09-04",
  "knowledge_role": "fact",
  "progression_group": "edania_external",
  "progression_order": 2,
  "sheet_ap_recommended": 375,
  "sheet_dp_recommended": 440
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

### `nymphamare.previous`

- seed_key: "nymphamare.previous"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "aetherion"
- content_name_ko: "아에테리온 성"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/aetherion.md"
### `nymphamare.next`

- seed_key: "nymphamare.next"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "orbita"
- content_name_ko: "오르비타 성"
- content_category: "combat"
- note: null
- order_no: 2
- relative_path: "../contents/orbita.md"
### `aetherion.next`

- seed_key: "aetherion.next"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "aetherion"
- content_name_ko: "아에테리온 성"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/aetherion.md"
### `orbita.previous`

- seed_key: "orbita.previous"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "orbita"
- content_name_ko: "오르비타 성"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/orbita.md"

## Evidence and Sources

### Current evidence

### `nymphamare.claim.progression::edania-external-history-2026-09-04`

- evidence_seed_key: "nymphamare.claim.progression::edania-external-history-2026-09-04"
- source_id: "edania-external-history-2026-09-04"
- title: "에다니아 외부 사냥터 업데이트 히스토리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?groupMasterNo=14463"
- publisher: "Pearl Abyss"
- source_type: "official_history"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "nymphamare.progression"
- claim_key: "requirement:progression"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
