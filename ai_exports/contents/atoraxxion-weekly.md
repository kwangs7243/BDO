<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 아토락시온 주간 토벌

## Identity

- slug: "atoraxxion-weekly"
- name_ko: "아토락시온 주간 토벌"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: "party"
- difficulty: null

## Overview

- summary: "통합된 일반 서버 난이도에서 바아·시카·요루·오르 4개 지역의 주간 보상을 각각 1회 진행한다."
- purpose: "네 지역의 주간 우두머리 보상과 전체 완료 보상을 획득한다."

## Requirements

### `atoraxxion-weekly.reward-rule`

- seed_key: "atoraxxion-weekly.reward-rule"
- kind: "other"
- requirement_level: "required"
- title: "현재 주간 보상 구조"
- description: "일반/시즌 보상 주기가 통합되었고 각 지역 주간 토벌 보상은 1회다. 새벽의 열쇠는 현재 보상 요구 조건이 아니다."
- structured_value:

```json
{
  "dawn_key_required": false,
  "separate_season_branch": false,
  "weekly_reward_per_region": 1
}
```

## Steps

### `atoraxxion-weekly.region-1`

- seed_key: "atoraxxion-weekly.region-1"
- phase: "repeat"
- order_no: 1
- title: "바아마키아"
- description: "바아마키아 주간 우두머리 보상을 진행한다."
- checkable: true

### `atoraxxion-weekly.region-2`

- seed_key: "atoraxxion-weekly.region-2"
- phase: "repeat"
- order_no: 2
- title: "시카라키아"
- description: "시카라키아 주간 우두머리 보상을 진행한다."
- checkable: true

### `atoraxxion-weekly.region-3`

- seed_key: "atoraxxion-weekly.region-3"
- phase: "repeat"
- order_no: 3
- title: "요루나키아"
- description: "요루나키아 주간 우두머리 보상을 진행한다."
- checkable: true

### `atoraxxion-weekly.region-4`

- seed_key: "atoraxxion-weekly.region-4"
- phase: "repeat"
- order_no: 4
- title: "오르제키아"
- description: "오르제키아 주간 우두머리 보상을 진행한다."
- checkable: true

## Schedules

### `atoraxxion-weekly.quest-reset`

- seed_key: "atoraxxion-weekly.quest-reset"
- rule_type: "quest_reset"
- recurrence_type: "weekly"
- weekday: 3
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "일반 주간 의뢰 공통 기준: 목요일 00:00"

## Rewards

### `atoraxxion-weekly.all-regions-cron`

- seed_key: "atoraxxion-weekly.all-regions-cron"
- name: "크론석"
- reward_type: "weekly_reward"
- amount: 500.0
- min_amount: null
- max_amount: null
- unit: "개/주"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "공식 성장 안내 기준 4종 우두머리 모두 완료 시 총량"
- order_no: 1

## Sections

### `atoraxxion-weekly.current-structure`

- seed_key: "atoraxxion-weekly.current-structure"
- section_type: "overview"
- title: "현재 통합 구조"
- order_no: 1

#### body_markdown

일반/시즌 난이도별 보상 주기와 새벽의 열쇠 요구 구조는 폐지됐다. 네 지역은 한 routine에서 각각 관리한다.

## Related Contents

### `last-gladiius-weekly.atoraxxion-weekly`

- seed_key: "last-gladiius-weekly.atoraxxion-weekly"
- direction: "incoming"
- relation_type: "related"
- content_slug: "last-gladiius-weekly"
- content_name_ko: "최후의 글라디우스 주간 토벌"
- content_category: "combat_pve"
- note: "현재 네 아토락시온 지역의 통합 주간 토벌 Content"
- order_no: 1
- relative_path: "../contents/last-gladiius-weekly.md"

## Evidence and Sources

### Current evidence

### `atoraxxion-weekly.summary::atoraxxion-unification-2025-12-17`

- evidence_seed_key: "atoraxxion-weekly.summary::atoraxxion-unification-2025-12-17"
- source_id: "atoraxxion-unification-2025-12-17"
- title: "12월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14944"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "atoraxxion-weekly"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "통합 난이도 및 지역별 주간 1회"
- active: true
- is_active: true

### `atoraxxion-weekly.requirement.reward-rule::atoraxxion-unification-2025-12-17`

- evidence_seed_key: "atoraxxion-weekly.requirement.reward-rule::atoraxxion-unification-2025-12-17"
- source_id: "atoraxxion-unification-2025-12-17"
- title: "12월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14944"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "atoraxxion-weekly.reward-rule"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "시즌 분기·새벽의 열쇠 폐지와 주간 1회"
- active: true
- is_active: true

### `atoraxxion-weekly.step.region-1::atoraxxion-unification-2025-12-17`

- evidence_seed_key: "atoraxxion-weekly.step.region-1::atoraxxion-unification-2025-12-17"
- source_id: "atoraxxion-unification-2025-12-17"
- title: "12월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14944"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "atoraxxion-weekly.region-1"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "바아마키아 주간 지역"
- active: true
- is_active: true

### `atoraxxion-weekly.step.region-2::atoraxxion-unification-2025-12-17`

- evidence_seed_key: "atoraxxion-weekly.step.region-2::atoraxxion-unification-2025-12-17"
- source_id: "atoraxxion-unification-2025-12-17"
- title: "12월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14944"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "atoraxxion-weekly.region-2"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "시카라키아 주간 지역"
- active: true
- is_active: true

### `atoraxxion-weekly.step.region-3::atoraxxion-unification-2025-12-17`

- evidence_seed_key: "atoraxxion-weekly.step.region-3::atoraxxion-unification-2025-12-17"
- source_id: "atoraxxion-unification-2025-12-17"
- title: "12월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14944"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "atoraxxion-weekly.region-3"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "요루나키아 주간 지역"
- active: true
- is_active: true

### `atoraxxion-weekly.step.region-4::atoraxxion-unification-2025-12-17`

- evidence_seed_key: "atoraxxion-weekly.step.region-4::atoraxxion-unification-2025-12-17"
- source_id: "atoraxxion-unification-2025-12-17"
- title: "12월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14944"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "atoraxxion-weekly.region-4"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "오르제키아 주간 지역"
- active: true
- is_active: true

### `atoraxxion-weekly.reward.all-regions-cron::routine-special-lineup-2026-01-08`

- evidence_seed_key: "atoraxxion-weekly.reward.all-regions-cron::routine-special-lineup-2026-01-08"
- source_id: "routine-special-lineup-2026-01-08"
- title: "풍성한 보상을 한 눈에, 검은사막 스페셜 라인업"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15057"
- publisher: "Pearl Abyss"
- source_type: "official_gm"
- published_at: "2026-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "atoraxxion-weekly.all-regions-cron"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "4종 완료 시 크론석 총 500개"
- active: true
- is_active: true

### `atoraxxion-weekly.schedule.quest-reset::ator-reset-patch`

- evidence_seed_key: "atoraxxion-weekly.schedule.quest-reset::ator-reset-patch"
- source_id: "ator-reset-patch"
- title: "2월 16일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=7543"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "atoraxxion-weekly.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "목요일 00:00 주간 의뢰 초기화"
- active: true
- is_active: true

### `atoraxxion-weekly.schedule.quest-reset::weekly-reset-2021`

- evidence_seed_key: "atoraxxion-weekly.schedule.quest-reset::weekly-reset-2021"
- source_id: "weekly-reset-2021"
- title: "7월 28일 (수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=6125"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "atoraxxion-weekly.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "목요일 00:00 주간 의뢰 초기화"
- active: true
- is_active: true

### Historical / inactive evidence

- None
