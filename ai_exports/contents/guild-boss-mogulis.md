<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 모굴리스

## Identity

- slug: "guild-boss-mogulis"
- name_ko: "모굴리스"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "돌꼬리 황무지에서 하위 골렘과 무적 전환을 처리하는 길드 우두머리다."
- purpose: "현행 위치·핵심 패턴·공식 보상을 확인한다."

## Requirements

### `guild-boss-mogulis.raid`

- seed_key: "guild-boss-mogulis.raid"
- kind: "other"
- requirement_level: "required"
- title: "길드 레이드"
- description: "전용 지역에서 소환 권한을 가진 길드원이 소환한다."
- structured_value:

```json
{
  "dedicated_raid_region": true,
  "knowledge_role": "fact"
}
```

### `guild-boss-mogulis.mechanics`

- seed_key: "guild-boss-mogulis.mechanics"
- kind: "other"
- requirement_level: "required"
- title: "핵심 기믹"
- description: "하위 골렘 중 무적이며 야생 골렘 소환은 2026-06-17 이후 전투당 한 번이다."
- structured_value:

```json
{
  "invulnerable_with_golems": true,
  "knowledge_role": "fact",
  "location": "돌꼬리 황무지",
  "wild_golem_max": 1
}
```

### `guild-boss-mogulis.rewards`

- seed_key: "guild-boss-mogulis.rewards"
- kind: "other"
- requirement_level: "required"
- title: "공식 보상"
- description: "공식 공통 보상표를 사용하고 비공개 확률은 만들지 않는다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "reward_table": {
    "advice": [
      50,
      60,
      70,
      80,
      90,
      100
    ],
    "black_stone": [
      60,
      120
    ],
    "crystals": [
      "반역",
      "검은",
      "각성",
      "발타라"
    ],
    "gold_10": [
      20,
      50
    ],
    "gold_100": [
      15,
      30
    ],
    "gold_1000": [
      6,
      7
    ],
    "lightstone": 2,
    "marni_fuel": [
      4,
      8
    ],
    "pure_magical_mass": [
      5,
      10
    ]
  }
}
```

## Steps

### `guild-boss-mogulis.step.mechanic`

- seed_key: "guild-boss-mogulis.step.mechanic"
- phase: "preparation"
- order_no: 1
- title: "핵심 패턴 대응"
- description: "하위 골렘을 먼저 처치한다."
- checkable: false

## Schedules

- None

## Rewards

### `guild-boss-mogulis.reward.crystals`

- seed_key: "guild-boss-mogulis.reward.crystals"
- name: "정령의 수정 4종"
- reward_type: "crystal"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 1

### `guild-boss-mogulis.reward.materials`

- seed_key: "guild-boss-mogulis.reward.materials"
- name: "순수한 마력 덩어리 외 공식 재료"
- reward_type: "material"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "상세 수량은 structured reward_table"
- order_no: 2

### `guild-boss-mogulis.reward.advice`

- seed_key: "guild-boss-mogulis.reward.advice"
- name: "발크스의 조언 (+50~+100)"
- reward_type: "enhancement"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "비공개 확률 제외"
- order_no: 3

### `guild-boss-mogulis.reward.lightstone`

- seed_key: "guild-boss-mogulis.reward.lightstone"
- name: "찬란한 불/땅의 광명석"
- reward_type: "lightstone"
- amount: null
- min_amount: 2.0
- max_amount: 2.0
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 4

### `guild-boss-mogulis.reward.gold`

- seed_key: "guild-boss-mogulis.reward.gold"
- name: "금괴 1,000G/100G/10G"
- reward_type: "currency"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "6~7/15~30/20~50"
- order_no: 5

## Sections

### `guild-boss-mogulis.section.scope`

- seed_key: "guild-boss-mogulis.section.scope"
- section_type: "notes"
- title: "범위"
- order_no: 1

#### body_markdown

공통 소환·주간 횟수는 guild-boss-current-system에서 관리한다.

## Related Contents

### `guild-boss-mogulis.relation.system`

- seed_key: "guild-boss-mogulis.relation.system"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "guild-boss-current-system"
- content_name_ko: "길드 우두머리 현행 시스템"
- content_category: "combat_pve"
- note: "공통 규칙"
- order_no: 1
- relative_path: "../contents/guild-boss-current-system.md"

## Evidence and Sources

### Current evidence

### `guild-boss-mogulis.claim.purpose::farming-moles-2026-06-17`

- evidence_seed_key: "guild-boss-mogulis.claim.purpose::farming-moles-2026-06-17"
- source_id: "farming-moles-2026-06-17"
- title: "6월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15751"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-mogulis"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.purpose::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-mogulis.claim.purpose::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-mogulis"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.purpose::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-mogulis.claim.purpose::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-mogulis"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.rewards::farming-moles-2026-06-17`

- evidence_seed_key: "guild-boss-mogulis.claim.rewards::farming-moles-2026-06-17"
- source_id: "farming-moles-2026-06-17"
- title: "6월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15751"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-mogulis"
- claim_key: "rewards"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.rewards::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-mogulis.claim.rewards::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-mogulis"
- claim_key: "rewards"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.rewards::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-mogulis.claim.rewards::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-mogulis"
- claim_key: "rewards"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.summary::farming-moles-2026-06-17`

- evidence_seed_key: "guild-boss-mogulis.claim.summary::farming-moles-2026-06-17"
- source_id: "farming-moles-2026-06-17"
- title: "6월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15751"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-mogulis"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.summary::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-mogulis.claim.summary::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-mogulis"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.summary::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-mogulis.claim.summary::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-mogulis"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.mechanics::farming-moles-2026-06-17`

- evidence_seed_key: "guild-boss-mogulis.claim.mechanics::farming-moles-2026-06-17"
- source_id: "farming-moles-2026-06-17"
- title: "6월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15751"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-mogulis.mechanics"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.mechanics::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-mogulis.claim.mechanics::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-mogulis.mechanics"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.mechanics::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-mogulis.claim.mechanics::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-mogulis.mechanics"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.raid::farming-moles-2026-06-17`

- evidence_seed_key: "guild-boss-mogulis.claim.raid::farming-moles-2026-06-17"
- source_id: "farming-moles-2026-06-17"
- title: "6월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15751"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-mogulis.raid"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.raid::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-mogulis.claim.raid::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-mogulis.raid"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.raid::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-mogulis.claim.raid::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-mogulis.raid"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.section.scope::farming-moles-2026-06-17`

- evidence_seed_key: "guild-boss-mogulis.claim.section.scope::farming-moles-2026-06-17"
- source_id: "farming-moles-2026-06-17"
- title: "6월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15751"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-mogulis.section.scope"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.section.scope::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-mogulis.claim.section.scope::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-mogulis.section.scope"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.section.scope::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-mogulis.claim.section.scope::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-mogulis.section.scope"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.step.mechanic::farming-moles-2026-06-17`

- evidence_seed_key: "guild-boss-mogulis.claim.step.mechanic::farming-moles-2026-06-17"
- source_id: "farming-moles-2026-06-17"
- title: "6월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15751"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-mogulis.step.mechanic"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.step.mechanic::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-mogulis.claim.step.mechanic::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-mogulis.step.mechanic"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-mogulis.claim.step.mechanic::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-mogulis.claim.step.mechanic::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-mogulis.step.mechanic"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
