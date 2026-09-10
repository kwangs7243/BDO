<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 낚시 현재 시스템

## Identity

- slug: "fishing-current-system"
- name_ko: "낚시 현재 시스템"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "낚시 레벨·잠재력·숙련도와 어장 자원을 구분하며, 숙련도 3000의 6.25%는 보물 등급 그룹 확률에 대한 숙련도 기여분이다."
- purpose: "낚시 핵심 능력치, 어장 상태와 자동 방생 조건을 현재 가이드에 연결한다."

## Requirements

### `fishing-current-system.stats`

- seed_key: "fishing-current-system.stats"
- kind: "stat"
- requirement_level: "required"
- title: "핵심 능력치"
- description: "낚시 레벨, 잠재력, 숙련도는 서로 다른 역할을 가진다."
- structured_value:

```json
{
  "stats": [
    "fishing_level",
    "fishing_potential",
    "fishing_mastery"
  ]
}
```

### `fishing-current-system.potential`

- seed_key: "fishing-current-system.potential"
- kind: "stat"
- requirement_level: "required"
- title: "낚시 잠재력"
- description: "0~5단계이며 입질 대기시간 등에 영향을 준다."
- structured_value:

```json
{
  "affects": [
    "bite_wait_time"
  ],
  "maximum": 5,
  "minimum": 0
}
```

### `fishing-current-system.mastery`

- seed_key: "fishing-current-system.mastery"
- kind: "stat"
- requirement_level: "required"
- title: "낚시 숙련도"
- description: "표의 값은 모든 낚시의 최종 확률이 아니라 숙련도 기반 보물 그룹 확률 기여분이다."
- structured_value:

```json
{
  "breakpoints": [
    {
      "mastery": 0,
      "treasure_group_contribution_percent": 0.0
    },
    {
      "mastery": 500,
      "treasure_group_contribution_percent": 1.25
    },
    {
      "mastery": 1000,
      "treasure_group_contribution_percent": 2.5
    },
    {
      "mastery": 1500,
      "treasure_group_contribution_percent": 3.75
    },
    {
      "mastery": 2000,
      "treasure_group_contribution_percent": 5.0
    },
    {
      "mastery": 3000,
      "treasure_group_contribution_percent": 6.25
    }
  ],
  "interpretation": "mastery_contribution",
  "not_global_final_probability": true
}
```

### `fishing-current-system.resources`

- seed_key: "fishing-current-system.resources"
- kind: "other"
- requirement_level: "required"
- title: "어장 자원"
- description: "풍부·보통·고갈 상태가 입질 대기시간에 영향을 주며 실시간 상태는 영구 seed에 저장하지 않는다."
- structured_value:

```json
{
  "affects": [
    "bite_wait_time"
  ],
  "persist_live_location_state": false,
  "states": [
    "풍부",
    "보통",
    "고갈"
  ]
}
```

### `fishing-current-system.discard-grades`

- seed_key: "fishing-current-system.discard-grades"
- kind: "level"
- requirement_level: "required"
- title: "자동 방생 등급"
- description: "설정한 등급 이하 물고기를 방생할 수 있으며 흰색은 기본, 초록·파랑·노랑은 각각 전문·장인·명장 1 이상에서 열린다."
- structured_value:

