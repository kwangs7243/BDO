<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 재배 입문 전략

## Identity

- slug: "farming-onboarding-strategy"
- name_ko: "재배 입문 전략"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- party_type: null
- difficulty: null

## Overview

- summary: "재배는 필요한 재료와 품종개량 목표를 먼저 정하고 현재 성장 주기·울타리·씨앗 제약에 맞춰 반복 가능한 사이클을 설계하는 생활 콘텐츠다."
- purpose: "요리·연금 재료, 품종개량 부산물, 환상마 재료 등 계정 목적에 맞는 첫 재배 루틴을 선택하도록 돕는다."

## Requirements

### `farming-onboarding-strategy.purpose-choice`

- seed_key: "farming-onboarding-strategy.purpose-choice"
- kind: "other"
- requirement_level: "required"
- title: "재배 목적 선택"
- description: "직접 사용할 작물, 품종개량 부산물, 씨앗 유지 중 무엇이 우선인지 정한다."
- structured_value:

```json
{
  "dynamic_market_rank_excluded": true,
  "goals": [
    "cooking_materials",
    "alchemy_materials",
    "breeding_byproducts",
    "dream_horse_materials",
    "seed_continuity"
  ],
  "knowledge_role": "strategy",
  "single_default_goal": false,
  "universal_best_crop": false
}
```

### `farming-onboarding-strategy.harvest-or-breed`

- seed_key: "farming-onboarding-strategy.harvest-or-breed"
- kind: "other"
- requirement_level: "required"
- title: "수확과 품종개량 선택"
- description: "작물 자체가 필요하면 수확, 씨앗과 부산물이 필요하면 품종개량을 우선한다."
- structured_value:

```json
{
  "breed_when": [
    "seed_stock_needed",
    "breeding_byproducts_needed"
  ],
  "harvest_when": [
    "crop_output_needed",
    "downstream_input_needed"
  ],
  "knowledge_role": "strategy",
  "mixed_cycle_supported": true,
  "universal_best_action": false
}
```

### `farming-onboarding-strategy.location-context`

- seed_key: "farming-onboarding-strategy.location-context"
- kind: "other"
- requirement_level: "required"
- title: "위치 선택 기준"
- description: "최단 성장시간만 보지 말고 이동, 창고, 접속 주기와 온도 적합도를 함께 비교한다."
- structured_value:

```json
{
  "decision_dimensions": [
    "travel_time",
    "nearby_storage",
    "login_cadence",
    "temperature_fit",
    "character_parking"
  ],
  "knowledge_role": "strategy",
  "universal_best_location": false
}
```

### `farming-onboarding-strategy.cycle-bottlenecks`

- seed_key: "farming-onboarding-strategy.cycle-bottlenecks"
- kind: "other"
- requirement_level: "required"
- title: "주기 병목"
- description: "완료 시점, 관리 이벤트, 씨앗 재고와 보관 정리가 반복을 끊는 병목이다."
- structured_value:

```json
{
  "bottlenecks": [
    "completion_timing",
    "crop_management_events",
    "seed_stock",
    "inventory_space",
    "storage_cleanup"
  ],
  "fertilizer_as_current_solution": false,
  "knowledge_role": "strategy"
}
```

## Steps

### `farming-onboarding-strategy.step.choose-goal`

- seed_key: "farming-onboarding-strategy.step.choose-goal"
- phase: "preparation"
- order_no: 1
- title: "첫 목적 정하기"
- description: "직접 쓸 재료 또는 품종개량 부산물 중 하나를 우선 목표로 정한다."
- checkable: false

### `farming-onboarding-strategy.step.check-current-facts`

- seed_key: "farming-onboarding-strategy.step.check-current-facts"
- phase: "preparation"
- order_no: 2
- title: "현재 규칙 확인"
- description: "20·21·22시간 성장 주기, 비료 삭제와 6월 후속 조정을 확인한다."
- checkable: false

### `farming-onboarding-strategy.step.choose-crop`

- seed_key: "farming-onboarding-strategy.step.choose-crop"
- phase: "preparation"
- order_no: 3
- title: "작물 고르기"
- description: "실제 후속 사용처와 확보할 씨앗 등급을 기준으로 첫 작물을 고른다."
- checkable: false

### `farming-onboarding-strategy.step.choose-location`

- seed_key: "farming-onboarding-strategy.step.choose-location"
- phase: "preparation"
- order_no: 4
- title: "운영 위치 고르기"
- description: "온도, 이동, 창고와 접속 주기를 포함해 감당 가능한 위치를 정한다."
- checkable: false

