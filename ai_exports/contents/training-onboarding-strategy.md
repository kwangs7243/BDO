<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 조련 입문 운영 전략

## Identity

- slug: "training-onboarding-strategy"
- name_ko: "조련 입문 운영 전략"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- party_type: "solo"
- difficulty: null

## Overview

- summary: "현재 말과 마구간 상태, 조련 목적을 확인한 뒤 포획·육성·교배·교환·황실 납품과 상위 말 진행 중 이번 세션의 한 가지 행동을 고르는 입문 전략이다."
- purpose: "조련 FACT를 복제하지 않고 초보자가 작은 첫 조련 목표를 실행하고 다음 병목을 판단하게 한다."

## Requirements

### `training-onboarding-strategy.purpose-choice`

- seed_key: "training-onboarding-strategy.purpose-choice"
- kind: "other"
- requirement_level: "required"
- title: "이번 조련 목적 선택"
- description: "포획·말 육성·교배·교환·황실 납품·준마·환상마 준비 중 이번 세션의 목적 하나를 먼저 고른다."
- structured_value:

```json
{
  "first_session": "one_small_training_goal",
  "goals": [
    "wild_horse_capture",
    "horse_leveling",
    "breeding",
    "exchange",
    "imperial_delivery",
    "courser_progression",
    "dream_horse_preparation",
    "general_training_growth"
  ],
  "knowledge_role": "strategy",
  "single_default_goal": false
}
```

### `training-onboarding-strategy.starting-horse-choice`

- seed_key: "training-onboarding-strategy.starting-horse-choice"
- kind: "other"
- requirement_level: "required"
- title: "시작할 말 선택"
- description: "보유 말의 세대·레벨·기술·교배 가능 횟수와 목적, 마구간 여유를 함께 보고 이번에 키울 말을 정한다."
- structured_value:

```json
{
  "dimensions": [
    "horse_generation",
    "horse_level",
    "learned_skills",
    "breeding_count",
    "session_goal",
    "stable_space"
  ],
  "knowledge_role": "strategy",
  "universal_best_horse": false
}
```

### `training-onboarding-strategy.capture-or-owned`

- seed_key: "training-onboarding-strategy.capture-or-owned"
- kind: "other"
- requirement_level: "required"
- title: "야생마 포획과 보유 말 육성 선택"
- description: "포획 자체가 목적이거나 적합한 보유 말이 없으면 야생마 포획을 검토하고, 목적에 맞는 말이 있으면 기존 말의 육성과 상태 확인을 우선한다."
- structured_value:

```json
{
  "capture_when": [
    "capture_is_goal",
    "no_suitable_owned_horse",
    "wild_horse_requirement_or_practice"
  ],
  "current_population_fact_owner": "wild-horse-capture",
  "knowledge_role": "strategy",
  "owned_horse_when": [
    "suitable_horse_available",
    "level_or_skill_growth_is_goal",
    "breeding_or_delivery_preparation"
  ],
  "universal_best_capture_location": false
}
```

### `training-onboarding-strategy.outcome-choice`

- seed_key: "training-onboarding-strategy.outcome-choice"
- kind: "other"
- requirement_level: "required"
- title: "육성 결과의 다음 행동 선택"
- description: "현재 말의 레벨·기술·교배 상태, 마구간 공간과 목적을 확인해 계속 육성·교배·교환·황실 납품 중 다음 행동을 고른다."
- structured_value:

```json
{
  "choices": [
    "continue_leveling",
    "breeding",
    "exchange",
    "imperial_delivery"
  ],
  "dimensions": [
    "horse_level",
    "learned_skills",
    "breeding_count",
    "stable_space",
    "goal",
    "desired_rewards"
  ],
  "fixed_breeding_ev": null,
  "fixed_silver_profit": null,
  "knowledge_role": "strategy"
}
```

### `training-onboarding-strategy.advanced-progression`

