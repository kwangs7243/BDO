<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 대양의 눈동자 칸

## Identity

- slug: "khan-guild-boss"
- name_ko: "대양의 눈동자 칸"
- category: "ocean_guide"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "오킬루아의 눈 전용 지역에서 길드 대포와 흑결정 포탄으로 진행하는 현행 길드 우두머리다."
- purpose: "기존 stable ID를 유지하며 현행 소환·대포·회복 저지·보상을 확인한다."

## Requirements

### `khan-guild-boss.summon`

- seed_key: "khan-guild-boss.summon"
- kind: "other"
- requirement_level: "required"
- title: "길드 소환"
- description: "길드 의뢰로 소환 조각 5개를 모으며 소환 정보는 길드 우두머리 소환 UI에서 관리되고 일반 가방·창고에 저장되지 않는다."
- structured_value:

```json
{
  "inventory_item": false,
  "knowledge_role": "fact",
  "managed_in": "길드 우두머리 소환 UI",
  "source": "길드 의뢰",
  "summon_pieces": 5
}
```

### `khan-guild-boss.combat-tools`

- seed_key: "khan-guild-boss.combat-tools"
- kind: "other"
- requirement_level: "required"
- title: "전투 도구"
- description: "[길드] 괴수잡이 대포와 포탄을 사용하고 흑결정 해초로 회복을 저지한다."
- structured_value:

```json
{
  "equipment": [
    "[길드] 괴수잡이 대포 조립 세트",
    "[길드] 괴수잡이 포탄"
  ],
  "knowledge_role": "fact",
  "seaweed": {
    "drop": "흑결정 포탄",
    "purpose": "회복 저지"
  }
}
```

### `khan-guild-boss.death-penalty`

- seed_key: "khan-guild-boss.death-penalty"
- kind: "other"
- requirement_level: "required"
- title: "사망 불이익"
- description: "칸에게 사망해도 불이익이 없다."
- structured_value:

```json
{
  "death_penalty": false,
  "knowledge_role": "fact"
}
```

### `khan-guild-boss.access`

- seed_key: "khan-guild-boss.access"
- kind: "other"
- requirement_level: "required"
- title: "현행 접근"
- description: "오킬루아의 눈에서 기본 주 1회, 전용 지역으로 진행한다."
- structured_value:

```json
{
  "base_weekly": 1,
  "knowledge_role": "fact",
  "location": "오킬루아의 눈"
}
```

### `khan-guild-boss.cannon`

