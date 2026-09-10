<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# [엘비아] 헥세 성역

## Identity

- slug: "hexe-sanctuary-elvia"
- name_ko: "[엘비아] 헥세 성역"
- category: "combat"
- status: "active"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "very_high"

## Overview

- summary: "이동·광역 범위·전리품 회수 조건에 따라 실측 편차가 큰 엘비아 사냥터."
- purpose: "결정화된 절망과 엘비아 전리품 획득"

## Requirements

### `hexe-sanctuary-elvia.current-stats`

- seed_key: "hexe-sanctuary-elvia.current-stats"
- kind: "stat"
- requirement_level: "recommended"
- title: "현재 권장 공격력과 상한"
- description: "표기 공격력 300, 사냥터 공격력 상한 1130."
- structured_value:

```json
{
  "ap_cap": 1130,
  "current_as_of": "2026-09-04",
  "knowledge_role": "fact",
  "sheet_ap_recommended": 300
}
```

### `hexe-sanctuary-elvia.major-loot`

- seed_key: "hexe-sanctuary-elvia.major-loot"
- kind: "item"
- requirement_level: "optional"
- title: "주요 전리품"
- description: "결정화된 절망, 잡동사니 및 엘비아 관련 전리품."
- structured_value:

```json
{
  "items": [
    "결정화된 절망",
    "잡동사니",
    "엘비아 관련 전리품"
  ],
  "knowledge_role": "fact",
  "price_values_omitted_without_current_item_source": true
}
```

### `hexe-sanctuary-elvia.strategy-variance`

- seed_key: "hexe-sanctuary-elvia.strategy-variance"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "실전 편차 요인"
- description: "밀실/필드 동선, 이동 시점, 광역 범위, 펫 회수와 숙련도가 결과에 영향을 준다."
- structured_value:

```json
{
  "current_as_of": "2026-09-04",
  "knowledge_role": "strategy",
  "silver_per_hour_is_dynamic": true,
  "tags": [
    "class_aoe_sensitive",
    "movement_sensitive",
    "pet_loot_sensitive",
    "marni_rotation_sensitive",
    "player_skill_high_variance"
  ]
}
```

### `hexe-sanctuary-elvia.measurement-h1`

- seed_key: "hexe-sanctuary-elvia.measurement-h1"
- kind: "other"
- requirement_level: "optional"
- title: "2026-03-11 전승 란 측정"
- description: "개별 1시간 세션이며 평균값이 아니다."
- structured_value:

```json
{
  "agris": false,
  "class_known": true,
  "class_name": "란",
  "duration_minutes": 60,
  "freshness": "current",
  "knowledge_role": "measurement",
  "loot_scroll_level": 2,
  "measured_at": "2026-03-11",
  "measurement_grade": "A",
  "reported_total_ap": 1300,
  "reported_total_dp": 600,
  "scope": "individual_session",
  "sheet_ap": 340,
  "sheet_dp": 404,
  "specialization": "전승",
  "trash_count": 18000
}
```

### `hexe-sanctuary-elvia.measurement-comparison`