- seed_key: "training-onboarding-strategy.advanced-progression"
- kind: "other"
- requirement_level: "recommended"
- title: "준마와 환상마 진행 전환"
- description: "현재 말과 준마 준비 상태, 보유 재료와 반복 루틴 준비를 확인한 뒤 준마·환상마·꿈결 환상마 진행으로 넘어간다."
- structured_value:

```json
{
  "beginner_default": false,
  "dimensions": [
    "current_horse",
    "courser_readiness",
    "training_materials",
    "recurring_material_routines"
  ],
  "fact_owners": [
    "courser-system",
    "dream-horse-awakening",
    "mythical-dream-horse",
    "dream-horse-material-routines"
  ],
  "knowledge_role": "strategy",
  "universal_priority": false
}
```

### `training-onboarding-strategy.session-mode`

- seed_key: "training-onboarding-strategy.session-mode"
- kind: "other"
- requirement_level: "recommended"
- title: "직접 조련과 자리 비움 육성 구분"
- description: "포획·상태 평가처럼 직접 확인할 행동과 안전한 왕복 경로의 말 육성을 구분하고, 이번 세션에서 실제 병목 하나만 개선한다."
- structured_value:

```json
{
  "dimensions": [
    "available_attention",
    "route_safety",
    "stable_space",
    "horse_goal"
  ],
  "improvement_per_session": 1,
  "knowledge_role": "strategy",
  "modes": [
    "active_capture_or_management",
    "afk_horse_leveling"
  ],
  "universal_best_training_method": false
}
```

## Steps

### `training-onboarding-strategy.step.choose-goal`

- seed_key: "training-onboarding-strategy.step.choose-goal"
- phase: "preparation"
- order_no: 1
- title: "이번 조련 목적 정하기"
- description: "포획·육성·교배·교환·황실 납품·상위 진행 중 이번 세션의 작은 목표 하나를 고른다."
- checkable: false

### `training-onboarding-strategy.step.inspect-horses-stable`

- seed_key: "training-onboarding-strategy.step.inspect-horses-stable"
- phase: "preparation"
- order_no: 2
- title: "보유 말과 마구간 확인"
- description: "말의 세대·레벨·기술·교배 횟수와 마구간 빈 공간을 확인한다."
- checkable: false

### `training-onboarding-strategy.step.choose-capture-or-owned`

- seed_key: "training-onboarding-strategy.step.choose-capture-or-owned"
- phase: "preparation"
- order_no: 3
- title: "포획 또는 보유 말 육성 선택"
- description: "현재 목적과 보유 말 상태에 따라 야생마를 포획할지 기존 말을 키울지 결정한다."
- checkable: false

### `training-onboarding-strategy.step.check-preparation`

- seed_key: "training-onboarding-strategy.step.check-preparation"
- phase: "preparation"
- order_no: 4
- title: "필요한 기본 준비 확인"
- description: "선택한 활동에 필요한 준비와 현재 생활 장비 구성을 기존 canonical Content에서 확인한다."
- checkable: false

### `training-onboarding-strategy.step.run-small-session`

- seed_key: "training-onboarding-strategy.step.run-small-session"
- phase: "first_time"
- order_no: 5
- title: "짧은 첫 조련 세션 실행"
- description: "포획 또는 말 육성 중 선택한 한 가지 활동을 짧게 실행한다."
- checkable: false

### `training-onboarding-strategy.step.review-horse-state`

- seed_key: "training-onboarding-strategy.step.review-horse-state"
- phase: "first_time"
- order_no: 6
- title: "말 상태 다시 확인"
- description: "세션 뒤 말 레벨·습득 기술·교배 가능 횟수와 마구간 상태를 다시 확인한다."
- checkable: false

### `training-onboarding-strategy.step.choose-next-outcome`

- seed_key: "training-onboarding-strategy.step.choose-next-outcome"
- phase: "first_time"
- order_no: 7
- title: "다음 처리 방식 선택"
- description: "현재 상태와 목적에 따라 계속 육성·교배·교환·황실 납품 중 다음 행동을 고른다."
- checkable: false

