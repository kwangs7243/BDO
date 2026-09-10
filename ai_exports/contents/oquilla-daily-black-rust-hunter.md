<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# [일일] 그믐달 길드의 검은무쇠이빨 사냥꾼

## Identity

- slug: "oquilla-daily-black-rust-hunter"
- name_ko: "[일일] 그믐달 길드의 검은무쇠이빨 사냥꾼"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "검은무쇠이빨 1마리 처치 후 까마귀 주화와 선박 장비 관련 선택 보상을 받는 성체 해왕류 일일 의뢰."
- purpose: "중범선 이후 선박 장비 재료 또는 강화 재료를 확보하는 대안 일일 의뢰."

## Requirements

### `oquilla-daily-black-rust-hunter.requirement.start-npc`

- seed_key: "oquilla-daily-black-rust-hunter.requirement.start-npc"
- kind: "other"
- requirement_level: "required"
- title: "수주 NPC"
- description: "오킬루아의 눈 라비켈"
- structured_value: null

## Steps

### `oquilla-daily-black-rust-hunter.step.complete-objective`

- seed_key: "oquilla-daily-black-rust-hunter.step.complete-objective"
- phase: "repeat"
- order_no: 1
- title: "의뢰 목표 완료"
- description: "검은무쇠이빨 1마리 처치"
- checkable: false

## Schedules

### `oquilla-daily-black-rust-hunter.schedule.quest-reset`

- seed_key: "oquilla-daily-black-rust-hunter.schedule.quest-reset"
- rule_type: "quest_reset"
- recurrence_type: "daily"
- weekday: null
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "일일 의뢰: 매일 00:00 KST 초기화"

## Rewards

### `oquilla-daily-black-rust-hunter.reward.oquilla-coin`

- seed_key: "oquilla-daily-black-rust-hunter.reward.oquilla-coin"
- name: "오킬루아 기념 주화"
- reward_type: "quest_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 1

### `oquilla-daily-black-rust-hunter.reward.crow-coins`

- seed_key: "oquilla-daily-black-rust-hunter.reward.crow-coins"
- name: "까마귀 주화"
- reward_type: "quest_reward"
- amount: 100.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 2

### `oquilla-daily-black-rust-hunter.reward.wave-black-stone`

- seed_key: "oquilla-daily-black-rust-hunter.reward.wave-black-stone"
- name: "파도의 블랙스톤"
- reward_type: "quest_reward"
- amount: 14.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "oquilla-daily-black-rust-hunter.choice-1"
- recommendation: null
- notes: null
- order_no: 3

### `oquilla-daily-black-rust-hunter.reward.post-carrack-material`

- seed_key: "oquilla-daily-black-rust-hunter.reward.post-carrack-material"
- name: "파도의 흔적이 담긴 접착제"
- reward_type: "quest_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "oquilla-daily-black-rust-hunter.choice-1"
- recommendation: null
- notes: null
- order_no: 4

### `oquilla-daily-black-rust-hunter.reward.contribution-exp`

- seed_key: "oquilla-daily-black-rust-hunter.reward.contribution-exp"
- name: "공헌도 경험치"
- reward_type: "experience"
- amount: 300.0
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 5

### `oquilla-daily-black-rust-hunter.reward.sailing-exp`

- seed_key: "oquilla-daily-black-rust-hunter.reward.sailing-exp"
- name: "항해 경험치"
- reward_type: "experience"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "2025-02-05 이후 기존 대비 1.5배"
- order_no: 6

## Sections

### `oquilla-daily-black-rust-hunter.section.mutual-exclusion`

- seed_key: "oquilla-daily-black-rust-hunter.section.mutual-exclusion"
- section_type: "common_mistakes"
- title: "어린 해왕류 일일과 상호 배타"
- order_no: 1

#### body_markdown

`[일일] 그믐달 어린 해왕류 사냥꾼`을 수주 또는 완료했다면 성체 일일 3종을 수주할 수 없다. 점진 본체·파란 장비 재료가 목표라면 두 계열의 보상을 비교하고 선택한다.

