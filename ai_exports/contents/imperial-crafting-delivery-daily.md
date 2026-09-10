<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 황실 제작 납품 일일

## Identity

- slug: "imperial-crafting-delivery-daily"
- name_ko: "황실 제작 납품 일일"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: "solo"
- difficulty: null

## Overview

- summary: "개인 납품 한도는 요리·연금이 각각 독립적으로 매일 00:00 초기화되며, 서버 가능 수량은 정각 기준 3시간마다 갱신된다."
- purpose: "공헌도 기반의 일일 요리·연금 황실 제작 납품 한도를 각각 사용한다."

## Requirements

### `imperial-crafting-delivery-daily.personal-limit`

- seed_key: "imperial-crafting-delivery-daily.personal-limit"
- kind: "stat"
- requirement_level: "required"
- title: "개인 일일 한도"
- description: "요리와 연금 각각의 하루 최대 납품 수량은 자신의 최대 공헌도 ÷ 2다. 정수 처리 규칙은 별도로 추정하지 않는다."
- structured_value:

```json
{
  "formula": "max_contribution / 2",
  "rounding": "unresolved"
}
```

### `imperial-crafting-delivery-daily.independent-pools`

- seed_key: "imperial-crafting-delivery-daily.independent-pools"
- kind: "other"
- requirement_level: "required"
- title: "요리·연금 독립 한도"
- description: "2024-11 이후 요리와 연금의 일일 납품 한도는 서로 독립이며 한쪽 납품이 다른 쪽 한도를 소모하지 않는다."
- structured_value:

```json
{
  "alchemy_pool": "independent",
  "combined_quota": false,
  "cooking_pool": "independent"
}
```

### `imperial-crafting-delivery-daily.server-stock`

- seed_key: "imperial-crafting-delivery-daily.server-stock"
- kind: "other"
- requirement_level: "required"
- title: "서버 가능 수량 갱신"
- description: "서버의 납품 가능 수량은 정각 기준 매 3시간마다 갱신된다."
- structured_value:

```json
{
  "anchor": "on_the_hour",
  "refresh_interval_hours": 3
}
```

## Steps

### `imperial-crafting-delivery-daily.cooking`

- seed_key: "imperial-crafting-delivery-daily.cooking"
- phase: "repeat"
- order_no: 1
- title: "요리 황실 납품"
- description: "요리 전용 일일 한도에서 납품한다."
- checkable: true

### `imperial-crafting-delivery-daily.alchemy`

- seed_key: "imperial-crafting-delivery-daily.alchemy"
- phase: "repeat"
- order_no: 2
- title: "연금 황실 납품"
- description: "연금 전용 일일 한도에서 납품한다."
- checkable: true

## Schedules

### `imperial-crafting-delivery-daily.personal-reset`

- seed_key: "imperial-crafting-delivery-daily.personal-reset"
- rule_type: "attempt_reset"
- recurrence_type: "daily"
- weekday: null
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "개인 요리·연금 납품 한도: 매일 00:00 초기화"

### `imperial-crafting-delivery-daily.server-stock-refresh`

- seed_key: "imperial-crafting-delivery-daily.server-stock-refresh"
- rule_type: "stock_refresh"
- recurrence_type: "interval"
- weekday: null
- time_local: null
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "서버 납품 가능 수량: 정각 기준 매 3시간 갱신"

## Rewards

- None

## Sections

### `imperial-crafting-delivery-daily.reset-separation`

- seed_key: "imperial-crafting-delivery-daily.reset-separation"
- section_type: "common_mistakes"
- title: "개인 초기화와 서버 갱신 구분"
- order_no: 1

#### body_markdown

개인 요리·연금 한도는 매일 00:00 초기화된다. 서버 납품 가능 수량 갱신은 정각 기준 3시간마다이며 별도 주기다.

## Related Contents

### `alchemy-imperial-current.delivery`

- seed_key: "alchemy-imperial-current.delivery"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "alchemy-imperial-current"
- content_name_ko: "황실 연금 현재 상자표"
- content_category: "life"
- note: "공통 황실 제작 납품 규칙의 연금 품목표다."
- order_no: 1
- relative_path: "../contents/alchemy-imperial-current.md"
### `life-mastery-effects.imperial-delivery`

- seed_key: "life-mastery-effects.imperial-delivery"
- direction: "incoming"
- relation_type: "related"
- content_slug: "life-mastery-effects"
- content_name_ko: "생활 분야별 숙련도 효과"
- content_category: "life"
- note: "요리 숙련도의 황실 제작 납품 보너스와 기존 일일 납품 주기를 구분한다."
- order_no: 1
- relative_path: "../contents/life-mastery-effects.md"
### `cooking-mastery-effects.imperial`