### `training-onboarding-strategy.step.check-advanced-readiness`

- seed_key: "training-onboarding-strategy.step.check-advanced-readiness"
- phase: "first_time"
- order_no: 8
- title: "상위 진행 준비 여부 확인"
- description: "준마·환상마 진행은 현재 말, 기술과 재료 루틴 준비가 갖춰졌을 때 별도로 검토한다."
- checkable: false

### `training-onboarding-strategy.step.record-bottleneck`

- seed_key: "training-onboarding-strategy.step.record-bottleneck"
- phase: "maintenance"
- order_no: 9
- title: "실제 병목 기록"
- description: "말 선택·마구간 공간·육성 시간·기술·교배 상태·재료 중 세션을 막은 병목을 기록한다."
- checkable: false

### `training-onboarding-strategy.step.improve-one-bottleneck`

- seed_key: "training-onboarding-strategy.step.improve-one-bottleneck"
- phase: "maintenance"
- order_no: 10
- title: "다음 세션 병목 하나 개선"
- description: "다음 세션에서는 기록한 병목 중 한 가지만 개선하고 같은 판단 루프를 다시 실행한다."
- checkable: false

## Schedules

- None

## Rewards

- None

## Sections

### `training-onboarding-strategy.section.goal-to-progression`

- seed_key: "training-onboarding-strategy.section.goal-to-progression"
- section_type: "strategy"
- title: "목적에서 말 progression으로"
- order_no: 1

#### body_markdown

특정 말이나 장비를 먼저 정답으로 고르지 않는다. 목적 → 현재 말과 마구간 → 이번 활동 → 결과 확인 → 다음 progression 순서로 판단한다. 포획·육성·교배·교환·납품의 시스템 규칙은 연결된 기존 Content에서 확인한다.

### `training-onboarding-strategy.section.training-loop`

- seed_key: "training-onboarding-strategy.section.training-loop"
- section_type: "strategy"
- title: "조련 운영 루프"
- order_no: 2

#### body_markdown

야생마를 포획하거나 보유 말을 선택한 뒤 짧게 육성하고 상태를 평가한다. 그 결과에 따라 계속 육성, 교배, 교환, 황실 납품 중 하나를 고르며 준마·환상마 준비는 재료와 반복 루틴이 갖춰진 뒤 별도 단계로 진행한다.

### `training-onboarding-strategy.section.common-mistakes`

- seed_key: "training-onboarding-strategy.section.common-mistakes"
- section_type: "common_mistakes"
- title: "현재 조련에서 피할 고정 답안"
- order_no: 3

#### body_markdown

9월 2일 이전 장비 build와 과거 마시장 가격을 현재 값으로 복제하지 않는다. 고정 silver/hour, 특정 포획 장소, 모든 말의 8세대·준마 육성, 초보자의 환상마 최우선 진행을 보편 규칙으로 두지 않는다. 이벤트 핫타임·보상·종료일을 영구 시스템으로 저장하지 않고, 교배와 교환의 차이 및 마구간 공간·교배 상태를 확인한다.

## Related Contents

### `training-onboarding-strategy.current-system`

- seed_key: "training-onboarding-strategy.current-system"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "training-current-system"
- content_name_ko: "조련 현재 시스템"
- content_category: "life"
- note: "조련 활동 범위와 현재 시스템"
- order_no: 1
- relative_path: "../contents/training-current-system.md"
### `training-onboarding-strategy.mastery`

- seed_key: "training-onboarding-strategy.mastery"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "training-mastery-effects"
- content_name_ko: "조련 숙련도 효과"
- content_category: "life"
- note: "포획·탑승물 경험치·세대 확률의 숙련도 FACT"
- order_no: 2
- relative_path: "../contents/training-mastery-effects.md"
### `training-onboarding-strategy.capture`

- seed_key: "training-onboarding-strategy.capture"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "wild-horse-capture"
- content_name_ko: "야생마 포획"
- content_category: "life"
- note: "야생마 포획과 2026년 개체 수 변경"
- order_no: 3
- relative_path: "../contents/wild-horse-capture.md"
### `training-onboarding-strategy.breeding-exchange`

