<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 도린 모르그림의 비밀일지

## Identity

- slug: "dorin-morgrim-secret-journal"
- name_ko: "도린 모르그림의 비밀일지"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "샤카투 상단의 수집일지 그룹에서 진행하는 2권의 상시 모험일지다."
- purpose: "57레벨 그룹 해금과 현재 아이템 획득 증가 주문서 보상을 추적한다."

## Requirements

### `dorin-morgrim-secret-journal.identity`

- seed_key: "dorin-morgrim-secret-journal.identity"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 책장 identity"
- description: "샤카투 상단의 수집일지 그룹에 속하며 현재 공식 보상 표는 2권까지 제시한다."
- structured_value:

```json
{
  "bookshelf_group": "샤카투 상단의 수집일지",
  "family_content": true,
  "journal_kind": "progression_reward",
  "knowledge_role": "fact",
  "simultaneous_journal_count": 3,
  "volume_count": 2
}
```

### `dorin-morgrim-secret-journal.unlock`

- seed_key: "dorin-morgrim-secret-journal.unlock"
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

### `dorin-morgrim-secret-journal.step.unlock`

- seed_key: "dorin-morgrim-secret-journal.step.unlock"
- phase: "unlock"
- order_no: 1
- title: "해금 조건 확인"
- description: "57레벨 달성 후 흑정령의 [모험일지] 샤카투 상단의 수집일지 의뢰를 완료하면 그룹의 일지 3종과 함께 열린다."
- checkable: true

### `dorin-morgrim-secret-journal.step.complete`

- seed_key: "dorin-morgrim-secret-journal.step.complete"
- phase: "reward"
- order_no: 2
- title: "일지 진행과 보상 확인"
- description: "장별 목표를 순서대로 완료하고 공식 책장에 표시된 현재 보상을 확인한다."
- checkable: true

## Schedules

- None

## Rewards

### `dorin-morgrim-secret-journal.reward.item-collection-scroll`

- seed_key: "dorin-morgrim-secret-journal.reward.item-collection-scroll"
- name: "아이템 획득 증가 주문서"
- reward_type: "fixed_item"
- amount: 27.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "현재 표의 3개 보상 9회를 합산"
- order_no: 1

## Sections

- None

## Related Contents

### `dorin-morgrim-secret-journal.foundation`

- seed_key: "dorin-morgrim-secret-journal.foundation"
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

### `dorin-morgrim-secret-journal.claim.purpose::adventure-log-bookshelf-guide`

- evidence_seed_key: "dorin-morgrim-secret-journal.claim.purpose::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "dorin-morgrim-secret-journal"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `dorin-morgrim-secret-journal.claim.summary::adventure-log-bookshelf-guide`

- evidence_seed_key: "dorin-morgrim-secret-journal.claim.summary::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "dorin-morgrim-secret-journal"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `dorin-morgrim-secret-journal.claim.identity::adventure-log-bookshelf-guide`

- evidence_seed_key: "dorin-morgrim-secret-journal.claim.identity::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "dorin-morgrim-secret-journal.identity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `dorin-morgrim-secret-journal.claim.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "dorin-morgrim-secret-journal.claim.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "dorin-morgrim-secret-journal.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `dorin-morgrim-secret-journal.claim.step.complete::adventure-log-bookshelf-guide`

- evidence_seed_key: "dorin-morgrim-secret-journal.claim.step.complete::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "dorin-morgrim-secret-journal.step.complete"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `dorin-morgrim-secret-journal.claim.step.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "dorin-morgrim-secret-journal.claim.step.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "dorin-morgrim-secret-journal.step.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `dorin-morgrim-secret-journal.claim.reward.item-collection-scroll::adventure-log-bookshelf-guide`

- evidence_seed_key: "dorin-morgrim-secret-journal.claim.reward.item-collection-scroll::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "dorin-morgrim-secret-journal.reward.item-collection-scroll"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
