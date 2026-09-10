<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 아에테리온 성

## Identity

- slug: "aetherion"
- name_ko: "아에테리온 성"
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

### `aetherion.progression`

- seed_key: "aetherion.progression"
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
  "progression_order": 1,
  "sheet_ap_recommended": 350,
  "sheet_dp_recommended": 427
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

### `aetherion.next`

- seed_key: "aetherion.next"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "nymphamare"
- content_name_ko: "님파마레 성"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/nymphamare.md"
### `nymphamare.previous`

- seed_key: "nymphamare.previous"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "nymphamare"
- content_name_ko: "님파마레 성"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/nymphamare.md"

## Evidence and Sources

### Current evidence

### `aetherion.claim.progression::edania-external-history-2026-09-04`

- evidence_seed_key: "aetherion.claim.progression::edania-external-history-2026-09-04"
- source_id: "edania-external-history-2026-09-04"
- title: "에다니아 외부 사냥터 업데이트 히스토리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?groupMasterNo=14463"
- publisher: "Pearl Abyss"
- source_type: "official_history"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "aetherion.progression"
- claim_key: "requirement:progression"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
