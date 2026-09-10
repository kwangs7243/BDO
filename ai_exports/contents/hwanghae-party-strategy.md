<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 황해도 파티 전략

## Identity

- slug: "hwanghae-party-strategy"
- name_ko: "황해도 파티 전략"
- category: "combat_pve"
- status: "active"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- party_type: "party"
- difficulty: "varies"

## Overview

- summary: "공식 사실과 분리한 최근 커뮤니티 합의 및 기믹 공략이다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `hwanghae-party-strategy.easy-pug`

- seed_key: "hwanghae-party-strategy.easy-pug"
- kind: "other"
- requirement_level: "recommended"
- title: "초행 파티 후보"
- description: "최근 커뮤니티에서는 불가살·지귀·우투리를 비교적 초행 파티 친화적인 후보로 자주 언급한다."
- structured_value:

```json
{
  "absolute_ranking": false,
  "bosses": [
    "Bulgasal",
    "Jigwi",
    "Uturi"
  ],
  "knowledge_role": "strategy",
  "scope": "recent_community_consensus",
  "source_dates": [
    "2026-07-27",
    "2026-07-30",
    "2026-07-31"
  ]
}
```

### `hwanghae-party-strategy.coordination`

- seed_key: "hwanghae-party-strategy.coordination"
- kind: "other"
- requirement_level: "recommended"
- title: "협업 요구가 큰 후보"
- description: "비형랑과 검은사당 흑봉황은 색·분신 또는 파티 합의가 더 필요한 후보로 언급된다."
- structured_value:

```json
{
  "absolute_ranking": false,
  "bosses": [
    "Bihyung",
    "Dark Bonghwang"
  ],
  "knowledge_role": "strategy",
  "scope": "recent_community_consensus",
  "source_dates": [
    "2026-07-27",
    "2026-07-31"
  ]
}
```

### `hwanghae-party-strategy.organized-party`

- seed_key: "hwanghae-party-strategy.organized-party"
- kind: "other"
- requirement_level: "recommended"
- title: "조직 파티 선호 후보"
- description: "폐세자와 청의동자는 고정 또는 조직된 파티 선호 후보로 언급된다."
- structured_value:

```json
{
  "absolute_ranking": false,
  "bosses": [
    "Deposed Crown Prince",
    "Blue-clad Youth"
  ],
  "knowledge_role": "strategy",
  "scope": "recent_community_consensus",
  "source_dates": [
    "2026-07-27",
    "2026-07-30"
  ]
}
```

### `hwanghae-party-strategy.mechanics`

- seed_key: "hwanghae-party-strategy.mechanics"
- kind: "other"
- requirement_level: "recommended"
- title: "대표 기믹 체크"
- description: "불가살·우투리·비형랑은 역할 분담과 시각 신호 확인이 중요하다."
- structured_value:

