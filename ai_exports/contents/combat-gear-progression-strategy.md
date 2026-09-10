<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 전투 장비 성장 전략

## Identity

- slug: "combat-gear-progression-strategy"
- name_ko: "전투 장비 성장 전략"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "현재 보유 장비와 목표 사냥터를 기준으로 다음 전투 장비 투자를 비교하는 전략 틀이다."
- purpose: "시점 의존적인 커뮤니티 성장 순서를 공식 시스템 사실과 분리한다."

## Requirements

### `combat-gear-progression-strategy.context`

- seed_key: "combat-gear-progression-strategy.context"
- kind: "gear"
- requirement_level: "recommended"
- title: "성장 순서 판단 맥락"
- description: "추천 순서는 계정 진행도, 보유 장비, 목표 사냥터와 당시 지원 이벤트에 따라 달라진다."
- structured_value:

```json
{
  "context_dimensions": [
    "account_progress",
    "owned_gear",
    "target_zone",
    "current_progression_support"
  ],
  "current_as_of": "2026-09-04",
  "exact_gear_stats_included": false,
  "knowledge_role": "strategy",
  "permanent_sequence": false
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `combat-gear-progression-strategy.section.workflow`

- seed_key: "combat-gear-progression-strategy.section.workflow"
- section_type: "strategy"
- title: "비교 절차"
- order_no: 1

#### body_markdown

현재 표기·최종 능력치와 목표 사냥터 제한을 먼저 확인한 뒤, 최신 공식 성장 지원과 날짜가 명시된 커뮤니티 경로를 교차 검토한다. 특정 장비 순서는 영구 정답으로 보존하지 않는다.

## Related Contents

### `combat-gear-progression-strategy.stats`

- seed_key: "combat-gear-progression-strategy.stats"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "sheet-vs-final-stats"
- content_name_ko: "표기 능력치와 최종 능력치"
- content_category: "combat_pve"
- note: "표기와 최종 능력치 차이를 먼저 이해한다."
- order_no: 1
- relative_path: "../contents/sheet-vs-final-stats.md"
### `combat-gear-progression-strategy.recommendation`

- seed_key: "combat-gear-progression-strategy.recommendation"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-zone-recommendation-system"
- content_name_ko: "사냥터 추천 시스템"
- content_category: "combat_pve"
- note: "목표 사냥터의 최종 공격력 범위를 참고한다."
- order_no: 2
- relative_path: "../contents/grind-zone-recommendation-system.md"
### `account-progression-foundation.combat`

- seed_key: "account-progression-foundation.combat"
- direction: "incoming"
- relation_type: "related"
- content_slug: "account-progression-foundation"
- content_name_ko: "가문 성장 기반"
- content_category: "progression"
- note: null
- order_no: 4
- relative_path: "../contents/account-progression-foundation.md"

## Evidence and Sources

### Current evidence

### `combat-gear-progression-strategy.claim.context::blood-altar-challenge-2026-07-15`

- evidence_seed_key: "combat-gear-progression-strategy.claim.context::blood-altar-challenge-2026-07-15"
- source_id: "blood-altar-challenge-2026-07-15"
- title: "7월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15878"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-gear-progression-strategy.context"
- claim_key: "requirement:combat-gear-progression-strategy.context"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `combat-gear-progression-strategy.claim.context::combat-gear-a-to-j-2026-04-22`

- evidence_seed_key: "combat-gear-progression-strategy.claim.context::combat-gear-a-to-j-2026-04-22"
- source_id: "combat-gear-a-to-j-2026-04-22"
- title: "전투 장비 A부터 J까지"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=151286"
- publisher: "Pearl Abyss Community"
- source_type: "community_strategy"
- published_at: "2026-04-22"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-gear-progression-strategy.context"
- claim_key: "requirement:combat-gear-progression-strategy.context"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `combat-gear-progression-strategy.claim.context::hyper-boost-gear-strategy-2026-08-19`

- evidence_seed_key: "combat-gear-progression-strategy.claim.context::hyper-boost-gear-strategy-2026-08-19"
- source_id: "hyper-boost-gear-strategy-2026-08-19"
- title: "하이퍼 부스트 장비 스펙업 가이드 정리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=156089"
- publisher: "Pearl Abyss Community"
- source_type: "community_strategy"
- published_at: "2026-08-19"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-gear-progression-strategy.context"
- claim_key: "requirement:combat-gear-progression-strategy.context"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