### `farming-onboarding-strategy.step.prepare-fence-seeds`

- seed_key: "farming-onboarding-strategy.step.prepare-fence-seeds"
- phase: "first_time"
- order_no: 5
- title: "울타리와 씨앗 준비"
- description: "공헌도와 작물 칸에 맞는 울타리와 다음 사이클까지 이을 씨앗을 준비한다."
- checkable: false

### `farming-onboarding-strategy.step.plan-harvest-breed`

- seed_key: "farming-onboarding-strategy.step.plan-harvest-breed"
- phase: "first_time"
- order_no: 6
- title: "수확·품종개량 비율 정하기"
- description: "필요 작물량과 다음 씨앗 재고를 보고 각 칸의 행동을 나눈다."
- checkable: false

### `farming-onboarding-strategy.step.run-record`

- seed_key: "farming-onboarding-strategy.step.run-record"
- phase: "maintenance"
- order_no: 7
- title: "한 사이클 실행·기록"
- description: "완료 시간, 관리 개입, 결과와 씨앗 잔량을 메모한다."
- checkable: false

### `farming-onboarding-strategy.step.review`

- seed_key: "farming-onboarding-strategy.step.review"
- phase: "maintenance"
- order_no: 8
- title: "다음 사이클 조정"
- description: "실제 병목을 구분하고 한 변수만 조정한다."
- checkable: false

## Schedules

- None

## Rewards

- None

## Sections

### `farming-onboarding-strategy.section.purpose-first`

- seed_key: "farming-onboarding-strategy.section.purpose-first"
- section_type: "strategy"
- title: "목적에서 작물로 역산"
- order_no: 1

#### body_markdown

순간 가격이 아니라 직접 사용할 재료, 부산물 또는 씨앗 유지 목표에서 작물과 수확·품종개량 비율을 역산한다.

### `farming-onboarding-strategy.section.location-cycle`

- seed_key: "farming-onboarding-strategy.section.location-cycle"
- section_type: "strategy"
- title: "위치보다 지속 가능한 주기"
- order_no: 2

#### body_markdown

온도뿐 아니라 이동·창고·접속 주기를 포함한다. 한 사이클을 기록한 뒤 실제 병목에 맞춰 위치나 운영 방식을 조정한다.

### `farming-onboarding-strategy.section.current-rules`

- seed_key: "farming-onboarding-strategy.section.current-rules"
- section_type: "common_mistakes"
- title: "개편 전 공략 제외"
- order_no: 3

#### body_markdown

2026-05-29는 준비 공지이고 06-04 실제 개편 및 06-10·06-17 후속 패치가 현재 기준이다. 과거 비료와 짧은 성장시간 설명을 그대로 따르지 않는다.

## Related Contents

### `farming-onboarding-strategy.current-system`

- seed_key: "farming-onboarding-strategy.current-system"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "farming-current-cycle"
- content_name_ko: "재배 현재 주기"
- content_category: "life"
- note: null
- order_no: 1
- relative_path: "../contents/farming-current-cycle.md"
### `farming-onboarding-strategy.fences`

- seed_key: "farming-onboarding-strategy.fences"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "farming-fences"
- content_name_ko: "재배 울타리"
- content_category: "life"
- note: null
- order_no: 2
- relative_path: "../contents/farming-fences.md"
### `farming-onboarding-strategy.seeds`

- seed_key: "farming-onboarding-strategy.seeds"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "farming-seeds-harvest-breeding"
- content_name_ko: "재배 씨앗·수확·품종개량"
- content_category: "life"
- note: null
- order_no: 3
- relative_path: "../contents/farming-seeds-harvest-breeding.md"
### `farming-onboarding-strategy.pouch`

- seed_key: "farming-onboarding-strategy.pouch"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "old-moon-seed-pouch"
- content_name_ko: "클로의 그믐달 씨앗 주머니"
- content_category: "life"
- note: null
- order_no: 4
- relative_path: "../contents/old-moon-seed-pouch.md"
### `farming-onboarding-strategy.moles`

- seed_key: "farming-onboarding-strategy.moles"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "farming-moles"
- content_name_ko: "재배 두더지와 슈슈"
- content_category: "life"
- note: null
- order_no: 5
- relative_path: "../contents/farming-moles.md"
### `farming-onboarding-strategy.workers`

