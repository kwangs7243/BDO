<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 툰그라드 유적지

## Identity

- slug: "tungrad-ruins"
- name_ko: "툰그라드 유적지"
- category: "combat"
- status: "active"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "very_high"

## Overview

- summary: "툰그라드 인도자와 울루키타의 정수를 활용하는 고난도 사냥터."
- purpose: "울루키타 성장 재료와 전리품 획득"

## Requirements

### `tungrad-ruins.current-stats`

- seed_key: "tungrad-ruins.current-stats"
- kind: "stat"
- requirement_level: "recommended"
- title: "현재 권장 수치"
- description: "표기 공격력 330, 공격력 상한 1395."
- structured_value:

```json
{
  "ap_cap": 1395,
  "knowledge_role": "fact",
  "sheet_ap_recommended": 330
}
```

### `tungrad-ruins.mechanic-agris`

- seed_key: "tungrad-ruins.mechanic-agris"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "인도자 기믹과 아그리스"
- description: "인도자 중심 흐름과 몬스터별 아그리스."
- structured_value:

```json
{
  "agris_costs": {
    "executioner": 14,
    "guide_or_ascetic": 8
  },
  "knowledge_role": "fact",
  "mechanic": [
    "guide_centered_pack",
    "crowd_disable",
    "defense_reduction",
    "Ulukita Essence"
  ]
}
```

### `tungrad-ruins.rework-2025`

- seed_key: "tungrad-ruins.rework-2025"
- kind: "stat"
- requirement_level: "optional"
- title: "2025 전투 개편"
- description: "방어력·생명력·정수 피해 조정."
- structured_value:

```json
{
  "effective_from": "2025-07-23",
  "essence_bonus_damage_change_percent": -25,
  "key_monster_hp_change_percent": -30,
  "knowledge_role": "fact",
  "monster_defense_change_percent": 42
}
```

### `tungrad-ruins.strategy`

- seed_key: "tungrad-ruins.strategy"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "팩 위치와 전리품 회수"
- description: "팩 위치, 회수 시점과 직업별 편차가 중요하다."
- structured_value:

```json
{
  "current_as_of": "2026-09-04",
  "knowledge_role": "strategy",
  "tags": [
    "pack_positioning_sensitive",
    "loot_timing_sensitive",
    "class_disparity"
  ]
}
```

### `tungrad-ruins.measurement-t1`

- seed_key: "tungrad-ruins.measurement-t1"
- kind: "other"
- requirement_level: "optional"
- title: "2026-03-11 위자드 측정"
- description: "상한 초과 개별 1시간 측정."
- structured_value:

```json
{
  "above_cap": true,
  "agris": false,
  "class_known": true,
  "class_name": "위자드",
  "duration_minutes": 60,
  "freshness": "current",
  "full_buffs_reported": true,
  "knowledge_role": "measurement",
  "loot_scroll_level": 2,
  "measured_at": "2026-03-11",
  "measurement_grade": "A",
  "pets": "T3 + T5",
  "scope": "individual_session",
  "sheet_ap": 363,
  "specialization": null,
  "trash_max": 35000,
  "trash_min": 30000
}
```

### `tungrad-ruins.measurement-comparison`

- seed_key: "tungrad-ruins.measurement-comparison"
- kind: "other"
- requirement_level: "optional"
- title: "2026-08-07 동일 사용자 비교"
- description: "동일 작성자 비교 중 툰그라드 기록."
- structured_value:

```json
{
  "agris": true,
  "class_known": false,
  "comparison_group": "same-user-2026-08-07",
  "drop_rate_percent": 300,
  "duration_minutes": 60,
  "freshness": "current",
  "knowledge_role": "measurement",
  "loot_scroll_level": 2,
  "measured_at": "2026-08-07",
  "measurement_grade": "B",
  "reported_ap": 1500,
  "scope": "individual_session",
  "trash_count": 55000
}
```

### `tungrad-ruins.measurement-timing`

- seed_key: "tungrad-ruins.measurement-timing"
- kind: "other"
- requirement_level: "optional"
- title: "2026-08-18 이동 시점 비교"
- description: "팩 종료 후 이동 시점을 달리한 비교."
- structured_value:

