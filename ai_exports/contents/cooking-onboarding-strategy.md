<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 요리 입문 전략

## Identity

- slug: "cooking-onboarding-strategy"
- name_ko: "요리 입문 전략"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- party_type: null
- difficulty: null

## Overview

- summary: "요리 목적과 결과물을 먼저 정하고 현재 제작식, 재료 공급, 반복 세션 병목과 결과물 처리 경로를 검증하는 생활 전략 콘텐츠다."
- purpose: "고정 수익표나 단일 품목 추천 없이 자신의 목표와 공급 조건에 맞는 첫 요리 루틴과 다음 행동을 결정하도록 돕는다."

## Requirements

### `cooking-onboarding-strategy.purpose-choice`

- seed_key: "cooking-onboarding-strategy.purpose-choice"
- kind: "other"
- requirement_level: "required"
- title: "요리 목적 선택"
- description: "직접 사용할 음식, 생활 레벨 성장, 마녀의 별미와 공헌도 진행, 황실 요리 납품, 후속 제작 재료, 시장 판매 중 이번 요리의 우선 목적을 먼저 정한다."
- structured_value:

```json
{
  "goals": [
    "direct_food_use",
    "life_level_growth",
    "witch_delicacy_contribution",
    "imperial_cooking_delivery",
    "downstream_or_project_material",
    "market_sale"
  ],
  "knowledge_role": "strategy",
  "single_default_goal": false
}
```

### `cooking-onboarding-strategy.recipe-selection`

- seed_key: "cooking-onboarding-strategy.recipe-selection"
- kind: "knowledge"
- requirement_level: "required"
- title: "목적 기반 요리 선택"
- description: "최종 사용 목적, 현재 요리 레벨, 안정적 재료 조달, 반복 가능한 양, 병목 재료 수, 황실 포장 가능 여부, 상위 요리 연결과 보관 부담을 함께 비교한다."
- structured_value:

```json
{
  "decision_dimensions": [
    "final_use",
    "cooking_level",
    "stable_supply",
    "repeatable_quantity",
    "bottleneck_count",
    "imperial_packaging",
    "downstream_recipe",
    "storage_load"
  ],
  "dynamic_market_rank_excluded": true,
  "knowledge_role": "strategy",
  "universal_best_recipe": false
}
```

### `cooking-onboarding-strategy.ingredient-sourcing`

- seed_key: "cooking-onboarding-strategy.ingredient-sourcing"
- kind: "other"
- requirement_level: "required"
- title: "재료 공급 경로 판단"
- description: "재료마다 NPC 고정 공급, 생산 노드와 일꾼, 재배, 채집, 직접 가공, 거래소, 부산물과 교환 중 지속 가능한 경로를 확인한다."
- structured_value:

```json
{
  "direct_or_external_by_material": true,
  "knowledge_role": "strategy",
  "supply_routes": [
    "npc_fixed_supply",
    "production_node_worker",
    "farming",
    "gathering",
    "processing",
    "marketplace",
    "byproduct_or_exchange"
  ],
  "universal_best_supply_route": false
}
```

### `cooking-onboarding-strategy.session-bottlenecks`

- seed_key: "cooking-onboarding-strategy.session-bottlenecks"
- kind: "other"
- requirement_level: "required"
- title: "반복 세션 병목"
- description: "핵심 재료 재고, 요리 시간, 요리 도구 내구도, 가방과 창고 공간, 반복량, 황실 포장과 이동 준비 중 실제 중단 원인을 찾는다."
- structured_value:

```json
{
  "bottlenecks": [
    "core_ingredient_stock",
    "cooking_time",
    "cooking_utensil_durability",
    "inventory_space",
    "storage_space",
    "repeat_quantity",
    "imperial_packaging_and_transport"
  ],
  "exact_gear_build_copied": false,
  "knowledge_role": "strategy",
  "mastery_solves_all": false
}
```

### `cooking-onboarding-strategy.imperial-decision`

- seed_key: "cooking-onboarding-strategy.imperial-decision"
- kind: "other"
- requirement_level: "required"
- title: "황실 요리 납품 판단"
- description: "현재 레벨과 상자 단계, 재료 조달 상태, 포장과 보관 준비, 가문 일일 가능 수량, 현재 시장 조건을 확인한 뒤 직접 제작과 외부 조달을 비교한다."
- structured_value:

