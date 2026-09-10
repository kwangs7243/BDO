<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# PvE 수정 구성 전략

## Identity

- slug: "pve-crystal-strategy"
- name_ko: "PvE 수정 구성 전략"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "사냥터의 공격력 제한, 적중 요구와 생존 위험에 맞춰 수정 프리셋을 선택하는 전략 틀이다."
- purpose: "상황에 따라 바뀌는 추천을 영구 사실이나 단일 정답으로 고정하지 않는다."

## Requirements

### `pve-crystal-strategy.context`

- seed_key: "pve-crystal-strategy.context"
- kind: "other"
- requirement_level: "recommended"
- title: "선택 맥락"
- description: "수정 구성은 사냥터 제한, 적중, 특수 공격 활용과 사망 위험을 함께 비교한다."
- structured_value:

```json
{
  "context_dimensions": [
    "zone_attack_cap",
    "accuracy",
    "special_attack",
    "survivability",
    "death_risk"
  ],
  "current_as_of": "2026-09-04",
  "knowledge_role": "strategy",
  "single_best_build": false
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `pve-crystal-strategy.section.selection`

- seed_key: "pve-crystal-strategy.section.selection"
- section_type: "strategy"
- title: "선택 순서"
- order_no: 1

#### body_markdown

먼저 사냥터 제한과 적중 요구를 확인하고, 남는 슬롯에서 특수 공격과 생존을 비교한다. 커뮤니티 추천은 작성 시점과 캐릭터·사냥터 맥락을 함께 기록한다.

## Related Contents

### `pve-crystal-strategy.system`

- seed_key: "pve-crystal-strategy.system"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "combat-crystal-system"
- content_name_ko: "전투 수정 시스템"
- content_category: "combat_pve"
- note: "수정 시스템의 보관·프리셋·제거 규칙이 전제다."
- order_no: 1
- relative_path: "../contents/combat-crystal-system.md"
### `pve-crystal-strategy.cap`

- seed_key: "pve-crystal-strategy.cap"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-zone-attack-cap"
- content_name_ko: "사냥터 공격력 제한"
- content_category: "combat_pve"
- note: "사냥터 제한 이후 효율을 비교한다."
- order_no: 2
- relative_path: "../contents/grind-zone-attack-cap.md"
### `grind-setup-strategy-foundation.crystals`

- seed_key: "grind-setup-strategy-foundation.crystals"
- direction: "incoming"
- relation_type: "related"
- content_slug: "grind-setup-strategy-foundation"
- content_name_ko: "사냥 세팅 전략 기초"
- content_category: "combat_pve"
- note: "사냥터 조건에 맞춘 수정 전략을 연결한다."
- order_no: 2
- relative_path: "../contents/grind-setup-strategy-foundation.md"

## Evidence and Sources

### Current evidence

### `pve-crystal-strategy.claim.context::crystal-guide`

- evidence_seed_key: "pve-crystal-strategy.claim.context::crystal-guide"
- source_id: "crystal-guide"
- title: "수정 가이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=310"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "pve-crystal-strategy.context"
- claim_key: "requirement:pve-crystal-strategy.context"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `pve-crystal-strategy.claim.context::grind-selection-strategy-2025-11-18`

- evidence_seed_key: "pve-crystal-strategy.claim.context::grind-selection-strategy-2025-11-18"
- source_id: "grind-selection-strategy-2025-11-18"
- title: "[신규/복귀 모험가] - 인게임에서 내게 맞는 사냥터 찾아보기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=142984"
- publisher: "Pearl Abyss Community"
- source_type: "community_strategy"
- published_at: "2025-11-18"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "pve-crystal-strategy.context"
- claim_key: "requirement:pve-crystal-strategy.context"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
