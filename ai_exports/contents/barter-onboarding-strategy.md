<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 물물교환 입문 운영 전략

## Identity

- slug: "barter-onboarding-strategy"
- name_ko: "물물교환 입문 운영 전략"
- category: "ocean_barter"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- party_type: null
- difficulty: null

## Overview

- summary: "매 회차 목표와 현재 목록·재고·적재 상태로 작은 항로를 선택하고 단계 재고와 귀환 창고를 함께 관리하는 정적 전략."
- purpose: "실시간 항로 최적화 없이 은화·주화·재료·재고 목적에 맞는 첫 물물교환과 반복 운영 판단을 제공한다."

## Requirements

### `barter-onboarding-strategy.purpose-choice`

- seed_key: "barter-onboarding-strategy.purpose-choice"
- kind: "other"
- requirement_level: "required"
- title: "물물교환 목적 선택"
- description: "은화 판매, 까마귀 주화, 중범선 재료, 다음 항로용 재고, 일일·주간 목표, 일반 성장 중 이번 회차의 목적을 고른다."
- structured_value:

```json
{
  "goals": [
    "silver_sale",
    "crow_coin",
    "carrack_material",
    "stockpile_for_future_routes",
    "daily_or_weekly_objective",
    "general_progression"
  ],
  "knowledge_role": "strategy",
  "single_default_goal": false
}
```

### `barter-onboarding-strategy.current-list-decision`

- seed_key: "barter-onboarding-strategy.current-list-decision"
- kind: "other"
- requirement_level: "required"
- title: "현재 목록 기반 항로 판단"
- description: "현재 목록, 보유 교역품, 적재 무게, 섬 묶음, 귀환 창고, 목적, 남은 교환 횟수와 이동거리를 함께 보고 작은 항로를 고른다."
- structured_value:

```json
{
  "dimensions": [
    "current_list",
    "cargo_weight",
    "owned_trade_goods",
    "island_cluster",
    "return_storage",
    "crow_coin_or_silver_goal",
    "carrack_material_need",
    "remaining_exchange_count",
    "travel_distance"
  ],
  "dynamic_route_excluded": true,
  "knowledge_role": "strategy",
  "runtime_optimizer": false,
  "universal_best_route": false
}
```

### `barter-onboarding-strategy.stage-stock`

- seed_key: "barter-onboarding-strategy.stage-stock"
- kind: "other"
- requirement_level: "required"
- title: "단계별 재고 운영"
- description: "낮은 단계 시작 재고, 중간 단계 연결 재고, 고단계 판매·주화·재료 목적을 구분하되 고정 보유량은 현재 목록과 플레이 주기·선박에 따라 조정한다."
- structured_value:

```json
{
  "depends_on": [
    "current_barter_list",
    "ship_cargo",
    "play_cadence",
    "goal"
  ],
  "fixed_stock_targets": null,
  "knowledge_role": "strategy",
  "stock_groups": [
    "low_tier_start",
    "intermediate_chain",
    "high_tier_goal"
  ]
}
```

### `barter-onboarding-strategy.cargo-storage`

- seed_key: "barter-onboarding-strategy.cargo-storage"
- kind: "other"
- requirement_level: "required"
- title: "적재와 창고 계획"
- description: "출발 재고, 중간 재고, 귀환 화물, 초과분과 다음 회차 예비분을 구분해 적재 한도와 창고 경유를 계획한다."
- structured_value:

```json
{
  "inventory_buckets": [
    "departure_stock",
    "intermediate_stock",
    "return_cargo",
    "overflow",
    "next_cycle_reserve"
  ],
  "knowledge_role": "strategy",
  "new_inventory_schema": false,
  "project_inventory_reused": false
}
```

### `barter-onboarding-strategy.higher-tier-transition`

- seed_key: "barter-onboarding-strategy.higher-tier-transition"
- kind: "other"
- requirement_level: "required"
- title: "6·7단계 전환 판단"
- description: "6·7단계는 초보 기본값이 아니며 선박 적재, 현재 항로, 목적과 낮은 단계 재고 소모 비용을 확인한 뒤 조건부로 선택한다."
- structured_value:

