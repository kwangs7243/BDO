<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 마녀의 별미

## Identity

- slug: "witch-delicacy"
- name_ko: "마녀의 별미"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "요리 중 획득하는 부산물로 맥주·우유·공헌도 경험치와 요리 경험치 교환에 사용한다."
- purpose: "요리 부산물의 현재 교환 용도를 기록한다."

## Requirements

### `witch-delicacy.origin`

- seed_key: "witch-delicacy.origin"
- kind: "item"
- requirement_level: "required"
- title: "획득 경로"
- description: "획득 경로의 현재 규칙이다."
- structured_value:

```json
{
  "activity": "cooking",
  "kind": "byproduct"
}
```

### `witch-delicacy.exchange`

- seed_key: "witch-delicacy.exchange"
- kind: "item"
- requirement_level: "required"
- title: "교환 보상 종류"
- description: "교환 보상 종류의 현재 규칙이다."
- structured_value:

```json
{
  "exclusive_npc": false,
  "guide_npc": "Nadia Rowen",
  "rewards": [
    "beer",
    "milk",
    "contribution_exp_and_cooking_exp"
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

### `cooking-onboarding-strategy.witch-delicacy`

- seed_key: "cooking-onboarding-strategy.witch-delicacy"
- direction: "incoming"
- relation_type: "related"
- content_slug: "cooking-onboarding-strategy"
- content_name_ko: "요리 입문 전략"
- content_category: "life"
- note: null
- order_no: 4
- relative_path: "../contents/cooking-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `witch-delicacy.claim.summary::cooking-guide`

- evidence_seed_key: "witch-delicacy.claim.summary::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "witch-delicacy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
