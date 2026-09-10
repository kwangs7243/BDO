<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 아이템 획득 증가 주문서

## Identity

- slug: "loot-scroll-system"
- name_ko: "아이템 획득 증가 주문서"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "아이템 획득 증가 주문서 1단계와 2단계는 확률 증가가 같고 수량 증가가 다르다."
- purpose: "주문서 단계별 확률과 수량 효과를 분리해 보존한다."

## Requirements

### `loot-scroll-system.stages`

- seed_key: "loot-scroll-system.stages"
- kind: "item"
- requirement_level: "required"
- title: "주문서 단계"
- description: "1단계와 2단계의 아이템 획득 확률 증가는 같고, 획득 수량 증가는 각각 50%와 100%다."
- structured_value:

```json
{
  "exact_probability_bonus_percent": null,
  "knowledge_role": "fact",
  "same_probability_bonus_between_stages": true,
  "stages": [
    {
      "quantity_bonus_percent": 50,
      "stage": 1
    },
    {
      "quantity_bonus_percent": 100,
      "stage": 2
    }
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

### `loot-scroll-system.drop-system`

- seed_key: "loot-scroll-system.drop-system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "item-drop-rate-system"
- content_name_ko: "아이템 획득 확률 증가 시스템"
- content_category: "combat_pve"
- note: "획득 확률과 수량을 구분하는 대표 소비 효과다."
- order_no: 1
- relative_path: "../contents/item-drop-rate-system.md"

## Evidence and Sources

### Current evidence

### `loot-scroll-system.claim.stages::item-drop-rate-guide`

- evidence_seed_key: "loot-scroll-system.claim.stages::item-drop-rate-guide"
- source_id: "item-drop-rate-guide"
- title: "아이템 획득 확률 증가"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=345"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "loot-scroll-system.stages"
- claim_key: "requirement:loot-scroll-system.stages"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
