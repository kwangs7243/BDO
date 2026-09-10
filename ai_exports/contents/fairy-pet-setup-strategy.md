<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 요정·반려동물 초기 설정 전략

## Identity

- slug: "fairy-pet-setup-strategy"
- name_ko: "요정·반려동물 초기 설정 전략"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- party_type: "solo"
- difficulty: "easy"

## Overview

- summary: "보유 요정과 반려동물을 실제 활동 목적에 맞게 설정하는 조건부 입문 전략이다."
- purpose: "종결 조합과 유료 변경을 강제하지 않고 현재 보유 자원으로 한 번에 하나씩 편의 설정을 개선한다."

## Requirements

### `fairy-pet-setup-strategy.fairy-priority`

- seed_key: "fairy-pet-setup-strategy.fairy-priority"
- kind: "other"
- requirement_level: "recommended"
- title: "요정 기술 우선순위는 활동별 선택"
- description: "신비한 응원과 아낌없는 손길은 전투 물약과 버프 자동화가 필요한 입문자에게 먼저 검토할 후보지만 모든 사용자에게 같은 단계와 조합이 정답은 아니다. 생활, 무게, 부활, 수중·사막 이용 빈도에 따라 다른 기술을 먼저 볼 수 있다."
- structured_value:

```json
{
  "common_beginner_candidates": [
    "신비한 응원",
    "아낌없는 손길"
  ],
  "decision_dimensions": [
    "combat",
    "life",
    "weight_convenience",
    "buff_automation",
    "resurrection",
    "underwater_or_desert"
  ],
  "knowledge_role": "strategy",
  "skill_priority_depends_on_activity": true,
  "universal_best_skill_set": false
}
```

### `fairy-pet-setup-strategy.fairy-stop-condition`

- seed_key: "fairy-pet-setup-strategy.fairy-stop-condition"
- kind: "other"
- requirement_level: "recommended"
- title: "초기 목표에서 멈출 수 있음"
- description: "당장 필요한 자동화 기능이 확보되면 나머지 기술은 플레이 중 얻는 자원으로 천천히 조정한다. 처음부터 다섯 기술의 최고 단계를 완성할 필요는 없다."
- structured_value:

```json
{
  "all_max_rank_skills_required": false,
  "beginner_can_stop_early": true,
  "improve_incrementally": true,
  "knowledge_role": "strategy"
}
```

### `fairy-pet-setup-strategy.fairy-reroll-budget`

- seed_key: "fairy-pet-setup-strategy.fairy-reroll-budget"
- kind: "item"
- requirement_level: "optional"
- title: "기술 변경은 선택 사항"
- description: "기술 변경 확률과 현재 보유 기술 수에 따른 구슬 소모를 확인하고 감당할 자원이 있을 때만 변경한다. 유료 또는 반복 reroll은 진행의 필수 조건이 아니다."
- structured_value:

```json
{
  "check_current_skill_count_cost": true,
  "check_probability_before_change": true,
  "fixed_cash_budget": null,
  "knowledge_role": "strategy",
  "paid_reroll_required": false
}
```

### `fairy-pet-setup-strategy.pet-purpose`

- seed_key: "fairy-pet-setup-strategy.pet-purpose"
- kind: "other"
- requirement_level: "recommended"
- title: "반려동물 그룹은 목적별 구성"
- description: "현재 보유 반려동물의 전리품 획득, 생활, 지식, 탑승물 관련 효과를 구분한 뒤 자주 하는 활동별 그룹을 만든다. 모든 활동에 통하는 단일 최고 반려동물이나 그룹을 고정하지 않는다."
- structured_value:

```json
{
  "decision_dimensions": [
    "loot_pickup",
    "life",
    "knowledge",
    "mount"
  ],
  "group_depends_on_activity": true,
  "knowledge_role": "strategy",
  "universal_best_group": false,
  "universal_best_pet": false
}
```

### `fairy-pet-setup-strategy.pet-exchange-plan`

- seed_key: "fairy-pet-setup-strategy.pet-exchange-plan"
- kind: "other"
- requirement_level: "recommended"
- title: "교환 전에 계승 대상 확정"
- description: "교환 유형과 보유 반려동물을 확인하고 남길 외형과 기술을 정한다. 교환 확률에 대한 위험 선택은 보유 수량과 실패 감수 정도에 따라 달라지므로 하나의 효율 정답으로 고정하지 않는다."
- structured_value:

