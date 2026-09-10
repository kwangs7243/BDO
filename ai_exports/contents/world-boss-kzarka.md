<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 크자카 (월드 우두머리)

## Identity

- slug: "world-boss-kzarka"
- name_ko: "크자카 (월드 우두머리)"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "open_world"
- difficulty: "varies"

## Overview

- summary: "크자카의 월드 우두머리 맥락을 검은사당·필드 우두머리와 분리한 canonical 엔터티."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `world-boss-kzarka.context`

- seed_key: "world-boss-kzarka.context"
- kind: "knowledge"
- requirement_level: "required"
- title: "엔터티 맥락"
- description: "공식 현재 월드 우두머리 명단의 엔터티다."
- structured_value:

```json
{
  "boss_name": "크자카",
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

### `world-boss-kzarka.system`

- seed_key: "world-boss-kzarka.system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "world-boss-current-system"
- content_name_ko: "월드 우두머리 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-current-system.md"
### `world-boss-current-roster.entity-world-boss-kzarka`

- seed_key: "world-boss-current-roster.entity-world-boss-kzarka"
- direction: "incoming"
- relation_type: "related"
- content_slug: "world-boss-current-roster"
- content_name_ko: "월드 우두머리 현재 명단"
- content_category: "combat_pve"
- note: "Kzarka 현재 명단 엔터티"
- order_no: 1
- relative_path: "../contents/world-boss-current-roster.md"

## Evidence and Sources

### Current evidence

### `world-boss-kzarka.claim.context::world-boss-guide`

- evidence_seed_key: "world-boss-kzarka.claim.context::world-boss-guide"
- source_id: "world-boss-guide"
- title: "월드 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=89"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "world-boss-kzarka.context"
- claim_key: "requirement:context"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
