<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 현행 물물교환 시스템

## Identity

- slug: "barter-current-system"
- name_ko: "현행 물물교환 시스템"
- category: "ocean_barter"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "2026-04-15 개편 이후의 저단 교환, 교섭력, 수송 제한, 까마귀 주화 교환과 돌발 물물교환 규칙."
- purpose: "현재 물물교환의 핵심 운영 규칙과 과거 규칙의 변경점을 구분한다."

## Requirements

### `barter-current-system.low-tier-output`

- seed_key: "barter-current-system.low-tier-output"
- kind: "other"
- requirement_level: "required"
- title: "저단 교환 결과 수량"
- description: "1→2단계와 2→3단계의 현재 결과 수량은 2~3개이며 1:1 교환은 발생하지 않는다."
- structured_value:

```json
{
  "current_min": 2,
  "max": 3,
  "previous_min": 1,
  "routes": [
    "1_to_2",
    "2_to_3"
  ]
}
```

### `barter-current-system.parley.crow-coin`

- seed_key: "barter-current-system.parley.crow-coin"
- kind: "other"
- requirement_level: "required"
- title: "까마귀 주화 교환 교섭력"
- description: "까마귀 주화 교환의 기본 필요 교섭력은 21,650이며 감소 효과로 실제 소비량은 더 낮아질 수 있다."
- structured_value:

```json
{
  "base_parley": 21650,
  "reduction_buffs_apply": true
}
```

### `barter-current-system.parley.ocean-rares`

- seed_key: "barter-current-system.parley.ocean-rares"
- kind: "other"
- requirement_level: "required"
- title: "[대양] 희귀 교역품 교섭력"
- description: "지정된 [대양] 희귀 교역품 5종의 기본 필요 교섭력은 14,286이며 감소 효과가 적용될 수 있다."
- structured_value:

```json
{
  "base_parley": 14286,
  "items": [
    "[대양] 콕스 해적단의 일지",
    "[대양] 관측 보고서",
    "[대양] 오색빛 산호 노리개",
    "[대양] 무쇠 수리 도구",
    "[대양] 해달족 낚시바늘"
  ],
  "reduction_buffs_apply": true
}
```

### `barter-current-system.transport-disabled`

- seed_key: "barter-current-system.transport-disabled"
- kind: "other"
- requirement_level: "required"
- title: "교역품 수송 제한"
- description: "물물교환 교역품은 현재 수송할 수 없다."
- structured_value:

```json
{
  "effective_from": "2026-04-15",
  "transport_allowed": false
}
```

## Steps

- None

## Schedules

- None

## Rewards

### `barter-current-system.sudden-crow-coin-1`

- seed_key: "barter-current-system.sudden-crow-coin-1"
- name: "돌발 물물교환 까마귀 주화 범위 1"
- reward_type: "crow_coin_range"
- amount: null
- min_amount: 4000.0
- max_amount: 5000.0
- unit: "까마귀 주화"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "2026-04-15 변경: 2,000~3,000 → 4,000~5,000"
- order_no: 1

### `barter-current-system.sudden-crow-coin-2`

- seed_key: "barter-current-system.sudden-crow-coin-2"
- name: "돌발 물물교환 까마귀 주화 범위 2"
- reward_type: "crow_coin_range"
- amount: null
- min_amount: 3500.0
- max_amount: 4000.0
- unit: "까마귀 주화"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "2026-04-15 변경: 1,800~2,000 → 3,500~4,000"
- order_no: 2

### `barter-current-system.sudden-crow-coin-3`

- seed_key: "barter-current-system.sudden-crow-coin-3"
- name: "돌발 물물교환 까마귀 주화 범위 3"
- reward_type: "crow_coin_range"
- amount: null
- min_amount: 3000.0
- max_amount: 3500.0
- unit: "까마귀 주화"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "2026-04-15 변경: 1,500~1,800 → 3,000~3,500"
- order_no: 3

### `barter-current-system.sudden-crow-coin-4`

- seed_key: "barter-current-system.sudden-crow-coin-4"
- name: "돌발 물물교환 까마귀 주화 범위 4"
- reward_type: "crow_coin_range"
- amount: null
- min_amount: 2500.0
- max_amount: 3000.0
- unit: "까마귀 주화"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "2026-04-15 변경: 1,300~1,500 → 2,500~3,000"
- order_no: 4

### `barter-current-system.sudden-crow-coin-5`

- seed_key: "barter-current-system.sudden-crow-coin-5"
- name: "돌발 물물교환 까마귀 주화 범위 5"
- reward_type: "crow_coin_range"
- amount: null
- min_amount: 1500.0
- max_amount: 2500.0
- unit: "까마귀 주화"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "2026-04-15 변경: 1,200~1,300 → 1,500~2,500"
- order_no: 5

### `barter-current-system.sudden-crow-coin-6`