- seed_key: "training-onboarding-strategy.breeding-exchange"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "horse-breeding-exchange"
- content_name_ko: "말 교배와 교환"
- content_category: "life"
- note: "교배와 교환의 소비 규칙"
- order_no: 4
- relative_path: "../contents/horse-breeding-exchange.md"
### `training-onboarding-strategy.imperial-delivery`

- seed_key: "training-onboarding-strategy.imperial-delivery"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "horse-imperial-delivery"
- content_name_ko: "말 황실 납품"
- content_category: "life"
- note: "황실 말 납품 조건과 보상"
- order_no: 5
- relative_path: "../contents/horse-imperial-delivery.md"
### `training-onboarding-strategy.courser`

- seed_key: "training-onboarding-strategy.courser"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "courser-system"
- content_name_ko: "준마 시스템"
- content_category: "life"
- note: "준마 판정과 상위 진행"
- order_no: 6
- relative_path: "../contents/courser-system.md"
### `training-onboarding-strategy.dream-awakening`

- seed_key: "training-onboarding-strategy.dream-awakening"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "dream-horse-awakening"
- content_name_ko: "환상마 각성"
- content_category: "life"
- note: "환상마 각성 조건과 재료"
- order_no: 7
- relative_path: "../contents/dream-horse-awakening.md"
### `training-onboarding-strategy.mythical`

- seed_key: "training-onboarding-strategy.mythical"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "mythical-dream-horse"
- content_name_ko: "꿈결 환상마"
- content_category: "life"
- note: "꿈결 환상마 progression"
- order_no: 8
- relative_path: "../contents/mythical-dream-horse.md"
### `training-onboarding-strategy.growth-quest`

- seed_key: "training-onboarding-strategy.growth-quest"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "training-growth-surprise-quest"
- content_name_ko: "조련 성장 깜짝 의뢰"
- content_category: "life"
- note: "조련 성장 깜짝 의뢰"
- order_no: 9
- relative_path: "../contents/training-growth-surprise-quest.md"
### `training-onboarding-strategy.material-routines`

- seed_key: "training-onboarding-strategy.material-routines"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "dream-horse-material-routines"
- content_name_ko: "꿈결 환상마 재료 루틴"
- content_category: "life"
- note: "상위 말 재료 반복 루틴과 고비 뿌리 사용처"
- order_no: 10
- relative_path: "../contents/dream-horse-material-routines.md"

## Evidence and Sources

### Current evidence

### `training-onboarding-strategy.claim.purpose::training-beginner-decisions-2026-02-05`

- evidence_seed_key: "training-onboarding-strategy.claim.purpose::training-beginner-decisions-2026-02-05"
- source_id: "training-beginner-decisions-2026-02-05"
- title: "조련 뉴비가 질문 올림."
- url: "https://www.inven.co.kr/board/black/3583/1995323"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2026-02-05"
- retrieved_at: "2026-09-07T09:35:53+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "training-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.purpose::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.purpose::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "training-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.summary::training-beginner-decisions-2026-02-05`

- evidence_seed_key: "training-onboarding-strategy.claim.summary::training-beginner-decisions-2026-02-05"
- source_id: "training-beginner-decisions-2026-02-05"
- title: "조련 뉴비가 질문 올림."
- url: "https://www.inven.co.kr/board/black/3583/1995323"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2026-02-05"
- retrieved_at: "2026-09-07T09:35:53+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "training-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.summary::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.summary::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "training-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.advanced-progression::dream-horse-awakening-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.advanced-progression::dream-horse-awakening-guide"
- source_id: "dream-horse-awakening-guide"
- title: "환상마 각성 확률 증가 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=350"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "training-onboarding-strategy.advanced-progression"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.advanced-progression::mythical-horse-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.advanced-progression::mythical-horse-guide"
- source_id: "mythical-horse-guide"
- title: "꿈결 환상마(몽상)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=355"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "training-onboarding-strategy.advanced-progression"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.advanced-progression::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.advanced-progression::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "training-onboarding-strategy.advanced-progression"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.capture-or-owned::blood-altar-challenge-2026-07-15`

- evidence_seed_key: "training-onboarding-strategy.claim.capture-or-owned::blood-altar-challenge-2026-07-15"
- source_id: "blood-altar-challenge-2026-07-15"
- title: "7월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15878"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "training-onboarding-strategy.capture-or-owned"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.capture-or-owned::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.capture-or-owned::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "training-onboarding-strategy.capture-or-owned"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.outcome-choice::training-beginner-decisions-2026-02-05`

