<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 오네트·오도어 주간 재료 의뢰

## Identity

- slug: "infinite-potion-weeklies"
- name_ko: "오네트·오도어 주간 재료 의뢰"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: "solo"
- difficulty: null

## Overview

- summary: "정령수 재료 주간 의뢰 6종을 모두 수주·완료할 수 있으며 목요일 00:00에 초기화된다."
- purpose: "오네트·오도어의 정령수 제작 재료 6종을 주간 의뢰로 모은다."

## Requirements

### `infinite-potion-weeklies.availability`

- seed_key: "infinite-potion-weeklies.availability"
- kind: "other"
- requirement_level: "required"
- title: "6종 모두 가능"
- description: "과거 택 1 구조가 폐지되어 6종 주간 의뢰를 모두 수주·완료할 수 있다."
- structured_value:

```json
{
  "all_available": true,
  "choose_only_one": false,
  "quest_count": 6
}
```

## Steps

### `infinite-potion-weeklies.valtara`

- seed_key: "infinite-potion-weeklies.valtara"
- phase: "repeat"
- order_no: 1
- title: "[주간] 발타라의 추억"
- description: "나반 초원 몬스터 250마리 및 부드러운 페리의 깃털 250개"
- checkable: true

### `infinite-potion-weeklies.clear-bell`

- seed_key: "infinite-potion-weeklies.clear-bell"
- phase: "repeat"
- order_no: 2
- title: "[주간] 청명한 방울"
- description: "숲 로나로스 1,000마리"
- checkable: true

### `infinite-potion-weeklies.narc`

- seed_key: "infinite-potion-weeklies.narc"
- phase: "repeat"
- order_no: 3
- title: "[주간] 나크의 위로"
- description: "만샤움 1,000마리"
- checkable: true

### `infinite-potion-weeklies.katzvariak`

- seed_key: "infinite-potion-weeklies.katzvariak"
- phase: "repeat"
- order_no: 4
- title: "[주간] 카츠바리악의 맹독"
- description: "트쉬라 폐허 1,500마리"
- checkable: true

### `infinite-potion-weeklies.red-wolf`

- seed_key: "infinite-potion-weeklies.red-wolf"
- phase: "repeat"
- order_no: 5
- title: "[주간] 붉은 늑대의 맹세"
- description: "가크툼 1,500마리"
- checkable: true

### `infinite-potion-weeklies.dragon-fang`

- seed_key: "infinite-potion-weeklies.dragon-fang"
- phase: "repeat"
- order_no: 6
- title: "[주간] 용의 이빨"
- description: "셰레칸의 묘 1,000마리"
- checkable: true

## Schedules

### `infinite-potion-weeklies.quest-reset`

- seed_key: "infinite-potion-weeklies.quest-reset"
- rule_type: "quest_reset"
- recurrence_type: "weekly"
- weekday: 3
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "6종 주간 의뢰 초기화: 목요일 00:00"

## Rewards

### `infinite-potion-weeklies.valtara-material`

- seed_key: "infinite-potion-weeklies.valtara-material"
- name: "발타라의 추억"
- reward_type: "weekly_material"
- amount: 5.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 1

### `infinite-potion-weeklies.valtara-cp`

- seed_key: "infinite-potion-weeklies.valtara-cp"
- name: "공헌도 EXP"
- reward_type: "contribution_exp"
- amount: 300.0
- min_amount: null
- max_amount: null
- unit: "EXP"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 2

### `infinite-potion-weeklies.clear-bell-material`

- seed_key: "infinite-potion-weeklies.clear-bell-material"
- name: "청명한 방울"
- reward_type: "weekly_material"
- amount: 5.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 3

### `infinite-potion-weeklies.clear-bell-cp`

- seed_key: "infinite-potion-weeklies.clear-bell-cp"
- name: "공헌도 EXP"
- reward_type: "contribution_exp"
- amount: 300.0
- min_amount: null
- max_amount: null
- unit: "EXP"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 4

### `infinite-potion-weeklies.narc-material`

- seed_key: "infinite-potion-weeklies.narc-material"
- name: "나크의 위로"
- reward_type: "weekly_material"
- amount: 5.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 5

### `infinite-potion-weeklies.narc-cp`

- seed_key: "infinite-potion-weeklies.narc-cp"
- name: "공헌도 EXP"
- reward_type: "contribution_exp"
- amount: 300.0
- min_amount: null
- max_amount: null
- unit: "EXP"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 6