```json
{
  "confirm_exchange_type": true,
  "decision_depends_on_owned_pets": true,
  "fixed_exchange_probability_strategy": null,
  "knowledge_role": "strategy",
  "plan_inheritance_before_exchange": true,
  "universal_exchange_path": false
}
```

### `fairy-pet-setup-strategy.pet-fifth-generation-plan`

- seed_key: "fairy-pet-setup-strategy.pet-fifth-generation-plan"
- kind: "other"
- requirement_level: "recommended"
- title: "교환이 끝난 한 마리부터 5세대"
- description: "외형과 기술 교환이 끝난 4세대 중 대장으로 사용할 한 마리만 먼저 5세대로 훈련한다. 활동 검증 뒤 필요할 때 그룹을 조정하며 모든 반려동물의 5세대 전환을 목표로 삼지 않는다."
- structured_value:

```json
{
  "adjust_group_after_use": true,
  "all_pets_need_fifth_generation": false,
  "choose_one_captain_first": true,
  "exchange_before_fifth_generation_when_needed": true,
  "knowledge_role": "strategy"
}
```

## Steps

### `fairy-pet-setup-strategy.step.inspect-fairy`

- seed_key: "fairy-pet-setup-strategy.step.inspect-fairy"
- phase: "preparation"
- order_no: 1
- title: "현재 요정 확인"
- description: "요정 등급, 레벨, 보유 기술과 기술 변경 시 필요한 구슬 수를 확인한다."
- checkable: false

### `fairy-pet-setup-strategy.step.choose-fairy-goal`

- seed_key: "fairy-pet-setup-strategy.step.choose-fairy-goal"
- phase: "preparation"
- order_no: 2
- title: "가장 필요한 요정 기능 하나 선택"
- description: "전투, 생활, 무게, 버프 자동화, 부활, 수중·사막 중 현재 불편이 큰 기능 하나를 고른다."
- checkable: false

### `fairy-pet-setup-strategy.step.inspect-pets`

- seed_key: "fairy-pet-setup-strategy.step.inspect-pets"
- phase: "preparation"
- order_no: 4
- title: "보유 반려동물 효과 확인"
- description: "각 반려동물의 세대, 교환 유형, 특기, 고유 기술과 주 기술을 확인한다."
- checkable: false

### `fairy-pet-setup-strategy.step.choose-activity`

- seed_key: "fairy-pet-setup-strategy.step.choose-activity"
- phase: "preparation"
- order_no: 5
- title: "반려동물 활동 목적 선택"
- description: "전리품 획득, 생활, 지식, 탑승물 중 이번에 개선할 활동을 하나 선택한다."
- checkable: false

### `fairy-pet-setup-strategy.step.build-group`

- seed_key: "fairy-pet-setup-strategy.step.build-group"
- phase: "preparation"
- order_no: 6
- title: "목적별 그룹 구성"
- description: "특기 중첩 여부와 기술을 확인해 현재 보유 반려동물로 활동 그룹을 만든다."
- checkable: false

### `fairy-pet-setup-strategy.step.finish-exchange`

- seed_key: "fairy-pet-setup-strategy.step.finish-exchange"
- phase: "preparation"
- order_no: 7
- title: "교환과 계승 먼저 완료"
- description: "5세대 후보는 교환 유형과 외형·기술 계승 계획을 확정하고 필요한 일반 교환을 먼저 끝낸다."
- checkable: false

### `fairy-pet-setup-strategy.step.stop-or-improve-fairy`

- seed_key: "fairy-pet-setup-strategy.step.stop-or-improve-fairy"
- phase: "maintenance"
- order_no: 3
- title: "요정 개선 또는 멈춤 판단"
- description: "필요 기능을 확보했다면 멈추고, 부족할 때만 확률과 자원 소모를 확인해 다음 한 기술을 조정한다."
- checkable: false

### `fairy-pet-setup-strategy.step.train-one-captain`

- seed_key: "fairy-pet-setup-strategy.step.train-one-captain"
- phase: "maintenance"
- order_no: 8
- title: "대장 한 마리부터 검증"
- description: "교환을 끝낸 4세대 한 마리를 5세대로 훈련해 대장으로 사용하고 실제 활동 뒤 그룹을 조정한다."
- checkable: false

