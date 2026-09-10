<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# PvE 광명석 조합 전략

## Identity

- slug: "pve-lightstone-strategy"
- name_ko: "PvE 광명석 조합 전략"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "사냥터와 현재 장비의 부족 능력치에 따라 광명석 조합을 비교하는 전략 틀이다."
- purpose: "커뮤니티 추천 조합을 조건 없는 영구 정답으로 고정하지 않는다."

## Requirements

### `pve-lightstone-strategy.context`

- seed_key: "pve-lightstone-strategy.context"
- kind: "other"
- requirement_level: "recommended"
- title: "조합 선택 맥락"
- description: "공격력 제한, 적중, 종족 추가 공격력과 생존 요구를 현재 장비 상태에 맞춰 비교한다."
- structured_value:

```json
{
  "context_dimensions": [
    "zone_attack_cap",
    "accuracy",
    "race_extra_ap",
    "survivability"
  ],
  "current_as_of": "2026-09-04",
  "knowledge_role": "strategy",
  "single_best_combination": false
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `pve-lightstone-strategy.section.review`

- seed_key: "pve-lightstone-strategy.section.review"
- section_type: "strategy"
- title: "검토 기준"
- order_no: 1

#### body_markdown

공식 유물·광명석 효과를 먼저 확인한 뒤, 커뮤니티 추천의 작성일과 적용 사냥터를 함께 비교한다.

## Related Contents

### `pve-lightstone-strategy.system`

- seed_key: "pve-lightstone-strategy.system"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "combat-lightstones"
- content_name_ko: "전투 광명석"
- content_category: "combat_pve"
- note: "광명석 장착 및 조합 구조가 전제다."
- order_no: 1
- relative_path: "../contents/combat-lightstones.md"
### `grind-setup-strategy-foundation.lightstones`

- seed_key: "grind-setup-strategy-foundation.lightstones"
- direction: "incoming"
- relation_type: "related"
- content_slug: "grind-setup-strategy-foundation"
- content_name_ko: "사냥 세팅 전략 기초"
- content_category: "combat_pve"
- note: "사냥터 조건에 맞춘 광명석 전략을 연결한다."
- order_no: 3
- relative_path: "../contents/grind-setup-strategy-foundation.md"

## Evidence and Sources

### Current evidence

### `pve-lightstone-strategy.claim.context::artifact-guide`

- evidence_seed_key: "pve-lightstone-strategy.claim.context::artifact-guide"
- source_id: "artifact-guide"
- title: "유물/광명석"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=272"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "pve-lightstone-strategy.context"
- claim_key: "requirement:pve-lightstone-strategy.context"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `pve-lightstone-strategy.claim.context::softcap-strategy-2025-07-29`

- evidence_seed_key: "pve-lightstone-strategy.claim.context::softcap-strategy-2025-07-29"
- source_id: "softcap-strategy-2025-07-29"
- title: "공방합과 소프트캡을 고려한 성장 전략"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=137536"
- publisher: "Pearl Abyss Community"
- source_type: "community_strategy"
- published_at: "2025-07-29"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "pve-lightstone-strategy.context"
- claim_key: "requirement:pve-lightstone-strategy.context"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
