<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 발레노스 메인 의뢰

## Identity

- slug: "main-quest-balenos"
- name_ko: "발레노스 메인 의뢰"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "고대인의 석실 시작 경로에서 초기 세계와 주요 시스템을 익히는 지역 메인 의뢰다."
- purpose: "발레노스 지역 완료를 이후 메인 의뢰 흐름의 첫 체크포인트로 기록한다."

## Requirements

### `main-quest-balenos.route`

- seed_key: "main-quest-balenos.route"
- kind: "quest"
- requirement_level: "required"
- title: "고대인의 석실 시작 경로"
- description: "고대인의 석실을 시작 지역으로 선택한 모험가는 발레노스 메인 의뢰를 따라 벨리아까지 진행한다."
- structured_value:

```json
{
  "checkpoint": "Balenos main quest completion",
  "knowledge_role": "fact",
  "start_region": "Ancient Stone Chamber"
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

### `main-quest-balenos.foundation`

- seed_key: "main-quest-balenos.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "main-quest-progression-foundation"
- content_name_ko: "메인 의뢰 성장 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-progression-foundation.md"
### `main-quest-jordaine-saga.balenos`

- seed_key: "main-quest-jordaine-saga.balenos"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "main-quest-jordaine-saga"
- content_name_ko: "조르다인 사가"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/main-quest-jordaine-saga.md"
### `main-quest-mountain-of-eternal-winter.balenos`

- seed_key: "main-quest-mountain-of-eternal-winter.balenos"
- direction: "incoming"
- relation_type: "alternative"
- content_slug: "main-quest-mountain-of-eternal-winter"
- content_name_ko: "끝없는 겨울의 산 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/main-quest-mountain-of-eternal-winter.md"

## Evidence and Sources

### Current evidence

### `main-quest-balenos.claim.route::new-adventurer-main-quest-guide`

- evidence_seed_key: "main-quest-balenos.claim.route::new-adventurer-main-quest-guide"
- source_id: "new-adventurer-main-quest-guide"
- title: "New Adventurer Main Quest Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=284"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "main-quest-balenos.route"
- claim_key: "requirement:route"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
