<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 꿈결 환상마 재료 루틴

## Identity

- slug: "dream-horse-material-routines"
- name_ko: "꿈결 환상마 재료 루틴"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- party_type: "solo"
- difficulty: null

## Overview

- summary: "고비 뿌리와 몽상의 깃털을 얻는 상시 주간·일일 조련 루틴이며, 남는 고비 뿌리는 준마 훈련 재료로 교환할 수 있다. 이벤트 추가 보상은 포함하지 않는다."
- purpose: "꿈결 환상마 몽상 재료를 모으고, 몽상 후 남는 고비 뿌리의 상시 사용처를 확인한다."

## Requirements

### `dream-horse-material-routines.fern-weekly-choice`

- seed_key: "dream-horse-material-routines.fern-weekly-choice"
- kind: "quest"
- requirement_level: "optional"
- title: "고비 뿌리 주간 택 1"
- description: "[주간] 바람을 뚫고 달려라 또는 [주간][조련] 말 포획하기 중 하나를 완료한다. 두 의뢰는 서로 배타적이다."
- structured_value:

```json
{
  "mutually_exclusive": true,
  "quests": [
    "[주간] 바람을 뚫고 달려라",
    "[주간][조련] 말 포획하기"
  ],
  "total_reward": 50
}
```

### `dream-horse-material-routines.feather-weekly`

- seed_key: "dream-horse-material-routines.feather-weekly"
- kind: "quest"
- requirement_level: "optional"
- title: "몽상의 깃털 주간"
- description: "[주간] 나도 날개를 가지고 싶어를 완료해 몽상의 깃털 2개를 획득한다."
- structured_value:

```json
{
  "reward_amount": 2
}
```

### `dream-horse-material-routines.support-choice`

- seed_key: "dream-horse-material-routines.support-choice"
- kind: "item"
- requirement_level: "optional"
- title: "와프라/리아나 지원 주간"
- description: "크로그달로의 근원석 지원 또는 당근 콘피테 지원 중 현재 가이드의 선택 구조로 몽상의 깃털 2개를 획득한다."
- structured_value:

```json
{
  "choices": [
    "크로그달로의 근원석",
    "당근 콘피테"
  ],
  "reward_amount": 2
}
```

### `dream-horse-material-routines.daily-fern`

- seed_key: "dream-horse-material-routines.daily-fern"
- kind: "quest"
- requirement_level: "optional"
- title: "조련 등급별 일일 의뢰"
- description: "조련 등급별 일일 의뢰를 통해 고비 뿌리를 획득한다. 등급별 수량은 이번 seed에서 확정하지 않는다."
- structured_value:

```json
{
  "amount_by_rank": null,
  "recurrence": "daily"
}
```

### `dream-horse-material-routines.fern-training-material-exchange`

- seed_key: "dream-horse-material-routines.fern-training-material-exchange"
- kind: "item"
- requirement_level: "optional"
- title: "남는 고비 뿌리 교환"
- description: "꿈결 환상마를 모두 보유해 더 이상 몽상을 시도하지 않는 경우, 와프라에게 고비 뿌리 3개를 준마 훈련 재료 1개로 교환할 수 있다."
- structured_value:

```json
{
  "choose_one": [
    {
      "amount": 1,
      "item": "돌꼬리 여물"
    },
    {
      "amount": 1,
      "item": "바람결 소라해초"
    },
    {
      "amount": 1,
      "item": "짙푸른 발굽뿌리"
    }
  ],
  "condition": "mythical_dream_horse_material_no_longer_needed",
  "input": {
    "amount": 3,
    "item": "고비 뿌리"
  },
  "knowledge_role": "fact",
  "npc": "와프라"
}
```

## Steps

### `dream-horse-material-routines.capture-horse`

- seed_key: "dream-horse-material-routines.capture-horse"
- phase: "repeat"
- order_no: 1
- title: "야생마 포획 주간 택 1"
- description: "고비 뿌리 주간 의뢰 두 종류 중 하나를 골라 야생마를 포획한다."
- checkable: true

### `dream-horse-material-routines.feather-weekly-step`

- seed_key: "dream-horse-material-routines.feather-weekly-step"
- phase: "repeat"
- order_no: 2
- title: "몽상의 깃털 주간 의뢰"
- description: "상시 주간 의뢰와 지원 선택 의뢰를 확인한다."
- checkable: true

### `dream-horse-material-routines.daily-step`

- seed_key: "dream-horse-material-routines.daily-step"
- phase: "repeat"
- order_no: 3
- title: "고비 뿌리 일일 의뢰"
- description: "자신의 조련 등급에 해당하는 일일 의뢰를 진행한다."
- checkable: true

## Schedules

### `dream-horse-material-routines.daily-reset`

- seed_key: "dream-horse-material-routines.daily-reset"
- rule_type: "quest_reset"
- recurrence_type: "daily"
- weekday: null
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "조련 등급별 일일 의뢰: 매일 00:00"

