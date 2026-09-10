<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 5세대 반려동물과 대장

## Identity

- slug: "pet-fifth-generation"
- name_ko: "5세대 반려동물과 대장"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- party_type: "solo"
- difficulty: "medium"

## Overview

- summary: "4세대 반려동물의 5세대 훈련, 제왕의 깃털, 교환 잠금, 대장 임명과 현재 효과를 정리한다."
- purpose: "일반 교환이 끝난 반려동물만 안전하게 5세대로 훈련하고 대장 한 마리의 효과를 활용한다."

## Requirements

### `pet-fifth-generation.training`

- seed_key: "pet-fifth-generation.training"
- kind: "item"
- requirement_level: "required"
- title: "4세대에서 5세대 훈련"
- description: "제왕의 깃털을 소지한 상태에서 4세대 반려동물을 5세대로 훈련한다. 제왕의 깃털은 성장의 시약 10개, 마력의 파편 40개, 상급 가벼운 깃털 800개를 간이 연금해 만든다."
- structured_value:

```json
{
  "from_generation": 4,
  "knowledge_role": "fact",
  "processing": "간이 연금",
  "recipe": {
    "마력의 파편": 40,
    "상급 가벼운 깃털": 800,
    "성장의 시약": 10
  },
  "required_item": "제왕의 깃털",
  "to_generation": 5
}
```

### `pet-fifth-generation.exchange-lock`

- seed_key: "pet-fifth-generation.exchange-lock"
- kind: "other"
- requirement_level: "required"
- title: "훈련 후 교환 불가"
- description: "5세대 훈련을 마친 반려동물은 일반 반려동물 교환을 할 수 없다. 외형이나 기술을 교환으로 바꿀 계획은 훈련 전에 끝낸다."
- structured_value:

```json
{
  "appearance_changes_on_training": false,
  "exchange_after_training": false,
  "knowledge_role": "fact",
  "plan_appearance_before_training": true,
  "plan_skills_before_training": true
}
```

### `pet-fifth-generation.captain`

- seed_key: "pet-fifth-generation.captain"
- kind: "other"
- requirement_level: "required"
- title: "대장 임명"
- description: "5세대 반려동물 중 한 마리만 대장으로 임명할 수 있으며 다른 5세대 반려동물로 대장을 변경할 수 있다."
- structured_value:

```json
{
  "captain_can_change": true,
  "captain_limit": 1,
  "captain_requires_generation": 5,
  "knowledge_role": "fact"
}
```

### `pet-fifth-generation.captain-effects`

- seed_key: "pet-fifth-generation.captain-effects"
- kind: "other"
- requirement_level: "required"
- title: "대장 효과"
- description: "대장 반려동물을 꺼내면 함께 꺼낸 모든 반려동물의 전리품 획득 시간이 15% 감소하고 대장 자신의 고유 기술 레벨이 1 오른다. 특기는 강화되지 않는다."
- structured_value:

```json
{
  "captain_unique_skill_level_increase": 1,
  "knowledge_role": "fact",
  "specialty_increase": false,
  "summoned_pet_loot_time_reduction_percent": 15
}
```

### `pet-fifth-generation.non-captain`

- seed_key: "pet-fifth-generation.non-captain"
- kind: "other"
- requirement_level: "required"
- title: "비대장 5세대"
- description: "대장으로 임명하지 않은 5세대 반려동물은 일반 4세대 반려동물과 같은 능력치가 적용된다. 모든 반려동물을 5세대로 만드는 별도 성능 목표는 아니다."
- structured_value:

```json
{
  "all_pets_need_fifth_generation": false,
  "knowledge_role": "fact",
  "non_captain_fifth_generation_matches_generation": 4
}
```

## Steps

### `pet-fifth-generation.step.train`

- seed_key: "pet-fifth-generation.step.train"
- phase: "unlock"
- order_no: 3
- title: "5세대 훈련"
- description: "완성한 4세대 반려동물과 제왕의 깃털로 5세대 훈련을 진행한다."
- checkable: false

### `pet-fifth-generation.step.finish-exchange`

- seed_key: "pet-fifth-generation.step.finish-exchange"
- phase: "preparation"
- order_no: 1
- title: "일반 교환 계획 완료"
- description: "외형과 기술을 더 교환할 필요가 없는 4세대 반려동물인지 먼저 확인한다."
- checkable: false

### `pet-fifth-generation.step.prepare-feather`

- seed_key: "pet-fifth-generation.step.prepare-feather"
- phase: "preparation"
- order_no: 2
- title: "제왕의 깃털 준비"
- description: "공식 현재 제작식으로 제왕의 깃털을 준비한다."
- checkable: false

### `pet-fifth-generation.step.appoint-captain`

- seed_key: "pet-fifth-generation.step.appoint-captain"
- phase: "maintenance"
- order_no: 4
- title: "대장 한 마리 임명"
- description: "5세대 반려동물 중 실제 활동에 사용할 한 마리를 대장으로 임명한다."
- checkable: false

### `pet-fifth-generation.step.verify-group`

- seed_key: "pet-fifth-generation.step.verify-group"
- phase: "maintenance"
- order_no: 5
- title: "소환 그룹에서 효과 확인"
- description: "대장과 함께 꺼낸 반려동물의 전리품 획득 시간 감소와 대장 고유 기술 상승을 확인한다."
- checkable: false

## Schedules

- None

## Rewards

- None

## Sections

### `pet-fifth-generation.section.lifecycle`

- seed_key: "pet-fifth-generation.section.lifecycle"
- section_type: "overview"
- title: "교환이 끝난 뒤의 훈련"
- order_no: 1

#### body_markdown

