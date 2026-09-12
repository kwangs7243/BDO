<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 연금 결과물과 부산물

## Identity

- slug: "alchemy-products-and-byproducts"
- name_ko: "연금 결과물과 부산물"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "연금은 주 결과물 외에 숙련도에 따라 일반·특수·희귀 추가 결과물을 얻을 수 있다."
- purpose: "연금 결과물 종류를 공식 변경 내역에 근거해 분류하되 전체 레시피 DB로 확대하지 않는다."

## Requirements

### `alchemy-products-and-byproducts.classes`

- seed_key: "alchemy-products-and-byproducts.classes"
- kind: "other"
- requirement_level: "required"
- title: "추가 결과물 분류"
- description: "추가 결과물 분류의 현재 규칙이다."
- structured_value:

```json
{
  "alchemy_stone_names_defer_to_2026_progression": true,
  "classes": [
    "normal",
    "special",
    "rare"
  ],
  "full_recipe_database": false,
  "mastery_affects_probability": true,
  "new_examples": [
    "plywood_hardener",
    "leather_glaze",
    "mystical_spirit_powder"
  ],
  "probability_increased_examples": [
    "sturdy_destruction_alchemy_stone",
    "sturdy_protection_alchemy_stone",
    "sturdy_life_alchemy_stone",
    "caphras_stone",
    "cron_stone"
  ]
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

### `alchemy-onboarding-strategy.products`

- seed_key: "alchemy-onboarding-strategy.products"
- direction: "incoming"
- relation_type: "related"
- content_slug: "alchemy-onboarding-strategy"
- content_name_ko: "연금 입문 전략"
- content_category: "life"
- note: null
- order_no: 3
- relative_path: "../contents/alchemy-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `alchemy-products-and-byproducts.claim.summary::alchemy-guide`

- evidence_seed_key: "alchemy-products-and-byproducts.claim.summary::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금 고급 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-products-and-byproducts"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-products-and-byproducts.claim.summary::alchemy-products-2024-03-20`

- evidence_seed_key: "alchemy-products-and-byproducts.claim.summary::alchemy-products-2024-03-20"
- source_id: "alchemy-products-2024-03-20"
- title: "3월 20일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11917"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-03-20"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-products-and-byproducts"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