### `dream-horse-material-routines.weekly-reset`

- seed_key: "dream-horse-material-routines.weekly-reset"
- rule_type: "quest_reset"
- recurrence_type: "weekly"
- weekday: 3
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "상시 주간 조련 의뢰: 목요일 00:00"

## Rewards

### `dream-horse-material-routines.fern-root-50`

- seed_key: "dream-horse-material-routines.fern-root-50"
- name: "고비 뿌리"
- reward_type: "weekly_material"
- amount: 50.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "서로 배타적인 두 주간 의뢰 중 하나의 보상; 합계 100개 아님"
- order_no: 1

### `dream-horse-material-routines.feather-2`

- seed_key: "dream-horse-material-routines.feather-2"
- name: "몽상의 깃털"
- reward_type: "weekly_material"
- amount: 2.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "[주간] 나도 날개를 가지고 싶어"
- order_no: 2

### `dream-horse-material-routines.support-feather-2`

- seed_key: "dream-horse-material-routines.support-feather-2"
- name: "몽상의 깃털"
- reward_type: "weekly_material"
- amount: 2.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "support-material"
- recommendation: null
- notes: "와프라/리아나 지원 선택 의뢰"
- order_no: 3

## Sections

### `dream-horse-material-routines.event-exclusion`

- seed_key: "dream-horse-material-routines.event-exclusion"
- section_type: "notes"
- title: "이벤트 보상 제외"
- order_no: 1

#### body_markdown

이벤트 추가 고비 뿌리·몽상의 깃털 및 조련 핫타임은 상시 보상에 포함하지 않는다.

## Related Contents

### `dream-horse-awakening.materials`

- seed_key: "dream-horse-awakening.materials"
- direction: "incoming"
- relation_type: "related"
- content_slug: "dream-horse-awakening"
- content_name_ko: "환상마 각성"
- content_category: "life"
- note: "환상마 훈련 재료 루틴과 연결된다."
- order_no: 1
- relative_path: "../contents/dream-horse-awakening.md"
### `horse-imperial-delivery.dream-materials`

- seed_key: "horse-imperial-delivery.dream-materials"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "horse-imperial-delivery"
- content_name_ko: "말 황실 납품"
- content_category: "life"
- note: "망념의 꽃은 환상마·꿈결 환상마 재료 흐름과 연결된다."
- order_no: 1
- relative_path: "../contents/horse-imperial-delivery.md"
### `mythical-dream-horse.materials`

- seed_key: "mythical-dream-horse.materials"
- direction: "incoming"
- relation_type: "related"
- content_slug: "mythical-dream-horse"
- content_name_ko: "꿈결 환상마"
- content_category: "life"
- note: "꿈을 부르는 향로 재료 루틴과 연결된다."
- order_no: 1
- relative_path: "../contents/mythical-dream-horse.md"
### `life-family-levels.training-routine`

- seed_key: "life-family-levels.training-routine"
- direction: "incoming"
- relation_type: "related"
- content_slug: "life-family-levels"
- content_name_ko: "가문 통합 생활 레벨"
- content_category: "life"
- note: "가문 통합 조련 레벨은 기존 조련 반복 콘텐츠의 공통 기반이다."
- order_no: 2
- relative_path: "../contents/life-family-levels.md"
### `training-onboarding-strategy.material-routines`

- seed_key: "training-onboarding-strategy.material-routines"
- direction: "incoming"
- relation_type: "related"
- content_slug: "training-onboarding-strategy"
- content_name_ko: "조련 입문 운영 전략"
- content_category: "life"
- note: "상위 말 재료 반복 루틴과 고비 뿌리 사용처"
- order_no: 10
- relative_path: "../contents/training-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `dream-horse-material-routines.summary::mythical-horse-guide`

- evidence_seed_key: "dream-horse-material-routines.summary::mythical-horse-guide"
- source_id: "mythical-horse-guide"
- title: "꿈결 환상마(몽상)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=355"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "dream-horse-material-routines"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: "상시 주간·일일 재료 루틴과 남는 고비 뿌리 교환"
- active: true
- is_active: true

### `dream-horse-material-routines.summary::mythical-horse-update-2023-07-12`

- evidence_seed_key: "dream-horse-material-routines.summary::mythical-horse-update-2023-07-12"
- source_id: "mythical-horse-update-2023-07-12"
- title: "7월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=10666"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-07-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "dream-horse-material-routines"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: "상시 주간·일일 재료 루틴과 남는 고비 뿌리 교환"
- active: true
- is_active: true

### `dream-horse-material-routines.summary::processing-mass-recipes-2026-07-22`

