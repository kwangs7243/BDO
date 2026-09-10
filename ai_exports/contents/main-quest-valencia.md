<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 발렌시아 메인 의뢰

## Identity

- slug: "main-quest-valencia"
- name_ko: "발렌시아 메인 의뢰"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "메디아 이후 제시되는 주요 지역 메인 의뢰 체크포인트다."
- purpose: "발렌시아 지역 완료 상태를 후속 가문 성장 경로와 연결한다."

## Requirements

### `main-quest-valencia.route`

- seed_key: "main-quest-valencia.route"
- kind: "quest"
- requirement_level: "required"
- title: "발렌시아 지역 진행"
- description: "공식 신규 모험가 가이드는 메디아 이후의 주요 지역 진행에 발렌시아를 제시한다."
- structured_value:

```json
{
  "checkpoint": "Valencia main quest completion",
  "knowledge_role": "fact",
  "listed_after": "Mediah"
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

### `main-quest-valencia.foundation`

- seed_key: "main-quest-valencia.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "main-quest-progression-foundation"
- content_name_ko: "메인 의뢰 성장 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-progression-foundation.md"
### `main-quest-valencia.mediah`

- seed_key: "main-quest-valencia.mediah"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "main-quest-mediah"
- content_name_ko: "메디아 메인 의뢰"
- content_category: "progression"
- note: "공식 가이드의 메디아 이후 주요 지역 진행 순서"
- order_no: 2
- relative_path: "../contents/main-quest-mediah.md"
### `main-quest-kamasylvia.valencia`

- seed_key: "main-quest-kamasylvia.valencia"
- direction: "incoming"
- relation_type: "related"
- content_slug: "main-quest-kamasylvia"
- content_name_ko: "카마실비아 메인 의뢰"
- content_category: "progression"
- note: "공식 가이드의 메디아 이후 주요 지역 진행 흐름"
- order_no: 2
- relative_path: "../contents/main-quest-kamasylvia.md"

## Evidence and Sources

### Current evidence

### `main-quest-valencia.claim.route::new-adventurer-main-quest-guide`

- evidence_seed_key: "main-quest-valencia.claim.route::new-adventurer-main-quest-guide"
- source_id: "new-adventurer-main-quest-guide"
- title: "New Adventurer Main Quest Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=284"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "main-quest-valencia.route"
- claim_key: "requirement:route"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