## Schedules

- None

## Rewards

- None

## Sections

### `fairy-pet-setup-strategy.section.first-session`

- seed_key: "fairy-pet-setup-strategy.section.first-session"
- section_type: "strategy"
- title: "첫 설정 세션"
- order_no: 1

#### body_markdown

요정은 지금 가장 필요한 편의 기능 하나, 반려동물은 가장 자주 하는 활동 그룹 하나를 먼저 설정한다. 한 세션에서 종결 조합을 만들지 않고 즉시 확인할 수 있는 개선 한 가지로 끝낸다.

### `fairy-pet-setup-strategy.section.decision-boundaries`

- seed_key: "fairy-pet-setup-strategy.section.decision-boundaries"
- section_type: "strategy"
- title: "비용과 비가역 작업의 경계"
- order_no: 2

#### body_markdown

요정 기술 변경은 확률과 구슬 소모를 확인한 선택 작업이다. 반려동물 5세대 훈련은 이후 일반 교환을 막으므로 외형과 기술 계승을 끝낸 한 마리부터 진행한다.

### `fairy-pet-setup-strategy.section.common-mistakes`

- seed_key: "fairy-pet-setup-strategy.section.common-mistakes"
- section_type: "common_mistakes"
- title: "보편적 종결 조합을 만들지 않기"
- order_no: 3

#### body_markdown

신비한 응원과 아낌없는 손길을 모든 사용자에게 필수 최고 단계로 고정하지 않는다. 모든 반려동물 특기가 중첩된다고 보거나 모든 반려동물을 5세대로 올리는 목표를 만들지 않으며 상업 가격과 이벤트 지급을 영구 전략에 포함하지 않는다.

## Related Contents

### `fairy-pet-setup-strategy.fairy-facts`

- seed_key: "fairy-pet-setup-strategy.fairy-facts"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "fairy-current-system"
- content_name_ko: "요정 레이라 현재 시스템"
- content_category: "progression"
- note: "현재 요정 시스템 FACT를 판단 근거로 사용"
- order_no: 1
- relative_path: "../contents/fairy-current-system.md"
### `fairy-pet-setup-strategy.pet-facts`

- seed_key: "fairy-pet-setup-strategy.pet-facts"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "pet-current-system"
- content_name_ko: "반려동물 현재 시스템"
- content_category: "progression"
- note: "현재 반려동물 시스템 FACT를 판단 근거로 사용"
- order_no: 2
- relative_path: "../contents/pet-current-system.md"
### `fairy-pet-setup-strategy.fifth-generation-facts`

- seed_key: "fairy-pet-setup-strategy.fifth-generation-facts"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "pet-fifth-generation"
- content_name_ko: "5세대 반려동물과 대장"
- content_category: "progression"
- note: "5세대 훈련과 교환 잠금 FACT를 판단 근거로 사용"
- order_no: 3
- relative_path: "../contents/pet-fifth-generation.md"

## Evidence and Sources

### Current evidence

