<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 연금 현재 시스템

## Identity

- slug: "alchemy-current-system"
- name_ko: "연금 현재 시스템"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "주거지에 연금술 도구를 설치하고 재료를 넣어 연금하며, 요구 수량이 3인 재료는 3개 이상 넣어야 성공률 100%가 된다."
- purpose: "연금 시작 조건과 재료 수량·실패 소비 규칙을 설명한다."

## Requirements

### `alchemy-current-system.setup`

- seed_key: "alchemy-current-system.setup"
- kind: "other"
- requirement_level: "required"
- title: "연금 시작 조건"
- description: "연금 시작 조건의 현재 규칙이다."
- structured_value:

```json
{
  "input": "ingredients",
  "installed_tool": "alchemy_tool",
  "location": "residence"
}
```

### `alchemy-current-system.quantity`

- seed_key: "alchemy-current-system.quantity"
- kind: "other"
- requirement_level: "required"
- title: "요구 수량 충족"
- description: "요구 수량 충족의 현재 규칙이다."
- structured_value:

```json
{
  "below_required_may_fail": true,
  "example_required_quantity": 3,
  "ingredients_consumed_on_failure": true,
  "success_percent_at_or_above": 100
}
```

### `alchemy-current-system.categories`

- seed_key: "alchemy-current-system.categories"
- kind: "other"
- requirement_level: "required"
- title: "대표 연금 결과 분류"
- description: "대표 연금 결과 분류의 현재 규칙이다."
- structured_value:

```json
{
  "alchemy_oils": [
    "oil_of_regeneration"
  ],
  "basic_reagents": [
    "clear_liquid_reagent",
    "pure_powder_reagent"
  ],
  "complete_recipe_database": false,
  "elixir_stages_supported": true,
  "processed_bloods": [
    "wise_mans_blood",
    "sinners_blood"
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

### `alchemy-onboarding-strategy.current-system`

- seed_key: "alchemy-onboarding-strategy.current-system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "alchemy-onboarding-strategy"
- content_name_ko: "연금 입문 전략"
- content_category: "life"
- note: null
- order_no: 1
- relative_path: "../contents/alchemy-onboarding-strategy.md"
### `group-hunting-whale-khalk.alchemy`

- seed_key: "group-hunting-whale-khalk.alchemy"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "group-hunting-whale-khalk"
- content_name_ko: "대왕 고래와 도망자 칼크 파티 수렵"
- content_category: "life"
- note: "수렵 부산물은 연금 재료 흐름과 연결된다."
- order_no: 2
- relative_path: "../contents/group-hunting-whale-khalk.md"
### `housing-life-economy.alchemy`

- seed_key: "housing-life-economy.alchemy"
- direction: "incoming"
- relation_type: "related"
- content_slug: "housing-life-economy"
- content_name_ko: "집과 생활 경제"
- content_category: "life"
- note: "주거지는 연금술 도구 설치 장소다."
- order_no: 3
- relative_path: "../contents/housing-life-economy.md"
### `production-node-current-system.alchemy`

- seed_key: "production-node-current-system.alchemy"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "production-node-current-system"
- content_name_ko: "생산 거점 현재 시스템"
- content_category: "life"
- note: "생산 거점 재료는 연금 콘텐츠로 이어진다."
- order_no: 4
- relative_path: "../contents/production-node-current-system.md"

## Evidence and Sources

### Current evidence

### `alchemy-current-system.claim.summary::alchemy-basic-guide`

- evidence_seed_key: "alchemy-current-system.claim.summary::alchemy-basic-guide"
- source_id: "alchemy-basic-guide"
- title: "연금 기초 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-12T11:55:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-current-system"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### `alchemy-current-system.claim.summary::alchemy-guide`

- evidence_seed_key: "alchemy-current-system.claim.summary::alchemy-guide"
- source_id: "alchemy-guide"
- title: "연금"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-current-system"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