```json
{
  "knowledge_role": "strategy",
  "mechanics": {
    "Bihyung": [
      "color calls",
      "clones",
      "party coordination"
    ],
    "Bulgasal": [
      "iron energy",
      "object handling",
      "distance and stacks",
      "safe circle"
    ],
    "Uturi": [
      "sacks and objects",
      "adds",
      "throw timing",
      "green circle",
      "beans",
      "failed mechanic may heal boss"
    ]
  },
  "scope": "mechanics_guide",
  "universal_numeric_difficulty": false
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

### `hwanghae-party-strategy.current-system`

- seed_key: "hwanghae-party-strategy.current-system"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "black-shrine-hwanghae-current-system"
- content_name_ko: "검은사당 황해도 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/black-shrine-hwanghae-current-system.md"

## Evidence and Sources

### Current evidence

### `hwanghae-party-strategy.claim.coordination::hwanghae-party-mode-2026-07-31`

- evidence_seed_key: "hwanghae-party-strategy.claim.coordination::hwanghae-party-mode-2026-07-31"
- source_id: "hwanghae-party-mode-2026-07-31"
- title: "Party Shrine Mode - PUG experience discussion"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1vc5znz/party_shrine_mode/"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_discussion"
- published_at: "2026-07-31"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "global"
- entity_type: "content_requirement"
- entity_id: "hwanghae-party-strategy.coordination"
- claim_key: "requirement:coordination"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `hwanghae-party-strategy.claim.coordination::hwanghae-party-strategy-2026-07-27`

- evidence_seed_key: "hwanghae-party-strategy.claim.coordination::hwanghae-party-strategy-2026-07-27"
- source_id: "hwanghae-party-strategy-2026-07-27"
- title: "Party Boss Shrine - current party difficulty discussion"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1v86p3p/party_boss_shrine/"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_discussion"
- published_at: "2026-07-27"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "global"
- entity_type: "content_requirement"
- entity_id: "hwanghae-party-strategy.coordination"
- claim_key: "requirement:coordination"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `hwanghae-party-strategy.claim.easy-pug::hwanghae-hyperboost-party-2026-07-30`

- evidence_seed_key: "hwanghae-party-strategy.claim.easy-pug::hwanghae-hyperboost-party-2026-07-30"
- source_id: "hwanghae-hyperboost-party-2026-07-30"
- title: "Hyper Boost party boss routing discussion"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1vb9189/having_to_do_the_party_bosses_for_the_hyperboost/"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_discussion"
- published_at: "2026-07-30"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "global"
- entity_type: "content_requirement"
- entity_id: "hwanghae-party-strategy.easy-pug"
- claim_key: "requirement:easy-pug"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `hwanghae-party-strategy.claim.easy-pug::hwanghae-party-mode-2026-07-31`

- evidence_seed_key: "hwanghae-party-strategy.claim.easy-pug::hwanghae-party-mode-2026-07-31"
- source_id: "hwanghae-party-mode-2026-07-31"
- title: "Party Shrine Mode - PUG experience discussion"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1vc5znz/party_shrine_mode/"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_discussion"
- published_at: "2026-07-31"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "global"
- entity_type: "content_requirement"
- entity_id: "hwanghae-party-strategy.easy-pug"
- claim_key: "requirement:easy-pug"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `hwanghae-party-strategy.claim.easy-pug::hwanghae-party-strategy-2026-07-27`

- evidence_seed_key: "hwanghae-party-strategy.claim.easy-pug::hwanghae-party-strategy-2026-07-27"
- source_id: "hwanghae-party-strategy-2026-07-27"
- title: "Party Boss Shrine - current party difficulty discussion"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1v86p3p/party_boss_shrine/"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_discussion"
- published_at: "2026-07-27"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "global"
- entity_type: "content_requirement"
- entity_id: "hwanghae-party-strategy.easy-pug"
- claim_key: "requirement:easy-pug"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `hwanghae-party-strategy.claim.mechanics::black-shrine-party-guide-current`

- evidence_seed_key: "hwanghae-party-strategy.claim.mechanics::black-shrine-party-guide-current"
- source_id: "black-shrine-party-guide-current"
- title: "Black Shrine Party Guide"
- url: "https://www.blackdesertfoundry.com/black-shrine-party-guide/"
- publisher: "Black Desert Foundry"
- source_type: "third_party_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "global"
- entity_type: "content_requirement"
- entity_id: "hwanghae-party-strategy.mechanics"
- claim_key: "requirement:mechanics"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `hwanghae-party-strategy.claim.mechanics::hwanghae-party-strategy-2026-07-27`

- evidence_seed_key: "hwanghae-party-strategy.claim.mechanics::hwanghae-party-strategy-2026-07-27"
- source_id: "hwanghae-party-strategy-2026-07-27"
- title: "Party Boss Shrine - current party difficulty discussion"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1v86p3p/party_boss_shrine/"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_discussion"
- published_at: "2026-07-27"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "global"
- entity_type: "content_requirement"
- entity_id: "hwanghae-party-strategy.mechanics"
- claim_key: "requirement:mechanics"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `hwanghae-party-strategy.claim.organized-party::hwanghae-hyperboost-party-2026-07-30`

- evidence_seed_key: "hwanghae-party-strategy.claim.organized-party::hwanghae-hyperboost-party-2026-07-30"
- source_id: "hwanghae-hyperboost-party-2026-07-30"
- title: "Hyper Boost party boss routing discussion"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1vb9189/having_to_do_the_party_bosses_for_the_hyperboost/"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_discussion"
- published_at: "2026-07-30"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "global"
- entity_type: "content_requirement"
- entity_id: "hwanghae-party-strategy.organized-party"
- claim_key: "requirement:organized-party"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `hwanghae-party-strategy.claim.organized-party::hwanghae-party-strategy-2026-07-27`

- evidence_seed_key: "hwanghae-party-strategy.claim.organized-party::hwanghae-party-strategy-2026-07-27"
- source_id: "hwanghae-party-strategy-2026-07-27"
- title: "Party Boss Shrine - current party difficulty discussion"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1v86p3p/party_boss_shrine/"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_discussion"
- published_at: "2026-07-27"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "global"
- entity_type: "content_requirement"
- entity_id: "hwanghae-party-strategy.organized-party"
- claim_key: "requirement:organized-party"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