```json
{
  "beginner_default": false,
  "conditions": [
    "ship_cargo",
    "current_route",
    "silver_crow_coin_or_material_goal",
    "lower_tier_stock_cost"
  ],
  "knowledge_role": "strategy",
  "tiers": [
    6,
    7
  ],
  "universal_best_route": false
}
```

## Steps

### `barter-onboarding-strategy.step.choose-goal`

- seed_key: "barter-onboarding-strategy.step.choose-goal"
- phase: "preparation"
- order_no: 1
- title: "이번 회차 목표 정하기"
- description: "은화·주화·재료·재고·반복 목표 중 이번 물물교환의 목적을 고른다."
- checkable: false

### `barter-onboarding-strategy.step.open-current-list`

- seed_key: "barter-onboarding-strategy.step.open-current-list"
- phase: "preparation"
- order_no: 2
- title: "현재 목록 열기"
- description: "현재 게임의 물물교환 목록을 열어 이번 회차 입력값을 확인한다."
- checkable: false

### `barter-onboarding-strategy.step.check-starting-stock`

- seed_key: "barter-onboarding-strategy.step.check-starting-stock"
- phase: "preparation"
- order_no: 3
- title: "시작 재고 확인"
- description: "목록에 필요한 시작 교역품과 보유 재고를 비교한다."
- checkable: false

### `barter-onboarding-strategy.step.check-cargo-capacity`

- seed_key: "barter-onboarding-strategy.step.check-cargo-capacity"
- phase: "preparation"
- order_no: 4
- title: "적재 한도 확인"
- description: "선박 적재 한도와 이미 실린 화물을 확인한다."
- checkable: false

### `barter-onboarding-strategy.step.choose-small-cluster`

- seed_key: "barter-onboarding-strategy.step.choose-small-cluster"
- phase: "preparation"
- order_no: 5
- title: "작은 항로 선택"
- description: "현재 목록과 재고에서 한 항로 또는 가까운 섬 묶음을 선택한다."
- checkable: false

### `barter-onboarding-strategy.step.load-needed-goods`

- seed_key: "barter-onboarding-strategy.step.load-needed-goods"
- phase: "preparation"
- order_no: 6
- title: "필요 교역품 적재"
- description: "선택한 교환에 필요한 교역품만 적재하고 귀환 화물 공간을 남긴다."
- checkable: false

### `barter-onboarding-strategy.step.execute-exchanges`

- seed_key: "barter-onboarding-strategy.step.execute-exchanges"
- phase: "first_time"
- order_no: 7
- title: "교환 실행"
- description: "선택한 순서대로 정박하고 실제 교환을 진행한다."
- checkable: false

### `barter-onboarding-strategy.step.update-stage-stock`

- seed_key: "barter-onboarding-strategy.step.update-stage-stock"
- phase: "first_time"
- order_no: 8
- title: "단계 재고 갱신"
- description: "교환으로 소비·획득한 중간 단계 교역품 재고를 갱신한다."
- checkable: false

### `barter-onboarding-strategy.step.visit-storage-if-needed`

- seed_key: "barter-onboarding-strategy.step.visit-storage-if-needed"
- phase: "maintenance"
- order_no: 9
- title: "필요한 창고 경유"
- description: "적재 한도나 다음 교환 때문에 필요하면 항구·창고를 경유한다."
- checkable: false

### `barter-onboarding-strategy.step.process-result-by-goal`

- seed_key: "barter-onboarding-strategy.step.process-result-by-goal"
- phase: "maintenance"
- order_no: 10
- title: "목적별 결과 처리"
- description: "결과를 은화 판매, 까마귀 주화, 중범선 재료 또는 다음 회차 재고로 처리한다."
- checkable: false

### `barter-onboarding-strategy.step.review-next-refresh`

- seed_key: "barter-onboarding-strategy.step.review-next-refresh"
- phase: "maintenance"
- order_no: 11
- title: "다음 갱신 준비"
- description: "이번 결과를 기준으로 다음 갱신에서 부족한 단계와 시작 재고를 확인한다."
- checkable: false

## Schedules

- None

## Rewards

- None

## Sections

### `barter-onboarding-strategy.section.current-list-route`

