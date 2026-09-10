<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 오르그

## Identity

- slug: "guild-boss-orgg"
- name_ko: "오르그"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "글리시 서쪽 절벽에서 광역 화염과 안전 지대를 판독하는 길드 우두머리다."
- purpose: "현행 위치·핵심 패턴·공식 보상을 확인한다."

## Requirements

### `guild-boss-orgg.raid`

- seed_key: "guild-boss-orgg.raid"
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

### `guild-boss-orgg.mechanics`

- seed_key: "guild-boss-orgg.mechanics"
- kind: "other"
- requirement_level: "required"
- title: "핵심 기믹"
- description: "체력 저하 뒤 광역 화염 경고 시 노란 원으로 이동한다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "location": "글리시 서쪽 절벽",
  "safe_zone": "yellow_circle"
}
```

### `guild-boss-orgg.rewards`

- seed_key: "guild-boss-orgg.rewards"
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

### `guild-boss-orgg.step.mechanic`

- seed_key: "guild-boss-orgg.step.mechanic"
- phase: "preparation"
- order_no: 1
- title: "핵심 패턴 대응"
- description: "노란 안전 지대로 이동한다."
- checkable: false

## Schedules

- None

## Rewards

### `guild-boss-orgg.reward.crystals`

- seed_key: "guild-boss-orgg.reward.crystals"
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

### `guild-boss-orgg.reward.materials`

- seed_key: "guild-boss-orgg.reward.materials"
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

### `guild-boss-orgg.reward.advice`

- seed_key: "guild-boss-orgg.reward.advice"
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

### `guild-boss-orgg.reward.lightstone`

- seed_key: "guild-boss-orgg.reward.lightstone"
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

### `guild-boss-orgg.reward.gold`

- seed_key: "guild-boss-orgg.reward.gold"
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

### `guild-boss-orgg.section.scope`

- seed_key: "guild-boss-orgg.section.scope"
- section_type: "notes"
- title: "범위"
- order_no: 1

#### body_markdown

공통 소환·주간 횟수는 guild-boss-current-system에서 관리한다.

## Related Contents

### `guild-boss-orgg.relation.system`

- seed_key: "guild-boss-orgg.relation.system"
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

### `guild-boss-orgg.claim.purpose::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-orgg.claim.purpose::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-orgg"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-orgg.claim.purpose::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-orgg.claim.purpose::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-orgg"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-orgg.claim.rewards::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-orgg.claim.rewards::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-orgg"
- claim_key: "rewards"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-orgg.claim.rewards::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-orgg.claim.rewards::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-orgg"
- claim_key: "rewards"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-orgg.claim.summary::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-orgg.claim.summary::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-orgg"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-orgg.claim.summary::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-orgg.claim.summary::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-orgg"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-orgg.claim.mechanics::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-orgg.claim.mechanics::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-orgg.mechanics"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-orgg.claim.mechanics::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-orgg.claim.mechanics::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-orgg.mechanics"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-orgg.claim.raid::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-orgg.claim.raid::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-orgg.raid"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-orgg.claim.raid::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-orgg.claim.raid::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-orgg.raid"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-orgg.claim.section.scope::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-orgg.claim.section.scope::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-orgg.section.scope"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-orgg.claim.section.scope::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-orgg.claim.section.scope::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-orgg.section.scope"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-orgg.claim.step.mechanic::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-orgg.claim.step.mechanic::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-orgg.step.mechanic"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-orgg.claim.step.mechanic::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-orgg.claim.step.mechanic::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-orgg.step.mechanic"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
