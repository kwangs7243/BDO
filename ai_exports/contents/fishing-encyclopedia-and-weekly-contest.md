<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 어류 도감과 주간 낚시 대회

## Identity

- slug: "fishing-encyclopedia-and-weekly-contest"
- name_ko: "어류 도감과 주간 낚시 대회"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "어류 도감은 발견 어종과 최대 크기를 기록하고, 주간 낚시 대회는 월~토 지정 어종의 최대 크기와 동률 시 먼저 잡은 기록으로 순위를 정한다."
- purpose: "낚시 기록 progression과 최신 상시 대회 주기를 이벤트 보상표 없이 구조화한다."

## Requirements

### `fishing-encyclopedia-and-weekly-contest.encyclopedia`

- seed_key: "fishing-encyclopedia-and-weekly-contest.encyclopedia"
- kind: "other"
- requirement_level: "required"
- title: "어류 도감"
- description: "낚은 어종의 발견과 최대 크기 기록을 관리하며 기록 갱신 시 확인할 수 있다."
- structured_value:

```json
{
  "full_ui_replication": false,
  "tracks": [
    "species_discovery",
    "maximum_size",
    "species_knowledge"
  ]
}
```

### `fishing-encyclopedia-and-weekly-contest.ranking`

- seed_key: "fishing-encyclopedia-and-weekly-contest.ranking"
- kind: "other"
- requirement_level: "required"
- title: "순위 규칙"
- description: "매주 지정된 어종의 기간 내 최대 크기로 순위를 정하고 크기가 같으면 먼저 낚은 기록이 앞선다."
- structured_value:

```json
{
  "metric": "maximum_size",
  "target_species": "weekly_designated",
  "tie_breaker": "earlier_catch"
}
```

### `fishing-encyclopedia-and-weekly-contest.current-cycle`

- seed_key: "fishing-encyclopedia-and-weekly-contest.current-cycle"
- kind: "other"
- requirement_level: "required"
- title: "현재 대회 주기"
- description: "최신 후속 패치 기준 월요일부터 토요일 기록으로 순위를 정하고 일요일부터 보상을 수령한다. 월요일 00:00~00:20은 집계·조회되지 않는다."
- structured_value:

```json
{
  "aggregation_unavailable": {
    "end": "00:20",
    "start": "00:00",
    "weekday": "Monday"
  },
  "inactive_day": "Sunday",
  "permanent_reward_table_seeded": false,
  "record_days": [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
  ],
  "reward_claim_starts": "Sunday"
}
```

## Steps

- None

## Schedules

### `fishing-encyclopedia-and-weekly-contest.record-window-start`

- seed_key: "fishing-encyclopedia-and-weekly-contest.record-window-start"
- rule_type: "content_schedule"
- recurrence_type: "weekly"
- weekday: 0
- time_local: "00:20"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "월요일 00:20 이후 새 기록 주기 진행; 월~토 기록"

### `fishing-encyclopedia-and-weekly-contest.record-settlement`

- seed_key: "fishing-encyclopedia-and-weekly-contest.record-settlement"
- rule_type: "record_settlement"
- recurrence_type: "weekly"
- weekday: 6
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "일요일부터 보상 수령 가능; 일요일은 대회 기록 진행 안 함"

### `fishing-encyclopedia-and-weekly-contest.reward-payout`

- seed_key: "fishing-encyclopedia-and-weekly-contest.reward-payout"
- rule_type: "reward_payout"
- recurrence_type: "weekly"
- weekday: 6
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "주간 낚시 대회 보상은 일요일부터 수령 가능"

## Rewards

- None

## Sections

- None

## Related Contents

### `fishing-encyclopedia-and-weekly-contest.system`

- seed_key: "fishing-encyclopedia-and-weekly-contest.system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "fishing-current-system"
- content_name_ko: "낚시 현재 시스템"
- content_category: "life"
- note: "낚시 기록 progression"
- order_no: 1
- relative_path: "../contents/fishing-current-system.md"
### `fishing-encyclopedia-and-weekly-contest.treasure`

