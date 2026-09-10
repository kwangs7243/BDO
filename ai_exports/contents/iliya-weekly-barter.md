<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# [물물교환][주간] 교역의 중심 일리야 섬

## Identity

- slug: "iliya-weekly-barter"
- name_ko: "[물물교환][주간] 교역의 중심 일리야 섬"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "물물교환 100회를 진행해 까마귀 주화 200과 수수께끼 물물교환 지원품 상자 3개를 받는 일리야 주간 의뢰."
- purpose: "물물교환을 진행하면서 주간 보상과 까마귀 주화를 추가 확보한다."

## Requirements

### `iliya-weekly-barter.requirement.start-npc`

- seed_key: "iliya-weekly-barter.requirement.start-npc"
- kind: "other"
- requirement_level: "required"
- title: "수주 NPC"
- description: "일리야 섬 물물교환원 프리코"
- structured_value: null

## Steps

### `iliya-weekly-barter.step.complete-objective`

- seed_key: "iliya-weekly-barter.step.complete-objective"
- phase: "repeat"
- order_no: 1
- title: "의뢰 목표 완료"
- description: "물물교환 100회 진행"
- checkable: false

## Schedules

### `iliya-weekly-barter.schedule.quest-reset`

- seed_key: "iliya-weekly-barter.schedule.quest-reset"
- rule_type: "quest_reset"
- recurrence_type: "weekly"
- weekday: 3
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "주간 의뢰: 매주 목요일 00:00 KST 초기화"

## Rewards

### `iliya-weekly-barter.reward.crow-coins`

- seed_key: "iliya-weekly-barter.reward.crow-coins"
- name: "까마귀 주화"
- reward_type: "quest_reward"
- amount: 200.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 1

### `iliya-weekly-barter.reward.mystery-support-box`

- seed_key: "iliya-weekly-barter.reward.mystery-support-box"
- name: "수수께끼 물물교환 지원품 상자"
- reward_type: "quest_reward"
- amount: 3.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 2

## Sections

- None

## Related Contents

### `iliya-weekly-barter.relation.carrack-advance`

- seed_key: "iliya-weekly-barter.relation.carrack-advance"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "carrack-advance"
- content_name_ko: "에페리아 중범선 : 점진"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/carrack-advance.md"
### `barter-onboarding-strategy.weekly`

- seed_key: "barter-onboarding-strategy.weekly"
- direction: "incoming"
- relation_type: "related"
- content_slug: "barter-onboarding-strategy"
- content_name_ko: "물물교환 입문 운영 전략"
- content_category: "ocean_barter"
- note: "주간 물물교환 목표"
- order_no: 10
- relative_path: "../contents/barter-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `iliya-weekly-barter.evidence.purpose::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "iliya-weekly-barter.evidence.purpose::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "iliya-weekly-barter"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "물물교환을 진행하면서 주간 보상과 까마귀 주화를 추가 확보한다."
- active: true
- is_active: true

### `iliya-weekly-barter.evidence.summary::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "iliya-weekly-barter.evidence.summary::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "iliya-weekly-barter"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "물물교환 100회를 진행해 까마귀 주화 200과 수수께끼 물물교환 지원품 상자 3개를 받는 일리야 주간 의뢰."
- active: true
- is_active: true

### `iliya-weekly-barter.evidence.relation.carrack-advance::carrack-guide`

- evidence_seed_key: "iliya-weekly-barter.evidence.relation.carrack-advance::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "iliya-weekly-barter.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `iliya-weekly-barter.evidence.relation.carrack-advance::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "iliya-weekly-barter.evidence.relation.carrack-advance::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "iliya-weekly-barter.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `iliya-weekly-barter.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "iliya-weekly-barter.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "iliya-weekly-barter.requirement.start-npc"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "수주 NPC: 일리야 섬 물물교환원 프리코"
- active: true
- is_active: true

### `iliya-weekly-barter.evidence.step.objective::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "iliya-weekly-barter.evidence.step.objective::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "iliya-weekly-barter.step.complete-objective"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "물물교환 100회 진행"
- active: true
- is_active: true

### `iliya-weekly-barter.evidence.reward.crow-coins::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "iliya-weekly-barter.evidence.reward.crow-coins::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "iliya-weekly-barter.reward.crow-coins"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 까마귀 주화"
- active: true
- is_active: true

### `iliya-weekly-barter.evidence.reward.mystery-support-box::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "iliya-weekly-barter.evidence.reward.mystery-support-box::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "iliya-weekly-barter.reward.mystery-support-box"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 수수께끼 물물교환 지원품 상자"
- active: true
- is_active: true

### `iliya-weekly-barter.evidence.schedule.reset::daily-weekly-reset-gm-2023`

- evidence_seed_key: "iliya-weekly-barter.evidence.schedule.reset::daily-weekly-reset-gm-2023"
- source_id: "daily-weekly-reset-gm-2023"
- title: "검은사막이 처음인 모험가 여러분을 위해 준비한 A to Z!"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=10577"
- publisher: "Pearl Abyss"
- source_type: "official_gm"
- published_at: "2023-07-25"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "iliya-weekly-barter.schedule.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 의뢰: 매주 목요일 00:00 KST 초기화"
- active: true
- is_active: true

### Historical / inactive evidence

- None
