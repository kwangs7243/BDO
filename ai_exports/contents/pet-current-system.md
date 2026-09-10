<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 반려동물 현재 시스템

## Identity

- slug: "pet-current-system"
- name_ko: "반려동물 현재 시스템"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- party_type: "solo"
- difficulty: "easy"

## Overview

- summary: "반려동물의 현재 획득과 등록, 행동 방식, 배고픔, 특기와 기술, 목적별 그룹, 일반 교환 규칙을 정리한다."
- purpose: "전리품 획득과 활동별 편의 효과를 이해하고 보유 반려동물을 안전하게 구성한다."

## Requirements

### `pet-current-system.acquisition`

- seed_key: "pet-current-system.acquisition"
- kind: "quest"
- requirement_level: "required"
- title: "획득과 등록"
- description: "반려동물은 의뢰 등으로 획득할 수 있으며 추천 의뢰 '[모험 지원] 반려동물, 모험의 동반자'의 보상은 가문당 한 번만 받을 수 있다. 획득한 반려동물 등록증을 사용해 이름을 정하고 등록한다."
- structured_value:

```json
{
  "full_quest_catalog_in_scope": false,
  "knowledge_role": "fact",
  "quest_acquisition_available": true,
  "quest_rewards_family_once": true,
  "recommended_quest_category": "[모험 지원] 반려동물, 모험의 동반자",
  "registration_item": "반려동물 등록증"
}
```

### `pet-current-system.action-mode`

- seed_key: "pet-current-system.action-mode"
- kind: "other"
- requirement_level: "required"
- title: "행동 방식"
- description: "행동 방식은 신중함, 보통, 기민함으로 나뉜다. 빠른 행동 방식일수록 전리품 획득 주기가 빨라지고 배고픔도 더 빠르게 소모된다."
- structured_value:

```json
{
  "faster_mode_increases_hunger_use": true,
  "faster_mode_increases_loot_frequency": true,
  "knowledge_role": "fact",
  "modes": [
    "신중함",
    "보통",
    "기민함"
  ]
}
```

### `pet-current-system.hunger`

- seed_key: "pet-current-system.hunger"
- kind: "item"
- requirement_level: "required"
- title: "배고픔과 먹이"
- description: "배고픔이 0이 되면 반려동물은 전리품을 줍지 않고 특기도 사용하지 않는다. 마구간지기 또는 거래소에서 구할 수 있는 먹이로 배고픔을 회복한다."
- structured_value:

```json
{
  "current_feed_price_in_scope": false,
  "feed_restores_hunger": true,
  "knowledge_role": "fact",
  "zero_hunger_disables_specialty": true,
  "zero_hunger_stops_loot": true
}
```

### `pet-current-system.specialty`

