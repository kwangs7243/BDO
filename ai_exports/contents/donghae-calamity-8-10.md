<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 동해도 팔·구·십재시니

## Identity

- slug: "donghae-calamity-8-10"
- name_ko: "동해도 팔·구·십재시니"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "varies"

## Overview

- summary: "8~10재시니는 빛의 보옥 없이 장착 장비 능력치 100%로 전투한다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `donghae-calamity-8-10.current`

- seed_key: "donghae-calamity-8-10.current"
- kind: "knowledge"
- requirement_level: "required"
- title: "고재시니 능력치 적용"
- description: "8재시니 이상은 빛의 보옥을 사용하지 않고 장비 능력치를 적용한다."
- structured_value:

```json
{
  "calamities": [
    8,
    9,
    10
  ],
  "character_gear_active": true,
  "character_gear_stat_percent": 100,
  "knowledge_role": "fact",
  "light_orb_active": false
}
```

### `donghae-calamity-8-10.duoksini-ap`

- seed_key: "donghae-calamity-8-10.duoksini-ap"
- kind: "knowledge"
- requirement_level: "required"
- title: "두억시니 요구 공격력"
- description: "2026-06-04 추가된 두억시니 8/9/10재시니 공격력 기준이다."
- structured_value:

```json
{
  "ap_by_calamity": {
    "10": 385,
    "8": 365,
    "9": 375
  },
  "boss": "Duoksini",
  "effective_from": "2026-06-04",
  "knowledge_role": "fact"
}
```

### `donghae-calamity-8-10.songakshi-ap`

- seed_key: "donghae-calamity-8-10.songakshi-ap"
- kind: "knowledge"
- requirement_level: "required"
- title: "손각시 요구 공격력"
- description: "2026-07-08 추가된 손각시 8/9/10재시니 공격력 기준이다."
- structured_value:

```json
{
  "ap_by_calamity": {
    "10": 385,
    "8": 365,
    "9": 375
  },
  "boss": "Songakshi",
  "effective_from": "2026-07-08",
  "knowledge_role": "fact"
}
```

### `donghae-calamity-8-10.songakshi-balance`

- seed_key: "donghae-calamity-8-10.songakshi-balance"
- kind: "knowledge"
- requirement_level: "required"
- title: "손각시 최신 조정"
- description: "2026-07-15 기준 피해 감소율은 난이도별 감소하고 생명력은 16.6% 증가했다."
- structured_value:

```json
{
  "boss": "Songakshi",
  "dr_change_percent": {
    "10": -4.6,
    "8": -2.9,
    "9": -1.7
  },
  "effective_from": "2026-07-15",
  "hp_change_percent": 16.6,
  "knowledge_role": "fact"
}
```

### `donghae-calamity-8-10.gumiho-current`

- seed_key: "donghae-calamity-8-10.gumiho-current"
- kind: "knowledge"
- requirement_level: "required"
- title: "구미호 8재시니 최신 조정"
- description: "2026-07-29 기준 요구 공격력 315, 생명력 72% 감소, 공격력 69% 감소다."
- structured_value:

```json
{
  "ap_change_percent": -69,
  "boss": "Gumiho",
  "calamity": 8,
  "effective_from": "2026-07-29",
  "hp_change_percent": -72,
  "knowledge_role": "fact",
  "required_ap": 315
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

### `donghae-calamity-8-10.current-system`

- seed_key: "donghae-calamity-8-10.current-system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "black-shrine-donghae-current-system"
- content_name_ko: "검은사당 동해도 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/black-shrine-donghae-current-system.md"
### `donghae-boss-strategy.high-calamity-system`

- seed_key: "donghae-boss-strategy.high-calamity-system"
- direction: "incoming"
- relation_type: "related"
- content_slug: "donghae-boss-strategy"
- content_name_ko: "동해도 우두머리 전략"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/donghae-boss-strategy.md"

## Evidence and Sources

### Current evidence

### `donghae-calamity-8-10.claim.current::farming-overhaul-2026-06-04`

- evidence_seed_key: "donghae-calamity-8-10.claim.current::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "donghae-calamity-8-10.current"
- claim_key: "requirement:current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `donghae-calamity-8-10.claim.duoksini-ap::farming-overhaul-2026-06-04`

- evidence_seed_key: "donghae-calamity-8-10.claim.duoksini-ap::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "donghae-calamity-8-10.duoksini-ap"
- claim_key: "requirement:duoksini-ap"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `donghae-calamity-8-10.claim.gumiho-current::black-shrine-donghae-guide`

- evidence_seed_key: "donghae-calamity-8-10.claim.gumiho-current::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "donghae-calamity-8-10.gumiho-current"
- claim_key: "requirement:gumiho-current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `donghae-calamity-8-10.claim.songakshi-ap::songakshi-high-calamity-2026-07-08`

- evidence_seed_key: "donghae-calamity-8-10.claim.songakshi-ap::songakshi-high-calamity-2026-07-08"
- source_id: "songakshi-high-calamity-2026-07-08"
- title: "7월 8일 업데이트 안내 - 손각시 팔·구·십재시니"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?groupContentNo=15844"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-07-08"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "donghae-calamity-8-10.songakshi-ap"
- claim_key: "requirement:songakshi-ap"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `donghae-calamity-8-10.claim.songakshi-balance::blood-altar-challenge-2026-07-15`

- evidence_seed_key: "donghae-calamity-8-10.claim.songakshi-balance::blood-altar-challenge-2026-07-15"
- source_id: "blood-altar-challenge-2026-07-15"
- title: "7월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15878"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "donghae-calamity-8-10.songakshi-balance"
- claim_key: "requirement:songakshi-balance"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `donghae-calamity-8-10.claim.gumiho-legacy::black-shrine-donghae-guide`

- evidence_seed_key: "donghae-calamity-8-10.claim.gumiho-legacy::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "donghae-calamity-8-10.gumiho-legacy"
- claim_key: "requirement:gumiho-legacy"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