```json
{
  "applies_to": [
    "manual_fishing",
    "auto_fishing"
  ],
  "thresholds": [
    {
      "discard_up_to": "white",
      "minimum_level": "default"
    },
    {
      "discard_up_to": "green",
      "minimum_level": "Professional 1"
    },
    {
      "discard_up_to": "blue",
      "minimum_level": "Artisan 1"
    },
    {
      "discard_up_to": "yellow",
      "minimum_level": "Master 1"
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

### `fishing-current-system.mastery-foundation`

- seed_key: "fishing-current-system.mastery-foundation"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-mastery-foundation"
- content_name_ko: "생활 숙련도 기반"
- content_category: "life"
- note: "최대 숙련도 3000 재사용"
- order_no: 1
- relative_path: "../contents/life-mastery-foundation.md"
### `fishing-current-system.auto`

- seed_key: "fishing-current-system.auto"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "auto-fishing"
- content_name_ko: "일반 자동 낚시"
- content_category: "life"
- note: "일반 자동 낚시"
- order_no: 2
- relative_path: "../contents/auto-fishing.md"
### `fishing-current-system.treasure`

- seed_key: "fishing-current-system.treasure"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "treasure-grade-fish"
- content_name_ko: "보물 등급 물고기"
- content_category: "life"
- note: "보물 등급 그룹"
- order_no: 3
- relative_path: "../contents/treasure-grade-fish.md"
### `auto-fishing.system`

- seed_key: "auto-fishing.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "auto-fishing"
- content_name_ko: "일반 자동 낚시"
- content_category: "life"
- note: "일반 낚시의 자동 처리"
- order_no: 1
- relative_path: "../contents/auto-fishing.md"
### `fish-freshness-and-trade.system`

- seed_key: "fish-freshness-and-trade.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "fish-freshness-and-trade"
- content_name_ko: "물고기 신선도와 무역"
- content_category: "life"
- note: "낚시 결과 판매"
- order_no: 1
- relative_path: "../contents/fish-freshness-and-trade.md"
### `fishing-encyclopedia-and-weekly-contest.system`

- seed_key: "fishing-encyclopedia-and-weekly-contest.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "fishing-encyclopedia-and-weekly-contest"
- content_name_ko: "어류 도감과 주간 낚시 대회"
- content_category: "life"
- note: "낚시 기록 progression"
- order_no: 1
- relative_path: "../contents/fishing-encyclopedia-and-weekly-contest.md"
### `fishing-onboarding-strategy.current-system`

- seed_key: "fishing-onboarding-strategy.current-system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "fishing-onboarding-strategy"
- content_name_ko: "낚시 입문 전략"
- content_category: "life"
- note: "낚시 잠재력·숙련도 등 사실 규칙은 현재 시스템에서 확인한다."
- order_no: 1
- relative_path: "../contents/fishing-onboarding-strategy.md"
### `treasure-grade-fish.mastery`

- seed_key: "treasure-grade-fish.mastery"
- direction: "incoming"
- relation_type: "related"
- content_slug: "treasure-grade-fish"
- content_name_ko: "보물 등급 물고기"
- content_category: "life"
- note: "낚시 숙련도 보물 그룹 기여분"
- order_no: 1
- relative_path: "../contents/treasure-grade-fish.md"

## Evidence and Sources

### Current evidence

### `fishing-current-system.summary::fishing-advanced-guide`

- evidence_seed_key: "fishing-current-system.summary::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fishing-current-system"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "낚시 능력치와 숙련도 기여분"
- active: true
- is_active: true

### `fishing-current-system.summary::life-mastery-prione-2025-01-08`

- evidence_seed_key: "fishing-current-system.summary::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fishing-current-system"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "낚시 능력치와 숙련도 기여분"
- active: true
- is_active: true

### `fishing-current-system.requirement.discard-grades::fishing-advanced-guide`

- evidence_seed_key: "fishing-current-system.requirement.discard-grades::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fishing-current-system.discard-grades"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "레벨별 자동 방생"
- active: true
- is_active: true

### `fishing-current-system.requirement.mastery::life-mastery-prione-2025-01-08`

- evidence_seed_key: "fishing-current-system.requirement.mastery::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fishing-current-system.mastery"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보물 그룹 숙련도 기여분"
- active: true
- is_active: true

### `fishing-current-system.requirement.potential::fishing-advanced-guide`

- evidence_seed_key: "fishing-current-system.requirement.potential::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fishing-current-system.potential"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "잠재력 5단계"
- active: true
- is_active: true

### `fishing-current-system.requirement.resources::fishing-basic-guide`

- evidence_seed_key: "fishing-current-system.requirement.resources::fishing-basic-guide"
- source_id: "fishing-basic-guide"
- title: "낚시 기초편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=107"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fishing-current-system.resources"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "어장 자원 상태"
- active: true
- is_active: true

### `fishing-current-system.requirement.stats::fishing-advanced-guide`

- evidence_seed_key: "fishing-current-system.requirement.stats::fishing-advanced-guide"
- source_id: "fishing-advanced-guide"
- title: "낚시 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fishing-current-system.stats"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "세 능력치"
- active: true
- is_active: true

### Historical / inactive evidence

- None
