<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 오드락시아 메인 의뢰

## Identity

- slug: "main-quest-odyllita"
- name_ko: "오드락시아 메인 의뢰"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "메디아 이후 주요 지역 흐름에 포함되는 오드락시아 메인 의뢰 체크포인트다."
- purpose: "지역 2부 완료와 후속 가문 공격력 의뢰 해금을 연결한다."

## Requirements

### `main-quest-odyllita.route`

- seed_key: "main-quest-odyllita.route"
- kind: "quest"
- requirement_level: "required"
- title: "오드락시아 지역 진행"
- description: "공식 신규 모험가 가이드는 메디아 이후의 주요 지역 진행에 오드락시아를 제시한다."
- structured_value:

```json
{
  "checkpoint": "Odyllita main quest completion",
  "followup_checkpoint": "Odyllita part 2 - Hadum's Realm",
  "knowledge_role": "fact"
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

### `main-quest-odyllita.foundation`

- seed_key: "main-quest-odyllita.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "main-quest-progression-foundation"
- content_name_ko: "메인 의뢰 성장 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-progression-foundation.md"
### `main-quest-odyllita.drieghan`

- seed_key: "main-quest-odyllita.drieghan"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "main-quest-drieghan"
- content_name_ko: "드리간 메인 의뢰"
- content_category: "progression"
- note: "공식 가이드의 주요 지역 진행 흐름"
- order_no: 2
- relative_path: "../contents/main-quest-drieghan.md"
### `main-quest-odyllita.family-ap`

- seed_key: "main-quest-odyllita.family-ap"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "odyllita-family-attack-quest"
- content_name_ko: "오드락시아 가문 공격력 의뢰"
- content_category: "progression"
- note: null
- order_no: 3
- relative_path: "../contents/odyllita-family-attack-quest.md"
### `odyllita-family-attack-quest.main`

- seed_key: "odyllita-family-attack-quest.main"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "odyllita-family-attack-quest"
- content_name_ko: "오드락시아 가문 공격력 의뢰"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/odyllita-family-attack-quest.md"

## Evidence and Sources

### Current evidence

### `main-quest-odyllita.claim.route::family-stat-quest-history`

- evidence_seed_key: "main-quest-odyllita.claim.route::family-stat-quest-history"
- source_id: "family-stat-quest-history"
- title: "Kamasylvia and Odyllita Family Stat Quest History"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=9723"
- publisher: "Pearl Abyss"
- source_type: "official_history"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "main-quest-odyllita.route"
- claim_key: "requirement:route"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `main-quest-odyllita.claim.route::new-adventurer-main-quest-guide`

- evidence_seed_key: "main-quest-odyllita.claim.route::new-adventurer-main-quest-guide"
- source_id: "new-adventurer-main-quest-guide"
- title: "New Adventurer Main Quest Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=284"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "main-quest-odyllita.route"
- claim_key: "requirement:route"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
