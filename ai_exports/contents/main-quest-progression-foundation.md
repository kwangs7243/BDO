<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 메인 의뢰 성장 기반

## Identity

- slug: "main-quest-progression-foundation"
- name_ko: "메인 의뢰 성장 기반"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "시작 분기부터 주요 지역 단위 완료 지점을 기록하는 메인 의뢰 진행 기반이다."
- purpose: "NPC별 공략이 아니라 지역·사가·해금 체크포인트 단위로 가문 진행을 추적한다."

## Requirements

### `main-quest-progression-foundation.structure`

- seed_key: "main-quest-progression-foundation.structure"
- kind: "quest"
- requirement_level: "required"
- title: "지역 단위 진행"
- description: "메인 의뢰는 시작 분기와 발레노스·조르다인 사가·메디아 이후 주요 지역 흐름으로 구성된다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "tracking_granularity": "region_or_chapter_checkpoint"
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

### `main-quest-progression-foundation.account`

- seed_key: "main-quest-progression-foundation.account"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "account-progression-foundation"
- content_name_ko: "가문 성장 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/account-progression-foundation.md"
### `main-quest-balenos.foundation`

- seed_key: "main-quest-balenos.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "main-quest-balenos"
- content_name_ko: "발레노스 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-balenos.md"
### `main-quest-drieghan.foundation`

- seed_key: "main-quest-drieghan.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "main-quest-drieghan"
- content_name_ko: "드리간 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-drieghan.md"
### `main-quest-jordaine-saga.foundation`

- seed_key: "main-quest-jordaine-saga.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "main-quest-jordaine-saga"
- content_name_ko: "조르다인 사가"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-jordaine-saga.md"
### `main-quest-kamasylvia.foundation`

- seed_key: "main-quest-kamasylvia.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "main-quest-kamasylvia"
- content_name_ko: "카마실비아 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-kamasylvia.md"
### `main-quest-mediah.foundation`

- seed_key: "main-quest-mediah.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "main-quest-mediah"
- content_name_ko: "메디아 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-mediah.md"
### `main-quest-morning-land.foundation`

- seed_key: "main-quest-morning-land.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "main-quest-morning-land"
- content_name_ko: "아침의 나라 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-morning-land.md"
### `main-quest-mountain-of-eternal-winter.foundation`

- seed_key: "main-quest-mountain-of-eternal-winter.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "main-quest-mountain-of-eternal-winter"
- content_name_ko: "끝없는 겨울의 산 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-mountain-of-eternal-winter.md"
### `main-quest-odyllita.foundation`

- seed_key: "main-quest-odyllita.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "main-quest-odyllita"
- content_name_ko: "오드락시아 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-odyllita.md"
### `main-quest-valencia.foundation`

- seed_key: "main-quest-valencia.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "main-quest-valencia"
- content_name_ko: "발렌시아 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-valencia.md"

## Evidence and Sources

### Current evidence

### `main-quest-progression-foundation.claim.structure::new-adventurer-main-quest-guide`

- evidence_seed_key: "main-quest-progression-foundation.claim.structure::new-adventurer-main-quest-guide"
- source_id: "new-adventurer-main-quest-guide"
- title: "New Adventurer Main Quest Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=284"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "main-quest-progression-foundation.structure"
- claim_key: "requirement:structure"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `main-quest-progression-foundation.claim.structure::quest-system-guide`

- evidence_seed_key: "main-quest-progression-foundation.claim.structure::quest-system-guide"
- source_id: "quest-system-guide"
- title: "Quest System Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=21"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "main-quest-progression-foundation.structure"
- claim_key: "requirement:structure"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
