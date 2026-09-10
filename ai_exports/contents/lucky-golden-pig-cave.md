<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 행운의 금돼지굴

## Identity

- slug: "lucky-golden-pig-cave"
- name_ko: "행운의 금돼지굴"
- category: "combat"
- status: "active"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "very_high"

## Overview

- summary: "일반 금돼지굴과 분리하는 잭팟·특수 변형."
- purpose: "특수 금돼지굴 보상 기회"

## Requirements

### `lucky-golden-pig-cave.variant`

- seed_key: "lucky-golden-pig-cave.variant"
- kind: "knowledge"
- requirement_level: "optional"
- title: "특수 변형"
- description: "일반 상시 금돼지굴과 합치지 않는 잭팟 변형."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "separate_from_standard": true,
  "variant_type": "jackpot_special"
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

### `lucky-golden-pig-cave.standard`

- seed_key: "lucky-golden-pig-cave.standard"
- direction: "outgoing"
- relation_type: "alternative"
- content_slug: "golden-pig-cave"
- content_name_ko: "금돼지굴"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/golden-pig-cave.md"
### `golden-pig-cave.lucky`

- seed_key: "golden-pig-cave.lucky"
- direction: "incoming"
- relation_type: "alternative"
- content_slug: "golden-pig-cave"
- content_name_ko: "금돼지굴"
- content_category: "combat"
- note: null
- order_no: 2
- relative_path: "../contents/golden-pig-cave.md"

## Evidence and Sources

### Current evidence

### `lucky-golden-pig-cave.claim.variant::v17b-provided-measurement-pack-2026-09-04`

- evidence_seed_key: "lucky-golden-pig-cave.claim.variant::v17b-provided-measurement-pack-2026-09-04"
- source_id: "v17b-provided-measurement-pack-2026-09-04"
- title: "V1.7B Grind Spot Deep Pack - provided measurement records"
- url: "attachment://b902d37c-2b3b-4e3e-b4f3-7c1ccf094a0c/pasted-text.txt"
- publisher: "User-provided research pack"
- source_type: "community_measurement"
- published_at: "2026-09-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "lucky-golden-pig-cave.variant"
- claim_key: "requirement:variant"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
