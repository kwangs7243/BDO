<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# [주간] 그믐달 길드의 칸디둠 사냥꾼

## Identity

- slug: "oquilla-weekly-candidum-hunter"
- name_ko: "[주간] 그믐달 길드의 칸디둠 사냥꾼"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "칸디둠 1마리를 처치해 까마귀 주화 500과 선택 보상을 받는 오킬루아 주간 의뢰."
- purpose: "흑룡 선수상·비층 바람 돛에 필요한 홍조빛 해저단괴를 효율적으로 확보한다."

## Requirements

### `oquilla-weekly-candidum-hunter.requirement.start-npc`

- seed_key: "oquilla-weekly-candidum-hunter.requirement.start-npc"
- kind: "other"
- requirement_level: "required"
- title: "수주 NPC"
- description: "오킬루아의 눈 라비켈"
- structured_value: null

## Steps

### `oquilla-weekly-candidum-hunter.step.complete-objective`

- seed_key: "oquilla-weekly-candidum-hunter.step.complete-objective"
- phase: "repeat"
- order_no: 1
- title: "의뢰 목표 완료"
- description: "칸디둠 1마리 처치"
- checkable: false

## Schedules

### `oquilla-weekly-candidum-hunter.schedule.quest-reset`

- seed_key: "oquilla-weekly-candidum-hunter.schedule.quest-reset"
- rule_type: "quest_reset"
- recurrence_type: "weekly"
- weekday: 3
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "주간 의뢰: 매주 목요일 00:00 KST 초기화"

## Rewards

### `oquilla-weekly-candidum-hunter.reward.crow-coins`

- seed_key: "oquilla-weekly-candidum-hunter.reward.crow-coins"
- name: "까마귀 주화"
- reward_type: "quest_reward"
- amount: 500.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 1

### `oquilla-weekly-candidum-hunter.reward.wave-black-stone`

- seed_key: "oquilla-weekly-candidum-hunter.reward.wave-black-stone"
- name: "파도의 블랙스톤"
- reward_type: "quest_reward"
- amount: 60.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "oquilla-weekly-candidum-hunter.choice-1"
- recommendation: null
- notes: null
- order_no: 2

### `oquilla-weekly-candidum-hunter.reward.red-lump`

- seed_key: "oquilla-weekly-candidum-hunter.reward.red-lump"
- name: "홍조빛 해저단괴"
- reward_type: "quest_reward"
- amount: 4.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "oquilla-weekly-candidum-hunter.choice-1"
- recommendation: "중범선 : 점진 제작 중이라면 홍조빛 해저단괴 4개를 우선 추천한다."
- notes: null
- order_no: 3

### `oquilla-weekly-candidum-hunter.reward.violent-plywood`

- seed_key: "oquilla-weekly-candidum-hunter.reward.violent-plywood"
- name: "난폭한 파도가 새겨진 합판"
- reward_type: "quest_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "oquilla-weekly-candidum-hunter.choice-1"
- recommendation: null
- notes: null
- order_no: 4

### `oquilla-weekly-candidum-hunter.reward.contribution-exp`

- seed_key: "oquilla-weekly-candidum-hunter.reward.contribution-exp"
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

### `oquilla-weekly-candidum-hunter.reward.sailing-exp`

- seed_key: "oquilla-weekly-candidum-hunter.reward.sailing-exp"
- name: "항해 경험치"
- reward_type: "experience"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "2025-02-05 이후 기존 대비 2배"
- order_no: 6

## Sections

- None

## Related Contents

### `oquilla-weekly-candidum-hunter.relation.carrack-advance`

- seed_key: "oquilla-weekly-candidum-hunter.relation.carrack-advance"
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

### `oquilla-weekly-candidum-hunter.evidence.purpose::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-candidum-hunter.evidence.purpose::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "oquilla-weekly-candidum-hunter"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "흑룡 선수상·비층 바람 돛에 필요한 홍조빛 해저단괴를 효율적으로 확보한다."
- active: true
- is_active: true

### `oquilla-weekly-candidum-hunter.evidence.summary::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-candidum-hunter.evidence.summary::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "oquilla-weekly-candidum-hunter"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "칸디둠 1마리를 처치해 까마귀 주화 500과 선택 보상을 받는 오킬루아 주간 의뢰."
- active: true
- is_active: true