```json
{
  "agris": true,
  "class_known": false,
  "duration_minutes": 60,
  "freshness": "current",
  "knowledge_role": "measurement",
  "loot_scroll_level": 2,
  "measured_at": "2026-08-18",
  "measurement_grade": "B",
  "scope": "individual_comparison",
  "variants": [
    {
      "movement": "immediate",
      "trash_count": 56000
    },
    {
      "movement": "delay_1_to_2_seconds",
      "trash_count": 61000
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

### `tungrad-ruins.section.interpretation`

- seed_key: "tungrad-ruins.section.interpretation"
- section_type: "strategy"
- title: "측정 해석"
- order_no: 1

#### body_markdown

측정치는 팩 위치·회수 시점·직업 조건에 묶인 기록이며 공식 평균이 아니다.

## Related Contents

### `tungrad-ruins.attack-cap`

- seed_key: "tungrad-ruins.attack-cap"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-zone-attack-cap"
- content_name_ko: "사냥터 공격력 제한"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/grind-zone-attack-cap.md"
### `tungrad-ruins.setup`

- seed_key: "tungrad-ruins.setup"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-setup-strategy-foundation"
- content_name_ko: "사냥 세팅 전략 기초"
- content_category: "combat_pve"
- note: null
- order_no: 2
- relative_path: "../contents/grind-setup-strategy-foundation.md"
### `tungrad-ruins.agris`

- seed_key: "tungrad-ruins.agris"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "agris-fever"
- content_name_ko: "아그리스의 열기"
- content_category: "combat_pve"
- note: null
- order_no: 3
- relative_path: "../contents/agris-fever.md"
### `dokkebi-forest.tungrad`

- seed_key: "dokkebi-forest.tungrad"
- direction: "incoming"
- relation_type: "alternative"
- content_slug: "dokkebi-forest"
- content_name_ko: "도깨비숲"
- content_category: "combat"
- note: null
- order_no: 2
- relative_path: "../contents/dokkebi-forest.md"

## Evidence and Sources

### Current evidence

### `tungrad-ruins.claim.current-stats::combat-system-rework-2025-07-23`

- evidence_seed_key: "tungrad-ruins.claim.current-stats::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "tungrad-ruins.current-stats"
- claim_key: "requirement:current-stats"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `tungrad-ruins.claim.measurement-comparison::v17b-provided-measurement-pack-2026-09-04`

- evidence_seed_key: "tungrad-ruins.claim.measurement-comparison::v17b-provided-measurement-pack-2026-09-04"
- source_id: "v17b-provided-measurement-pack-2026-09-04"
- title: "V1.7B Grind Spot Deep Pack - provided measurement records"
- url: "attachment://b902d37c-2b3b-4e3e-b4f3-7c1ccf094a0c/pasted-text.txt"
- publisher: "User-provided research pack"
- source_type: "community_measurement"
- published_at: "2026-09-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "tungrad-ruins.measurement-comparison"
- claim_key: "requirement:measurement-comparison"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `tungrad-ruins.claim.measurement-t1::v17b-provided-measurement-pack-2026-09-04`

- evidence_seed_key: "tungrad-ruins.claim.measurement-t1::v17b-provided-measurement-pack-2026-09-04"
- source_id: "v17b-provided-measurement-pack-2026-09-04"
- title: "V1.7B Grind Spot Deep Pack - provided measurement records"
- url: "attachment://b902d37c-2b3b-4e3e-b4f3-7c1ccf094a0c/pasted-text.txt"
- publisher: "User-provided research pack"
- source_type: "community_measurement"
- published_at: "2026-09-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "tungrad-ruins.measurement-t1"
- claim_key: "requirement:measurement-t1"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `tungrad-ruins.claim.measurement-timing::v17b-provided-measurement-pack-2026-09-04`

- evidence_seed_key: "tungrad-ruins.claim.measurement-timing::v17b-provided-measurement-pack-2026-09-04"
- source_id: "v17b-provided-measurement-pack-2026-09-04"
- title: "V1.7B Grind Spot Deep Pack - provided measurement records"
- url: "attachment://b902d37c-2b3b-4e3e-b4f3-7c1ccf094a0c/pasted-text.txt"
- publisher: "User-provided research pack"
- source_type: "community_measurement"
- published_at: "2026-09-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "tungrad-ruins.measurement-timing"
- claim_key: "requirement:measurement-timing"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `tungrad-ruins.claim.mechanic-agris::combat-system-rework-2025-07-23`

- evidence_seed_key: "tungrad-ruins.claim.mechanic-agris::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "tungrad-ruins.mechanic-agris"
- claim_key: "requirement:mechanic-agris"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `tungrad-ruins.claim.rework-2025::combat-system-rework-2025-07-23`

- evidence_seed_key: "tungrad-ruins.claim.rework-2025::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "tungrad-ruins.rework-2025"
- claim_key: "requirement:rework-2025"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `tungrad-ruins.claim.strategy::orzekea-dsr-tungrad-2026-06-11`

- evidence_seed_key: "tungrad-ruins.claim.strategy::orzekea-dsr-tungrad-2026-06-11"
- source_id: "orzekea-dsr-tungrad-2026-06-11"
- title: "Orzekea versus Darkseekers Retreat and Tungrad discussion"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1u2szo9/orzekea_vs_dsrtungrad/"
- publisher: "Reddit r/blackdesertonline"
- source_type: "community_strategy"
- published_at: "2026-06-11"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "GLOBAL"
- entity_type: "content"
- entity_id: "tungrad-ruins.strategy"
- claim_key: "requirement:strategy"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