- seed_key: "barter-onboarding-strategy.section.current-list-route"
- section_type: "strategy"
- title: "고정 항로 대신 현재 목록으로 판단"
- order_no: 1

#### body_markdown

항로는 현재 물물교환 목록, 보유 재고, 적재 상태, 섬 묶음과 귀환 창고에 따라 매 회차 다시 고른다. 커뮤니티 스케줄러의 알고리즘·점수·순위는 복제하지 않고 입력에 따라 결과가 달라진다는 운영 원칙만 사용한다.

### `barter-onboarding-strategy.section.stage-and-storage`

- seed_key: "barter-onboarding-strategy.section.stage-and-storage"
- section_type: "strategy"
- title: "단계 재고와 창고를 함께 운영"
- order_no: 2

#### body_markdown

낮은 단계는 시작점, 중간 단계는 연결 재고, 고단계는 판매·주화·재료 목적에 맞춰 구분한다. 고정 수량을 정답으로 두지 않고 현재 목록, 선박 적재량과 플레이 주기에 맞춰 창고 경유와 다음 회차 예비분을 정한다.

### `barter-onboarding-strategy.section.common-mistakes`

- seed_key: "barter-onboarding-strategy.section.common-mistakes"
- section_type: "common_mistakes"
- title: "물물교환 입문에서 피할 판단"
- order_no: 3

#### body_markdown

과거 항로 표나 특정 섬을 현재의 보편적 최적 경로로 고정하지 않는다. 전체 목록을 한 번에 처리하려고 과적하거나 귀환 공간 없이 출항하지 않으며, 낮은 단계 재고를 고려하지 않고 6·7단계를 기본 선택으로 삼지 않는다. 동적 시세·시간당 수익·스케줄러 점수는 정적 정본으로 저장하지 않는다.

## Related Contents

### `barter-onboarding-strategy.current-system`

- seed_key: "barter-onboarding-strategy.current-system"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "barter-current-system"
- content_name_ko: "현행 물물교환 시스템"
- content_category: "ocean_barter"
- note: "현행 물물교환 규칙"
- order_no: 1
- relative_path: "../contents/barter-current-system.md"
### `barter-onboarding-strategy.stage-values`

- seed_key: "barter-onboarding-strategy.stage-values"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "barter-stage-values"
- content_name_ko: "물물교환 단계별 가치와 무게"
- content_category: "ocean_barter"
- note: "단계별 가치와 무게 FACT"
- order_no: 2
- relative_path: "../contents/barter-stage-values.md"
### `barter-onboarding-strategy.advanced-route`

- seed_key: "barter-onboarding-strategy.advanced-route"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "barter-route-strategy"
- content_name_ko: "물물교환 동선 전략"
- content_category: "ocean_barter"
- note: "고급 거리 측정·항로 참고"
- order_no: 3
- relative_path: "../contents/barter-route-strategy.md"
### `barter-onboarding-strategy.tier6`

- seed_key: "barter-onboarding-strategy.tier6"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "barter-tier6-routes"
- content_name_ko: "6단계 물물교환 교역로"
- content_category: "ocean_barter"
- note: "6단계 공식 항로"
- order_no: 4
- relative_path: "../contents/barter-tier6-routes.md"
### `barter-onboarding-strategy.tier7`

- seed_key: "barter-onboarding-strategy.tier7"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "barter-tier7-routes"
- content_name_ko: "7단계 물물교환 교역로"
- content_category: "ocean_barter"
- note: "7단계 공식 항로"
- order_no: 5
- relative_path: "../contents/barter-tier7-routes.md"
### `barter-onboarding-strategy.crow-shop`

- seed_key: "barter-onboarding-strategy.crow-shop"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "crow-coin-material-shop"
- content_name_ko: "까마귀 주화 증축 재료 상점"
- content_category: "ocean_project"
- note: "까마귀 주화·재료 목적"
- order_no: 6
- relative_path: "../contents/crow-coin-material-shop.md"
### `barter-onboarding-strategy.advance-project`

