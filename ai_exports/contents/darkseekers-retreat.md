<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 어둠 추종자 침소

## Identity

- slug: "darkseekers-retreat"
- name_ko: "어둠 추종자 침소"
- category: "combat"
- status: "active"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "very_high"

## Overview

- summary: "특수 장판·이벤트 여부가 세션 전리품 편차에 영향을 주는 울루키타 사냥터."
- purpose: "카부아·불꽃·포식의 정수 계열 획득"

## Requirements

### `darkseekers-retreat.current-stats`

- seed_key: "darkseekers-retreat.current-stats"
- kind: "stat"
- requirement_level: "recommended"
- title: "현재 권장 수치"
- description: "표기 공격력 340, 공격력 상한 1490. 과거 권장 방어력 420."
- structured_value:

```json
{
  "ap_cap": 1490,
  "historical_sheet_dp_recommended": 420,
  "knowledge_role": "fact",
  "sheet_ap_recommended": 340
}
```

### `darkseekers-retreat.major-loot`

- seed_key: "darkseekers-retreat.major-loot"
- kind: "item"
- requirement_level: "optional"
- title: "주요 전리품"
- description: "카부아, 불꽃·불씨, 포식의 정수 계열."
- structured_value:

```json
{
  "items": [
    "Kabuua Artifact",
    "Kabuua Fragment",
    "Flame and Ember",
    "Essence of Devouring"
  ],
  "knowledge_role": "fact"
}
```

### `darkseekers-retreat.rework-2025`

- seed_key: "darkseekers-retreat.rework-2025"
- kind: "stat"
- requirement_level: "optional"
- title: "2025 전투 개편"
- description: "방어력·생명력·공격력 조정."
- structured_value:

```json
{
  "effective_from": "2025-07-23",
  "knowledge_role": "fact",
  "monster_attack_change_percent": -7,
  "monster_defense_change_percent": 37,
  "monster_hp_change_percent": -15
}
```

### `darkseekers-retreat.strategy-event`

- seed_key: "darkseekers-retreat.strategy-event"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "이벤트 편차"
- description: "특수 장판/이벤트가 전리품 편차를 키울 수 있다."
- structured_value:

```json
{
  "average_from_samples_forbidden": true,
  "current_as_of": "2026-09-04",
  "knowledge_role": "strategy",
  "tags": [
    "event_rng_sensitive",
    "class_sensitive"
  ]
}
```

### `darkseekers-retreat.measurement-d1-hour`

- seed_key: "darkseekers-retreat.measurement-d1-hour"
- kind: "other"
- requirement_level: "optional"
- title: "각성 발키리 1시간 측정"
- description: "특수 장판 1회를 포함한 개별 기록."
- structured_value:

```json
{
  "agris": true,
  "class_known": true,
  "class_name": "발키리",
  "duration_minutes": 60,
  "freshness": "current",
  "knowledge_role": "measurement",
  "loot_scroll_level": 2,
  "measurement_grade": "A",
  "reported_attack_value": 1515,
  "reported_rare_events": 9,
  "scope": "individual_session",
  "source_updated_at": "2026-07-11",
  "special_field_events": 1,
  "specialization": "각성",
  "trash_min": 40000
}
```

### `darkseekers-retreat.measurement-d1-half`

- seed_key: "darkseekers-retreat.measurement-d1-half"
- kind: "other"
- requirement_level: "optional"
- title: "각성 발키리 30분 측정"
- description: "특수 장판이 없었던 개별 기록."
- structured_value:

```json
{
  "agris": true,
  "class_known": true,
  "class_name": "발키리",
  "duration_minutes": 30,
  "freshness": "current",
  "knowledge_role": "measurement",
  "loot_scroll_level": 2,
  "measurement_grade": "A",
  "reported_attack_value": 1535,
  "reported_rare_events": 4,
  "scope": "individual_session",
  "source_updated_at": "2026-07-11",
  "special_field_events": 0,
  "specialization": "각성",
  "trash_min": 20000
}
```

### `darkseekers-retreat.measurement-comparison`

- seed_key: "darkseekers-retreat.measurement-comparison"
- kind: "other"
- requirement_level: "optional"
- title: "2026-08-07 동일 사용자 비교"
- description: "동일 작성자 비교 중 침소 기록."
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
  "trash_count": 35000
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `darkseekers-retreat.section.interpretation`

- seed_key: "darkseekers-retreat.section.interpretation"
- section_type: "strategy"
- title: "측정 해석"
- order_no: 1

#### body_markdown

40,000개는 특정 각성 발키리 세션 기록이다. 35,000개 비교 표본과 이벤트·직업·동선 차이를 함께 본다.

