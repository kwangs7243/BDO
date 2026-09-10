<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 대왕 고래와 도망자 칼크 파티 수렵

## Identity

- slug: "group-hunting-whale-khalk"
- name_ko: "대왕 고래와 도망자 칼크 파티 수렵"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "대왕 고래와 도망자 칼크는 채널 출현·파티 추적·화승총 공격을 사용하는 대표 파티 수렵이다."
- purpose: "기여도 파티 순위와 대표 보상 범주를 과도한 낡은 드롭표 없이 기록한다."

## Requirements

### `group-hunting-whale-khalk.whale`

- seed_key: "group-hunting-whale-khalk.whale"
- kind: "party"
- requirement_level: "required"
- title: "대왕 고래"
- description: "대왕 고래의 현재 규칙이다."
- structured_value:

```json
{
  "butcher_chance_per_eligible_party_member": true,
  "channel_spawn": true,
  "complete_drop_table": false,
  "eligible_top_parties": 20,
  "loot_categories": [
    "whale_molar",
    "tendon",
    "oil",
    "meat"
  ],
  "party_hunting": true,
  "tracking": "ship",
  "weapon": "matchlock"
}
```

### `group-hunting-whale-khalk.khalk`

- seed_key: "group-hunting-whale-khalk.khalk"
- kind: "party"
- requirement_level: "required"
- title: "도망자 칼크"
- description: "도망자 칼크의 현재 규칙이다."
- structured_value:

```json
{
  "complete_drop_table": false,
  "eligible_top_parties": 5,
  "loot_categories": [
    "shining_khalk_claw",
    "hide",
    "horn"
  ],
  "party_hunting": true
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

### `group-hunting-whale-khalk.cooking`

- seed_key: "group-hunting-whale-khalk.cooking"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "cooking-current-system"
- content_name_ko: "요리 현재 시스템"
- content_category: "life"
- note: "수렵 고기는 요리 재료 흐름과 연결된다."
- order_no: 1
- relative_path: "../contents/cooking-current-system.md"
### `group-hunting-whale-khalk.alchemy`

- seed_key: "group-hunting-whale-khalk.alchemy"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "alchemy-current-system"
- content_name_ko: "연금 현재 시스템"
- content_category: "life"
- note: "수렵 부산물은 연금 재료 흐름과 연결된다."
- order_no: 2
- relative_path: "../contents/alchemy-current-system.md"

## Evidence and Sources

### Current evidence

### `group-hunting-whale-khalk.claim.current::hunting-guide`

- evidence_seed_key: "group-hunting-whale-khalk.claim.current::hunting-guide"
- source_id: "hunting-guide"
- title: "수렵"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "group-hunting-whale-khalk"
- claim_key: "requirements:group-hunting-whale-khalk"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
