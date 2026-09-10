<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 가공 입문 전략

## Identity

- slug: "processing-onboarding-strategy"
- name_ko: "가공 입문 전략"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- party_type: null
- difficulty: null

## Overview

- summary: "가공은 먼저 결과물의 실제 사용처를 정하고 재료·가공 방식·일반 또는 대량가공·보관 병목을 한 경로로 검증하는 생활 콘텐츠다."
- purpose: "가격표나 단일 품목 추천 대신 계정의 요리·연금·제작·프로젝트 수요에 맞는 첫 가공 루트를 설계하도록 돕는다."

## Requirements

### `processing-onboarding-strategy.purpose-choice`

- seed_key: "processing-onboarding-strategy.purpose-choice"
- kind: "other"
- requirement_level: "required"
- title: "가공 목적 선택"
- description: "직접 사용, 프로젝트 재료, 후속 제작 또는 판매 중 결과물의 목적을 먼저 정한다."
- structured_value:

```json
{
  "dynamic_market_rank_excluded": true,
  "goals": [
    "downstream_recipe_input",
    "project_material",
    "workshop_input",
    "inventory_transformation",
    "market_sale"
  ],
  "knowledge_role": "strategy",
  "single_default_goal": false
}
```

### `processing-onboarding-strategy.normal-or-mass`

- seed_key: "processing-onboarding-strategy.normal-or-mass"
- kind: "other"
- requirement_level: "required"
- title: "일반·대량가공 선택"
- description: "소량 시험과 새 경로 확인은 일반가공, 지원되는 반복 대량 작업은 가공석과 숙련도를 확인해 대량가공을 검토한다."
- structured_value:

```json
{
  "fixed_quantity_threshold": null,
  "knowledge_role": "strategy",
  "mass_when": [
    "large_repeat_batch",
    "mass_recipe_confirmed",
    "gear_and_mastery_ready"
  ],
  "normal_when": [
    "small_batch",
    "first_route_test",
    "recipe_support_uncertain"
  ],
  "universal_best_mode": false
}
```

### `processing-onboarding-strategy.route-validation`

- seed_key: "processing-onboarding-strategy.route-validation"
- kind: "knowledge"
- requirement_level: "required"
- title: "가공 경로 검증"
- description: "원재료, 가공 방식, 결과물과 후속 사용처를 제작노트·가공 UI의 현재 정보로 확인한다."
- structured_value:

```json
{
  "knowledge_requirement_may_apply": true,
  "knowledge_role": "strategy",
  "recipe_catalog_static": false,
  "route_fields": [
    "input_material",
    "processing_method",
    "output",
    "downstream_use"
  ]
}
```

### `processing-onboarding-strategy.session-bottlenecks`

- seed_key: "processing-onboarding-strategy.session-bottlenecks"
- kind: "other"
- requirement_level: "required"
- title: "세션 병목"
- description: "재료량, 무게, 가방·창고 공간, 성공률과 후속 소비 속도가 세션 길이를 제한한다."
- structured_value:

```json
{
  "bottlenecks": [
    "input_stock",
    "weight",
    "inventory_space",
    "storage_space",
    "processing_success",
    "downstream_consumption"
  ],
  "knowledge_role": "strategy",
  "single_bottleneck_assumed": false
}
```

## Steps

### `processing-onboarding-strategy.step.choose-output`

- seed_key: "processing-onboarding-strategy.step.choose-output"
- phase: "preparation"
- order_no: 1
- title: "필요 결과물 정하기"
- description: "요리·연금·제작·프로젝트 등 실제 후속 사용처에서 필요한 결과물을 하나 고른다."
- checkable: false

### `processing-onboarding-strategy.step.trace-route`

- seed_key: "processing-onboarding-strategy.step.trace-route"
- phase: "preparation"
- order_no: 2
- title: "경로 역산"
- description: "결과물에서 필요한 가공 방식과 원재료를 역산한다."
- checkable: false