```json
{
  "compare_self_craft_and_external_supply": true,
  "decision_dimensions": [
    "cooking_level",
    "box_tier",
    "ingredient_supply",
    "packaging_readiness",
    "storage_and_transport",
    "family_daily_capacity",
    "current_market_check"
  ],
  "dynamic_market_rank_excluded": true,
  "fixed_profit_threshold": null,
  "knowledge_role": "strategy",
  "universal_best_box": false
}
```

## Steps

### `cooking-onboarding-strategy.step.choose-goal`

- seed_key: "cooking-onboarding-strategy.step.choose-goal"
- phase: "preparation"
- order_no: 1
- title: "요리 목적 선택"
- description: "이번 세션에서 직접 사용, 성장, 공헌도 부산물, 황실 납품, 후속 제작 또는 판매 중 우선 목적 하나를 정한다."
- checkable: false

### `cooking-onboarding-strategy.step.choose-output`

- seed_key: "cooking-onboarding-strategy.step.choose-output"
- phase: "preparation"
- order_no: 2
- title: "결과물 하나 결정"
- description: "목적과 현재 요리 레벨에 맞는 결과물 하나를 첫 검증 대상으로 정한다."
- checkable: false

### `cooking-onboarding-strategy.step.verify-recipe`

- seed_key: "cooking-onboarding-strategy.step.verify-recipe"
- phase: "preparation"
- order_no: 3
- title: "현재 제작식 확인"
- description: "게임의 제작 노트에서 현재 재료와 수량, 대체 재료 조건을 확인한다."
- checkable: false

### `cooking-onboarding-strategy.step.classify-ingredients`

- seed_key: "cooking-onboarding-strategy.step.classify-ingredients"
- phase: "preparation"
- order_no: 4
- title: "재료 공급 경로 분류"
- description: "필요 재료를 NPC, 노드와 일꾼, 재배, 채집, 가공, 거래소, 부산물과 교환 경로로 나눈다."
- checkable: false

### `cooking-onboarding-strategy.step.choose-supply-route`

- seed_key: "cooking-onboarding-strategy.step.choose-supply-route"
- phase: "preparation"
- order_no: 5
- title: "지속 가능한 공급 선택"
- description: "보유 재고와 반복할 양을 기준으로 재료별 직접 생산과 외부 조달 경로를 정한다."
- checkable: false

### `cooking-onboarding-strategy.step.run-small-batch`

- seed_key: "cooking-onboarding-strategy.step.run-small-batch"
- phase: "first_time"
- order_no: 6
- title: "소량 제작 검증"
- description: "작은 묶음으로 실제 제작식과 대체 재료, 결과물 처리 흐름을 확인한다."
- checkable: false

### `cooking-onboarding-strategy.step.check-session-bottleneck`

- seed_key: "cooking-onboarding-strategy.step.check-session-bottleneck"
- phase: "first_time"
- order_no: 7
- title: "반복 세션 병목 확인"
- description: "반복량을 늘리기 전에 재료, 시간, 도구 내구도, 가방과 창고 중 먼저 막히는 지점을 확인한다."
- checkable: false

### `cooking-onboarding-strategy.step.choose-outlet`

- seed_key: "cooking-onboarding-strategy.step.choose-outlet"
- phase: "maintenance"
- order_no: 8
- title: "결과물 처리 결정"
- description: "황실 납품, 직접 사용, 보관, 후속 제작, 판매 중 현재 목적에 맞는 처리 경로를 선택한다."
- checkable: false

### `cooking-onboarding-strategy.step.improve-one-bottleneck`

- seed_key: "cooking-onboarding-strategy.step.improve-one-bottleneck"
- phase: "maintenance"
- order_no: 9
- title: "다음 병목 하나 개선"
- description: "세션 기록에서 가장 먼저 멈춘 원인 하나만 골라 다음 반복 전에 개선한다."
- checkable: false

## Schedules

- None

## Rewards

- None

## Sections

### `cooking-onboarding-strategy.section.goal-supply`

- seed_key: "cooking-onboarding-strategy.section.goal-supply"
- section_type: "strategy"
- title: "목적에서 재료 공급까지 연결"
- order_no: 1

#### body_markdown

요리 이름이나 수익 순위부터 고정하지 않는다. 사용할 결과물과 반복량을 정하고, 제작 노트의 현재 식을 확인한 다음 재료별 공급 경로와 병목을 연결한다.

### `cooking-onboarding-strategy.section.imperial-decision`

