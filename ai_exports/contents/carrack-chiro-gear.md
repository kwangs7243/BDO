<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 중범선 치로 장비

## Identity

- slug: "carrack-chiro-gear"
- name_ko: "중범선 치로 장비"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "중범선 장비 성장의 중간 단계인 파란색 치로 장비."
- purpose: "토로에서 치로를 거쳐 팔라시로 이어지는 현행 장비 progression을 분명히 한다."

## Requirements

### `carrack-chiro-gear.enhancement`

- seed_key: "carrack-chiro-gear.enhancement"
- kind: "gear"
- requirement_level: "required"
- title: "+10 치로 장비"
- description: "팔라시 각 부위 제작에는 같은 부위의 +10 치로 장비가 1개 필요하다."
- structured_value:

```json
{
  "amount": 1,
  "enhancement": 10,
  "parts": [
    "함포",
    "돛",
    "선수상",
    "흑장갑"
  ]
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `carrack-chiro-gear.progression`

- seed_key: "carrack-chiro-gear.progression"
- section_type: "overview"
- title: "현행 장비 progression"
- order_no: 1

#### body_markdown

토로 → 치로 → 팔라시 순서다. 치로는 +10 강화 후 팔라시 제작 재료로 사용되는 중간 단계이며 현재 최종 장비가 아니다.

## Related Contents

### `carrack-chiro-gear.relation.types`

- seed_key: "carrack-chiro-gear.relation.types"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "carrack-types"
- content_name_ko: "에페리아 중범선 네 종류"
- content_category: "ocean_project"
- note: "중범선 네 종류의 파란 장비"
- order_no: 1
- relative_path: "../contents/carrack-types.md"
### `carrack-chiro-gear.relation.palasi`

- seed_key: "carrack-chiro-gear.relation.palasi"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "carrack-palasi-gear"
- content_name_ko: "중범선 팔라시 장비"
- content_category: "ocean_project"
- note: "+10 치로 장비가 팔라시 제작의 선행 재료"
- order_no: 2
- relative_path: "../contents/carrack-palasi-gear.md"
### `carrack-palasi-gear.relation.chiro`

- seed_key: "carrack-palasi-gear.relation.chiro"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "carrack-palasi-gear"
- content_name_ko: "중범선 팔라시 장비"
- content_category: "ocean_project"
- note: "+10 치로의 동일 부위가 제작 재료"
- order_no: 1
- relative_path: "../contents/carrack-palasi-gear.md"
### `carrack-advance.relation.chiro`

- seed_key: "carrack-advance.relation.chiro"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "carrack-advance"
- content_name_ko: "에페리아 중범선 : 점진"
- content_category: "ocean_project"
- note: "중범선 완성 후 토로→치로→팔라시 장비 성장"
- order_no: 3
- relative_path: "../contents/carrack-advance.md"
### `carrack-types.relation.chiro`

- seed_key: "carrack-types.relation.chiro"
- direction: "incoming"
- relation_type: "related"
- content_slug: "carrack-types"
- content_name_ko: "에페리아 중범선 네 종류"
- content_category: "ocean_project"
- note: "중범선 장비 성장"
- order_no: 3
- relative_path: "../contents/carrack-types.md"

## Evidence and Sources

### Current evidence

### `carrack-chiro-gear.evidence.enhancement::ocean-progression-2026-08-26`

- evidence_seed_key: "carrack-chiro-gear.evidence.enhancement::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-chiro-gear.enhancement"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "팔라시 각 부위 제작에는 같은 부위의 +10 치로 장비가 1개 필요하다."
- active: true
- is_active: true

### `carrack-chiro-gear.evidence.progression::carrack-guide`

- evidence_seed_key: "carrack-chiro-gear.evidence.progression::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "carrack-chiro-gear.progression"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "토로 → 치로 → 팔라시 순서다. 치로는 +10 강화 후 팔라시 제작 재료로 사용되는 중간 단계이며 현재 최종 장비가 아니다."
- active: true
- is_active: true

### `carrack-chiro-gear.evidence.progression::ocean-progression-2026-08-26`

- evidence_seed_key: "carrack-chiro-gear.evidence.progression::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "carrack-chiro-gear.progression"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "토로 → 치로 → 팔라시 순서다. 치로는 +10 강화 후 팔라시 제작 재료로 사용되는 중간 단계이며 현재 최종 장비가 아니다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
