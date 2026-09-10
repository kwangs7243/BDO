<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 사냥 세팅 전략 기초

## Identity

- slug: "grind-setup-strategy-foundation"
- name_ko: "사냥 세팅 전략 기초"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "사냥터별 공격력 제한·적중·특수 공격·버프·획득 효과를 한 번에 점검하는 전략 틀이다."
- purpose: "사냥 세팅 추천을 검증 가능한 사실과 시점 의존 전략으로 분리한다."

## Requirements

### `grind-setup-strategy-foundation.checkpoints`

- seed_key: "grind-setup-strategy-foundation.checkpoints"
- kind: "other"
- requirement_level: "recommended"
- title: "세팅 점검 항목"
- description: "목표 사냥터의 최종 공격력 범위와 제한, 적중·특수 공격, 수정·광명석, 버프, 획득 효과를 순서대로 점검한다."
- structured_value:

```json
{
  "checkpoints": [
    "final_ap_range",
    "zone_attack_cap",
    "accuracy",
    "special_attack",
    "crystals",
    "lightstones",
    "combat_buffs",
    "drop_rate",
    "agris"
  ],
  "class_and_zone_context_required": true,
  "current_as_of": "2026-09-04",
  "knowledge_role": "strategy"
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `grind-setup-strategy-foundation.section.boundary`

- seed_key: "grind-setup-strategy-foundation.section.boundary"
- section_type: "strategy"
- title: "사실과 추천의 경계"
- order_no: 1

#### body_markdown

공식 수치와 적용 규칙은 FACT로 고정하되, 수정·광명석·장비의 선택은 작성일·직업·사냥터·플레이 방식이 붙은 STRATEGY로 다룬다. 가이드 인덱스는 자료 탐색용이며 그 자체를 수치 근거로 사용하지 않는다.

## Related Contents

### `grind-setup-strategy-foundation.recommendation`

- seed_key: "grind-setup-strategy-foundation.recommendation"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "grind-zone-recommendation-system"
- content_name_ko: "사냥터 추천 시스템"
- content_category: "combat_pve"
- note: "최종 공격력 기반 추천 규칙을 먼저 확인한다."
- order_no: 1
- relative_path: "../contents/grind-zone-recommendation-system.md"
### `grind-setup-strategy-foundation.crystals`

- seed_key: "grind-setup-strategy-foundation.crystals"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "pve-crystal-strategy"
- content_name_ko: "PvE 수정 구성 전략"
- content_category: "combat_pve"
- note: "사냥터 조건에 맞춘 수정 전략을 연결한다."
- order_no: 2
- relative_path: "../contents/pve-crystal-strategy.md"
### `grind-setup-strategy-foundation.lightstones`

- seed_key: "grind-setup-strategy-foundation.lightstones"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "pve-lightstone-strategy"
- content_name_ko: "PvE 광명석 조합 전략"
- content_category: "combat_pve"
- note: "사냥터 조건에 맞춘 광명석 전략을 연결한다."
- order_no: 3
- relative_path: "../contents/pve-lightstone-strategy.md"
### `grind-setup-strategy-foundation.buffs`

- seed_key: "grind-setup-strategy-foundation.buffs"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "combat-buff-foundation"
- content_name_ko: "전투 버프 기초"
- content_category: "combat_pve"
- note: "전투 버프 준비 항목을 연결한다."
- order_no: 4
- relative_path: "../contents/combat-buff-foundation.md"
### `grind-setup-strategy-foundation.loot`

- seed_key: "grind-setup-strategy-foundation.loot"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "item-drop-rate-system"
- content_name_ko: "아이템 획득 확률 증가 시스템"
- content_category: "combat_pve"
- note: "아이템 획득 확률과 수량 효과를 연결한다."
- order_no: 5
- relative_path: "../contents/item-drop-rate-system.md"
### `marni-combat-analyzer.measurement-foundation`

- seed_key: "marni-combat-analyzer.measurement-foundation"
- direction: "incoming"
- relation_type: "related"
- content_slug: "marni-combat-analyzer"
- content_name_ko: "마르니의 전투 분석기"
- content_category: "system"
- note: null
- order_no: 1
- relative_path: "../contents/marni-combat-analyzer.md"
### `darkseekers-retreat.setup`

- seed_key: "darkseekers-retreat.setup"
- direction: "incoming"
- relation_type: "related"
- content_slug: "darkseekers-retreat"
- content_name_ko: "어둠 추종자 침소"
- content_category: "combat"
- note: null
- order_no: 2
- relative_path: "../contents/darkseekers-retreat.md"
### `hexe-sanctuary-elvia.setup`

- seed_key: "hexe-sanctuary-elvia.setup"
- direction: "incoming"
- relation_type: "related"
- content_slug: "hexe-sanctuary-elvia"
- content_name_ko: "[엘비아] 헥세 성역"
- content_category: "combat"
- note: null
- order_no: 2
- relative_path: "../contents/hexe-sanctuary-elvia.md"
### `tungrad-ruins.setup`

- seed_key: "tungrad-ruins.setup"
- direction: "incoming"
- relation_type: "related"
- content_slug: "tungrad-ruins"
- content_name_ko: "툰그라드 유적지"
- content_category: "combat"
- note: null
- order_no: 2
- relative_path: "../contents/tungrad-ruins.md"

## Evidence and Sources

### Current evidence

### `grind-setup-strategy-foundation.claim.checkpoints::blood-altar-challenge-2026-07-15`

- evidence_seed_key: "grind-setup-strategy-foundation.claim.checkpoints::blood-altar-challenge-2026-07-15"
- source_id: "blood-altar-challenge-2026-07-15"
- title: "7월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15878"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "grind-setup-strategy-foundation.checkpoints"
- claim_key: "requirement:grind-setup-strategy-foundation.checkpoints"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `grind-setup-strategy-foundation.claim.checkpoints::combat-system-rework-2025-07-23`

- evidence_seed_key: "grind-setup-strategy-foundation.claim.checkpoints::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "grind-setup-strategy-foundation.checkpoints"
- claim_key: "requirement:grind-setup-strategy-foundation.checkpoints"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `grind-setup-strategy-foundation.claim.checkpoints::grind-selection-strategy-2025-11-18`

- evidence_seed_key: "grind-setup-strategy-foundation.claim.checkpoints::grind-selection-strategy-2025-11-18"
- source_id: "grind-selection-strategy-2025-11-18"
- title: "[신규/복귀 모험가] - 인게임에서 내게 맞는 사냥터 찾아보기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=142984"
- publisher: "Pearl Abyss Community"
- source_type: "community_strategy"
- published_at: "2025-11-18"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "grind-setup-strategy-foundation.checkpoints"
- claim_key: "requirement:grind-setup-strategy-foundation.checkpoints"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `grind-setup-strategy-foundation.claim.checkpoints::softcap-strategy-2025-07-29`

- evidence_seed_key: "grind-setup-strategy-foundation.claim.checkpoints::softcap-strategy-2025-07-29"
- source_id: "softcap-strategy-2025-07-29"
- title: "공방합과 소프트캡을 고려한 성장 전략"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=137536"
- publisher: "Pearl Abyss Community"
- source_type: "community_strategy"
- published_at: "2025-07-29"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "grind-setup-strategy-foundation.checkpoints"
- claim_key: "requirement:grind-setup-strategy-foundation.checkpoints"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
