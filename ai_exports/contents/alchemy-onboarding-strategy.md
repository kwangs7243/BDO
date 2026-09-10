<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 연금 입문 전략

## Identity

- slug: "alchemy-onboarding-strategy"
- name_ko: "연금 입문 전략"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- party_type: null
- difficulty: null

## Overview

- summary: "연금 목적과 최종 결과물을 정하고 현재 제작식, 중간재 연결, 재료 공급 병목과 결과물 처리 경로를 역산하는 생활 전략 콘텐츠다."
- purpose: "전체 제작식이나 고정 수익표 없이 목표 결과물에서 첫 소량 제작과 다음 공급 행동까지 안전하게 결정하도록 돕는다."

## Requirements

### `alchemy-onboarding-strategy.purpose-choice`

- seed_key: "alchemy-onboarding-strategy.purpose-choice"
- kind: "other"
- requirement_level: "required"
- title: "연금 목적 선택"
- description: "직접 사용할 비약·향수·연금 결과, 다른 제작 중간재, Project 재료, 황실 연금 납품, 시장 판매, 연금 경험치 성장 중 우선 목적을 정한다."
- structured_value:

```json
{
  "alchemy_stone_growth_separate": true,
  "goals": [
    "direct_elixir_perfume_or_alchemy_use",
    "crafting_intermediate",
    "project_material",
    "imperial_alchemy_delivery",
    "market_sale",
    "alchemy_experience_growth"
  ],
  "knowledge_role": "strategy",
  "single_default_goal": false
}
```

### `alchemy-onboarding-strategy.dependency-chain`

- seed_key: "alchemy-onboarding-strategy.dependency-chain"
- kind: "knowledge"
- requirement_level: "required"
- title: "최종 결과물에서 공급까지 역산"
- description: "최종 결과물에서 중간 연금재, 혈액·오일·시약·흔적·수액·식물 등의 하위 재료와 실제 확보 경로 순서로 거슬러 내려간다."
- structured_value:

```json
{
  "full_recipe_catalog": false,
  "knowledge_role": "strategy",
  "reverse_chain": [
    "final_product",
    "alchemy_intermediate",
    "blood_oil_reagent_trace_sap_plant",
    "acquisition_route"
  ],
  "verify_current_recipe_per_target": true
}
```

### `alchemy-onboarding-strategy.recipe-validation`

- seed_key: "alchemy-onboarding-strategy.recipe-validation"
- kind: "knowledge"
- requirement_level: "required"
- title: "정확한 비율과 소량 검증"
- description: "제작 노트에서 현재 재료 비율을 확인하고, 잘못된 수량으로 실패해도 재료가 소비될 수 있으므로 첫 제작은 작은 묶음으로 검증한다."
- structured_value:

```json
{
  "current_recipe_check_required": true,
  "failure_may_consume_materials": true,
  "first_batch": "small",
  "knowledge_role": "strategy",
  "static_recipe_catalog": false
}
```

### `alchemy-onboarding-strategy.ingredient-sourcing`

- seed_key: "alchemy-onboarding-strategy.ingredient-sourcing"
- kind: "other"
- requirement_level: "required"
- title: "재료별 병목과 공급 경로"
- description: "목표 제작식마다 직접 채집, 수렵 연계, 생산 노드, 재배, 거래소, 교환과 황실 인장, 기존 재고 중 공급 경로와 실제 병목을 확인한다."
- structured_value:

```json
{
  "bottleneck_depends_on_recipe": true,
  "knowledge_role": "strategy",
  "supply_routes": [
    "gathering",
    "hunting_link",
    "production_node",
    "farming",
    "marketplace",
    "exchange_or_imperial_seal",
    "owned_inventory"
  ],
  "universal_bottleneck_material": false
}
```

### `alchemy-onboarding-strategy.imperial-and-output-decision`

