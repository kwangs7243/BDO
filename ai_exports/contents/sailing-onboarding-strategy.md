<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 항해 입문 운영 전략

## Identity

- slug: "sailing-onboarding-strategy"
- name_ko: "항해 입문 운영 전략"
- category: "ocean_guide"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- party_type: null
- difficulty: null

## Overview

- summary: "항해 목적을 먼저 정하고 출항 준비, 짧은 첫 항해, 귀환 정리와 다음 병목 개선을 연결하는 정적 운영 전략."
- purpose: "기존 선박·선원 FACT를 복제하지 않고 사용자의 목적과 현재 상태에 맞는 첫 항해와 성장 순서를 결정한다."

## Requirements

### `sailing-onboarding-strategy.purpose-choice`

- seed_key: "sailing-onboarding-strategy.purpose-choice"
- kind: "other"
- requirement_level: "required"
- title: "항해 목적 선택"
- description: "물물교환 물류, 중범선 성장, 해양 사냥, 오킬루아 루틴, 판옥선·상위 선박, 대양 탐험 중 이번 항해의 목적을 먼저 고른다."
- structured_value:

```json
{
  "goals": [
    "barter_logistics",
    "carrack_progression",
    "ocean_hunting",
    "oquilla_routines",
    "panokseon_or_advanced_ship",
    "ocean_exploration"
  ],
  "knowledge_role": "strategy",
  "single_default_goal": false,
  "universal_ship_first": false
}
```

### `sailing-onboarding-strategy.departure-readiness`

- seed_key: "sailing-onboarding-strategy.departure-readiness"
- kind: "other"
- requirement_level: "required"
- title: "출항 준비 상태"
- description: "출항 전 선박 식량·포탄·내구도, 선원 건강·선실, 화물 무게, 재고 계획, 보급·수리 필요와 귀환 항구를 함께 점검한다."
- structured_value:

```json
{
  "creates_checklist_template": false,
  "dimensions": [
    "ship_food",
    "cannon_ammo",
    "ship_durability",
    "sailor_health",
    "crew_slots",
    "cargo_weight",
    "inventory_plan",
    "repair_or_supply_need",
    "return_port"
  ],
  "knowledge_role": "strategy"
}
```

### `sailing-onboarding-strategy.carrack-choice`

- seed_key: "sailing-onboarding-strategy.carrack-choice"
- kind: "other"
- requirement_level: "required"
- title: "목적별 중범선 선택"
- description: "물물교환, 해양 전투, 속도·회전·적재 선호, 현재 보유 선박과 장기 목표를 비교하고 기존 중범선 FACT에서 맞는 분기를 확인한다."
- structured_value:

```json
{
  "dimensions": [
    "barter_focus",
    "ocean_combat_focus",
    "speed_turn_cargo_preference",
    "current_ship",
    "long_term_progression_goal"
  ],
  "exact_stats_owned_by": "carrack-types",
  "knowledge_role": "strategy",
  "universal_best_carrack": false
}
```

### `sailing-onboarding-strategy.sailor-investment`

- seed_key: "sailing-onboarding-strategy.sailor-investment"
- kind: "other"
- requirement_level: "required"
- title: "선원 투자 시점"
- description: "현재 목적과 선실에서 필요한 역할부터 배치하고, 건강·식량 또는 역할 부족이 반복 루틴을 막을 때 선원 투자를 선박 성장과 비교한다."
- structured_value:

```json
{
  "dimensions": [
    "voyage_goal",
    "crew_slots",
    "required_roles",
    "health_or_food_interruptions",
    "ship_progression_bottleneck"
  ],
  "fixed_best_in_slot": false,
  "knowledge_role": "strategy",
  "universal_best_crew": false
}
```

### `sailing-onboarding-strategy.first-voyage-scope`