### `processing-onboarding-strategy.step.verify-current-recipe`

- seed_key: "processing-onboarding-strategy.step.verify-current-recipe"
- phase: "preparation"
- order_no: 3
- title: "현재 제작식 확인"
- description: "가공 UI와 제작노트에서 현재 제작식, 지식 조건과 대량가공 지원 여부를 확인한다."
- checkable: false

### `processing-onboarding-strategy.step.check-stock`

- seed_key: "processing-onboarding-strategy.step.check-stock"
- phase: "preparation"
- order_no: 4
- title: "재료·보관 점검"
- description: "원재료 재고, 무게와 결과물을 둘 가방·창고 공간을 확인한다."
- checkable: false

### `processing-onboarding-strategy.step.choose-mode`

- seed_key: "processing-onboarding-strategy.step.choose-mode"
- phase: "first_time"
- order_no: 5
- title: "일반·대량가공 고르기"
- description: "첫 소량 시험인지 반복 대량 작업인지에 따라 모드를 선택한다."
- checkable: false

### `processing-onboarding-strategy.step.run-small-test`

- seed_key: "processing-onboarding-strategy.step.run-small-test"
- phase: "first_time"
- order_no: 6
- title: "소량 시험"
- description: "작은 묶음으로 결과물과 후속 사용처가 의도와 맞는지 확인한다."
- checkable: false

### `processing-onboarding-strategy.step.run-record`

- seed_key: "processing-onboarding-strategy.step.run-record"
- phase: "maintenance"
- order_no: 7
- title: "세션 실행·기록"
- description: "중단 원인, 남은 재료, 결과물과 보관 상태를 기록한다."
- checkable: false

### `processing-onboarding-strategy.step.review`

- seed_key: "processing-onboarding-strategy.step.review"
- phase: "maintenance"
- order_no: 8
- title: "병목 조정"
- description: "재료·무게·보관·성공률·후속 소비 중 실제 병목 하나를 다음 세션에서 조정한다."
- checkable: false

## Schedules

- None

## Rewards

- None

## Sections

### `processing-onboarding-strategy.section.output-first`

- seed_key: "processing-onboarding-strategy.section.output-first"
- section_type: "strategy"
- title: "결과물에서 원재료로 역산"
- order_no: 1

#### body_markdown

가공 자체를 목표로 삼기보다 결과물을 어디에 쓸지 먼저 정한다. 원재료→방식→결과물→후속 사용의 연결이 확인된 작은 묶음부터 시작한다.

### `processing-onboarding-strategy.section.mode-bottleneck`

- seed_key: "processing-onboarding-strategy.section.mode-bottleneck"
- section_type: "strategy"
- title: "대량가공은 병목에 맞춰 선택"
- order_no: 2

#### body_markdown

대량가공은 모든 제작식의 기본값이 아니다. 지원되는 제작식인지 확인하고 재료량·무게·보관·후속 소비가 준비된 반복 작업에서 검토한다.

### `processing-onboarding-strategy.section.current-known-issue`

- seed_key: "processing-onboarding-strategy.section.current-known-issue"
- section_type: "common_mistakes"
- title: "현재 제작식과 알려진 문제 확인"
- order_no: 3

#### body_markdown

2026-09-06 기준 가공(L)-공작의 카나페 매듭 제작식에 요리사 모자를 사용할 수 없는 알려진 문제가 있으며 09-09 수정 예정으로 공지됐다. 예정일 이후 실제 수정 여부를 다시 확인한다.

## Related Contents

### `processing-onboarding-strategy.current-system`

- seed_key: "processing-onboarding-strategy.current-system"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "processing-current-system"
- content_name_ko: "가공 현재 시스템"
- content_category: "life"
- note: null
- order_no: 1
- relative_path: "../contents/processing-current-system.md"
### `processing-onboarding-strategy.mass`

