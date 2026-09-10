<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 사냥터 추천 시스템

## Identity

- slug: "grind-zone-recommendation-system"
- name_ko: "사냥터 추천 시스템"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "사냥터 정보 UI는 최종 공격력을 기준으로 ±50 범위의 사냥터를 추천한다."
- purpose: "추천 UI의 입력 능력치와 제외 조건을 명확히 한다."

## Requirements

### `grind-zone-recommendation-system.current`

- seed_key: "grind-zone-recommendation-system.current"
- kind: "stat"
- requirement_level: "required"
- title: "현행 추천 기준"
- description: "최종 공격력 ±50 범위가 추천 대상이며 방어력은 필터 조건에 포함되지 않는다."
- structured_value:

```json
{
  "basis": "final_ap",
  "defense_filter_included": false,
  "includes": [
    "monster_extra_ap",
    "race_extra_ap"
  ],
  "knowledge_role": "fact",
  "range_minus": 50,
  "range_plus": 50
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

### `grind-zone-recommendation-system.final-stats`

- seed_key: "grind-zone-recommendation-system.final-stats"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sheet-vs-final-stats"
- content_name_ko: "표기 능력치와 최종 능력치"
- content_category: "combat_pve"
- note: "표기 공격력이 아닌 최종 공격력을 사용한다."
- order_no: 1
- relative_path: "../contents/sheet-vs-final-stats.md"
### `grind-zone-recommendation-system.cap`

- seed_key: "grind-zone-recommendation-system.cap"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-zone-attack-cap"
- content_name_ko: "사냥터 공격력 제한"
- content_category: "combat_pve"
- note: "추천 범위와 개별 사냥터 공격력 제한은 별도 규칙이다."
- order_no: 2
- relative_path: "../contents/grind-zone-attack-cap.md"
### `grind-setup-strategy-foundation.recommendation`

- seed_key: "grind-setup-strategy-foundation.recommendation"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "grind-setup-strategy-foundation"
- content_name_ko: "사냥 세팅 전략 기초"
- content_category: "combat_pve"
- note: "최종 공격력 기반 추천 규칙을 먼저 확인한다."
- order_no: 1
- relative_path: "../contents/grind-setup-strategy-foundation.md"
### `combat-gear-progression-strategy.recommendation`

- seed_key: "combat-gear-progression-strategy.recommendation"
- direction: "incoming"
- relation_type: "related"
- content_slug: "combat-gear-progression-strategy"
- content_name_ko: "전투 장비 성장 전략"
- content_category: "combat_pve"
- note: "목표 사냥터의 최종 공격력 범위를 참고한다."
- order_no: 2
- relative_path: "../contents/combat-gear-progression-strategy.md"
### `account-progression-foundation.grind`

- seed_key: "account-progression-foundation.grind"
- direction: "incoming"
- relation_type: "related"
- content_slug: "account-progression-foundation"
- content_name_ko: "가문 성장 기반"
- content_category: "progression"
- note: null
- order_no: 6
- relative_path: "../contents/account-progression-foundation.md"

## Evidence and Sources

### Current evidence

### `grind-zone-recommendation-system.claim.current::blood-altar-challenge-2026-07-15`

- evidence_seed_key: "grind-zone-recommendation-system.claim.current::blood-altar-challenge-2026-07-15"
- source_id: "blood-altar-challenge-2026-07-15"
- title: "7월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15878"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "grind-zone-recommendation-system.current"
- claim_key: "requirement:grind-zone-recommendation-system.current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
