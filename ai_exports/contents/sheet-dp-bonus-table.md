<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 표기 방어력 구간 보너스

## Identity

- slug: "sheet-dp-bonus-table"
- name_ko: "표기 방어력 구간 보너스"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "표기 방어력별 피해 감소율과 추가 피해 감소 경계값을 구조화한 표다."
- purpose: "방어력 구간 보너스의 경계값을 공식 표 기준으로 검증한다."

## Requirements

### `sheet-dp-bonus-table.current`

- seed_key: "sheet-dp-bonus-table.current"
- kind: "stat"
- requirement_level: "required"
- title: "현행 방어력 구간표"
- description: "피해 감소율과 추가 피해 감소의 시작 방어력 지점을 각각 보존한다."
- structured_value:

```json
{
  "benchmarks": {
    "dp_400_flat_dr": 81,
    "dp_401_rate_percent": 30,
    "dp_481_flat_dr": 91,
    "dp_486_flat_dr": 92,
    "dp_531_flat_dr": 101
  },
  "current_as_of": "2026-09-04",
  "damage_reduction_rate_breakpoints": {
    "203": 1,
    "211": 2,
    "218": 3,
    "226": 4,
    "233": 5,
    "241": 6,
    "248": 7,
    "256": 8,
    "263": 9,
    "271": 10,
    "278": 11,
    "286": 12,
    "293": 13,
    "301": 14,
    "308": 15,
    "315": 16,
    "322": 17,
    "329": 18,
    "335": 19,
    "341": 20,
    "347": 21,
    "353": 22,
    "359": 23,
    "365": 24,
    "371": 25,
    "377": 26,
    "383": 27,
    "389": 28,
    "395": 29,
    "401": 30
  },
  "flat_damage_reduction_breakpoints": {
    "253": 2,
    "256": 4,
    "259": 6,
    "262": 8,
    "265": 10,
    "270": 12,
    "275": 14,
    "279": 16,
    "283": 18,
    "287": 20,
    "290": 22,
    "293": 24,
    "296": 26,
    "299": 28,
    "302": 31,
    "305": 35,
    "308": 37,
    "311": 40,
    "314": 43,
    "317": 46,
    "321": 50,
    "324": 51,
    "326": 52,
    "328": 53,
    "330": 54,
    "332": 55,
    "334": 56,
    "336": 57,
    "338": 58,
    "340": 59,
    "342": 60,
    "345": 61,
    "348": 63,
    "351": 64,
    "357": 65,
    "360": 66,
    "363": 67,
    "366": 68,
    "369": 69,
    "371": 70,
    "374": 71,
    "377": 72,
    "380": 73,
    "383": 74,
    "387": 75,
    "390": 76,
    "392": 77,
    "395": 78,
    "400": 81,
    "405": 82,
    "410": 83,
    "415": 84,
    "420": 85,
    "426": 86,
    "440": 87,
    "455": 88,
    "476": 90,
    "481": 91,
    "486": 92,
    "491": 93,
    "496": 94,
    "501": 95,
    "506": 96,
    "511": 97,
    "516": 98,
    "521": 99,
    "526": 100,
    "531": 101
  },
  "knowledge_role": "fact"
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

### `sheet-dp-bonus-table.foundation`

- seed_key: "sheet-dp-bonus-table.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "combat-stat-foundation"
- content_name_ko: "전투 능력치 기초"
- content_category: "combat_pve"
- note: "표기 방어력의 구간 보너스를 정의한다."
- order_no: 1
- relative_path: "../contents/combat-stat-foundation.md"

## Evidence and Sources

### Current evidence

### `sheet-dp-bonus-table.claim.current::combat-stat-bonus-guide`

- evidence_seed_key: "sheet-dp-bonus-table.claim.current::combat-stat-bonus-guide"
- source_id: "combat-stat-bonus-guide"
- title: "공격력 및 방어력 구간 보너스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=416"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "sheet-dp-bonus-table.current"
- claim_key: "requirement:sheet-dp-bonus-table.current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