- seed_key: "sailing-onboarding-strategy.first-voyage-scope"
- kind: "other"
- requirement_level: "required"
- title: "첫 항해 범위"
- description: "첫 세션은 한 가지 짧은 목표로 제한하고 이동·적재·전투 중 실제 병목을 기록해 다음 세션에서 하나만 개선한다."
- structured_value:

```json
{
  "first_session": "one_short_goal",
  "improvement_per_session": 1,
  "knowledge_role": "strategy",
  "observe": [
    "movement",
    "cargo",
    "combat",
    "supply"
  ]
}
```

## Steps

### `sailing-onboarding-strategy.step.choose-goal`

- seed_key: "sailing-onboarding-strategy.step.choose-goal"
- phase: "preparation"
- order_no: 1
- title: "이번 항해 목적 정하기"
- description: "물류·성장·사냥·루틴·탐험 중 이번 세션의 목적 하나를 고른다."
- checkable: false

### `sailing-onboarding-strategy.step.check-ship-progression`

- seed_key: "sailing-onboarding-strategy.step.check-ship-progression"
- phase: "preparation"
- order_no: 2
- title: "선박과 성장 단계 확인"
- description: "사용할 선박과 현재 증축·장비 진행 상태를 확인한다."
- checkable: false

### `sailing-onboarding-strategy.step.check-wharf-registration`

- seed_key: "sailing-onboarding-strategy.step.check-wharf-registration"
- phase: "preparation"
- order_no: 3
- title: "선착장 등록 상태 확인"
- description: "선박이 현재 선착장에 등록되어 출항 가능한지 확인한다."
- checkable: false

### `sailing-onboarding-strategy.step.supply-and-repair`

- seed_key: "sailing-onboarding-strategy.step.supply-and-repair"
- phase: "preparation"
- order_no: 4
- title: "보급·수리 상태 확인"
- description: "식량, 포탄, 내구도와 필요한 수리·보급을 출항 전에 확인한다."
- checkable: false

### `sailing-onboarding-strategy.step.check-crew-and-cargo`

- seed_key: "sailing-onboarding-strategy.step.check-crew-and-cargo"
- phase: "preparation"
- order_no: 5
- title: "선원과 화물 확인"
- description: "목적에 필요한 선원, 선실 여유, 건강과 화물 무게를 확인한다."
- checkable: false

### `sailing-onboarding-strategy.step.set-short-target`

- seed_key: "sailing-onboarding-strategy.step.set-short-target"
- phase: "first_time"
- order_no: 6
- title: "짧은 목표 설정"
- description: "첫 항해에는 한 가지 짧은 목표와 귀환 항구만 정한다."
- checkable: false

### `sailing-onboarding-strategy.step.observe-bottleneck`

- seed_key: "sailing-onboarding-strategy.step.observe-bottleneck"
- phase: "first_time"
- order_no: 7
- title: "실제 병목 확인"
- description: "이동·적재·전투·보급 중 시간을 막은 병목을 하나 기록한다."
- checkable: false

### `sailing-onboarding-strategy.step.return-and-organize`

- seed_key: "sailing-onboarding-strategy.step.return-and-organize"
- phase: "maintenance"
- order_no: 8
- title: "복귀 후 정리"
- description: "항구로 돌아와 보급·수리하고 화물과 재고를 목적에 맞게 정리한다."
- checkable: false

### `sailing-onboarding-strategy.step.improve-one-bottleneck`

- seed_key: "sailing-onboarding-strategy.step.improve-one-bottleneck"
- phase: "maintenance"
- order_no: 9
- title: "다음 세션 개선"
- description: "선박, 장비, 선원, 화물 계획 중 가장 먼저 막힌 한 가지를 개선한다."
- checkable: false

## Schedules

- None

## Rewards

- None

## Sections

### `sailing-onboarding-strategy.section.goal-and-ship`

- seed_key: "sailing-onboarding-strategy.section.goal-and-ship"
- section_type: "strategy"
- title: "목적에서 선박 성장으로 연결"
- order_no: 1