### `infinite-potion-weeklies.katzvariak-material`

- seed_key: "infinite-potion-weeklies.katzvariak-material"
- name: "카츠바리악의 맹독"
- reward_type: "weekly_material"
- amount: 5.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 7

### `infinite-potion-weeklies.katzvariak-cp`

- seed_key: "infinite-potion-weeklies.katzvariak-cp"
- name: "공헌도 EXP"
- reward_type: "contribution_exp"
- amount: 300.0
- min_amount: null
- max_amount: null
- unit: "EXP"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 8

### `infinite-potion-weeklies.red-wolf-material`

- seed_key: "infinite-potion-weeklies.red-wolf-material"
- name: "붉은 늑대의 맹세"
- reward_type: "weekly_material"
- amount: 5.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 9

### `infinite-potion-weeklies.red-wolf-cp`

- seed_key: "infinite-potion-weeklies.red-wolf-cp"
- name: "공헌도 EXP"
- reward_type: "contribution_exp"
- amount: 300.0
- min_amount: null
- max_amount: null
- unit: "EXP"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 10

### `infinite-potion-weeklies.dragon-fang-material`

- seed_key: "infinite-potion-weeklies.dragon-fang-material"
- name: "용의 이빨"
- reward_type: "weekly_material"
- amount: 5.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 11

### `infinite-potion-weeklies.dragon-fang-cp`

- seed_key: "infinite-potion-weeklies.dragon-fang-cp"
- name: "공헌도 EXP"
- reward_type: "contribution_exp"
- amount: 300.0
- min_amount: null
- max_amount: null
- unit: "EXP"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 12

## Sections

### `infinite-potion-weeklies.valtara-section`

- seed_key: "infinite-potion-weeklies.valtara-section"
- section_type: "overview"
- title: "[주간] 발타라의 추억"
- order_no: 1

#### body_markdown

목표: 나반 초원 몬스터 250마리 및 부드러운 페리의 깃털 250개

보상: 발타라의 추억 5개, 공헌도 EXP 300

### `infinite-potion-weeklies.clear-bell-section`

- seed_key: "infinite-potion-weeklies.clear-bell-section"
- section_type: "overview"
- title: "[주간] 청명한 방울"
- order_no: 2

#### body_markdown

목표: 숲 로나로스 1,000마리

보상: 청명한 방울 5개, 공헌도 EXP 300

### `infinite-potion-weeklies.narc-section`

- seed_key: "infinite-potion-weeklies.narc-section"
- section_type: "overview"
- title: "[주간] 나크의 위로"
- order_no: 3

#### body_markdown

목표: 만샤움 1,000마리

보상: 나크의 위로 5개, 공헌도 EXP 300

### `infinite-potion-weeklies.katzvariak-section`

- seed_key: "infinite-potion-weeklies.katzvariak-section"
- section_type: "overview"
- title: "[주간] 카츠바리악의 맹독"
- order_no: 4

#### body_markdown

목표: 트쉬라 폐허 1,500마리

보상: 카츠바리악의 맹독 5개, 공헌도 EXP 300

### `infinite-potion-weeklies.red-wolf-section`

- seed_key: "infinite-potion-weeklies.red-wolf-section"
- section_type: "overview"
- title: "[주간] 붉은 늑대의 맹세"
- order_no: 5

#### body_markdown

목표: 가크툼 1,500마리

보상: 붉은 늑대의 맹세 5개, 공헌도 EXP 300

### `infinite-potion-weeklies.dragon-fang-section`

- seed_key: "infinite-potion-weeklies.dragon-fang-section"
- section_type: "overview"
- title: "[주간] 용의 이빨"
- order_no: 6

#### body_markdown

목표: 셰레칸의 묘 1,000마리

보상: 용의 이빨 5개, 공헌도 EXP 300

## Related Contents

- None

## Evidence and Sources

### Current evidence

### `infinite-potion-weeklies.summary::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.summary::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "infinite-potion-weeklies"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "6종 모두 가능 및 최신 목표"
- active: true
- is_active: true

### `infinite-potion-weeklies.requirement.availability::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.requirement.availability::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "infinite-potion-weeklies.availability"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "택 1 폐지, 6종 모두 가능"
- active: true
- is_active: true

### `infinite-potion-weeklies.step.clear-bell::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.step.clear-bell::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "infinite-potion-weeklies.clear-bell"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "청명한 방울 최신 목표: 숲 로나로스 1,000마리"
- active: true
- is_active: true

