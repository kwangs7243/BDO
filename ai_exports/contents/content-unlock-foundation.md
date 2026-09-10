<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 콘텐츠 해금 기반

## Identity

- slug: "content-unlock-foundation"
- name_ko: "콘텐츠 해금 기반"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "주요 의뢰 완료가 새 이동 수단·시스템·전투 콘텐츠를 여는 관계를 모아 보는 기반이다."
- purpose: "선행 의뢰와 실제 해금 대상을 명시적인 관계로 추적한다."

## Requirements

### `content-unlock-foundation.rule`

- seed_key: "content-unlock-foundation.rule"
- kind: "quest"
- requirement_level: "required"
- title: "선행 의뢰 기반 해금"
- description: "일부 시스템과 콘텐츠는 지정 메인 의뢰 또는 연속 의뢰 완료 후 이용할 수 있다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "progression_effect": "content_unlock"
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

### `content-unlock-foundation.account`

- seed_key: "content-unlock-foundation.account"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "account-progression-foundation"
- content_name_ko: "가문 성장 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/account-progression-foundation.md"
### `content-unlock-foundation.magnus-storage`

- seed_key: "content-unlock-foundation.magnus-storage"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "magnus-remote-storage"
- content_name_ko: "마그누스 원격 창고"
- content_category: "life"
- note: null
- order_no: 2
- relative_path: "../contents/magnus-remote-storage.md"
### `content-unlock-foundation.black-shrine`

- seed_key: "content-unlock-foundation.black-shrine"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "black-shrine-donghae-weekly"
- content_name_ko: "검은 사당 - 동해도 주간 토벌"
- content_category: "combat_pve"
- note: null
- order_no: 3
- relative_path: "../contents/black-shrine-donghae-weekly.md"

## Evidence and Sources

### Current evidence

### `content-unlock-foundation.claim.rule::magnus-guide`

- evidence_seed_key: "content-unlock-foundation.claim.rule::magnus-guide"
- source_id: "magnus-guide"
- title: "어비스 원 : 마그누스"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=305"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "content-unlock-foundation.rule"
- claim_key: "requirement:rule"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `content-unlock-foundation.claim.rule::morning-land-launch-2023-03-29`

- evidence_seed_key: "content-unlock-foundation.claim.rule::morning-land-launch-2023-03-29"
- source_id: "morning-land-launch-2023-03-29"
- title: "2023-03-29 Update - Land of the Morning Light"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=10062"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-03-29"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "content-unlock-foundation.rule"
- claim_key: "requirement:rule"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
