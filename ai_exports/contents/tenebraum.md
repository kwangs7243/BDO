<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 테네브라움 성

## Identity

- slug: "tenebraum"
- name_ko: "테네브라움 성"
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

### `tenebraum.progression`

- seed_key: "tenebraum.progression"
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
  "progression_order": 4
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

### `tenebraum.previous`

- seed_key: "tenebraum.previous"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "orbita"
- content_name_ko: "오르비타 성"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/orbita.md"
### `tenebraum.next`

- seed_key: "tenebraum.next"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "zephyros"
- content_name_ko: "제피로스 성"
- content_category: "combat"
- note: null
- order_no: 2
- relative_path: "../contents/zephyros.md"
### `zephyros.previous`

- seed_key: "zephyros.previous"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "zephyros"
- content_name_ko: "제피로스 성"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/zephyros.md"
### `orbita.next`

- seed_key: "orbita.next"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "orbita"
- content_name_ko: "오르비타 성"
- content_category: "combat"
- note: null
- order_no: 2
- relative_path: "../contents/orbita.md"

## Evidence and Sources

### Current evidence

### `tenebraum.claim.progression::edania-external-history-2026-09-04`

- evidence_seed_key: "tenebraum.claim.progression::edania-external-history-2026-09-04"
- source_id: "edania-external-history-2026-09-04"
- title: "에다니아 외부 사냥터 업데이트 히스토리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?groupMasterNo=14463"
- publisher: "Pearl Abyss"
- source_type: "official_history"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "tenebraum.progression"
- claim_key: "requirement:progression"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