- seed_key: "khan-guild-boss.cannon"
- kind: "other"
- requirement_level: "required"
- title: "대포 운용"
- description: "대포는 설치 30분 또는 칸 공격으로 파괴되며 세 사격 방식을 사용한다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "lifetime_minutes": 30,
  "modes": [
    "일반",
    "과충전",
    "속사"
  ]
}
```

### `khan-guild-boss.seaweed`

- seed_key: "khan-guild-boss.seaweed"
- kind: "other"
- requirement_level: "required"
- title: "해초 기믹"
- description: "프라티가 보호하는 해초를 파괴해 강한 포탄을 얻고 회복을 막는다."
- structured_value:

```json
{
  "khan_heals_on_failure": true,
  "knowledge_role": "fact",
  "protected_by": "프라티"
}
```

## Steps

### `khan-guild-boss.step.cannon`

- seed_key: "khan-guild-boss.step.cannon"
- phase: "preparation"
- order_no: 1
- title: "대포 준비"
- description: "길드 대포와 포탄을 준비한다."
- checkable: false

### `khan-guild-boss.step.seaweed`

- seed_key: "khan-guild-boss.step.seaweed"
- phase: "first_time"
- order_no: 2
- title: "해초 파괴"
- description: "프라티와 해초를 처리한다."
- checkable: false

## Schedules

- None

## Rewards

### `khan-guild-boss.reward.upgrade-materials`

- seed_key: "khan-guild-boss.reward.upgrade-materials"
- name: "선박·장비 개량 재료"
- reward_type: "material"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "칸 처치 전리품 범주"
- order_no: 1

### `khan-guild-boss.reward.treasure`

- seed_key: "khan-guild-boss.reward.treasure"
- name: "대양 보물 관련 전리품"
- reward_type: "treasure"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "칸 처치 전리품 범주"
- order_no: 2

### `khan-guild-boss.reward.concentrated-magic`

- seed_key: "khan-guild-boss.reward.concentrated-magic"
- name: "응축된 칸의 마력"
- reward_type: "material"
- amount: null
- min_amount: 1.0
- max_amount: 1.0
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 3

### `khan-guild-boss.reward.current-table`

- seed_key: "khan-guild-boss.reward.current-table"
- name: "현행 공식 보상표"
- reward_type: "bundle"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "광명석·산호·진액·연료·크론석·블랙스톤·금괴·힘줄·비늘 등 공개 범위"
- order_no: 4

## Sections

### `khan-guild-boss.heart-recipes`

- seed_key: "khan-guild-boss.heart-recipes"
- section_type: "notes"
- title: "칸의 심장 제작 분기"
- order_no: 1

#### body_markdown

응축된 칸의 마력은 `칸의 심장 : 파괴`, `칸의 심장 : 수호`, `칸의 심장 : 생명` 제작식으로 이어진다.

### `khan-guild-boss.section.current-rewards`

- seed_key: "khan-guild-boss.section.current-rewards"
- section_type: "notes"
- title: "현행 보상"
- order_no: 2

#### body_markdown

공식 가이드의 공개 수량 범위만 사용한다.

## Related Contents

### `khan-guild-boss.relation.oquilla`

- seed_key: "khan-guild-boss.relation.oquilla"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "ocean-first-mates"
- content_name_ko: "대양 부선장"
- content_category: "ocean_guide"
- note: "오킬루아의 눈 접근과 대양 의뢰 흐름"
- order_no: 1
- relative_path: "../contents/ocean-first-mates.md"
### `khan-guild-boss.relation.system`

- seed_key: "khan-guild-boss.relation.system"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "guild-boss-current-system"
- content_name_ko: "길드 우두머리 현행 시스템"
- content_category: "combat_pve"
- note: "현행 공통 규칙"
- order_no: 2
- relative_path: "../contents/guild-boss-current-system.md"

## Evidence and Sources

### Current evidence

### `khan-guild-boss.claim.purpose::guild-boss-guide-current`

- evidence_seed_key: "khan-guild-boss.claim.purpose::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "khan-guild-boss"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `khan-guild-boss.evidence.rewards::guild-boss-guide-current`

- evidence_seed_key: "khan-guild-boss.evidence.rewards::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "khan-guild-boss"
- claim_key: "rewards"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "칸 전리품과 응축된 칸의 마력"
- active: true
- is_active: true

### `khan-guild-boss.evidence.rewards::ocean-all-guide`

- evidence_seed_key: "khan-guild-boss.evidence.rewards::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "khan-guild-boss"
- claim_key: "rewards"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "칸 전리품과 응축된 칸의 마력"
- active: true
- is_active: true

### `khan-guild-boss.claim.summary::guild-boss-guide-current`

- evidence_seed_key: "khan-guild-boss.claim.summary::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "khan-guild-boss"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `khan-guild-boss.claim.access::guild-boss-guide-current`

- evidence_seed_key: "khan-guild-boss.claim.access::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "khan-guild-boss.access"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `khan-guild-boss.claim.cannon::guild-boss-guide-current`

- evidence_seed_key: "khan-guild-boss.claim.cannon::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "khan-guild-boss.cannon"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `khan-guild-boss.evidence.combat-tools::guild-boss-guide-current`

- evidence_seed_key: "khan-guild-boss.evidence.combat-tools::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "khan-guild-boss.combat-tools"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "길드 대포·흑결정 해초·회복 저지"
- active: true
- is_active: true

### `khan-guild-boss.evidence.combat-tools::ocean-all-guide`

- evidence_seed_key: "khan-guild-boss.evidence.combat-tools::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "khan-guild-boss.combat-tools"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "길드 대포·흑결정 해초·회복 저지"
- active: true
- is_active: true

### `khan-guild-boss.evidence.death-penalty::ocean-all-guide`

- evidence_seed_key: "khan-guild-boss.evidence.death-penalty::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "khan-guild-boss.death-penalty"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "칸 사망 시 불이익 없음"
- active: true
- is_active: true

### `khan-guild-boss.claim.seaweed::guild-boss-guide-current`

- evidence_seed_key: "khan-guild-boss.claim.seaweed::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "khan-guild-boss.seaweed"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `khan-guild-boss.evidence.summon::guild-boss-guide-current`

- evidence_seed_key: "khan-guild-boss.evidence.summon::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "khan-guild-boss.summon"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "소환 조각 5개와 길드 우두머리 UI 관리"
- active: true
- is_active: true

### `khan-guild-boss.evidence.summon::ocean-all-guide`

- evidence_seed_key: "khan-guild-boss.evidence.summon::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "khan-guild-boss.summon"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "소환 조각 5개와 길드 우두머리 UI 관리"
- active: true
- is_active: true

### `khan-guild-boss.evidence.hearts::ocean-all-guide`

- evidence_seed_key: "khan-guild-boss.evidence.hearts::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "khan-guild-boss.heart-recipes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "파괴·수호·생명 심장 제작 분기"
- active: true
- is_active: true

### `khan-guild-boss.claim.section.current-rewards::guild-boss-guide-current`

- evidence_seed_key: "khan-guild-boss.claim.section.current-rewards::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "khan-guild-boss.section.current-rewards"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `khan-guild-boss.claim.step.cannon::guild-boss-guide-current`

- evidence_seed_key: "khan-guild-boss.claim.step.cannon::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "khan-guild-boss.step.cannon"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `khan-guild-boss.claim.step.seaweed::guild-boss-guide-current`

- evidence_seed_key: "khan-guild-boss.claim.step.seaweed::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "khan-guild-boss.step.seaweed"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