- seed_key: "farming-onboarding-strategy.workers"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "worker-current-system"
- content_name_ko: "일꾼 현재 시스템"
- content_category: "life"
- note: null
- order_no: 6
- relative_path: "../contents/worker-current-system.md"
### `farming-onboarding-strategy.storage`

- seed_key: "farming-onboarding-strategy.storage"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "storage-current-system"
- content_name_ko: "창고 현재 시스템"
- content_category: "life"
- note: null
- order_no: 7
- relative_path: "../contents/storage-current-system.md"
### `alchemy-onboarding-strategy.farming`

- seed_key: "alchemy-onboarding-strategy.farming"
- direction: "incoming"
- relation_type: "related"
- content_slug: "alchemy-onboarding-strategy"
- content_name_ko: "연금 입문 전략"
- content_category: "life"
- note: null
- order_no: 7
- relative_path: "../contents/alchemy-onboarding-strategy.md"
### `cooking-onboarding-strategy.farming`

- seed_key: "cooking-onboarding-strategy.farming"
- direction: "incoming"
- relation_type: "related"
- content_slug: "cooking-onboarding-strategy"
- content_name_ko: "요리 입문 전략"
- content_category: "life"
- note: null
- order_no: 7
- relative_path: "../contents/cooking-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `farming-onboarding-strategy.claim.purpose::farming-purpose-strategy-2025-09-15`

- evidence_seed_key: "farming-onboarding-strategy.claim.purpose::farming-purpose-strategy-2025-09-15"
- source_id: "farming-purpose-strategy-2025-09-15"
- title: "고인물들이 재배를 하는 이유는?#재배가이드1"
- url: "https://blackdesertonlineyoutube.tistory.com/223"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-09-15"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "farming-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.summary::farming-guide`

- evidence_seed_key: "farming-onboarding-strategy.claim.summary::farming-guide"
- source_id: "farming-guide"
- title: "재배"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=94"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "farming-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.summary::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-onboarding-strategy.claim.summary::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "farming-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.summary::farming-purpose-strategy-2025-09-15`

- evidence_seed_key: "farming-onboarding-strategy.claim.summary::farming-purpose-strategy-2025-09-15"
- source_id: "farming-purpose-strategy-2025-09-15"
- title: "고인물들이 재배를 하는 이유는?#재배가이드1"
- url: "https://blackdesertonlineyoutube.tistory.com/223"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-09-15"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "farming-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.cycle-bottlenecks::farming-onboarding-strategy-2025-09-21`

- evidence_seed_key: "farming-onboarding-strategy.claim.cycle-bottlenecks::farming-onboarding-strategy-2025-09-21"
- source_id: "farming-onboarding-strategy-2025-09-21"
- title: "재배 하는 방법_초급편#재배가이드2"
- url: "https://blackdesertonlineyoutube.tistory.com/226"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-09-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-onboarding-strategy.cycle-bottlenecks"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.cycle-bottlenecks::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-onboarding-strategy.claim.cycle-bottlenecks::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-onboarding-strategy.cycle-bottlenecks"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.cycle-bottlenecks::grind-profit-update-2026-06-10`

- evidence_seed_key: "farming-onboarding-strategy.claim.cycle-bottlenecks::grind-profit-update-2026-06-10"
- source_id: "grind-profit-update-2026-06-10"
- title: "6월 10일(수) 업데이트 안내 (최종 수정 : 2026-06-11 19:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15720"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-06-10"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-onboarding-strategy.cycle-bottlenecks"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.harvest-or-breed::farming-guide`

- evidence_seed_key: "farming-onboarding-strategy.claim.harvest-or-breed::farming-guide"
- source_id: "farming-guide"
- title: "재배"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=94"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-onboarding-strategy.harvest-or-breed"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.harvest-or-breed::farming-purpose-strategy-2025-09-15`

- evidence_seed_key: "farming-onboarding-strategy.claim.harvest-or-breed::farming-purpose-strategy-2025-09-15"
- source_id: "farming-purpose-strategy-2025-09-15"
- title: "고인물들이 재배를 하는 이유는?#재배가이드1"
- url: "https://blackdesertonlineyoutube.tistory.com/223"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-09-15"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-onboarding-strategy.harvest-or-breed"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.location-context::farming-onboarding-strategy-2025-09-21`

- evidence_seed_key: "farming-onboarding-strategy.claim.location-context::farming-onboarding-strategy-2025-09-21"
- source_id: "farming-onboarding-strategy-2025-09-21"
- title: "재배 하는 방법_초급편#재배가이드2"
- url: "https://blackdesertonlineyoutube.tistory.com/226"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-09-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-onboarding-strategy.location-context"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.location-context::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-onboarding-strategy.claim.location-context::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-onboarding-strategy.location-context"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.purpose-choice::farming-purpose-strategy-2025-09-15`

