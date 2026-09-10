<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 동해도 하이퍼 부스트 방어구 지원

## Identity

- slug: "donghae-hyperboost-armor-support"
- name_ko: "동해도 하이퍼 부스트 방어구 지원"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "varies"

## Overview

- summary: "지원 의뢰의 공격력 조건과 실제 우두머리 입장 조건을 별도 값으로 관리한다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `donghae-hyperboost-armor-support.conditions`

- seed_key: "donghae-hyperboost-armor-support.conditions"
- kind: "knowledge"
- requirement_level: "required"
- title: "지원 의뢰 조건"
- description: "각 조건을 만족해 지정 우두머리를 처치하면 방어구 지원을 받을 수 있다."
- structured_value:

```json
{
  "entries": [
    {
      "boss": "Golden Pig King",
      "calamity": 8,
      "choice": false,
      "reward": "Labreska's Helmet",
      "support_quest_ap": 305
    },
    {
      "boss": "Golden Pig King",
      "calamity": 9,
      "choice": true,
      "reward": "Ator's Shoes",
      "support_quest_ap": 315
    },
    {
      "boss": "Sangoon",
      "calamity": 8,
      "choice": false,
      "reward": "Fallen God's Armor",
      "support_quest_ap": 310
    },
    {
      "boss": "Gumiho",
      "calamity": 8,
      "choice": true,
      "reward": "Dahn's Gloves",
      "support_quest_ap": 315
    }
  ],
  "knowledge_role": "fact",
  "support_quest_ap_is_distinct_from_boss_entry_ap": true
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

### `donghae-hyperboost-armor-support.current-system`

- seed_key: "donghae-hyperboost-armor-support.current-system"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "black-shrine-donghae-current-system"
- content_name_ko: "검은사당 동해도 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/black-shrine-donghae-current-system.md"

## Evidence and Sources

### Current evidence

### `donghae-hyperboost-armor-support.claim.conditions::black-shrine-donghae-guide`

- evidence_seed_key: "donghae-hyperboost-armor-support.claim.conditions::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "donghae-hyperboost-armor-support.conditions"
- claim_key: "requirement:conditions"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
