<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 레크라샨 해왕류 의뢰

## Identity

- slug: "lekrashan-hunting"
- name_ko: "레크라샨 해왕류 의뢰"
- category: "ocean_guide"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "오킬루아의 눈 해란에게 레크라샨 사냥터 일일·주간 해왕류 의뢰를 수주한다."
- purpose: "현재 목표 수량과 과거 목표를 분리하고 보상 선택지를 확인한다."

## Requirements

### `lekrashan-hunting.npc-location`

- seed_key: "lekrashan-hunting.npc-location"
- kind: "other"
- requirement_level: "required"
- title: "수주 NPC와 사냥터"
- description: "오킬루아의 눈 <랏 사절단> 해란에게 수주하며 대형 해왕류 군락지 레크라샨 사냥터에서 진행한다."
- structured_value:

```json
{
  "hunting_ground": "대형 해왕류 군락지 - 레크라샨",
  "npc": "해란",
  "npc_location": "오킬루아의 눈"
}
```

### `lekrashan-hunting.daily-target`

- seed_key: "lekrashan-hunting.daily-target"
- kind: "other"
- requirement_level: "required"
- title: "일일 현재 목표"
- description: "[일일] 바닷길을 막고있는 괴수들은 검은 파도를 쫓는 검은무쇠이빨 5마리와 나인샤크 5마리를 처치한다."
- structured_value:

```json
{
  "black_rust": 5,
  "nineshark": 5
}
```

### `lekrashan-hunting.weekly-target`

- seed_key: "lekrashan-hunting.weekly-target"
- kind: "other"
- requirement_level: "required"
- title: "주간 목표"
- description: "[주간] 무자비한 괴수 무리는 검은 파도를 쫓는 검은무쇠이빨 10마리와 나인샤크 10마리를 처치한다."
- structured_value:

```json
{
  "black_rust": 10,
  "nineshark": 10
}
```

## Steps

- None

## Schedules

### `lekrashan-hunting.daily-reset`

- seed_key: "lekrashan-hunting.daily-reset"
- rule_type: "quest_reset"
- recurrence_type: "daily"
- weekday: null
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "일일 의뢰 재수주 초기화"

### `lekrashan-hunting.weekly-reset`

- seed_key: "lekrashan-hunting.weekly-reset"
- rule_type: "quest_reset"
- recurrence_type: "weekly"
- weekday: 3
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "일반 주간 의뢰 목요일 00:00 KST 초기화"

## Rewards

### `lekrashan-hunting.reward.daily-crow`

- seed_key: "lekrashan-hunting.reward.daily-crow"
- name: "까마귀 주화"
- reward_type: "currency"
- amount: 200.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 1

### `lekrashan-hunting.reward.daily-green`

- seed_key: "lekrashan-hunting.reward.daily-green"
- name: "오킬루아 녹빛 담수"
- reward_type: "material"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "lekrashan-hunting.daily-choice"
- recommendation: null
- notes: null
- order_no: 2

### `lekrashan-hunting.reward.daily-blue`

- seed_key: "lekrashan-hunting.reward.daily-blue"
- name: "오킬루아 물빛 담수"
- reward_type: "material"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "lekrashan-hunting.daily-choice"
- recommendation: null
- notes: null
- order_no: 3

### `lekrashan-hunting.reward.daily-gold`

- seed_key: "lekrashan-hunting.reward.daily-gold"
- name: "오킬루아 금빛 담수"
- reward_type: "material"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "lekrashan-hunting.daily-choice"
- recommendation: null
- notes: null
- order_no: 4

### `lekrashan-hunting.reward.weekly-contribution`

- seed_key: "lekrashan-hunting.reward.weekly-contribution"
- name: "공헌도 경험치"
- reward_type: "experience"
- amount: 500.0
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 5

### `lekrashan-hunting.reward.weekly-sailing`

- seed_key: "lekrashan-hunting.reward.weekly-sailing"
- name: "항해 경험치"
- reward_type: "experience"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 6

### `lekrashan-hunting.reward.weekly-crow`

- seed_key: "lekrashan-hunting.reward.weekly-crow"
- name: "까마귀 주화"
- reward_type: "currency"
- amount: 500.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 7

### `lekrashan-hunting.reward.weekly-green`

- seed_key: "lekrashan-hunting.reward.weekly-green"
- name: "오킬루아 녹빛 담수"
- reward_type: "material"
- amount: 3.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "lekrashan-hunting.weekly-choice"
- recommendation: null
- notes: null
- order_no: 8

### `lekrashan-hunting.reward.weekly-blue`

- seed_key: "lekrashan-hunting.reward.weekly-blue"
- name: "오킬루아 물빛 담수"
- reward_type: "material"
- amount: 3.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "lekrashan-hunting.weekly-choice"
- recommendation: null
- notes: null
- order_no: 9

### `lekrashan-hunting.reward.weekly-gold`

- seed_key: "lekrashan-hunting.reward.weekly-gold"
- name: "오킬루아 금빛 담수"
- reward_type: "material"
- amount: 3.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "lekrashan-hunting.weekly-choice"
- recommendation: null
- notes: null
- order_no: 10

## Sections

- None

## Related Contents

### `lekrashan-hunting.relation.weekly-framework`

- seed_key: "lekrashan-hunting.relation.weekly-framework"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "weekly-quest-framework"
- content_name_ko: "주간 의뢰 공통 규칙"
- content_category: "system"
- note: "일반 주간 목요일 초기화 규칙"
- order_no: 1
- relative_path: "../contents/weekly-quest-framework.md"
### `lekrashan-hunting.relation.sea-crystals`

- seed_key: "lekrashan-hunting.relation.sea-crystals"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sea-crystals"
- content_name_ko: "해원석 progression"
- content_category: "ocean_project"
- note: "담수 선택 보상 사용처"
- order_no: 2
- relative_path: "../contents/sea-crystals.md"

## Evidence and Sources

### Current evidence

### `lekrashan-hunting.evidence.daily-rewards::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "lekrashan-hunting.evidence.daily-rewards::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "lekrashan-hunting"
- claim_key: "daily_rewards"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일일 까마귀 주화 200개와 담수 1개 선택"
- active: true
- is_active: true

### `lekrashan-hunting.evidence.weekly-rewards::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "lekrashan-hunting.evidence.weekly-rewards::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "lekrashan-hunting"
- claim_key: "weekly_rewards"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 공헌도 500·항해 경험치·까마귀 주화 500개·담수 3개 선택"
- active: true
- is_active: true

### `lekrashan-hunting.evidence.daily-target::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "lekrashan-hunting.evidence.daily-target::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "lekrashan-hunting.daily-target"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "현재 일일 5+5 목표"
- active: true
- is_active: true

### `lekrashan-hunting.evidence.npc-location::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "lekrashan-hunting.evidence.npc-location::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "lekrashan-hunting.npc-location"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "해란 수주와 레크라샨 사냥터"
- active: true
- is_active: true

### `lekrashan-hunting.evidence.weekly-target::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "lekrashan-hunting.evidence.weekly-target::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "lekrashan-hunting.weekly-target"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 10+10 목표"
- active: true
- is_active: true

### Historical / inactive evidence

### `lekrashan-hunting.evidence.daily-target-old::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "lekrashan-hunting.evidence.daily-target-old::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "lekrashan-hunting.daily-target-old"
- claim_key: "structured_value"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "과거 일일 20+20 목표"
- active: false
- is_active: false