- seed_key: "cooking-onboarding-strategy.section.imperial-decision"
- section_type: "strategy"
- title: "황실 요리는 독립적인 일일 출구로 판단"
- order_no: 2

#### body_markdown

황실 제작 납품은 일반 판매와 같은 고정 수익 구조가 아니다. 현재 레벨과 상자 단계, 일일 가능 수량, 재료 확보, 포장과 이동 준비를 확인하고 직접 제작과 외부 조달을 그때그때 비교한다.

### `cooking-onboarding-strategy.section.common-mistakes`

- seed_key: "cooking-onboarding-strategy.section.common-mistakes"
- section_type: "common_mistakes"
- title: "요리 입문에서 피할 판단"
- order_no: 3

#### body_markdown

과거 가격표만 보고 요리를 고정하거나 공급 경로 확인 없이 대량 제작하지 않는다. 2026-09-02 이전 장비·광명석 구성을 현재 세팅으로 복제하지 않고, 황실 납품과 일반 판매를 같은 구조로 보거나 대량 요리와 숙련도가 모든 재료 병목을 해결한다고 가정하지 않는다.

## Related Contents

### `cooking-onboarding-strategy.current-system`

- seed_key: "cooking-onboarding-strategy.current-system"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "cooking-current-system"
- content_name_ko: "요리 현재 시스템"
- content_category: "life"
- note: null
- order_no: 1
- relative_path: "../contents/cooking-current-system.md"
### `cooking-onboarding-strategy.mastery`

- seed_key: "cooking-onboarding-strategy.mastery"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "cooking-mastery-effects"
- content_name_ko: "요리 숙련도 효과"
- content_category: "life"
- note: null
- order_no: 2
- relative_path: "../contents/cooking-mastery-effects.md"
### `cooking-onboarding-strategy.mass-production`

- seed_key: "cooking-onboarding-strategy.mass-production"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "cooking-mass-production"
- content_name_ko: "대량 요리"
- content_category: "life"
- note: null
- order_no: 3
- relative_path: "../contents/cooking-mass-production.md"
### `cooking-onboarding-strategy.witch-delicacy`

- seed_key: "cooking-onboarding-strategy.witch-delicacy"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "witch-delicacy"
- content_name_ko: "마녀의 별미"
- content_category: "life"
- note: null
- order_no: 4
- relative_path: "../contents/witch-delicacy.md"
### `cooking-onboarding-strategy.imperial`

- seed_key: "cooking-onboarding-strategy.imperial"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "imperial-crafting-delivery-daily"
- content_name_ko: "황실 제작 납품 일일"
- content_category: "life"
- note: null
- order_no: 5
- relative_path: "../contents/imperial-crafting-delivery-daily.md"
### `cooking-onboarding-strategy.growth`

- seed_key: "cooking-onboarding-strategy.growth"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "cooking-growth-surprise-quest"
- content_name_ko: "요리 성장 깜짝 의뢰"
- content_category: "life"
- note: null
- order_no: 6
- relative_path: "../contents/cooking-growth-surprise-quest.md"
### `cooking-onboarding-strategy.farming`

- seed_key: "cooking-onboarding-strategy.farming"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "farming-onboarding-strategy"
- content_name_ko: "재배 입문 전략"
- content_category: "life"
- note: null
- order_no: 7
- relative_path: "../contents/farming-onboarding-strategy.md"
### `cooking-onboarding-strategy.production-nodes`

- seed_key: "cooking-onboarding-strategy.production-nodes"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "production-node-current-system"
- content_name_ko: "생산 거점 현재 시스템"
- content_category: "life"
- note: null
- order_no: 8
- relative_path: "../contents/production-node-current-system.md"
### `cooking-onboarding-strategy.storage`

- seed_key: "cooking-onboarding-strategy.storage"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "storage-current-system"
- content_name_ko: "창고 현재 시스템"
- content_category: "life"
- note: null
- order_no: 9
- relative_path: "../contents/storage-current-system.md"

## Evidence and Sources

### Current evidence

### `cooking-onboarding-strategy.claim.purpose::cooking-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.purpose::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "cooking-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.purpose::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.purpose::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "cooking-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.purpose::cooking-imperial-strategy-2025-01-30`

