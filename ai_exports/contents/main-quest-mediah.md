<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 메디아 메인 의뢰

## Identity

- slug: "main-quest-mediah"
- name_ko: "메디아 메인 의뢰"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "조르다인 사가 이후 이어지는 주요 지역 메인 의뢰 체크포인트다."
- purpose: "메디아 완료를 이후 대륙·지역 진행의 기준 상태로 기록한다."

## Requirements

### `main-quest-mediah.route`

- seed_key: "main-quest-mediah.route"
- kind: "quest"
- requirement_level: "required"
- title: "메디아 지역 진행"
- description: "일반 메인 의뢰 경로에서는 조르다인 사가 이후 메디아 메인 의뢰로 이어진다."
- structured_value:

```json
{
  "checkpoint": "Mediah main quest completion",
  "knowledge_role": "fact",
  "route": "standard_main_quest"
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

### `main-quest-mediah.foundation`

- seed_key: "main-quest-mediah.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "main-quest-progression-foundation"
- content_name_ko: "메인 의뢰 성장 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-progression-foundation.md"
### `main-quest-mediah.jordaine`

- seed_key: "main-quest-mediah.jordaine"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "main-quest-jordaine-saga"
- content_name_ko: "조르다인 사가"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/main-quest-jordaine-saga.md"
### `main-quest-valencia.mediah`

- seed_key: "main-quest-valencia.mediah"
- direction: "incoming"
- relation_type: "related"
- content_slug: "main-quest-valencia"
- content_name_ko: "발렌시아 메인 의뢰"
- content_category: "progression"
- note: "공식 가이드의 메디아 이후 주요 지역 진행 순서"
- order_no: 2
- relative_path: "../contents/main-quest-valencia.md"

## Evidence and Sources

### Current evidence

### `main-quest-mediah.claim.route::new-adventurer-main-quest-guide`

- evidence_seed_key: "main-quest-mediah.claim.route::new-adventurer-main-quest-guide"
- source_id: "new-adventurer-main-quest-guide"
- title: "New Adventurer Main Quest Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=284"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "main-quest-mediah.route"
- claim_key: "requirement:route"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
