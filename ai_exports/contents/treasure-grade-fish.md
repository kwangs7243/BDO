<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 보물 등급 물고기

## Identity

- slug: "treasure-grade-fish"
- name_ko: "보물 등급 물고기"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "2024 낚시 개선에서 45종이 추가됐고 특정 담수·해수 포인트에서 낚이며 황실 낚시 납품에는 사용할 수 없다."
- purpose: "전체 어종 좌표 백과 대신 보물 물고기 그룹의 현재 공통 규칙만 저장한다."

## Requirements

### `treasure-grade-fish.group`

- seed_key: "treasure-grade-fish.group"
- kind: "item"
- requirement_level: "required"
- title: "보물 어종 그룹"
- description: "공식 낚시 개선에서 보물 어종 45종이 추가됐다."
- structured_value:

```json
{
  "high_base_price": true,
  "introduced_count": 45,
  "knowledge_on_catch": true,
  "locations": [
    "specific_freshwater_points",
    "specific_saltwater_points"
  ]
}
```

### `treasure-grade-fish.imperial`

- seed_key: "treasure-grade-fish.imperial"
- kind: "other"
- requirement_level: "required"
- title: "황실 낚시 납품"
- description: "보물 등급 물고기는 황실 낚시 납품에 사용할 수 없다."
- structured_value:

```json
{
  "imperial_fishing_delivery_allowed": false
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `treasure-grade-fish.scope`

- seed_key: "treasure-grade-fish.scope"
- section_type: "notes"
- title: "후속 Fish Atlas"
- order_no: 1

#### body_markdown

45종 전체 좌표·낚시터 drop pool·수익 비교는 이번 Pack에 포함하지 않는다.

## Related Contents

### `treasure-grade-fish.mastery`

- seed_key: "treasure-grade-fish.mastery"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "fishing-current-system"
- content_name_ko: "낚시 현재 시스템"
- content_category: "life"
- note: "낚시 숙련도 보물 그룹 기여분"
- order_no: 1
- relative_path: "../contents/fishing-current-system.md"
### `treasure-grade-fish.imperial-delivery`

- seed_key: "treasure-grade-fish.imperial-delivery"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "imperial-fishing-delivery"
- content_name_ko: "황실 낚시 납품"
- content_category: "life"
- note: "납품 불가 예외"
- order_no: 2
- relative_path: "../contents/imperial-fishing-delivery.md"
### `fishing-encyclopedia-and-weekly-contest.treasure`

- seed_key: "fishing-encyclopedia-and-weekly-contest.treasure"
- direction: "incoming"
- relation_type: "related"
- content_slug: "fishing-encyclopedia-and-weekly-contest"
- content_name_ko: "어류 도감과 주간 낚시 대회"
- content_category: "life"
- note: "지정 어종에 보물 등급이 포함될 수 있음"
- order_no: 2
- relative_path: "../contents/fishing-encyclopedia-and-weekly-contest.md"
### `fishing-current-system.treasure`

- seed_key: "fishing-current-system.treasure"
- direction: "incoming"
- relation_type: "related"
- content_slug: "fishing-current-system"
- content_name_ko: "낚시 현재 시스템"
- content_category: "life"
- note: "보물 등급 그룹"
- order_no: 3
- relative_path: "../contents/fishing-current-system.md"
### `imperial-fishing-delivery.treasure`

- seed_key: "imperial-fishing-delivery.treasure"
- direction: "incoming"
- relation_type: "related"
- content_slug: "imperial-fishing-delivery"
- content_name_ko: "황실 낚시 납품"
- content_category: "life"
- note: "보물 등급은 납품 불가"
- order_no: 3
- relative_path: "../contents/imperial-fishing-delivery.md"

## Evidence and Sources

### Current evidence

### `treasure-grade-fish.summary::fishing-improvement-history`

- evidence_seed_key: "treasure-grade-fish.summary::fishing-improvement-history"
- source_id: "fishing-improvement-history"
- title: "낚시 콘텐츠 개선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13112"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "treasure-grade-fish"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "45종과 납품 불가"
- active: true
- is_active: true

### `treasure-grade-fish.requirement.group::fishing-improvement-history`

- evidence_seed_key: "treasure-grade-fish.requirement.group::fishing-improvement-history"
- source_id: "fishing-improvement-history"
- title: "낚시 콘텐츠 개선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13112"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "treasure-grade-fish.group"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "45종·특정 포인트·지식"
- active: true
- is_active: true

### `treasure-grade-fish.requirement.imperial::fishing-improvement-history`

- evidence_seed_key: "treasure-grade-fish.requirement.imperial::fishing-improvement-history"
- source_id: "fishing-improvement-history"
- title: "낚시 콘텐츠 개선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13112"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "treasure-grade-fish.imperial"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "황실 낚시 납품 불가"
- active: true
- is_active: true

### Historical / inactive evidence

- None
