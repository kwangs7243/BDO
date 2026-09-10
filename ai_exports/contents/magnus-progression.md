<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 마그누스 전체 진행

## Identity

- slug: "magnus-progression"
- name_ko: "마그누스 전체 진행"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "마그누스 시작 조건부터 지역별 심연의 혈관과 최종 보상까지 추적하는 가문 연속 의뢰다."
- purpose: "세부 퍼즐 공략 없이 시작·중간 관문·최종 완료와 핵심 해금만 기록한다."

## Requirements

### `magnus-progression.start`

- seed_key: "magnus-progression.start"
- kind: "quest"
- requirement_level: "required"
- title: "시작 조건"
- description: "진행 경로에 맞는 선행 메인 의뢰를 충족한 뒤 흑정령의 [마그누스] 추억의 벨리아로 시작한다."
- structured_value:

```json
{
  "accepted_from": "흑정령",
  "alternative_entry_paths": [
    "일반 메인 의뢰",
    "간소화 의뢰",
    "끝없는 겨울의 산 시작"
  ],
  "knowledge_role": "fact",
  "start_quest": "[마그누스] 추억의 벨리아"
}
```

### `magnus-progression.regional-gates`

- seed_key: "magnus-progression.regional-gates"
- kind: "quest"
- requirement_level: "required"
- title: "지역 진행 관문"
- description: "진행 중 세렌디아와 칼페온 메인 의뢰 완료 여부에 따라 다음 심연의 혈관 구간이 열린다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "regional_main_quest_gates": [
    "Serendia",
    "Calpheon"
  ]
}
```

### `magnus-progression.completion`

- seed_key: "magnus-progression.completion"
- kind: "quest"
- requirement_level: "required"
- title: "최종 완료"
- description: "[마그누스] 도움의 대가 완료를 전체 연속 의뢰의 대표 완료 지점으로 기록한다."
- structured_value:

```json
{
  "completion_quest": "[마그누스] 도움의 대가",
  "knowledge_role": "fact",
  "scope": "family"
}
```

## Steps

### `magnus-progression.step.start`

- seed_key: "magnus-progression.step.start"
- phase: "unlock"
- order_no: 1
- title: "마그누스 시작"
- description: "진행 경로별 선행 조건을 확인하고 [마그누스] 추억의 벨리아를 수주한다."
- checkable: false

### `magnus-progression.step.veins`

- seed_key: "magnus-progression.step.veins"
- phase: "first_time"
- order_no: 2
- title: "심연의 혈관 진행"
- description: "지역별 마그누스 구간을 진행하며 심연의 혈관 지식을 연다."
- checkable: false

### `magnus-progression.step.complete`

- seed_key: "magnus-progression.step.complete"
- phase: "reward"
- order_no: 3
- title: "도움의 대가 완료"
- description: "최종 의뢰를 완료하고 가문 보상과 편의 기능 해금을 확인한다."
- checkable: false

## Schedules

- None

## Rewards

### `magnus-progression.reward.pen-boss-armor`

- seed_key: "magnus-progression.reward.pen-boss-armor"
- name: "동(V) 우두머리 방어구 선택"
- reward_type: "quest_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "magnus-pen-boss-armor"
- recommendation: "보유 장비와 장기 세팅을 확인한 뒤 선택"
- notes: "가문당 1회 선택 보상"
- order_no: 1

## Sections

- None

## Related Contents

### `magnus-progression.account`

- seed_key: "magnus-progression.account"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "account-progression-foundation"
- content_name_ko: "가문 성장 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/account-progression-foundation.md"
### `magnus-progression.convenience`

- seed_key: "magnus-progression.convenience"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "family-convenience-unlock-foundation"
- content_name_ko: "가문 편의 기능 해금"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/family-convenience-unlock-foundation.md"
### `magnus-progression.remote-storage`

- seed_key: "magnus-progression.remote-storage"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "magnus-remote-storage"
- content_name_ko: "마그누스 원격 창고"
- content_category: "life"
- note: null
- order_no: 3
- relative_path: "../contents/magnus-remote-storage.md"
### `magnus-progression.storage`

- seed_key: "magnus-progression.storage"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "storage-current-system"
- content_name_ko: "창고 현재 시스템"
- content_category: "life"
- note: null
- order_no: 4
- relative_path: "../contents/storage-current-system.md"
### `magnus-progression.morning-land`

- seed_key: "magnus-progression.morning-land"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "main-quest-morning-land"
- content_name_ko: "아침의 나라 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 5
- relative_path: "../contents/main-quest-morning-land.md"
### `main-quest-morning-land.magnus`

- seed_key: "main-quest-morning-land.magnus"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "main-quest-morning-land"
- content_name_ko: "아침의 나라 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/main-quest-morning-land.md"

## Evidence and Sources

### Current evidence

### `magnus-progression.claim.completion::magnus-guide`

- evidence_seed_key: "magnus-progression.claim.completion::magnus-guide"
- source_id: "magnus-guide"
- title: "어비스 원 : 마그누스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=305"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "magnus-progression.completion"
- claim_key: "requirement:completion"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `magnus-progression.claim.regional-gates::magnus-guide`

- evidence_seed_key: "magnus-progression.claim.regional-gates::magnus-guide"
- source_id: "magnus-guide"
- title: "어비스 원 : 마그누스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=305"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "magnus-progression.regional-gates"
- claim_key: "requirement:regional-gates"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `magnus-progression.claim.start::magnus-guide`

- evidence_seed_key: "magnus-progression.claim.start::magnus-guide"
- source_id: "magnus-guide"
- title: "어비스 원 : 마그누스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=305"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "magnus-progression.start"
- claim_key: "requirement:start"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `magnus-progression.claim.step-complete::magnus-guide`

- evidence_seed_key: "magnus-progression.claim.step-complete::magnus-guide"
- source_id: "magnus-guide"
- title: "어비스 원 : 마그누스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=305"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "magnus-progression.step.complete"
- claim_key: "step:complete"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `magnus-progression.claim.step-start::magnus-guide`

- evidence_seed_key: "magnus-progression.claim.step-start::magnus-guide"
- source_id: "magnus-guide"
- title: "어비스 원 : 마그누스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=305"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "magnus-progression.step.start"
- claim_key: "step:start"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `magnus-progression.claim.step-veins::magnus-guide`

- evidence_seed_key: "magnus-progression.claim.step-veins::magnus-guide"
- source_id: "magnus-guide"
- title: "어비스 원 : 마그누스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=305"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "magnus-progression.step.veins"
- claim_key: "step:veins"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `magnus-progression.claim.reward-pen::magnus-guide`

- evidence_seed_key: "magnus-progression.claim.reward-pen::magnus-guide"
- source_id: "magnus-guide"
- title: "어비스 원 : 마그누스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=305"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "magnus-progression.reward.pen-boss-armor"
- claim_key: "reward:pen-boss-armor"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