- seed_key: "alchemy-onboarding-strategy.imperial-and-output-decision"
- kind: "other"
- requirement_level: "required"
- title: "결과물과 황실 연금 판단"
- description: "직접 사용, 황실 납품, 후속 제작, 판매 중 출구를 고르고 재료비와 조달 상태를 확인해 직접 제작과 외부 조달을 조건부로 비교한다."
- structured_value:

```json
{
  "alchemy_stone_progression_is_advanced_path": true,
  "compare_self_craft_and_external_supply": true,
  "dynamic_market_rank_excluded": true,
  "fixed_margin_threshold": null,
  "knowledge_role": "strategy",
  "outlets": [
    "direct_use",
    "imperial_alchemy_delivery",
    "downstream_crafting",
    "market_sale"
  ],
  "universal_best_product": false
}
```

## Steps

### `alchemy-onboarding-strategy.step.choose-final-output`

- seed_key: "alchemy-onboarding-strategy.step.choose-final-output"
- phase: "preparation"
- order_no: 1
- title: "최종 결과물 선택"
- description: "직접 사용, 중간재, Project, 황실 납품, 판매 또는 성장 중 목적에 맞는 최종 결과물을 하나 정한다."
- checkable: false

### `alchemy-onboarding-strategy.step.verify-recipe`

- seed_key: "alchemy-onboarding-strategy.step.verify-recipe"
- phase: "preparation"
- order_no: 2
- title: "현재 제작식 확인"
- description: "게임의 제작 노트에서 현재 재료 종류와 정확한 비율을 확인한다."
- checkable: false

### `alchemy-onboarding-strategy.step.trace-intermediates`

- seed_key: "alchemy-onboarding-strategy.step.trace-intermediates"
- phase: "preparation"
- order_no: 3
- title: "중간 재료 역산"
- description: "중간 연금재가 있다면 최종 결과물에서 하위 재료와 확보 경로까지 역산한다."
- checkable: false

### `alchemy-onboarding-strategy.step.classify-shortages`

- seed_key: "alchemy-onboarding-strategy.step.classify-shortages"
- phase: "preparation"
- order_no: 4
- title: "부족 재료 분류"
- description: "보유 재고와 필요량을 비교하고 부족분을 채집, 수렵, 노드, 재배, 거래소, 교환 경로로 나눈다."
- checkable: false

### `alchemy-onboarding-strategy.step.confirm-ratios`

- seed_key: "alchemy-onboarding-strategy.step.confirm-ratios"
- phase: "preparation"
- order_no: 5
- title: "재료 비율 재확인"
- description: "실패 시 재료 소비 위험을 줄이도록 투입 전에 각 재료 비율과 대체 가능 여부를 다시 확인한다."
- checkable: false

### `alchemy-onboarding-strategy.step.run-small-batch`

- seed_key: "alchemy-onboarding-strategy.step.run-small-batch"
- phase: "first_time"
- order_no: 6
- title: "소량 제작 검증"
- description: "작은 묶음으로 제작 성공과 결과물, 중간재 연결을 확인한다."
- checkable: false

### `alchemy-onboarding-strategy.step.choose-repeat-volume`

- seed_key: "alchemy-onboarding-strategy.step.choose-repeat-volume"
- phase: "first_time"
- order_no: 7
- title: "반복량 결정"
- description: "검증 결과와 안정적으로 확보 가능한 재료량을 기준으로 이번 반복량을 정한다."
- checkable: false

### `alchemy-onboarding-strategy.step.check-stock-space`

- seed_key: "alchemy-onboarding-strategy.step.check-stock-space"
- phase: "maintenance"
- order_no: 8
- title: "재고와 공간 확인"
- description: "반복 전에 핵심 재료 재고, 가방, 창고, 결과물 보관 공간을 확인한다."
- checkable: false

### `alchemy-onboarding-strategy.step.choose-outlet`

