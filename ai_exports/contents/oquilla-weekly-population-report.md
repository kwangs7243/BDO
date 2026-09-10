<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# [주간] 개체수 증가 보고

## Identity

- slug: "oquilla-weekly-population-report"
- name_ko: "[주간] 개체수 증가 보고"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "어린 해왕류 20마리를 처치해 콕스해적단의 유물(전투) 2개를 받는 주간 의뢰."
- purpose: "점진 파란 장비에 총 120개 필요한 전투 유물을 추가 확보한다."

## Requirements

### `oquilla-weekly-population-report.requirement.start-npc`

- seed_key: "oquilla-weekly-population-report.requirement.start-npc"
- kind: "other"
- requirement_level: "required"
- title: "수주 NPC"
- description: "오킬루아의 눈 셰르엄 리키 인근 병사"
- structured_value: null

## Steps

### `oquilla-weekly-population-report.step.complete-objective`

- seed_key: "oquilla-weekly-population-report.step.complete-objective"
- phase: "repeat"
- order_no: 1
- title: "의뢰 목표 완료"
- description: "어린 해왕류 20마리 처치"
- checkable: false

## Schedules

### `oquilla-weekly-population-report.schedule.quest-reset`

- seed_key: "oquilla-weekly-population-report.schedule.quest-reset"
- rule_type: "quest_reset"
- recurrence_type: "weekly"
- weekday: 3
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "주간 의뢰: 매주 목요일 00:00 KST 초기화"

## Rewards

### `oquilla-weekly-population-report.reward.combat-artifact`

- seed_key: "oquilla-weekly-population-report.reward.combat-artifact"
- name: "콕스해적단의 유물(전투)"
- reward_type: "quest_reward"
- amount: 2.0
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

### `oquilla-weekly-population-report.relation.carrack-advance`

- seed_key: "oquilla-weekly-population-report.relation.carrack-advance"
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

### `oquilla-weekly-population-report.evidence.purpose::ocean-barter-rework-2024-03-27`

- evidence_seed_key: "oquilla-weekly-population-report.evidence.purpose::ocean-barter-rework-2024-03-27"
- source_id: "ocean-barter-rework-2024-03-27"
- title: "3월 27일(수) 업데이트 안내 (최종 수정 : 2024-05-22 11:50)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11951"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-03-27"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "oquilla-weekly-population-report"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진 파란 장비에 총 120개 필요한 전투 유물을 추가 확보한다."
- active: true
- is_active: true

### `oquilla-weekly-population-report.evidence.purpose::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-population-report.evidence.purpose::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "oquilla-weekly-population-report"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진 파란 장비에 총 120개 필요한 전투 유물을 추가 확보한다."
- active: true
- is_active: true

### `oquilla-weekly-population-report.evidence.summary::ocean-barter-rework-2024-03-27`

- evidence_seed_key: "oquilla-weekly-population-report.evidence.summary::ocean-barter-rework-2024-03-27"
- source_id: "ocean-barter-rework-2024-03-27"
- title: "3월 27일(수) 업데이트 안내 (최종 수정 : 2024-05-22 11:50)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11951"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-03-27"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "oquilla-weekly-population-report"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "어린 해왕류 20마리를 처치해 콕스해적단의 유물(전투) 2개를 받는 주간 의뢰."
- active: true
- is_active: true

### `oquilla-weekly-population-report.evidence.summary::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-population-report.evidence.summary::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "oquilla-weekly-population-report"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "어린 해왕류 20마리를 처치해 콕스해적단의 유물(전투) 2개를 받는 주간 의뢰."
- active: true
- is_active: true

### `oquilla-weekly-population-report.evidence.relation.carrack-advance::carrack-guide`

- evidence_seed_key: "oquilla-weekly-population-report.evidence.relation.carrack-advance::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "oquilla-weekly-population-report.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `oquilla-weekly-population-report.evidence.relation.carrack-advance::ocean-barter-rework-2024-03-27`

- evidence_seed_key: "oquilla-weekly-population-report.evidence.relation.carrack-advance::ocean-barter-rework-2024-03-27"
- source_id: "ocean-barter-rework-2024-03-27"
- title: "3월 27일(수) 업데이트 안내 (최종 수정 : 2024-05-22 11:50)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11951"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-03-27"
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "oquilla-weekly-population-report.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `oquilla-weekly-population-report.evidence.relation.carrack-advance::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-population-report.evidence.relation.carrack-advance::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "oquilla-weekly-population-report.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `oquilla-weekly-population-report.evidence.requirement.start-npc::ocean-barter-rework-2024-03-27`

- evidence_seed_key: "oquilla-weekly-population-report.evidence.requirement.start-npc::ocean-barter-rework-2024-03-27"
- source_id: "ocean-barter-rework-2024-03-27"
- title: "3월 27일(수) 업데이트 안내 (최종 수정 : 2024-05-22 11:50)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11951"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-03-27"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "oquilla-weekly-population-report.requirement.start-npc"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "수주 NPC: 오킬루아의 눈 셰르엄 리키 인근 병사"
- active: true
- is_active: true

### `oquilla-weekly-population-report.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-population-report.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "oquilla-weekly-population-report.requirement.start-npc"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "수주 NPC: 오킬루아의 눈 셰르엄 리키 인근 병사"
- active: true
- is_active: true

### `oquilla-weekly-population-report.evidence.step.objective::ocean-barter-rework-2024-03-27`

- evidence_seed_key: "oquilla-weekly-population-report.evidence.step.objective::ocean-barter-rework-2024-03-27"
- source_id: "ocean-barter-rework-2024-03-27"
- title: "3월 27일(수) 업데이트 안내 (최종 수정 : 2024-05-22 11:50)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11951"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-03-27"
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "oquilla-weekly-population-report.step.complete-objective"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "어린 해왕류 20마리 처치"
- active: true
- is_active: true

### `oquilla-weekly-population-report.evidence.step.objective::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-population-report.evidence.step.objective::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "oquilla-weekly-population-report.step.complete-objective"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "어린 해왕류 20마리 처치"
- active: true
- is_active: true

### `oquilla-weekly-population-report.evidence.reward.combat-artifact::ocean-barter-rework-2024-03-27`

- evidence_seed_key: "oquilla-weekly-population-report.evidence.reward.combat-artifact::ocean-barter-rework-2024-03-27"
- source_id: "ocean-barter-rework-2024-03-27"
- title: "3월 27일(수) 업데이트 안내 (최종 수정 : 2024-05-22 11:50)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11951"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-03-27"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-weekly-population-report.reward.combat-artifact"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 콕스해적단의 유물(전투)"
- active: true
- is_active: true

### `oquilla-weekly-population-report.evidence.reward.combat-artifact::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-weekly-population-report.evidence.reward.combat-artifact::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-weekly-population-report.reward.combat-artifact"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 콕스해적단의 유물(전투)"
- active: true
- is_active: true

### `oquilla-weekly-population-report.evidence.schedule.reset::daily-weekly-reset-gm-2023`

- evidence_seed_key: "oquilla-weekly-population-report.evidence.schedule.reset::daily-weekly-reset-gm-2023"
- source_id: "daily-weekly-reset-gm-2023"
- title: "검은사막이 처음인 모험가 여러분을 위해 준비한 A to Z!"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=10577"
- publisher: "Pearl Abyss"
- source_type: "official_gm"
- published_at: "2023-07-25"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "oquilla-weekly-population-report.schedule.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 의뢰: 매주 목요일 00:00 KST 초기화"
- active: true
- is_active: true

### Historical / inactive evidence

- None
