<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 이고르 바탈리의 모험일지

## Identity

- slug: "igor-bartali-adventure-log"
- name_ko: "이고르 바탈리의 모험일지"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "현재 핵심 가문 능력치 보상이 통합된 15권의 대표 모험일지다."
- purpose: "해금 조건과 15권 전체 완료 상태, 2025-07-23 이후의 현재 영구 공격력·방어력 보상을 추적한다."

## Requirements

### `igor-bartali-adventure-log.unlock`

- seed_key: "igor-bartali-adventure-log.unlock"
- kind: "quest"
- requirement_level: "required"
- title: "책장 해금 조건"
- description: "51레벨 이상이며 칼페온 메인 의뢰 완료 계열 또는 간소화 의뢰의 푸가르 비망록 6장을 완료하면 열린다."
- structured_value:

```json
{
  "any_of": [
    "Calpheon main quest completion",
    "Fughar simplified memoir chapter 6"
  ],
  "knowledge_role": "fact",
  "minimum_level": 51
}
```

### `igor-bartali-adventure-log.current-consolidation`

- seed_key: "igor-bartali-adventure-log.current-consolidation"
- kind: "stat"
- requirement_level: "required"
- title: "현재 핵심 능력치 통합"
- description: "2025년 7월 23일 이후 이벤트 일지를 제외한 핵심 능력치 보상은 이고르 바탈리의 모험일지 완료 보상으로 통합되어 있다."
- structured_value:

```json
{
  "consolidated_stats": [
    "AP",
    "DP",
    "accuracy",
    "evasion",
    "max_stamina",
    "max_resource",
    "max_hp"
  ],
  "effective_date": "2025-07-23",
  "knowledge_role": "fact"
}
```

### `igor-bartali-adventure-log.volume-count`

- seed_key: "igor-bartali-adventure-log.volume-count"
- kind: "other"
- requirement_level: "required"
- title: "현재 권 수"
- description: "현재 공식 책장 보상 표는 이고르 바탈리의 모험일지를 1권부터 15권까지 제시한다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "volume_count": 15
}
```

## Steps

### `igor-bartali-adventure-log.step.unlock`

- seed_key: "igor-bartali-adventure-log.step.unlock"
- phase: "unlock"
- order_no: 1
- title: "책장 해금"
- description: "레벨과 선행 메인 의뢰 조건을 충족해 모험일지 책장을 연다."
- checkable: false

### `igor-bartali-adventure-log.step.complete`

- seed_key: "igor-bartali-adventure-log.step.complete"
- phase: "reward"
- order_no: 2
- title: "전체 일지 완료"
- description: "세부 장별 공략이 아니라 전체 완료와 가문 영구 보상 수령을 기록한다."
- checkable: false

## Schedules

- None

## Rewards

### `igor-bartali-adventure-log.reward.family-ap`

- seed_key: "igor-bartali-adventure-log.reward.family-ap"
- name: "가문 공격력"
- reward_type: "fixed_effect"
- amount: 6.0
- min_amount: null
- max_amount: null
- unit: "point"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "가문 영구 적용"
- order_no: 1

### `igor-bartali-adventure-log.reward.family-dp`

- seed_key: "igor-bartali-adventure-log.reward.family-dp"
- name: "가문 방어력"
- reward_type: "fixed_effect"
- amount: 6.0
- min_amount: null
- max_amount: null
- unit: "point"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "가문 영구 적용"
- order_no: 2

## Sections

- None

## Related Contents

### `igor-bartali-adventure-log.foundation`

- seed_key: "igor-bartali-adventure-log.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "adventure-log-foundation"
- content_name_ko: "모험일지 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/adventure-log-foundation.md"
### `igor-bartali-adventure-log.stats`

- seed_key: "igor-bartali-adventure-log.stats"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "permanent-stat-progression"
- content_name_ko: "영구 능력치 성장"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/permanent-stat-progression.md"
### `emma-bartali-record-log.igor`

- seed_key: "emma-bartali-record-log.igor"
- direction: "incoming"
- relation_type: "related"
- content_slug: "emma-bartali-record-log"
- content_name_ko: "엠마 바탈리의 기록일지"
- content_category: "progression"
- note: "1장 조건에 이고르 바탈리 5권 완료가 포함됨"
- order_no: 2
- relative_path: "../contents/emma-bartali-record-log.md"

## Evidence and Sources

### Current evidence

### `igor-bartali-adventure-log.claim.purpose::combat-system-rework-2025-07-23`

- evidence_seed_key: "igor-bartali-adventure-log.claim.purpose::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "igor-bartali-adventure-log"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `igor-bartali-adventure-log.claim.purpose::hyperboost-progression-2026`

- evidence_seed_key: "igor-bartali-adventure-log.claim.purpose::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "igor-bartali-adventure-log"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `igor-bartali-adventure-log.claim.summary::adventure-log-bookshelf-guide`

- evidence_seed_key: "igor-bartali-adventure-log.claim.summary::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "igor-bartali-adventure-log"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `igor-bartali-adventure-log.claim.summary::hyperboost-progression-2026`

- evidence_seed_key: "igor-bartali-adventure-log.claim.summary::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "igor-bartali-adventure-log"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `igor-bartali-adventure-log.claim.consolidation::adventure-log-bookshelf-guide`

- evidence_seed_key: "igor-bartali-adventure-log.claim.consolidation::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "igor-bartali-adventure-log.current-consolidation"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `igor-bartali-adventure-log.claim.consolidation::combat-system-rework-2025-07-23`

- evidence_seed_key: "igor-bartali-adventure-log.claim.consolidation::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "igor-bartali-adventure-log.current-consolidation"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `igor-bartali-adventure-log.claim.consolidation::hyperboost-progression-2026`

- evidence_seed_key: "igor-bartali-adventure-log.claim.consolidation::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "igor-bartali-adventure-log.current-consolidation"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `igor-bartali-adventure-log.claim.consolidation::pit-weekly-2025`

- evidence_seed_key: "igor-bartali-adventure-log.claim.consolidation::pit-weekly-2025"
- source_id: "pit-weekly-2025"
- title: "7월 23일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "igor-bartali-adventure-log.current-consolidation"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `igor-bartali-adventure-log.claim.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "igor-bartali-adventure-log.claim.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "igor-bartali-adventure-log.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `igor-bartali-adventure-log.claim.volume-count::adventure-log-bookshelf-guide`