- seed_key: "processing-onboarding-strategy.mass"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "mass-processing"
- content_name_ko: "대량가공"
- content_category: "life"
- note: null
- order_no: 2
- relative_path: "../contents/mass-processing.md"
### `processing-onboarding-strategy.gear`

- seed_key: "processing-onboarding-strategy.gear"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "processing-stones-and-clothes"
- content_name_ko: "가공석과 가공복"
- content_category: "life"
- note: null
- order_no: 3
- relative_path: "../contents/processing-stones-and-clothes.md"
### `processing-onboarding-strategy.common-gear`

- seed_key: "processing-onboarding-strategy.common-gear"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-common-gear"
- content_name_ko: "생활 통합 장비"
- content_category: "life"
- note: null
- order_no: 4
- relative_path: "../contents/life-common-gear.md"
### `processing-onboarding-strategy.mastery`

- seed_key: "processing-onboarding-strategy.mastery"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-mastery-foundation"
- content_name_ko: "생활 숙련도 기반"
- content_category: "life"
- note: null
- order_no: 5
- relative_path: "../contents/life-mastery-foundation.md"
### `processing-onboarding-strategy.storage`

- seed_key: "processing-onboarding-strategy.storage"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "storage-current-system"
- content_name_ko: "창고 현재 시스템"
- content_category: "life"
- note: null
- order_no: 6
- relative_path: "../contents/storage-current-system.md"
### `processing-onboarding-strategy.workshop`

- seed_key: "processing-onboarding-strategy.workshop"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "workshop-crafting-logistics"
- content_name_ko: "공방 제작 물류"
- content_category: "life"
- note: null
- order_no: 7
- relative_path: "../contents/workshop-crafting-logistics.md"

## Evidence and Sources

### Current evidence

### `processing-onboarding-strategy.claim.purpose::processing-guide`

- evidence_seed_key: "processing-onboarding-strategy.claim.purpose::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "processing-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.purpose::processing-route-strategy-2026-01-21`

- evidence_seed_key: "processing-onboarding-strategy.claim.purpose::processing-route-strategy-2026-01-21"
- source_id: "processing-route-strategy-2026-01-21"
- title: "무역 5부 - 가공 무역 꿀팁 (완)"
- url: "https://www.inven.co.kr/board/black/3584/58481"
- publisher: "검은사막 인벤 / 엠케이k"
- source_type: "community_strategy"
- published_at: "2026-01-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "processing-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.summary::black-energy-overflow-2026-03-18`

- evidence_seed_key: "processing-onboarding-strategy.claim.summary::black-energy-overflow-2026-03-18"
- source_id: "black-energy-overflow-2026-03-18"
- title: "3월 18일(수) 업데이트 안내 - 검은 기운의 범람지"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15332"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-03-18"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "processing-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.summary::processing-guide`

- evidence_seed_key: "processing-onboarding-strategy.claim.summary::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "processing-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.summary::processing-route-strategy-2026-01-21`

- evidence_seed_key: "processing-onboarding-strategy.claim.summary::processing-route-strategy-2026-01-21"
- source_id: "processing-route-strategy-2026-01-21"
- title: "무역 5부 - 가공 무역 꿀팁 (완)"
- url: "https://www.inven.co.kr/board/black/3584/58481"
- publisher: "검은사막 인벤 / 엠케이k"
- source_type: "community_strategy"
- published_at: "2026-01-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "processing-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.normal-or-mass::processing-guide`

- evidence_seed_key: "processing-onboarding-strategy.claim.normal-or-mass::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "processing-onboarding-strategy.normal-or-mass"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.normal-or-mass::processing-mass-recipes-2026-07-22`

