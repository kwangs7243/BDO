<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 영구 능력치 성장

## Identity

- slug: "permanent-stat-progression"
- name_ko: "영구 능력치 성장"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "메인 의뢰와 모험일지에서 얻는 가문 공통 공격력·방어력 등 영구 능력치를 모아 보는 기반이다."
- purpose: "장비 수치와 별개인 가문 영구 능력치 획득 경로를 연결한다."

## Requirements

### `permanent-stat-progression.scope`

- seed_key: "permanent-stat-progression.scope"
- kind: "stat"
- requirement_level: "required"
- title: "가문 영구 능력치"
- description: "일부 메인 의뢰와 모험일지 완료 보상은 가문 전체의 영구 능력치에 반영된다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "persistence": "permanent",
  "scope": "family",
  "separate_from_gear": true
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

- None

## Related Contents

### `permanent-stat-progression.parent`

- seed_key: "permanent-stat-progression.parent"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "permanent-family-reward-foundation"
- content_name_ko: "영구 가문 보상 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/permanent-family-reward-foundation.md"
### `permanent-stat-progression.combat-stats`

- seed_key: "permanent-stat-progression.combat-stats"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "combat-stat-foundation"
- content_name_ko: "전투 능력치 기초"
- content_category: "combat_pve"
- note: null
- order_no: 2
- relative_path: "../contents/combat-stat-foundation.md"
### `igor-bartali-adventure-log.stats`

- seed_key: "igor-bartali-adventure-log.stats"
- direction: "incoming"
- relation_type: "related"
- content_slug: "igor-bartali-adventure-log"
- content_name_ko: "이고르 바탈리의 모험일지"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/igor-bartali-adventure-log.md"
### `kamasylvia-family-defense-quest.stats`

- seed_key: "kamasylvia-family-defense-quest.stats"
- direction: "incoming"
- relation_type: "related"
- content_slug: "kamasylvia-family-defense-quest"
- content_name_ko: "카마실비아 가문 방어력 의뢰"
- content_category: "progression"
- note: null
- order_no: 3
- relative_path: "../contents/kamasylvia-family-defense-quest.md"
### `odyllita-family-attack-quest.stats`

- seed_key: "odyllita-family-attack-quest.stats"
- direction: "incoming"
- relation_type: "related"
- content_slug: "odyllita-family-attack-quest"
- content_name_ko: "오드락시아 가문 공격력 의뢰"
- content_category: "progression"
- note: null
- order_no: 3
- relative_path: "../contents/odyllita-family-attack-quest.md"
### `main-quest-morning-land.stats`

- seed_key: "main-quest-morning-land.stats"
- direction: "incoming"
- relation_type: "related"
- content_slug: "main-quest-morning-land"
- content_name_ko: "아침의 나라 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 4
- relative_path: "../contents/main-quest-morning-land.md"

## Evidence and Sources

### Current evidence

### `permanent-stat-progression.claim.scope::adventure-log-bookshelf-guide`

- evidence_seed_key: "permanent-stat-progression.claim.scope::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "permanent-stat-progression.scope"
- claim_key: "requirement:scope"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `permanent-stat-progression.claim.scope::family-stat-quest-history`

- evidence_seed_key: "permanent-stat-progression.claim.scope::family-stat-quest-history"
- source_id: "family-stat-quest-history"
- title: "Kamasylvia and Odyllita Family Stat Quest History"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=9723"
- publisher: "Pearl Abyss"
- source_type: "official_history"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "permanent-stat-progression.scope"
- claim_key: "requirement:scope"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `permanent-stat-progression.claim.scope::hyperboost-progression-2026`

- evidence_seed_key: "permanent-stat-progression.claim.scope::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "permanent-stat-progression.scope"
- claim_key: "requirement:scope"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