- seed_key: "barter-current-system.sudden-crow-coin-6"
- name: "돌발 물물교환 까마귀 주화 범위 6"
- reward_type: "crow_coin_range"
- amount: null
- min_amount: 1200.0
- max_amount: 1500.0
- unit: "까마귀 주화"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "2026-04-15 변경: 1,100~1,200 → 1,200~1,500"
- order_no: 6

### `barter-current-system.sudden-crow-coin-7`

- seed_key: "barter-current-system.sudden-crow-coin-7"
- name: "돌발 물물교환 까마귀 주화 범위 7"
- reward_type: "crow_coin_range"
- amount: null
- min_amount: 1000.0
- max_amount: 1200.0
- unit: "까마귀 주화"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "2026-04-15 변경: 500~1,000 → 1,000~1,200"
- order_no: 7

## Sections

### `barter-current-system.crow-nest`

- seed_key: "barter-current-system.crow-nest"
- section_type: "overview"
- title: "까마귀 주화 교환 거점"
- order_no: 1

#### body_markdown

기존 하코번 섬의 대량 까마귀 주화 교환 역할은 까마귀의 둥지로 이동했고, 현재 까마귀 주화 교환에는 4단계 교역품을 사용한다.

## Related Contents

### `barter-current-system.relation.stage-values`

- seed_key: "barter-current-system.relation.stage-values"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "barter-stage-values"
- content_name_ko: "물물교환 단계별 가치와 무게"
- content_category: "ocean_barter"
- note: "단계별 판매가와 무게"
- order_no: 1
- relative_path: "../contents/barter-stage-values.md"
### `barter-current-system.relation.tier6`

- seed_key: "barter-current-system.relation.tier6"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "barter-tier6-routes"
- content_name_ko: "6단계 물물교환 교역로"
- content_category: "ocean_barter"
- note: "5→6단계 교역로"
- order_no: 2
- relative_path: "../contents/barter-tier6-routes.md"
### `barter-current-system.relation.tier7`

- seed_key: "barter-current-system.relation.tier7"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "barter-tier7-routes"
- content_name_ko: "7단계 물물교환 교역로"
- content_category: "ocean_barter"
- note: "6→7단계 교역로"
- order_no: 3
- relative_path: "../contents/barter-tier7-routes.md"
### `barter-current-system.relation.strategy`

- seed_key: "barter-current-system.relation.strategy"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "barter-route-strategy"
- content_name_ko: "물물교환 동선 전략"
- content_category: "ocean_barter"
- note: "공식 규칙과 분리된 커뮤니티 동선 측정"
- order_no: 4
- relative_path: "../contents/barter-route-strategy.md"
### `barter-current-system.relation.crow-shop`

- seed_key: "barter-current-system.relation.crow-shop"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "crow-coin-material-shop"
- content_name_ko: "까마귀 주화 증축 재료 상점"
- content_category: "ocean_project"
- note: "까마귀 주화의 증축 재료 사용처"
- order_no: 5
- relative_path: "../contents/crow-coin-material-shop.md"
### `barter-onboarding-strategy.current-system`

- seed_key: "barter-onboarding-strategy.current-system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "barter-onboarding-strategy"
- content_name_ko: "물물교환 입문 운영 전략"
- content_category: "ocean_barter"
- note: "현행 물물교환 규칙"
- order_no: 1
- relative_path: "../contents/barter-onboarding-strategy.md"
### `barter-route-strategy.relation.current-system`

- seed_key: "barter-route-strategy.relation.current-system"
- direction: "incoming"
- relation_type: "related"
- content_slug: "barter-route-strategy"
- content_name_ko: "물물교환 동선 전략"
- content_category: "ocean_barter"
- note: "공식 규칙과 분리된 실전 동선 참고"
- order_no: 1
- relative_path: "../contents/barter-route-strategy.md"
### `barter-stage-values.relation.current-system`

- seed_key: "barter-stage-values.relation.current-system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "barter-stage-values"
- content_name_ko: "물물교환 단계별 가치와 무게"
- content_category: "ocean_barter"
- note: "현행 물물교환 규칙의 단계별 기준표"
- order_no: 1
- relative_path: "../contents/barter-stage-values.md"
### `barter-tier6-routes.relation.current-system`

- seed_key: "barter-tier6-routes.relation.current-system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "barter-tier6-routes"
- content_name_ko: "6단계 물물교환 교역로"
- content_category: "ocean_barter"
- note: "현행 물물교환의 5→6단계 교역"
- order_no: 1
- relative_path: "../contents/barter-tier6-routes.md"
### `barter-tier7-routes.relation.current-system`

- seed_key: "barter-tier7-routes.relation.current-system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "barter-tier7-routes"
- content_name_ko: "7단계 물물교환 교역로"
- content_category: "ocean_barter"
- note: "현행 물물교환의 6→7단계 교역"
- order_no: 1
- relative_path: "../contents/barter-tier7-routes.md"
### `life-mastery-effects.ocean-system`

