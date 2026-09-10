<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 페리드

## Identity

- slug: "guild-boss-ferrid"
- name_ko: "페리드"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "오마르 용암 동굴에서 전방 기절과 원거리 2연속 넉다운을 피하는 길드 우두머리다."
- purpose: "현행 위치·핵심 패턴·공식 보상을 확인한다."

## Requirements

### `guild-boss-ferrid.raid`

- seed_key: "guild-boss-ferrid.raid"
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

### `guild-boss-ferrid.mechanics`

- seed_key: "guild-boss-ferrid.mechanics"
- kind: "other"
- requirement_level: "required"
- title: "핵심 기믹"
- description: "뒤에서 공격하고 내려찍기 뒤 용암족을 처리한다."
- structured_value:

```json
{
  "attack_from_back": true,
  "knowledge_role": "fact",
  "lava_adds": true,
  "location": "오마르 용암 동굴",
  "ranged_knockdown_hits": 2
}
```

### `guild-boss-ferrid.rewards`

- seed_key: "guild-boss-ferrid.rewards"
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

### `guild-boss-ferrid.step.mechanic`

- seed_key: "guild-boss-ferrid.step.mechanic"
- phase: "preparation"
- order_no: 1
- title: "핵심 패턴 대응"
- description: "후방을 잡고 용암족을 처리한다."
- checkable: false

## Schedules

- None

## Rewards

### `guild-boss-ferrid.reward.crystals`

- seed_key: "guild-boss-ferrid.reward.crystals"
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

### `guild-boss-ferrid.reward.materials`

- seed_key: "guild-boss-ferrid.reward.materials"
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

### `guild-boss-ferrid.reward.advice`

- seed_key: "guild-boss-ferrid.reward.advice"
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

### `guild-boss-ferrid.reward.lightstone`

- seed_key: "guild-boss-ferrid.reward.lightstone"
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

### `guild-boss-ferrid.reward.gold`

- seed_key: "guild-boss-ferrid.reward.gold"
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

### `guild-boss-ferrid.section.scope`

- seed_key: "guild-boss-ferrid.section.scope"
- section_type: "notes"
- title: "범위"
- order_no: 1

#### body_markdown

공통 소환·주간 횟수는 guild-boss-current-system에서 관리한다.

## Related Contents

### `guild-boss-ferrid.relation.system`

- seed_key: "guild-boss-ferrid.relation.system"
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

### `guild-boss-ferrid.claim.purpose::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-ferrid.claim.purpose::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-ferrid"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-ferrid.claim.purpose::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-ferrid.claim.purpose::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-ferrid"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-ferrid.claim.rewards::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-ferrid.claim.rewards::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-ferrid"
- claim_key: "rewards"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-ferrid.claim.rewards::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-ferrid.claim.rewards::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-ferrid"
- claim_key: "rewards"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-ferrid.claim.summary::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-ferrid.claim.summary::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-ferrid"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-ferrid.claim.summary::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-ferrid.claim.summary::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-ferrid"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-ferrid.claim.mechanics::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-ferrid.claim.mechanics::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-ferrid.mechanics"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-ferrid.claim.mechanics::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-ferrid.claim.mechanics::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-ferrid.mechanics"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-ferrid.claim.raid::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-ferrid.claim.raid::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-ferrid.raid"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-ferrid.claim.raid::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-ferrid.claim.raid::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-ferrid.raid"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-ferrid.claim.section.scope::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-ferrid.claim.section.scope::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-ferrid.section.scope"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-ferrid.claim.section.scope::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-ferrid.claim.section.scope::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-ferrid.section.scope"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-ferrid.claim.step.mechanic::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-ferrid.claim.step.mechanic::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-ferrid.step.mechanic"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-ferrid.claim.step.mechanic::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-ferrid.claim.step.mechanic::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-ferrid.step.mechanic"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
