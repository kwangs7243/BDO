<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 전투 광명석

## Identity

- slug: "combat-lightstones"
- name_ko: "전투 광명석"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "전투 광명석은 유물 슬롯에 장착하고 네 개의 조합으로 추가 효과를 구성한다."
- purpose: "광명석 단품 효과와 네 슬롯 조합 효과를 구분한다."

## Requirements

### `combat-lightstones.system`

- seed_key: "combat-lightstones.system"
- kind: "item"
- requirement_level: "required"
- title: "광명석 장착과 조합"
- description: "총 4개의 광명석을 두 유물에 장착하며 지정 조합은 별도 조합 효과를 활성화할 수 있다."
- structured_value:

```json
{
  "combination_effects_exist": true,
  "knowledge_role": "fact",
  "single_effect_separate_from_combination": true,
  "total_slots": 4
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

### `combat-lightstones.artifacts`

- seed_key: "combat-lightstones.artifacts"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "combat-artifacts"
- content_name_ko: "전투 유물"
- content_category: "combat_pve"
- note: "전투 유물의 네 광명석 슬롯에 장착한다."
- order_no: 1
- relative_path: "../contents/combat-artifacts.md"
### `pve-lightstone-strategy.system`

- seed_key: "pve-lightstone-strategy.system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "pve-lightstone-strategy"
- content_name_ko: "PvE 광명석 조합 전략"
- content_category: "combat_pve"
- note: "광명석 장착 및 조합 구조가 전제다."
- order_no: 1
- relative_path: "../contents/pve-lightstone-strategy.md"

## Evidence and Sources

### Current evidence

### `combat-lightstones.claim.system::artifact-guide`

- evidence_seed_key: "combat-lightstones.claim.system::artifact-guide"
- source_id: "artifact-guide"
- title: "유물/광명석"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=272"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-lightstones.system"
- claim_key: "requirement:combat-lightstones.system"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