- evidence_seed_key: "dream-horse-material-routines.summary::processing-mass-recipes-2026-07-22"
- source_id: "processing-mass-recipes-2026-07-22"
- title: "7월 22일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Notice/Detail?groupContentNo=15905&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-22"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "dream-horse-material-routines"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: "상시 주간·일일 재료 루틴과 남는 고비 뿌리 교환"
- active: true
- is_active: true

### `dream-horse-material-routines.requirement.daily::mythical-horse-guide`

- evidence_seed_key: "dream-horse-material-routines.requirement.daily::mythical-horse-guide"
- source_id: "mythical-horse-guide"
- title: "꿈결 환상마(몽상)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=355"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "dream-horse-material-routines.daily-fern"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "등급별 일일 고비 뿌리 경로, 수량 미확정"
- active: true
- is_active: true

### `dream-horse-material-routines.requirement.feather::mythical-horse-guide`

- evidence_seed_key: "dream-horse-material-routines.requirement.feather::mythical-horse-guide"
- source_id: "mythical-horse-guide"
- title: "꿈결 환상마(몽상)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=355"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "dream-horse-material-routines.feather-weekly"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "몽상의 깃털 2개"
- active: true
- is_active: true

### `dream-horse-material-routines.requirement.fern-training-material-exchange::processing-mass-recipes-2026-07-22`

- evidence_seed_key: "dream-horse-material-routines.requirement.fern-training-material-exchange::processing-mass-recipes-2026-07-22"
- source_id: "processing-mass-recipes-2026-07-22"
- title: "7월 22일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Notice/Detail?groupContentNo=15905&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-22"
- retrieved_at: "2026-09-06T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "dream-horse-material-routines.fern-training-material-exchange"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: "고비 뿌리 3개를 준마 훈련 재료 1개로 선택 교환"
- active: true
- is_active: true

### `dream-horse-material-routines.requirement.fern-choice::mythical-horse-guide`

- evidence_seed_key: "dream-horse-material-routines.requirement.fern-choice::mythical-horse-guide"
- source_id: "mythical-horse-guide"
- title: "꿈결 환상마(몽상)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=355"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "dream-horse-material-routines.fern-weekly-choice"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "고비 뿌리 50개 주간 택 1"
- active: true
- is_active: true

### `dream-horse-material-routines.requirement.support::mythical-horse-guide`

- evidence_seed_key: "dream-horse-material-routines.requirement.support::mythical-horse-guide"
- source_id: "mythical-horse-guide"
- title: "꿈결 환상마(몽상)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=355"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "dream-horse-material-routines.support-choice"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "지원 선택 의뢰와 깃털 2개"
- active: true
- is_active: true

### `dream-horse-material-routines.reward.feather::mythical-horse-guide`

- evidence_seed_key: "dream-horse-material-routines.reward.feather::mythical-horse-guide"
- source_id: "mythical-horse-guide"
- title: "꿈결 환상마(몽상)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=355"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "dream-horse-material-routines.feather-2"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "몽상의 깃털 2개"
- active: true
- is_active: true

### `dream-horse-material-routines.reward.fern::mythical-horse-guide`

- evidence_seed_key: "dream-horse-material-routines.reward.fern::mythical-horse-guide"
- source_id: "mythical-horse-guide"
- title: "꿈결 환상마(몽상)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=355"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "dream-horse-material-routines.fern-root-50"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 택 1 보상 50개"
- active: true
- is_active: true

### `dream-horse-material-routines.reward.support-feather::mythical-horse-guide`

- evidence_seed_key: "dream-horse-material-routines.reward.support-feather::mythical-horse-guide"
- source_id: "mythical-horse-guide"
- title: "꿈결 환상마(몽상)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=355"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "dream-horse-material-routines.support-feather-2"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "지원 의뢰 몽상의 깃털 2개"
- active: true
- is_active: true

### `dream-horse-material-routines.schedule.daily::mythical-horse-guide`

- evidence_seed_key: "dream-horse-material-routines.schedule.daily::mythical-horse-guide"
- source_id: "mythical-horse-guide"
- title: "꿈결 환상마(몽상)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=355"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "dream-horse-material-routines.daily-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "매일 00:00"
- active: true
- is_active: true

### `dream-horse-material-routines.schedule.weekly::mythical-horse-guide`

- evidence_seed_key: "dream-horse-material-routines.schedule.weekly::mythical-horse-guide"
- source_id: "mythical-horse-guide"
- title: "꿈결 환상마(몽상)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=355"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "dream-horse-material-routines.weekly-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "목요일 00:00"
- active: true
- is_active: true

### `dream-horse-material-routines.schedule.weekly::weekly-reset-2021`

- evidence_seed_key: "dream-horse-material-routines.schedule.weekly::weekly-reset-2021"
- source_id: "weekly-reset-2021"
- title: "7월 28일 (수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=6125"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "dream-horse-material-routines.weekly-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "목요일 00:00"
- active: true
- is_active: true

### Historical / inactive evidence

- None
