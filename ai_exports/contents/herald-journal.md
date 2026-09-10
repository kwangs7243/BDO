<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 외침꾼의 일지

## Identity

- slug: "herald-journal"
- name_ko: "외침꾼의 일지"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "그믐달 상단의 행동일지 그룹에서 진행하는 3권의 상시 모험일지다."
- purpose: "58레벨 그룹 해금과 현재 발크스의 외침·칭호 보상 구조를 추적한다."

## Requirements

### `herald-journal.identity`

- seed_key: "herald-journal.identity"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 책장 identity"
- description: "그믐달 상단의 행동일지 그룹에 속하며 현재 공식 보상 표는 3권을 제시한다."
- structured_value:

```json
{
  "bookshelf_group": "그믐달 상단의 행동일지",
  "family_content": true,
  "journal_kind": "progression_reward",
  "knowledge_role": "fact",
  "simultaneous_journal_count": 2,
  "volume_count": 3
}
```

### `herald-journal.unlock`

- seed_key: "herald-journal.unlock"
- kind: "quest"
- requirement_level: "required"
- title: "현재 해금 조건"
- description: "58레벨 달성 후 흑정령의 [모험일지] 그믐달 상단의 행동일지 의뢰를 완료하면 마가한의 서와 함께 열린다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "minimum_level": 58,
  "unlock_quest": "[모험일지] 그믐달 상단의 행동일지"
}
```

## Steps

### `herald-journal.step.unlock`

- seed_key: "herald-journal.step.unlock"
- phase: "unlock"
- order_no: 1
- title: "해금 조건 확인"
- description: "58레벨 달성 후 흑정령의 [모험일지] 그믐달 상단의 행동일지 의뢰를 완료하면 마가한의 서와 함께 열린다."
- checkable: true

### `herald-journal.step.complete`

- seed_key: "herald-journal.step.complete"
- phase: "reward"
- order_no: 2
- title: "일지 진행과 보상 확인"
- description: "장별 목표를 순서대로 완료하고 공식 책장에 표시된 현재 보상을 확인한다."
- checkable: true

## Schedules

- None

## Rewards

### `herald-journal.reward.valks-cry`

- seed_key: "herald-journal.reward.valks-cry"
- name: "발크스의 외침"
- reward_type: "fixed_item"
- amount: 50.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "현재 표의 10개 보상 5회를 합산"
- order_no: 1

## Sections

- None

## Related Contents

### `herald-journal.foundation`

- seed_key: "herald-journal.foundation"
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

### `herald-journal.claim.purpose::adventure-log-bookshelf-guide`

- evidence_seed_key: "herald-journal.claim.purpose::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "herald-journal"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `herald-journal.claim.summary::adventure-log-bookshelf-guide`

- evidence_seed_key: "herald-journal.claim.summary::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "herald-journal"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `herald-journal.claim.identity::adventure-log-bookshelf-guide`

- evidence_seed_key: "herald-journal.claim.identity::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "herald-journal.identity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `herald-journal.claim.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "herald-journal.claim.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "herald-journal.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `herald-journal.claim.step.complete::adventure-log-bookshelf-guide`

- evidence_seed_key: "herald-journal.claim.step.complete::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "herald-journal.step.complete"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `herald-journal.claim.step.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "herald-journal.claim.step.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "herald-journal.step.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `herald-journal.claim.reward.valks-cry::adventure-log-bookshelf-guide`

- evidence_seed_key: "herald-journal.claim.reward.valks-cry::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "herald-journal.reward.valks-cry"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
