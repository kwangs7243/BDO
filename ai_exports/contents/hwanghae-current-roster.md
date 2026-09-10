<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 황해도 검은사당 현재 명단

## Identity

- slug: "hwanghae-current-roster"
- name_ko: "황해도 검은사당 현재 명단"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "party"
- difficulty: "varies"

## Overview

- summary: "현재 공식 명단은 지귀·우투리·청의동자·불가살·흑봉황·비형랑·폐세자 7종이다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `hwanghae-current-roster.current`

- seed_key: "hwanghae-current-roster.current"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 7종"
- description: "공식 현재 명단 7종을 엔터티로 연결한다."
- structured_value:

```json
{
  "entities": [
    {
      "name": "지귀",
      "slug": "hwanghae-shrine-jigwi"
    },
    {
      "name": "우투리",
      "slug": "hwanghae-shrine-uturi"
    },
    {
      "name": "청의동자",
      "slug": "hwanghae-shrine-blue-clad-youth"
    },
    {
      "name": "불가살",
      "slug": "hwanghae-shrine-bulgasal"
    },
    {
      "name": "흑봉황",
      "slug": "hwanghae-shrine-dark-bonghwang"
    },
    {
      "name": "비형랑",
      "slug": "hwanghae-shrine-bihyung"
    },
    {
      "name": "폐세자",
      "slug": "hwanghae-shrine-deposed-crown-prince"
    }
  ],
  "entity_count": 7,
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

### `hwanghae-current-roster.entity-jigwi`

- seed_key: "hwanghae-current-roster.entity-jigwi"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "hwanghae-shrine-jigwi"
- content_name_ko: "지귀 (황해도 검은사당)"
- content_category: "combat_pve"
- note: "지귀 현재 명단 엔터티"
- order_no: 1
- relative_path: "../contents/hwanghae-shrine-jigwi.md"
### `hwanghae-current-roster.entity-uturi`

- seed_key: "hwanghae-current-roster.entity-uturi"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "hwanghae-shrine-uturi"
- content_name_ko: "우투리 (황해도 검은사당)"
- content_category: "combat_pve"
- note: "우투리 현재 명단 엔터티"
- order_no: 2
- relative_path: "../contents/hwanghae-shrine-uturi.md"
### `hwanghae-current-roster.entity-blue-clad-youth`

- seed_key: "hwanghae-current-roster.entity-blue-clad-youth"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "hwanghae-shrine-blue-clad-youth"
- content_name_ko: "청의동자 (황해도 검은사당)"
- content_category: "combat_pve"
- note: "청의동자 현재 명단 엔터티"
- order_no: 3
- relative_path: "../contents/hwanghae-shrine-blue-clad-youth.md"
### `hwanghae-current-roster.entity-bulgasal`

- seed_key: "hwanghae-current-roster.entity-bulgasal"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "hwanghae-shrine-bulgasal"
- content_name_ko: "불가살 (황해도 검은사당)"
- content_category: "combat_pve"
- note: "불가살 현재 명단 엔터티"
- order_no: 4
- relative_path: "../contents/hwanghae-shrine-bulgasal.md"
### `hwanghae-current-roster.entity-dark-bonghwang`

- seed_key: "hwanghae-current-roster.entity-dark-bonghwang"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "hwanghae-shrine-dark-bonghwang"
- content_name_ko: "흑봉황 (황해도 검은사당)"
- content_category: "combat_pve"
- note: "흑봉황 현재 명단 엔터티"
- order_no: 5
- relative_path: "../contents/hwanghae-shrine-dark-bonghwang.md"
### `hwanghae-current-roster.entity-bihyung`

- seed_key: "hwanghae-current-roster.entity-bihyung"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "hwanghae-shrine-bihyung"
- content_name_ko: "비형랑 (황해도 검은사당)"
- content_category: "combat_pve"
- note: "비형랑 현재 명단 엔터티"
- order_no: 6
- relative_path: "../contents/hwanghae-shrine-bihyung.md"
### `hwanghae-current-roster.entity-deposed-crown-prince`

- seed_key: "hwanghae-current-roster.entity-deposed-crown-prince"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "hwanghae-shrine-deposed-crown-prince"
- content_name_ko: "폐세자 (황해도 검은사당)"
- content_category: "combat_pve"
- note: "폐세자 현재 명단 엔터티"
- order_no: 7
- relative_path: "../contents/hwanghae-shrine-deposed-crown-prince.md"

## Evidence and Sources

### Current evidence

### `hwanghae-current-roster.claim.current::black-shrine-hwanghae-guide`

- evidence_seed_key: "hwanghae-current-roster.claim.current::black-shrine-hwanghae-guide"
- source_id: "black-shrine-hwanghae-guide"
- title: "검은 사당 - 황해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=404"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "hwanghae-current-roster.current"
- claim_key: "requirement:current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `hwanghae-current-roster.claim.legacy-six::black-shrine-party-guide-current`

- evidence_seed_key: "hwanghae-current-roster.claim.legacy-six::black-shrine-party-guide-current"
- source_id: "black-shrine-party-guide-current"
- title: "Black Shrine Party Guide"
- url: "https://www.blackdesertfoundry.com/black-shrine-party-guide/"
- publisher: "Black Desert Foundry"
- source_type: "third_party_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "global"
- entity_type: "content_requirement"
- entity_id: "hwanghae-current-roster.legacy-six"
- claim_key: "requirement:legacy-six"
- verification_status: "conflict"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
