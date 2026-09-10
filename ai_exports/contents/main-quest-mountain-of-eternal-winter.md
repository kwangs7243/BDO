<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 끝없는 겨울의 산 메인 의뢰

## Identity

- slug: "main-quest-mountain-of-eternal-winter"
- name_ko: "끝없는 겨울의 산 메인 의뢰"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "신규 모험가가 고대인의 석실 대신 선택할 수 있는 별도 시작 지역 메인 의뢰다."
- purpose: "현재 시작 분기를 발레노스 경로와 구분해 기록한다."

## Requirements

### `main-quest-mountain-of-eternal-winter.start`

- seed_key: "main-quest-mountain-of-eternal-winter.start"
- kind: "quest"
- requirement_level: "required"
- title: "시작 지역 선택"
- description: "캐릭터 생성 뒤 시작 지역으로 끝없는 겨울의 산을 선택하면 해당 지역 메인 의뢰로 시작한다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "route_type": "alternative_start",
  "start_region": "Mountain of Eternal Winter"
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

### `main-quest-mountain-of-eternal-winter.foundation`

- seed_key: "main-quest-mountain-of-eternal-winter.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "main-quest-progression-foundation"
- content_name_ko: "메인 의뢰 성장 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-progression-foundation.md"
### `main-quest-mountain-of-eternal-winter.balenos`

- seed_key: "main-quest-mountain-of-eternal-winter.balenos"
- direction: "outgoing"
- relation_type: "alternative"
- content_slug: "main-quest-balenos"
- content_name_ko: "발레노스 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/main-quest-balenos.md"

## Evidence and Sources

### Current evidence

### `main-quest-mountain-of-eternal-winter.claim.start::new-adventurer-main-quest-guide`

- evidence_seed_key: "main-quest-mountain-of-eternal-winter.claim.start::new-adventurer-main-quest-guide"
- source_id: "new-adventurer-main-quest-guide"
- title: "New Adventurer Main Quest Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=284"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "main-quest-mountain-of-eternal-winter.start"
- claim_key: "requirement:start"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