- seed_key: "alchemy-onboarding-strategy.step.choose-outlet"
- phase: "maintenance"
- order_no: 9
- title: "결과물 처리 결정"
- description: "직접 사용, 황실 납품, 후속 제작, 보관 또는 판매 중 현재 목적에 맞는 출구를 선택한다."
- checkable: false

### `alchemy-onboarding-strategy.step.improve-one-bottleneck`

- seed_key: "alchemy-onboarding-strategy.step.improve-one-bottleneck"
- phase: "maintenance"
- order_no: 10
- title: "다음 병목 하나 개선"
- description: "세션에서 가장 먼저 부족해진 재료나 공간 문제 하나만 골라 다음 반복 전에 개선한다."
- checkable: false

## Schedules

- None

## Rewards

- None

## Sections

### `alchemy-onboarding-strategy.section.reverse-dependency`

- seed_key: "alchemy-onboarding-strategy.section.reverse-dependency"
- section_type: "strategy"
- title: "최종 결과물에서 재료 공급망까지 역산"
- order_no: 1

#### body_markdown

연금 전체 제작식을 고정 목록으로 복제하지 않는다. 필요한 최종 결과물 하나에서 중간재와 하위 재료를 거슬러 내려가고, 제작 노트의 현재 식과 실제 공급 경로를 확인한다.

### `alchemy-onboarding-strategy.section.supply-imperial`

- seed_key: "alchemy-onboarding-strategy.section.supply-imperial"
- section_type: "strategy"
- title: "병목과 결과물 출구를 분리해 판단"
- order_no: 2

#### body_markdown

병목은 목표 제작식과 보유 재고에 따라 달라진다. 재료 공급을 확인한 뒤 직접 사용, 황실 납품, 후속 제작, 판매 중 출구를 고르며, 현재 가격이 필요한 판단은 그 시점에 별도로 확인한다.

### `alchemy-onboarding-strategy.section.common-mistakes`

- seed_key: "alchemy-onboarding-strategy.section.common-mistakes"
- section_type: "common_mistakes"
- title: "연금 입문에서 피할 판단"
- order_no: 3

#### body_markdown

재료 비율 확인 없이 대량 반복하거나 중간재 연결을 건너뛰고 최종 물품부터 쌓지 않는다. 오래된 황실 손익표를 현재 가치로 사용하지 않고, 연금석 성장을 일반 연금 생산과 섞거나 모든 연금에서 같은 재료가 병목이라고 가정하지 않는다.

## Related Contents

### `alchemy-onboarding-strategy.current-system`

- seed_key: "alchemy-onboarding-strategy.current-system"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "alchemy-current-system"
- content_name_ko: "연금 현재 시스템"
- content_category: "life"
- note: null
- order_no: 1
- relative_path: "../contents/alchemy-current-system.md"
### `alchemy-onboarding-strategy.mastery`

- seed_key: "alchemy-onboarding-strategy.mastery"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "alchemy-mastery-effects"
- content_name_ko: "연금 숙련도 효과"
- content_category: "life"
- note: null
- order_no: 2
- relative_path: "../contents/alchemy-mastery-effects.md"
### `alchemy-onboarding-strategy.products`

- seed_key: "alchemy-onboarding-strategy.products"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "alchemy-products-and-byproducts"
- content_name_ko: "연금 결과물과 부산물"
- content_category: "life"
- note: null
- order_no: 3
- relative_path: "../contents/alchemy-products-and-byproducts.md"
### `alchemy-onboarding-strategy.imperial`

- seed_key: "alchemy-onboarding-strategy.imperial"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "alchemy-imperial-current"
- content_name_ko: "황실 연금 현재 상자표"
- content_category: "life"
- note: null
- order_no: 4
- relative_path: "../contents/alchemy-imperial-current.md"
### `alchemy-onboarding-strategy.growth`

