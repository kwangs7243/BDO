<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 길드 우두머리 구미호·두억시니

## Identity

- slug: "guild-boss-gumiho-duoksini"
- name_ko: "길드 우두머리 구미호·두억시니"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "서부 경비 캠프 인근에서 명성 25,000으로 두 우두머리를 동시에 상대한다."
- purpose: "표준 조각 우두머리와 다른 소환·처치·보상 흐름을 확인한다."

## Requirements

### `guild-boss-gumiho-duoksini.access`

- seed_key: "guild-boss-gumiho-duoksini.access"
- kind: "other"
- requirement_level: "required"
- title: "소환 조건"
- description: "명성 25,000으로 주 1회 소환하며 처치 시 명성 10,000을 얻는다."
- structured_value:

```json
{
  "fame_cost": 25000,
  "fame_reward": 10000,
  "knowledge_role": "fact",
  "location": "서부 경비 캠프 인근",
  "weekly": 1
}
```

### `guild-boss-gumiho-duoksini.encounter`

- seed_key: "guild-boss-gumiho-duoksini.encounter"
- kind: "other"
- requirement_level: "required"
- title: "동시 전투"
- description: "둘을 모두 처치한 뒤 보물 상자도 처치한다."
- structured_value:

```json
{
  "bosses": [
    "구미호",
    "두억시니"
  ],
  "defeat_chest": true,
  "knowledge_role": "fact"
}
```

### `guild-boss-gumiho-duoksini.rewards`

- seed_key: "guild-boss-gumiho-duoksini.rewards"
- kind: "other"
- requirement_level: "required"
- title: "규모별 금괴"
- description: "1,000G 9~11개, 100G·10G는 규모별 상세 표다."
- structured_value:

```json
{
  "gold_10": {
    "extra_large": [
      60,
      75
    ],
    "large": [
      60,
      75
    ],
    "medium": [
      60,
      75
    ],
    "small": [
      30,
      45
    ]
  },
  "gold_100": {
    "extra_large": [
      38,
      45
    ],
    "large": [
      30,
      38
    ],
    "medium": [
      23,
      30
    ],
    "small": [
      23,
      30
    ]
  },
  "gold_1000": [
    9,
    11
  ],
  "knowledge_role": "fact"
}
```

### `guild-boss-gumiho-duoksini.identity`

- seed_key: "guild-boss-gumiho-duoksini.identity"
- kind: "other"
- requirement_level: "required"
- title: "검은사당과 분리"
- description: "동해도 검은사당 동명 우두머리와 별도 Content다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "separate_from_black_shrine": true
}
```

## Steps

### `guild-boss-gumiho-duoksini.step.bosses`

- seed_key: "guild-boss-gumiho-duoksini.step.bosses"
- phase: "preparation"
- order_no: 1
- title: "둘 모두 처치"
- description: "구미호와 두억시니를 모두 처치한다."
- checkable: false

### `guild-boss-gumiho-duoksini.step.chest`

- seed_key: "guild-boss-gumiho-duoksini.step.chest"
- phase: "first_time"
- order_no: 2
- title: "상자 처치"
- description: "뒤이어 나타난 상자를 처치한다."
- checkable: false

## Schedules

- None

## Rewards

### `guild-boss-gumiho-duoksini.reward.advice`

- seed_key: "guild-boss-gumiho-duoksini.reward.advice"
- name: "발크스의 조언 (+50~+100)"
- reward_type: "enhancement"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 1

### `guild-boss-gumiho-duoksini.reward.crystals`

- seed_key: "guild-boss-gumiho-duoksini.reward.crystals"
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
- order_no: 2

### `guild-boss-gumiho-duoksini.reward.gold`

- seed_key: "guild-boss-gumiho-duoksini.reward.gold"
- name: "금괴"
- reward_type: "currency"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "규모별 requirement 참조"
- order_no: 3

## Sections

### `guild-boss-gumiho-duoksini.section.boundary`

- seed_key: "guild-boss-gumiho-duoksini.section.boundary"
- section_type: "notes"
- title: "보상 경계"
- order_no: 1

#### body_markdown

상단 요약과 규모별 상세 표가 다르면 상세 표를 보존한다.

## Related Contents

### `guild-boss-gumiho-duoksini.relation.system`

- seed_key: "guild-boss-gumiho-duoksini.relation.system"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "guild-boss-current-system"
- content_name_ko: "길드 우두머리 현행 시스템"
- content_category: "combat_pve"
- note: "직접 소환 규칙"
- order_no: 1
- relative_path: "../contents/guild-boss-current-system.md"
### `guild-boss-gumiho-duoksini.relation.gumiho`

- seed_key: "guild-boss-gumiho-duoksini.relation.gumiho"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "donghae-shrine-gumiho"
- content_name_ko: "구미호 (동해도 검은사당)"
- content_category: "combat_pve"
- note: "동명 검은사당과 분리"
- order_no: 2
- relative_path: "../contents/donghae-shrine-gumiho.md"
### `guild-boss-gumiho-duoksini.relation.duoksini`

- seed_key: "guild-boss-gumiho-duoksini.relation.duoksini"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "donghae-shrine-duoksini"
- content_name_ko: "두억시니 (동해도 검은사당)"
- content_category: "combat_pve"
- note: "동명 검은사당과 분리"
- order_no: 3
- relative_path: "../contents/donghae-shrine-duoksini.md"

## Evidence and Sources

### Current evidence

### `guild-boss-gumiho-duoksini.claim.purpose::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.purpose::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-gumiho-duoksini"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-gumiho-duoksini.claim.purpose::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.purpose::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-gumiho-duoksini"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-gumiho-duoksini.claim.rewards::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.rewards::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-gumiho-duoksini"
- claim_key: "rewards"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-gumiho-duoksini.claim.rewards::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.rewards::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-gumiho-duoksini"
- claim_key: "rewards"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-gumiho-duoksini.claim.summary::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.summary::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-gumiho-duoksini"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-gumiho-duoksini.claim.summary::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.summary::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-gumiho-duoksini"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-gumiho-duoksini.claim.access::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.access::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-gumiho-duoksini.access"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-gumiho-duoksini.claim.access::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.access::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-gumiho-duoksini.access"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-gumiho-duoksini.claim.encounter::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.encounter::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-gumiho-duoksini.encounter"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-gumiho-duoksini.claim.encounter::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.encounter::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-gumiho-duoksini.encounter"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-gumiho-duoksini.claim.identity::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.identity::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-gumiho-duoksini.identity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-gumiho-duoksini.claim.identity::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.identity::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-gumiho-duoksini.identity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-gumiho-duoksini.claim.section.boundary::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.section.boundary::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-gumiho-duoksini.section.boundary"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-gumiho-duoksini.claim.section.boundary::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.section.boundary::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-gumiho-duoksini.section.boundary"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-gumiho-duoksini.claim.step.bosses::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.step.bosses::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-gumiho-duoksini.step.bosses"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-gumiho-duoksini.claim.step.bosses::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.step.bosses::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-gumiho-duoksini.step.bosses"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-gumiho-duoksini.claim.step.chest::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.step.chest::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-gumiho-duoksini.step.chest"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-gumiho-duoksini.claim.step.chest::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-gumiho-duoksini.claim.step.chest::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-gumiho-duoksini.step.chest"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
