<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 생활 통합 장비

## Identity

- slug: "life-common-gear"
- name_ko: "생활 통합 장비"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "모든 생활 장비는 가문 장비이며, 액세서리·생활 연금석·청명의 보주는 전역 슬롯, 나머지는 분야별 슬롯을 사용한다."
- purpose: "가문 공용 통합 UI와 전역·분야별 생활 장비 슬롯을 현재 규칙으로 구분한다."

## Requirements

### `life-common-gear.family-wide`

- seed_key: "life-common-gear.family-wide"
- kind: "gear"
- requirement_level: "required"
- title: "가문 공용 장비"
- description: "가문 내 모든 캐릭터가 같은 생활 장비 효과를 사용하며 통합 UI에서 분야별 구성을 저장하고 바로 적용할 수 있다."
- structured_value:

```json
{
  "integrated_ui": true,
  "presets": {
    "apply": true,
    "save": true
  },
  "same_effects_all_characters": true,
  "scope": "family"
}
```

### `life-common-gear.global-slots`

- seed_key: "life-common-gear.global-slots"
- kind: "gear"
- requirement_level: "required"
- title: "전역 생활 슬롯"
- description: "생활 액세서리, 생활 연금석, 청명의 보주는 하나의 장착 구성이 전체 생활 분야에 적용된다."
- structured_value:

```json
{
  "per_life_category_copies": false,
  "slots": [
    "생활 액세서리",
    "생활 연금석",
    "청명의 보주"
  ]
}
```

### `life-common-gear.category-slots`

- seed_key: "life-common-gear.category-slots"
- kind: "gear"
- requirement_level: "required"
- title: "분야별 생활 슬롯"
- description: "의복·도구·유물·광명석 등은 각 생활 분야에 맞는 슬롯을 사용한다."
- structured_value:

```json
{
  "alchemy": [
    "연금복",
    "플라스크",
    "연금 유물/광명석"
  ],
  "cooking": [
    "요리복",
    "국자",
    "요리 유물/광명석"
  ],
  "fishing": [
    "낚시복",
    "낚시 의자",
    "낚싯대",
    "찌",
    "작살",
    "낚시 유물/광명석"
  ],
  "gathering": [
    "채집복",
    "채집 도구",
    "채집 유물/광명석"
  ],
  "hunting": [
    "수렵복",
    "수렵 가방",
    "화승총",
    "저격총",
    "수렵 유물/광명석"
  ],
  "processing": [
    "공예가의 옷",
    "가공석",
    "가공 유물/광명석"
  ],
  "sailing": [
    "항해복",
    "항해 일지",
    "항해 유물/광명석"
  ],
  "training": [
    "조련복",
    "마편",
    "조련 유물/광명석"
  ]
}
```

### `life-common-gear.combat-life-concurrent`

- seed_key: "life-common-gear.combat-life-concurrent"
- kind: "gear"
- requirement_level: "required"
- title: "전투·생활 장비 동시 활용"
- description: "전투 장비와 생활 장비를 동시에 활용하므로 생활 장비 사용을 위해 전투 방어구를 벗는 과거 workflow가 아니다."
- structured_value:

```json
{
  "combat_and_life_equipment_simultaneous": true,
  "remove_combat_gear_for_life": false
}
```

### `life-common-gear.removed-stats`

- seed_key: "life-common-gear.removed-stats"
- kind: "gear"
- requirement_level: "required"
- title: "삭제된 과거 장비 효과"
- description: "통합으로 생활 장비의 일부 방어력과 최대 소지 무게 증가 효과가 삭제됐다."
- structured_value:

```json
{
  "active_legacy_claims_allowed": false,
  "removed_effect_categories": [
    "방어력",
    "최대 소지 무게 증가"
  ]
}
```

### `life-common-gear.cron-meal-weight`

- seed_key: "life-common-gear.cron-meal-weight"
- kind: "item"
- requirement_level: "required"
- title: "해물을 곁들인 크론 정식 변경"
- description: "최대 소지 무게 증가 효과가 기존 100 LT에서 현재 250 LT로 변경됐다."
- structured_value:

