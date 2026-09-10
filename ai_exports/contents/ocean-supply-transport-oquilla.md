<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# [일일] 보급물자 운송 (오킬루아의 눈)

## Identity

- slug: "ocean-supply-transport-oquilla"
- name_ko: "[일일] 보급물자 운송 (오킬루아의 눈)"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "일리야 섬 다리오에게서 받아 오킬루아의 눈 라비켈에게 보급물자를 180분 안에 전달하는 일일 의뢰."
- purpose: "콕스해적단의 유물(협상 하급)과 까마귀 주화를 매일 확보한다."

## Requirements

### `ocean-supply-transport-oquilla.requirement.start-npc`

- seed_key: "ocean-supply-transport-oquilla.requirement.start-npc"
- kind: "other"
- requirement_level: "required"
- title: "수주 NPC"
- description: "일리야 섬 다리오"
- structured_value: null

## Steps

### `ocean-supply-transport-oquilla.step.complete-objective`

- seed_key: "ocean-supply-transport-oquilla.step.complete-objective"
- phase: "repeat"
- order_no: 1
- title: "의뢰 목표 완료"
- description: "일리야 섬 다리오의 보급물자를 오킬루아의 눈 라비켈에게 180분 이내 전달"
- checkable: false

## Schedules

### `ocean-supply-transport-oquilla.schedule.quest-reset`

- seed_key: "ocean-supply-transport-oquilla.schedule.quest-reset"
- rule_type: "quest_reset"
- recurrence_type: "daily"
- weekday: null
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "일일 의뢰: 매일 00:00 KST 초기화"

## Rewards

### `ocean-supply-transport-oquilla.reward.parley-beginner`

- seed_key: "ocean-supply-transport-oquilla.reward.parley-beginner"
- name: "콕스해적단의 유물(협상 하급)"
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

### `ocean-supply-transport-oquilla.reward.crow-coins`

- seed_key: "ocean-supply-transport-oquilla.reward.crow-coins"
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

## Sections

### `ocean-supply-transport-oquilla.section.time-limit`

- seed_key: "ocean-supply-transport-oquilla.section.time-limit"
- section_type: "preparation"
- title: "제한 시간"
- order_no: 1

#### body_markdown

2025-02-05 업데이트에서 제한 시간이 60분에서 180분으로 늘어났다.

## Related Contents

### `ocean-supply-transport-oquilla.relation.carrack-advance`

- seed_key: "ocean-supply-transport-oquilla.relation.carrack-advance"
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

### `ocean-supply-transport-oquilla.evidence.purpose::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-supply-transport-oquilla.evidence.purpose::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "ocean-supply-transport-oquilla"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "콕스해적단의 유물(협상 하급)과 까마귀 주화를 매일 확보한다."
- active: true
- is_active: true

### `ocean-supply-transport-oquilla.evidence.summary::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-supply-transport-oquilla.evidence.summary::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "ocean-supply-transport-oquilla"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일리야 섬 다리오에게서 받아 오킬루아의 눈 라비켈에게 보급물자를 180분 안에 전달하는 일일 의뢰."
- active: true
- is_active: true

### `ocean-supply-transport-oquilla.evidence.relation.carrack-advance::carrack-guide`

- evidence_seed_key: "ocean-supply-transport-oquilla.evidence.relation.carrack-advance::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "ocean-supply-transport-oquilla.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `ocean-supply-transport-oquilla.evidence.relation.carrack-advance::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-supply-transport-oquilla.evidence.relation.carrack-advance::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "ocean-supply-transport-oquilla.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `ocean-supply-transport-oquilla.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-supply-transport-oquilla.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ocean-supply-transport-oquilla.requirement.start-npc"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "수주 NPC: 일리야 섬 다리오"
- active: true
- is_active: true

### `ocean-supply-transport-oquilla.evidence.section.time-limit::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-supply-transport-oquilla.evidence.section.time-limit::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "ocean-supply-transport-oquilla.section.time-limit"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "제한 시간"
- active: true
- is_active: true

### `ocean-supply-transport-oquilla.evidence.step.objective::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-supply-transport-oquilla.evidence.step.objective::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "ocean-supply-transport-oquilla.step.complete-objective"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일리야 섬 다리오의 보급물자를 오킬루아의 눈 라비켈에게 180분 이내 전달"
- active: true
- is_active: true

### `ocean-supply-transport-oquilla.evidence.reward.crow-coins::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-supply-transport-oquilla.evidence.reward.crow-coins::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-supply-transport-oquilla.reward.crow-coins"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 까마귀 주화"
- active: true
- is_active: true

### `ocean-supply-transport-oquilla.evidence.reward.parley-beginner::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-supply-transport-oquilla.evidence.reward.parley-beginner::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-supply-transport-oquilla.reward.parley-beginner"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 콕스해적단의 유물(협상 하급)"
- active: true
- is_active: true

### `ocean-supply-transport-oquilla.evidence.schedule.reset::daily-weekly-reset-gm-2023`

- evidence_seed_key: "ocean-supply-transport-oquilla.evidence.schedule.reset::daily-weekly-reset-gm-2023"
- source_id: "daily-weekly-reset-gm-2023"
- title: "검은사막이 처음인 모험가 여러분을 위해 준비한 A to Z!"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=10577"
- publisher: "Pearl Abyss"
- source_type: "official_gm"
- published_at: "2023-07-25"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "ocean-supply-transport-oquilla.schedule.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일일 의뢰: 매일 00:00 KST 초기화"
- active: true
- is_active: true

### Historical / inactive evidence

- None
