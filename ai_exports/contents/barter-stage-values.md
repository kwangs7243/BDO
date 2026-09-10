<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 물물교환 단계별 가치와 무게

## Identity

- slug: "barter-stage-values"
- name_ko: "물물교환 단계별 가치와 무게"
- category: "ocean_barter"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "현행 1~7단계 교역품의 판매 가능 여부, 판매가와 단위 무게."
- purpose: "선박 적재와 매각 계획에 필요한 공식 수치를 제공한다."

## Requirements

### `barter-stage-values.tier1`

- seed_key: "barter-stage-values.tier1"
- kind: "item"
- requirement_level: "required"
- title: "1단계"
- description: "1단계: 판매 불가, 100 LT."
- structured_value:

```json
{
  "sale_price_silver": null,
  "saleable": false,
  "weight_lt": 100
}
```

### `barter-stage-values.tier2`

- seed_key: "barter-stage-values.tier2"
- kind: "item"
- requirement_level: "required"
- title: "2단계"
- description: "2단계: 판매 불가, 400 LT."
- structured_value:

```json
{
  "previous_weight_lt": 800,
  "sale_price_silver": null,
  "saleable": false,
  "weight_lt": 400
}
```

### `barter-stage-values.tier3`

- seed_key: "barter-stage-values.tier3"
- kind: "item"
- requirement_level: "required"
- title: "3단계"
- description: "3단계: 1,000,000 은화, 900 LT."
- structured_value:

```json
{
  "sale_price_silver": 1000000,
  "saleable": true,
  "weight_lt": 900
}
```

### `barter-stage-values.tier4`

- seed_key: "barter-stage-values.tier4"
- kind: "item"
- requirement_level: "required"
- title: "4단계"
- description: "4단계: 2,000,000 은화, 1,000 LT."
- structured_value:

```json
{
  "sale_price_silver": 2000000,
  "saleable": true,
  "weight_lt": 1000
}
```

### `barter-stage-values.tier5-normal`

- seed_key: "barter-stage-values.tier5-normal"
- kind: "item"
- requirement_level: "required"
- title: "5단계 일반"
- description: "5단계 일반: 10,000,000 은화, 1,000 LT."
- structured_value:

```json
{
  "sale_price_silver": 10000000,
  "saleable": true,
  "weight_lt": 1000
}
```

### `barter-stage-values.tier5-ocean`

- seed_key: "barter-stage-values.tier5-ocean"
- kind: "item"
- requirement_level: "required"
- title: "5단계 희귀 [대양]"
- description: "5단계 희귀 [대양]: 25,000,000 은화, 1,000 LT."
- structured_value:

```json
{
  "sale_price_silver": 25000000,
  "saleable": true,
  "weight_lt": 1000
}
```

### `barter-stage-values.tier6`

- seed_key: "barter-stage-values.tier6"
- kind: "item"
- requirement_level: "required"
- title: "6단계"
- description: "6단계: 50,000,000 은화, 2,000 LT."
- structured_value:

```json
{
  "sale_price_silver": 50000000,
  "saleable": true,
  "weight_lt": 2000
}
```

### `barter-stage-values.tier7`

- seed_key: "barter-stage-values.tier7"
- kind: "item"
- requirement_level: "required"
- title: "7단계"
- description: "7단계: 100,000,000 은화, 2,000 LT."
- structured_value:

```json
{
  "sale_price_silver": 100000000,
  "saleable": true,
  "weight_lt": 2000
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

### `barter-stage-values.relation.current-system`

- seed_key: "barter-stage-values.relation.current-system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "barter-current-system"
- content_name_ko: "현행 물물교환 시스템"
- content_category: "ocean_barter"
- note: "현행 물물교환 규칙의 단계별 기준표"
- order_no: 1
- relative_path: "../contents/barter-current-system.md"
### `barter-current-system.relation.stage-values`

- seed_key: "barter-current-system.relation.stage-values"
- direction: "incoming"
- relation_type: "related"
- content_slug: "barter-current-system"
- content_name_ko: "현행 물물교환 시스템"
- content_category: "ocean_barter"
- note: "단계별 판매가와 무게"
- order_no: 1
- relative_path: "../contents/barter-current-system.md"
### `barter-onboarding-strategy.stage-values`

- seed_key: "barter-onboarding-strategy.stage-values"
- direction: "incoming"
- relation_type: "related"
- content_slug: "barter-onboarding-strategy"
- content_name_ko: "물물교환 입문 운영 전략"
- content_category: "ocean_barter"
- note: "단계별 가치와 무게 FACT"
- order_no: 2
- relative_path: "../contents/barter-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `barter-stage-values.evidence.tier1::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-stage-values.evidence.tier1::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-stage-values.tier1"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "1단계: 판매 불가, 100 LT."
- active: true
- is_active: true

### `barter-stage-values.evidence.tier2::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-stage-values.evidence.tier2::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-stage-values.tier2"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2단계: 판매 불가, 400 LT."
- active: true
- is_active: true

### `barter-stage-values.evidence.tier3::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-stage-values.evidence.tier3::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-stage-values.tier3"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "3단계: 1,000,000 은화, 900 LT."
- active: true
- is_active: true

### `barter-stage-values.evidence.tier4::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-stage-values.evidence.tier4::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-stage-values.tier4"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "4단계: 2,000,000 은화, 1,000 LT."
- active: true
- is_active: true

### `barter-stage-values.evidence.tier5-normal::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-stage-values.evidence.tier5-normal::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-stage-values.tier5-normal"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "5단계 일반: 10,000,000 은화, 1,000 LT."
- active: true
- is_active: true

### `barter-stage-values.evidence.tier5-ocean::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-stage-values.evidence.tier5-ocean::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-stage-values.tier5-ocean"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "5단계 희귀 [대양]: 25,000,000 은화, 1,000 LT."
- active: true
- is_active: true

### `barter-stage-values.evidence.tier6::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-stage-values.evidence.tier6::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-stage-values.tier6"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "6단계: 50,000,000 은화, 2,000 LT."
- active: true
- is_active: true

### `barter-stage-values.evidence.tier7::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-stage-values.evidence.tier7::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "barter-stage-values.tier7"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "7단계: 100,000,000 은화, 2,000 LT."
- active: true
- is_active: true

### Historical / inactive evidence

- None