## Related Contents

### `oquilla-daily-black-rust-hunter.relation.carrack-advance`

- seed_key: "oquilla-daily-black-rust-hunter.relation.carrack-advance"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "carrack-advance"
- content_name_ko: "에페리아 중범선 : 점진"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/carrack-advance.md"

## Evidence and Sources

### Current evidence

### `oquilla-daily-black-rust-hunter.evidence.purpose::ocean-barter-rework-2024-03-27`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.purpose::ocean-barter-rework-2024-03-27"
- source_id: "ocean-barter-rework-2024-03-27"
- title: "3월 27일(수) 업데이트 안내 (최종 수정 : 2024-05-22 11:50)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11951"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-03-27"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "oquilla-daily-black-rust-hunter"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "중범선 이후 선박 장비 재료 또는 강화 재료를 확보하는 대안 일일 의뢰."
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.purpose::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.purpose::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "oquilla-daily-black-rust-hunter"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "중범선 이후 선박 장비 재료 또는 강화 재료를 확보하는 대안 일일 의뢰."
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.summary::ocean-barter-rework-2024-03-27`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.summary::ocean-barter-rework-2024-03-27"
- source_id: "ocean-barter-rework-2024-03-27"
- title: "3월 27일(수) 업데이트 안내 (최종 수정 : 2024-05-22 11:50)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11951"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-03-27"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "oquilla-daily-black-rust-hunter"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "검은무쇠이빨 1마리 처치 후 까마귀 주화와 선박 장비 관련 선택 보상을 받는 성체 해왕류 일일 의뢰."
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.summary::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.summary::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "oquilla-daily-black-rust-hunter"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "검은무쇠이빨 1마리 처치 후 까마귀 주화와 선박 장비 관련 선택 보상을 받는 성체 해왕류 일일 의뢰."
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.relation.carrack-advance::carrack-guide`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.relation.carrack-advance::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "oquilla-daily-black-rust-hunter.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.relation.carrack-advance::ocean-barter-rework-2024-03-27`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.relation.carrack-advance::ocean-barter-rework-2024-03-27"
- source_id: "ocean-barter-rework-2024-03-27"
- title: "3월 27일(수) 업데이트 안내 (최종 수정 : 2024-05-22 11:50)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11951"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-03-27"
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "oquilla-daily-black-rust-hunter.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.relation.carrack-advance::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.relation.carrack-advance::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "oquilla-daily-black-rust-hunter.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.requirement.start-npc::ocean-barter-rework-2024-03-27`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.requirement.start-npc::ocean-barter-rework-2024-03-27"
- source_id: "ocean-barter-rework-2024-03-27"
- title: "3월 27일(수) 업데이트 안내 (최종 수정 : 2024-05-22 11:50)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11951"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-03-27"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "oquilla-daily-black-rust-hunter.requirement.start-npc"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "수주 NPC: 오킬루아의 눈 라비켈"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "oquilla-daily-black-rust-hunter.requirement.start-npc"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "수주 NPC: 오킬루아의 눈 라비켈"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.section.mutual-exclusion::carrack-guide`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.section.mutual-exclusion::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "oquilla-daily-black-rust-hunter.section.mutual-exclusion"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "어린 해왕류 일일과 상호 배타"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.section.mutual-exclusion::ocean-barter-rework-2024-03-27`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.section.mutual-exclusion::ocean-barter-rework-2024-03-27"
- source_id: "ocean-barter-rework-2024-03-27"
- title: "3월 27일(수) 업데이트 안내 (최종 수정 : 2024-05-22 11:50)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11951"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-03-27"
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "oquilla-daily-black-rust-hunter.section.mutual-exclusion"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "어린 해왕류 일일과 상호 배타"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.step.objective::ocean-barter-rework-2024-03-27`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.step.objective::ocean-barter-rework-2024-03-27"
- source_id: "ocean-barter-rework-2024-03-27"
- title: "3월 27일(수) 업데이트 안내 (최종 수정 : 2024-05-22 11:50)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11951"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-03-27"
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "oquilla-daily-black-rust-hunter.step.complete-objective"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "검은무쇠이빨 1마리 처치"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.step.objective::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.step.objective::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "oquilla-daily-black-rust-hunter.step.complete-objective"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "검은무쇠이빨 1마리 처치"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.contribution-exp::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.contribution-exp::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-daily-black-rust-hunter.reward.contribution-exp"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "공헌도 경험치 현행 보상"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.reward.crow-coins::ocean-barter-rework-2024-03-27`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.reward.crow-coins::ocean-barter-rework-2024-03-27"
- source_id: "ocean-barter-rework-2024-03-27"
- title: "3월 27일(수) 업데이트 안내 (최종 수정 : 2024-05-22 11:50)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11951"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-03-27"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-daily-black-rust-hunter.reward.crow-coins"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 까마귀 주화"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.reward.crow-coins::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.reward.crow-coins::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-daily-black-rust-hunter.reward.crow-coins"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 까마귀 주화"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.reward.oquilla-coin::ocean-barter-rework-2024-03-27`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.reward.oquilla-coin::ocean-barter-rework-2024-03-27"
- source_id: "ocean-barter-rework-2024-03-27"
- title: "3월 27일(수) 업데이트 안내 (최종 수정 : 2024-05-22 11:50)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11951"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-03-27"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-daily-black-rust-hunter.reward.oquilla-coin"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 오킬루아 기념 주화"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.reward.oquilla-coin::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.reward.oquilla-coin::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-daily-black-rust-hunter.reward.oquilla-coin"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 오킬루아 기념 주화"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.reward.post-carrack-material::ocean-barter-rework-2024-03-27`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.reward.post-carrack-material::ocean-barter-rework-2024-03-27"
- source_id: "ocean-barter-rework-2024-03-27"
- title: "3월 27일(수) 업데이트 안내 (최종 수정 : 2024-05-22 11:50)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11951"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-03-27"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-daily-black-rust-hunter.reward.post-carrack-material"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 파도의 흔적이 담긴 접착제"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.reward.post-carrack-material::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.reward.post-carrack-material::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-daily-black-rust-hunter.reward.post-carrack-material"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 파도의 흔적이 담긴 접착제"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.sailing-exp::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.sailing-exp::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-daily-black-rust-hunter.reward.sailing-exp"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "항해 경험치 현행 보상"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.reward.wave-black-stone::ocean-barter-rework-2024-03-27`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.reward.wave-black-stone::ocean-barter-rework-2024-03-27"
- source_id: "ocean-barter-rework-2024-03-27"
- title: "3월 27일(수) 업데이트 안내 (최종 수정 : 2024-05-22 11:50)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11951"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-03-27"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-daily-black-rust-hunter.reward.wave-black-stone"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 파도의 블랙스톤"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.reward.wave-black-stone::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.reward.wave-black-stone::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-daily-black-rust-hunter.reward.wave-black-stone"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 파도의 블랙스톤"
- active: true
- is_active: true

### `oquilla-daily-black-rust-hunter.evidence.schedule.reset::daily-weekly-reset-gm-2023`

- evidence_seed_key: "oquilla-daily-black-rust-hunter.evidence.schedule.reset::daily-weekly-reset-gm-2023"
- source_id: "daily-weekly-reset-gm-2023"
- title: "검은사막이 처음인 모험가 여러분을 위해 준비한 A to Z!"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=10577"
- publisher: "Pearl Abyss"
- source_type: "official_gm"
- published_at: "2023-07-25"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "oquilla-daily-black-rust-hunter.schedule.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일일 의뢰: 매일 00:00 KST 초기화"
- active: true
- is_active: true

### Historical / inactive evidence

- None
