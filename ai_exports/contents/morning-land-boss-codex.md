<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 우두머리 도감 : 아침의 나라

## Identity

- slug: "morning-land-boss-codex"
- name_ko: "우두머리 도감 : 아침의 나라"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "아침의 나라 우두머리 기록과 권별 보상을 책장에서 확인하는 도감형 진행 콘텐츠다."
- purpose: "검은 사당 주간 토벌과 동일 entity로 합치지 않고 도감 완료 보상만 추적한다."

## Requirements

### `morning-land-boss-codex.identity`

- seed_key: "morning-land-boss-codex.identity"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 책장 identity"
- description: "일반 모험일지와 구분되는 boss codex이며 현재 공식 보상 표는 2~5권 완료 보상을 제시한다."
- structured_value:

```json
{
  "bookshelf_group": "우두머리 도감 : 아침의 나라",
  "family_content": true,
  "journal_kind": "boss_codex",
  "knowledge_role": "fact",
  "rewarded_volumes": [
    2,
    3,
    4,
    5
  ],
  "same_as_black_shrine_weekly": false
}
```

### `morning-land-boss-codex.unlock`

- seed_key: "morning-land-boss-codex.unlock"
- kind: "quest"
- requirement_level: "required"
- title: "현재 해금 조건"
- description: "현재 공식 책장 표에는 별도 획득 조건이 없다고 표시된다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "unlock_condition": "none_listed"
}
```

## Steps

### `morning-land-boss-codex.step.unlock`

- seed_key: "morning-land-boss-codex.step.unlock"
- phase: "unlock"
- order_no: 1
- title: "해금 조건 확인"
- description: "현재 공식 책장 표에는 별도 획득 조건이 없다고 표시된다."
- checkable: true

### `morning-land-boss-codex.step.complete`

- seed_key: "morning-land-boss-codex.step.complete"
- phase: "reward"
- order_no: 2
- title: "일지 진행과 보상 확인"
- description: "장별 목표를 순서대로 완료하고 공식 책장에 표시된 현재 보상을 확인한다."
- checkable: true

## Schedules

- None

## Rewards

### `morning-land-boss-codex.reward.hongik-ember`

- seed_key: "morning-land-boss-codex.reward.hongik-ember"
- name: "피어오르는 홍익의 불씨"
- reward_type: "fixed_item"
- amount: 220.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "2~5권 보상 40+50+60+70개 합산"
- order_no: 1

## Sections

- None

## Related Contents

### `morning-land-boss-codex.foundation`

- seed_key: "morning-land-boss-codex.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "adventure-log-foundation"
- content_name_ko: "모험일지 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/adventure-log-foundation.md"
### `morning-land-boss-codex.donghae`

- seed_key: "morning-land-boss-codex.donghae"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "black-shrine-donghae-current-system"
- content_name_ko: "검은사당 동해도 현재 시스템"
- content_category: "combat_pve"
- note: "주간 토벌 Content와 identity 분리"
- order_no: 2
- relative_path: "../contents/black-shrine-donghae-current-system.md"
### `morning-land-boss-codex.hwanghae`

- seed_key: "morning-land-boss-codex.hwanghae"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "black-shrine-hwanghae-current-system"
- content_name_ko: "검은사당 황해도 현재 시스템"
- content_category: "combat_pve"
- note: "주간 토벌 Content와 identity 분리"
- order_no: 3
- relative_path: "../contents/black-shrine-hwanghae-current-system.md"

## Evidence and Sources

### Current evidence

### `morning-land-boss-codex.claim.purpose::adventure-log-bookshelf-guide`

- evidence_seed_key: "morning-land-boss-codex.claim.purpose::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "morning-land-boss-codex"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `morning-land-boss-codex.claim.summary::adventure-log-bookshelf-guide`

- evidence_seed_key: "morning-land-boss-codex.claim.summary::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "morning-land-boss-codex"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `morning-land-boss-codex.claim.identity::adventure-log-bookshelf-guide`

- evidence_seed_key: "morning-land-boss-codex.claim.identity::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "morning-land-boss-codex.identity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `morning-land-boss-codex.claim.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "morning-land-boss-codex.claim.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "morning-land-boss-codex.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `morning-land-boss-codex.claim.step.complete::adventure-log-bookshelf-guide`

- evidence_seed_key: "morning-land-boss-codex.claim.step.complete::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "morning-land-boss-codex.step.complete"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `morning-land-boss-codex.claim.step.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "morning-land-boss-codex.claim.step.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "morning-land-boss-codex.step.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `morning-land-boss-codex.claim.reward.hongik-ember::adventure-log-bookshelf-guide`

- evidence_seed_key: "morning-land-boss-codex.claim.reward.hongik-ember::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "morning-land-boss-codex.reward.hongik-ember"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
