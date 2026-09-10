<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 마르니 저격총

## Identity

- slug: "marni-sniper-rifle"
- name_ko: "마르니 저격총"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "마르니 저격총 제작은 응축된 마력의 검은 결정 10개를 쓰며, 최신 강화 재료는 응축된 마력의 블랙스톤이다."
- purpose: "2026년 3월 제작 변경과 4월 강화 변경을 시간 순서대로 구분한다."

## Requirements

### `marni-sniper-rifle.recipe`

- seed_key: "marni-sniper-rifle.recipe"
- kind: "item"
- requirement_level: "required"
- title: "현재 제작식"
- description: "현재 제작식의 현재 규칙이다."
- structured_value:

```json
{
  "condensed_magical_black_crystal": 10,
  "fire_horn": 1000,
  "mystical_powder": 1000,
  "plus_10_sniper_rifle": 1,
  "resplendent_obsidian": 10
}
```

### `marni-sniper-rifle.enhancement`

- seed_key: "marni-sniper-rifle.enhancement"
- kind: "item"
- requirement_level: "required"
- title: "현재 강화 재료"
- description: "현재 강화 재료의 현재 규칙이다."
- structured_value:

```json
{
  "distinct_from": "condensed_magical_black_crystal",
  "effective_from": "2026-04-01",
  "material": "condensed_magical_black_stone"
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

### `marni-sniper-rifle.firearms`

- seed_key: "marni-sniper-rifle.firearms"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "hunting-firearms"
- content_name_ko: "수렵 장비와 화승총 강화"
- content_category: "life"
- note: "저격총 장비 계열의 제작·강화 상세다."
- order_no: 1
- relative_path: "../contents/hunting-firearms.md"

## Evidence and Sources

### Current evidence

### `marni-sniper-rifle.claim.enhancement::marni-sniper-enhancement-2026-04-01`

- evidence_seed_key: "marni-sniper-rifle.claim.enhancement::marni-sniper-enhancement-2026-04-01"
- source_id: "marni-sniper-enhancement-2026-04-01"
- title: "4월 1일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15388"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-01"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "marni-sniper-rifle"
- claim_key: "requirement:marni-sniper-rifle.enhancement"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### `marni-sniper-rifle.claim.recipe::marni-sniper-crafting-2026-03-25`

- evidence_seed_key: "marni-sniper-rifle.claim.recipe::marni-sniper-crafting-2026-03-25"
- source_id: "marni-sniper-crafting-2026-03-25"
- title: "3월 25일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15352"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-03-25"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "marni-sniper-rifle"
- claim_key: "requirement:marni-sniper-rifle.recipe"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `marni-sniper-rifle.claim.legacy-black-crystal-enhancement::marni-sniper-crafting-2026-03-25`

- evidence_seed_key: "marni-sniper-rifle.claim.legacy-black-crystal-enhancement::marni-sniper-crafting-2026-03-25"
- source_id: "marni-sniper-crafting-2026-03-25"
- title: "3월 25일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15352"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-03-25"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "marni-sniper-rifle"
- claim_key: "legacy:condensed-magical-black-crystal-enhancement"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: false
- is_active: false

### `marni-sniper-rifle.claim.legacy-black-crystal-enhancement::marni-sniper-enhancement-2026-04-01`

- evidence_seed_key: "marni-sniper-rifle.claim.legacy-black-crystal-enhancement::marni-sniper-enhancement-2026-04-01"
- source_id: "marni-sniper-enhancement-2026-04-01"
- title: "4월 1일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15388"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-01"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "marni-sniper-rifle"
- claim_key: "legacy:condensed-magical-black-crystal-enhancement"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: false
- is_active: false

### `marni-sniper-rifle.claim.legacy-scorching-sun::marni-sniper-crafting-2026-03-25`

- evidence_seed_key: "marni-sniper-rifle.claim.legacy-scorching-sun::marni-sniper-crafting-2026-03-25"
- source_id: "marni-sniper-crafting-2026-03-25"
- title: "3월 25일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15352"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-03-25"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "marni-sniper-rifle"
- claim_key: "legacy:scorching-sun-gem-crafting"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: false
- is_active: false