- seed_key: "alchemy-onboarding-strategy.growth"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "alchemy-growth-surprise-quest"
- content_name_ko: "연금 성장 깜짝 의뢰"
- content_category: "life"
- note: null
- order_no: 5
- relative_path: "../contents/alchemy-growth-surprise-quest.md"
### `alchemy-onboarding-strategy.gathering`

- seed_key: "alchemy-onboarding-strategy.gathering"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "gathering-onboarding-strategy"
- content_name_ko: "채집 입문 전략"
- content_category: "life"
- note: null
- order_no: 6
- relative_path: "../contents/gathering-onboarding-strategy.md"
### `alchemy-onboarding-strategy.farming`

- seed_key: "alchemy-onboarding-strategy.farming"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "farming-onboarding-strategy"
- content_name_ko: "재배 입문 전략"
- content_category: "life"
- note: null
- order_no: 7
- relative_path: "../contents/farming-onboarding-strategy.md"
### `alchemy-onboarding-strategy.production-nodes`

- seed_key: "alchemy-onboarding-strategy.production-nodes"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "production-node-current-system"
- content_name_ko: "생산 거점 현재 시스템"
- content_category: "life"
- note: null
- order_no: 8
- relative_path: "../contents/production-node-current-system.md"
### `alchemy-onboarding-strategy.storage`

- seed_key: "alchemy-onboarding-strategy.storage"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "storage-current-system"
- content_name_ko: "창고 현재 시스템"
- content_category: "life"
- note: null
- order_no: 9
- relative_path: "../contents/storage-current-system.md"
### `alchemy-onboarding-strategy.alchemy-stone-next`

- seed_key: "alchemy-onboarding-strategy.alchemy-stone-next"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "alchemy-stone-current-progression"
- content_name_ko: "연금석 현재 성장 체계"
- content_category: "life"
- note: null
- order_no: 10
- relative_path: "../contents/alchemy-stone-current-progression.md"

## Evidence and Sources

### Current evidence

