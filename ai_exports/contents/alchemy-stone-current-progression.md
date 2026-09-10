<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 연금석 현재 성장 체계

## Identity

- slug: "alchemy-stone-current-progression"
- name_ko: "연금석 현재 성장 체계"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "일반 연금석은 불완전·견고·예리·영롱·화려·빛나는 6단계로 성장하며 거친·다듬어진 단계는 삭제되었다."
- purpose: "2026년 개편 이후 일반 연금석의 단계·색상·통합 성장 규칙을 기록한다."

## Requirements

### `alchemy-stone-current-progression.stages`

- seed_key: "alchemy-stone-current-progression.stages"
- kind: "other"
- requirement_level: "required"
- title: "현재 단계와 색상"
- description: "현재 단계와 색상의 현재 규칙이다."
- structured_value:

```json
{
  "removed": [
    "rough",
    "polished"
  ],
  "stages": [
    {
      "color": "white",
      "name": "imperfect"
    },
    {
      "color": "green",
      "name": "sturdy"
    },
    {
      "color": "blue",
      "name": "sharp"
    },
    {
      "color": "yellow",
      "name": "resplendent"
    },
    {
      "color": "red",
      "name": "splendid"
    },
    {
      "color": "purple",
      "name": "shining"
    }
  ]
}
```

### `alchemy-stone-current-progression.rules`

- seed_key: "alchemy-stone-current-progression.rules"
- kind: "other"
- requirement_level: "required"
- title: "통합 성장 규칙"
- description: "통합 성장 규칙의 현재 규칙이다."
- structured_value:

```json
{
  "all_enhancement_levels_available": true,
  "ancient_anvil_per_type": [
    "destruction",
    "protection",
    "life"
  ],
  "combined_state_can_grow": true,
  "failure_destruction": false,
  "failure_downgrade": false
}
```

### `alchemy-stone-current-progression.essence`

- seed_key: "alchemy-stone-current-progression.essence"
- kind: "item"
- requirement_level: "required"
- title: "충만한 하늘의 정수"
- description: "충만한 하늘의 정수의 현재 규칙이다."
- structured_value:

```json
{
  "recipes": [
    {
      "output": 1,
      "sharp_black_crystal_shard": 20,
      "weak_sky_essence": 1
    },
    {
      "oquilla_old_moon_piece": 2,
      "output": 1,
      "weak_sky_essence": 1
    },
    {
      "batch": 10,
      "black_stone_powder": 1,
      "output": 10
    }
  ],
  "uses": [
    "growth",
    "combine_with_vell_or_khan_heart_and_stone"
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

### `alchemy-stone-current-progression.integrated-life-stone`

- seed_key: "alchemy-stone-current-progression.integrated-life-stone"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-alchemy-stones"
- content_name_ko: "생활 연금석"
- content_category: "life"
- note: "일반 파괴·수호·생명 연금석 개편과 통합 생명의 연금석은 별개다."
- order_no: 1
- relative_path: "../contents/life-alchemy-stones.md"
### `alchemy-stone-growth.progression`

- seed_key: "alchemy-stone-growth.progression"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "alchemy-stone-growth"
- content_name_ko: "연금석 성장 확률과 아그리스"
- content_category: "life"
- note: "현재 6단계 성장 체계의 수치표다."
- order_no: 1
- relative_path: "../contents/alchemy-stone-growth.md"
### `alchemy-onboarding-strategy.alchemy-stone-next`

- seed_key: "alchemy-onboarding-strategy.alchemy-stone-next"
- direction: "incoming"
- relation_type: "related"
- content_slug: "alchemy-onboarding-strategy"
- content_name_ko: "연금 입문 전략"
- content_category: "life"
- note: null
- order_no: 10
- relative_path: "../contents/alchemy-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `alchemy-stone-current-progression.claim.current::dark-rift-reward-2026-01-14`

- evidence_seed_key: "alchemy-stone-current-progression.claim.current::dark-rift-reward-2026-01-14"
- source_id: "dark-rift-reward-2026-01-14"
- title: "1월 14일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15070"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-14"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-stone-current-progression"
- claim_key: "requirements:alchemy-stone-current-progression"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `alchemy-stone-current-progression.claim.legacy-failure::alchemy-stone-guide`

- evidence_seed_key: "alchemy-stone-current-progression.claim.legacy-failure::alchemy-stone-guide"
- source_id: "alchemy-stone-guide"
- title: "연금석"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=101"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-stone-current-progression"
- claim_key: "legacy:growth-failure-downgrade-or-destruction"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: false
- is_active: false

### `alchemy-stone-current-progression.claim.legacy-stages::alchemy-stone-guide`

- evidence_seed_key: "alchemy-stone-current-progression.claim.legacy-stages::alchemy-stone-guide"
- source_id: "alchemy-stone-guide"
- title: "연금석"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=101"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-stone-current-progression"
- claim_key: "legacy:rough-polished-eight-stage-progression"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: false
- is_active: false
