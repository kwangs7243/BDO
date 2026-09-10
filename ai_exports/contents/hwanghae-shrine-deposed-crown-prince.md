<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 폐세자 (황해도 검은사당)

## Identity

- slug: "hwanghae-shrine-deposed-crown-prince"
- name_ko: "폐세자 (황해도 검은사당)"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "party"
- difficulty: "varies"

## Overview

- summary: "폐세자의 황해도 5인 검은사당 맥락을 다른 동명 우두머리와 분리한 canonical 엔터티."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `hwanghae-shrine-deposed-crown-prince.context`

- seed_key: "hwanghae-shrine-deposed-crown-prince.context"
- kind: "knowledge"
- requirement_level: "required"
- title: "엔터티 맥락"
- description: "황해도 5인 파티 검은사당 우두머리다."
- structured_value:

```json
{
  "boss_name": "폐세자",
  "context": "black_shrine_hwanghae",
  "knowledge_role": "fact",
  "party_size": 5
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

### `hwanghae-shrine-deposed-crown-prince.system`

- seed_key: "hwanghae-shrine-deposed-crown-prince.system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "black-shrine-hwanghae-current-system"
- content_name_ko: "검은사당 황해도 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/black-shrine-hwanghae-current-system.md"
### `hwanghae-current-roster.entity-deposed-crown-prince`

- seed_key: "hwanghae-current-roster.entity-deposed-crown-prince"
- direction: "incoming"
- relation_type: "related"
- content_slug: "hwanghae-current-roster"
- content_name_ko: "황해도 검은사당 현재 명단"
- content_category: "combat_pve"
- note: "폐세자 현재 명단 엔터티"
- order_no: 7
- relative_path: "../contents/hwanghae-current-roster.md"

## Evidence and Sources

### Current evidence

### `hwanghae-shrine-deposed-crown-prince.claim.context::black-shrine-hwanghae-guide`

- evidence_seed_key: "hwanghae-shrine-deposed-crown-prince.claim.context::black-shrine-hwanghae-guide"
- source_id: "black-shrine-hwanghae-guide"
- title: "검은 사당 - 황해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=404"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "hwanghae-shrine-deposed-crown-prince.context"
- claim_key: "requirement:context"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