```json
{
  "current_max_weight_lt": 250,
  "item": "해물을 곁들인 크론 정식",
  "previous_max_weight_lt": 100
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `life-common-gear.overview`

- seed_key: "life-common-gear.overview"
- section_type: "overview"
- title: "한눈에 보기"
- order_no: 1

#### body_markdown

2026-09-02 적용된 가문 단위 생활 통합 장비 UI 개편을 기준으로 한다.

### `life-common-gear.preparation`

- seed_key: "life-common-gear.preparation"
- section_type: "preparation"
- title: "준비 정보 범위"
- order_no: 2

#### body_markdown

생활 장비 정보는 가문 단위 통합 장비 UI 기준으로 정리한다.

### `life-common-gear.global-slots`

- seed_key: "life-common-gear.global-slots"
- section_type: "overview"
- title: "전체 생활에 적용되는 장비"
- order_no: 3

#### body_markdown

생활 액세서리, 생활 연금석, 청명의 보주는 생활 분야마다 복제하지 않고 전역 슬롯의 장착 효과를 공유한다.

### `life-common-gear.category-slots`

- seed_key: "life-common-gear.category-slots"
- section_type: "overview"
- title: "생활 분야별 장비"
- order_no: 4

#### body_markdown

의복, 도구, 유물과 광명석 등은 채집·가공·낚시·수렵·요리·연금·조련·항해 등 실제 생활 분야별 장비 구성에 저장한다.

### `life-common-gear.legacy-workflow`

- seed_key: "life-common-gear.legacy-workflow"
- section_type: "common_mistakes"
- title: "캐릭터별 장비 교체 방식 아님"
- order_no: 5

#### body_markdown

현재는 모든 생활 장비가 가문 장비이며 전투 장비와 동시에 활용한다. 생활 효과를 받기 위해 캐릭터마다 별도 액세서리 세트를 보유하거나 전투 방어구를 벗는 방식이 아니다.

## Related Contents

### `life-common-gear.accessories`

- seed_key: "life-common-gear.accessories"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-accessory-progression"
- content_name_ko: "생활 액세서리 진행 체계"
- content_category: "life"
- note: "전역 생활 액세서리 슬롯"
- order_no: 1
- relative_path: "../contents/life-accessory-progression.md"
### `life-common-gear.artifacts`

- seed_key: "life-common-gear.artifacts"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-artifacts-lightstones"
- content_name_ko: "생활 유물과 광명석"
- content_category: "life"
- note: "분야별 생활 유물·광명석 슬롯"
- order_no: 2
- relative_path: "../contents/life-artifacts-lightstones.md"
### `life-common-gear.alchemy-stone`

- seed_key: "life-common-gear.alchemy-stone"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-alchemy-stones"
- content_name_ko: "생활 연금석"
- content_category: "life"
- note: "전역 생활 연금석 슬롯"
- order_no: 3
- relative_path: "../contents/life-alchemy-stones.md"
### `life-common-gear.cheongmyeong-orb`

- seed_key: "life-common-gear.cheongmyeong-orb"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "cheongmyeong-orb"
- content_name_ko: "청명의 보주"
- content_category: "life"
- note: "전역 청명의 보주 슬롯"
- order_no: 4
- relative_path: "../contents/cheongmyeong-orb.md"
### `cheongmyeong-orb.integrated-equipment`

- seed_key: "cheongmyeong-orb.integrated-equipment"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "cheongmyeong-orb"
- content_name_ko: "청명의 보주"
- content_category: "life"
- note: "청명의 보주는 전체 생활에 적용되는 전역 슬롯이다."
- order_no: 1
- relative_path: "../contents/cheongmyeong-orb.md"
### `cooking-current-system.common-gear`

- seed_key: "cooking-current-system.common-gear"
- direction: "incoming"
- relation_type: "related"
- content_slug: "cooking-current-system"
- content_name_ko: "요리 현재 시스템"
- content_category: "life"
- note: "생활 공통 장비와 생활 숙련도 기반을 사용한다."
- order_no: 1
- relative_path: "../contents/cooking-current-system.md"
### `life-alchemy-stones.integrated-equipment`

- seed_key: "life-alchemy-stones.integrated-equipment"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "life-alchemy-stones"
- content_name_ko: "생활 연금석"
- content_category: "life"
- note: "생활 연금석은 전체 생활에 적용되는 전역 슬롯이다."
- order_no: 1
- relative_path: "../contents/life-alchemy-stones.md"
### `life-artifacts-lightstones.integrated-equipment`

- seed_key: "life-artifacts-lightstones.integrated-equipment"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "life-artifacts-lightstones"
- content_name_ko: "생활 유물과 광명석"
- content_category: "life"
- note: "유물·광명석은 생활 분야별 장비다."
- order_no: 1
- relative_path: "../contents/life-artifacts-lightstones.md"
### `life-mastery-tools.integrated-equipment`

- seed_key: "life-mastery-tools.integrated-equipment"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "life-mastery-tools"
- content_name_ko: "생활 숙련도 도구"
- content_category: "life"
- note: "생활 분야별 장비 슬롯을 사용한다."
- order_no: 1
- relative_path: "../contents/life-mastery-tools.md"
### `life-accessory-progression.integrated-equipment`

- seed_key: "life-accessory-progression.integrated-equipment"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "life-accessory-progression"
- content_name_ko: "생활 액세서리 진행 체계"
- content_category: "life"
- note: "생활 액세서리는 전역 생활 장비 슬롯을 사용한다."
- order_no: 3
- relative_path: "../contents/life-accessory-progression.md"
### `processing-onboarding-strategy.common-gear`

- seed_key: "processing-onboarding-strategy.common-gear"
- direction: "incoming"
- relation_type: "related"
- content_slug: "processing-onboarding-strategy"
- content_name_ko: "가공 입문 전략"
- content_category: "life"
- note: null
- order_no: 4
- relative_path: "../contents/processing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `life-common-gear.purpose::life-unification-2026-09-02`

- evidence_seed_key: "life-common-gear.purpose::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-common-gear"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "가문 단위 생활 통합 장비 개편"
- active: true
- is_active: true

### `life-common-gear.summary::life-unification-2026-09-02`

- evidence_seed_key: "life-common-gear.summary::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-common-gear"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "가문 장비와 전역·분야별 슬롯"
- active: true
- is_active: true

### `life-common-gear.requirement.category-slots::life-unification-2026-09-02`

- evidence_seed_key: "life-common-gear.requirement.category-slots::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-common-gear.category-slots"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "분야별 장비 분류"
- active: true
- is_active: true

### `life-common-gear.requirement.combat-life-concurrent::life-unification-2026-09-02`

- evidence_seed_key: "life-common-gear.requirement.combat-life-concurrent::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-common-gear.combat-life-concurrent"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "전투·생활 장비 동시 활용"
- active: true
- is_active: true

### `life-common-gear.requirement.cron-meal-weight::life-unification-2026-09-02`

- evidence_seed_key: "life-common-gear.requirement.cron-meal-weight::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-common-gear.cron-meal-weight"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "크론 정식 최대 무게 250 LT"
- active: true
- is_active: true

### `life-common-gear.requirement.family-wide::life-unification-2026-09-02`

- evidence_seed_key: "life-common-gear.requirement.family-wide::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-common-gear.family-wide"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "가문 공용 장비·UI·프리셋"
- active: true
- is_active: true

### `life-common-gear.requirement.global-slots::life-unification-2026-09-02`

- evidence_seed_key: "life-common-gear.requirement.global-slots::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-common-gear.global-slots"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "액세서리·연금석·보주 전역 슬롯"
- active: true
- is_active: true

### `life-common-gear.requirement.removed-stats::life-unification-2026-09-02`

- evidence_seed_key: "life-common-gear.requirement.removed-stats::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-common-gear.removed-stats"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일부 방어력·최대 무게 효과 삭제"
- active: true
- is_active: true

### `life-common-gear.section.overview::life-unification-2026-09-02`

- evidence_seed_key: "life-common-gear.section.overview::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "life-common-gear.overview"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-09-02 개편 기준"
- active: true
- is_active: true

### `life-common-gear.section.preparation::life-unification-2026-09-02`

- evidence_seed_key: "life-common-gear.section.preparation::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "life-common-gear.preparation"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "가문 단위 통합 장비 UI 기준"
- active: true
- is_active: true

### Historical / inactive evidence

### `life-common-gear.legacy.character-specific::life-unification-2026-09-02`

- evidence_seed_key: "life-common-gear.legacy.character-specific::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-common-gear"
- claim_key: "legacy.character_specific_equipment"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "캐릭터별 생활 장비 workflow는 가문 장비로 대체됨"
- active: false
- is_active: false

### `life-common-gear.legacy.defense-weight::life-unification-2026-09-02`

- evidence_seed_key: "life-common-gear.legacy.defense-weight::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-common-gear"
- claim_key: "legacy.defense_and_weight_stats"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "일부 방어력·최대 소지 무게 효과 삭제"
- active: false
- is_active: false