- seed_key: "life-mastery-effects.ocean-system"
- direction: "incoming"
- relation_type: "related"
- content_slug: "life-mastery-effects"
- content_name_ko: "생활 분야별 숙련도 효과"
- content_category: "life"
- note: "항해 숙련도는 기존 대양 시스템 데이터와 연결된다."
- order_no: 2
- relative_path: "../contents/life-mastery-effects.md"
### `ocean-first-mates.relation.sudden-barter`

- seed_key: "ocean-first-mates.relation.sudden-barter"
- direction: "incoming"
- relation_type: "related"
- content_slug: "ocean-first-mates"
- content_name_ko: "대양 부선장"
- content_category: "ocean_guide"
- note: "클레이아 고용 재료 획득처"
- order_no: 2
- relative_path: "../contents/ocean-first-mates.md"
### `life-family-levels.ocean-sailing`

- seed_key: "life-family-levels.ocean-sailing"
- direction: "incoming"
- relation_type: "related"
- content_slug: "life-family-levels"
- content_name_ko: "가문 통합 생활 레벨"
- content_category: "life"
- note: "가문 통합 항해·교역 레벨은 기존 대양 콘텐츠의 공통 기반이다."
- order_no: 3
- relative_path: "../contents/life-family-levels.md"
### `account-progression-foundation.barter`

- seed_key: "account-progression-foundation.barter"
- direction: "incoming"
- relation_type: "related"
- content_slug: "account-progression-foundation"
- content_name_ko: "가문 성장 기반"
- content_category: "progression"
- note: null
- order_no: 9
- relative_path: "../contents/account-progression-foundation.md"

## Evidence and Sources

### Current evidence

### `barter-current-system.evidence.low-tier-output::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-current-system.evidence.low-tier-output::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-current-system.low-tier-output"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "1→2단계와 2→3단계의 현재 결과 수량은 2~3개이며 1:1 교환은 발생하지 않는다."
- active: true
- is_active: true

### `barter-current-system.evidence.parley-crow-coin::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-current-system.evidence.parley-crow-coin::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-current-system.parley.crow-coin"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "까마귀 주화 교환의 기본 필요 교섭력은 21,650이며 감소 효과로 실제 소비량은 더 낮아질 수 있다."
- active: true
- is_active: true

### `barter-current-system.evidence.parley-ocean-rares::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-current-system.evidence.parley-ocean-rares::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-current-system.parley.ocean-rares"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "지정된 [대양] 희귀 교역품 5종의 기본 필요 교섭력은 14,286이며 감소 효과가 적용될 수 있다."
- active: true
- is_active: true

### `barter-current-system.evidence.transport-disabled::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-current-system.evidence.transport-disabled::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-current-system.transport-disabled"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "물물교환 교역품은 현재 수송할 수 없다."
- active: true
- is_active: true

### `barter-current-system.evidence.crow-nest::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-current-system.evidence.crow-nest::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "barter-current-system.crow-nest"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "기존 하코번 섬의 대량 까마귀 주화 교환 역할은 까마귀의 둥지로 이동했고, 현재 까마귀 주화 교환에는 4단계 교역품을 사용한다."
- active: true
- is_active: true

### `barter-current-system.evidence.sudden-crow-coin-1::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-current-system.evidence.sudden-crow-coin-1::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "barter-current-system.sudden-crow-coin-1"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-04-15 변경: 2,000~3,000 → 4,000~5,000"
- active: true
- is_active: true

### `barter-current-system.evidence.sudden-crow-coin-2::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-current-system.evidence.sudden-crow-coin-2::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "barter-current-system.sudden-crow-coin-2"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-04-15 변경: 1,800~2,000 → 3,500~4,000"
- active: true
- is_active: true

### `barter-current-system.evidence.sudden-crow-coin-3::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-current-system.evidence.sudden-crow-coin-3::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "barter-current-system.sudden-crow-coin-3"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-04-15 변경: 1,500~1,800 → 3,000~3,500"
- active: true
- is_active: true

### `barter-current-system.evidence.sudden-crow-coin-4::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-current-system.evidence.sudden-crow-coin-4::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "barter-current-system.sudden-crow-coin-4"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-04-15 변경: 1,300~1,500 → 2,500~3,000"
- active: true
- is_active: true

### `barter-current-system.evidence.sudden-crow-coin-5::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-current-system.evidence.sudden-crow-coin-5::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "barter-current-system.sudden-crow-coin-5"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-04-15 변경: 1,200~1,300 → 1,500~2,500"
- active: true
- is_active: true

### `barter-current-system.evidence.sudden-crow-coin-6::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-current-system.evidence.sudden-crow-coin-6::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "barter-current-system.sudden-crow-coin-6"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-04-15 변경: 1,100~1,200 → 1,200~1,500"
- active: true
- is_active: true

### `barter-current-system.evidence.sudden-crow-coin-7::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-current-system.evidence.sudden-crow-coin-7::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "barter-current-system.sudden-crow-coin-7"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-04-15 변경: 500~1,000 → 1,000~1,200"
- active: true
- is_active: true

### Historical / inactive evidence

- None