#### body_markdown

선박을 먼저 정답으로 고르지 않는다. 이번 활동이 물물교환, 전투, 루틴, 탐험 중 무엇인지 정한 뒤 현재 선박으로 가능한 짧은 목표를 실행하고, 중범선 분기와 상위 장비는 확인된 병목에 맞춰 검토한다.

### `sailing-onboarding-strategy.section.departure-return-loop`

- seed_key: "sailing-onboarding-strategy.section.departure-return-loop"
- section_type: "strategy"
- title: "출항과 귀환을 한 루프로 운영"
- order_no: 2

#### body_markdown

출항 전 식량·포탄·내구도·선원·화물·귀환 항구를 확인하고, 복귀 후 보급·수리·재고 정리를 마쳐 다음 세션의 준비 상태를 만든다. 이 조건부 점검은 새 반복 체크리스트를 생성하지 않는다.

### `sailing-onboarding-strategy.section.common-mistakes`

- seed_key: "sailing-onboarding-strategy.section.common-mistakes"
- section_type: "common_mistakes"
- title: "항해 입문에서 피할 판단"
- order_no: 3

#### body_markdown

목적 없이 선박 증축부터 진행하거나, 보급·수리·선원 상태를 확인하지 않고 출항하지 않는다. 과거 치로 장비나 오래된 선원 조합을 현재의 보편적 최종 세팅으로 보지 않으며, 특정 중범선을 모든 목적의 최선으로 고정하지 않는다. 적재량과 귀환 경로 없이 해상 활동 범위를 늘리지 않는다.

## Related Contents

### `sailing-onboarding-strategy.carrack-types`

- seed_key: "sailing-onboarding-strategy.carrack-types"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "carrack-types"
- content_name_ko: "에페리아 중범선 네 종류"
- content_category: "ocean_project"
- note: "목적별 중범선 분기 FACT"
- order_no: 1
- relative_path: "../contents/carrack-types.md"
### `sailing-onboarding-strategy.sailor-growth`

- seed_key: "sailing-onboarding-strategy.sailor-growth"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sailor-hiring-growth"
- content_name_ko: "선원 고용과 성장"
- content_category: "ocean_guide"
- note: "선원 고용과 성장"
- order_no: 2
- relative_path: "../contents/sailor-hiring-growth.md"
### `sailing-onboarding-strategy.sailor-roles`

- seed_key: "sailing-onboarding-strategy.sailor-roles"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sailor-role-slots"
- content_name_ko: "선원 역할 슬롯"
- content_category: "ocean_guide"
- note: "목적별 선원 역할과 선실"
- order_no: 3
- relative_path: "../contents/sailor-role-slots.md"
### `sailing-onboarding-strategy.sailor-health`

- seed_key: "sailing-onboarding-strategy.sailor-health"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sailor-health-food"
- content_name_ko: "선원 건강과 식량"
- content_category: "ocean_guide"
- note: "선원 건강과 식량"
- order_no: 4
- relative_path: "../contents/sailor-health-food.md"
### `sailing-onboarding-strategy.consumables`

- seed_key: "sailing-onboarding-strategy.consumables"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "ocean-consumables"
- content_name_ko: "현행 항해·교역 소비품"
- content_category: "ocean_guide"
- note: "출항 보급품"
- order_no: 5
- relative_path: "../contents/ocean-consumables.md"
### `sailing-onboarding-strategy.upgrade-materials`

- seed_key: "sailing-onboarding-strategy.upgrade-materials"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "carrack-upgrade-materials"
- content_name_ko: "중범선 분기별 증축 핵심 재료"
- content_category: "ocean_project"
- note: "중범선 증축 재료"
- order_no: 6
- relative_path: "../contents/carrack-upgrade-materials.md"
### `sailing-onboarding-strategy.sea-crystals`

