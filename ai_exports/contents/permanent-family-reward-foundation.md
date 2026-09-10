<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 영구 가문 보상 기반

## Identity

- slug: "permanent-family-reward-foundation"
- name_ko: "영구 가문 보상 기반"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "한 번 획득하면 가문에 지속 적용되는 의뢰·모험일지 보상을 추적하는 기반이다."
- purpose: "영구 가문 보상을 캐릭터 보상과 반복 지급 보상에서 분리한다."

## Requirements

### `permanent-family-reward-foundation.scope`

- seed_key: "permanent-family-reward-foundation.scope"
- kind: "knowledge"
- requirement_level: "required"
- title: "영구 가문 적용"
- description: "대표 메인 의뢰와 모험일지는 가문 단위 영구 능력치 또는 편의 보상을 제공한다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "persistence": "permanent",
  "repeatable": false,
  "scope": "family"
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

### `permanent-family-reward-foundation.account`

- seed_key: "permanent-family-reward-foundation.account"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "account-progression-foundation"
- content_name_ko: "가문 성장 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/account-progression-foundation.md"
### `kamasylvia-family-defense-quest.parent`

- seed_key: "kamasylvia-family-defense-quest.parent"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "kamasylvia-family-defense-quest"
- content_name_ko: "카마실비아 가문 방어력 의뢰"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/kamasylvia-family-defense-quest.md"
### `odyllita-family-attack-quest.parent`

- seed_key: "odyllita-family-attack-quest.parent"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "odyllita-family-attack-quest"
- content_name_ko: "오드락시아 가문 공격력 의뢰"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/odyllita-family-attack-quest.md"
### `permanent-stat-progression.parent`

- seed_key: "permanent-stat-progression.parent"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "permanent-stat-progression"
- content_name_ko: "영구 능력치 성장"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/permanent-stat-progression.md"
### `adventure-log-foundation.rewards`

- seed_key: "adventure-log-foundation.rewards"
- direction: "incoming"
- relation_type: "related"
- content_slug: "adventure-log-foundation"
- content_name_ko: "모험일지 기반"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/adventure-log-foundation.md"

## Evidence and Sources

### Current evidence

### `permanent-family-reward-foundation.claim.scope::adventure-log-bookshelf-guide`

- evidence_seed_key: "permanent-family-reward-foundation.claim.scope::adventure-log-bookshelf-guide"
- source_id: "adventure-log-bookshelf-guide"
- title: "모험일지 책장"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T15:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "permanent-family-reward-foundation.scope"
- claim_key: "requirement:scope"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `permanent-family-reward-foundation.claim.scope::hyperboost-progression-2026`

- evidence_seed_key: "permanent-family-reward-foundation.claim.scope::hyperboost-progression-2026"
- source_id: "hyperboost-progression-2026"
- title: "2026 Hyper Boost Progression Guide"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=15920"
- publisher: "Pearl Abyss"
- source_type: "official_gm_note"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "permanent-family-reward-foundation.scope"
- claim_key: "requirement:scope"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `permanent-family-reward-foundation.claim.scope::magnus-guide`

- evidence_seed_key: "permanent-family-reward-foundation.claim.scope::magnus-guide"
- source_id: "magnus-guide"
- title: "어비스 원 : 마그누스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=305"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "permanent-family-reward-foundation.scope"
- claim_key: "requirement:scope"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
