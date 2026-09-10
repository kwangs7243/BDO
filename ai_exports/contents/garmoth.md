<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 가모스

## Identity

- slug: "garmoth"
- name_ko: "가모스"
- category: "world_boss"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "정해진 월드 우두머리 시간표에 출현하며, 처치 시 지역 의뢰가 자동 진행되어 가문당 주 3회까지 보상을 받는다."
- purpose: "가모스 출현 시간에 맞춰 토벌하고 주간 최대 3회의 자동 지역 의뢰 보상을 받는다."

## Requirements

### `garmoth.weekly-reward-cap`

- seed_key: "garmoth.weekly-reward-cap"
- kind: "other"
- requirement_level: "required"
- title: "주간 보상 한도"
- description: "가모스 처치 시 지역 의뢰가 자동 진행되며 가문당 주간 최대 3회 보상을 획득한다."
- structured_value:

```json
{
  "quest_activation": "automatic_on_kill",
  "weekly_reward_cap": 3
}
```

## Steps

- None

## Schedules

### `garmoth.attempt-reset`

- seed_key: "garmoth.attempt-reset"
- rule_type: "attempt_reset"
- recurrence_type: "weekly"
- weekday: 3
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "주 3회 보상 횟수 초기화: 목요일 00:00 KST"

### `garmoth.world-boss-spawn`

- seed_key: "garmoth.world-boss-spawn"
- rule_type: "spawn"
- recurrence_type: "scheduled"
- weekday: null
- time_local: null
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "공식 월드 우두머리 시간표에 따른 출현; 주간 보상 한도와 별도"

## Rewards

### `garmoth.weekly-kill-reward`

- seed_key: "garmoth.weekly-kill-reward"
- name: "가모스 토벌 지역 의뢰 보상"
- reward_type: "weekly_reward"
- amount: null
- min_amount: null
- max_amount: 3.0
- unit: "회/주"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "월드 우두머리 출현 횟수와 별도의 보상 한도"
- order_no: 1

## Sections

- None

## Related Contents

### `world-boss-current-system.garmoth-existing`

- seed_key: "world-boss-current-system.garmoth-existing"
- direction: "incoming"
- relation_type: "related"
- content_slug: "world-boss-current-system"
- content_name_ko: "월드 우두머리 현재 시스템"
- content_category: "combat_pve"
- note: "기존 가모스 주간 루틴을 재사용한다."
- order_no: 3
- relative_path: "../contents/world-boss-current-system.md"
### `world-boss-current-roster.entity-garmoth`

- seed_key: "world-boss-current-roster.entity-garmoth"
- direction: "incoming"
- relation_type: "related"
- content_slug: "world-boss-current-roster"
- content_name_ko: "월드 우두머리 현재 명단"
- content_category: "combat_pve"
- note: "Garmoth 현재 명단 엔터티"
- order_no: 8
- relative_path: "../contents/world-boss-current-roster.md"

## Evidence and Sources

### Current evidence

### `garmoth.summary::world-boss-guide`

- evidence_seed_key: "garmoth.summary::world-boss-guide"
- source_id: "world-boss-guide"
- title: "월드 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=89"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "garmoth"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-02"
- evidence_note: "자동 지역 의뢰와 주 3회 보상"
- active: true
- is_active: true

### `garmoth.requirement.weekly-cap::garmoth-reward-2024-05-29`

- evidence_seed_key: "garmoth.requirement.weekly-cap::garmoth-reward-2024-05-29"
- source_id: "garmoth-reward-2024-05-29"
- title: "5월 29일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12254"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-05-29"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "garmoth.weekly-reward-cap"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 보상 최대 3회 및 자동 진행"
- active: true
- is_active: true

### `garmoth.requirement.weekly-cap::world-boss-guide`

- evidence_seed_key: "garmoth.requirement.weekly-cap::world-boss-guide"
- source_id: "world-boss-guide"
- title: "월드 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=89"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "garmoth.weekly-reward-cap"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 보상 최대 3회 및 자동 진행"
- active: true
- is_active: true

### `garmoth.reward.weekly-kill::garmoth-reward-2024-05-29`

- evidence_seed_key: "garmoth.reward.weekly-kill::garmoth-reward-2024-05-29"
- source_id: "garmoth-reward-2024-05-29"
- title: "5월 29일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12254"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-05-29"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "garmoth.weekly-kill-reward"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "가문당 주 3회 보상"
- active: true
- is_active: true

### `garmoth.schedule.attempt-reset::garmoth-reward-2024-05-29`

- evidence_seed_key: "garmoth.schedule.attempt-reset::garmoth-reward-2024-05-29"
- source_id: "garmoth-reward-2024-05-29"
- title: "5월 29일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12254"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-05-29"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "garmoth.attempt-reset"
- claim_key: "schedule.attempt_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "목요일 00:00 보상 횟수 초기화"
- active: true
- is_active: true

### `garmoth.schedule.attempt-reset::world-boss-guide`

- evidence_seed_key: "garmoth.schedule.attempt-reset::world-boss-guide"
- source_id: "world-boss-guide"
- title: "월드 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=89"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "garmoth.attempt-reset"
- claim_key: "schedule.attempt_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "목요일 00:00 보상 횟수 초기화"
- active: true
- is_active: true

### `garmoth.schedule.spawn::world-boss-guide`

- evidence_seed_key: "garmoth.schedule.spawn::world-boss-guide"
- source_id: "world-boss-guide"
- title: "월드 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=89"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "garmoth.world-boss-spawn"
- claim_key: "schedule.spawn"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "공식 시간표 출현과 주간 보상 한도 분리"
- active: true
- is_active: true

### Historical / inactive evidence

- None
