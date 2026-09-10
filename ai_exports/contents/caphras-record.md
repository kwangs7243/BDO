<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 카프라스의 기록

## Identity

- slug: "caphras-record"
- name_ko: "카프라스의 기록"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "까마귀 상단의 기록일지 그룹에 속하는 카프라스 관련 상시 모험일지다."
- purpose: "현재 책장이 명시한 2권 동시 개방 사실만 추적하고 전체 권 수나 보상을 추정하지 않는다."

## Requirements

### `caphras-record.identity`

- seed_key: "caphras-record.identity"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 책장 identity"
- description: "까마귀 상단의 기록일지 그룹의 독립 진행 일지이며 현재 책장은 그룹 해금 시 카프라스의 기록 2권이 열린다고 명시한다."
- structured_value:

```json
{
  "aggregate_reward_seeded": false,
  "bookshelf_group": "까마귀 상단의 기록일지",
  "directly_unlocked_volume": 2,
  "family_content": true,
  "journal_kind": "progression_reward",
  "knowledge_role": "fact"
}
```

### `caphras-record.unlock`

- seed_key: "caphras-record.unlock"
- kind: "quest"
- requirement_level: "required"
- title: "현재 해금 조건"
- description: "55레벨 달성 후 흑정령의 [모험일지] 까마귀 상단의 기록일지 의뢰를 완료하면 카프라스의 기록 2권이 함께 열린다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "minimum_level": 55,
  "unlock_quest": "[모험일지] 까마귀 상단의 기록일지"
}
```

## Steps

### `caphras-record.step.unlock`

- seed_key: "caphras-record.step.unlock"
- phase: "unlock"
- order_no: 1
- title: "해금 조건 확인"
- description: "55레벨 달성 후 흑정령의 [모험일지] 까마귀 상단의 기록일지 의뢰를 완료하면 카프라스의 기록 2권이 함께 열린다."
- checkable: true

### `caphras-record.step.complete`

- seed_key: "caphras-record.step.complete"
- phase: "reward"
- order_no: 2
- title: "일지 진행과 보상 확인"
- description: "장별 목표를 순서대로 완료하고 공식 책장에 표시된 현재 보상을 확인한다."
- checkable: true

## Schedules

- None

## Rewards

- None

## Sections

- None

## Related Contents

### `caphras-record.foundation`

- seed_key: "caphras-record.foundation"
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

### `caphras-record.claim.purpose::adventure-log-bookshelf-guide`

- evidence_seed_key: "caphras-record.claim.purpose::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "caphras-record"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `caphras-record.claim.summary::adventure-log-bookshelf-guide`

- evidence_seed_key: "caphras-record.claim.summary::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "caphras-record"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `caphras-record.claim.identity::adventure-log-bookshelf-guide`

- evidence_seed_key: "caphras-record.claim.identity::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "caphras-record.identity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `caphras-record.claim.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "caphras-record.claim.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "caphras-record.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `caphras-record.claim.step.complete::adventure-log-bookshelf-guide`

- evidence_seed_key: "caphras-record.claim.step.complete::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "caphras-record.step.complete"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `caphras-record.claim.step.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "caphras-record.claim.step.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "caphras-record.step.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