- evidence_seed_key: "cooking-onboarding-strategy.claim.purpose::cooking-imperial-strategy-2025-01-30"
- source_id: "cooking-imperial-strategy-2025-01-30"
- title: "요리 황납#황실납품#요리#도인#채소절임#정식#국밥"
- url: "https://blackdesertonlineyoutube.tistory.com/186"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-01-30"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "cooking-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.summary::cooking-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.summary::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "cooking-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.summary::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.summary::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "cooking-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.summary::imperial-delivery-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.summary::imperial-delivery-guide"
- source_id: "imperial-delivery-guide"
- title: "황실 납품"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=109"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "cooking-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.imperial-decision::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.imperial-decision::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cooking-onboarding-strategy.imperial-decision"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.imperial-decision::cooking-imperial-strategy-2025-01-30`

- evidence_seed_key: "cooking-onboarding-strategy.claim.imperial-decision::cooking-imperial-strategy-2025-01-30"
- source_id: "cooking-imperial-strategy-2025-01-30"
- title: "요리 황납#황실납품#요리#도인#채소절임#정식#국밥"
- url: "https://blackdesertonlineyoutube.tistory.com/186"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-01-30"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cooking-onboarding-strategy.imperial-decision"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.imperial-decision::imperial-delivery-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.imperial-decision::imperial-delivery-guide"
- source_id: "imperial-delivery-guide"
- title: "황실 납품"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=109"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cooking-onboarding-strategy.imperial-decision"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.imperial-decision::imperial-delivery-history`

- evidence_seed_key: "cooking-onboarding-strategy.claim.imperial-decision::imperial-delivery-history"
- source_id: "imperial-delivery-history"
- title: "황실 제작 납품 개선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13111"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cooking-onboarding-strategy.imperial-decision"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.ingredient-sourcing::cooking-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.ingredient-sourcing::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cooking-onboarding-strategy.ingredient-sourcing"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.ingredient-sourcing::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.ingredient-sourcing::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cooking-onboarding-strategy.ingredient-sourcing"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.ingredient-sourcing::cooking-imperial-strategy-2025-01-30`

- evidence_seed_key: "cooking-onboarding-strategy.claim.ingredient-sourcing::cooking-imperial-strategy-2025-01-30"
- source_id: "cooking-imperial-strategy-2025-01-30"
- title: "요리 황납#황실납품#요리#도인#채소절임#정식#국밥"
- url: "https://blackdesertonlineyoutube.tistory.com/186"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-01-30"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cooking-onboarding-strategy.ingredient-sourcing"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.purpose-choice::cooking-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.purpose-choice::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cooking-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.purpose-choice::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.purpose-choice::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cooking-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.purpose-choice::cooking-imperial-strategy-2025-01-30`

- evidence_seed_key: "cooking-onboarding-strategy.claim.purpose-choice::cooking-imperial-strategy-2025-01-30"
- source_id: "cooking-imperial-strategy-2025-01-30"
- title: "요리 황납#황실납품#요리#도인#채소절임#정식#국밥"
- url: "https://blackdesertonlineyoutube.tistory.com/186"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-01-30"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cooking-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.recipe-selection::cooking-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.recipe-selection::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cooking-onboarding-strategy.recipe-selection"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.recipe-selection::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.recipe-selection::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cooking-onboarding-strategy.recipe-selection"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.recipe-selection::cooking-imperial-strategy-2025-01-30`

- evidence_seed_key: "cooking-onboarding-strategy.claim.recipe-selection::cooking-imperial-strategy-2025-01-30"
- source_id: "cooking-imperial-strategy-2025-01-30"
- title: "요리 황납#황실납품#요리#도인#채소절임#정식#국밥"
- url: "https://blackdesertonlineyoutube.tistory.com/186"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-01-30"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cooking-onboarding-strategy.recipe-selection"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.session-bottlenecks::cooking-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.session-bottlenecks::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cooking-onboarding-strategy.session-bottlenecks"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.session-bottlenecks::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.session-bottlenecks::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cooking-onboarding-strategy.session-bottlenecks"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.session-bottlenecks::life-unification-2026-09-02`

- evidence_seed_key: "cooking-onboarding-strategy.claim.session-bottlenecks::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cooking-onboarding-strategy.session-bottlenecks"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.section.common-mistakes::cooking-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.section.common-mistakes::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "cooking-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.section.common-mistakes::cooking-imperial-strategy-2025-01-30`

