<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 황실 낚시 납품

## Identity

- slug: "imperial-fishing-delivery"
- name_ko: "황실 낚시 납품"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "주요 파란색·노란색 물고기를 원가의 250%로 납품하며 서버별 수량 제한은 자정을 기준으로 매 3시간 갱신된다."
- purpose: "황실 낚시 납품의 대상·가격·재고 주기를 일반 무역과 분리한다."

## Requirements

### `imperial-fishing-delivery.eligibility`

- seed_key: "imperial-fishing-delivery.eligibility"
- kind: "item"
- requirement_level: "required"
- title: "납품 대상"
- description: "현재 가이드 기준 주요 대상은 파란색과 노란색 등급이며 일부 품목은 예외다."
- structured_value:

```json
{
  "exceptions_exist": true,
  "key_eligible_grades": [
    "blue",
    "yellow"
  ]
}
```

### `imperial-fishing-delivery.price`

- seed_key: "imperial-fishing-delivery.price"
- kind: "stat"
- requirement_level: "required"
- title: "납품 가격"
- description: "납품 가능 물고기는 원가 기준 250%로 납품한다."
- structured_value:

```json
{
  "base_price_percent": 250
}
```

### `imperial-fishing-delivery.quota`

- seed_key: "imperial-fishing-delivery.quota"
- kind: "other"
- requirement_level: "required"
- title: "서버 재고"
- description: "서버별 물고기 납품 수량 제한이 있고 자정 기준 매 3시간 갱신된다."
- structured_value:

```json
{
  "anchor": "00:00",
  "refresh_interval_hours": 3,
  "server_quota": true
}
```

## Steps

- None

## Schedules

### `imperial-fishing-delivery.quota-refresh`

- seed_key: "imperial-fishing-delivery.quota-refresh"
- rule_type: "stock_refresh"
- recurrence_type: "interval"
- weekday: null
- time_local: null
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "서버별 황실 낚시 납품 수량은 자정 기준 매 3시간 갱신"

## Rewards

- None

## Sections

- None

## Related Contents

### `imperial-fishing-delivery.trade`

- seed_key: "imperial-fishing-delivery.trade"
- direction: "outgoing"
- relation_type: "alternative"
- content_slug: "fish-freshness-and-trade"
- content_name_ko: "물고기 신선도와 무역"
- content_category: "life"
- note: "일반 무역 판매와 별도"
- order_no: 1
- relative_path: "../contents/fish-freshness-and-trade.md"
### `imperial-fishing-delivery.crafting`

- seed_key: "imperial-fishing-delivery.crafting"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "imperial-crafting-delivery-daily"
- content_name_ko: "황실 제작 납품 일일"
- content_category: "life"
- note: "황실 납품 interval 표현을 재사용하되 개인 한도는 공유하지 않음"
- order_no: 2
- relative_path: "../contents/imperial-crafting-delivery-daily.md"
### `imperial-fishing-delivery.treasure`

- seed_key: "imperial-fishing-delivery.treasure"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "treasure-grade-fish"
- content_name_ko: "보물 등급 물고기"
- content_category: "life"
- note: "보물 등급은 납품 불가"
- order_no: 3
- relative_path: "../contents/treasure-grade-fish.md"
### `fish-freshness-and-trade.imperial`

- seed_key: "fish-freshness-and-trade.imperial"
- direction: "incoming"
- relation_type: "alternative"
- content_slug: "fish-freshness-and-trade"
- content_name_ko: "물고기 신선도와 무역"
- content_category: "life"
- note: "일반 무역과 황실 낚시 납품은 별도 방식"
- order_no: 2
- relative_path: "../contents/fish-freshness-and-trade.md"
### `treasure-grade-fish.imperial-delivery`

- seed_key: "treasure-grade-fish.imperial-delivery"
- direction: "incoming"
- relation_type: "related"
- content_slug: "treasure-grade-fish"
- content_name_ko: "보물 등급 물고기"
- content_category: "life"
- note: "납품 불가 예외"
- order_no: 2
- relative_path: "../contents/treasure-grade-fish.md"
### `mystical-fish-tank.imperial`

- seed_key: "mystical-fish-tank.imperial"
- direction: "incoming"
- relation_type: "related"
- content_slug: "mystical-fish-tank"
- content_name_ko: "심청의 신묘한 어항"
- content_category: "life"
- note: "보관한 납품 가능 물고기 판매"
- order_no: 3
- relative_path: "../contents/mystical-fish-tank.md"
### `fishing-onboarding-strategy.imperial`

- seed_key: "fishing-onboarding-strategy.imperial"
- direction: "incoming"
- relation_type: "related"
- content_slug: "fishing-onboarding-strategy"
- content_name_ko: "낚시 입문 전략"
- content_category: "life"
- note: "황실 낚시 납품 경로를 확인한다."
- order_no: 4
- relative_path: "../contents/fishing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `imperial-fishing-delivery.summary::fishing-advanced-guide`

- evidence_seed_key: "imperial-fishing-delivery.summary::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "imperial-fishing-delivery"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "대상·250%·3시간 갱신"
- active: true
- is_active: true

### `imperial-fishing-delivery.summary::fishing-basic-guide`

- evidence_seed_key: "imperial-fishing-delivery.summary::fishing-basic-guide"
- source_id: "fishing-basic-guide"
- title: "낚시 기초편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=107"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "imperial-fishing-delivery"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "대상·250%·3시간 갱신"
- active: true
- is_active: true

### `imperial-fishing-delivery.requirement.eligibility::fishing-advanced-guide`

- evidence_seed_key: "imperial-fishing-delivery.requirement.eligibility::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "imperial-fishing-delivery.eligibility"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "파란색·노란색 및 예외"
- active: true
- is_active: true

### `imperial-fishing-delivery.requirement.price::fishing-advanced-guide`

- evidence_seed_key: "imperial-fishing-delivery.requirement.price::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "imperial-fishing-delivery.price"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "250%"
- active: true
- is_active: true

### `imperial-fishing-delivery.requirement.quota::fishing-advanced-guide`

- evidence_seed_key: "imperial-fishing-delivery.requirement.quota::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "imperial-fishing-delivery.quota"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "서버 수량과 3시간 갱신"
- active: true
- is_active: true

### `imperial-fishing-delivery.requirement.quota::fishing-basic-guide`

- evidence_seed_key: "imperial-fishing-delivery.requirement.quota::fishing-basic-guide"
- source_id: "fishing-basic-guide"
- title: "낚시 기초편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=107"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "imperial-fishing-delivery.quota"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "서버 수량과 3시간 갱신"
- active: true
- is_active: true

### `imperial-fishing-delivery.schedule.quota-refresh::fishing-advanced-guide`

- evidence_seed_key: "imperial-fishing-delivery.schedule.quota-refresh::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "imperial-fishing-delivery.quota-refresh"
- claim_key: "schedule.stock_refresh"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "자정 기준 3시간 interval"
- active: true
- is_active: true

### `imperial-fishing-delivery.schedule.quota-refresh::fishing-basic-guide`

- evidence_seed_key: "imperial-fishing-delivery.schedule.quota-refresh::fishing-basic-guide"
- source_id: "fishing-basic-guide"
- title: "낚시 기초편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=107"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "imperial-fishing-delivery.quota-refresh"
- claim_key: "schedule.stock_refresh"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "자정 기준 3시간 interval"
- active: true
- is_active: true

### Historical / inactive evidence

- None
