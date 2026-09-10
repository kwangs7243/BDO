<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 항해 스페셜 패스 (2026)

## Identity

- slug: "sailing-special-pass-2026"
- name_ko: "항해 스페셜 패스 (2026)"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "물물교환 1회당 1포인트를 쌓아 최대 400포인트까지 중범선 제작 지원 보상을 받는 2026 기간제 패스."
- purpose: "400회 물물교환을 진행하면서 중범선 제작 재료·까마귀 주화·파도의 블랙스톤을 대량 확보한다."

## Requirements

- None

## Steps

### `sailing-special-pass-2026.step.activate`

- seed_key: "sailing-special-pass-2026.step.activate"
- phase: "preparation"
- order_no: 1
- title: "패스 활성화"
- description: "항해 스페셜 패스를 사용해 추가 보상을 활성화한다."
- checkable: false

### `sailing-special-pass-2026.step.barter-400`

- seed_key: "sailing-special-pass-2026.step.barter-400"
- phase: "repeat"
- order_no: 2
- title: "물물교환 400회"
- description: "물물교환 1회마다 1포인트를 얻어 400포인트까지 진행한다."
- checkable: false

### `sailing-special-pass-2026.step.claim`

- seed_key: "sailing-special-pass-2026.step.claim"
- phase: "reward"
- order_no: 3
- title: "구간 보상 수령"
- description: "달성한 누적 포인트 구간의 보상을 패스 UI에서 수령한다."
- checkable: false

## Schedules

### `sailing-special-pass-2026.schedule.reward-end`

- seed_key: "sailing-special-pass-2026.schedule.reward-end"
- rule_type: "event_end"
- recurrence_type: "manual"
- weekday: null
- time_local: null
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "포인트 획득 및 보상 수령: 2026-09-22 정기점검 전까지"

### `sailing-special-pass-2026.schedule.sale-end`

- seed_key: "sailing-special-pass-2026.schedule.sale-end"
- rule_type: "event_end"
- recurrence_type: "manual"
- weekday: null
- time_local: null
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "패스 판매: 2026-09-16 정기점검 전까지"

## Rewards

### `sailing-special-pass-2026.reward.regular-box`

- seed_key: "sailing-special-pass-2026.reward.regular-box"
- name: "중범선 증축 지원 선택 상자"
- reward_type: "event_reward"
- amount: 20.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: "자연 수급 후 마지막 부족 재료에 맞춰 개봉하는 것을 권장."
- notes: "상자 1개당 두 선택 그룹에서 각각 1종 선택"
- order_no: 1

### `sailing-special-pass-2026.reward.fancy-box`

- seed_key: "sailing-special-pass-2026.reward.fancy-box"
- name: "화려한 중범선 증축 지원 선택 상자"
- reward_type: "event_reward"
- amount: 18.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: "점진 본체 및 파란 장비 최종 부족분에 맞춰 사용."
- notes: "전투 유물4 / 빛나는 코발트1 / 화려한 암염1 / 화려한 진주1 / 심해의 눈물1 중 택1"
- order_no: 2

### `sailing-special-pass-2026.reward.crow-coins`

- seed_key: "sailing-special-pass-2026.reward.crow-coins"
- name: "까마귀 주화"
- reward_type: "event_reward"
- amount: 10000.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: "선택상자와 자연 수급을 먼저 계산한 뒤 남은 병목에 사용."
- notes: null
- order_no: 3

### `sailing-special-pass-2026.reward.wave-black-stone`

- seed_key: "sailing-special-pass-2026.reward.wave-black-stone"
- name: "파도의 블랙스톤"
- reward_type: "event_reward"
- amount: 4000.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 4

## Sections

### `sailing-special-pass-2026.section.period`

- seed_key: "sailing-special-pass-2026.section.period"
- section_type: "overview"
- title: "진행 기간"
- order_no: 1

#### body_markdown

판매는 2026-09-16 정기점검 전까지, 포인트 획득 및 보상 수령은 2026-09-22 정기점검 전까지 가능하다.

### `sailing-special-pass-2026.section.regular-box-choices`

- seed_key: "sailing-special-pass-2026.section.regular-box-choices"
- section_type: "preparation"
- title: "일반 지원 선택 상자 구성"
- order_no: 2

#### body_markdown

중범선 증축 지원 선택 상자 1개는 두 선택 그룹에서 각각 1종을 고른다.

**그룹 1**
- 홍조빛 해저단괴 5
- 심해초 줄기 15
- 달의 핏줄이 새겨진 아마포 30
- 강화된 섬나무 증착합판 30
- 순수한 암초 조각 30
- 달의 비늘이 새겨진 합판 80

**그룹 2**
- 파도빛이 감도는 규격 각목 25
- 짙은 파도빛이 감도는 규격 각목 20
- 순수한 진주 결정 7
- 대양의 견고한 현철 15
- 콕스해적단의 유물(협상 하급) 10
- 콕스해적단의 유물(협상 상급) 5

### `sailing-special-pass-2026.section.opening-strategy`