### `infinite-potion-weeklies.step.dragon-fang::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.step.dragon-fang::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "infinite-potion-weeklies.dragon-fang"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "용의 이빨 최신 목표: 셰레칸의 묘 1,000마리"
- active: true
- is_active: true

### `infinite-potion-weeklies.step.katzvariak::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.step.katzvariak::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "infinite-potion-weeklies.katzvariak"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "카츠바리악의 맹독 최신 목표: 트쉬라 폐허 1,500마리"
- active: true
- is_active: true

### `infinite-potion-weeklies.step.narc::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.step.narc::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "infinite-potion-weeklies.narc"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "나크의 위로 최신 목표: 만샤움 1,000마리"
- active: true
- is_active: true

### `infinite-potion-weeklies.step.red-wolf::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.step.red-wolf::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "infinite-potion-weeklies.red-wolf"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "붉은 늑대의 맹세 최신 목표: 가크툼 1,500마리"
- active: true
- is_active: true

### `infinite-potion-weeklies.step.valtara::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.step.valtara::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "infinite-potion-weeklies.valtara"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "발타라의 추억 최신 목표: 나반 초원 몬스터 250마리 및 부드러운 페리의 깃털 250개"
- active: true
- is_active: true

### `infinite-potion-weeklies.reward.clear-bell-cp::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.reward.clear-bell-cp::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "infinite-potion-weeklies.clear-bell-cp"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "공헌도 EXP 300"
- active: true
- is_active: true

### `infinite-potion-weeklies.reward.clear-bell-material::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.reward.clear-bell-material::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "infinite-potion-weeklies.clear-bell-material"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "청명한 방울 5개"
- active: true
- is_active: true

### `infinite-potion-weeklies.reward.dragon-fang-cp::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.reward.dragon-fang-cp::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "infinite-potion-weeklies.dragon-fang-cp"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "공헌도 EXP 300"
- active: true
- is_active: true

### `infinite-potion-weeklies.reward.dragon-fang-material::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.reward.dragon-fang-material::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "infinite-potion-weeklies.dragon-fang-material"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "용의 이빨 5개"
- active: true
- is_active: true

### `infinite-potion-weeklies.reward.katzvariak-cp::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.reward.katzvariak-cp::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "infinite-potion-weeklies.katzvariak-cp"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "공헌도 EXP 300"
- active: true
- is_active: true

### `infinite-potion-weeklies.reward.katzvariak-material::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.reward.katzvariak-material::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "infinite-potion-weeklies.katzvariak-material"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "카츠바리악의 맹독 5개"
- active: true
- is_active: true

### `infinite-potion-weeklies.reward.narc-cp::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.reward.narc-cp::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "infinite-potion-weeklies.narc-cp"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "공헌도 EXP 300"
- active: true
- is_active: true

### `infinite-potion-weeklies.reward.narc-material::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.reward.narc-material::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "infinite-potion-weeklies.narc-material"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "나크의 위로 5개"
- active: true
- is_active: true

### `infinite-potion-weeklies.reward.red-wolf-cp::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.reward.red-wolf-cp::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "infinite-potion-weeklies.red-wolf-cp"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "공헌도 EXP 300"
- active: true
- is_active: true

### `infinite-potion-weeklies.reward.red-wolf-material::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.reward.red-wolf-material::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "infinite-potion-weeklies.red-wolf-material"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "붉은 늑대의 맹세 5개"
- active: true
- is_active: true

### `infinite-potion-weeklies.reward.valtara-cp::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.reward.valtara-cp::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "infinite-potion-weeklies.valtara-cp"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "공헌도 EXP 300"
- active: true
- is_active: true

### `infinite-potion-weeklies.reward.valtara-material::infinite-potion-weekly-2024-09-11`

- evidence_seed_key: "infinite-potion-weeklies.reward.valtara-material::infinite-potion-weekly-2024-09-11"
- source_id: "infinite-potion-weekly-2024-09-11"
- title: "9월 11일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12824"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-09-11"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "infinite-potion-weeklies.valtara-material"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "발타라의 추억 5개"
- active: true
- is_active: true

### `infinite-potion-weeklies.schedule.quest-reset::weekly-reset-2021`

- evidence_seed_key: "infinite-potion-weeklies.schedule.quest-reset::weekly-reset-2021"
- source_id: "weekly-reset-2021"
- title: "7월 28일 (수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=6125"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "infinite-potion-weeklies.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "목요일 00:00"
- active: true
- is_active: true

### Historical / inactive evidence

- None
