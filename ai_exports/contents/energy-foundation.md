<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 기운 기반

## Identity

- slug: "energy-foundation"
- name_ko: "기운 기반"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "최대 기운은 가문 공유지만 현재 보유 기운은 캐릭터별이며, 기본 자연 회복은 접속 중 3분당 1, 미접속 중 1시간당 1이다."
- purpose: "가문 최대치와 캐릭터별 현재치를 분리하고 최신 채집 기운 변경을 기록한다."

## Requirements

### `energy-foundation.pool-scopes`

- seed_key: "energy-foundation.pool-scopes"
- kind: "stat"
- requirement_level: "required"
- title: "최대치와 현재치의 범위"
- description: "증가한 최대 기운은 가문 모든 캐릭터가 공유하지만 현재 보유 기운은 캐릭터별이다."
- structured_value:

```json
{
  "base_max_energy": 30,
  "current_energy_scope": "per_character",
  "globally_shared_current_pool": false,
  "maximum_energy_scope": "family_shared",
  "primary_growth": "knowledge_categories"
}
```

### `energy-foundation.natural-regeneration`

- seed_key: "energy-foundation.natural-regeneration"
- kind: "stat"
- requirement_level: "required"
- title: "기본 자연 회복"
- description: "버프를 제외한 기본 회복은 접속 캐릭터 3분당 1, 미접속 캐릭터 1시간당 1이다."
- structured_value:

```json
{
  "baseline": true,
  "offline": {
    "amount": 1,
    "hours": 1
  },
  "online": {
    "amount": 1,
    "minutes": 3
  }
}
```

### `energy-foundation.gathering-change`

- seed_key: "energy-foundation.gathering-change"
- kind: "stat"
- requirement_level: "required"
- title: "채집 기운 최신 변경"
- description: "채집 시 기운을 소모하지 않을 확률은 기존 대비 10% 상향됐고 전문 3에서 최대에 도달한다."
- structured_value:

```json
{
  "exact_maximum_percent": null,
  "maximum_reached_at": "Professional 3",
  "no_energy_consumption_chance_increase_percentage_points": 10
}
```

### `energy-foundation.removed-lightstone-energy`

- seed_key: "energy-foundation.removed-lightstone-energy"
- kind: "gear"
- requirement_level: "required"
- title: "삭제된 광명석 기운 효과"
- description: "개운한 꿈 조합은 삭제됐고 하품하는 고슴도치의 기운 회복 효과도 제거됐다."
- structured_value:

