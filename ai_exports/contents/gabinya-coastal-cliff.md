<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 가비냐 해안 절벽

## Identity

- slug: "gabinya-coastal-cliff"
- name_ko: "가비냐 해안 절벽"
- category: "combat"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "very_high"

## Overview

- summary: "2026-07-29 추가된 최상위권 사냥터."
- purpose: "창조 계열 재료와 데보레카 액세서리 획득"

## Requirements

### `gabinya-coastal-cliff.current-stats`

- seed_key: "gabinya-coastal-cliff.current-stats"
- kind: "stat"
- requirement_level: "recommended"
- title: "현재 권장 수치"
- description: "표기 400/470, 최종 1990/820, 공격력 상한 2020."
- structured_value:

```json
{
  "ap_cap": 2020,
  "crowd_control": [
    "knockdown",
    "bound"
  ],
  "final_ap_recommended": 1990,
  "final_dp_recommended": 820,
  "knowledge_role": "fact",
  "launched_at": "2026-07-29",
  "sheet_ap_recommended": 400,
  "sheet_dp_recommended": 470,
  "tier": "top_end"
}
```

### `gabinya-coastal-cliff.loot-agris`

- seed_key: "gabinya-coastal-cliff.loot-agris"
- kind: "item"
- requirement_level: "optional"
- title: "잡동사니·주요 전리품·아그리스"
- description: "유황 거상 파편과 몬스터별 아그리스 소모량."
- structured_value:

```json
{
  "agris_costs": {
    "rock_or_stone_colossus": 16,
    "sulfur_stalagmite": 77,
    "sulfur_volcano_colossus": null
  },
  "knowledge_role": "fact",
  "major_loot": [
    "Creation pigments/glow",
    "Corrupted Immortal Oil",
    "Deboreka Necklace",
    "Deboreka Earring",
    "Deboreka Belt",
    "Deboreka Ring",
    "Al Yurad Ring fragment",
    "Kabuua/Dehkia core boxes"
  ],
  "trash_item": "유황 거상 파편",
  "trash_npc_price": 165508
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

### `gabinya-coastal-cliff.attack-cap`

- seed_key: "gabinya-coastal-cliff.attack-cap"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-zone-attack-cap"
- content_name_ko: "사냥터 공격력 제한"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/grind-zone-attack-cap.md"
### `gabinya-coastal-cliff.agris`

- seed_key: "gabinya-coastal-cliff.agris"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "agris-fever"
- content_name_ko: "아그리스의 열기"
- content_category: "combat_pve"
- note: null
- order_no: 2
- relative_path: "../contents/agris-fever.md"

## Evidence and Sources

### Current evidence

### `gabinya-coastal-cliff.claim.current-stats::gabinya-coastal-cliff-2026-07-29`

- evidence_seed_key: "gabinya-coastal-cliff.claim.current-stats::gabinya-coastal-cliff-2026-07-29"
- source_id: "gabinya-coastal-cliff-2026-07-29"
- title: "7월 29일(수) 업데이트 안내 - 가비냐 해안 절벽"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15966"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-07-29"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "gabinya-coastal-cliff.current-stats"
- claim_key: "requirement:current-stats"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `gabinya-coastal-cliff.claim.loot-agris::edania-internal-launch-2026-08-12`

- evidence_seed_key: "gabinya-coastal-cliff.claim.loot-agris::edania-internal-launch-2026-08-12"
- source_id: "edania-internal-launch-2026-08-12"
- title: "8월 12일(수) 업데이트 안내 - 에다니아 내부 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "gabinya-coastal-cliff.loot-agris"
- claim_key: "requirement:loot-agris"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `gabinya-coastal-cliff.claim.loot-agris::gabinya-coastal-cliff-2026-07-29`

- evidence_seed_key: "gabinya-coastal-cliff.claim.loot-agris::gabinya-coastal-cliff-2026-07-29"
- source_id: "gabinya-coastal-cliff-2026-07-29"
- title: "7월 29일(수) 업데이트 안내 - 가비냐 해안 절벽"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15966"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-07-29"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "gabinya-coastal-cliff.loot-agris"
- claim_key: "requirement:loot-agris"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