### `fairy-pet-setup-strategy.claim.purpose::fairy-beginner-strategy-2026-08-20`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.purpose::fairy-beginner-strategy-2026-08-20"
- source_id: "fairy-beginner-strategy-2026-08-20"
- title: "뉴비 요정작 방법"
- url: "https://www.inven.co.kr/board/black/3584/59007"
- publisher: "검은사막 인벤 / 화나면문다"
- source_type: "community_strategy"
- published_at: "2026-08-20"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fairy-pet-setup-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.purpose::pet-exchange-decisions-2026-06-04`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.purpose::pet-exchange-decisions-2026-06-04"
- source_id: "pet-exchange-decisions-2026-06-04"
- title: "반려동물 3세대 교환 어느게 효율적인지"
- url: "https://www.inven.co.kr/board/black/3584/58842"
- publisher: "검은사막 인벤 / 카나트"
- source_type: "community_strategy"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fairy-pet-setup-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.summary::fairy-beginner-strategy-2026-08-20`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.summary::fairy-beginner-strategy-2026-08-20"
- source_id: "fairy-beginner-strategy-2026-08-20"
- title: "뉴비 요정작 방법"
- url: "https://www.inven.co.kr/board/black/3584/59007"
- publisher: "검은사막 인벤 / 화나면문다"
- source_type: "community_strategy"
- published_at: "2026-08-20"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fairy-pet-setup-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.summary::fairy-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.summary::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fairy-pet-setup-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.summary::pet-exchange-decisions-2026-06-04`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.summary::pet-exchange-decisions-2026-06-04"
- source_id: "pet-exchange-decisions-2026-06-04"
- title: "반려동물 3세대 교환 어느게 효율적인지"
- url: "https://www.inven.co.kr/board/black/3584/58842"
- publisher: "검은사막 인벤 / 카나트"
- source_type: "community_strategy"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fairy-pet-setup-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.summary::pet-fifth-generation-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.summary::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fairy-pet-setup-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.summary::pet-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.summary::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fairy-pet-setup-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.fairy-priority::fairy-beginner-strategy-2026-08-20`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.fairy-priority::fairy-beginner-strategy-2026-08-20"
- source_id: "fairy-beginner-strategy-2026-08-20"
- title: "뉴비 요정작 방법"
- url: "https://www.inven.co.kr/board/black/3584/59007"
- publisher: "검은사막 인벤 / 화나면문다"
- source_type: "community_strategy"
- published_at: "2026-08-20"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-pet-setup-strategy.fairy-priority"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.fairy-priority::fairy-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.fairy-priority::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-pet-setup-strategy.fairy-priority"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.fairy-reroll-budget::fairy-beginner-strategy-2026-08-20`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.fairy-reroll-budget::fairy-beginner-strategy-2026-08-20"
- source_id: "fairy-beginner-strategy-2026-08-20"
- title: "뉴비 요정작 방법"
- url: "https://www.inven.co.kr/board/black/3584/59007"
- publisher: "검은사막 인벤 / 화나면문다"
- source_type: "community_strategy"
- published_at: "2026-08-20"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-pet-setup-strategy.fairy-reroll-budget"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.fairy-reroll-budget::fairy-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.fairy-reroll-budget::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-pet-setup-strategy.fairy-reroll-budget"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.fairy-reroll-budget::fairy-probability-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.fairy-reroll-budget::fairy-probability-guide-current"
- source_id: "fairy-probability-guide-current"
- title: "요정 기술 습득 / 날개 돋이 확률"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=338"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-pet-setup-strategy.fairy-reroll-budget"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.fairy-stop-condition::fairy-beginner-strategy-2026-08-20`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.fairy-stop-condition::fairy-beginner-strategy-2026-08-20"
- source_id: "fairy-beginner-strategy-2026-08-20"
- title: "뉴비 요정작 방법"
- url: "https://www.inven.co.kr/board/black/3584/59007"
- publisher: "검은사막 인벤 / 화나면문다"
- source_type: "community_strategy"
- published_at: "2026-08-20"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-pet-setup-strategy.fairy-stop-condition"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.pet-exchange-plan::pet-exchange-decisions-2026-06-04`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.pet-exchange-plan::pet-exchange-decisions-2026-06-04"
- source_id: "pet-exchange-decisions-2026-06-04"
- title: "반려동물 3세대 교환 어느게 효율적인지"
- url: "https://www.inven.co.kr/board/black/3584/58842"
- publisher: "검은사막 인벤 / 카나트"
- source_type: "community_strategy"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-pet-setup-strategy.pet-exchange-plan"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.pet-exchange-plan::pet-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.pet-exchange-plan::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-pet-setup-strategy.pet-exchange-plan"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.pet-fifth-generation-plan::pet-fifth-generation-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.pet-fifth-generation-plan::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-pet-setup-strategy.pet-fifth-generation-plan"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.pet-purpose::pet-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.pet-purpose::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fairy-pet-setup-strategy.pet-purpose"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.section.common-mistakes::fairy-beginner-strategy-2026-08-20`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.section.common-mistakes::fairy-beginner-strategy-2026-08-20"
- source_id: "fairy-beginner-strategy-2026-08-20"
- title: "뉴비 요정작 방법"
- url: "https://www.inven.co.kr/board/black/3584/59007"
- publisher: "검은사막 인벤 / 화나면문다"
- source_type: "community_strategy"
- published_at: "2026-08-20"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fairy-pet-setup-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.section.common-mistakes::pet-fifth-generation-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.section.common-mistakes::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fairy-pet-setup-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.section.common-mistakes::pet-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.section.common-mistakes::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fairy-pet-setup-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.section.decision-boundaries::fairy-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.section.decision-boundaries::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fairy-pet-setup-strategy.section.decision-boundaries"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.section.decision-boundaries::fairy-probability-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.section.decision-boundaries::fairy-probability-guide-current"
- source_id: "fairy-probability-guide-current"
- title: "요정 기술 습득 / 날개 돋이 확률"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=338"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fairy-pet-setup-strategy.section.decision-boundaries"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.section.decision-boundaries::pet-fifth-generation-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.section.decision-boundaries::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fairy-pet-setup-strategy.section.decision-boundaries"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.section.first-session::fairy-beginner-strategy-2026-08-20`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.section.first-session::fairy-beginner-strategy-2026-08-20"
- source_id: "fairy-beginner-strategy-2026-08-20"
- title: "뉴비 요정작 방법"
- url: "https://www.inven.co.kr/board/black/3584/59007"
- publisher: "검은사막 인벤 / 화나면문다"
- source_type: "community_strategy"
- published_at: "2026-08-20"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fairy-pet-setup-strategy.section.first-session"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.section.first-session::pet-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.section.first-session::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "fairy-pet-setup-strategy.section.first-session"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.step.build-group::pet-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.step.build-group::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-pet-setup-strategy.step.build-group"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.step.choose-activity::pet-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.step.choose-activity::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-pet-setup-strategy.step.choose-activity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.step.choose-fairy-goal::fairy-beginner-strategy-2026-08-20`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.step.choose-fairy-goal::fairy-beginner-strategy-2026-08-20"
- source_id: "fairy-beginner-strategy-2026-08-20"
- title: "뉴비 요정작 방법"
- url: "https://www.inven.co.kr/board/black/3584/59007"
- publisher: "검은사막 인벤 / 화나면문다"
- source_type: "community_strategy"
- published_at: "2026-08-20"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-pet-setup-strategy.step.choose-fairy-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.step.choose-fairy-goal::fairy-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.step.choose-fairy-goal::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-pet-setup-strategy.step.choose-fairy-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.step.finish-exchange::pet-fifth-generation-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.step.finish-exchange::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-pet-setup-strategy.step.finish-exchange"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.step.finish-exchange::pet-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.step.finish-exchange::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-pet-setup-strategy.step.finish-exchange"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.step.inspect-fairy::fairy-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.step.inspect-fairy::fairy-guide-current"
- source_id: "fairy-guide-current"
- title: "요정 레이라"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=181"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-pet-setup-strategy.step.inspect-fairy"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.step.inspect-fairy::fairy-probability-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.step.inspect-fairy::fairy-probability-guide-current"
- source_id: "fairy-probability-guide-current"
- title: "요정 기술 습득 / 날개 돋이 확률"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=338"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-pet-setup-strategy.step.inspect-fairy"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.step.inspect-pets::pet-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.step.inspect-pets::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-pet-setup-strategy.step.inspect-pets"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.step.stop-or-improve-fairy::fairy-beginner-strategy-2026-08-20`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.step.stop-or-improve-fairy::fairy-beginner-strategy-2026-08-20"
- source_id: "fairy-beginner-strategy-2026-08-20"
- title: "뉴비 요정작 방법"
- url: "https://www.inven.co.kr/board/black/3584/59007"
- publisher: "검은사막 인벤 / 화나면문다"
- source_type: "community_strategy"
- published_at: "2026-08-20"
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-pet-setup-strategy.step.stop-or-improve-fairy"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.step.stop-or-improve-fairy::fairy-probability-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.step.stop-or-improve-fairy::fairy-probability-guide-current"
- source_id: "fairy-probability-guide-current"
- title: "요정 기술 습득 / 날개 돋이 확률"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=338"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-pet-setup-strategy.step.stop-or-improve-fairy"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `fairy-pet-setup-strategy.claim.step.train-one-captain::pet-fifth-generation-guide-current`

- evidence_seed_key: "fairy-pet-setup-strategy.claim.step.train-one-captain::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fairy-pet-setup-strategy.step.train-one-captain"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
