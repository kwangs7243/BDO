<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 표기 공격력 구간 보너스

## Identity

- slug: "sheet-ap-bonus-table"
- name_ko: "표기 공격력 구간 보너스"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "현행 표기 공격력별 보너스 공격력과 몬스터 추가 공격력 구간을 구조화한 표다."
- purpose: "경계값과 대표 지점을 정확히 검증하고 과거 표와 혼합하지 않는다."

## Requirements

### `sheet-ap-bonus-table.current`

- seed_key: "sheet-ap-bonus-table.current"
- kind: "stat"
- requirement_level: "required"
- title: "현행 공격력 구간표"
- description: "보너스 공격력은 공식 표의 시작 지점으로, 몬스터 추가 공격력은 구간식과 경계값으로 보존한다."
- structured_value:

```json
{
  "bonus_ap_breakpoints": {
    "100": 5,
    "140": 10,
    "170": 15,
    "184": 20,
    "209": 30,
    "235": 40,
    "245": 48,
    "249": 57,
    "253": 69,
    "257": 83,
    "261": 101,
    "265": 122,
    "269": 137,
    "273": 142,
    "277": 148,
    "281": 154,
    "285": 160,
    "289": 167,
    "293": 174,
    "297": 181,
    "301": 188,
    "305": 196,
    "309": 200,
    "316": 203,
    "321": 205,
    "328": 208,
    "332": 211,
    "337": 214,
    "342": 217,
    "347": 220,
    "352": 223,
    "358": 225,
    "364": 227,
    "369": 230,
    "375": 233,
    "381": 236,
    "386": 239,
    "392": 242,
    "397": 245,
    "399": 247,
    "401": 249,
    "403": 251,
    "405": 253,
    "407": 255,
    "409": 257,
    "411": 259,
    "413": 261,
    "415": 263,
    "417": 265,
    "419": 267,
    "421": 269,
    "423": 271,
    "425": 273,
    "427": 275,
    "429": 277,
    "431": 279,
    "433": 281,
    "435": 283,
    "437": 285,
    "439": 287,
    "441": 289,
    "443": 291,
    "445": 293,
    "447": 295,
    "449": 297
  },
  "current_as_of": "2026-09-04",
  "knowledge_role": "fact",
  "monster_extra_ap_benchmarks": {
    "309": 0,
    "310": 8,
    "400": 728,
    "401": 744,
    "450": 1528
  },
  "monster_extra_ap_formula": [
    {
      "formula": "0",
      "sheet_ap_max": 309,
      "sheet_ap_min": 100
    },
    {
      "formula": "(sheet_ap - 309) * 8",
      "sheet_ap_max": 400,
      "sheet_ap_min": 310
    },
    {
      "formula": "728 + (sheet_ap - 400) * 16",
      "sheet_ap_max": 450,
      "sheet_ap_min": 401
    }
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
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "combat-stat-foundation"
- content_name_ko: "전투 능력치 기초"
- content_category: "combat_pve"
- note: "표기 공격력의 구간 보너스를 정의한다."
- order_no: 1
- relative_path: "../contents/combat-stat-foundation.md"
### `monster-extra-ap.ap-table`

- seed_key: "monster-extra-ap.ap-table"
- direction: "incoming"
- relation_type: "related"
- content_slug: "monster-extra-ap"
- content_name_ko: "몬스터 추가 공격력"
- content_category: "combat_pve"
- note: "표기 공격력 구간에 따른 몬스터 추가 공격력 표를 참조한다."
- order_no: 1
- relative_path: "../contents/monster-extra-ap.md"

## Evidence and Sources

### Current evidence

### `sheet-ap-bonus-table.claim.current::combat-stat-bonus-guide`

- evidence_seed_key: "sheet-ap-bonus-table.claim.current::combat-stat-bonus-guide"
- source_id: "combat-stat-bonus-guide"
- title: "공격력 및 방어력 구간 보너스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=416"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "sheet-ap-bonus-table.current"
- claim_key: "requirement:sheet-ap-bonus-table.current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `sheet-ap-bonus-table.claim.legacy::combat-stat-bonus-guide`

- evidence_seed_key: "sheet-ap-bonus-table.claim.legacy::combat-stat-bonus-guide"
- source_id: "combat-stat-bonus-guide"
- title: "공격력 및 방어력 구간 보너스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=416"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "sheet-ap-bonus-table.legacy"
- claim_key: "legacy:pre-current-ap-bonus-table"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
