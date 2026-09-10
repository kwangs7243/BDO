<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 검은 봉황 (월드 우두머리)

## Identity

- slug: "world-boss-black-phoenix"
- name_ko: "검은 봉황 (월드 우두머리)"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "open_world"
- difficulty: "varies"

## Overview

- summary: "2026-08-05 라이브된 월드 우두머리로, 정해진 아침의 나라 우두머리 시간에 확률적으로 대체 등장한다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `world-boss-black-phoenix.current`

- seed_key: "world-boss-black-phoenix.current"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 라이브 상태"
- description: "별도 고정 시간표가 아니라 산군·우투리·불가살·금돼지왕 예정 시간에 정해진 확률로 대체 등장한다."
- structured_value:

```json
{
  "effective_from": "2026-08-05",
  "knowledge_role": "fact",
  "live": true,
  "replacement_mechanic": true,
  "replaces": [
    "Sangoon",
    "Uturi",
    "Bulgasal",
    "Golden Pig King"
  ],
  "separate_schedule": false
}
```

### `world-boss-black-phoenix.loot`

- seed_key: "world-boss-black-phoenix.loot"
- kind: "knowledge"
- requirement_level: "required"
- title: "주요 전리품 범주"
- description: "공식 업데이트에 안내된 전리품 범주를 현재 보상으로 관리한다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "loot_categories": [
    "Black Phoenix specific loot",
    "boss crystals and aura materials",
    "enhancement and marketable materials"
  ]
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

### `world-boss-black-phoenix.current-system`

- seed_key: "world-boss-black-phoenix.current-system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "world-boss-current-system"
- content_name_ko: "월드 우두머리 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-current-system.md"
### `world-boss-black-phoenix.shrine-distinction`

- seed_key: "world-boss-black-phoenix.shrine-distinction"
- direction: "outgoing"
- relation_type: "alternative"
- content_slug: "hwanghae-shrine-dark-bonghwang"
- content_name_ko: "흑봉황 (황해도 검은사당)"
- content_category: "combat_pve"
- note: "검은사당 흑봉황과 맥락이 다른 별도 엔터티다."
- order_no: 2
- relative_path: "../contents/hwanghae-shrine-dark-bonghwang.md"
### `world-boss-current-roster.entity-world-boss-black-phoenix`

- seed_key: "world-boss-current-roster.entity-world-boss-black-phoenix"
- direction: "incoming"
- relation_type: "related"
- content_slug: "world-boss-current-roster"
- content_name_ko: "월드 우두머리 현재 명단"
- content_category: "combat_pve"
- note: "Black Phoenix 현재 명단 엔터티"
- order_no: 14
- relative_path: "../contents/world-boss-current-roster.md"

## Evidence and Sources

### Current evidence

### `world-boss-black-phoenix.claim.current::world-boss-guide`

- evidence_seed_key: "world-boss-black-phoenix.claim.current::world-boss-guide"
- source_id: "world-boss-guide"
- title: "월드 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=89"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "world-boss-black-phoenix.current"
- claim_key: "requirement:current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `world-boss-black-phoenix.claim.loot::world-boss-guide`

- evidence_seed_key: "world-boss-black-phoenix.claim.loot::world-boss-guide"
- source_id: "world-boss-guide"
- title: "월드 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=89"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "world-boss-black-phoenix.loot"
- claim_key: "requirement:loot"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
