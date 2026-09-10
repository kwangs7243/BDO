<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# [일일] 길드는 자선단체가 아니다

## Identity

- slug: "oquilla-daily-guild-charity"
- name_ko: "[일일] 길드는 자선단체가 아니다"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "어린 해왕류 2마리를 쫓아내고 점진 파란 장비 재료 선택 보상을 받는 오킬루아 일일 의뢰."
- purpose: "메이나 함포 제작에 필요한 파도빛이 감도는 규격 각목을 확보한다."

## Requirements

### `oquilla-daily-guild-charity.requirement.start-npc`

- seed_key: "oquilla-daily-guild-charity.requirement.start-npc"
- kind: "other"
- requirement_level: "required"
- title: "수주 NPC"
- description: "오킬루아의 눈 셰르엄 리키 인근 병사"
- structured_value: null

## Steps

### `oquilla-daily-guild-charity.step.complete-objective`

- seed_key: "oquilla-daily-guild-charity.step.complete-objective"
- phase: "repeat"
- order_no: 1
- title: "의뢰 목표 완료"
- description: "어린 해왕류 2마리 쫓아내기"
- checkable: false

## Schedules

### `oquilla-daily-guild-charity.schedule.quest-reset`

- seed_key: "oquilla-daily-guild-charity.schedule.quest-reset"
- rule_type: "quest_reset"
- recurrence_type: "daily"
- weekday: null
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "일일 의뢰: 매일 00:00 KST 초기화"

## Rewards

### `oquilla-daily-guild-charity.reward.oquilla-coin`

- seed_key: "oquilla-daily-guild-charity.reward.oquilla-coin"
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

### `oquilla-daily-guild-charity.reward.wave-timber`

- seed_key: "oquilla-daily-guild-charity.reward.wave-timber"
- name: "파도빛이 감도는 규격 각목"
- reward_type: "quest_reward"
- amount: 5.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "oquilla-daily-guild-charity.choice-1"
- recommendation: "중범선 : 점진 제작 중이라면 파도빛이 감도는 규격 각목 5개를 우선 추천한다."
- notes: null
- order_no: 2

### `oquilla-daily-guild-charity.reward.violent-plywood`

- seed_key: "oquilla-daily-guild-charity.reward.violent-plywood"
- name: "난폭한 파도가 새겨진 합판"
- reward_type: "quest_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "oquilla-daily-guild-charity.choice-1"
- recommendation: null
- notes: null
- order_no: 3

## Sections

- None

## Related Contents

### `oquilla-daily-guild-charity.relation.carrack-advance`

- seed_key: "oquilla-daily-guild-charity.relation.carrack-advance"
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

### `oquilla-daily-guild-charity.evidence.purpose::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-guild-charity.evidence.purpose::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "oquilla-daily-guild-charity"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "메이나 함포 제작에 필요한 파도빛이 감도는 규격 각목을 확보한다."
- active: true
- is_active: true

### `oquilla-daily-guild-charity.evidence.summary::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-guild-charity.evidence.summary::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "oquilla-daily-guild-charity"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "어린 해왕류 2마리를 쫓아내고 점진 파란 장비 재료 선택 보상을 받는 오킬루아 일일 의뢰."
- active: true
- is_active: true

### `oquilla-daily-guild-charity.evidence.relation.carrack-advance::carrack-guide`

- evidence_seed_key: "oquilla-daily-guild-charity.evidence.relation.carrack-advance::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "oquilla-daily-guild-charity.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `oquilla-daily-guild-charity.evidence.relation.carrack-advance::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-guild-charity.evidence.relation.carrack-advance::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "oquilla-daily-guild-charity.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `oquilla-daily-guild-charity.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-guild-charity.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "oquilla-daily-guild-charity.requirement.start-npc"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "수주 NPC: 오킬루아의 눈 셰르엄 리키 인근 병사"
- active: true
- is_active: true

### `oquilla-daily-guild-charity.evidence.step.objective::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-guild-charity.evidence.step.objective::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "oquilla-daily-guild-charity.step.complete-objective"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "어린 해왕류 2마리 쫓아내기"
- active: true
- is_active: true

### `oquilla-daily-guild-charity.evidence.reward.oquilla-coin::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-guild-charity.evidence.reward.oquilla-coin::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-daily-guild-charity.reward.oquilla-coin"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 오킬루아 기념 주화"
- active: true
- is_active: true

### `oquilla-daily-guild-charity.evidence.reward.violent-plywood::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-guild-charity.evidence.reward.violent-plywood::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-daily-guild-charity.reward.violent-plywood"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 난폭한 파도가 새겨진 합판"
- active: true
- is_active: true

### `oquilla-daily-guild-charity.evidence.reward.wave-timber.recommendation::carrack-guide`

- evidence_seed_key: "oquilla-daily-guild-charity.evidence.reward.wave-timber.recommendation::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-daily-guild-charity.reward.wave-timber"
- claim_key: "recommendation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "중범선 : 점진 제작 중이라면 파도빛이 감도는 규격 각목 5개를 우선 추천한다."
- active: true
- is_active: true

### `oquilla-daily-guild-charity.evidence.reward.wave-timber.recommendation::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-guild-charity.evidence.reward.wave-timber.recommendation::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-daily-guild-charity.reward.wave-timber"
- claim_key: "recommendation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "중범선 : 점진 제작 중이라면 파도빛이 감도는 규격 각목 5개를 우선 추천한다."
- active: true
- is_active: true

### `oquilla-daily-guild-charity.evidence.reward.wave-timber::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "oquilla-daily-guild-charity.evidence.reward.wave-timber::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "oquilla-daily-guild-charity.reward.wave-timber"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 파도빛이 감도는 규격 각목"
- active: true
- is_active: true

### `oquilla-daily-guild-charity.evidence.schedule.reset::daily-weekly-reset-gm-2023`

- evidence_seed_key: "oquilla-daily-guild-charity.evidence.schedule.reset::daily-weekly-reset-gm-2023"
- source_id: "daily-weekly-reset-gm-2023"
- title: "검은사막이 처음인 모험가 여러분을 위해 준비한 A to Z!"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=10577"
- publisher: "Pearl Abyss"
- source_type: "official_gm"
- published_at: "2023-07-25"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "oquilla-daily-guild-charity.schedule.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일일 의뢰: 매일 00:00 KST 초기화"
- active: true
- is_active: true

### Historical / inactive evidence

- None
