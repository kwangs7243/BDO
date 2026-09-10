<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 야영지 전투 버프

## Identity

- slug: "camp-combat-buffs"
- name_ko: "야영지 전투 버프"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "야영지에서 구매하는 전투 버프는 교회·소모품 버프와 별도 출처로 관리한다."
- purpose: "야영지 버프를 다른 버프 묶음과 혼동하지 않고 현행 공식 안내에 연결한다."

## Requirements

### `camp-combat-buffs.separate-source`

- seed_key: "camp-combat-buffs.separate-source"
- kind: "other"
- requirement_level: "required"
- title: "별도 버프 출처"
- description: "야영지 상점 전투 버프는 교회 버프 및 음식·비약과 별도의 구매·적용 항목이다."
- structured_value:

```json
{
  "exact_effects_in_this_seed": false,
  "knowledge_role": "fact",
  "separate_from": [
    "church",
    "food",
    "elixir",
    "perfume"
  ],
  "source": "camp_shop"
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

### `camp-combat-buffs.foundation`

- seed_key: "camp-combat-buffs.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "combat-buff-foundation"
- content_name_ko: "전투 버프 기초"
- content_category: "combat_pve"
- note: "전투 버프의 야영지 항목이다."
- order_no: 1
- relative_path: "../contents/combat-buff-foundation.md"

## Evidence and Sources

### Current evidence

### `camp-combat-buffs.claim.separate-source::camp-church-rework-2025-12-30`

- evidence_seed_key: "camp-combat-buffs.claim.separate-source::camp-church-rework-2025-12-30"
- source_id: "camp-church-rework-2025-12-30"
- title: "2025년 12월 30일 야영지 및 교회 버프 개편"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15012"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-30"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "camp-combat-buffs.separate-source"
- claim_key: "requirement:camp-combat-buffs.separate-source"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