- evidence_seed_key: "igor-bartali-adventure-log.claim.volume-count::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "igor-bartali-adventure-log.volume-count"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `igor-bartali-adventure-log.claim.step-complete::adventure-log-bookshelf-guide`

- evidence_seed_key: "igor-bartali-adventure-log.claim.step-complete::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "igor-bartali-adventure-log.step.complete"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `igor-bartali-adventure-log.claim.step-complete::hyperboost-progression-2026`

- evidence_seed_key: "igor-bartali-adventure-log.claim.step-complete::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "igor-bartali-adventure-log.step.complete"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `igor-bartali-adventure-log.claim.step-unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "igor-bartali-adventure-log.claim.step-unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "igor-bartali-adventure-log.step.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `igor-bartali-adventure-log.claim.reward-ap::hyperboost-progression-2026`

- evidence_seed_key: "igor-bartali-adventure-log.claim.reward-ap::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "igor-bartali-adventure-log.reward.family-ap"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `igor-bartali-adventure-log.claim.reward-dp::hyperboost-progression-2026`

- evidence_seed_key: "igor-bartali-adventure-log.claim.reward-dp::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "igor-bartali-adventure-log.reward.family-dp"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `igor-bartali-adventure-log.claim.legacy::adventure-log-bookshelf-guide`

- evidence_seed_key: "igor-bartali-adventure-log.claim.legacy::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "igor-bartali-adventure-log.legacy-rewards"
- claim_key: "description"
- verification_status: "superseded"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: false
- is_active: false

### `igor-bartali-adventure-log.claim.legacy::combat-system-rework-2025-07-23`

- evidence_seed_key: "igor-bartali-adventure-log.claim.legacy::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "igor-bartali-adventure-log.legacy-rewards"
- claim_key: "description"
- verification_status: "superseded"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: false
- is_active: false

### `igor-bartali-adventure-log.claim.legacy::pit-weekly-2025`

- evidence_seed_key: "igor-bartali-adventure-log.claim.legacy::pit-weekly-2025"
- source_id: "pit-weekly-2025"
- title: "7월 23일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "igor-bartali-adventure-log.legacy-rewards"
- claim_key: "description"
- verification_status: "superseded"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: false
- is_active: false
