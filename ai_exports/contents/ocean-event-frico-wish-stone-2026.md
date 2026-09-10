<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# [이벤트] 프리코의 항해 기원석 연계 의뢰

## Identity

- slug: "ocean-event-frico-wish-stone-2026"
- name_ko: "[이벤트] 프리코의 항해 기원석 연계 의뢰"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "벨리아→일리야 연계 의뢰로 프리코의 항해 기원석을 획득하는 2026 기간제 항해 이벤트."
- purpose: "항해·교역 경험치와 항해 숙련도 보조 효과를 받아 이벤트 기간 물물교환과 중범선 제작을 가속한다."

## Requirements

- None

## Steps

### `ocean-event-frico-wish-stone-2026.step.black-spirit`

- seed_key: "ocean-event-frico-wish-stone-2026.step.black-spirit"
- phase: "first_time"
- order_no: 1
- title: "심상치 않은 바다의 기운"
- description: "흑정령에게 의뢰를 받아 벨리아 선착장의 크루와에게 안내받는다."
- checkable: true

### `ocean-event-frico-wish-stone-2026.step.frico`

- seed_key: "ocean-event-frico-wish-stone-2026.step.frico"
- phase: "first_time"
- order_no: 2
- title: "뒤숭숭한 뱃사람들의 소문"
- description: "벨리아 크루와의 연계 의뢰를 받아 일리야 섬 프리코에게 이동해 완료한다."
- checkable: true

## Schedules

### `ocean-event-frico-wish-stone-2026.schedule.event-end`

- seed_key: "ocean-event-frico-wish-stone-2026.schedule.event-end"
- rule_type: "event_end"
- recurrence_type: "manual"
- weekday: null
- time_local: null
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "현재 진행 이벤트 공지 기준 2026-09-16 정기점검 전까지"

## Rewards

### `ocean-event-frico-wish-stone-2026.reward.wish-stone`

- seed_key: "ocean-event-frico-wish-stone-2026.reward.wish-stone"
- name: "[이벤트] 프리코의 항해 기원석"
- reward_type: "event_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: "이벤트 기간 물물교환/항해 시 모험가의 고서 슬롯에 장착."
- notes: "항해 경험치 +30%, 교역 경험치 +30%, 항해 숙련도 +100"
- order_no: 1

## Sections

### `ocean-event-frico-wish-stone-2026.section.effect`

- seed_key: "ocean-event-frico-wish-stone-2026.section.effect"
- section_type: "strategy"
- title: "기원석 효과"
- order_no: 1

#### body_markdown

모험가의 고서 슬롯에 장착하면 항해 경험치 획득량 +30%, 교역 경험치 획득량 +30%, 항해 숙련도 +100 효과를 받는다.

### `ocean-event-frico-wish-stone-2026.section.extension`

- seed_key: "ocean-event-frico-wish-stone-2026.section.extension"
- section_type: "notes"
- title: "종료일 연장 반영"
- order_no: 2

#### body_markdown

원 공지에는 9월 9일 종료로 안내된 구간이 있으나, 2026-09-02 현재 진행 이벤트 모아보기에서 대양 항해·교역 이벤트 종료가 9월 16일 정기점검 전으로 연장되어 있어 최신 공지를 우선한다.

## Related Contents

### `ocean-event-frico-wish-stone-2026.relation.carrack-advance`

- seed_key: "ocean-event-frico-wish-stone-2026.relation.carrack-advance"
- direction: "outgoing"
- relation_type: "project_link"
- content_slug: "carrack-advance"
- content_name_ko: "에페리아 중범선 : 점진"
- content_category: "ocean_project"
- note: "이벤트 기간 항해/교역 진행 가속"
- order_no: 1
- relative_path: "../contents/carrack-advance.md"

## Evidence and Sources

### Current evidence

### `ocean-event-frico-wish-stone-2026.evidence.purpose::ocean-event-2026-08-26`

- evidence_seed_key: "ocean-event-frico-wish-stone-2026.evidence.purpose::ocean-event-2026-08-26"
- source_id: "ocean-event-2026-08-26"
- title: "[항해&교역] 종합 선물 세트 도착 (feat. 치로 장비 제작 속도 UP)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16091"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-26"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "ocean-event-frico-wish-stone-2026"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "항해·교역 경험치와 항해 숙련도 보조 효과를 받아 이벤트 기간 물물교환과 중범선 제작을 가속한다."
- active: true
- is_active: true

### `ocean-event-frico-wish-stone-2026.evidence.summary::ocean-event-2026-08-26`