## Related Contents

### `darkseekers-retreat.attack-cap`

- seed_key: "darkseekers-retreat.attack-cap"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-zone-attack-cap"
- content_name_ko: "사냥터 공격력 제한"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/grind-zone-attack-cap.md"
### `darkseekers-retreat.setup`

- seed_key: "darkseekers-retreat.setup"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-setup-strategy-foundation"
- content_name_ko: "사냥 세팅 전략 기초"
- content_category: "combat_pve"
- note: null
- order_no: 2
- relative_path: "../contents/grind-setup-strategy-foundation.md"
### `darkseekers-retreat.agris`

- seed_key: "darkseekers-retreat.agris"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "agris-fever"
- content_name_ko: "아그리스의 열기"
- content_category: "combat_pve"
- note: null
- order_no: 3
- relative_path: "../contents/agris-fever.md"

## Evidence and Sources

### Current evidence

### `darkseekers-retreat.claim.current-stats::combat-system-rework-2025-07-23`

- evidence_seed_key: "darkseekers-retreat.claim.current-stats::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "darkseekers-retreat.current-stats"
- claim_key: "requirement:current-stats"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `darkseekers-retreat.claim.major-loot::combat-system-rework-2025-07-23`

- evidence_seed_key: "darkseekers-retreat.claim.major-loot::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "darkseekers-retreat.major-loot"
- claim_key: "requirement:major-loot"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `darkseekers-retreat.claim.measurement-comparison::v17b-provided-measurement-pack-2026-09-04`

- evidence_seed_key: "darkseekers-retreat.claim.measurement-comparison::v17b-provided-measurement-pack-2026-09-04"
- source_id: "v17b-provided-measurement-pack-2026-09-04"
- title: "V1.7B Grind Spot Deep Pack - provided measurement records"
- url: "attachment://b902d37c-2b3b-4e3e-b4f3-7c1ccf094a0c/pasted-text.txt"
- publisher: "User-provided research pack"
- source_type: "community_measurement"
- published_at: "2026-09-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "darkseekers-retreat.measurement-comparison"
- claim_key: "requirement:measurement-comparison"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `darkseekers-retreat.claim.measurement-d1-half::v17b-provided-measurement-pack-2026-09-04`

- evidence_seed_key: "darkseekers-retreat.claim.measurement-d1-half::v17b-provided-measurement-pack-2026-09-04"
- source_id: "v17b-provided-measurement-pack-2026-09-04"
- title: "V1.7B Grind Spot Deep Pack - provided measurement records"
- url: "attachment://b902d37c-2b3b-4e3e-b4f3-7c1ccf094a0c/pasted-text.txt"
- publisher: "User-provided research pack"
- source_type: "community_measurement"
- published_at: "2026-09-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "darkseekers-retreat.measurement-d1-half"
- claim_key: "requirement:measurement-d1-half"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `darkseekers-retreat.claim.measurement-d1-hour::v17b-provided-measurement-pack-2026-09-04`

- evidence_seed_key: "darkseekers-retreat.claim.measurement-d1-hour::v17b-provided-measurement-pack-2026-09-04"
- source_id: "v17b-provided-measurement-pack-2026-09-04"
- title: "V1.7B Grind Spot Deep Pack - provided measurement records"
- url: "attachment://b902d37c-2b3b-4e3e-b4f3-7c1ccf094a0c/pasted-text.txt"
- publisher: "User-provided research pack"
- source_type: "community_measurement"
- published_at: "2026-09-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "darkseekers-retreat.measurement-d1-hour"
- claim_key: "requirement:measurement-d1-hour"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `darkseekers-retreat.claim.rework-2025::combat-system-rework-2025-07-23`

- evidence_seed_key: "darkseekers-retreat.claim.rework-2025::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "darkseekers-retreat.rework-2025"
- claim_key: "requirement:rework-2025"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `darkseekers-retreat.claim.strategy-event::orzekea-dsr-tungrad-2026-06-11`

- evidence_seed_key: "darkseekers-retreat.claim.strategy-event::orzekea-dsr-tungrad-2026-06-11"
- source_id: "orzekea-dsr-tungrad-2026-06-11"
- title: "Orzekea versus Darkseekers Retreat and Tungrad discussion"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1u2szo9/orzekea_vs_dsrtungrad/"
- publisher: "Reddit r/blackdesertonline"
- source_type: "community_strategy"
- published_at: "2026-06-11"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "GLOBAL"
- entity_type: "content"
- entity_id: "darkseekers-retreat.strategy-event"
- claim_key: "requirement:strategy-event"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
