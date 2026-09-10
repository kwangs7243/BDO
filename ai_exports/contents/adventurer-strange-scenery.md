<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 어느 모험가의 낯선 풍경

## Identity

- slug: "adventurer-strange-scenery"
- name_ko: "어느 모험가의 낯선 풍경"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "11레벨부터 책장에서 진행하는 상시 모험일지로 현재 표는 9권까지의 주요 보상을 제시한다."
- purpose: "낮은 레벨 해금과 아침의 나라 관련 재화·반려동물 등 현재 주요 보상을 추적한다."

## Requirements

### `adventurer-strange-scenery.identity`

- seed_key: "adventurer-strange-scenery.identity"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 책장 identity"
- description: "독립 상시 모험일지이며 현재 공식 보상 표에 5~9권 보상이 있고 마지막으로 제시된 권은 9권이다."
- structured_value:

```json
{
  "bookshelf_group": "어느 모험가의 낯선 풍경",
  "family_content": true,
  "journal_kind": "progression_reward",
  "knowledge_role": "fact",
  "latest_listed_volume": 9
}
```

### `adventurer-strange-scenery.unlock`

- seed_key: "adventurer-strange-scenery.unlock"
- kind: "quest"
- requirement_level: "required"
- title: "현재 해금 조건"
- description: "11레벨 달성 시 책장에서 진행할 수 있다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "minimum_level": 11
}
```

## Steps

### `adventurer-strange-scenery.step.unlock`

- seed_key: "adventurer-strange-scenery.step.unlock"
- phase: "unlock"
- order_no: 1
- title: "해금 조건 확인"
- description: "11레벨 달성 시 책장에서 진행할 수 있다."
- checkable: true

### `adventurer-strange-scenery.step.complete`

- seed_key: "adventurer-strange-scenery.step.complete"
- phase: "reward"
- order_no: 2
- title: "일지 진행과 보상 확인"
- description: "장별 목표를 순서대로 완료하고 공식 책장에 표시된 현재 보상을 확인한다."
- checkable: true

## Schedules

- None

## Rewards

### `adventurer-strange-scenery.reward.primordial-ember`

- seed_key: "adventurer-strange-scenery.reward.primordial-ember"
- name: "태초의 불씨"
- reward_type: "fixed_item"
- amount: 15.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "5권 1~5장 각 3개"
- order_no: 1

### `adventurer-strange-scenery.reward.sangpyeong-coin`

- seed_key: "adventurer-strange-scenery.reward.sangpyeong-coin"
- name: "상평통보"
- reward_type: "fixed_item"
- amount: 200.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "6권 1장"
- order_no: 2

### `adventurer-strange-scenery.reward.jangnankkaebi-pet`

- seed_key: "adventurer-strange-scenery.reward.jangnankkaebi-pet"
- name: "[반려동물] 장난깨비"
- reward_type: "fixed_item"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "9권 5장"
- order_no: 3

## Sections

- None

## Related Contents

### `adventurer-strange-scenery.foundation`

- seed_key: "adventurer-strange-scenery.foundation"
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

### `adventurer-strange-scenery.claim.purpose::adventure-log-bookshelf-guide`

- evidence_seed_key: "adventurer-strange-scenery.claim.purpose::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "adventurer-strange-scenery"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `adventurer-strange-scenery.claim.summary::adventure-log-bookshelf-guide`

- evidence_seed_key: "adventurer-strange-scenery.claim.summary::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "adventurer-strange-scenery"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `adventurer-strange-scenery.claim.identity::adventure-log-bookshelf-guide`

- evidence_seed_key: "adventurer-strange-scenery.claim.identity::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "adventurer-strange-scenery.identity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `adventurer-strange-scenery.claim.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "adventurer-strange-scenery.claim.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "adventurer-strange-scenery.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `adventurer-strange-scenery.claim.step.complete::adventure-log-bookshelf-guide`

- evidence_seed_key: "adventurer-strange-scenery.claim.step.complete::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "adventurer-strange-scenery.step.complete"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `adventurer-strange-scenery.claim.step.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "adventurer-strange-scenery.claim.step.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "adventurer-strange-scenery.step.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `adventurer-strange-scenery.claim.reward.jangnankkaebi-pet::adventure-log-bookshelf-guide`

- evidence_seed_key: "adventurer-strange-scenery.claim.reward.jangnankkaebi-pet::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "adventurer-strange-scenery.reward.jangnankkaebi-pet"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `adventurer-strange-scenery.claim.reward.primordial-ember::adventure-log-bookshelf-guide`

- evidence_seed_key: "adventurer-strange-scenery.claim.reward.primordial-ember::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "adventurer-strange-scenery.reward.primordial-ember"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `adventurer-strange-scenery.claim.reward.sangpyeong-coin::adventure-log-bookshelf-guide`

- evidence_seed_key: "adventurer-strange-scenery.claim.reward.sangpyeong-coin::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "adventurer-strange-scenery.reward.sangpyeong-coin"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