### `alchemy-onboarding-strategy.claim.purpose::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.purpose::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.purpose::alchemy-imperial-strategy-2024-11-09`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.purpose::alchemy-imperial-strategy-2024-11-09"
- source_id: "alchemy-imperial-strategy-2024-11-09"
- title: "연금 황실 납품 가격#연금황납#연금"
- url: "https://blackdesertonlineyoutube.tistory.com/169"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-11-09"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.purpose::alchemy-node-strategy-2025-10-28`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.purpose::alchemy-node-strategy-2025-10-28"
- source_id: "alchemy-node-strategy-2025-10-28"
- title: "[25년 10월] 돌릴만한 노드 추천"
- url: "https://www.kr.playblackdesert.com/ko-kr/Forum/ForumTopic/Detail?_opinionNo=0&_topicNo=142101"
- publisher: "새별-KR"
- source_type: "community_strategy"
- published_at: "2025-10-28"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.summary::alchemy-basic-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.summary::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.summary::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.summary::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.summary::alchemy-node-strategy-2025-10-28`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.summary::alchemy-node-strategy-2025-10-28"
- source_id: "alchemy-node-strategy-2025-10-28"
- title: "[25년 10월] 돌릴만한 노드 추천"
- url: "https://www.kr.playblackdesert.com/ko-kr/Forum/ForumTopic/Detail?_opinionNo=0&_topicNo=142101"
- publisher: "새별-KR"
- source_type: "community_strategy"
- published_at: "2025-10-28"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.dependency-chain::alchemy-basic-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.dependency-chain::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "alchemy-onboarding-strategy.dependency-chain"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.dependency-chain::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.dependency-chain::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "alchemy-onboarding-strategy.dependency-chain"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.dependency-chain::alchemy-node-strategy-2025-10-28`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.dependency-chain::alchemy-node-strategy-2025-10-28"
- source_id: "alchemy-node-strategy-2025-10-28"
- title: "[25년 10월] 돌릴만한 노드 추천"
- url: "https://www.kr.playblackdesert.com/ko-kr/Forum/ForumTopic/Detail?_opinionNo=0&_topicNo=142101"
- publisher: "새별-KR"
- source_type: "community_strategy"
- published_at: "2025-10-28"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "alchemy-onboarding-strategy.dependency-chain"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.imperial-and-output-decision::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.imperial-and-output-decision::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "alchemy-onboarding-strategy.imperial-and-output-decision"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.imperial-and-output-decision::alchemy-imperial-strategy-2024-11-09`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.imperial-and-output-decision::alchemy-imperial-strategy-2024-11-09"
- source_id: "alchemy-imperial-strategy-2024-11-09"
- title: "연금 황실 납품 가격#연금황납#연금"
- url: "https://blackdesertonlineyoutube.tistory.com/169"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-11-09"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "alchemy-onboarding-strategy.imperial-and-output-decision"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.imperial-and-output-decision::imperial-delivery-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.imperial-and-output-decision::imperial-delivery-guide"
- source_id: "imperial-delivery-guide"
- title: "황실 납품"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=109"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "alchemy-onboarding-strategy.imperial-and-output-decision"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.imperial-and-output-decision::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.imperial-and-output-decision::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "alchemy-onboarding-strategy.imperial-and-output-decision"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.ingredient-sourcing::alchemy-basic-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.ingredient-sourcing::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "alchemy-onboarding-strategy.ingredient-sourcing"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.ingredient-sourcing::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.ingredient-sourcing::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "alchemy-onboarding-strategy.ingredient-sourcing"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.ingredient-sourcing::alchemy-node-strategy-2025-10-28`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.ingredient-sourcing::alchemy-node-strategy-2025-10-28"
- source_id: "alchemy-node-strategy-2025-10-28"
- title: "[25년 10월] 돌릴만한 노드 추천"
- url: "https://www.kr.playblackdesert.com/ko-kr/Forum/ForumTopic/Detail?_opinionNo=0&_topicNo=142101"
- publisher: "새별-KR"
- source_type: "community_strategy"
- published_at: "2025-10-28"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "alchemy-onboarding-strategy.ingredient-sourcing"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.purpose-choice::alchemy-basic-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.purpose-choice::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "alchemy-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.purpose-choice::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.purpose-choice::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "alchemy-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.purpose-choice::alchemy-node-strategy-2025-10-28`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.purpose-choice::alchemy-node-strategy-2025-10-28"
- source_id: "alchemy-node-strategy-2025-10-28"
- title: "[25년 10월] 돌릴만한 노드 추천"
- url: "https://www.kr.playblackdesert.com/ko-kr/Forum/ForumTopic/Detail?_opinionNo=0&_topicNo=142101"
- publisher: "새별-KR"
- source_type: "community_strategy"
- published_at: "2025-10-28"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "alchemy-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.recipe-validation::alchemy-basic-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.recipe-validation::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "alchemy-onboarding-strategy.recipe-validation"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.recipe-validation::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.recipe-validation::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "alchemy-onboarding-strategy.recipe-validation"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.section.common-mistakes::alchemy-basic-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.section.common-mistakes::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "alchemy-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.section.common-mistakes::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.section.common-mistakes::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "alchemy-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.section.common-mistakes::alchemy-imperial-strategy-2024-11-09`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.section.common-mistakes::alchemy-imperial-strategy-2024-11-09"
- source_id: "alchemy-imperial-strategy-2024-11-09"
- title: "연금 황실 납품 가격#연금황납#연금"
- url: "https://blackdesertonlineyoutube.tistory.com/169"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-11-09"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "alchemy-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.section.common-mistakes::alchemy-stone-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.section.common-mistakes::alchemy-stone-guide"
- source_id: "alchemy-stone-guide"
- title: "연금석"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=101"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "alchemy-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.section.reverse-dependency::alchemy-basic-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.section.reverse-dependency::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "alchemy-onboarding-strategy.section.reverse-dependency"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.section.reverse-dependency::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.section.reverse-dependency::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "alchemy-onboarding-strategy.section.reverse-dependency"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.section.reverse-dependency::alchemy-node-strategy-2025-10-28`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.section.reverse-dependency::alchemy-node-strategy-2025-10-28"
- source_id: "alchemy-node-strategy-2025-10-28"
- title: "[25년 10월] 돌릴만한 노드 추천"
- url: "https://www.kr.playblackdesert.com/ko-kr/Forum/ForumTopic/Detail?_opinionNo=0&_topicNo=142101"
- publisher: "새별-KR"
- source_type: "community_strategy"
- published_at: "2025-10-28"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "alchemy-onboarding-strategy.section.reverse-dependency"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.section.supply-imperial::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.section.supply-imperial::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "alchemy-onboarding-strategy.section.supply-imperial"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.section.supply-imperial::alchemy-imperial-strategy-2024-11-09`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.section.supply-imperial::alchemy-imperial-strategy-2024-11-09"
- source_id: "alchemy-imperial-strategy-2024-11-09"
- title: "연금 황실 납품 가격#연금황납#연금"
- url: "https://blackdesertonlineyoutube.tistory.com/169"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-11-09"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "alchemy-onboarding-strategy.section.supply-imperial"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.section.supply-imperial::alchemy-node-strategy-2025-10-28`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.section.supply-imperial::alchemy-node-strategy-2025-10-28"
- source_id: "alchemy-node-strategy-2025-10-28"
- title: "[25년 10월] 돌릴만한 노드 추천"
- url: "https://www.kr.playblackdesert.com/ko-kr/Forum/ForumTopic/Detail?_opinionNo=0&_topicNo=142101"
- publisher: "새별-KR"
- source_type: "community_strategy"
- published_at: "2025-10-28"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "alchemy-onboarding-strategy.section.supply-imperial"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.section.supply-imperial::imperial-delivery-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.section.supply-imperial::imperial-delivery-guide"
- source_id: "imperial-delivery-guide"
- title: "황실 납품"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=109"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "alchemy-onboarding-strategy.section.supply-imperial"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.check-stock-space::alchemy-basic-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.check-stock-space::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.check-stock-space"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.check-stock-space::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.check-stock-space::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.check-stock-space"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.check-stock-space::alchemy-node-strategy-2025-10-28`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.check-stock-space::alchemy-node-strategy-2025-10-28"
- source_id: "alchemy-node-strategy-2025-10-28"
- title: "[25년 10월] 돌릴만한 노드 추천"
- url: "https://www.kr.playblackdesert.com/ko-kr/Forum/ForumTopic/Detail?_opinionNo=0&_topicNo=142101"
- publisher: "새별-KR"
- source_type: "community_strategy"
- published_at: "2025-10-28"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.check-stock-space"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.choose-final-output::alchemy-basic-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.choose-final-output::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.choose-final-output"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.choose-final-output::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.choose-final-output::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.choose-final-output"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.choose-final-output::alchemy-node-strategy-2025-10-28`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.choose-final-output::alchemy-node-strategy-2025-10-28"
- source_id: "alchemy-node-strategy-2025-10-28"
- title: "[25년 10월] 돌릴만한 노드 추천"
- url: "https://www.kr.playblackdesert.com/ko-kr/Forum/ForumTopic/Detail?_opinionNo=0&_topicNo=142101"
- publisher: "새별-KR"
- source_type: "community_strategy"
- published_at: "2025-10-28"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.choose-final-output"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.choose-outlet::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.choose-outlet::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.choose-outlet"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.choose-outlet::alchemy-imperial-strategy-2024-11-09`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.choose-outlet::alchemy-imperial-strategy-2024-11-09"
- source_id: "alchemy-imperial-strategy-2024-11-09"
- title: "연금 황실 납품 가격#연금황납#연금"
- url: "https://blackdesertonlineyoutube.tistory.com/169"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2024-11-09"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.choose-outlet"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.choose-outlet::imperial-delivery-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.choose-outlet::imperial-delivery-guide"
- source_id: "imperial-delivery-guide"
- title: "황실 납품"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=109"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.choose-outlet"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.choose-repeat-volume::alchemy-basic-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.choose-repeat-volume::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.choose-repeat-volume"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.choose-repeat-volume::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.choose-repeat-volume::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.choose-repeat-volume"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.choose-repeat-volume::alchemy-node-strategy-2025-10-28`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.choose-repeat-volume::alchemy-node-strategy-2025-10-28"
- source_id: "alchemy-node-strategy-2025-10-28"
- title: "[25년 10월] 돌릴만한 노드 추천"
- url: "https://www.kr.playblackdesert.com/ko-kr/Forum/ForumTopic/Detail?_opinionNo=0&_topicNo=142101"
- publisher: "새별-KR"
- source_type: "community_strategy"
- published_at: "2025-10-28"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.choose-repeat-volume"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.classify-shortages::alchemy-basic-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.classify-shortages::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.classify-shortages"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.classify-shortages::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.classify-shortages::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.classify-shortages"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.classify-shortages::alchemy-node-strategy-2025-10-28`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.classify-shortages::alchemy-node-strategy-2025-10-28"
- source_id: "alchemy-node-strategy-2025-10-28"
- title: "[25년 10월] 돌릴만한 노드 추천"
- url: "https://www.kr.playblackdesert.com/ko-kr/Forum/ForumTopic/Detail?_opinionNo=0&_topicNo=142101"
- publisher: "새별-KR"
- source_type: "community_strategy"
- published_at: "2025-10-28"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.classify-shortages"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.confirm-ratios::alchemy-basic-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.confirm-ratios::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.confirm-ratios"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.confirm-ratios::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.confirm-ratios::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.confirm-ratios"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.improve-one-bottleneck::alchemy-basic-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.improve-one-bottleneck::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.improve-one-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.improve-one-bottleneck::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.improve-one-bottleneck::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.improve-one-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.improve-one-bottleneck::alchemy-node-strategy-2025-10-28`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.improve-one-bottleneck::alchemy-node-strategy-2025-10-28"
- source_id: "alchemy-node-strategy-2025-10-28"
- title: "[25년 10월] 돌릴만한 노드 추천"
- url: "https://www.kr.playblackdesert.com/ko-kr/Forum/ForumTopic/Detail?_opinionNo=0&_topicNo=142101"
- publisher: "새별-KR"
- source_type: "community_strategy"
- published_at: "2025-10-28"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.improve-one-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.run-small-batch::alchemy-basic-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.run-small-batch::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.run-small-batch"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.run-small-batch::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.run-small-batch::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.run-small-batch"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.trace-intermediates::alchemy-basic-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.trace-intermediates::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.trace-intermediates"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.trace-intermediates::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.trace-intermediates::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.trace-intermediates"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.trace-intermediates::alchemy-node-strategy-2025-10-28`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.trace-intermediates::alchemy-node-strategy-2025-10-28"
- source_id: "alchemy-node-strategy-2025-10-28"
- title: "[25년 10월] 돌릴만한 노드 추천"
- url: "https://www.kr.playblackdesert.com/ko-kr/Forum/ForumTopic/Detail?_opinionNo=0&_topicNo=142101"
- publisher: "새별-KR"
- source_type: "community_strategy"
- published_at: "2025-10-28"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.trace-intermediates"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.verify-recipe::alchemy-basic-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.verify-recipe::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.verify-recipe"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-onboarding-strategy.claim.step.verify-recipe::alchemy-guide`

- evidence_seed_key: "alchemy-onboarding-strategy.claim.step.verify-recipe::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alchemy-onboarding-strategy.step.verify-recipe"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