- evidence_seed_key: "cooking-onboarding-strategy.claim.section.common-mistakes::cooking-imperial-strategy-2025-01-30"
- source_id: "cooking-imperial-strategy-2025-01-30"
- title: "요리 황납#황실납품#요리#도인#채소절임#정식#국밥"
- url: "https://blackdesertonlineyoutube.tistory.com/186"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-01-30"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "cooking-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.section.common-mistakes::life-unification-2026-09-02`

- evidence_seed_key: "cooking-onboarding-strategy.claim.section.common-mistakes::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "cooking-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.section.goal-supply::cooking-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.section.goal-supply::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "cooking-onboarding-strategy.section.goal-supply"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.section.goal-supply::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.section.goal-supply::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "cooking-onboarding-strategy.section.goal-supply"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.section.imperial-decision::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.section.imperial-decision::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "cooking-onboarding-strategy.section.imperial-decision"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.section.imperial-decision::cooking-imperial-strategy-2025-01-30`

- evidence_seed_key: "cooking-onboarding-strategy.claim.section.imperial-decision::cooking-imperial-strategy-2025-01-30"
- source_id: "cooking-imperial-strategy-2025-01-30"
- title: "요리 황납#황실납품#요리#도인#채소절임#정식#국밥"
- url: "https://blackdesertonlineyoutube.tistory.com/186"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-01-30"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "cooking-onboarding-strategy.section.imperial-decision"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.section.imperial-decision::imperial-delivery-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.section.imperial-decision::imperial-delivery-guide"
- source_id: "imperial-delivery-guide"
- title: "황실 납품"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=109"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "cooking-onboarding-strategy.section.imperial-decision"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.section.imperial-decision::imperial-delivery-history`

- evidence_seed_key: "cooking-onboarding-strategy.claim.section.imperial-decision::imperial-delivery-history"
- source_id: "imperial-delivery-history"
- title: "황실 제작 납품 개선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13111"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "cooking-onboarding-strategy.section.imperial-decision"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.check-session-bottleneck::cooking-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.check-session-bottleneck::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.check-session-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.check-session-bottleneck::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.check-session-bottleneck::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.check-session-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.check-session-bottleneck::life-unification-2026-09-02`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.check-session-bottleneck::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.check-session-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.choose-goal::cooking-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.choose-goal::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.choose-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.choose-goal::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.choose-goal::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.choose-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.choose-outlet::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.choose-outlet::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.choose-outlet"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.choose-outlet::cooking-imperial-strategy-2025-01-30`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.choose-outlet::cooking-imperial-strategy-2025-01-30"
- source_id: "cooking-imperial-strategy-2025-01-30"
- title: "요리 황납#황실납품#요리#도인#채소절임#정식#국밥"
- url: "https://blackdesertonlineyoutube.tistory.com/186"
- publisher: "검사학개론"
- source_type: "community_strategy"
- published_at: "2025-01-30"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.choose-outlet"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.choose-outlet::imperial-delivery-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.choose-outlet::imperial-delivery-guide"
- source_id: "imperial-delivery-guide"
- title: "황실 납품"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=109"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.choose-outlet"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.choose-output::cooking-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.choose-output::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.choose-output"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.choose-output::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.choose-output::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.choose-output"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.choose-supply-route::cooking-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.choose-supply-route::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.choose-supply-route"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.choose-supply-route::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.choose-supply-route::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.choose-supply-route"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.classify-ingredients::cooking-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.classify-ingredients::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.classify-ingredients"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.classify-ingredients::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.classify-ingredients::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.classify-ingredients"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.improve-one-bottleneck::cooking-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.improve-one-bottleneck::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.improve-one-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.improve-one-bottleneck::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.improve-one-bottleneck::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.improve-one-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.run-small-batch::cooking-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.run-small-batch::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.run-small-batch"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.run-small-batch::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.run-small-batch::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.run-small-batch"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.verify-recipe::cooking-guide`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.verify-recipe::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.verify-recipe"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### `cooking-onboarding-strategy.claim.step.verify-recipe::cooking-imperial-direction-2025-12-25`

- evidence_seed_key: "cooking-onboarding-strategy.claim.step.verify-recipe::cooking-imperial-direction-2025-12-25"
- source_id: "cooking-imperial-direction-2025-12-25"
- title: "이번 패치 이후 요리 황납의 방향에 대해서."
- url: "https://www.inven.co.kr/board/black/3584/50504"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2025-12-25"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "cooking-onboarding-strategy.step.verify-recipe"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-06"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
