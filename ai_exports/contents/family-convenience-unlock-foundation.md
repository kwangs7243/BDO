<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 가문 편의 기능 해금

## Identity

- slug: "family-convenience-unlock-foundation"
- name_ko: "가문 편의 기능 해금"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "가문 진행으로 영구 해금되는 이동·창고·공용 편의 기능의 연결 기반이다."
- purpose: "편의 기능 자체의 상세 규칙을 중복하지 않고 선행 진행만 연결한다."

## Requirements

### `family-convenience-unlock-foundation.scope`

- seed_key: "family-convenience-unlock-foundation.scope"
- kind: "quest"
- requirement_level: "required"
- title: "가문 편의 해금"
- description: "마그누스 연속 의뢰 완료로 심연의 혈관 이동과 다른 지역 창고 이용 같은 가문 편의가 열린다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "scope": "family",
  "unlock_kind": "convenience"
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

### `family-convenience-unlock-foundation.account`

- seed_key: "family-convenience-unlock-foundation.account"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "account-progression-foundation"
- content_name_ko: "가문 성장 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/account-progression-foundation.md"
### `family-convenience-unlock-foundation.remote-storage`

- seed_key: "family-convenience-unlock-foundation.remote-storage"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "magnus-remote-storage"
- content_name_ko: "마그누스 원격 창고"
- content_category: "life"
- note: null
- order_no: 2
- relative_path: "../contents/magnus-remote-storage.md"
### `family-convenience-unlock-foundation.family-silver`

- seed_key: "family-convenience-unlock-foundation.family-silver"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "family-silver-unification"
- content_name_ko: "가문 통합 은화"
- content_category: "life"
- note: null
- order_no: 3
- relative_path: "../contents/family-silver-unification.md"
### `family-convenience-unlock-foundation.storage`

- seed_key: "family-convenience-unlock-foundation.storage"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "storage-current-system"
- content_name_ko: "창고 현재 시스템"
- content_category: "life"
- note: null
- order_no: 4
- relative_path: "../contents/storage-current-system.md"
### `fairy-current-system.family-convenience`

- seed_key: "fairy-current-system.family-convenience"
- direction: "incoming"
- relation_type: "related"
- content_slug: "fairy-current-system"
- content_name_ko: "요정 레이라 현재 시스템"
- content_category: "progression"
- note: "가문 편의 해금 흐름과 연결"
- order_no: 2
- relative_path: "../contents/fairy-current-system.md"
### `magnus-progression.convenience`

- seed_key: "magnus-progression.convenience"
- direction: "incoming"
- relation_type: "related"
- content_slug: "magnus-progression"
- content_name_ko: "마그누스 전체 진행"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/magnus-progression.md"
### `pet-current-system.family-convenience`

- seed_key: "pet-current-system.family-convenience"
- direction: "incoming"
- relation_type: "related"
- content_slug: "pet-current-system"
- content_name_ko: "반려동물 현재 시스템"
- content_category: "progression"
- note: "가문 편의 해금 흐름과 연결"
- order_no: 2
- relative_path: "../contents/pet-current-system.md"

## Evidence and Sources

### Current evidence

### `family-convenience-unlock-foundation.claim.scope::magnus-guide`

- evidence_seed_key: "family-convenience-unlock-foundation.claim.scope::magnus-guide"
- source_id: "magnus-guide"
- title: "어비스 원 : 마그누스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=305"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "family-convenience-unlock-foundation.scope"
- claim_key: "requirement:scope"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
