<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 죽은 자들의 도시

## Identity

- slug: "city-of-the-dead"
- name_ko: "죽은 자들의 도시"
- category: "combat"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "very_high"

## Overview

- summary: "전령 계열에 군중 제어를 적용하고 울루키타의 정수 효과를 활용하는 사냥터."
- purpose: "울루키타 전리품과 카부아 계열 획득"

## Requirements

### `city-of-the-dead.current-stats`

- seed_key: "city-of-the-dead.current-stats"
- kind: "stat"
- requirement_level: "recommended"
- title: "현재 권장 수치"
- description: "표기 공격력 320, 공격력 상한 1295. 과거 권장 방어력 380."
- structured_value:

```json
{
  "ap_cap": 1295,
  "historical_sheet_dp_recommended": 380,
  "knowledge_role": "fact",
  "sheet_ap_recommended": 320
}
```

### `city-of-the-dead.mechanic`

- seed_key: "city-of-the-dead.mechanic"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "전령 무력화 기믹"
- description: "전령 계열에 CC를 적용해 주변 적을 무력화하고 울루키타의 정수를 얻는다."
- structured_value:

```json
{
  "buff": "Ulukita Essence",
  "knowledge_role": "fact",
  "uses_crowd_control": true
}
```

### `city-of-the-dead.june-2026-current`

- seed_key: "city-of-the-dead.june-2026-current"
- kind: "item"
- requirement_level: "optional"
- title: "2026-06-10 최신 조정"
- description: "잡동사니, 아그리스, 정수 및 카부아 전리품 최신 값."
- structured_value:

```json
{
  "commander_trash_max": 250,
  "commander_trash_min": 220,
  "effective_from": "2026-06-10",
  "essence_of_devouring_chance_change_percent": 20,
  "kabuua_artifact_available": true,
  "kabuua_fragment_available": true,
  "knowledge_role": "fact",
  "main_agris_cost": 9,
  "main_trash_max": 6,
  "main_trash_min": 4,
  "previous_commander_trash": [
    120,
    210
  ],
  "previous_main_agris_cost": 6,
  "previous_main_trash": [
    2,
    4
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

### `city-of-the-dead.attack-cap`

- seed_key: "city-of-the-dead.attack-cap"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-zone-attack-cap"
- content_name_ko: "사냥터 공격력 제한"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/grind-zone-attack-cap.md"
### `city-of-the-dead.agris`

- seed_key: "city-of-the-dead.agris"
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

### `city-of-the-dead.claim.current-stats::combat-system-rework-2025-07-23`

- evidence_seed_key: "city-of-the-dead.claim.current-stats::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "city-of-the-dead.current-stats"
- claim_key: "requirement:current-stats"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `city-of-the-dead.claim.june-2026-current::grind-profit-update-2026-06-10`

- evidence_seed_key: "city-of-the-dead.claim.june-2026-current::grind-profit-update-2026-06-10"
- source_id: "grind-profit-update-2026-06-10"
- title: "6월 10일(수) 업데이트 안내 (최종 수정 : 2026-06-11 19:22)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15720"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-06-10"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "city-of-the-dead.june-2026-current"
- claim_key: "requirement:june-2026-current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `city-of-the-dead.claim.mechanic::combat-system-rework-2025-07-23`

- evidence_seed_key: "city-of-the-dead.claim.mechanic::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "city-of-the-dead.mechanic"
- claim_key: "requirement:mechanic"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
