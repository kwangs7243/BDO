<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 마가한의 서

## Identity

- slug: "book-of-margahan"
- name_ko: "마가한의 서"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "아그리스의 열기 최대치·일일 회복량·잡동사니 수량 효과를 강화하는 모험일지다."
- purpose: "아그리스 자체 해금과 모험일지 강화 효과를 혼동하지 않도록 분리한다."

## Requirements

### `book-of-margahan.unlock`

- seed_key: "book-of-margahan.unlock"
- kind: "quest"
- requirement_level: "required"
- title: "그믐달 상단의 행동일지 해금"
- description: "58레벨 이상에서 흑정령의 [모험일지] 그믐달 상단의 행동일지를 완료하면 마가한의 서를 진행할 수 있다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "minimum_level": 58,
  "unlock_quest": "[모험일지] 그믐달 상단의 행동일지"
}
```

### `book-of-margahan.agris-enhancement`

- seed_key: "book-of-margahan.agris-enhancement"
- kind: "stat"
- requirement_level: "required"
- title: "아그리스 강화 효과"
- description: "1권과 2권 완료로 기본 최대치 50,000에 50,000, 일일 회복 15,000에 5,000, 잡동사니 수량 증가 100%에 50%p를 더한다."
- structured_value:

```json
{
  "agris_point_cap_increase": 50000,
  "daily_recovery_increase": 5000,
  "does_not_unlock_agris": true,
  "knowledge_role": "fact",
  "trash_loot_bonus_percentage_point_increase": 50
}
```

## Steps

### `book-of-margahan.step.volume-1`

- seed_key: "book-of-margahan.step.volume-1"
- phase: "first_time"
- order_no: 1
- title: "1권 완료"
- description: "1권 목표를 완료해 아그리스 최대치와 잡동사니 수량 효과를 강화한다."
- checkable: false

### `book-of-margahan.step.volume-2`

- seed_key: "book-of-margahan.step.volume-2"
- phase: "reward"
- order_no: 2
- title: "2권 완료"
- description: "60레벨 이후 2권 목표를 완료해 최대치와 일일 회복량 강화를 마친다."
- checkable: false

## Schedules

- None

## Rewards

### `book-of-margahan.reward.point-cap`

- seed_key: "book-of-margahan.reward.point-cap"
- name: "아그리스 최대 포인트 증가"
- reward_type: "fixed_effect"
- amount: 50000.0
- min_amount: null
- max_amount: null
- unit: "point"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 1

### `book-of-margahan.reward.daily-recovery`

- seed_key: "book-of-margahan.reward.daily-recovery"
- name: "아그리스 일일 회복량 증가"
- reward_type: "fixed_effect"
- amount: 5000.0
- min_amount: null
- max_amount: null
- unit: "point_per_day"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 2

### `book-of-margahan.reward.trash-bonus`

- seed_key: "book-of-margahan.reward.trash-bonus"
- name: "잡동사니 수량 증가 효과 추가"
- reward_type: "fixed_effect"
- amount: 50.0
- min_amount: null
- max_amount: null
- unit: "percentage_point"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 3

## Sections

- None

## Related Contents

### `book-of-margahan.foundation`

- seed_key: "book-of-margahan.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "adventure-log-foundation"
- content_name_ko: "모험일지 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/adventure-log-foundation.md"
### `book-of-margahan.agris`

- seed_key: "book-of-margahan.agris"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "agris-fever"
- content_name_ko: "아그리스의 열기"
- content_category: "combat_pve"
- note: "마가한의 서는 아그리스의 열기를 해금하지 않고 기존 효과를 강화한다."
- order_no: 2
- relative_path: "../contents/agris-fever.md"

## Evidence and Sources

### Current evidence

### `book-of-margahan.claim.purpose::adventure-log-bookshelf-guide`

- evidence_seed_key: "book-of-margahan.claim.purpose::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "book-of-margahan"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `book-of-margahan.claim.purpose::agris-fever-guide`

- evidence_seed_key: "book-of-margahan.claim.purpose::agris-fever-guide"
- source_id: "agris-fever-guide"
- title: "아그리스의 열기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=175"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "book-of-margahan"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `book-of-margahan.claim.summary::adventure-log-bookshelf-guide`

- evidence_seed_key: "book-of-margahan.claim.summary::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "book-of-margahan"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `book-of-margahan.claim.summary::agris-fever-guide`

- evidence_seed_key: "book-of-margahan.claim.summary::agris-fever-guide"
- source_id: "agris-fever-guide"
- title: "아그리스의 열기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=175"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "book-of-margahan"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `book-of-margahan.claim.enhancement::agris-fever-guide`

- evidence_seed_key: "book-of-margahan.claim.enhancement::agris-fever-guide"
- source_id: "agris-fever-guide"
- title: "아그리스의 열기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=175"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "book-of-margahan.agris-enhancement"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `book-of-margahan.claim.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "book-of-margahan.claim.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "book-of-margahan.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `book-of-margahan.claim.unlock::agris-fever-guide`

- evidence_seed_key: "book-of-margahan.claim.unlock::agris-fever-guide"
- source_id: "agris-fever-guide"
- title: "아그리스의 열기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=175"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "book-of-margahan.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `book-of-margahan.claim.step-volume-1::agris-fever-guide`

- evidence_seed_key: "book-of-margahan.claim.step-volume-1::agris-fever-guide"
- source_id: "agris-fever-guide"
- title: "아그리스의 열기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=175"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "book-of-margahan.step.volume-1"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `book-of-margahan.claim.step-volume-2::agris-fever-guide`

- evidence_seed_key: "book-of-margahan.claim.step-volume-2::agris-fever-guide"
- source_id: "agris-fever-guide"
- title: "아그리스의 열기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=175"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "book-of-margahan.step.volume-2"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `book-of-margahan.claim.reward-recovery::agris-fever-guide`

- evidence_seed_key: "book-of-margahan.claim.reward-recovery::agris-fever-guide"
- source_id: "agris-fever-guide"
- title: "아그리스의 열기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=175"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "book-of-margahan.reward.daily-recovery"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `book-of-margahan.claim.reward-cap::agris-fever-guide`

- evidence_seed_key: "book-of-margahan.claim.reward-cap::agris-fever-guide"
- source_id: "agris-fever-guide"
- title: "아그리스의 열기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=175"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "book-of-margahan.reward.point-cap"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `book-of-margahan.claim.reward-bonus::agris-fever-guide`

- evidence_seed_key: "book-of-margahan.claim.reward-bonus::agris-fever-guide"
- source_id: "agris-fever-guide"
- title: "아그리스의 열기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=175"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "book-of-margahan.reward.trash-bonus"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
