<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# [주간] 오킬루아에서 지내고 싶다고?

## Identity

- slug: "oquilla-weekly-swordfish"
- name_ko: "[주간] 오킬루아에서 지내고 싶다고?"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "황새치 1마리를 건네 오킬루아 기념 주화 10개를 받는 주간 의뢰."
- purpose: "오킬루아 기념 주화를 추가 확보하는 선택형 주간 루틴."

## Requirements

### `oquilla-weekly-swordfish.requirement.start-npc`

- seed_key: "oquilla-weekly-swordfish.requirement.start-npc"
- kind: "other"
- requirement_level: "required"
- title: "수주 NPC"
- description: "오킬루아의 눈 무역관리 카리오"
- structured_value: null

## Steps

### `oquilla-weekly-swordfish.step.complete-objective`

- seed_key: "oquilla-weekly-swordfish.step.complete-objective"
- phase: "repeat"
- order_no: 1
- title: "의뢰 목표 완료"
- description: "황새치 1마리 건네기"
- checkable: false

## Schedules

### `oquilla-weekly-swordfish.schedule.quest-reset`

- seed_key: "oquilla-weekly-swordfish.schedule.quest-reset"
- rule_type: "quest_reset"
- recurrence_type: "weekly"
- weekday: 3
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "주간 의뢰: 매주 목요일 00:00 KST 초기화"

## Rewards

### `oquilla-weekly-swordfish.reward.oquilla-coin`

- seed_key: "oquilla-weekly-swordfish.reward.oquilla-coin"
- name: "오킬루아 기념 주화"
- reward_type: "quest_reward"
- amount: 10.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 1

## Sections

- None

## Related Contents

- None

## Evidence and Sources

### Current evidence

### `oquilla-weekly-swordfish.evidence.purpose::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-swordfish.evidence.purpose::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "oquilla-weekly-swordfish"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "오킬루아 기념 주화를 추가 확보하는 선택형 주간 루틴."
- active: true
- is_active: true

### `oquilla-weekly-swordfish.evidence.summary::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-swordfish.evidence.summary::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "oquilla-weekly-swordfish"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "황새치 1마리를 건네 오킬루아 기념 주화 10개를 받는 주간 의뢰."
- active: true
- is_active: true

### `oquilla-weekly-swordfish.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-swordfish.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "oquilla-weekly-swordfish.requirement.start-npc"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "수주 NPC: 오킬루아의 눈 무역관리 카리오"
- active: true
- is_active: true

### `oquilla-weekly-swordfish.evidence.step.objective::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-swordfish.evidence.step.objective::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "oquilla-weekly-swordfish.step.complete-objective"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "황새치 1마리 건네기"
- active: true
- is_active: true

### `oquilla-weekly-swordfish.evidence.reward.oquilla-coin::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-swordfish.evidence.reward.oquilla-coin::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-weekly-swordfish.reward.oquilla-coin"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 오킬루아 기념 주화"
- active: true
- is_active: true

### `oquilla-weekly-swordfish.evidence.schedule.reset::daily-weekly-reset-gm-2023`

- evidence_seed_key: "oquilla-weekly-swordfish.evidence.schedule.reset::daily-weekly-reset-gm-2023"
- source_id: "daily-weekly-reset-gm-2023"
- title: "검은사막이 처음인 모험가 여러분을 위해 준비한 A to Z!"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=10577"
- publisher: "Pearl Abyss"
- source_type: "official_gm"
- published_at: "2023-07-25"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "oquilla-weekly-swordfish.schedule.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 의뢰: 매주 목요일 00:00 KST 초기화"
- active: true
- is_active: true

### Historical / inactive evidence

- None
