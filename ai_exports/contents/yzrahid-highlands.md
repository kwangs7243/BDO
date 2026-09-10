<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 이스라히드 고원

## Identity

- slug: "yzrahid-highlands"
- name_ko: "이스라히드 고원"
- category: "combat"
- status: "active"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "very_high"

## Overview

- summary: "시커리온 중심의 수리·병기 소환·반복 전투 사냥터."
- purpose: "카부아 유물·울림의 불꽃 계열 재료 획득"

## Requirements

### `yzrahid-highlands.current-stats`

- seed_key: "yzrahid-highlands.current-stats"
- kind: "stat"
- requirement_level: "recommended"
- title: "현재 권장 수치"
- description: "표기 공격력 310, 공격력 상한 1180. 과거 권장 방어력 420."
- structured_value:

```json
{
  "ap_cap": 1180,
  "historical_sheet_dp_recommended": 420,
  "knowledge_role": "fact",
  "sheet_ap_recommended": 310
}
```

### `yzrahid-highlands.mechanic-loot`

- seed_key: "yzrahid-highlands.mechanic-loot"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "시커리온 기믹과 전리품"
- description: "시커리온의 수리·병기 소환 흐름."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "major_loot": [
    "Kabuua Artifact",
    "Flame of Resonance",
    "Kabuua Fragment",
    "Embers",
    "Black Magic Crystal"
  ],
  "mechanic": [
    "repair",
    "weapon_summon",
    "repeated_combat"
  ]
}
```

### `yzrahid-highlands.rework-2025`

- seed_key: "yzrahid-highlands.rework-2025"
- kind: "stat"
- requirement_level: "optional"
- title: "2025 전투 개편"
- description: "방어력과 버프 피해 조정 및 카프라스의 돌 추가."
- structured_value:

```json
{
  "caphras_stone_added": true,
  "effective_from": "2025-07-23",
  "knowledge_role": "fact",
  "monster_defense_change_percent": 23,
  "sikerion_buff_damage_change_percent": -60
}
```

### `yzrahid-highlands.june-2026-current`

- seed_key: "yzrahid-highlands.june-2026-current"
- kind: "item"
- requirement_level: "optional"
- title: "2026-06-10 최신 조정"
- description: "동력이 넘치는 킬라르의 최신 잡동사니와 아그리스."
- structured_value:

```json
{
  "agris_cost": 264,
  "effective_from": "2026-06-10",
  "knowledge_role": "fact",
  "monster": "동력이 넘치는 킬라르",
  "previous_agris_cost": 132,
  "previous_trash_max": 110,
  "previous_trash_min": 100,
  "trash_max": 240,
  "trash_min": 200
}
```

### `yzrahid-highlands.strategy`

- seed_key: "yzrahid-highlands.strategy"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "운용 특성"
- description: "피로도가 낮다는 평가가 있으나 시커리온 광역 패턴 사망 위험이 있다."
- structured_value:

```json
{
  "current_as_of": "2026-09-04",
  "knowledge_role": "strategy",
  "profit_comparison_dynamic": true,
  "tags": [
    "stationary_mechanic",
    "low_fatigue_reported",
    "death_risk"
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

### `yzrahid-highlands.attack-cap`

- seed_key: "yzrahid-highlands.attack-cap"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-zone-attack-cap"
- content_name_ko: "사냥터 공격력 제한"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/grind-zone-attack-cap.md"
### `yzrahid-highlands.agris`

- seed_key: "yzrahid-highlands.agris"
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

### `yzrahid-highlands.claim.current-stats::combat-system-rework-2025-07-23`

- evidence_seed_key: "yzrahid-highlands.claim.current-stats::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "yzrahid-highlands.current-stats"
- claim_key: "requirement:current-stats"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `yzrahid-highlands.claim.june-2026-current::grind-profit-update-2026-06-10`

- evidence_seed_key: "yzrahid-highlands.claim.june-2026-current::grind-profit-update-2026-06-10"
- source_id: "grind-profit-update-2026-06-10"
- title: "6월 10일(수) 업데이트 안내 (최종 수정 : 2026-06-11 19:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15720"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-06-10"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "yzrahid-highlands.june-2026-current"
- claim_key: "requirement:june-2026-current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `yzrahid-highlands.claim.mechanic-loot::combat-system-rework-2025-07-23`

- evidence_seed_key: "yzrahid-highlands.claim.mechanic-loot::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "yzrahid-highlands.mechanic-loot"
- claim_key: "requirement:mechanic-loot"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `yzrahid-highlands.claim.rework-2025::combat-system-rework-2025-07-23`

- evidence_seed_key: "yzrahid-highlands.claim.rework-2025::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "yzrahid-highlands.rework-2025"
- claim_key: "requirement:rework-2025"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `yzrahid-highlands.claim.strategy::orzekea-dsr-tungrad-2026-06-11`

- evidence_seed_key: "yzrahid-highlands.claim.strategy::orzekea-dsr-tungrad-2026-06-11"
- source_id: "orzekea-dsr-tungrad-2026-06-11"
- title: "Orzekea versus Darkseekers Retreat and Tungrad discussion"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1u2szo9/orzekea_vs_dsrtungrad/"
- publisher: "Reddit r/blackdesertonline"
- source_type: "community_strategy"
- published_at: "2026-06-11"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "GLOBAL"
- entity_type: "content"
- entity_id: "yzrahid-highlands.strategy"
- claim_key: "requirement:strategy"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
