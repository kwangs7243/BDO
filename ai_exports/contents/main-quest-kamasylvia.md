<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 카마실비아 메인 의뢰

## Identity

- slug: "main-quest-kamasylvia"
- name_ko: "카마실비아 메인 의뢰"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "메디아 이후 주요 지역 흐름에 포함되는 카마실비아 메인 의뢰 체크포인트다."
- purpose: "지역 완료와 후속 가문 방어력 의뢰 해금을 연결한다."

## Requirements

### `main-quest-kamasylvia.route`

- seed_key: "main-quest-kamasylvia.route"
- kind: "quest"
- requirement_level: "required"
- title: "카마실비아 지역 진행"
- description: "공식 신규 모험가 가이드는 메디아 이후의 주요 지역 진행에 카마실비아를 제시한다."
- structured_value:

```json
{
  "checkpoint": "Kamasylvia main quest completion",
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

### `main-quest-kamasylvia.foundation`

- seed_key: "main-quest-kamasylvia.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "main-quest-progression-foundation"
- content_name_ko: "메인 의뢰 성장 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-progression-foundation.md"
### `main-quest-kamasylvia.valencia`

- seed_key: "main-quest-kamasylvia.valencia"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "main-quest-valencia"
- content_name_ko: "발렌시아 메인 의뢰"
- content_category: "progression"
- note: "공식 가이드의 메디아 이후 주요 지역 진행 흐름"
- order_no: 2
- relative_path: "../contents/main-quest-valencia.md"
### `main-quest-kamasylvia.family-dp`

- seed_key: "main-quest-kamasylvia.family-dp"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "kamasylvia-family-defense-quest"
- content_name_ko: "카마실비아 가문 방어력 의뢰"
- content_category: "progression"
- note: null
- order_no: 3
- relative_path: "../contents/kamasylvia-family-defense-quest.md"
### `kamasylvia-family-defense-quest.main`

- seed_key: "kamasylvia-family-defense-quest.main"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "kamasylvia-family-defense-quest"
- content_name_ko: "카마실비아 가문 방어력 의뢰"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/kamasylvia-family-defense-quest.md"
### `main-quest-drieghan.kamasylvia`

- seed_key: "main-quest-drieghan.kamasylvia"
- direction: "incoming"
- relation_type: "related"
- content_slug: "main-quest-drieghan"
- content_name_ko: "드리간 메인 의뢰"
- content_category: "progression"
- note: "공식 가이드의 주요 지역 진행 흐름"
- order_no: 2
- relative_path: "../contents/main-quest-drieghan.md"

## Evidence and Sources

### Current evidence

### `main-quest-kamasylvia.claim.route::new-adventurer-main-quest-guide`

- evidence_seed_key: "main-quest-kamasylvia.claim.route::new-adventurer-main-quest-guide"
- source_id: "new-adventurer-main-quest-guide"
- title: "New Adventurer Main Quest Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=284"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "main-quest-kamasylvia.route"
- claim_key: "requirement:route"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