- seed_key: "hexe-sanctuary-elvia.measurement-comparison"
- kind: "other"
- requirement_level: "optional"
- title: "2026-08-07 동일 사용자 비교"
- description: "동일 작성자의 세 사냥터 비교 중 헥세 기록."
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
  "reported_ap": 1300,
  "scope": "individual_session",
  "trash_count": 50000
}
```

### `hexe-sanctuary-elvia.measurement-berserker`

- seed_key: "hexe-sanctuary-elvia.measurement-berserker"
- kind: "other"
- requirement_level: "optional"
- title: "2026-08-10 전승 자이언트 측정"
- description: "작성자가 보고한 일반 범위와 최고 기록이며 공식 기대값이 아니다."
- structured_value:

```json
{
  "agris": true,
  "class_known": true,
  "class_name": "자이언트",
  "duration_minutes": 60,
  "freshness": "current",
  "knowledge_role": "measurement",
  "loot_scroll_level": 2,
  "measured_at": "2026-08-10",
  "measurement_grade": "B",
  "reported_ap": 388,
  "reported_max_trash": 65000,
  "scope": "individual_session",
  "specialization": "전승",
  "trash_max": 61000,
  "trash_min": 58000
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `hexe-sanctuary-elvia.section.interpretation`

- seed_key: "hexe-sanctuary-elvia.section.interpretation"
- section_type: "strategy"
- title: "측정 해석"
- order_no: 1

#### body_markdown

측정값은 조건이 다른 개별 세션이다. 특정 수치를 평균으로 사용하지 않고 클래스·Agris·밀실·펫·동선을 함께 비교한다.

## Related Contents

### `hexe-sanctuary-elvia.attack-cap`

- seed_key: "hexe-sanctuary-elvia.attack-cap"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-zone-attack-cap"
- content_name_ko: "사냥터 공격력 제한"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/grind-zone-attack-cap.md"
### `hexe-sanctuary-elvia.setup`

- seed_key: "hexe-sanctuary-elvia.setup"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-setup-strategy-foundation"
- content_name_ko: "사냥 세팅 전략 기초"
- content_category: "combat_pve"
- note: null
- order_no: 2
- relative_path: "../contents/grind-setup-strategy-foundation.md"
### `hexe-sanctuary-elvia.agris`

- seed_key: "hexe-sanctuary-elvia.agris"
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

### `hexe-sanctuary-elvia.claim.current-stats::combat-system-rework-2025-07-23`

- evidence_seed_key: "hexe-sanctuary-elvia.claim.current-stats::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "hexe-sanctuary-elvia.current-stats"
- claim_key: "requirement:current-stats"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `hexe-sanctuary-elvia.claim.major-loot::combat-system-rework-2025-07-23`

- evidence_seed_key: "hexe-sanctuary-elvia.claim.major-loot::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "hexe-sanctuary-elvia.major-loot"
- claim_key: "requirement:major-loot"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `hexe-sanctuary-elvia.claim.measurement-berserker::v17b-provided-measurement-pack-2026-09-04`

- evidence_seed_key: "hexe-sanctuary-elvia.claim.measurement-berserker::v17b-provided-measurement-pack-2026-09-04"
- source_id: "v17b-provided-measurement-pack-2026-09-04"
- title: "V1.7B Grind Spot Deep Pack - provided measurement records"
- url: "attachment://b902d37c-2b3b-4e3e-b4f3-7c1ccf094a0c/pasted-text.txt"
- publisher: "User-provided research pack"
- source_type: "community_measurement"
- published_at: "2026-09-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "hexe-sanctuary-elvia.measurement-berserker"
- claim_key: "requirement:measurement-berserker"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `hexe-sanctuary-elvia.claim.measurement-comparison::v17b-provided-measurement-pack-2026-09-04`

- evidence_seed_key: "hexe-sanctuary-elvia.claim.measurement-comparison::v17b-provided-measurement-pack-2026-09-04"
- source_id: "v17b-provided-measurement-pack-2026-09-04"
- title: "V1.7B Grind Spot Deep Pack - provided measurement records"
- url: "attachment://b902d37c-2b3b-4e3e-b4f3-7c1ccf094a0c/pasted-text.txt"
- publisher: "User-provided research pack"
- source_type: "community_measurement"
- published_at: "2026-09-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "hexe-sanctuary-elvia.measurement-comparison"
- claim_key: "requirement:measurement-comparison"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `hexe-sanctuary-elvia.claim.measurement-h1::v17b-provided-measurement-pack-2026-09-04`

- evidence_seed_key: "hexe-sanctuary-elvia.claim.measurement-h1::v17b-provided-measurement-pack-2026-09-04"
- source_id: "v17b-provided-measurement-pack-2026-09-04"
- title: "V1.7B Grind Spot Deep Pack - provided measurement records"
- url: "attachment://b902d37c-2b3b-4e3e-b4f3-7c1ccf094a0c/pasted-text.txt"
- publisher: "User-provided research pack"
- source_type: "community_measurement"
- published_at: "2026-09-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "hexe-sanctuary-elvia.measurement-h1"
- claim_key: "requirement:measurement-h1"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `hexe-sanctuary-elvia.claim.strategy::hexe-economy-discussion-2026-08-10`

- evidence_seed_key: "hexe-sanctuary-elvia.claim.strategy::hexe-economy-discussion-2026-08-10"
- source_id: "hexe-economy-discussion-2026-08-10"
- title: "Hexe income discussion at high gear"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1vk9m70/hexe_more_money_per_hr_than_edina_at_1800gs/"
- publisher: "Reddit r/blackdesertonline"
- source_type: "community_strategy"
- published_at: "2026-08-10"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "GLOBAL"
- entity_type: "content"
- entity_id: "hexe-sanctuary-elvia.strategy-variance"
- claim_key: "requirement:strategy-variance"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `hexe-sanctuary-elvia.claim.strategy::hexe-pet-bottleneck-2026-07-17`

- evidence_seed_key: "hexe-sanctuary-elvia.claim.strategy::hexe-pet-bottleneck-2026-07-17"
- source_id: "hexe-pet-bottleneck-2026-07-17"
- title: "Is Marni Hexe better suited to faster and larger AOE classes?"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1uz2r6h/is_marni_hexe_just_better_suited_to_faster_and/"
- publisher: "Reddit r/blackdesertonline"
- source_type: "community_strategy"
- published_at: "2026-07-17"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "GLOBAL"
- entity_type: "content"
- entity_id: "hexe-sanctuary-elvia.strategy-variance"
- claim_key: "requirement:strategy-variance"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