- seed_key: "sailing-special-pass-2026.section.opening-strategy"
- section_type: "strategy"
- title: "점진 제작 중 개봉 원칙"
- order_no: 3

#### body_markdown

선택 상자를 먼저 전부 열지 말고, 일일·주간·재료 물물교환으로 자연 수급한 뒤 실제 부족량을 갱신한다. 그 다음 파란 무역선 장비 병목 → 점진 본체 병목 순으로 상자를 배분하고 까마귀 주화는 마지막 부족분 보충에 쓴다.

## Related Contents

### `sailing-special-pass-2026.relation.carrack-advance`

- seed_key: "sailing-special-pass-2026.relation.carrack-advance"
- direction: "outgoing"
- relation_type: "project_link"
- content_slug: "carrack-advance"
- content_name_ko: "에페리아 중범선 : 점진"
- content_category: "ocean_project"
- note: "중범선 제작 가속용 기간제 패스"
- order_no: 1
- relative_path: "../contents/carrack-advance.md"

## Evidence and Sources

### Current evidence

### `sailing-special-pass-2026.evidence.purpose::carrack-guide`

- evidence_seed_key: "sailing-special-pass-2026.evidence.purpose::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "sailing-special-pass-2026"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "400회 물물교환을 진행하면서 중범선 제작 재료·까마귀 주화·파도의 블랙스톤을 대량 확보한다."
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.purpose::sailing-special-pass-2026`

- evidence_seed_key: "sailing-special-pass-2026.evidence.purpose::sailing-special-pass-2026"
- source_id: "sailing-special-pass-2026"
- title: "중범선 제작 속도 UP, 항해 스페셜 패스"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=16054"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-19"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "sailing-special-pass-2026"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "400회 물물교환을 진행하면서 중범선 제작 재료·까마귀 주화·파도의 블랙스톤을 대량 확보한다."
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.summary::sailing-special-pass-2026`

- evidence_seed_key: "sailing-special-pass-2026.evidence.summary::sailing-special-pass-2026"
- source_id: "sailing-special-pass-2026"
- title: "중범선 제작 속도 UP, 항해 스페셜 패스"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=16054"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-19"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "sailing-special-pass-2026"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "물물교환 1회당 1포인트를 쌓아 최대 400포인트까지 중범선 제작 지원 보상을 받는 2026 기간제 패스."
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.summary::sailing-special-pass-shop-2026`

- evidence_seed_key: "sailing-special-pass-2026.evidence.summary::sailing-special-pass-shop-2026"
- source_id: "sailing-special-pass-shop-2026"
- title: "8월 19일(수) 펄 상점 패키지 및 신규 상품 소개"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16066"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-19"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "sailing-special-pass-2026"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "물물교환 1회당 1포인트를 쌓아 최대 400포인트까지 중범선 제작 지원 보상을 받는 2026 기간제 패스."
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.section.strategy::carrack-guide`

- evidence_seed_key: "sailing-special-pass-2026.evidence.section.strategy::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "sailing-special-pass-2026.section.opening-strategy"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진 제작 요구량과 일/주간 수급원을 바탕으로 한 사용자 목표별 운영 추천"
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.section.strategy::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "sailing-special-pass-2026.evidence.section.strategy::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "sailing-special-pass-2026.section.opening-strategy"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진 제작 요구량과 일/주간 수급원을 바탕으로 한 사용자 목표별 운영 추천"
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.section.strategy::sailing-special-pass-2026`

- evidence_seed_key: "sailing-special-pass-2026.evidence.section.strategy::sailing-special-pass-2026"
- source_id: "sailing-special-pass-2026"
- title: "중범선 제작 속도 UP, 항해 스페셜 패스"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=16054"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-19"
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "sailing-special-pass-2026.section.opening-strategy"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진 제작 요구량과 일/주간 수급원을 바탕으로 한 사용자 목표별 운영 추천"
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.section.regular-box::sailing-special-pass-2026`

- evidence_seed_key: "sailing-special-pass-2026.evidence.section.regular-box::sailing-special-pass-2026"
- source_id: "sailing-special-pass-2026"
- title: "중범선 제작 속도 UP, 항해 스페셜 패스"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=16054"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-19"
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "sailing-special-pass-2026.section.regular-box-choices"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일반 지원 선택 상자 구성"
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.section.regular-box::sailing-special-pass-shop-2026`

- evidence_seed_key: "sailing-special-pass-2026.evidence.section.regular-box::sailing-special-pass-shop-2026"
- source_id: "sailing-special-pass-shop-2026"
- title: "8월 19일(수) 펄 상점 패키지 및 신규 상품 소개"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16066"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-19"
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "sailing-special-pass-2026.section.regular-box-choices"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일반 지원 선택 상자 구성"
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.step.barter-400::sailing-special-pass-2026`