- seed_key: "barter-onboarding-strategy.advance-project"
- direction: "outgoing"
- relation_type: "project_link"
- content_slug: "carrack-advance"
- content_name_ko: "에페리아 중범선 : 점진"
- content_category: "ocean_project"
- note: "중범선 점진 재료 목적"
- order_no: 7
- relative_path: "../contents/carrack-advance.md"
### `barter-onboarding-strategy.storage`

- seed_key: "barter-onboarding-strategy.storage"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "storage-current-system"
- content_name_ko: "창고 현재 시스템"
- content_category: "life"
- note: "출발·중간·귀환 재고"
- order_no: 8
- relative_path: "../contents/storage-current-system.md"
### `barter-onboarding-strategy.daily`

- seed_key: "barter-onboarding-strategy.daily"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "ocean-iliya-daily-barter"
- content_name_ko: "[물물교환][일일] 활기찬 일리야 섬"
- content_category: "ocean_project"
- note: "일일 물물교환 목표"
- order_no: 9
- relative_path: "../contents/ocean-iliya-daily-barter.md"
### `barter-onboarding-strategy.weekly`

- seed_key: "barter-onboarding-strategy.weekly"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "iliya-weekly-barter"
- content_name_ko: "[물물교환][주간] 교역의 중심 일리야 섬"
- content_category: "ocean_project"
- note: "주간 물물교환 목표"
- order_no: 10
- relative_path: "../contents/iliya-weekly-barter.md"

## Evidence and Sources

### Current evidence

