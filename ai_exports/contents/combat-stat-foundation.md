<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 전투 능력치 기초

## Identity

- slug: "combat-stat-foundation"
- name_ko: "전투 능력치 기초"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "표기 공격력·방어력과 최종 전투 능력치를 구분해 읽기 위한 기준이다."
- purpose: "서로 다른 공격·방어 능력치를 하나의 수치로 오해하지 않도록 용어와 적용 범위를 고정한다."

## Requirements

### `combat-stat-foundation.layers`

- seed_key: "combat-stat-foundation.layers"
- kind: "stat"
- requirement_level: "required"
- title: "능력치 계층"
- description: "표기 공격력·표기 방어력, 추가 공격력, 적중·회피, 특수 공격은 서로 다른 계층으로 계산된다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "separate_layers": [
    "sheet_ap",
    "sheet_dp",
    "extra_ap",
    "accuracy_evasion",
    "special_attack"
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

### `sheet-ap-bonus-table.foundation`

- seed_key: "sheet-ap-bonus-table.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "sheet-ap-bonus-table"
- content_name_ko: "표기 공격력 구간 보너스"
- content_category: "combat_pve"
- note: "표기 공격력의 구간 보너스를 정의한다."
- order_no: 1
- relative_path: "../contents/sheet-ap-bonus-table.md"
### `sheet-dp-bonus-table.foundation`

- seed_key: "sheet-dp-bonus-table.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "sheet-dp-bonus-table"
- content_name_ko: "표기 방어력 구간 보너스"
- content_category: "combat_pve"
- note: "표기 방어력의 구간 보너스를 정의한다."
- order_no: 1
- relative_path: "../contents/sheet-dp-bonus-table.md"
### `sheet-vs-final-stats.foundation`

- seed_key: "sheet-vs-final-stats.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "sheet-vs-final-stats"
- content_name_ko: "표기 능력치와 최종 능력치"
- content_category: "combat_pve"
- note: "전투 능력치 기초의 표기·최종 수치 구분이다."
- order_no: 1
- relative_path: "../contents/sheet-vs-final-stats.md"
### `permanent-stat-progression.combat-stats`

- seed_key: "permanent-stat-progression.combat-stats"
- direction: "incoming"
- relation_type: "related"
- content_slug: "permanent-stat-progression"
- content_name_ko: "영구 능력치 성장"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/permanent-stat-progression.md"

## Evidence and Sources

### Current evidence

### `combat-stat-foundation.claim.layers::combat-stat-bonus-guide`

- evidence_seed_key: "combat-stat-foundation.claim.layers::combat-stat-bonus-guide"
- source_id: "combat-stat-bonus-guide"
- title: "공격력 및 방어력 구간 보너스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=416"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-stat-foundation.layers"
- claim_key: "requirement:combat-stat-foundation.layers"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `combat-stat-foundation.claim.layers::combat-system-rework-2025-07-23`

- evidence_seed_key: "combat-stat-foundation.claim.layers::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-stat-foundation.layers"
- claim_key: "requirement:combat-stat-foundation.layers"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