- seed_key: "pet-current-system.specialty"
- kind: "other"
- requirement_level: "required"
- title: "특기와 중첩"
- description: "특기는 일반 기술과 별도 기능이다. 채집물 탐지, 적대 모험가 탐지, 몬스터 도발, 희귀 몬스터 탐지는 함께 꺼낸 반려동물 수만큼 적용되지만 자동 낚시 시간 감소, 사막 질병 저항, 채집량 증가는 여러 마리를 꺼내도 하나만 적용된다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "non_stacking_specialties": [
    "자동 낚시 시간 감소",
    "사막 질병 저항",
    "채집량 증가"
  ],
  "separate_from_skills": true,
  "stacking_specialties": [
    "채집물 탐지",
    "적대 모험가 탐지",
    "몬스터 도발",
    "희귀 몬스터 탐지"
  ]
}
```

### `pet-current-system.skills`

- seed_key: "pet-current-system.skills"
- kind: "other"
- requirement_level: "required"
- title: "고유 기술과 주 기술"
- description: "반려동물 기술은 고유 기술과 주 기술로 구분되며 세대에 따라 습득할 수 있는 주 기술 수가 달라진다. 이번 데이터는 반려동물별 전체 기술 목록을 만들지 않는다."
- structured_value:

```json
{
  "full_pet_skill_catalog_in_scope": false,
  "knowledge_role": "fact",
  "main_skill_slots_depend_on_generation": true,
  "skill_categories": [
    "고유 기술",
    "주 기술"
  ]
}
```

### `pet-current-system.groups`

- seed_key: "pet-current-system.groups"
- kind: "other"
- requirement_level: "optional"
- title: "목적별 그룹"
- description: "반려동물 메뉴에서 보유 반려동물을 활동 목적에 맞는 그룹으로 묶고 그룹 단위로 맡기거나 찾을 수 있다."
- structured_value:

```json
{
  "group_summon_supported": true,
  "knowledge_role": "fact",
  "purpose_groups_supported": true,
  "universal_group_composition": false
}
```

### `pet-current-system.exchange`

- seed_key: "pet-current-system.exchange"
- kind: "other"
- requirement_level: "required"
- title: "일반 반려동물 교환"
- description: "일반 교환은 최대 5마리까지 등록하고 결과 반려동물의 외형과 기술 계승 대상을 선택할 수 있으며 결과는 최대 4세대다. 클래식·레어·스페셜·이벤트 중 같은 교환 유형끼리만 교환한다."
- structured_value:

```json
{
  "exchange_types": [
    "클래식",
    "레어",
    "스페셜",
    "이벤트"
  ],
  "full_probability_matrix_in_scope": false,
  "inheritance_choices": [
    "외형",
    "기술"
  ],
  "knowledge_role": "fact",
  "max_registered_pets": 5,
  "max_result_generation": 4,
  "same_exchange_type_required": true
}
```

## Steps

### `pet-current-system.step.register`

- seed_key: "pet-current-system.step.register"
- phase: "unlock"
- order_no: 2
- title: "반려동물 등록"
- description: "획득한 반려동물 등록증을 사용하고 이름을 정해 가문에 등록한다."
- checkable: false

### `pet-current-system.step.review-owned`

- seed_key: "pet-current-system.step.review-owned"
- phase: "preparation"
- order_no: 1
- title: "보유 반려동물 확인"
- description: "반려동물 메뉴를 열어 세대, 교환 유형, 특기와 기술을 확인한다."
- checkable: false

### `pet-current-system.step.choose-mode`

- seed_key: "pet-current-system.step.choose-mode"
- phase: "preparation"
- order_no: 3
- title: "행동 방식 선택"
- description: "전리품 획득 주기와 배고픔 소모의 균형에 맞춰 신중함·보통·기민함을 선택한다."
- checkable: false

### `pet-current-system.step.compare-effects`

- seed_key: "pet-current-system.step.compare-effects"
- phase: "preparation"
- order_no: 5
- title: "특기와 기술 구분"
- description: "활동에 필요한 효과가 특기인지 고유 기술인지 주 기술인지 구분하고 특기의 중첩 여부를 확인한다."
- checkable: false

### `pet-current-system.step.make-groups`

- seed_key: "pet-current-system.step.make-groups"
- phase: "preparation"
- order_no: 6
- title: "목적별 그룹 구성"
- description: "전투·생활·지식·탑승물 등 실제 활동 목적에 맞춰 보유 반려동물 그룹을 구성한다."
- checkable: false

### `pet-current-system.step.plan-exchange`

- seed_key: "pet-current-system.step.plan-exchange"
- phase: "preparation"
- order_no: 7
- title: "교환 전에 계승 계획"
- description: "같은 교환 유형인지 확인하고 외형과 기술 중 무엇을 계승할지 정한 뒤 일반 교환을 진행한다."
- checkable: false

### `pet-current-system.step.feed`

- seed_key: "pet-current-system.step.feed"
- phase: "maintenance"
- order_no: 4
- title: "배고픔 관리"
- description: "전리품 획득과 특기가 멈추기 전에 먹이로 배고픔을 회복한다."
- checkable: false

## Schedules

- None

## Rewards

- None

## Sections

### `pet-current-system.section.system-boundary`

- seed_key: "pet-current-system.section.system-boundary"
- section_type: "overview"
- title: "일반 교환과 5세대 훈련의 경계"
- order_no: 1

#### body_markdown

일반 교환은 최대 4세대 결과와 외형·기술 계승을 다루고, 5세대 훈련은 완성한 4세대 반려동물을 대장 후보로 바꾸는 별도 수명주기다.

### `pet-current-system.section.activity-setup`

- seed_key: "pet-current-system.section.activity-setup"
- section_type: "notes"
- title: "활동별 설정 기준"
- order_no: 2

#### body_markdown

행동 방식은 전리품 획득 주기와 배고픔 소모를 함께 바꾸며, 특기 중에는 중첩되는 것과 한 마리만 적용되는 것이 있다. 목적별 그룹은 보유 효과와 실제 활동을 기준으로 구성한다.

### `pet-current-system.section.common-mistakes`

- seed_key: "pet-current-system.section.common-mistakes"
- section_type: "common_mistakes"
- title: "중첩과 수명주기 혼동 방지"
- order_no: 3

#### body_markdown

모든 특기가 중첩된다고 가정하거나 배고픔 0에서도 전리품 획득과 특기가 유지된다고 보지 않는다. 일반 교환과 5세대 훈련을 같은 작업으로 취급하지 않고 상업 패키지나 이벤트 반려동물을 영구 진행 경로로 저장하지 않는다.

## Related Contents

### `pet-current-system.account-progression`

- seed_key: "pet-current-system.account-progression"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "account-progression-foundation"
- content_name_ko: "가문 성장 기반"
- content_category: "progression"
- note: "가문 단위 반려동물 등록과 성장 기반"
- order_no: 1
- relative_path: "../contents/account-progression-foundation.md"
### `pet-current-system.family-convenience`

- seed_key: "pet-current-system.family-convenience"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "family-convenience-unlock-foundation"
- content_name_ko: "가문 편의 기능 해금"
- content_category: "progression"
- note: "가문 편의 해금 흐름과 연결"
- order_no: 2
- relative_path: "../contents/family-convenience-unlock-foundation.md"
### `pet-current-system.life-family-levels`

- seed_key: "pet-current-system.life-family-levels"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-family-levels"
- content_name_ko: "가문 통합 생활 레벨"
- content_category: "life"
- note: "생활 활동 목적별 특기와 기술 구성"
- order_no: 3
- relative_path: "../contents/life-family-levels.md"
### `pet-current-system.energy-knowledge`

- seed_key: "pet-current-system.energy-knowledge"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "energy-foundation"
- content_name_ko: "기운 기반"
- content_category: "life"
- note: "지식 획득 관련 반려동물 효과를 검토할 때 연결"
- order_no: 4
- relative_path: "../contents/energy-foundation.md"
### `pet-fifth-generation.pet-current-system`

- seed_key: "pet-fifth-generation.pet-current-system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "pet-fifth-generation"
- content_name_ko: "5세대 반려동물과 대장"
- content_category: "progression"
- note: "일반 반려동물 교환과 효과 구조를 먼저 이해"
- order_no: 1
- relative_path: "../contents/pet-fifth-generation.md"
### `fairy-pet-setup-strategy.pet-facts`

- seed_key: "fairy-pet-setup-strategy.pet-facts"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "fairy-pet-setup-strategy"
- content_name_ko: "요정·반려동물 초기 설정 전략"
- content_category: "progression"
- note: "현재 반려동물 시스템 FACT를 판단 근거로 사용"
- order_no: 2
- relative_path: "../contents/fairy-pet-setup-strategy.md"

## Evidence and Sources

### Current evidence

### `pet-current-system.claim.purpose::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.purpose::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "pet-current-system"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.summary::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.summary::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "pet-current-system"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.acquisition::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.acquisition::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "pet-current-system.acquisition"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.action-mode::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.action-mode::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "pet-current-system.action-mode"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.exchange::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.exchange::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "pet-current-system.exchange"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.groups::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.groups::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "pet-current-system.groups"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.hunger::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.hunger::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "pet-current-system.hunger"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.skills::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.skills::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "pet-current-system.skills"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.specialty::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.specialty::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "pet-current-system.specialty"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.section.activity-setup::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.section.activity-setup::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "pet-current-system.section.activity-setup"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.section.common-mistakes::pet-fifth-generation-guide-current`

- evidence_seed_key: "pet-current-system.claim.section.common-mistakes::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "pet-current-system.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.section.common-mistakes::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.section.common-mistakes::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "pet-current-system.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.section.system-boundary::pet-fifth-generation-guide-current`

- evidence_seed_key: "pet-current-system.claim.section.system-boundary::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "pet-current-system.section.system-boundary"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.section.system-boundary::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.section.system-boundary::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "pet-current-system.section.system-boundary"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.step.choose-mode::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.step.choose-mode::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "pet-current-system.step.choose-mode"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.step.compare-effects::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.step.compare-effects::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "pet-current-system.step.compare-effects"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.step.feed::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.step.feed::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "pet-current-system.step.feed"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.step.make-groups::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.step.make-groups::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "pet-current-system.step.make-groups"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.step.plan-exchange::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.step.plan-exchange::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "pet-current-system.step.plan-exchange"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.step.register::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.step.register::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "pet-current-system.step.register"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-current-system.claim.step.review-owned::pet-guide-current`

- evidence_seed_key: "pet-current-system.claim.step.review-owned::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "pet-current-system.step.review-owned"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
