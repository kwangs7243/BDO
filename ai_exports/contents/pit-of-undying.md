<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 불멸의 나락

## Identity

- slug: "pit-of-undying"
- name_ko: "불멸의 나락"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "주간 결투 콘텐츠. 최신 공식 성장 이정표에서 최고 단계 기준 크론석 최대 500개 획득 경로로 안내된다."
- purpose: "주간 결투를 완료하고 최고 단계 기준 보상을 획득한다."

## Requirements

### `pit-of-undying.unlock-quest`

- seed_key: "pit-of-undying.unlock-quest"
- kind: "quest"
- requirement_level: "required"
- title: "선행 의뢰"
- description: "흑정령 추천 의뢰 [까마귀의 둥지] 까마귀의 용병을 완료한다."
- structured_value: null

### `pit-of-undying.weekly-rule`

- seed_key: "pit-of-undying.weekly-rule"
- kind: "other"
- requirement_level: "required"
- title: "주간 구조"
- description: "가문 단위 주간 콘텐츠이며 세부 등급별 토큰 보상표는 이번 seed에서 확정하지 않는다."
- structured_value:

```json
{
  "routine_scope": "weekly"
}
```

## Steps

### `pit-of-undying.enter`

- seed_key: "pit-of-undying.enter"
- phase: "repeat"
- order_no: 1
- title: "불멸의 나락 입장"
- description: "ESC → 전쟁 → 불멸의 나락에서 이번 주 결투를 진행한다."
- checkable: true

## Schedules

### `pit-of-undying.quest-reset`

- seed_key: "pit-of-undying.quest-reset"
- rule_type: "quest_reset"
- recurrence_type: "weekly"
- weekday: 3
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "주간 의뢰 공통 기준: 목요일 00:00 KST"

## Rewards

### `pit-of-undying.cron-max`

- seed_key: "pit-of-undying.cron-max"
- name: "크론석"
- reward_type: "weekly_reward"
- amount: null
- min_amount: null
- max_amount: 500.0
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "최고 단계 기준 최대 수량; 등급별 세부 표는 미입력"
- order_no: 1

## Sections

- None

## Related Contents

### `emma-bartali-record-log.pit`

- seed_key: "emma-bartali-record-log.pit"
- direction: "incoming"
- relation_type: "related"
- content_slug: "emma-bartali-record-log"
- content_name_ko: "엠마 바탈리의 기록일지"
- content_category: "progression"
- note: "3장 조건에 불멸의 까마귀 휘장 승급 의뢰가 포함됨"
- order_no: 3
- relative_path: "../contents/emma-bartali-record-log.md"

## Evidence and Sources

### Current evidence

### `pit-of-undying.summary::growth-milestone-2026-08-26`

- evidence_seed_key: "pit-of-undying.summary::growth-milestone-2026-08-26"
- source_id: "growth-milestone-2026-08-26"
- title: "하이퍼부스트와 함께, 차근차근 장비 성장 이정표"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15761"
- publisher: "Pearl Abyss"
- source_type: "official_gm"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "pit-of-undying"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 콘텐츠 및 크론석 최대 500개"
- active: true
- is_active: true

### `pit-of-undying.summary::pit-weekly-2025`

- evidence_seed_key: "pit-of-undying.summary::pit-weekly-2025"
- source_id: "pit-weekly-2025"
- title: "7월 23일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "pit-of-undying"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 콘텐츠 및 크론석 최대 500개"
- active: true
- is_active: true

### `pit-of-undying.requirement.unlock::pit-weekly-2025`

- evidence_seed_key: "pit-of-undying.requirement.unlock::pit-weekly-2025"
- source_id: "pit-weekly-2025"
- title: "7월 23일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "pit-of-undying.unlock-quest"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "선행 의뢰와 접근 경로"
- active: true
- is_active: true

### `pit-of-undying.requirement.weekly::pit-weekly-2025`

- evidence_seed_key: "pit-of-undying.requirement.weekly::pit-weekly-2025"
- source_id: "pit-weekly-2025"
- title: "7월 23일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "pit-of-undying.weekly-rule"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 반복 구조"
- active: true
- is_active: true

### `pit-of-undying.reward.cron-max::growth-milestone-2026-08-26`

- evidence_seed_key: "pit-of-undying.reward.cron-max::growth-milestone-2026-08-26"
- source_id: "growth-milestone-2026-08-26"
- title: "하이퍼부스트와 함께, 차근차근 장비 성장 이정표"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15761"
- publisher: "Pearl Abyss"
- source_type: "official_gm"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "pit-of-undying.cron-max"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "최고 단계 기준 크론석 최대 500개"
- active: true
- is_active: true

### `pit-of-undying.schedule.quest-reset::pit-weekly-2025`

- evidence_seed_key: "pit-of-undying.schedule.quest-reset::pit-weekly-2025"
- source_id: "pit-weekly-2025"
- title: "7월 23일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "pit-of-undying.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 의뢰 공통 목요일 00:00"
- active: true
- is_active: true

### `pit-of-undying.schedule.quest-reset::weekly-reset-2021`

- evidence_seed_key: "pit-of-undying.schedule.quest-reset::weekly-reset-2021"
- source_id: "weekly-reset-2021"
- title: "7월 28일 (수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=6125"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "pit-of-undying.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 의뢰 공통 목요일 00:00"
- active: true
- is_active: true

### Historical / inactive evidence

- None
