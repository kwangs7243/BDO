<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 말 교배와 교환

## Identity

- slug: "horse-breeding-exchange"
- name_ko: "말 교배와 교환"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "교배는 교배 시장 또는 보유 말끼리 진행하고 횟수를 소모하며, 교환은 두 말을 모두 소멸시켜 자마를 얻는다."
- purpose: "교배와 교환의 서로 다른 소비 규칙을 설명한다."

## Requirements

### `horse-breeding-exchange.breeding`

- seed_key: "horse-breeding-exchange.breeding"
- kind: "other"
- requirement_level: "required"
- title: "교배"
- description: "교배의 현재 규칙이다."
- structured_value:

```json
{
  "breeding_count_decreases": true,
  "methods": [
    "breeding_market",
    "own_horses"
  ]
}
```

### `horse-breeding-exchange.exchange`

- seed_key: "horse-breeding-exchange.exchange"
- kind: "item"
- requirement_level: "required"
- title: "교환"
- description: "교환의 현재 규칙이다."
- structured_value:

```json
{
  "both_parent_horses_removed": true,
  "location": "own_stable"
}
```

### `horse-breeding-exchange.offspring`

- seed_key: "horse-breeding-exchange.offspring"
- kind: "other"
- requirement_level: "required"
- title: "자마 세대"
- description: "자마 세대의 현재 규칙이다."
- structured_value:

```json
{
  "full_calculator": false,
  "influenced_by_parents": true,
  "training_mastery_contributes_to_higher_generation": true
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

### `training-onboarding-strategy.breeding-exchange`

- seed_key: "training-onboarding-strategy.breeding-exchange"
- direction: "incoming"
- relation_type: "related"
- content_slug: "training-onboarding-strategy"
- content_name_ko: "조련 입문 운영 전략"
- content_category: "life"
- note: "교배와 교환의 소비 규칙"
- order_no: 4
- relative_path: "../contents/training-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `horse-breeding-exchange.claim.summary::training-guide`

- evidence_seed_key: "horse-breeding-exchange.claim.summary::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "horse-breeding-exchange"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