- evidence_seed_key: "processing-onboarding-strategy.claim.normal-or-mass::processing-mass-recipes-2026-07-22"
- source_id: "processing-mass-recipes-2026-07-22"
- title: "7월 22일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Notice/Detail?groupContentNo=15905&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-22"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "processing-onboarding-strategy.normal-or-mass"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.normal-or-mass::processing-route-strategy-2026-01-21`

- evidence_seed_key: "processing-onboarding-strategy.claim.normal-or-mass::processing-route-strategy-2026-01-21"
- source_id: "processing-route-strategy-2026-01-21"
- title: "무역 5부 - 가공 무역 꿀팁 (완)"
- url: "https://www.inven.co.kr/board/black/3584/58481"
- publisher: "검은사막 인벤 / 엠케이k"
- source_type: "community_strategy"
- published_at: "2026-01-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "processing-onboarding-strategy.normal-or-mass"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.purpose-choice::processing-guide`

- evidence_seed_key: "processing-onboarding-strategy.claim.purpose-choice::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "processing-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.purpose-choice::processing-route-strategy-2026-01-21`

- evidence_seed_key: "processing-onboarding-strategy.claim.purpose-choice::processing-route-strategy-2026-01-21"
- source_id: "processing-route-strategy-2026-01-21"
- title: "무역 5부 - 가공 무역 꿀팁 (완)"
- url: "https://www.inven.co.kr/board/black/3584/58481"
- publisher: "검은사막 인벤 / 엠케이k"
- source_type: "community_strategy"
- published_at: "2026-01-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "processing-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.route-validation::black-energy-overflow-2026-03-18`

- evidence_seed_key: "processing-onboarding-strategy.claim.route-validation::black-energy-overflow-2026-03-18"
- source_id: "black-energy-overflow-2026-03-18"
- title: "3월 18일(수) 업데이트 안내 - 검은 기운의 범람지"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15332"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-03-18"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "processing-onboarding-strategy.route-validation"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.route-validation::processing-guide`

- evidence_seed_key: "processing-onboarding-strategy.claim.route-validation::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "processing-onboarding-strategy.route-validation"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.route-validation::processing-mass-recipes-2026-07-22`

- evidence_seed_key: "processing-onboarding-strategy.claim.route-validation::processing-mass-recipes-2026-07-22"
- source_id: "processing-mass-recipes-2026-07-22"
- title: "7월 22일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Notice/Detail?groupContentNo=15905&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-22"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "processing-onboarding-strategy.route-validation"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.session-bottlenecks::processing-guide`

- evidence_seed_key: "processing-onboarding-strategy.claim.session-bottlenecks::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "processing-onboarding-strategy.session-bottlenecks"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.session-bottlenecks::processing-route-strategy-2026-01-21`

- evidence_seed_key: "processing-onboarding-strategy.claim.session-bottlenecks::processing-route-strategy-2026-01-21"
- source_id: "processing-route-strategy-2026-01-21"
- title: "무역 5부 - 가공 무역 꿀팁 (완)"
- url: "https://www.inven.co.kr/board/black/3584/58481"
- publisher: "검은사막 인벤 / 엠케이k"
- source_type: "community_strategy"
- published_at: "2026-01-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "processing-onboarding-strategy.session-bottlenecks"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.section.current-known-issue::known-issues-current-2026-09-04`

- evidence_seed_key: "processing-onboarding-strategy.claim.section.current-known-issue::known-issues-current-2026-09-04"
- source_id: "known-issues-current-2026-09-04"
- title: "알려진 문제점 (최종 수정 : 2026-09-03 17:37)"
- url: "https://www.kr.playblackdesert.com/News/Notice/Detail?groupContentNo=2989&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_known_issues"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "processing-onboarding-strategy.section.current-known-issue"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.section.mode-bottleneck::processing-guide`

- evidence_seed_key: "processing-onboarding-strategy.claim.section.mode-bottleneck::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "processing-onboarding-strategy.section.mode-bottleneck"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.section.mode-bottleneck::processing-mass-recipes-2026-07-22`

