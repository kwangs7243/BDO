<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# [물물교환][일일] 활기찬 일리야 섬

## Identity

- slug: "ocean-iliya-daily-barter"
- name_ko: "[물물교환][일일] 활기찬 일리야 섬"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "물물교환 15회를 진행하는 일리야 섬 통합 일일 의뢰. 2025-05-14부터 기존 I~III가 하나로 통합되었다."
- purpose: "무역선 파란 장비 제작 재료와 까마귀 주화를 매일 확보한다."

## Requirements

### `ocean-iliya-daily-barter.requirement.start-npc`

- seed_key: "ocean-iliya-daily-barter.requirement.start-npc"
- kind: "other"
- requirement_level: "required"
- title: "수주 NPC"
- description: "일리야 섬 주민 NPC / 통합 의뢰"
- structured_value: null

## Steps

### `ocean-iliya-daily-barter.step.complete-objective`

- seed_key: "ocean-iliya-daily-barter.step.complete-objective"
- phase: "repeat"
- order_no: 1
- title: "의뢰 목표 완료"
- description: "물물교환 15회 진행"
- checkable: false

## Schedules

### `ocean-iliya-daily-barter.schedule.quest-reset`

- seed_key: "ocean-iliya-daily-barter.schedule.quest-reset"
- rule_type: "quest_reset"
- recurrence_type: "daily"
- weekday: null
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "일일 의뢰: 매일 00:00 KST 초기화"

## Rewards

### `ocean-iliya-daily-barter.reward.pure-pearl`

- seed_key: "ocean-iliya-daily-barter.reward.pure-pearl"
- name: "순수한 진주 결정"
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

### `ocean-iliya-daily-barter.reward.deep-memory-glue`

- seed_key: "ocean-iliya-daily-barter.reward.deep-memory-glue"
- name: "심해의 기억이 담긴 아교"
- reward_type: "quest_reward"
- amount: 8.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 2

### `ocean-iliya-daily-barter.reward.pure-reef`

- seed_key: "ocean-iliya-daily-barter.reward.pure-reef"
- name: "순수한 암초 조각"
- reward_type: "quest_reward"
- amount: 8.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 3

### `ocean-iliya-daily-barter.reward.enhanced-plywood`

- seed_key: "ocean-iliya-daily-barter.reward.enhanced-plywood"
- name: "강화된 섬나무 증착합판"
- reward_type: "quest_reward"
- amount: 10.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 4

### `ocean-iliya-daily-barter.reward.parley-expert`

- seed_key: "ocean-iliya-daily-barter.reward.parley-expert"
- name: "콕스해적단의 유물(협상 상급)"
- reward_type: "quest_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 5

### `ocean-iliya-daily-barter.reward.crow-coins`

- seed_key: "ocean-iliya-daily-barter.reward.crow-coins"
- name: "까마귀 주화"
- reward_type: "quest_reward"
- amount: 50.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 6

## Sections

### `ocean-iliya-daily-barter.section.consolidation`

- seed_key: "ocean-iliya-daily-barter.section.consolidation"
- section_type: "notes"
- title: "통합 이력"
- order_no: 1

#### body_markdown

2025-05-14 업데이트로 `[물물교환][일일] 활기찬 일리야 섬 I~III`가 삭제되고 `활기찬 일리야 섬` 하나로 통합되었다. 목표는 물물교환 15회이며 통합 전 전체 보상과 동일하다.

## Related Contents

### `ocean-iliya-daily-barter.relation.carrack-advance`

- seed_key: "ocean-iliya-daily-barter.relation.carrack-advance"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "carrack-advance"
- content_name_ko: "에페리아 중범선 : 점진"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/carrack-advance.md"
### `barter-onboarding-strategy.daily`