- evidence_seed_key: "sailing-special-pass-2026.evidence.step.barter-400::sailing-special-pass-2026"
- source_id: "sailing-special-pass-2026"
- title: "중범선 제작 속도 UP, 항해 스페셜 패스"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=16054"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-19"
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-special-pass-2026.step.barter-400"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "물물교환 1회=1포인트, 400포인트 목표"
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.reward.crow-coins::sailing-special-pass-2026`

- evidence_seed_key: "sailing-special-pass-2026.evidence.reward.crow-coins::sailing-special-pass-2026"
- source_id: "sailing-special-pass-2026"
- title: "중범선 제작 속도 UP, 항해 스페셜 패스"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=16054"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-19"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "sailing-special-pass-2026.reward.crow-coins"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "까마귀 주화 총 10,000개"
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.reward.fancy-box::sailing-special-pass-2026`

- evidence_seed_key: "sailing-special-pass-2026.evidence.reward.fancy-box::sailing-special-pass-2026"
- source_id: "sailing-special-pass-2026"
- title: "중범선 제작 속도 UP, 항해 스페셜 패스"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=16054"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-19"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "sailing-special-pass-2026.reward.fancy-box"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "화려한 지원 선택 상자 총 18개"
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.reward.fancy-box::sailing-special-pass-shop-2026`

- evidence_seed_key: "sailing-special-pass-2026.evidence.reward.fancy-box::sailing-special-pass-shop-2026"
- source_id: "sailing-special-pass-shop-2026"
- title: "8월 19일(수) 펄 상점 패키지 및 신규 상품 소개"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16066"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-19"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "sailing-special-pass-2026.reward.fancy-box"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "화려한 지원 선택 상자 총 18개"
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.reward.regular-box::sailing-special-pass-2026`

- evidence_seed_key: "sailing-special-pass-2026.evidence.reward.regular-box::sailing-special-pass-2026"
- source_id: "sailing-special-pass-2026"
- title: "중범선 제작 속도 UP, 항해 스페셜 패스"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=16054"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-19"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "sailing-special-pass-2026.reward.regular-box"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일반 지원 선택 상자 총 20개"
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.reward.regular-box::sailing-special-pass-shop-2026`

- evidence_seed_key: "sailing-special-pass-2026.evidence.reward.regular-box::sailing-special-pass-shop-2026"
- source_id: "sailing-special-pass-shop-2026"
- title: "8월 19일(수) 펄 상점 패키지 및 신규 상품 소개"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16066"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-19"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "sailing-special-pass-2026.reward.regular-box"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일반 지원 선택 상자 총 20개"
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.reward.wave-black-stone::sailing-special-pass-2026`

- evidence_seed_key: "sailing-special-pass-2026.evidence.reward.wave-black-stone::sailing-special-pass-2026"
- source_id: "sailing-special-pass-2026"
- title: "중범선 제작 속도 UP, 항해 스페셜 패스"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=16054"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-19"
- retrieved_at: null
- region: "KR"
- entity_type: "reward"
- entity_id: "sailing-special-pass-2026.reward.wave-black-stone"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "파도의 블랙스톤 총 4,000개"
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.schedule.reward-end::current-events-2026-09-02`

- evidence_seed_key: "sailing-special-pass-2026.evidence.schedule.reward-end::current-events-2026-09-02"
- source_id: "current-events-2026-09-02"
- title: "[진행중인 이벤트 모아보기]"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?groupContentNo=13733"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-09-02"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "sailing-special-pass-2026.schedule.reward-end"
- claim_key: "schedule.event_end"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "포인트/보상 2026-09-22 정기점검 전"
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.schedule.reward-end::sailing-special-pass-2026`

- evidence_seed_key: "sailing-special-pass-2026.evidence.schedule.reward-end::sailing-special-pass-2026"
- source_id: "sailing-special-pass-2026"
- title: "중범선 제작 속도 UP, 항해 스페셜 패스"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=16054"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-19"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "sailing-special-pass-2026.schedule.reward-end"
- claim_key: "schedule.event_end"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "포인트/보상 2026-09-22 정기점검 전"
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.schedule.sale-end::current-events-2026-09-02`

- evidence_seed_key: "sailing-special-pass-2026.evidence.schedule.sale-end::current-events-2026-09-02"
- source_id: "current-events-2026-09-02"
- title: "[진행중인 이벤트 모아보기]"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?groupContentNo=13733"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-09-02"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "sailing-special-pass-2026.schedule.sale-end"
- claim_key: "schedule.event_end"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "판매 2026-09-16 정기점검 전"
- active: true
- is_active: true

### `sailing-special-pass-2026.evidence.schedule.sale-end::sailing-special-pass-shop-2026`

- evidence_seed_key: "sailing-special-pass-2026.evidence.schedule.sale-end::sailing-special-pass-shop-2026"
- source_id: "sailing-special-pass-shop-2026"
- title: "8월 19일(수) 펄 상점 패키지 및 신규 상품 소개"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16066"
- publisher: "Pearl Abyss"
- source_type: "official_forum"
- published_at: "2026-08-19"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "sailing-special-pass-2026.schedule.sale-end"
- claim_key: "schedule.event_end"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "판매 2026-09-16 정기점검 전"
- active: true
- is_active: true

### Historical / inactive evidence

- None
