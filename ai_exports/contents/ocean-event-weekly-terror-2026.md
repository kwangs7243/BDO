<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# [이벤트][주간] 바다의 질서를 위협하는 공포

## Identity

- slug: "ocean-event-weekly-terror-2026"
- name_ko: "[이벤트][주간] 바다의 질서를 위협하는 공포"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "어린 해왕류 5마리 처치 후 기간제 항해 이벤트 보상을 받는 주간 의뢰."
- purpose: "이벤트 기간 중 중범선/선박 성장 자원을 추가 확보한다."

## Requirements

### `ocean-event-weekly-terror-2026.requirement.start-npc`

- seed_key: "ocean-event-weekly-terror-2026.requirement.start-npc"
- kind: "other"
- requirement_level: "required"
- title: "수주 NPC"
- description: "일리야 섬 물물교환원 프리코"
- structured_value: null

## Steps

### `ocean-event-weekly-terror-2026.step.complete-objective`

- seed_key: "ocean-event-weekly-terror-2026.step.complete-objective"
- phase: "repeat"
- order_no: 1
- title: "의뢰 목표 완료"
- description: "어린 해왕류 5마리 처치"
- checkable: false

## Schedules

### `ocean-event-weekly-terror-2026.schedule.event-end`

- seed_key: "ocean-event-weekly-terror-2026.schedule.event-end"
- rule_type: "event_end"
- recurrence_type: "manual"
- weekday: null
- time_local: null
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "2026-09-02 현재 진행 이벤트 공지 기준 9월 16일 정기점검 전 종료"

### `ocean-event-weekly-terror-2026.schedule.quest-reset`

- seed_key: "ocean-event-weekly-terror-2026.schedule.quest-reset"
- rule_type: "quest_reset"
- recurrence_type: "weekly"
- weekday: 3
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "주간 의뢰: 매주 목요일 00:00 KST 초기화"

## Rewards

### `ocean-event-weekly-terror-2026.reward.chiro-box`

- seed_key: "ocean-event-weekly-terror-2026.reward.chiro-box"
- name: "[이벤트] 치로의 선박 장비 재료 상자"
- reward_type: "quest_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "ocean-event-weekly-terror-2026.choice-1"
- recommendation: null
- notes: "난폭한 파도가 새겨진 합판 30 + 정교하게 다듬어진 지지대 30 + 파도의 흔적이 담긴 접착제 30"
- order_no: 1

### `ocean-event-weekly-terror-2026.reward.crow-coins`

- seed_key: "ocean-event-weekly-terror-2026.reward.crow-coins"
- name: "까마귀 주화"
- reward_type: "quest_reward"
- amount: 2000.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "ocean-event-weekly-terror-2026.choice-1"
- recommendation: "현재 중범선 : 점진 제작을 우선한다면 까마귀 주화 2,000개를 추천한다. 치로 재료는 중범선 이후 장비 단계용이다."
- notes: null
- order_no: 2

## Sections

### `ocean-event-weekly-terror-2026.section.prerequisite`

- seed_key: "ocean-event-weekly-terror-2026.section.prerequisite"
- section_type: "preparation"
- title: "선행 의뢰"
- order_no: 1

#### body_markdown

`[이벤트] 뒤숭숭한 뱃사람들의 소문` 완료 후 주간 의뢰를 진행할 수 있다.

## Related Contents

### `ocean-event-weekly-terror-2026.relation.carrack-advance`

- seed_key: "ocean-event-weekly-terror-2026.relation.carrack-advance"
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

