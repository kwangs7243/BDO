<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 일꾼 종족과 등급

## Identity

- slug: "worker-races-grades"
- name_ko: "일꾼 종족과 등급"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "고블린 계열은 작업·이동 속도, 자이언트 계열은 생산거점 기본 수확량, 인간 계열은 행운이 핵심 특성이다."
- purpose: "일꾼 계열 특성과 5단계 등급을 전략 추천 없이 구조화한다."

## Requirements

### `worker-races-grades.families`

- seed_key: "worker-races-grades.families"
- kind: "other"
- requirement_level: "required"
- title: "일꾼 계열 특성"
- description: "세 대표 계열의 공식 특성을 구분한다."
- structured_value:

```json
{
  "giant_family": {
    "base_yield_bonus_percent_approx": 68.4,
    "effects": [
      "base_production_node_yield",
      "high_stamina"
    ],
    "examples": [
      "자이언트",
      "파두스",
      "거북이"
    ],
    "not_universal_final_stat": true
  },
  "goblin_family": {
    "effects": [
      "work_speed",
      "movement_speed"
    ],
    "examples": [
      "고블린",
      "파푸",
      "도깨비"
    ]
  },
  "human_family": {
    "effects": [
      "luck"
    ],
    "examples": [
      "인간",
      "돌쇠"
    ],
    "historical_base_luck_increase": 3,
    "not_universal_final_stat": true
  }
}
```

### `worker-races-grades.grades`

- seed_key: "worker-races-grades.grades"
- kind: "other"
- requirement_level: "required"
- title: "일꾼 등급"
- description: "현재 5단계와 특수 일꾼 예외를 기록한다."
- structured_value:

```json
{
  "fixed_special_workers": {
    "fixed_grade": true,
    "fixed_stats_and_unique_skill": true,
    "promotion_allowed": false
  },
  "grades": [
    "어수룩한",
    "일반",
    "숙련",
    "전문",
    "장인"
  ],
  "naive_exists_only_for": "giant_family"
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

- None

## Evidence and Sources

### Current evidence

### `worker-races-grades.claim.current::worker-guide`

- evidence_seed_key: "worker-races-grades.claim.current::worker-guide"
- source_id: "worker-guide"
- title: "일꾼"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=95"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-races-grades"
- claim_key: "requirements:worker-races-grades"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `worker-races-grades.claim.current::worker-overhaul-2023-05-24`

- evidence_seed_key: "worker-races-grades.claim.current::worker-overhaul-2023-05-24"
- source_id: "worker-overhaul-2023-05-24"
- title: "5월 24일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=10369"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-05-24"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-races-grades"
- claim_key: "requirements:worker-races-grades"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