```json
{
  "refreshing_dream_deleted": true,
  "yawning_hedgehog_energy_regeneration_removed": true
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `energy-foundation.scope-warning`

- seed_key: "energy-foundation.scope-warning"
- section_type: "common_mistakes"
- title: "가문 최대치와 캐릭터 현재치"
- order_no: 1

#### body_markdown

생활 레벨과 생활 장비가 가문 단위라는 사실을 현재 기운 pool까지 가문 공용이라는 뜻으로 확대하면 안 된다.

## Related Contents

### `energy-foundation.artifact-effects`

- seed_key: "energy-foundation.artifact-effects"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-artifacts-lightstones"
- content_name_ko: "생활 유물과 광명석"
- content_category: "life"
- note: "9월 2일 삭제·변경된 기운 관련 광명석 효과와 연결한다."
- order_no: 1
- relative_path: "../contents/life-artifacts-lightstones.md"
### `energy-foundation.mastery-effects`

- seed_key: "energy-foundation.mastery-effects"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-mastery-effects"
- content_name_ko: "생활 분야별 숙련도 효과"
- content_category: "life"
- note: "채집의 기운 소비와 숙련도의 채집 결과 효과는 서로 다른 규칙이다."
- order_no: 2
- relative_path: "../contents/life-mastery-effects.md"
### `account-progression-foundation.energy`

- seed_key: "account-progression-foundation.energy"
- direction: "incoming"
- relation_type: "related"
- content_slug: "account-progression-foundation"
- content_name_ko: "가문 성장 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/account-progression-foundation.md"
### `gathering-current-system.energy-foundation`

- seed_key: "gathering-current-system.energy-foundation"
- direction: "incoming"
- relation_type: "related"
- content_slug: "gathering-current-system"
- content_name_ko: "채집 현재 시스템"
- content_category: "life"
- note: "기운 범위와 회복 규칙 재사용"
- order_no: 1
- relative_path: "../contents/gathering-current-system.md"
### `gathering-onboarding-strategy.energy`

- seed_key: "gathering-onboarding-strategy.energy"
- direction: "incoming"
- relation_type: "related"
- content_slug: "gathering-onboarding-strategy"
- content_name_ko: "채집 입문 전략"
- content_category: "life"
- note: "세션 범위를 정할 때 기운 구조를 확인한다."
- order_no: 4
- relative_path: "../contents/gathering-onboarding-strategy.md"
### `pet-current-system.energy-knowledge`

- seed_key: "pet-current-system.energy-knowledge"
- direction: "incoming"
- relation_type: "related"
- content_slug: "pet-current-system"
- content_name_ko: "반려동물 현재 시스템"
- content_category: "progression"
- note: "지식 획득 관련 반려동물 효과를 검토할 때 연결"
- order_no: 4
- relative_path: "../contents/pet-current-system.md"

## Evidence and Sources

### Current evidence

### `energy-foundation.summary::energy-advanced-guide`

- evidence_seed_key: "energy-foundation.summary::energy-advanced-guide"
- source_id: "energy-advanced-guide"
- title: "기운 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=30"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "energy-foundation"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "최대·현재 기운 범위와 자연 회복"
- active: true
- is_active: true

### `energy-foundation.summary::energy-profile-guide`

- evidence_seed_key: "energy-foundation.summary::energy-profile-guide"
- source_id: "energy-profile-guide"
- title: "내 정보"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=14"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "energy-foundation"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "최대·현재 기운 범위와 자연 회복"
- active: true
- is_active: true

### `energy-foundation.requirement.gathering-change::life-unification-2026-09-02`

- evidence_seed_key: "energy-foundation.requirement.gathering-change::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "energy-foundation.gathering-change"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "채집 무소모 확률 상향과 전문 3 상한"
- active: true
- is_active: true

### `energy-foundation.requirement.natural-regeneration::energy-advanced-guide`

- evidence_seed_key: "energy-foundation.requirement.natural-regeneration::energy-advanced-guide"
- source_id: "energy-advanced-guide"
- title: "기운 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=30"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "energy-foundation.natural-regeneration"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "접속/미접속 기본 자연 회복"
- active: true
- is_active: true

### `energy-foundation.requirement.pool-scopes::energy-advanced-guide`

- evidence_seed_key: "energy-foundation.requirement.pool-scopes::energy-advanced-guide"
- source_id: "energy-advanced-guide"
- title: "기운 고급편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=30"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "energy-foundation.pool-scopes"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "최대 기운 가문 공유, 현재 기운 캐릭터별"
- active: true
- is_active: true

### `energy-foundation.requirement.pool-scopes::energy-profile-guide`

- evidence_seed_key: "energy-foundation.requirement.pool-scopes::energy-profile-guide"
- source_id: "energy-profile-guide"
- title: "내 정보"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=14"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "energy-foundation.pool-scopes"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "최대 기운 가문 공유, 현재 기운 캐릭터별"
- active: true
- is_active: true

### `energy-foundation.requirement.removed-lightstone-energy::life-unification-2026-09-02`

- evidence_seed_key: "energy-foundation.requirement.removed-lightstone-energy::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "energy-foundation.removed-lightstone-energy"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "삭제된 개운한 꿈과 고슴도치 기운 회복 효과"
- active: true
- is_active: true

### Historical / inactive evidence

### `energy-foundation.legacy.shared-current-pool::energy-profile-guide`

- evidence_seed_key: "energy-foundation.legacy.shared-current-pool::energy-profile-guide"
- source_id: "energy-profile-guide"
- title: "내 정보"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=14"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "energy-foundation"
- claim_key: "legacy.current_energy_family_pool"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "현재 보유 기운을 가문 공용 pool로 보는 해석은 잘못됨"
- active: false
- is_active: false