- evidence_seed_key: "processing-onboarding-strategy.claim.section.mode-bottleneck::processing-mass-recipes-2026-07-22"
- source_id: "processing-mass-recipes-2026-07-22"
- title: "7월 22일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Notice/Detail?groupContentNo=15905&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-22"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "processing-onboarding-strategy.section.mode-bottleneck"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.section.mode-bottleneck::processing-route-strategy-2026-01-21`

- evidence_seed_key: "processing-onboarding-strategy.claim.section.mode-bottleneck::processing-route-strategy-2026-01-21"
- source_id: "processing-route-strategy-2026-01-21"
- title: "무역 5부 - 가공 무역 꿀팁 (완)"
- url: "https://www.inven.co.kr/board/black/3584/58481"
- publisher: "검은사막 인벤 / 엠케이k"
- source_type: "community_strategy"
- published_at: "2026-01-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "processing-onboarding-strategy.section.mode-bottleneck"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.section.output-first::processing-guide`

- evidence_seed_key: "processing-onboarding-strategy.claim.section.output-first::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "processing-onboarding-strategy.section.output-first"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.section.output-first::processing-route-strategy-2026-01-21`

- evidence_seed_key: "processing-onboarding-strategy.claim.section.output-first::processing-route-strategy-2026-01-21"
- source_id: "processing-route-strategy-2026-01-21"
- title: "무역 5부 - 가공 무역 꿀팁 (완)"
- url: "https://www.inven.co.kr/board/black/3584/58481"
- publisher: "검은사막 인벤 / 엠케이k"
- source_type: "community_strategy"
- published_at: "2026-01-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "processing-onboarding-strategy.section.output-first"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.step.check-stock::processing-guide`

- evidence_seed_key: "processing-onboarding-strategy.claim.step.check-stock::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "processing-onboarding-strategy.step.check-stock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.step.check-stock::processing-route-strategy-2026-01-21`

- evidence_seed_key: "processing-onboarding-strategy.claim.step.check-stock::processing-route-strategy-2026-01-21"
- source_id: "processing-route-strategy-2026-01-21"
- title: "무역 5부 - 가공 무역 꿀팁 (완)"
- url: "https://www.inven.co.kr/board/black/3584/58481"
- publisher: "검은사막 인벤 / 엠케이k"
- source_type: "community_strategy"
- published_at: "2026-01-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "processing-onboarding-strategy.step.check-stock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.step.choose-mode::processing-guide`

- evidence_seed_key: "processing-onboarding-strategy.claim.step.choose-mode::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "processing-onboarding-strategy.step.choose-mode"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.step.choose-mode::processing-mass-recipes-2026-07-22`

- evidence_seed_key: "processing-onboarding-strategy.claim.step.choose-mode::processing-mass-recipes-2026-07-22"
- source_id: "processing-mass-recipes-2026-07-22"
- title: "7월 22일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Notice/Detail?groupContentNo=15905&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-22"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "processing-onboarding-strategy.step.choose-mode"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.step.choose-output::processing-guide`

- evidence_seed_key: "processing-onboarding-strategy.claim.step.choose-output::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "processing-onboarding-strategy.step.choose-output"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.step.choose-output::processing-route-strategy-2026-01-21`

- evidence_seed_key: "processing-onboarding-strategy.claim.step.choose-output::processing-route-strategy-2026-01-21"
- source_id: "processing-route-strategy-2026-01-21"
- title: "무역 5부 - 가공 무역 꿀팁 (완)"
- url: "https://www.inven.co.kr/board/black/3584/58481"
- publisher: "검은사막 인벤 / 엠케이k"
- source_type: "community_strategy"
- published_at: "2026-01-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "processing-onboarding-strategy.step.choose-output"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.step.review::processing-guide`

- evidence_seed_key: "processing-onboarding-strategy.claim.step.review::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "processing-onboarding-strategy.step.review"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.step.review::processing-route-strategy-2026-01-21`