- seed_key: "cooking-mastery-effects.imperial"
- direction: "incoming"
- relation_type: "related"
- content_slug: "cooking-mastery-effects"
- content_name_ko: "요리 숙련도 효과"
- content_category: "life"
- note: "황실 요리 납품 추가 이익 효과와 연결된다."
- order_no: 2
- relative_path: "../contents/cooking-mastery-effects.md"
### `imperial-fishing-delivery.crafting`

- seed_key: "imperial-fishing-delivery.crafting"
- direction: "incoming"
- relation_type: "related"
- content_slug: "imperial-fishing-delivery"
- content_name_ko: "황실 낚시 납품"
- content_category: "life"
- note: "황실 납품 interval 표현을 재사용하되 개인 한도는 공유하지 않음"
- order_no: 2
- relative_path: "../contents/imperial-fishing-delivery.md"
### `cooking-onboarding-strategy.imperial`

- seed_key: "cooking-onboarding-strategy.imperial"
- direction: "incoming"
- relation_type: "related"
- content_slug: "cooking-onboarding-strategy"
- content_name_ko: "요리 입문 전략"
- content_category: "life"
- note: null
- order_no: 5
- relative_path: "../contents/cooking-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `imperial-crafting-delivery-daily.summary::cooking-guide`

- evidence_seed_key: "imperial-crafting-delivery-daily.summary::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "imperial-crafting-delivery-daily"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "개인 일일 초기화와 서버 3시간 갱신 분리"
- active: true
- is_active: true

### `imperial-crafting-delivery-daily.summary::imperial-delivery-history`

- evidence_seed_key: "imperial-crafting-delivery-daily.summary::imperial-delivery-history"
- source_id: "imperial-delivery-history"
- title: "황실 제작 납품 개선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13111"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "imperial-crafting-delivery-daily"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "개인 일일 초기화와 서버 3시간 갱신 분리"
- active: true
- is_active: true

### `imperial-crafting-delivery-daily.summary::imperial-stock-refresh`

- evidence_seed_key: "imperial-crafting-delivery-daily.summary::imperial-stock-refresh"
- source_id: "imperial-stock-refresh"
- title: "5월 31일(금) 서버 순차 점검 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12266"
- publisher: "Pearl Abyss"
- source_type: "official_notice"
- published_at: "2024-05-31"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "imperial-crafting-delivery-daily"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "개인 일일 초기화와 서버 3시간 갱신 분리"
- active: true
- is_active: true

### `imperial-crafting-delivery-daily.requirement.independent-pools::imperial-delivery-history`

- evidence_seed_key: "imperial-crafting-delivery-daily.requirement.independent-pools::imperial-delivery-history"
- source_id: "imperial-delivery-history"
- title: "황실 제작 납품 개선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13111"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "imperial-crafting-delivery-daily.independent-pools"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "요리·연금 독립 한도"
- active: true
- is_active: true

### `imperial-crafting-delivery-daily.requirement.personal-limit::cooking-guide`

- evidence_seed_key: "imperial-crafting-delivery-daily.requirement.personal-limit::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "imperial-crafting-delivery-daily.personal-limit"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "최대 공헌도 ÷ 2, 반올림 추정 없음"
- active: true
- is_active: true

### `imperial-crafting-delivery-daily.requirement.server-stock::imperial-stock-refresh`

- evidence_seed_key: "imperial-crafting-delivery-daily.requirement.server-stock::imperial-stock-refresh"
- source_id: "imperial-stock-refresh"
- title: "5월 31일(금) 서버 순차 점검 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12266"
- publisher: "Pearl Abyss"
- source_type: "official_notice"
- published_at: "2024-05-31"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "imperial-crafting-delivery-daily.server-stock"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "정각 기준 매 3시간"
- active: true
- is_active: true

### `imperial-crafting-delivery-daily.schedule.personal-reset::cooking-guide`

- evidence_seed_key: "imperial-crafting-delivery-daily.schedule.personal-reset::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "imperial-crafting-delivery-daily.personal-reset"
- claim_key: "schedule.attempt_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "매일 00:00 개인 한도 초기화"
- active: true
- is_active: true

### `imperial-crafting-delivery-daily.schedule.stock-refresh::imperial-stock-refresh`

- evidence_seed_key: "imperial-crafting-delivery-daily.schedule.stock-refresh::imperial-stock-refresh"
- source_id: "imperial-stock-refresh"
- title: "5월 31일(금) 서버 순차 점검 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12266"
- publisher: "Pearl Abyss"
- source_type: "official_notice"
- published_at: "2024-05-31"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "imperial-crafting-delivery-daily.server-stock-refresh"
- claim_key: "schedule.stock_refresh"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "정각 기준 매 3시간 서버 수량 갱신"
- active: true
- is_active: true

### Historical / inactive evidence

- None
