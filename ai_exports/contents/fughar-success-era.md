<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 푸가르의 성공시대

## Identity

- slug: "fughar-success-era"
- name_ko: "푸가르의 성공시대"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "까마귀 상단의 기록일지 그룹에서 진행하는 3권의 상시 모험일지다."
- purpose: "공통 해금과 현재 주요 완료 보상을 journal 단위로 추적한다."

## Requirements

### `fughar-success-era.identity`

- seed_key: "fughar-success-era.identity"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 책장 identity"
- description: "까마귀 상단의 기록일지 그룹에 속하며 현재 공식 보상 표는 3권까지 제시한다."
- structured_value:

```json
{
  "bookshelf_group": "까마귀 상단의 기록일지",
  "family_content": true,
  "journal_kind": "progression_reward",
  "knowledge_role": "fact",
  "simultaneous_journal_count": 4,
  "volume_count": 3
}
```

### `fughar-success-era.unlock`

- seed_key: "fughar-success-era.unlock"
- kind: "quest"
- requirement_level: "required"
- title: "현재 해금 조건"
- description: "55레벨 달성 후 흑정령의 [모험일지] 까마귀 상단의 기록일지 의뢰를 완료하면 그룹의 일지 4종과 함께 열린다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "minimum_level": 55,
  "unlock_quest": "[모험일지] 까마귀 상단의 기록일지"
}
```

## Steps

### `fughar-success-era.step.unlock`

- seed_key: "fughar-success-era.step.unlock"
- phase: "unlock"
- order_no: 1
- title: "해금 조건 확인"
- description: "55레벨 달성 후 흑정령의 [모험일지] 까마귀 상단의 기록일지 의뢰를 완료하면 그룹의 일지 4종과 함께 열린다."
- checkable: true

### `fughar-success-era.step.complete`

- seed_key: "fughar-success-era.step.complete"
- phase: "reward"
- order_no: 2
- title: "일지 진행과 보상 확인"
- description: "장별 목표를 순서대로 완료하고 공식 책장에 표시된 현재 보상을 확인한다."
- checkable: true

## Schedules

- None

## Rewards

### `fughar-success-era.reward.special-gift-box`

- seed_key: "fughar-success-era.reward.special-gift-box"
- name: "[이벤트] 푸가르의 특별한 선물 상자"
- reward_type: "fixed_item"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "3권 1장 현재 보상"
- order_no: 1

## Sections

- None

## Related Contents

### `fughar-success-era.foundation`

- seed_key: "fughar-success-era.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "adventure-log-foundation"
- content_name_ko: "모험일지 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/adventure-log-foundation.md"

## Evidence and Sources

### Current evidence

### `fughar-success-era.claim.purpose::adventure-log-bookshelf-guide`

- evidence_seed_key: "fughar-success-era.claim.purpose::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fughar-success-era"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `fughar-success-era.claim.summary::adventure-log-bookshelf-guide`

- evidence_seed_key: "fughar-success-era.claim.summary::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "fughar-success-era"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `fughar-success-era.claim.identity::adventure-log-bookshelf-guide`

- evidence_seed_key: "fughar-success-era.claim.identity::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fughar-success-era.identity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `fughar-success-era.claim.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "fughar-success-era.claim.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "fughar-success-era.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `fughar-success-era.claim.step.complete::adventure-log-bookshelf-guide`

- evidence_seed_key: "fughar-success-era.claim.step.complete::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fughar-success-era.step.complete"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `fughar-success-era.claim.step.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "fughar-success-era.claim.step.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "fughar-success-era.step.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `fughar-success-era.claim.reward.special-gift-box::adventure-log-bookshelf-guide`

- evidence_seed_key: "fughar-success-era.claim.reward.special-gift-box::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "fughar-success-era.reward.special-gift-box"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
