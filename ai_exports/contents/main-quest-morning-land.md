<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 아침의 나라 메인 의뢰

## Identity

- slug: "main-quest-morning-land"
- name_ko: "아침의 나라 메인 의뢰"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "마그누스 완료 뒤 설화 일지 단위로 진행하며 검은 사당 우두머리를 여는 메인 의뢰다."
- purpose: "진입 조건, 대표 설화 완료와 영구 가문 능력치·검은 사당 해금을 연결한다."

## Requirements

### `main-quest-morning-land.entry`

- seed_key: "main-quest-morning-land.entry"
- kind: "quest"
- requirement_level: "required"
- title: "아침의 나라 진입 조건"
- description: "56레벨 이상이며 [마그누스] 심연에서 온 상자를 완료한 뒤 아침의 나라 메인 의뢰를 시작한다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "minimum_level": 56,
  "prerequisite_quest": "[마그누스] 심연에서 온 상자"
}
```

### `main-quest-morning-land.tales`

- seed_key: "main-quest-morning-land.tales"
- kind: "quest"
- requirement_level: "required"
- title: "설화 일지 진행"
- description: "초기 8개 설화 일지를 선택해 진행하고 완료한 설화에 대응하는 검은 사당 우두머리를 연다."
- structured_value:

```json
{
  "choice_order": true,
  "initial_tale_count": 8,
  "knowledge_role": "fact",
  "unlock_effect": "corresponding_black_shrine_boss"
}
```

## Steps

- None

## Schedules

- None

## Rewards

### `main-quest-morning-land.reward.family-ap`

- seed_key: "main-quest-morning-land.reward.family-ap"
- name: "가문 공격력"
- reward_type: "fixed_effect"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "point"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "메인 의뢰 완료 기준 가문 영구 적용"
- order_no: 1

### `main-quest-morning-land.reward.family-dp`

- seed_key: "main-quest-morning-land.reward.family-dp"
- name: "가문 방어력"
- reward_type: "fixed_effect"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "point"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "메인 의뢰 완료 기준 가문 영구 적용"
- order_no: 2

## Sections

- None

## Related Contents

### `main-quest-morning-land.foundation`

- seed_key: "main-quest-morning-land.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "main-quest-progression-foundation"
- content_name_ko: "메인 의뢰 성장 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-progression-foundation.md"
### `main-quest-morning-land.magnus`

- seed_key: "main-quest-morning-land.magnus"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "magnus-progression"
- content_name_ko: "마그누스 전체 진행"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/magnus-progression.md"
### `main-quest-morning-land.black-shrine`

- seed_key: "main-quest-morning-land.black-shrine"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "black-shrine-donghae-weekly"
- content_name_ko: "검은 사당 - 동해도 주간 토벌"
- content_category: "combat_pve"
- note: null
- order_no: 3
- relative_path: "../contents/black-shrine-donghae-weekly.md"
### `main-quest-morning-land.stats`

- seed_key: "main-quest-morning-land.stats"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "permanent-stat-progression"
- content_name_ko: "영구 능력치 성장"
- content_category: "progression"
- note: null
- order_no: 4
- relative_path: "../contents/permanent-stat-progression.md"
### `morning-land-story-codex.morning-land-main`

- seed_key: "morning-land-story-codex.morning-land-main"
- direction: "incoming"
- relation_type: "related"
- content_slug: "morning-land-story-codex"
- content_name_ko: "아침의 나라 이야기 도감 : 동해도/황해도 편"
- content_category: "progression"
- note: "메인 의뢰 진행과 선택 분기에 따라 페이지가 채워짐"
- order_no: 2
- relative_path: "../contents/morning-land-story-codex.md"
### `magnus-progression.morning-land`

- seed_key: "magnus-progression.morning-land"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "magnus-progression"
- content_name_ko: "마그누스 전체 진행"
- content_category: "progression"
- note: null
- order_no: 5
- relative_path: "../contents/magnus-progression.md"

## Evidence and Sources

### Current evidence

### `main-quest-morning-land.claim.entry::morning-land-main-quest-guide`

- evidence_seed_key: "main-quest-morning-land.claim.entry::morning-land-main-quest-guide"
- source_id: "morning-land-main-quest-guide"
- title: "Land of the Morning Light Main Quest Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=314"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "main-quest-morning-land.entry"
- claim_key: "requirement:entry"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `main-quest-morning-land.claim.tales::morning-land-launch-2023-03-29`

- evidence_seed_key: "main-quest-morning-land.claim.tales::morning-land-launch-2023-03-29"
- source_id: "morning-land-launch-2023-03-29"
- title: "2023-03-29 Update - Land of the Morning Light"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=10062"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-03-29"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "main-quest-morning-land.tales"
- claim_key: "requirement:tales"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `main-quest-morning-land.claim.tales::morning-land-main-quest-guide`

- evidence_seed_key: "main-quest-morning-land.claim.tales::morning-land-main-quest-guide"
- source_id: "morning-land-main-quest-guide"
- title: "Land of the Morning Light Main Quest Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=314"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "main-quest-morning-land.tales"
- claim_key: "requirement:tales"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `main-quest-morning-land.claim.reward-ap::hyperboost-progression-2026`

- evidence_seed_key: "main-quest-morning-land.claim.reward-ap::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "main-quest-morning-land.reward.family-ap"
- claim_key: "reward:family-ap"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `main-quest-morning-land.claim.reward-dp::hyperboost-progression-2026`

- evidence_seed_key: "main-quest-morning-land.claim.reward-dp::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "main-quest-morning-land.reward.family-dp"
- claim_key: "reward:family-dp"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