### `oquilla-weekly-candidum-hunter.evidence.relation.carrack-advance::carrack-guide`

- evidence_seed_key: "oquilla-weekly-candidum-hunter.evidence.relation.carrack-advance::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "oquilla-weekly-candidum-hunter.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `oquilla-weekly-candidum-hunter.evidence.relation.carrack-advance::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-candidum-hunter.evidence.relation.carrack-advance::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "oquilla-weekly-candidum-hunter.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `oquilla-weekly-candidum-hunter.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-candidum-hunter.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "oquilla-weekly-candidum-hunter.requirement.start-npc"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "수주 NPC: 오킬루아의 눈 라비켈"
- active: true
- is_active: true

### `oquilla-weekly-candidum-hunter.evidence.step.objective::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-candidum-hunter.evidence.step.objective::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "oquilla-weekly-candidum-hunter.step.complete-objective"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "칸디둠 1마리 처치"
- active: true
- is_active: true

### `oquilla-weekly-candidum-hunter.evidence.contribution-exp::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-candidum-hunter.evidence.contribution-exp::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-weekly-candidum-hunter.reward.contribution-exp"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "공헌도 경험치 현행 보상"
- active: true
- is_active: true

### `oquilla-weekly-candidum-hunter.evidence.reward.crow-coins::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-candidum-hunter.evidence.reward.crow-coins::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-weekly-candidum-hunter.reward.crow-coins"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 까마귀 주화"
- active: true
- is_active: true

### `oquilla-weekly-candidum-hunter.evidence.reward.red-lump.recommendation::carrack-guide`

- evidence_seed_key: "oquilla-weekly-candidum-hunter.evidence.reward.red-lump.recommendation::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-weekly-candidum-hunter.reward.red-lump"
- claim_key: "recommendation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "중범선 : 점진 제작 중이라면 홍조빛 해저단괴 4개를 우선 추천한다."
- active: true
- is_active: true

### `oquilla-weekly-candidum-hunter.evidence.reward.red-lump.recommendation::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-candidum-hunter.evidence.reward.red-lump.recommendation::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-weekly-candidum-hunter.reward.red-lump"
- claim_key: "recommendation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "중범선 : 점진 제작 중이라면 홍조빛 해저단괴 4개를 우선 추천한다."
- active: true
- is_active: true

### `oquilla-weekly-candidum-hunter.evidence.reward.red-lump::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-candidum-hunter.evidence.reward.red-lump::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-weekly-candidum-hunter.reward.red-lump"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 홍조빛 해저단괴"
- active: true
- is_active: true

### `oquilla-weekly-candidum-hunter.evidence.sailing-exp::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-candidum-hunter.evidence.sailing-exp::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-weekly-candidum-hunter.reward.sailing-exp"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "항해 경험치 현행 보상"
- active: true
- is_active: true

### `oquilla-weekly-candidum-hunter.evidence.reward.violent-plywood::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-candidum-hunter.evidence.reward.violent-plywood::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-weekly-candidum-hunter.reward.violent-plywood"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 난폭한 파도가 새겨진 합판"
- active: true
- is_active: true

### `oquilla-weekly-candidum-hunter.evidence.reward.wave-black-stone::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-candidum-hunter.evidence.reward.wave-black-stone::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-weekly-candidum-hunter.reward.wave-black-stone"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 파도의 블랙스톤"
- active: true
- is_active: true

### `oquilla-weekly-candidum-hunter.evidence.schedule.reset::daily-weekly-reset-gm-2023`

- evidence_seed_key: "oquilla-weekly-candidum-hunter.evidence.schedule.reset::daily-weekly-reset-gm-2023"
- source_id: "daily-weekly-reset-gm-2023"
- title: "검은사막이 처음인 모험가 여러분을 위해 준비한 A to Z!"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=10577"
- publisher: "Pearl Abyss"
- source_type: "official_gm"
- published_at: "2023-07-25"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "oquilla-weekly-candidum-hunter.schedule.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 의뢰: 매주 목요일 00:00 KST 초기화"
- active: true
- is_active: true

### Historical / inactive evidence

- None
