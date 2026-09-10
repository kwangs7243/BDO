<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 생활 분야별 숙련도 효과

## Identity

- slug: "life-mastery-effects"
- name_ko: "생활 분야별 숙련도 효과"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "생활 숙련도는 분야마다 생산량, 성공·보상 확률 또는 관련 능력치에 서로 다른 효과를 준다."
- purpose: "세부 확률표를 복제하지 않고 후속 생활 팩이 공유할 숙련도 효과 분류를 제공한다."

## Requirements

### `life-mastery-effects.effect-taxonomy`

- seed_key: "life-mastery-effects.effect-taxonomy"
- kind: "other"
- requirement_level: "required"
- title: "분야별 효과 분류"
- description: "각 생활 분야의 숙련도 효과는 서로 다른 결과 항목에 적용된다."
- structured_value:

```json
{
  "alchemy": [
    "alchemy_result_effects"
  ],
  "cooking": [
    "mass_cooking",
    "maximum_quantity",
    "higher_grade_rate",
    "imperial_delivery_bonus"
  ],
  "fishing": [
    "treasure_grade_fish_rate"
  ],
  "gathering": [
    "basic_item_rate",
    "basic_item_quantity",
    "special_item_rate",
    "special_item_quantity",
    "rare_item_rate",
    "rare_item_quantity"
  ],
  "hunting": [
    "hunting_gather_quantity"
  ],
  "processing": [
    "mass_processing_throughput"
  ],
  "sailing": [
    "ship_speed",
    "ship_acceleration",
    "ship_turning",
    "ship_braking"
  ],
  "training": [
    "wild_horse_capture_rate",
    "mount_exp",
    "higher_generation_breeding_exchange_rate"
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

### `life-mastery-effects.gathering`

- seed_key: "life-mastery-effects.gathering"
- section_type: "overview"
- title: "채집"
- order_no: 1

#### body_markdown

기본·특수·희귀 채집물의 획득 확률과 획득 수량에 영향을 준다.

### `life-mastery-effects.processing`

- seed_key: "life-mastery-effects.processing"
- section_type: "overview"
- title: "가공"
- order_no: 2

#### body_markdown

대량가공 처리량에 영향을 준다. 가공 성공률은 별도 효과로 구분한다.

### `life-mastery-effects.fishing-hunting`

- seed_key: "life-mastery-effects.fishing-hunting"
- section_type: "overview"
- title: "낚시·수렵"
- order_no: 3

#### body_markdown

낚시는 보물 등급 어종 획득 확률 등에, 수렵은 수렵 채집물 획득 수량 등에 영향을 준다.

### `life-mastery-effects.cooking-alchemy`

- seed_key: "life-mastery-effects.cooking-alchemy"
- section_type: "overview"
- title: "요리·연금"
- order_no: 4

#### body_markdown

요리는 대량 요리, 최대 수량·상위 요리 확률, 황실 제작 납품 보너스에 영향을 주며 연금은 연금 결과에 영향을 준다.

### `life-mastery-effects.training-sailing`

- seed_key: "life-mastery-effects.training-sailing"
- section_type: "overview"
- title: "조련·항해"
- order_no: 5

#### body_markdown

조련은 포획·탑승물 경험치·교배/교환 결과에, 항해는 선박 속도·가속·회전·제동에 영향을 준다.

## Related Contents

### `life-mastery-effects.imperial-delivery`

- seed_key: "life-mastery-effects.imperial-delivery"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "imperial-crafting-delivery-daily"
- content_name_ko: "황실 제작 납품 일일"
- content_category: "life"
- note: "요리 숙련도의 황실 제작 납품 보너스와 기존 일일 납품 주기를 구분한다."
- order_no: 1
- relative_path: "../contents/imperial-crafting-delivery-daily.md"
### `life-mastery-effects.ocean-system`

- seed_key: "life-mastery-effects.ocean-system"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "barter-current-system"
- content_name_ko: "현행 물물교환 시스템"
- content_category: "ocean_barter"
- note: "항해 숙련도는 기존 대양 시스템 데이터와 연결된다."
- order_no: 2
- relative_path: "../contents/barter-current-system.md"
### `life-mastery-foundation.effects`

- seed_key: "life-mastery-foundation.effects"
- direction: "incoming"
- relation_type: "related"
- content_slug: "life-mastery-foundation"
- content_name_ko: "생활 숙련도 기반"
- content_category: "life"
- note: "분야별 숙련도 효과는 별도 Content에서 설명한다."
- order_no: 1
- relative_path: "../contents/life-mastery-foundation.md"
### `processing-current-system.mastery`

- seed_key: "processing-current-system.mastery"
- direction: "incoming"
- relation_type: "related"
- content_slug: "processing-current-system"
- content_name_ko: "가공 현재 시스템"
- content_category: "life"
- note: "가공 숙련도 기반"
- order_no: 1
- relative_path: "../contents/processing-current-system.md"
### `energy-foundation.mastery-effects`

- seed_key: "energy-foundation.mastery-effects"
- direction: "incoming"
- relation_type: "related"
- content_slug: "energy-foundation"
- content_name_ko: "기운 기반"
- content_category: "life"
- note: "채집의 기운 소비와 숙련도의 채집 결과 효과는 서로 다른 규칙이다."
- order_no: 2
- relative_path: "../contents/energy-foundation.md"
### `gathering-current-system.mastery-foundation`

- seed_key: "gathering-current-system.mastery-foundation"
- direction: "incoming"
- relation_type: "related"
- content_slug: "gathering-current-system"
- content_name_ko: "채집 현재 시스템"
- content_category: "life"
- note: "생활 숙련도 공통 효과 재사용"
- order_no: 2
- relative_path: "../contents/gathering-current-system.md"

## Evidence and Sources

### Current evidence

### `life-mastery-effects.summary::life-mastery-prione-2025-01-08`

- evidence_seed_key: "life-mastery-effects.summary::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-mastery-effects"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2025-01-08 생활 숙련도 3000 확장표의 분야별 효과"
- active: true
- is_active: true

### `life-mastery-effects.requirement.effect-taxonomy::life-mastery-prione-2025-01-08`

- evidence_seed_key: "life-mastery-effects.requirement.effect-taxonomy::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-mastery-effects.effect-taxonomy"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "분야별 숙련도 효과 taxonomy"
- active: true
- is_active: true

### `life-mastery-effects.section.cooking-alchemy::life-mastery-prione-2025-01-08`

- evidence_seed_key: "life-mastery-effects.section.cooking-alchemy::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "life-mastery-effects.cooking-alchemy"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "요리·연금"
- active: true
- is_active: true

### `life-mastery-effects.section.fishing-hunting::life-mastery-prione-2025-01-08`

- evidence_seed_key: "life-mastery-effects.section.fishing-hunting::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "life-mastery-effects.fishing-hunting"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "낚시·수렵"
- active: true
- is_active: true

### `life-mastery-effects.section.gathering::life-mastery-prione-2025-01-08`

- evidence_seed_key: "life-mastery-effects.section.gathering::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "life-mastery-effects.gathering"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "채집"
- active: true
- is_active: true

### `life-mastery-effects.section.processing::life-mastery-prione-2025-01-08`

- evidence_seed_key: "life-mastery-effects.section.processing::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "life-mastery-effects.processing"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "가공"
- active: true
- is_active: true

### `life-mastery-effects.section.training-sailing::life-mastery-prione-2025-01-08`

- evidence_seed_key: "life-mastery-effects.section.training-sailing::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "life-mastery-effects.training-sailing"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "조련·항해"
- active: true
- is_active: true

### Historical / inactive evidence

- None