- evidence_seed_key: "training-onboarding-strategy.claim.outcome-choice::training-beginner-decisions-2026-02-05"
- source_id: "training-beginner-decisions-2026-02-05"
- title: "조련 뉴비가 질문 올림."
- url: "https://www.inven.co.kr/board/black/3583/1995323"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2026-02-05"
- retrieved_at: "2026-09-07T09:35:53+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "training-onboarding-strategy.outcome-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.outcome-choice::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.outcome-choice::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "training-onboarding-strategy.outcome-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.purpose-choice::training-beginner-decisions-2026-02-05`

- evidence_seed_key: "training-onboarding-strategy.claim.purpose-choice::training-beginner-decisions-2026-02-05"
- source_id: "training-beginner-decisions-2026-02-05"
- title: "조련 뉴비가 질문 올림."
- url: "https://www.inven.co.kr/board/black/3583/1995323"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2026-02-05"
- retrieved_at: "2026-09-07T09:35:53+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "training-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.purpose-choice::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.purpose-choice::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "training-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.session-mode::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.session-mode::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "training-onboarding-strategy.session-mode"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.starting-horse-choice::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.starting-horse-choice::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "training-onboarding-strategy.starting-horse-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.section.common-mistakes::life-unification-2026-09-02`

- evidence_seed_key: "training-onboarding-strategy.claim.section.common-mistakes::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "training-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.section.common-mistakes::training-beginner-decisions-2026-02-05`

- evidence_seed_key: "training-onboarding-strategy.claim.section.common-mistakes::training-beginner-decisions-2026-02-05"
- source_id: "training-beginner-decisions-2026-02-05"
- title: "조련 뉴비가 질문 올림."
- url: "https://www.inven.co.kr/board/black/3583/1995323"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2026-02-05"
- retrieved_at: "2026-09-07T09:35:53+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "training-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.section.common-mistakes::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.section.common-mistakes::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "training-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.section.goal-to-progression::dream-horse-awakening-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.section.goal-to-progression::dream-horse-awakening-guide"
- source_id: "dream-horse-awakening-guide"
- title: "환상마 각성 확률 증가 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=350"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "training-onboarding-strategy.section.goal-to-progression"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.section.goal-to-progression::mythical-horse-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.section.goal-to-progression::mythical-horse-guide"
- source_id: "mythical-horse-guide"
- title: "꿈결 환상마(몽상)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=355"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "training-onboarding-strategy.section.goal-to-progression"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.section.goal-to-progression::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.section.goal-to-progression::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "training-onboarding-strategy.section.goal-to-progression"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.section.training-loop::training-beginner-decisions-2026-02-05`

- evidence_seed_key: "training-onboarding-strategy.claim.section.training-loop::training-beginner-decisions-2026-02-05"
- source_id: "training-beginner-decisions-2026-02-05"
- title: "조련 뉴비가 질문 올림."
- url: "https://www.inven.co.kr/board/black/3583/1995323"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2026-02-05"
- retrieved_at: "2026-09-07T09:35:53+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "training-onboarding-strategy.section.training-loop"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.section.training-loop::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.section.training-loop::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "training-onboarding-strategy.section.training-loop"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.step.check-advanced-readiness::dream-horse-awakening-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.step.check-advanced-readiness::dream-horse-awakening-guide"
- source_id: "dream-horse-awakening-guide"
- title: "환상마 각성 확률 증가 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=350"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "training-onboarding-strategy.step.check-advanced-readiness"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.step.check-advanced-readiness::mythical-horse-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.step.check-advanced-readiness::mythical-horse-guide"
- source_id: "mythical-horse-guide"
- title: "꿈결 환상마(몽상)"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=355"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "training-onboarding-strategy.step.check-advanced-readiness"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.step.check-advanced-readiness::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.step.check-advanced-readiness::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "training-onboarding-strategy.step.check-advanced-readiness"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.step.check-preparation::life-unification-2026-09-02`