일반 교환은 외형·기술 계승과 최대 4세대 결과를 다룬다. 5세대 훈련은 교환을 마친 4세대 한 마리를 대장 후보로 만드는 후속 단계이며 훈련 뒤 일반 교환은 잠긴다.

### `pet-fifth-generation.section.captain-boundary`

- seed_key: "pet-fifth-generation.section.captain-boundary"
- section_type: "notes"
- title: "대장은 한 마리"
- order_no: 2

#### body_markdown

대장 효과는 대장으로 임명해 꺼낸 한 마리와 함께 소환한 그룹에 적용된다. 대장이 아닌 5세대는 4세대와 같은 능력이고 특기는 대장 효과로 강화되지 않는다.

### `pet-fifth-generation.section.common-mistakes`

- seed_key: "pet-fifth-generation.section.common-mistakes"
- section_type: "common_mistakes"
- title: "훈련 전 교환 확인"
- order_no: 3

#### body_markdown

5세대 훈련 뒤에도 일반 교환이 가능하다고 가정하지 않는다. 외형과 기술 계승을 먼저 끝내고, 모든 반려동물을 5세대로 만드는 것을 필수 진행 목표로 두지 않는다.

## Related Contents

### `pet-fifth-generation.pet-current-system`

- seed_key: "pet-fifth-generation.pet-current-system"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "pet-current-system"
- content_name_ko: "반려동물 현재 시스템"
- content_category: "progression"
- note: "일반 반려동물 교환과 효과 구조를 먼저 이해"
- order_no: 1
- relative_path: "../contents/pet-current-system.md"
### `fairy-pet-setup-strategy.fifth-generation-facts`

- seed_key: "fairy-pet-setup-strategy.fifth-generation-facts"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "fairy-pet-setup-strategy"
- content_name_ko: "요정·반려동물 초기 설정 전략"
- content_category: "progression"
- note: "5세대 훈련과 교환 잠금 FACT를 판단 근거로 사용"
- order_no: 3
- relative_path: "../contents/fairy-pet-setup-strategy.md"

## Evidence and Sources

### Current evidence

### `pet-fifth-generation.claim.purpose::pet-fifth-generation-guide-current`

- evidence_seed_key: "pet-fifth-generation.claim.purpose::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "pet-fifth-generation"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-fifth-generation.claim.summary::pet-fifth-generation-guide-current`

- evidence_seed_key: "pet-fifth-generation.claim.summary::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "pet-fifth-generation"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-fifth-generation.claim.captain::pet-fifth-generation-guide-current`

- evidence_seed_key: "pet-fifth-generation.claim.captain::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "pet-fifth-generation.captain"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-fifth-generation.claim.captain-effects::pet-fifth-generation-guide-current`

- evidence_seed_key: "pet-fifth-generation.claim.captain-effects::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "pet-fifth-generation.captain-effects"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-fifth-generation.claim.exchange-lock::pet-fifth-generation-guide-current`

- evidence_seed_key: "pet-fifth-generation.claim.exchange-lock::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "pet-fifth-generation.exchange-lock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-fifth-generation.claim.non-captain::pet-fifth-generation-guide-current`

- evidence_seed_key: "pet-fifth-generation.claim.non-captain::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "pet-fifth-generation.non-captain"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-fifth-generation.claim.training::pet-fifth-generation-guide-current`

- evidence_seed_key: "pet-fifth-generation.claim.training::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "pet-fifth-generation.training"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-fifth-generation.claim.section.captain-boundary::pet-fifth-generation-guide-current`

- evidence_seed_key: "pet-fifth-generation.claim.section.captain-boundary::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "pet-fifth-generation.section.captain-boundary"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-fifth-generation.claim.section.common-mistakes::pet-fifth-generation-guide-current`

- evidence_seed_key: "pet-fifth-generation.claim.section.common-mistakes::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "pet-fifth-generation.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-fifth-generation.claim.section.lifecycle::pet-fifth-generation-guide-current`

- evidence_seed_key: "pet-fifth-generation.claim.section.lifecycle::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "pet-fifth-generation.section.lifecycle"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-fifth-generation.claim.section.lifecycle::pet-guide-current`

- evidence_seed_key: "pet-fifth-generation.claim.section.lifecycle::pet-guide-current"
- source_id: "pet-guide-current"
- title: "반려동물"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=180"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "pet-fifth-generation.section.lifecycle"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-fifth-generation.claim.step.appoint-captain::pet-fifth-generation-guide-current`

- evidence_seed_key: "pet-fifth-generation.claim.step.appoint-captain::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "pet-fifth-generation.step.appoint-captain"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-fifth-generation.claim.step.finish-exchange::pet-fifth-generation-guide-current`

- evidence_seed_key: "pet-fifth-generation.claim.step.finish-exchange::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "pet-fifth-generation.step.finish-exchange"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-fifth-generation.claim.step.prepare-feather::pet-fifth-generation-guide-current`

- evidence_seed_key: "pet-fifth-generation.claim.step.prepare-feather::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "pet-fifth-generation.step.prepare-feather"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-fifth-generation.claim.step.train::pet-fifth-generation-guide-current`

- evidence_seed_key: "pet-fifth-generation.claim.step.train::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "pet-fifth-generation.step.train"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `pet-fifth-generation.claim.step.verify-group::pet-fifth-generation-guide-current`

- evidence_seed_key: "pet-fifth-generation.claim.step.verify-group::pet-fifth-generation-guide-current"
- source_id: "pet-fifth-generation-guide-current"
- title: "5세대 반려동물 훈련"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=296"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-07T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "pet-fifth-generation.step.verify-group"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
