<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 금돼지왕 (월드 우두머리)

## Identity

- slug: "world-boss-golden-pig-king"
- name_ko: "금돼지왕 (월드 우두머리)"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "open_world"
- difficulty: "varies"

## Overview

- summary: "금돼지왕의 월드 우두머리 맥락을 검은사당·필드 우두머리와 분리한 canonical 엔터티."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `world-boss-golden-pig-king.context`

- seed_key: "world-boss-golden-pig-king.context"
- kind: "knowledge"
- requirement_level: "required"
- title: "엔터티 맥락"
- description: "공식 현재 월드 우두머리 명단의 엔터티다."
- structured_value:

```json
{
  "boss_name": "금돼지왕",
  "context": "world_boss",
  "current_roster": true,
  "knowledge_role": "fact"
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

### `world-boss-golden-pig-king.system`

- seed_key: "world-boss-golden-pig-king.system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "world-boss-current-system"
- content_name_ko: "월드 우두머리 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-current-system.md"
### `world-boss-current-roster.entity-world-boss-golden-pig-king`

- seed_key: "world-boss-current-roster.entity-world-boss-golden-pig-king"
- direction: "incoming"
- relation_type: "related"
- content_slug: "world-boss-current-roster"
- content_name_ko: "월드 우두머리 현재 명단"
- content_category: "combat_pve"
- note: "Golden Pig King 현재 명단 엔터티"
- order_no: 11
- relative_path: "../contents/world-boss-current-roster.md"

## Evidence and Sources

### Current evidence

### `world-boss-golden-pig-king.claim.context::world-boss-guide`

- evidence_seed_key: "world-boss-golden-pig-king.claim.context::world-boss-guide"
- source_id: "world-boss-guide"
- title: "월드 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=89"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "world-boss-golden-pig-king.context"
- claim_key: "requirement:context"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
