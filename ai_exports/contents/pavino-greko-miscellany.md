<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 파비노 그레코의 잡학도서

## Identity

- slug: "pavino-greko-miscellany"
- name_ko: "파비노 그레코의 잡학도서"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "그믐달 상단의 행동일지 7~10권으로 구분되는 4권의 상시 모험일지다."
- purpose: "공통 해금 뒤 파비노 그레코에게 개별 수주하는 현재 진행 경계와 주요 보상을 추적한다."

## Requirements

### `pavino-greko-miscellany.identity`

- seed_key: "pavino-greko-miscellany.identity"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 책장 identity"
- description: "그믐달 상단의 행동일지 그룹 7~10권에 해당하는 파비노 그레코의 잡학도서 4권이다."
- structured_value:

```json
{
  "bookshelf_group": "그믐달 상단의 행동일지",
  "family_content": true,
  "group_volume_range": "7-10",
  "individual_quest_acceptance": true,
  "journal_kind": "progression_reward",
  "knowledge_role": "fact",
  "volume_count": 4
}
```

### `pavino-greko-miscellany.unlock`

- seed_key: "pavino-greko-miscellany.unlock"
- kind: "quest"
- requirement_level: "required"
- title: "현재 해금 조건"
- description: "58레벨 및 [모험일지] 그믐달 상단의 행동일지 완료 후 파비노 그레코에게 각 권의 의뢰를 개별 수주한다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "minimum_level": 58,
  "unlock_quest": "[모험일지] 그믐달 상단의 행동일지"
}
```

## Steps

### `pavino-greko-miscellany.step.unlock`

- seed_key: "pavino-greko-miscellany.step.unlock"
- phase: "unlock"
- order_no: 1
- title: "해금 조건 확인"
- description: "58레벨 및 [모험일지] 그믐달 상단의 행동일지 완료 후 파비노 그레코에게 각 권의 의뢰를 개별 수주한다."
- checkable: true

### `pavino-greko-miscellany.step.complete`

- seed_key: "pavino-greko-miscellany.step.complete"
- phase: "reward"
- order_no: 2
- title: "일지 진행과 보상 확인"
- description: "장별 목표를 순서대로 완료하고 공식 책장에 표시된 현재 보상을 확인한다."
- checkable: true

## Schedules

- None

## Rewards

### `pavino-greko-miscellany.reward.gold-bar-1kg`

- seed_key: "pavino-greko-miscellany.reward.gold-bar-1kg"
- name: "금괴 1kG"
- reward_type: "fixed_item"
- amount: 7.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "4권 현재 표의 1+1+1+2+2개 합산"
- order_no: 1

## Sections

- None

## Related Contents

### `pavino-greko-miscellany.foundation`

- seed_key: "pavino-greko-miscellany.foundation"
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

### `pavino-greko-miscellany.claim.purpose::adventure-log-bookshelf-guide`

- evidence_seed_key: "pavino-greko-miscellany.claim.purpose::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "pavino-greko-miscellany"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `pavino-greko-miscellany.claim.summary::adventure-log-bookshelf-guide`

- evidence_seed_key: "pavino-greko-miscellany.claim.summary::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "pavino-greko-miscellany"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `pavino-greko-miscellany.claim.identity::adventure-log-bookshelf-guide`

- evidence_seed_key: "pavino-greko-miscellany.claim.identity::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "pavino-greko-miscellany.identity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `pavino-greko-miscellany.claim.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "pavino-greko-miscellany.claim.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "pavino-greko-miscellany.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `pavino-greko-miscellany.claim.step.complete::adventure-log-bookshelf-guide`

- evidence_seed_key: "pavino-greko-miscellany.claim.step.complete::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "pavino-greko-miscellany.step.complete"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `pavino-greko-miscellany.claim.step.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "pavino-greko-miscellany.claim.step.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "pavino-greko-miscellany.step.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `pavino-greko-miscellany.claim.reward.gold-bar-1kg::adventure-log-bookshelf-guide`

- evidence_seed_key: "pavino-greko-miscellany.claim.reward.gold-bar-1kg::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "pavino-greko-miscellany.reward.gold-bar-1kg"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
