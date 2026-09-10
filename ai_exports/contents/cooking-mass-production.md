<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 대량 요리

## Identity

- slug: "cooking-mass-production"
- name_ko: "대량 요리"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "10회 이상 연속 요리할 때 확률로 발동해 10회분 재료를 소모하고 10회분 결과물을 만들지만 요리 도구 내구도는 1만 소모한다."
- purpose: "대량 요리의 발동 조건과 재료·결과·내구도 처리를 구분한다."

## Requirements

### `cooking-mass-production.trigger`

- seed_key: "cooking-mass-production.trigger"
- kind: "other"
- requirement_level: "required"
- title: "발동 조건"
- description: "발동 조건의 현재 규칙이다."
- structured_value:

```json
{
  "continuous_crafts": 10,
  "probability_scales_with": "cooking_mastery"
}
```

### `cooking-mass-production.batch`

- seed_key: "cooking-mass-production.batch"
- kind: "item"
- requirement_level: "required"
- title: "발동 시 처리"
- description: "발동 시 처리의 현재 규칙이다."
- structured_value:

```json
{
  "ingredient_crafts_consumed": 10,
  "result_crafts_produced": 10,
  "utensil_durability_consumed": 1
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

### `cooking-onboarding-strategy.mass-production`

- seed_key: "cooking-onboarding-strategy.mass-production"
- direction: "incoming"
- relation_type: "related"
- content_slug: "cooking-onboarding-strategy"
- content_name_ko: "요리 입문 전략"
- content_category: "life"
- note: null
- order_no: 3
- relative_path: "../contents/cooking-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `cooking-mass-production.claim.batch::cooking-guide`

- evidence_seed_key: "cooking-mass-production.claim.batch::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "cooking-mass-production"
- claim_key: "requirement:cooking-mass-production.batch"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### `cooking-mass-production.claim.summary::cooking-guide`

- evidence_seed_key: "cooking-mass-production.claim.summary::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "cooking-mass-production"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
