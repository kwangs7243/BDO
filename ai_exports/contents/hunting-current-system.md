<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 수렵 현재 시스템

## Identity

- slug: "hunting-current-system"
- name_ko: "수렵 현재 시스템"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "수렵 몬스터는 일반 전투 무기보다 수렵용 화승총·저격총으로 처치하고 도축용 칼로 채집한다."
- purpose: "수렵 전투와 처치 후 도축을 일반 채집 도축과 구분한다."

## Requirements

### `hunting-current-system.flow`

- seed_key: "hunting-current-system.flow"
- kind: "other"
- requirement_level: "required"
- title: "수렵 흐름"
- description: "수렵 흐름의 현재 규칙이다."
- structured_value:

```json
{
  "combat_weapons_efficient": false,
  "hunting_weapons": [
    "matchlock",
    "sniper_rifle"
  ],
  "post_kill_tool": "butcher_knife"
}
```

### `hunting-current-system.balance-2026-09-02`

- seed_key: "hunting-current-system.balance-2026-09-02"
- kind: "other"
- requirement_level: "required"
- title: "현재 방어·체력 판정"
- description: "현재 방어·체력 판정의 현재 규칙이다."
- structured_value:

```json
{
  "combat_critical_and_special_damage_scope_expanded": true,
  "combat_gear_defense_applies": true,
  "hp_20_percent_exceptions": [
    "라우라우",
    "산발바닥",
    "대왕고래"
  ],
  "hunting_specific_defense_removed": true,
  "morning_light_sniper_hp_increase_percent": 10,
  "most_hunting_monster_hp_increase_percent": 20
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

### `hunting-current-system.gathering`

- seed_key: "hunting-current-system.gathering"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "gathering-current-system"
- content_name_ko: "채집 현재 시스템"
- content_category: "life"
- note: "수렵 처치 후 도축과 일반 동물 자원 채집은 구분한다."
- order_no: 1
- relative_path: "../contents/gathering-current-system.md"
### `hunting-onboarding-strategy.current-system`

- seed_key: "hunting-onboarding-strategy.current-system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "hunting-onboarding-strategy"
- content_name_ko: "수렵 입문 전략"
- content_category: "life"
- note: "처치와 도축 등 현재 사실 규칙은 현재 시스템에서 확인한다."
- order_no: 1
- relative_path: "../contents/hunting-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `hunting-current-system.claim.balance::life-unification-2026-09-02`

- evidence_seed_key: "hunting-current-system.claim.balance::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "hunting-current-system"
- claim_key: "requirement:hunting-current-system.balance-2026-09-02"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### `hunting-current-system.claim.flow::hunting-guide`

- evidence_seed_key: "hunting-current-system.claim.flow::hunting-guide"
- source_id: "hunting-guide"
- title: "수렵"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "hunting-current-system"
- claim_key: "requirement:hunting-current-system.flow"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