- seed_key: "fishing-encyclopedia-and-weekly-contest.treasure"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "treasure-grade-fish"
- content_name_ko: "보물 등급 물고기"
- content_category: "life"
- note: "지정 어종에 보물 등급이 포함될 수 있음"
- order_no: 2
- relative_path: "../contents/treasure-grade-fish.md"
### `fishing-encyclopedia-and-weekly-contest.sailor`

- seed_key: "fishing-encyclopedia-and-weekly-contest.sailor"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "carrack-sailor-fishing"
- content_name_ko: "중범선 선원 낚시"
- content_category: "ocean_guide"
- note: "선원 낚시 기록도 도감·대회에 반영"
- order_no: 3
- relative_path: "../contents/carrack-sailor-fishing.md"
### `fishing-onboarding-strategy.weekly`

- seed_key: "fishing-onboarding-strategy.weekly"
- direction: "incoming"
- relation_type: "related"
- content_slug: "fishing-onboarding-strategy"
- content_name_ko: "낚시 입문 전략"
- content_category: "life"
- note: "주간 대회의 현재 대상과 조건은 해당 콘텐츠에서 확인한다."
- order_no: 5
- relative_path: "../contents/fishing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `fishing-encyclopedia-and-weekly-contest.summary::fish-encyclopedia-2025-04-16`

- evidence_seed_key: "fishing-encyclopedia-and-weekly-contest.summary::fish-encyclopedia-2025-04-16"
- source_id: "fish-encyclopedia-2025-04-16"
- title: "4월 16일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13826"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-04-16"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fishing-encyclopedia-and-weekly-contest"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "도감 기록과 최신 대회 주기"
- active: true
- is_active: true

### `fishing-encyclopedia-and-weekly-contest.summary::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "fishing-encyclopedia-and-weekly-contest.summary::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "fishing-encyclopedia-and-weekly-contest"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "도감 기록과 최신 대회 주기"
- active: true
- is_active: true

### `fishing-encyclopedia-and-weekly-contest.requirement.current-cycle::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "fishing-encyclopedia-and-weekly-contest.requirement.current-cycle::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fishing-encyclopedia-and-weekly-contest.current-cycle"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "월~토 기록·일요일 보상·월요일 집계 공백"
- active: true
- is_active: true

### `fishing-encyclopedia-and-weekly-contest.requirement.encyclopedia::fish-encyclopedia-2025-04-16`

- evidence_seed_key: "fishing-encyclopedia-and-weekly-contest.requirement.encyclopedia::fish-encyclopedia-2025-04-16"
- source_id: "fish-encyclopedia-2025-04-16"
- title: "4월 16일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13826"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-04-16"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fishing-encyclopedia-and-weekly-contest.encyclopedia"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "발견·최대 크기"
- active: true
- is_active: true

### `fishing-encyclopedia-and-weekly-contest.requirement.ranking::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "fishing-encyclopedia-and-weekly-contest.requirement.ranking::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fishing-encyclopedia-and-weekly-contest.ranking"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "최대 크기·동률 선착순"
- active: true
- is_active: true

### `fishing-encyclopedia-and-weekly-contest.schedule.record-settlement::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "fishing-encyclopedia-and-weekly-contest.schedule.record-settlement::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "fishing-encyclopedia-and-weekly-contest.record-settlement"
- claim_key: "schedule.record_settlement"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일요일 00:00 기록 종료·보상 가능"
- active: true
- is_active: true

### `fishing-encyclopedia-and-weekly-contest.schedule.record-window-start::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "fishing-encyclopedia-and-weekly-contest.schedule.record-window-start::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "fishing-encyclopedia-and-weekly-contest.record-window-start"
- claim_key: "schedule.content"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "월요일 00:20 기록 주기"
- active: true
- is_active: true

### `fishing-encyclopedia-and-weekly-contest.schedule.reward-payout::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "fishing-encyclopedia-and-weekly-contest.schedule.reward-payout::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "fishing-encyclopedia-and-weekly-contest.reward-payout"
- claim_key: "schedule.reward_payout"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일요일부터 보상 수령"
- active: true
- is_active: true

### Historical / inactive evidence

- None