- evidence_seed_key: "farming-onboarding-strategy.claim.purpose-choice::farming-purpose-strategy-2025-09-15"
- source_id: "farming-purpose-strategy-2025-09-15"
- title: "고인물들이 재배를 하는 이유는?#재배가이드1"
- url: "https://blackdesertonlineyoutube.tistory.com/223"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-09-15"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.section.current-rules::farming-market-prep-2026-05-29`

- evidence_seed_key: "farming-onboarding-strategy.claim.section.current-rules::farming-market-prep-2026-05-29"
- source_id: "farming-market-prep-2026-05-29"
- title: "5월 29일(금) 통합 거래소 임시 점검 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Notice/Detail?groupContentNo=15670&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-29"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "farming-onboarding-strategy.section.current-rules"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.section.current-rules::farming-moles-2026-06-17`

- evidence_seed_key: "farming-onboarding-strategy.claim.section.current-rules::farming-moles-2026-06-17"
- source_id: "farming-moles-2026-06-17"
- title: "6월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15751"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "farming-onboarding-strategy.section.current-rules"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.section.current-rules::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-onboarding-strategy.claim.section.current-rules::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "farming-onboarding-strategy.section.current-rules"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.section.current-rules::grind-profit-update-2026-06-10`

- evidence_seed_key: "farming-onboarding-strategy.claim.section.current-rules::grind-profit-update-2026-06-10"
- source_id: "grind-profit-update-2026-06-10"
- title: "6월 10일(수) 업데이트 안내 (최종 수정 : 2026-06-11 19:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15720"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-06-10"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "farming-onboarding-strategy.section.current-rules"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.section.location-cycle::farming-onboarding-strategy-2025-09-21`

- evidence_seed_key: "farming-onboarding-strategy.claim.section.location-cycle::farming-onboarding-strategy-2025-09-21"
- source_id: "farming-onboarding-strategy-2025-09-21"
- title: "재배 하는 방법_초급편#재배가이드2"
- url: "https://blackdesertonlineyoutube.tistory.com/226"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-09-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "farming-onboarding-strategy.section.location-cycle"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.section.location-cycle::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-onboarding-strategy.claim.section.location-cycle::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "farming-onboarding-strategy.section.location-cycle"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.section.purpose-first::farming-purpose-strategy-2025-09-15`

- evidence_seed_key: "farming-onboarding-strategy.claim.section.purpose-first::farming-purpose-strategy-2025-09-15"
- source_id: "farming-purpose-strategy-2025-09-15"
- title: "고인물들이 재배를 하는 이유는?#재배가이드1"
- url: "https://blackdesertonlineyoutube.tistory.com/223"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-09-15"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "farming-onboarding-strategy.section.purpose-first"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.step.check-current-facts::farming-moles-2026-06-17`

- evidence_seed_key: "farming-onboarding-strategy.claim.step.check-current-facts::farming-moles-2026-06-17"
- source_id: "farming-moles-2026-06-17"
- title: "6월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15751"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "farming-onboarding-strategy.step.check-current-facts"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.step.check-current-facts::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-onboarding-strategy.claim.step.check-current-facts::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "farming-onboarding-strategy.step.check-current-facts"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.step.check-current-facts::grind-profit-update-2026-06-10`

- evidence_seed_key: "farming-onboarding-strategy.claim.step.check-current-facts::grind-profit-update-2026-06-10"
- source_id: "grind-profit-update-2026-06-10"
- title: "6월 10일(수) 업데이트 안내 (최종 수정 : 2026-06-11 19:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15720"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-06-10"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "farming-onboarding-strategy.step.check-current-facts"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.step.choose-crop::farming-guide`

- evidence_seed_key: "farming-onboarding-strategy.claim.step.choose-crop::farming-guide"
- source_id: "farming-guide"
- title: "재배"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=94"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "farming-onboarding-strategy.step.choose-crop"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.step.choose-crop::farming-purpose-strategy-2025-09-15`