- seed_key: "sailing-onboarding-strategy.sea-crystals"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sea-crystals"
- content_name_ko: "해원석 progression"
- content_category: "ocean_project"
- note: "상위 장비 선택지"
- order_no: 7
- relative_path: "../contents/sea-crystals.md"
### `sailing-onboarding-strategy.advance-project`

- seed_key: "sailing-onboarding-strategy.advance-project"
- direction: "outgoing"
- relation_type: "project_link"
- content_slug: "carrack-advance"
- content_name_ko: "에페리아 중범선 : 점진"
- content_category: "ocean_project"
- note: "점진 프로젝트 진행도"
- order_no: 8
- relative_path: "../contents/carrack-advance.md"
### `sailing-onboarding-strategy.ocean-hunting`

- seed_key: "sailing-onboarding-strategy.ocean-hunting"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sea-crocodile-hunting"
- content_name_ko: "바다 악어 사냥"
- content_category: "ocean_guide"
- note: "해양 사냥 목적"
- order_no: 9
- relative_path: "../contents/sea-crocodile-hunting.md"
### `sailing-onboarding-strategy.panokseon`

- seed_key: "sailing-onboarding-strategy.panokseon"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "panokseon"
- content_name_ko: "판옥선"
- content_category: "ocean_guide"
- note: "판옥선·상위 선박 목적"
- order_no: 10
- relative_path: "../contents/panokseon.md"

## Evidence and Sources

### Current evidence