- evidence_seed_key: "ocean-event-frico-wish-stone-2026.evidence.summary::ocean-event-2026-08-26"
- source_id: "ocean-event-2026-08-26"
- title: "[항해&교역] 종합 선물 세트 도착 (feat. 치로 장비 제작 속도 UP)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16091"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-26"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "ocean-event-frico-wish-stone-2026"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "벨리아→일리야 연계 의뢰로 프리코의 항해 기원석을 획득하는 2026 기간제 항해 이벤트."
- active: true
- is_active: true

### `ocean-event-frico-wish-stone-2026.evidence.section.effect::ocean-event-2026-08-26`

- evidence_seed_key: "ocean-event-frico-wish-stone-2026.evidence.section.effect::ocean-event-2026-08-26"
- source_id: "ocean-event-2026-08-26"
- title: "[항해&교역] 종합 선물 세트 도착 (feat. 치로 장비 제작 속도 UP)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16091"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-26"
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "ocean-event-frico-wish-stone-2026.section.effect"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "기원석 효과"
- active: true
- is_active: true

### `ocean-event-frico-wish-stone-2026.evidence.section.extension::current-events-2026-09-02`

- evidence_seed_key: "ocean-event-frico-wish-stone-2026.evidence.section.extension::current-events-2026-09-02"
- source_id: "current-events-2026-09-02"
- title: "[진행중인 이벤트 모아보기]"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?groupContentNo=13733"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-09-02"
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "ocean-event-frico-wish-stone-2026.section.extension"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "9/2 최신 진행 이벤트에서 종료일 9/16로 연장 반영"
- active: true
- is_active: true

### `ocean-event-frico-wish-stone-2026.evidence.section.extension::ocean-event-2026-08-26`

- evidence_seed_key: "ocean-event-frico-wish-stone-2026.evidence.section.extension::ocean-event-2026-08-26"
- source_id: "ocean-event-2026-08-26"
- title: "[항해&교역] 종합 선물 세트 도착 (feat. 치로 장비 제작 속도 UP)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16091"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-26"
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "ocean-event-frico-wish-stone-2026.section.extension"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "9/2 최신 진행 이벤트에서 종료일 9/16로 연장 반영"
- active: true
- is_active: true

### `ocean-event-frico-wish-stone-2026.evidence.step.black-spirit::ocean-event-2026-08-26`

- evidence_seed_key: "ocean-event-frico-wish-stone-2026.evidence.step.black-spirit::ocean-event-2026-08-26"
- source_id: "ocean-event-2026-08-26"
- title: "[항해&교역] 종합 선물 세트 도착 (feat. 치로 장비 제작 속도 UP)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16091"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-26"
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "ocean-event-frico-wish-stone-2026.step.black-spirit"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "1단계 이벤트 의뢰"
- active: true
- is_active: true

### `ocean-event-frico-wish-stone-2026.evidence.step.frico::ocean-event-2026-08-26`

- evidence_seed_key: "ocean-event-frico-wish-stone-2026.evidence.step.frico::ocean-event-2026-08-26"
- source_id: "ocean-event-2026-08-26"
- title: "[항해&교역] 종합 선물 세트 도착 (feat. 치로 장비 제작 속도 UP)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16091"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-26"
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "ocean-event-frico-wish-stone-2026.step.frico"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2단계 이벤트 의뢰"
- active: true
- is_active: true

### `ocean-event-frico-wish-stone-2026.evidence.reward.wish-stone::ocean-event-2026-08-26`

- evidence_seed_key: "ocean-event-frico-wish-stone-2026.evidence.reward.wish-stone::ocean-event-2026-08-26"
- source_id: "ocean-event-2026-08-26"
- title: "[항해&교역] 종합 선물 세트 도착 (feat. 치로 장비 제작 속도 UP)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16091"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-26"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "ocean-event-frico-wish-stone-2026.reward.wish-stone"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "프리코의 항해 기원석 및 효과"
- active: true
- is_active: true

### `ocean-event-frico-wish-stone-2026.evidence.schedule.event-end::current-events-2026-09-02`

- evidence_seed_key: "ocean-event-frico-wish-stone-2026.evidence.schedule.event-end::current-events-2026-09-02"
- source_id: "current-events-2026-09-02"
- title: "[진행중인 이벤트 모아보기]"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?groupContentNo=13733"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-09-02"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "ocean-event-frico-wish-stone-2026.schedule.event-end"
- claim_key: "schedule.event_end"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "대양 항해·교역 이벤트 2026-09-16 정기점검 전 종료"
- active: true
- is_active: true

### Historical / inactive evidence

- None
