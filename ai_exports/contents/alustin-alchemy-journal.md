<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 알루스틴의 연금일지

## Identity

- slug: "alustin-alchemy-journal"
- name_ko: "알루스틴의 연금일지"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "샤카투 상단의 수집일지 그룹에서 진행하는 상시 모험일지다."
- purpose: "현재 책장 identity와 공통 해금 조건만 추적하며 확인되지 않은 권 수·aggregate 보상은 만들지 않는다."

## Requirements

### `alustin-alchemy-journal.identity`

- seed_key: "alustin-alchemy-journal.identity"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 책장 identity"
- description: "샤카투 상단의 수집일지 그룹의 독립 진행 일지이며 현재 공식 주요 보상 표에는 권 수와 aggregate 보상이 별도로 제시되지 않는다."
- structured_value:

```json
{
  "aggregate_reward_seeded": false,
  "bookshelf_group": "샤카투 상단의 수집일지",
  "family_content": true,
  "journal_kind": "progression_reward",
  "knowledge_role": "fact",
  "simultaneous_journal_count": 3
}
```

### `alustin-alchemy-journal.unlock`

- seed_key: "alustin-alchemy-journal.unlock"
- kind: "quest"
- requirement_level: "required"
- title: "현재 해금 조건"
- description: "57레벨 달성 후 흑정령의 [모험일지] 샤카투 상단의 수집일지 의뢰를 완료하면 그룹의 일지 3종과 함께 열린다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "minimum_level": 57,
  "unlock_quest": "[모험일지] 샤카투 상단의 수집일지"
}
```

## Steps

### `alustin-alchemy-journal.step.unlock`

- seed_key: "alustin-alchemy-journal.step.unlock"
- phase: "unlock"
- order_no: 1
- title: "해금 조건 확인"
- description: "57레벨 달성 후 흑정령의 [모험일지] 샤카투 상단의 수집일지 의뢰를 완료하면 그룹의 일지 3종과 함께 열린다."
- checkable: true

### `alustin-alchemy-journal.step.complete`

- seed_key: "alustin-alchemy-journal.step.complete"
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

### `alustin-alchemy-journal.foundation`

- seed_key: "alustin-alchemy-journal.foundation"
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

### `alustin-alchemy-journal.claim.purpose::adventure-log-bookshelf-guide`

- evidence_seed_key: "alustin-alchemy-journal.claim.purpose::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "alustin-alchemy-journal"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `alustin-alchemy-journal.claim.summary::adventure-log-bookshelf-guide`

- evidence_seed_key: "alustin-alchemy-journal.claim.summary::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "alustin-alchemy-journal"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `alustin-alchemy-journal.claim.identity::adventure-log-bookshelf-guide`

- evidence_seed_key: "alustin-alchemy-journal.claim.identity::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "alustin-alchemy-journal.identity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `alustin-alchemy-journal.claim.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "alustin-alchemy-journal.claim.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "alustin-alchemy-journal.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `alustin-alchemy-journal.claim.step.complete::adventure-log-bookshelf-guide`

- evidence_seed_key: "alustin-alchemy-journal.claim.step.complete::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alustin-alchemy-journal.step.complete"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `alustin-alchemy-journal.claim.step.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "alustin-alchemy-journal.claim.step.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "alustin-alchemy-journal.step.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