- evidence_seed_key: "training-onboarding-strategy.claim.step.check-preparation::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "training-onboarding-strategy.step.check-preparation"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.step.check-preparation::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.step.check-preparation::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "training-onboarding-strategy.step.check-preparation"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.step.choose-capture-or-owned::blood-altar-challenge-2026-07-15`

- evidence_seed_key: "training-onboarding-strategy.claim.step.choose-capture-or-owned::blood-altar-challenge-2026-07-15"
- source_id: "blood-altar-challenge-2026-07-15"
- title: "7월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15878"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "training-onboarding-strategy.step.choose-capture-or-owned"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.step.choose-capture-or-owned::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.step.choose-capture-or-owned::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "training-onboarding-strategy.step.choose-capture-or-owned"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.step.choose-goal::training-beginner-decisions-2026-02-05`

- evidence_seed_key: "training-onboarding-strategy.claim.step.choose-goal::training-beginner-decisions-2026-02-05"
- source_id: "training-beginner-decisions-2026-02-05"
- title: "조련 뉴비가 질문 올림."
- url: "https://www.inven.co.kr/board/black/3583/1995323"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2026-02-05"
- retrieved_at: "2026-09-07T09:35:53+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "training-onboarding-strategy.step.choose-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.step.choose-goal::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.step.choose-goal::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "training-onboarding-strategy.step.choose-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.step.choose-next-outcome::training-beginner-decisions-2026-02-05`

- evidence_seed_key: "training-onboarding-strategy.claim.step.choose-next-outcome::training-beginner-decisions-2026-02-05"
- source_id: "training-beginner-decisions-2026-02-05"
- title: "조련 뉴비가 질문 올림."
- url: "https://www.inven.co.kr/board/black/3583/1995323"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2026-02-05"
- retrieved_at: "2026-09-07T09:35:53+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "training-onboarding-strategy.step.choose-next-outcome"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.step.choose-next-outcome::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.step.choose-next-outcome::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "training-onboarding-strategy.step.choose-next-outcome"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.step.improve-one-bottleneck::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.step.improve-one-bottleneck::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "training-onboarding-strategy.step.improve-one-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.step.inspect-horses-stable::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.step.inspect-horses-stable::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "training-onboarding-strategy.step.inspect-horses-stable"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.step.record-bottleneck::training-beginner-decisions-2026-02-05`

- evidence_seed_key: "training-onboarding-strategy.claim.step.record-bottleneck::training-beginner-decisions-2026-02-05"
- source_id: "training-beginner-decisions-2026-02-05"
- title: "조련 뉴비가 질문 올림."
- url: "https://www.inven.co.kr/board/black/3583/1995323"
- publisher: "검은사막 인벤"
- source_type: "community_strategy"
- published_at: "2026-02-05"
- retrieved_at: "2026-09-07T09:35:53+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "training-onboarding-strategy.step.record-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.step.record-bottleneck::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.step.record-bottleneck::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "training-onboarding-strategy.step.record-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.step.review-horse-state::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.step.review-horse-state::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "training-onboarding-strategy.step.review-horse-state"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `training-onboarding-strategy.claim.step.run-small-session::training-guide`

- evidence_seed_key: "training-onboarding-strategy.claim.step.run-small-session::training-guide"
- source_id: "training-guide"
- title: "조련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=103"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "training-onboarding-strategy.step.run-small-session"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