### `barter-onboarding-strategy.claim.purpose::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.purpose::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "barter-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.purpose::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.purpose::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "barter-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.purpose::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.purpose::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "barter-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.purpose::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.purpose::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "barter-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.summary::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.summary::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "barter-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.summary::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.summary::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "barter-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.summary::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.summary::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "barter-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.summary::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.summary::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "barter-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.cargo-storage::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.cargo-storage::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.cargo-storage"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.cargo-storage::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.cargo-storage::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.cargo-storage"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.cargo-storage::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.cargo-storage::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.cargo-storage"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.cargo-storage::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.cargo-storage::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.cargo-storage"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.current-list-decision::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.current-list-decision::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.current-list-decision"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.current-list-decision::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.current-list-decision::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.current-list-decision"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.current-list-decision::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.current-list-decision::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.current-list-decision"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.current-list-decision::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.current-list-decision::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.current-list-decision"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.higher-tier-transition::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.higher-tier-transition::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.higher-tier-transition"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.higher-tier-transition::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.higher-tier-transition::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.higher-tier-transition"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.higher-tier-transition::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.higher-tier-transition::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.higher-tier-transition"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.higher-tier-transition::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.higher-tier-transition::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.higher-tier-transition"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.purpose-choice::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.purpose-choice::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.purpose-choice::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.purpose-choice::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.purpose-choice::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.purpose-choice::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.purpose-choice::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.purpose-choice::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.stage-stock::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.stage-stock::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.stage-stock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.stage-stock::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.stage-stock::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.stage-stock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.stage-stock::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.stage-stock::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.stage-stock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.stage-stock::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.stage-stock::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-onboarding-strategy.stage-stock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.section.common-mistakes::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.section.common-mistakes::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "barter-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.section.common-mistakes::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.section.common-mistakes::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "barter-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.section.common-mistakes::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.section.common-mistakes::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "barter-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.section.common-mistakes::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.section.common-mistakes::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "barter-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.section.current-list-route::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.section.current-list-route::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "barter-onboarding-strategy.section.current-list-route"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.section.current-list-route::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.section.current-list-route::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "barter-onboarding-strategy.section.current-list-route"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.section.current-list-route::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.section.current-list-route::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "barter-onboarding-strategy.section.current-list-route"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.section.current-list-route::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.section.current-list-route::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "barter-onboarding-strategy.section.current-list-route"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.section.stage-and-storage::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.section.stage-and-storage::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "barter-onboarding-strategy.section.stage-and-storage"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.section.stage-and-storage::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.section.stage-and-storage::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "barter-onboarding-strategy.section.stage-and-storage"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.section.stage-and-storage::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.section.stage-and-storage::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "barter-onboarding-strategy.section.stage-and-storage"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.section.stage-and-storage::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.section.stage-and-storage::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "barter-onboarding-strategy.section.stage-and-storage"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.check-cargo-capacity::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.check-cargo-capacity::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.check-cargo-capacity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.check-cargo-capacity::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.check-cargo-capacity::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.check-cargo-capacity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.check-cargo-capacity::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.check-cargo-capacity::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.check-cargo-capacity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.check-cargo-capacity::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.check-cargo-capacity::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.check-cargo-capacity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.check-starting-stock::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.check-starting-stock::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.check-starting-stock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.check-starting-stock::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.check-starting-stock::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.check-starting-stock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.check-starting-stock::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.check-starting-stock::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.check-starting-stock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.check-starting-stock::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.check-starting-stock::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.check-starting-stock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.choose-goal::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.choose-goal::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.choose-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.choose-goal::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.choose-goal::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.choose-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.choose-goal::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.choose-goal::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.choose-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.choose-goal::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.choose-goal::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.choose-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.choose-small-cluster::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.choose-small-cluster::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.choose-small-cluster"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.choose-small-cluster::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.choose-small-cluster::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.choose-small-cluster"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.choose-small-cluster::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.choose-small-cluster::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.choose-small-cluster"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.choose-small-cluster::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.choose-small-cluster::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.choose-small-cluster"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.execute-exchanges::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.execute-exchanges::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.execute-exchanges"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.execute-exchanges::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.execute-exchanges::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.execute-exchanges"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.execute-exchanges::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.execute-exchanges::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.execute-exchanges"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.execute-exchanges::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.execute-exchanges::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.execute-exchanges"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.load-needed-goods::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.load-needed-goods::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.load-needed-goods"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.load-needed-goods::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.load-needed-goods::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.load-needed-goods"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.load-needed-goods::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.load-needed-goods::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.load-needed-goods"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.load-needed-goods::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.load-needed-goods::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.load-needed-goods"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.open-current-list::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.open-current-list::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.open-current-list"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.open-current-list::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.open-current-list::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.open-current-list"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.open-current-list::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.open-current-list::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.open-current-list"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.open-current-list::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.open-current-list::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.open-current-list"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.process-result-by-goal::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.process-result-by-goal::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.process-result-by-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.process-result-by-goal::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.process-result-by-goal::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.process-result-by-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.process-result-by-goal::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.process-result-by-goal::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.process-result-by-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.process-result-by-goal::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.process-result-by-goal::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.process-result-by-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.review-next-refresh::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.review-next-refresh::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.review-next-refresh"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.review-next-refresh::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.review-next-refresh::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.review-next-refresh"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.review-next-refresh::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.review-next-refresh::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.review-next-refresh"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.review-next-refresh::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.review-next-refresh::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.review-next-refresh"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.update-stage-stock::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.update-stage-stock::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.update-stage-stock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.update-stage-stock::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.update-stage-stock::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.update-stage-stock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.update-stage-stock::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.update-stage-stock::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.update-stage-stock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.update-stage-stock::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.update-stage-stock::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.update-stage-stock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.visit-storage-if-needed::barter-accessibility-2026-05-20`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.visit-storage-if-needed::barter-accessibility-2026-05-20"
- source_id: "barter-accessibility-2026-05-20"
- title: "5월 20일(수) 업데이트 안내 (최종 수정 : 2026-06-16 16:26)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15614"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-05-20"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.visit-storage-if-needed"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.visit-storage-if-needed::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.visit-storage-if-needed::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.visit-storage-if-needed"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.visit-storage-if-needed::barter-scheduler-strategy-2026-06-06`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.visit-storage-if-needed::barter-scheduler-strategy-2026-06-06"
- source_id: "barter-scheduler-strategy-2026-06-06"
- title: "[항해] 물물교환 지능형 스케쥴러 시스템 배포 및 가이드 (BY 송도조씨)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152762"
- publisher: "Delicate-KR"
- source_type: "community_strategy"
- published_at: "2026-06-06"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.visit-storage-if-needed"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `barter-onboarding-strategy.claim.step.visit-storage-if-needed::sailing-academy-community-2026-06-14`

- evidence_seed_key: "barter-onboarding-strategy.claim.step.visit-storage-if-needed::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "barter-onboarding-strategy.step.visit-storage-if-needed"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
