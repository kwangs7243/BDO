<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 동해도 빛의 보옥 시스템

## Identity

- slug: "donghae-light-orb-system"
- name_ko: "동해도 빛의 보옥 시스템"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "varies"

## Overview

- summary: "1~7재시니에는 현재 빛의 보옥이 적용되고 최대 6개를 장착한다. 8재시니 이상에는 적용되지 않는다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `donghae-light-orb-system.current`

- seed_key: "donghae-light-orb-system.current"
- kind: "knowledge"
- requirement_level: "required"
- title: "1~7재시니 현재 기여"
- description: "1~7재시니는 빛의 보옥 90%, 장비 능력치 10%가 적용된다."
- structured_value:

```json
{
  "calamities": [
    1,
    2,
    3,
    4,
    5,
    6,
    7
  ],
  "character_gear_stat_percent": 10,
  "knowledge_role": "fact",
  "light_orb_active": true,
  "light_orb_stat_percent": 90,
  "max_orbs": 6
}
```

### `donghae-light-orb-system.per-orb`

- seed_key: "donghae-light-orb-system.per-orb"
- kind: "knowledge"
- requirement_level: "required"
- title: "보옥별 효과"
- description: "보옥 하나당 속성 공격력 50, 속성 방어력 100 및 추가 배분 점수 3점을 제공하고 각 점수는 능력 3에 해당한다."
- structured_value:

```json
{
  "ability_per_point": 3,
  "elemental_ap_per_orb": 50,
  "elemental_dp_per_orb": 100,
  "extra_points_per_orb": 3,
  "knowledge_role": "fact"
}
```

### `donghae-light-orb-system.special-rules`

- seed_key: "donghae-light-orb-system.special-rules"
- kind: "knowledge"
- requirement_level: "required"
- title: "속성 전투 고정값"
- description: "속성 치명타 확률은 50%, 우두머리 속성 상태이상 저항은 20%다."
- structured_value:

```json
{
  "boss_elemental_cc_resistance_percent": 20,
  "elemental_critical_chance_percent": 50,
  "knowledge_role": "fact"
}
```

### `donghae-light-orb-system.sixth-orb-unlock`

- seed_key: "donghae-light-orb-system.sixth-orb-unlock"
- kind: "knowledge"
- requirement_level: "required"
- title: "여섯 번째 보옥 해금"
- description: "구미호 설화 지식 보유 후 흑정령 의뢰 '[아침의 나라] 설화깨비의 시련 - 육재시니'로 해금한다."
- structured_value:

```json
{
  "effective_from": "2026-06-04",
  "knowledge_role": "fact",
  "orb_number": 6,
  "quest": "[아침의 나라] 설화깨비의 시련 - 육재시니",
  "requires_knowledge": "Kumiho Tale"
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

### `donghae-light-orb-system.current-system`

- seed_key: "donghae-light-orb-system.current-system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "black-shrine-donghae-current-system"
- content_name_ko: "검은사당 동해도 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/black-shrine-donghae-current-system.md"

## Evidence and Sources

### Current evidence

### `donghae-light-orb-system.claim.current::black-shrine-donghae-guide`

- evidence_seed_key: "donghae-light-orb-system.claim.current::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "donghae-light-orb-system.current"
- claim_key: "requirement:current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `donghae-light-orb-system.claim.current::farming-overhaul-2026-06-04`

- evidence_seed_key: "donghae-light-orb-system.claim.current::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "donghae-light-orb-system.current"
- claim_key: "requirement:current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `donghae-light-orb-system.claim.per-orb::black-shrine-donghae-guide`

- evidence_seed_key: "donghae-light-orb-system.claim.per-orb::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "donghae-light-orb-system.per-orb"
- claim_key: "requirement:per-orb"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `donghae-light-orb-system.claim.sixth-orb-unlock::farming-overhaul-2026-06-04`

- evidence_seed_key: "donghae-light-orb-system.claim.sixth-orb-unlock::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "donghae-light-orb-system.sixth-orb-unlock"
- claim_key: "requirement:sixth-orb-unlock"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `donghae-light-orb-system.claim.special-rules::black-shrine-donghae-guide`

- evidence_seed_key: "donghae-light-orb-system.claim.special-rules::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "donghae-light-orb-system.special-rules"
- claim_key: "requirement:special-rules"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `donghae-light-orb-system.claim.legacy-max-five::farming-overhaul-2026-06-04`

- evidence_seed_key: "donghae-light-orb-system.claim.legacy-max-five::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "donghae-light-orb-system.legacy-max-five"
- claim_key: "requirement:legacy-max-five"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