- evidence_seed_key: "processing-onboarding-strategy.claim.step.review::processing-route-strategy-2026-01-21"
- source_id: "processing-route-strategy-2026-01-21"
- title: "무역 5부 - 가공 무역 꿀팁 (완)"
- url: "https://www.inven.co.kr/board/black/3584/58481"
- publisher: "검은사막 인벤 / 엠케이k"
- source_type: "community_strategy"
- published_at: "2026-01-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "processing-onboarding-strategy.step.review"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.step.run-record::black-energy-overflow-2026-03-18`

- evidence_seed_key: "processing-onboarding-strategy.claim.step.run-record::black-energy-overflow-2026-03-18"
- source_id: "black-energy-overflow-2026-03-18"
- title: "3월 18일(수) 업데이트 안내 - 검은 기운의 범람지"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15332"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-03-18"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "processing-onboarding-strategy.step.run-record"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.step.run-record::processing-route-strategy-2026-01-21`

- evidence_seed_key: "processing-onboarding-strategy.claim.step.run-record::processing-route-strategy-2026-01-21"
- source_id: "processing-route-strategy-2026-01-21"
- title: "무역 5부 - 가공 무역 꿀팁 (완)"
- url: "https://www.inven.co.kr/board/black/3584/58481"
- publisher: "검은사막 인벤 / 엠케이k"
- source_type: "community_strategy"
- published_at: "2026-01-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "processing-onboarding-strategy.step.run-record"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.step.run-small-test::processing-guide`

- evidence_seed_key: "processing-onboarding-strategy.claim.step.run-small-test::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "processing-onboarding-strategy.step.run-small-test"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.step.run-small-test::processing-route-strategy-2026-01-21`

- evidence_seed_key: "processing-onboarding-strategy.claim.step.run-small-test::processing-route-strategy-2026-01-21"
- source_id: "processing-route-strategy-2026-01-21"
- title: "무역 5부 - 가공 무역 꿀팁 (완)"
- url: "https://www.inven.co.kr/board/black/3584/58481"
- publisher: "검은사막 인벤 / 엠케이k"
- source_type: "community_strategy"
- published_at: "2026-01-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "processing-onboarding-strategy.step.run-small-test"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.step.trace-route::processing-guide`

- evidence_seed_key: "processing-onboarding-strategy.claim.step.trace-route::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "processing-onboarding-strategy.step.trace-route"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.step.trace-route::processing-route-strategy-2026-01-21`

- evidence_seed_key: "processing-onboarding-strategy.claim.step.trace-route::processing-route-strategy-2026-01-21"
- source_id: "processing-route-strategy-2026-01-21"
- title: "무역 5부 - 가공 무역 꿀팁 (완)"
- url: "https://www.inven.co.kr/board/black/3584/58481"
- publisher: "검은사막 인벤 / 엠케이k"
- source_type: "community_strategy"
- published_at: "2026-01-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "processing-onboarding-strategy.step.trace-route"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.step.verify-current-recipe::black-energy-overflow-2026-03-18`

- evidence_seed_key: "processing-onboarding-strategy.claim.step.verify-current-recipe::black-energy-overflow-2026-03-18"
- source_id: "black-energy-overflow-2026-03-18"
- title: "3월 18일(수) 업데이트 안내 - 검은 기운의 범람지"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15332"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-03-18"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "processing-onboarding-strategy.step.verify-current-recipe"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.step.verify-current-recipe::processing-guide`

- evidence_seed_key: "processing-onboarding-strategy.claim.step.verify-current-recipe::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "processing-onboarding-strategy.step.verify-current-recipe"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `processing-onboarding-strategy.claim.step.verify-current-recipe::processing-mass-recipes-2026-07-22`

- evidence_seed_key: "processing-onboarding-strategy.claim.step.verify-current-recipe::processing-mass-recipes-2026-07-22"
- source_id: "processing-mass-recipes-2026-07-22"
- title: "7월 22일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Notice/Detail?groupContentNo=15905&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-22"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "processing-onboarding-strategy.step.verify-current-recipe"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
