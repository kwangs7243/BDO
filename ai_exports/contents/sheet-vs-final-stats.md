<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 표기 능력치와 최종 능력치

## Identity

- slug: "sheet-vs-final-stats"
- name_ko: "표기 능력치와 최종 능력치"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "장비 창의 표기 수치와 몬스터에게 적용되는 최종 수치는 같지 않다."
- purpose: "사냥터 추천과 장비 비교에서 표기 수치만으로 판단하는 오류를 막는다."

## Requirements

### `sheet-vs-final-stats.distinction`

- seed_key: "sheet-vs-final-stats.distinction"
- kind: "stat"
- requirement_level: "required"
- title: "표기와 최종 수치 구분"
- description: "최종 공격력은 표기 공격력 외에 구간 보너스와 몬스터·종족 추가 공격력 등을 포함할 수 있다."
- structured_value:

```json
{
  "final_ap_components": [
    "sheet_ap",
    "sheet_ap_bonus",
    "monster_extra_ap",
    "race_extra_ap"
  ],
  "knowledge_role": "fact",
  "sheet_equals_final": false
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

### `sheet-vs-final-stats.foundation`

- seed_key: "sheet-vs-final-stats.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "combat-stat-foundation"
- content_name_ko: "전투 능력치 기초"
- content_category: "combat_pve"
- note: "전투 능력치 기초의 표기·최종 수치 구분이다."
- order_no: 1
- relative_path: "../contents/combat-stat-foundation.md"
### `combat-gear-progression-strategy.stats`

- seed_key: "combat-gear-progression-strategy.stats"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "combat-gear-progression-strategy"
- content_name_ko: "전투 장비 성장 전략"
- content_category: "combat_pve"
- note: "표기와 최종 능력치 차이를 먼저 이해한다."
- order_no: 1
- relative_path: "../contents/combat-gear-progression-strategy.md"
### `grind-zone-recommendation-system.final-stats`

- seed_key: "grind-zone-recommendation-system.final-stats"
- direction: "incoming"
- relation_type: "related"
- content_slug: "grind-zone-recommendation-system"
- content_name_ko: "사냥터 추천 시스템"
- content_category: "combat_pve"
- note: "표기 공격력이 아닌 최종 공격력을 사용한다."
- order_no: 1
- relative_path: "../contents/grind-zone-recommendation-system.md"

## Evidence and Sources

### Current evidence

### `sheet-vs-final-stats.claim.distinction::blood-altar-challenge-2026-07-15`

- evidence_seed_key: "sheet-vs-final-stats.claim.distinction::blood-altar-challenge-2026-07-15"
- source_id: "blood-altar-challenge-2026-07-15"
- title: "7월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15878"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "sheet-vs-final-stats.distinction"
- claim_key: "requirement:sheet-vs-final-stats.distinction"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `sheet-vs-final-stats.claim.distinction::combat-stat-bonus-guide`

- evidence_seed_key: "sheet-vs-final-stats.claim.distinction::combat-stat-bonus-guide"
- source_id: "combat-stat-bonus-guide"
- title: "공격력 및 방어력 구간 보너스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=416"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "sheet-vs-final-stats.distinction"
- claim_key: "requirement:sheet-vs-final-stats.distinction"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
