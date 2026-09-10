<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 물고기 신선도와 무역

## Identity

- slug: "fish-freshness-and-trade"
- name_ko: "물고기 신선도와 무역"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "일반 물고기 가격 보증기간은 48시간, 오딜리타 원산지는 60시간이며 시간이 지나면 가격이 감소한다."
- purpose: "2025-05-21 이후 보증기간과 판매가 요소를 구식 24·36시간에서 교정한다."

## Requirements

### `fish-freshness-and-trade.durations`

- seed_key: "fish-freshness-and-trade.durations"
- kind: "stat"
- requirement_level: "required"
- title: "현재 가격 보증기간"
- description: "일반 48시간, 오딜리타 60시간이다. 끝없는 겨울의 산은 더 긴 기존 기간 유지가 확인되지만 정확한 시간은 입력하지 않는다."
- structured_value:

```json
{
  "mountain_of_eternal_winter_hours": null,
  "mountain_status": "longer_unchanged_exact_unresolved",
  "odyllita_hours": 60,
  "standard_hours": 48
}
```

### `fish-freshness-and-trade.expiry-value`

- seed_key: "fish-freshness-and-trade.expiry-value"
- kind: "stat"
- requirement_level: "required"
- title: "시간 경과 가치"
- description: "현재 가이드 기준 보증기간 종료 시점에는 원가의 약 30% 수준이 된다."
- structured_value:

```json
{
  "approximate": true,
  "near_expiry_base_value_percent": 30
}
```

### `fish-freshness-and-trade.sale-factors`

- seed_key: "fish-freshness-and-trade.sale-factors"
- kind: "other"
- requirement_level: "required"
- title: "판매가 요소"
- description: "물고기 무역 판매가는 원가, 신선도, 거리, 무역 효과와 흥정에 연결된다."
- structured_value:

```json
{
  "factors": [
    "base_price",
    "freshness",
    "distance_bonus",
    "trade_effects",
    "bargaining"
  ],
  "full_formula_in_scope": false
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

### `fish-freshness-and-trade.system`

- seed_key: "fish-freshness-and-trade.system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "fishing-current-system"
- content_name_ko: "낚시 현재 시스템"
- content_category: "life"
- note: "낚시 결과 판매"
- order_no: 1
- relative_path: "../contents/fishing-current-system.md"
### `fish-freshness-and-trade.imperial`

- seed_key: "fish-freshness-and-trade.imperial"
- direction: "outgoing"
- relation_type: "alternative"
- content_slug: "imperial-fishing-delivery"
- content_name_ko: "황실 낚시 납품"
- content_category: "life"
- note: "일반 무역과 황실 낚시 납품은 별도 방식"
- order_no: 2
- relative_path: "../contents/imperial-fishing-delivery.md"
### `fish-freshness-and-trade.tank`

- seed_key: "fish-freshness-and-trade.tank"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "mystical-fish-tank"
- content_name_ko: "심청의 신묘한 어항"
- content_category: "life"
- note: "어항의 5배 보증기간"
- order_no: 3
- relative_path: "../contents/mystical-fish-tank.md"
### `imperial-fishing-delivery.trade`

- seed_key: "imperial-fishing-delivery.trade"
- direction: "incoming"
- relation_type: "alternative"
- content_slug: "imperial-fishing-delivery"
- content_name_ko: "황실 낚시 납품"
- content_category: "life"
- note: "일반 무역 판매와 별도"
- order_no: 1
- relative_path: "../contents/imperial-fishing-delivery.md"
### `mystical-fish-tank.freshness`

- seed_key: "mystical-fish-tank.freshness"
- direction: "incoming"
- relation_type: "related"
- content_slug: "mystical-fish-tank"
- content_name_ko: "심청의 신묘한 어항"
- content_category: "life"
- note: "가격 보증기간 5배"
- order_no: 2
- relative_path: "../contents/mystical-fish-tank.md"
### `storage-current-system.fish-freshness`

- seed_key: "storage-current-system.fish-freshness"
- direction: "incoming"
- relation_type: "related"
- content_slug: "storage-current-system"
- content_name_ko: "창고 현재 시스템"
- content_category: "life"
- note: "물고기 가격 보증기간은 창고에서도 계속 흐른다."
- order_no: 2
- relative_path: "../contents/storage-current-system.md"
### `fishing-onboarding-strategy.freshness`

- seed_key: "fishing-onboarding-strategy.freshness"
- direction: "incoming"
- relation_type: "related"
- content_slug: "fishing-onboarding-strategy"
- content_name_ko: "낚시 입문 전략"
- content_category: "life"
- note: "물고기 신선도와 처분 경로를 확인한다."
- order_no: 3
- relative_path: "../contents/fishing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `fish-freshness-and-trade.summary::fish-freshness-2025-05-21`

- evidence_seed_key: "fish-freshness-and-trade.summary::fish-freshness-2025-05-21"
- source_id: "fish-freshness-2025-05-21"
- title: "5월 21일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13995"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-21"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fish-freshness-and-trade"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "현재 보증기간과 가격 감소"
- active: true
- is_active: true

### `fish-freshness-and-trade.summary::fishing-advanced-guide`

- evidence_seed_key: "fish-freshness-and-trade.summary::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fish-freshness-and-trade"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "현재 보증기간과 가격 감소"
- active: true
- is_active: true

### `fish-freshness-and-trade.requirement.durations::fish-freshness-2025-05-21`

- evidence_seed_key: "fish-freshness-and-trade.requirement.durations::fish-freshness-2025-05-21"
- source_id: "fish-freshness-2025-05-21"
- title: "5월 21일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13995"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-21"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fish-freshness-and-trade.durations"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "48·60시간 및 겨울산 미확정"
- active: true
- is_active: true

### `fish-freshness-and-trade.requirement.expiry-value::fishing-advanced-guide`

- evidence_seed_key: "fish-freshness-and-trade.requirement.expiry-value::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fish-freshness-and-trade.expiry-value"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "만료 시 약 30%"
- active: true
- is_active: true

### `fish-freshness-and-trade.requirement.sale-factors::fishing-advanced-guide`

- evidence_seed_key: "fish-freshness-and-trade.requirement.sale-factors::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fish-freshness-and-trade.sale-factors"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "판매가 요소"
- active: true
- is_active: true

### Historical / inactive evidence

### `fish-freshness-and-trade.legacy.odyllita-36h::fish-freshness-2025-05-21`

- evidence_seed_key: "fish-freshness-and-trade.legacy.odyllita-36h::fish-freshness-2025-05-21"
- source_id: "fish-freshness-2025-05-21"
- title: "5월 21일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13995"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-21"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fish-freshness-and-trade"
- claim_key: "legacy.odyllita_guarantee_hours"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "오딜리타 36시간은 60시간으로 대체"
- active: false
- is_active: false

### `fish-freshness-and-trade.legacy.standard-24h::fish-freshness-2025-05-21`

- evidence_seed_key: "fish-freshness-and-trade.legacy.standard-24h::fish-freshness-2025-05-21"
- source_id: "fish-freshness-2025-05-21"
- title: "5월 21일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13995"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-21"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fish-freshness-and-trade"
- claim_key: "legacy.standard_guarantee_hours"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "일반 24시간은 48시간으로 대체"
- active: false
- is_active: false
