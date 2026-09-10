<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 전투 유물

## Identity

- slug: "combat-artifacts"
- name_ko: "전투 유물"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "두 개의 유물과 유물당 두 개의 광명석 슬롯으로 전투 능력치를 구성한다."
- purpose: "전투 유물의 장착 구조와 대표 현행 수치를 검증한다."

## Requirements

### `combat-artifacts.slots`

- seed_key: "combat-artifacts.slots"
- kind: "item"
- requirement_level: "required"
- title: "유물 장착 구조"
- description: "유물은 2개를 장착하며 각 유물에는 광명석 2개, 총 4개를 장착한다."
- structured_value:

```json
{
  "artifact_slots": 2,
  "knowledge_role": "fact",
  "lightstone_sockets_per_artifact": 2,
  "total_lightstone_sockets": 4
}
```

### `combat-artifacts.kabua`

- seed_key: "combat-artifacts.kabua"
- kind: "item"
- requirement_level: "optional"
- title: "카부아의 유물"
- description: "카부아의 유물은 공격력 7, 적중력 20, 최대 생명력 100, 최대 지구력 75를 제공한다."
- structured_value:

```json
{
  "accuracy": 20,
  "ap": 7,
  "item": "카부아의 유물",
  "knowledge_role": "fact",
  "max_hp": 100,
  "max_stamina": 75
}
```

### `combat-artifacts.guiding`

- seed_key: "combat-artifacts.guiding"
- kind: "item"
- requirement_level: "optional"
- title: "인도하는 불빛 유물"
- description: "인도하는 불빛 유물의 대표 전투 수치는 추가 공격력 3, 적중력 5, 최대 생명력 250이다."
- structured_value:

```json
{
  "accuracy": 5,
  "extra_ap": 3,
  "item_family": "인도하는 불빛",
  "knowledge_role": "fact",
  "max_hp": 250
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

### `combat-artifacts.life-system`

- seed_key: "combat-artifacts.life-system"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-artifacts-lightstones"
- content_name_ko: "생활 유물과 광명석"
- content_category: "life"
- note: "생활 유물과 같은 장착 기반을 쓰지만 전투 수치와 조합을 별도 관리한다."
- order_no: 1
- relative_path: "../contents/life-artifacts-lightstones.md"
### `combat-lightstones.artifacts`

- seed_key: "combat-lightstones.artifacts"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "combat-lightstones"
- content_name_ko: "전투 광명석"
- content_category: "combat_pve"
- note: "전투 유물의 네 광명석 슬롯에 장착한다."
- order_no: 1
- relative_path: "../contents/combat-lightstones.md"

## Evidence and Sources

### Current evidence

### `combat-artifacts.claim.guiding::artifact-guide`

- evidence_seed_key: "combat-artifacts.claim.guiding::artifact-guide"
- source_id: "artifact-guide"
- title: "유물/광명석"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=272"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-artifacts.guiding"
- claim_key: "requirement:combat-artifacts.guiding"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `combat-artifacts.claim.kabua::artifact-guide`

- evidence_seed_key: "combat-artifacts.claim.kabua::artifact-guide"
- source_id: "artifact-guide"
- title: "유물/광명석"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=272"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-artifacts.kabua"
- claim_key: "requirement:combat-artifacts.kabua"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `combat-artifacts.claim.slots::artifact-guide`

- evidence_seed_key: "combat-artifacts.claim.slots::artifact-guide"
- source_id: "artifact-guide"
- title: "유물/광명석"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=272"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-artifacts.slots"
- claim_key: "requirement:combat-artifacts.slots"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