- seed_key: "barter-onboarding-strategy.daily"
- direction: "incoming"
- relation_type: "related"
- content_slug: "barter-onboarding-strategy"
- content_name_ko: "물물교환 입문 운영 전략"
- content_category: "ocean_barter"
- note: "일일 물물교환 목표"
- order_no: 9
- relative_path: "../contents/barter-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `ocean-iliya-daily-barter.evidence.purpose::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.purpose::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "ocean-iliya-daily-barter"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "무역선 파란 장비 제작 재료와 까마귀 주화를 매일 확보한다."
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.purpose::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.purpose::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "ocean-iliya-daily-barter"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "무역선 파란 장비 제작 재료와 까마귀 주화를 매일 확보한다."
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.summary::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.summary::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "ocean-iliya-daily-barter"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "물물교환 15회를 진행하는 일리야 섬 통합 일일 의뢰. 2025-05-14부터 기존 I~III가 하나로 통합되었다."
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.summary::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.summary::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "ocean-iliya-daily-barter"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "물물교환 15회를 진행하는 일리야 섬 통합 일일 의뢰. 2025-05-14부터 기존 I~III가 하나로 통합되었다."
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.relation.carrack-advance::carrack-guide`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.relation.carrack-advance::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "ocean-iliya-daily-barter.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.relation.carrack-advance::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.relation.carrack-advance::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "ocean-iliya-daily-barter.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.relation.carrack-advance::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.relation.carrack-advance::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "ocean-iliya-daily-barter.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.requirement.start-npc::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.requirement.start-npc::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ocean-iliya-daily-barter.requirement.start-npc"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "수주 NPC: 일리야 섬 주민 NPC / 통합 의뢰"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.requirement.start-npc::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ocean-iliya-daily-barter.requirement.start-npc"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "수주 NPC: 일리야 섬 주민 NPC / 통합 의뢰"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.section.consolidation::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.section.consolidation::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "ocean-iliya-daily-barter.section.consolidation"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "통합 이력"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.section.consolidation::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.section.consolidation::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "ocean-iliya-daily-barter.section.consolidation"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "통합 이력"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.step.objective::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.step.objective::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "ocean-iliya-daily-barter.step.complete-objective"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "물물교환 15회 진행"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.step.objective::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.step.objective::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "ocean-iliya-daily-barter.step.complete-objective"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "물물교환 15회 진행"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.reward.crow-coins::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.reward.crow-coins::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-iliya-daily-barter.reward.crow-coins"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 까마귀 주화"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.reward.crow-coins::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.reward.crow-coins::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-iliya-daily-barter.reward.crow-coins"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 까마귀 주화"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.reward.deep-memory-glue::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.reward.deep-memory-glue::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-iliya-daily-barter.reward.deep-memory-glue"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 심해의 기억이 담긴 아교"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.reward.deep-memory-glue::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.reward.deep-memory-glue::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-iliya-daily-barter.reward.deep-memory-glue"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 심해의 기억이 담긴 아교"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.reward.enhanced-plywood::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.reward.enhanced-plywood::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-iliya-daily-barter.reward.enhanced-plywood"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 강화된 섬나무 증착합판"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.reward.enhanced-plywood::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.reward.enhanced-plywood::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-iliya-daily-barter.reward.enhanced-plywood"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 강화된 섬나무 증착합판"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.reward.parley-expert::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.reward.parley-expert::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-iliya-daily-barter.reward.parley-expert"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 콕스해적단의 유물(협상 상급)"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.reward.parley-expert::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.reward.parley-expert::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-iliya-daily-barter.reward.parley-expert"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 콕스해적단의 유물(협상 상급)"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.reward.pure-pearl::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.reward.pure-pearl::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-iliya-daily-barter.reward.pure-pearl"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 순수한 진주 결정"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.reward.pure-pearl::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.reward.pure-pearl::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-iliya-daily-barter.reward.pure-pearl"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 순수한 진주 결정"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.reward.pure-reef::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.reward.pure-reef::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-iliya-daily-barter.reward.pure-reef"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 순수한 암초 조각"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.reward.pure-reef::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.reward.pure-reef::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-iliya-daily-barter.reward.pure-reef"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 순수한 암초 조각"
- active: true
- is_active: true

### `ocean-iliya-daily-barter.evidence.schedule.reset::daily-weekly-reset-gm-2023`

- evidence_seed_key: "ocean-iliya-daily-barter.evidence.schedule.reset::daily-weekly-reset-gm-2023"
- source_id: "daily-weekly-reset-gm-2023"
- title: "검은사막이 처음인 모험가 여러분을 위해 준비한 A to Z!"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=10577"
- publisher: "Pearl Abyss"
- source_type: "official_gm"
- published_at: "2023-07-25"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "ocean-iliya-daily-barter.schedule.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일일 의뢰: 매일 00:00 KST 초기화"
- active: true
- is_active: true

### Historical / inactive evidence

- None