### `sailing-onboarding-strategy.claim.purpose::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.purpose::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "sailing-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.purpose::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.purpose::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "sailing-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.purpose::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.purpose::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "sailing-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.purpose::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.purpose::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "sailing-onboarding-strategy"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.summary::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.summary::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "sailing-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.summary::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.summary::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "sailing-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.summary::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.summary::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "sailing-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.summary::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.summary::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "sailing-onboarding-strategy"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.carrack-choice::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.carrack-choice::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.carrack-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.carrack-choice::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.carrack-choice::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.carrack-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.carrack-choice::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.carrack-choice::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.carrack-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.carrack-choice::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.carrack-choice::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.carrack-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.departure-readiness::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.departure-readiness::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.departure-readiness"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.departure-readiness::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.departure-readiness::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.departure-readiness"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.departure-readiness::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.departure-readiness::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.departure-readiness"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.departure-readiness::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.departure-readiness::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.departure-readiness"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.first-voyage-scope::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.first-voyage-scope::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.first-voyage-scope"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.first-voyage-scope::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.first-voyage-scope::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.first-voyage-scope"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.first-voyage-scope::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.first-voyage-scope::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.first-voyage-scope"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.first-voyage-scope::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.first-voyage-scope::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.first-voyage-scope"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.purpose-choice::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.purpose-choice::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.purpose-choice::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.purpose-choice::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.purpose-choice::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.purpose-choice::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.purpose-choice::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.purpose-choice::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.purpose-choice"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.sailor-investment::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.sailor-investment::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.sailor-investment"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.sailor-investment::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.sailor-investment::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.sailor-investment"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.sailor-investment::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.sailor-investment::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.sailor-investment"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.sailor-investment::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.sailor-investment::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailing-onboarding-strategy.sailor-investment"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.section.common-mistakes::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.section.common-mistakes::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "sailing-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.section.common-mistakes::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.section.common-mistakes::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "sailing-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.section.common-mistakes::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.section.common-mistakes::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "sailing-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.section.common-mistakes::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.section.common-mistakes::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "sailing-onboarding-strategy.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.section.departure-return-loop::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.section.departure-return-loop::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "sailing-onboarding-strategy.section.departure-return-loop"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.section.departure-return-loop::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.section.departure-return-loop::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "sailing-onboarding-strategy.section.departure-return-loop"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.section.departure-return-loop::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.section.departure-return-loop::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "sailing-onboarding-strategy.section.departure-return-loop"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.section.departure-return-loop::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.section.departure-return-loop::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "sailing-onboarding-strategy.section.departure-return-loop"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.section.goal-and-ship::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.section.goal-and-ship::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "sailing-onboarding-strategy.section.goal-and-ship"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.section.goal-and-ship::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.section.goal-and-ship::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "sailing-onboarding-strategy.section.goal-and-ship"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.section.goal-and-ship::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.section.goal-and-ship::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "sailing-onboarding-strategy.section.goal-and-ship"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.section.goal-and-ship::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.section.goal-and-ship::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "sailing-onboarding-strategy.section.goal-and-ship"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.check-crew-and-cargo::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.check-crew-and-cargo::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.check-crew-and-cargo"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.check-crew-and-cargo::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.check-crew-and-cargo::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.check-crew-and-cargo"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.check-crew-and-cargo::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.check-crew-and-cargo::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.check-crew-and-cargo"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.check-crew-and-cargo::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.check-crew-and-cargo::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.check-crew-and-cargo"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.check-ship-progression::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.check-ship-progression::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.check-ship-progression"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.check-ship-progression::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.check-ship-progression::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.check-ship-progression"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.check-ship-progression::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.check-ship-progression::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.check-ship-progression"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.check-ship-progression::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.check-ship-progression::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.check-ship-progression"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.check-wharf-registration::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.check-wharf-registration::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.check-wharf-registration"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.check-wharf-registration::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.check-wharf-registration::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.check-wharf-registration"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.check-wharf-registration::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.check-wharf-registration::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.check-wharf-registration"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.check-wharf-registration::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.check-wharf-registration::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.check-wharf-registration"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.choose-goal::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.choose-goal::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.choose-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.choose-goal::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.choose-goal::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.choose-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.choose-goal::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.choose-goal::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.choose-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.choose-goal::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.choose-goal::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.choose-goal"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.improve-one-bottleneck::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.improve-one-bottleneck::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.improve-one-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.improve-one-bottleneck::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.improve-one-bottleneck::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.improve-one-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.improve-one-bottleneck::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.improve-one-bottleneck::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.improve-one-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.improve-one-bottleneck::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.improve-one-bottleneck::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.improve-one-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.observe-bottleneck::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.observe-bottleneck::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.observe-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.observe-bottleneck::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.observe-bottleneck::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.observe-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.observe-bottleneck::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.observe-bottleneck::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.observe-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.observe-bottleneck::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.observe-bottleneck::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.observe-bottleneck"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.return-and-organize::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.return-and-organize::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.return-and-organize"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.return-and-organize::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.return-and-organize::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.return-and-organize"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.return-and-organize::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.return-and-organize::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.return-and-organize"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.return-and-organize::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.return-and-organize::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.return-and-organize"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.set-short-target::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.set-short-target::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.set-short-target"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.set-short-target::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.set-short-target::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.set-short-target"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.set-short-target::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.set-short-target::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.set-short-target"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.set-short-target::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.set-short-target::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.set-short-target"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.supply-and-repair::carrack-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.supply-and-repair::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.supply-and-repair"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.supply-and-repair::ocean-all-guide`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.supply-and-repair::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.supply-and-repair"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.supply-and-repair::ocean-progression-2026-08-26`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.supply-and-repair::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.supply-and-repair"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `sailing-onboarding-strategy.claim.step.supply-and-repair::sailing-academy-community-2026-06-14`

- evidence_seed_key: "sailing-onboarding-strategy.claim.step.supply-and-repair::sailing-academy-community-2026-06-14"
- source_id: "sailing-academy-community-2026-06-14"
- title: "아카데미 항해 강의."
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=153075"
- publisher: "흑귀하양-KR"
- source_type: "community_strategy"
- published_at: "2026-06-14"
- retrieved_at: "2026-09-07T04:45:55+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "sailing-onboarding-strategy.step.supply-and-repair"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