### `ocean-event-weekly-terror-2026.evidence.purpose::current-events-2026-09-02`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.purpose::current-events-2026-09-02"
- source_id: "current-events-2026-09-02"
- title: "[진행중인 이벤트 모아보기]"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?groupContentNo=13733"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-09-02"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "ocean-event-weekly-terror-2026"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "이벤트 기간 중 중범선/선박 성장 자원을 추가 확보한다."
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.purpose::ocean-event-2026-08-26`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.purpose::ocean-event-2026-08-26"
- source_id: "ocean-event-2026-08-26"
- title: "[항해&교역] 종합 선물 세트 도착 (feat. 치로 장비 제작 속도 UP)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16091"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-26"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "ocean-event-weekly-terror-2026"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "이벤트 기간 중 중범선/선박 성장 자원을 추가 확보한다."
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.summary::current-events-2026-09-02`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.summary::current-events-2026-09-02"
- source_id: "current-events-2026-09-02"
- title: "[진행중인 이벤트 모아보기]"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?groupContentNo=13733"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-09-02"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "ocean-event-weekly-terror-2026"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "어린 해왕류 5마리 처치 후 기간제 항해 이벤트 보상을 받는 주간 의뢰."
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.summary::ocean-event-2026-08-26`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.summary::ocean-event-2026-08-26"
- source_id: "ocean-event-2026-08-26"
- title: "[항해&교역] 종합 선물 세트 도착 (feat. 치로 장비 제작 속도 UP)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16091"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-26"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "ocean-event-weekly-terror-2026"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "어린 해왕류 5마리 처치 후 기간제 항해 이벤트 보상을 받는 주간 의뢰."
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.relation.carrack-advance::carrack-guide`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.relation.carrack-advance::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "ocean-event-weekly-terror-2026.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.relation.carrack-advance::current-events-2026-09-02`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.relation.carrack-advance::current-events-2026-09-02"
- source_id: "current-events-2026-09-02"
- title: "[진행중인 이벤트 모아보기]"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?groupContentNo=13733"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-09-02"
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "ocean-event-weekly-terror-2026.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.relation.carrack-advance::ocean-event-2026-08-26`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.relation.carrack-advance::ocean-event-2026-08-26"
- source_id: "ocean-event-2026-08-26"
- title: "[항해&교역] 종합 선물 세트 도착 (feat. 치로 장비 제작 속도 UP)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16091"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-26"
- retrieved_at: null
- region: "KR"
- entity_type: "content_relation"
- entity_id: "ocean-event-weekly-terror-2026.relation.carrack-advance"
- claim_key: "relation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진/무역선 파란 장비 재료 획득처와 연결"
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.requirement.start-npc::current-events-2026-09-02`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.requirement.start-npc::current-events-2026-09-02"
- source_id: "current-events-2026-09-02"
- title: "[진행중인 이벤트 모아보기]"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?groupContentNo=13733"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-09-02"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ocean-event-weekly-terror-2026.requirement.start-npc"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "수주 NPC: 일리야 섬 물물교환원 프리코"
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.requirement.start-npc::ocean-event-2026-08-26`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.requirement.start-npc::ocean-event-2026-08-26"
- source_id: "ocean-event-2026-08-26"
- title: "[항해&교역] 종합 선물 세트 도착 (feat. 치로 장비 제작 속도 UP)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16091"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-26"
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ocean-event-weekly-terror-2026.requirement.start-npc"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "수주 NPC: 일리야 섬 물물교환원 프리코"
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.section.prerequisite::ocean-event-2026-08-26`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.section.prerequisite::ocean-event-2026-08-26"
- source_id: "ocean-event-2026-08-26"
- title: "[항해&교역] 종합 선물 세트 도착 (feat. 치로 장비 제작 속도 UP)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16091"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-26"
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "ocean-event-weekly-terror-2026.section.prerequisite"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "선행 의뢰"
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.step.objective::current-events-2026-09-02`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.step.objective::current-events-2026-09-02"
- source_id: "current-events-2026-09-02"
- title: "[진행중인 이벤트 모아보기]"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?groupContentNo=13733"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-09-02"
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "ocean-event-weekly-terror-2026.step.complete-objective"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "어린 해왕류 5마리 처치"
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.step.objective::ocean-event-2026-08-26`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.step.objective::ocean-event-2026-08-26"
- source_id: "ocean-event-2026-08-26"
- title: "[항해&교역] 종합 선물 세트 도착 (feat. 치로 장비 제작 속도 UP)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16091"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-26"
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "ocean-event-weekly-terror-2026.step.complete-objective"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "어린 해왕류 5마리 처치"
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.reward.chiro-box::current-events-2026-09-02`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.reward.chiro-box::current-events-2026-09-02"
- source_id: "current-events-2026-09-02"
- title: "[진행중인 이벤트 모아보기]"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?groupContentNo=13733"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-09-02"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-event-weekly-terror-2026.reward.chiro-box"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: [이벤트] 치로의 선박 장비 재료 상자"
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.reward.chiro-box::ocean-event-2026-08-26`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.reward.chiro-box::ocean-event-2026-08-26"
- source_id: "ocean-event-2026-08-26"
- title: "[항해&교역] 종합 선물 세트 도착 (feat. 치로 장비 제작 속도 UP)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16091"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-26"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-event-weekly-terror-2026.reward.chiro-box"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: [이벤트] 치로의 선박 장비 재료 상자"
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.reward.crow-coins.recommendation::carrack-guide`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.reward.crow-coins.recommendation::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-event-weekly-terror-2026.reward.crow-coins"
- claim_key: "recommendation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "현재 중범선 : 점진 제작을 우선한다면 까마귀 주화 2,000개를 추천한다. 치로 재료는 중범선 이후 장비 단계용이다."
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.reward.crow-coins.recommendation::ocean-event-2026-08-26`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.reward.crow-coins.recommendation::ocean-event-2026-08-26"
- source_id: "ocean-event-2026-08-26"
- title: "[항해&교역] 종합 선물 세트 도착 (feat. 치로 장비 제작 속도 UP)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16091"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-26"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-event-weekly-terror-2026.reward.crow-coins"
- claim_key: "recommendation"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "현재 중범선 : 점진 제작을 우선한다면 까마귀 주화 2,000개를 추천한다. 치로 재료는 중범선 이후 장비 단계용이다."
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.reward.crow-coins::current-events-2026-09-02`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.reward.crow-coins::current-events-2026-09-02"
- source_id: "current-events-2026-09-02"
- title: "[진행중인 이벤트 모아보기]"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?groupContentNo=13733"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-09-02"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-event-weekly-terror-2026.reward.crow-coins"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 까마귀 주화"
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.reward.crow-coins::ocean-event-2026-08-26`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.reward.crow-coins::ocean-event-2026-08-26"
- source_id: "ocean-event-2026-08-26"
- title: "[항해&교역] 종합 선물 세트 도착 (feat. 치로 장비 제작 속도 UP)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16091"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-26"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-event-weekly-terror-2026.reward.crow-coins"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "보상: 까마귀 주화"
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.schedule.event-end::current-events-2026-09-02`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.schedule.event-end::current-events-2026-09-02"
- source_id: "current-events-2026-09-02"
- title: "[진행중인 이벤트 모아보기]"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?groupContentNo=13733"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-09-02"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "ocean-event-weekly-terror-2026.schedule.event-end"
- claim_key: "schedule.event_end"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "이벤트 종료 2026-09-16 정기점검 전"
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.schedule.reset::daily-weekly-reset-gm-2023`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.schedule.reset::daily-weekly-reset-gm-2023"
- source_id: "daily-weekly-reset-gm-2023"
- title: "검은사막이 처음인 모험가 여러분을 위해 준비한 A to Z!"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=10577"
- publisher: "Pearl Abyss"
- source_type: "official_gm"
- published_at: "2023-07-25"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "ocean-event-weekly-terror-2026.schedule.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 의뢰: 매주 목요일 00:00 KST 초기화"
- active: true
- is_active: true

### `ocean-event-weekly-terror-2026.evidence.schedule.reset::ocean-event-2026-08-26`

- evidence_seed_key: "ocean-event-weekly-terror-2026.evidence.schedule.reset::ocean-event-2026-08-26"
- source_id: "ocean-event-2026-08-26"
- title: "[항해&교역] 종합 선물 세트 도착 (feat. 치로 장비 제작 속도 UP)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16091"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-26"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "ocean-event-weekly-terror-2026.schedule.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 의뢰: 매주 목요일 00:00 KST 초기화"
- active: true
- is_active: true

### Historical / inactive evidence

- None
