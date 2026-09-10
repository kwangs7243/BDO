<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 아침의 나라 이야기 도감 : 동해도/황해도 편

## Identity

- slug: "morning-land-story-codex"
- name_ko: "아침의 나라 이야기 도감 : 동해도/황해도 편"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "이미 진행한 아침의 나라 이야기를 다시 보는 재감상용 도감이다."
- purpose: "영구 능력치 progression journal과 구분하고 메인 의뢰 선택 분기에 따라 페이지가 채워지는 archive 성격을 기록한다."

## Requirements

### `morning-land-story-codex.identity`

- seed_key: "morning-land-story-codex.identity"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 책장 identity"
- description: "기존 모험일지와 달리 이야기 재감상용 도감이며 메인 의뢰 진행과 선택 분기에서 얻은 지식으로 빈 페이지가 채워진다."
- structured_value:

```json
{
  "bookshelf_group": "아침의 나라 이야기 도감 : 동해도/황해도 편",
  "family_content": true,
  "journal_kind": "story_replay_archive",
  "knowledge_role": "fact",
  "page_fill_dependency": "morning_land_story_knowledge_and_choices",
  "standard_stat_progression": false
}
```

### `morning-land-story-codex.unlock`

- seed_key: "morning-land-story-codex.unlock"
- kind: "quest"
- requirement_level: "required"
- title: "현재 해금 조건"
- description: "현재 공식 책장 표에는 별도 획득 조건이 없지만 페이지 내용은 아침의 나라 이야기 진행과 선택 분기에 따라 채워진다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "unlock_condition": "none_listed"
}
```

## Steps

### `morning-land-story-codex.step.unlock`

- seed_key: "morning-land-story-codex.step.unlock"
- phase: "unlock"
- order_no: 1
- title: "해금 조건 확인"
- description: "현재 공식 책장 표에는 별도 획득 조건이 없지만 페이지 내용은 아침의 나라 이야기 진행과 선택 분기에 따라 채워진다."
- checkable: true

### `morning-land-story-codex.step.complete`

- seed_key: "morning-land-story-codex.step.complete"
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

### `morning-land-story-codex.foundation`

- seed_key: "morning-land-story-codex.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "adventure-log-foundation"
- content_name_ko: "모험일지 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/adventure-log-foundation.md"
### `morning-land-story-codex.morning-land-main`

- seed_key: "morning-land-story-codex.morning-land-main"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "main-quest-morning-land"
- content_name_ko: "아침의 나라 메인 의뢰"
- content_category: "progression"
- note: "메인 의뢰 진행과 선택 분기에 따라 페이지가 채워짐"
- order_no: 2
- relative_path: "../contents/main-quest-morning-land.md"

## Evidence and Sources

### Current evidence

### `morning-land-story-codex.claim.purpose::adventure-log-bookshelf-guide`

- evidence_seed_key: "morning-land-story-codex.claim.purpose::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "morning-land-story-codex"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `morning-land-story-codex.claim.summary::adventure-log-bookshelf-guide`

- evidence_seed_key: "morning-land-story-codex.claim.summary::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "morning-land-story-codex"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `morning-land-story-codex.claim.identity::adventure-log-bookshelf-guide`

- evidence_seed_key: "morning-land-story-codex.claim.identity::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "morning-land-story-codex.identity"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `morning-land-story-codex.claim.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "morning-land-story-codex.claim.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "morning-land-story-codex.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `morning-land-story-codex.claim.step.complete::adventure-log-bookshelf-guide`

- evidence_seed_key: "morning-land-story-codex.claim.step.complete::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "morning-land-story-codex.step.complete"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `morning-land-story-codex.claim.step.unlock::adventure-log-bookshelf-guide`

- evidence_seed_key: "morning-land-story-codex.claim.step.unlock::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "morning-land-story-codex.step.unlock"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
