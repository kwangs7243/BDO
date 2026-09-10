<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 월드 우두머리 현재 명단

## Identity

- slug: "world-boss-current-roster"
- name_ko: "월드 우두머리 현재 명단"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "open_world"
- difficulty: "varies"

## Overview

- summary: "공식 가이드 본문의 열거 항목을 기준으로 현재 14개 엔터티를 관리한다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `world-boss-current-roster.current`

- seed_key: "world-boss-current-roster.current"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 14개 엔터티"
- description: "가이드의 실제 열거 목록은 14개다."
- structured_value:

```json
{
  "count_basis": "enumerated_entities",
  "entities": [
    {
      "name": "Kzarka",
      "slug": "world-boss-kzarka"
    },
    {
      "name": "Nouver",
      "slug": "world-boss-nouver"
    },
    {
      "name": "Karanda",
      "slug": "world-boss-karanda"
    },
    {
      "name": "Kutum",
      "slug": "world-boss-kutum"
    },
    {
      "name": "Quint",
      "slug": "world-boss-quint"
    },
    {
      "name": "Muraka",
      "slug": "world-boss-muraka"
    },
    {
      "name": "Mirumok Destroyer Offin",
      "slug": "world-boss-offin"
    },
    {
      "name": "Garmoth",
      "slug": "garmoth"
    },
    {
      "name": "Vell",
      "slug": "vell"
    },
    {
      "name": "Sangoon",
      "slug": "world-boss-sangoon"
    },
    {
      "name": "Golden Pig King",
      "slug": "world-boss-golden-pig-king"
    },
    {
      "name": "Uturi",
      "slug": "world-boss-uturi"
    },
    {
      "name": "Bulgasal",
      "slug": "world-boss-bulgasal"
    },
    {
      "name": "Black Phoenix",
      "slug": "world-boss-black-phoenix"
    }
  ],
  "entity_count": 14,
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

### `world-boss-current-roster.entity-world-boss-kzarka`

- seed_key: "world-boss-current-roster.entity-world-boss-kzarka"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "world-boss-kzarka"
- content_name_ko: "크자카 (월드 우두머리)"
- content_category: "combat_pve"
- note: "Kzarka 현재 명단 엔터티"
- order_no: 1
- relative_path: "../contents/world-boss-kzarka.md"
### `world-boss-current-roster.entity-world-boss-nouver`

- seed_key: "world-boss-current-roster.entity-world-boss-nouver"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "world-boss-nouver"
- content_name_ko: "누베르 (월드 우두머리)"
- content_category: "combat_pve"
- note: "Nouver 현재 명단 엔터티"
- order_no: 2
- relative_path: "../contents/world-boss-nouver.md"
### `world-boss-current-roster.entity-world-boss-karanda`

- seed_key: "world-boss-current-roster.entity-world-boss-karanda"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "world-boss-karanda"
- content_name_ko: "카란다 (월드 우두머리)"
- content_category: "combat_pve"
- note: "Karanda 현재 명단 엔터티"
- order_no: 3
- relative_path: "../contents/world-boss-karanda.md"
### `world-boss-current-roster.entity-world-boss-kutum`

- seed_key: "world-boss-current-roster.entity-world-boss-kutum"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "world-boss-kutum"
- content_name_ko: "쿠툼 (월드 우두머리)"
- content_category: "combat_pve"
- note: "Kutum 현재 명단 엔터티"
- order_no: 4
- relative_path: "../contents/world-boss-kutum.md"
### `world-boss-current-roster.entity-world-boss-quint`

- seed_key: "world-boss-current-roster.entity-world-boss-quint"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "world-boss-quint"
- content_name_ko: "귄트 (월드 우두머리)"
- content_category: "combat_pve"
- note: "Quint 현재 명단 엔터티"
- order_no: 5
- relative_path: "../contents/world-boss-quint.md"
### `world-boss-current-roster.entity-world-boss-muraka`

- seed_key: "world-boss-current-roster.entity-world-boss-muraka"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "world-boss-muraka"
- content_name_ko: "무라카 (월드 우두머리)"
- content_category: "combat_pve"
- note: "Muraka 현재 명단 엔터티"
- order_no: 6
- relative_path: "../contents/world-boss-muraka.md"
### `world-boss-current-roster.entity-world-boss-offin`

- seed_key: "world-boss-current-roster.entity-world-boss-offin"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "world-boss-offin"
- content_name_ko: "미루목 파괴자 오핀 (월드 우두머리)"
- content_category: "combat_pve"
- note: "Mirumok Destroyer Offin 현재 명단 엔터티"
- order_no: 7
- relative_path: "../contents/world-boss-offin.md"
### `world-boss-current-roster.entity-garmoth`

- seed_key: "world-boss-current-roster.entity-garmoth"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "garmoth"
- content_name_ko: "가모스"
- content_category: "world_boss"
- note: "Garmoth 현재 명단 엔터티"
- order_no: 8
- relative_path: "../contents/garmoth.md"
### `world-boss-current-roster.entity-vell`

- seed_key: "world-boss-current-roster.entity-vell"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "vell"
- content_name_ko: "벨"
- content_category: "world_boss"
- note: "Vell 현재 명단 엔터티"
- order_no: 9
- relative_path: "../contents/vell.md"
### `world-boss-current-roster.entity-world-boss-sangoon`

- seed_key: "world-boss-current-roster.entity-world-boss-sangoon"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "world-boss-sangoon"
- content_name_ko: "산군 (월드 우두머리)"
- content_category: "combat_pve"
- note: "Sangoon 현재 명단 엔터티"
- order_no: 10
- relative_path: "../contents/world-boss-sangoon.md"
### `world-boss-current-roster.entity-world-boss-golden-pig-king`

- seed_key: "world-boss-current-roster.entity-world-boss-golden-pig-king"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "world-boss-golden-pig-king"
- content_name_ko: "금돼지왕 (월드 우두머리)"
- content_category: "combat_pve"
- note: "Golden Pig King 현재 명단 엔터티"
- order_no: 11
- relative_path: "../contents/world-boss-golden-pig-king.md"
### `world-boss-current-roster.entity-world-boss-uturi`

- seed_key: "world-boss-current-roster.entity-world-boss-uturi"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "world-boss-uturi"
- content_name_ko: "우투리 (월드 우두머리)"
- content_category: "combat_pve"
- note: "Uturi 현재 명단 엔터티"
- order_no: 12
- relative_path: "../contents/world-boss-uturi.md"
### `world-boss-current-roster.entity-world-boss-bulgasal`

- seed_key: "world-boss-current-roster.entity-world-boss-bulgasal"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "world-boss-bulgasal"
- content_name_ko: "불가살 (월드 우두머리)"
- content_category: "combat_pve"
- note: "Bulgasal 현재 명단 엔터티"
- order_no: 13
- relative_path: "../contents/world-boss-bulgasal.md"
### `world-boss-current-roster.entity-world-boss-black-phoenix`

- seed_key: "world-boss-current-roster.entity-world-boss-black-phoenix"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "world-boss-black-phoenix"
- content_name_ko: "검은 봉황 (월드 우두머리)"
- content_category: "combat_pve"
- note: "Black Phoenix 현재 명단 엔터티"
- order_no: 14
- relative_path: "../contents/world-boss-black-phoenix.md"

## Evidence and Sources

### Current evidence

### `world-boss-current-roster.claim.current::world-boss-guide`

- evidence_seed_key: "world-boss-current-roster.claim.current::world-boss-guide"
- source_id: "world-boss-guide"
- title: "월드 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=89"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "world-boss-current-roster.current"
- claim_key: "requirement:current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `world-boss-current-roster.claim.guide-fixed-thirteen::world-boss-guide`

- evidence_seed_key: "world-boss-current-roster.claim.guide-fixed-thirteen::world-boss-guide"
- source_id: "world-boss-guide"
- title: "월드 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=89"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "world-boss-current-roster.guide-fixed-thirteen"
- claim_key: "requirement:guide-fixed-thirteen"
- verification_status: "conflict"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
