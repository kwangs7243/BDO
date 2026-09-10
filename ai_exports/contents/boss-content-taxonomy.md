<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 우두머리 콘텐츠 분류

## Identity

- slug: "boss-content-taxonomy"
- name_ko: "우두머리 콘텐츠 분류"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "varies"

## Overview

- summary: "검은사당 동해도·황해도, 월드 우두머리, 필드 우두머리를 서로 다른 규칙 체계로 구분한다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `boss-content-taxonomy.contexts`

- seed_key: "boss-content-taxonomy.contexts"
- kind: "knowledge"
- requirement_level: "required"
- title: "콘텐츠 맥락"
- description: "같은 이름의 우두머리라도 검은사당과 월드 우두머리는 별도 엔터티다."
- structured_value:

```json
{
  "contexts": [
    "black_shrine_donghae",
    "black_shrine_hwanghae",
    "world_boss",
    "field_boss"
  ],
  "knowledge_role": "fact",
  "same_name_entities_are_context_scoped": true
}
```

### `boss-content-taxonomy.black-shadow`

- seed_key: "boss-content-taxonomy.black-shadow"
- kind: "knowledge"
- requirement_level: "required"
- title: "검은 그림자 분류"
- description: "검은 그림자는 월드 우두머리가 아니라 토요일 17:00에 등장하는 필드 우두머리이며, 향후 제거 발표만으로 현재 삭제 처리하지 않는다."
- structured_value:

```json
{
  "context": "field_boss",
  "deleted_currently": false,
  "entity": "Black Shadow",
  "knowledge_role": "fact",
  "spawn_time": "17:00",
  "spawn_weekday": 5,
  "timezone": "Asia/Seoul",
  "world_boss": false
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

### `guild-boss-current-system.relation.taxonomy`

- seed_key: "guild-boss-current-system.relation.taxonomy"
- direction: "incoming"
- relation_type: "related"
- content_slug: "guild-boss-current-system"
- content_name_ko: "길드 우두머리 현행 시스템"
- content_category: "combat_pve"
- note: "우두머리 분류"
- order_no: 1
- relative_path: "../contents/guild-boss-current-system.md"
### `world-boss-current-system.taxonomy`

- seed_key: "world-boss-current-system.taxonomy"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "world-boss-current-system"
- content_name_ko: "월드 우두머리 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-current-system.md"
### `black-shrine-donghae-current-system.taxonomy`

- seed_key: "black-shrine-donghae-current-system.taxonomy"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "black-shrine-donghae-current-system"
- content_name_ko: "검은사당 동해도 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 2
- relative_path: "../contents/black-shrine-donghae-current-system.md"
### `black-shrine-hwanghae-current-system.taxonomy`

- seed_key: "black-shrine-hwanghae-current-system.taxonomy"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "black-shrine-hwanghae-current-system"
- content_name_ko: "검은사당 황해도 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 2
- relative_path: "../contents/black-shrine-hwanghae-current-system.md"

## Evidence and Sources

### Current evidence

### `boss-content-taxonomy.claim.black-shadow::rare-wild-horses-2025-12-23`

- evidence_seed_key: "boss-content-taxonomy.claim.black-shadow::rare-wild-horses-2025-12-23"
- source_id: "rare-wild-horses-2025-12-23"
- title: "12월 23일(화) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14989"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-23"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "boss-content-taxonomy.black-shadow"
- claim_key: "requirement:black-shadow"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `boss-content-taxonomy.claim.contexts::black-shrine-donghae-guide`

- evidence_seed_key: "boss-content-taxonomy.claim.contexts::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "boss-content-taxonomy.contexts"
- claim_key: "requirement:contexts"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `boss-content-taxonomy.claim.contexts::black-shrine-hwanghae-guide`

- evidence_seed_key: "boss-content-taxonomy.claim.contexts::black-shrine-hwanghae-guide"
- source_id: "black-shrine-hwanghae-guide"
- title: "검은 사당 - 황해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=404"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "boss-content-taxonomy.contexts"
- claim_key: "requirement:contexts"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `boss-content-taxonomy.claim.contexts::world-boss-guide`

- evidence_seed_key: "boss-content-taxonomy.claim.contexts::world-boss-guide"
- source_id: "world-boss-guide"
- title: "월드 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=89"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "boss-content-taxonomy.contexts"
- claim_key: "requirement:contexts"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