- evidence_seed_key: "farming-onboarding-strategy.claim.step.choose-crop::farming-purpose-strategy-2025-09-15"
- source_id: "farming-purpose-strategy-2025-09-15"
- title: "고인물들이 재배를 하는 이유는?#재배가이드1"
- url: "https://blackdesertonlineyoutube.tistory.com/223"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-09-15"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "farming-onboarding-strategy.step.choose-crop"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.step.choose-goal::farming-purpose-strategy-2025-09-15`

- evidence_seed_key: "farming-onboarding-strategy.claim.step.choose-goal::farming-purpose-strategy-2025-09-15"
- source_id: "farming-purpose-strategy-2025-09-15"
- title: "고인물들이 재배를 하는 이유는?#재배가이드1"
- url: "https://blackdesertonlineyoutube.tistory.com/223"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-09-15"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "farming-onboarding-strategy.step.choose-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.step.choose-location::farming-onboarding-strategy-2025-09-21`

- evidence_seed_key: "farming-onboarding-strategy.claim.step.choose-location::farming-onboarding-strategy-2025-09-21"
- source_id: "farming-onboarding-strategy-2025-09-21"
- title: "재배 하는 방법_초급편#재배가이드2"
- url: "https://blackdesertonlineyoutube.tistory.com/226"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-09-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "farming-onboarding-strategy.step.choose-location"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.step.choose-location::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-onboarding-strategy.claim.step.choose-location::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "farming-onboarding-strategy.step.choose-location"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.step.plan-harvest-breed::farming-guide`

- evidence_seed_key: "farming-onboarding-strategy.claim.step.plan-harvest-breed::farming-guide"
- source_id: "farming-guide"
- title: "재배"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=94"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "farming-onboarding-strategy.step.plan-harvest-breed"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.step.plan-harvest-breed::farming-purpose-strategy-2025-09-15`

- evidence_seed_key: "farming-onboarding-strategy.claim.step.plan-harvest-breed::farming-purpose-strategy-2025-09-15"
- source_id: "farming-purpose-strategy-2025-09-15"
- title: "고인물들이 재배를 하는 이유는?#재배가이드1"
- url: "https://blackdesertonlineyoutube.tistory.com/223"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-09-15"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "farming-onboarding-strategy.step.plan-harvest-breed"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.step.prepare-fence-seeds::farming-guide`

- evidence_seed_key: "farming-onboarding-strategy.claim.step.prepare-fence-seeds::farming-guide"
- source_id: "farming-guide"
- title: "재배"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=94"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "farming-onboarding-strategy.step.prepare-fence-seeds"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.step.prepare-fence-seeds::farming-onboarding-strategy-2025-09-21`

- evidence_seed_key: "farming-onboarding-strategy.claim.step.prepare-fence-seeds::farming-onboarding-strategy-2025-09-21"
- source_id: "farming-onboarding-strategy-2025-09-21"
- title: "재배 하는 방법_초급편#재배가이드2"
- url: "https://blackdesertonlineyoutube.tistory.com/226"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-09-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "farming-onboarding-strategy.step.prepare-fence-seeds"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.step.review::farming-onboarding-strategy-2025-09-21`

- evidence_seed_key: "farming-onboarding-strategy.claim.step.review::farming-onboarding-strategy-2025-09-21"
- source_id: "farming-onboarding-strategy-2025-09-21"
- title: "재배 하는 방법_초급편#재배가이드2"
- url: "https://blackdesertonlineyoutube.tistory.com/226"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-09-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "farming-onboarding-strategy.step.review"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.step.review::farming-purpose-strategy-2025-09-15`

- evidence_seed_key: "farming-onboarding-strategy.claim.step.review::farming-purpose-strategy-2025-09-15"
- source_id: "farming-purpose-strategy-2025-09-15"
- title: "고인물들이 재배를 하는 이유는?#재배가이드1"
- url: "https://blackdesertonlineyoutube.tistory.com/223"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-09-15"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "farming-onboarding-strategy.step.review"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.step.run-record::farming-onboarding-strategy-2025-09-21`

- evidence_seed_key: "farming-onboarding-strategy.claim.step.run-record::farming-onboarding-strategy-2025-09-21"
- source_id: "farming-onboarding-strategy-2025-09-21"
- title: "재배 하는 방법_초급편#재배가이드2"
- url: "https://blackdesertonlineyoutube.tistory.com/226"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-09-21"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "farming-onboarding-strategy.step.run-record"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `farming-onboarding-strategy.claim.step.run-record::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-onboarding-strategy.claim.step.run-record::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "farming-onboarding-strategy.step.run-record"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
