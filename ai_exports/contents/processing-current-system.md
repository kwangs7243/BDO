<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 가공 현재 시스템

## Identity

- slug: "processing-current-system"
- name_ko: "가공 현재 시스템"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "가공은 여러 방식으로 재료를 변환하며 기본 성공률은 70%다. 간이 연금과 간이 요리는 가공 레벨이 아닌 각각 연금·요리 성장에 연결된다."
- purpose: "가공 방식, 기본 성공률과 레벨 효과를 현재 가이드 기준으로 정리한다."

## Requirements

### `processing-current-system.methods`

- seed_key: "processing-current-system.methods"
- kind: "other"
- requirement_level: "required"
- title: "가공 방식"
- description: "현재 가이드의 대표 가공 방식이다."
- structured_value:

```json
{
  "methods": [
    "흔들어 섞기",
    "빻기",
    "장작 패기",
    "말리기",
    "솎아내기",
    "가열하기",
    "수리하기",
    "간이 연금",
    "간이 요리",
    "공작",
    "황실 포장"
  ]
}
```

### `processing-current-system.simple-progression`

- seed_key: "processing-current-system.simple-progression"
- kind: "stat"
- requirement_level: "required"
- title: "간이 가공 성장 분야"
- description: "간이 연금과 간이 요리는 가공 경험치가 아니라 각각 연금과 요리 성장에 연결된다."
- structured_value:

```json
{
  "processing": false,
  "simple_alchemy": "alchemy",
  "simple_cooking": "cooking"
}
```

### `processing-current-system.base-success`

- seed_key: "processing-current-system.base-success"
- kind: "stat"
- requirement_level: "required"
- title: "기본 성공률"
- description: "장비와 기타 효과를 더하기 전 기본 가공 성공률은 70%다."
- structured_value:

```json
{
  "base_success_percent": 70,
  "globally_increased_above_70": false
}
```

### `processing-current-system.level-effects`

- seed_key: "processing-current-system.level-effects"
- kind: "stat"
- requirement_level: "required"
- title: "가공 레벨 효과"
- description: "가공 레벨이 오르면 일반 결과물 수량과 높은 등급 결과물 획득 가능성이 증가한다. 구체 확률은 추정하지 않는다."
- structured_value:

```json
{
  "exact_probability": null,
  "higher_grade_result_chance_increases": true,
  "normal_output_quantity_increases": true
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

### `processing-current-system.mastery`

- seed_key: "processing-current-system.mastery"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-mastery-effects"
- content_name_ko: "생활 분야별 숙련도 효과"
- content_category: "life"
- note: "가공 숙련도 기반"
- order_no: 1
- relative_path: "../contents/life-mastery-effects.md"
### `processing-current-system.mass`

- seed_key: "processing-current-system.mass"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "mass-processing"
- content_name_ko: "대량가공"
- content_category: "life"
- note: "대량가공"
- order_no: 2
- relative_path: "../contents/mass-processing.md"
### `processing-current-system.gear`

- seed_key: "processing-current-system.gear"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "processing-stones-and-clothes"
- content_name_ko: "가공석과 가공복"
- content_category: "life"
- note: "가공석·가공복"
- order_no: 3
- relative_path: "../contents/processing-stones-and-clothes.md"
### `mass-processing.system`

- seed_key: "mass-processing.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "mass-processing"
- content_name_ko: "대량가공"
- content_category: "life"
- note: "가공 시스템의 대량 처리"
- order_no: 1
- relative_path: "../contents/mass-processing.md"
### `processing-onboarding-strategy.current-system`

- seed_key: "processing-onboarding-strategy.current-system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "processing-onboarding-strategy"
- content_name_ko: "가공 입문 전략"
- content_category: "life"
- note: null
- order_no: 1
- relative_path: "../contents/processing-onboarding-strategy.md"
### `production-node-current-system.processing`

- seed_key: "production-node-current-system.processing"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "production-node-current-system"
- content_name_ko: "생산 거점 현재 시스템"
- content_category: "life"
- note: "생산 거점 재료는 가공 콘텐츠로 이어진다."
- order_no: 2
- relative_path: "../contents/production-node-current-system.md"

## Evidence and Sources

### Current evidence

### `processing-current-system.summary::processing-guide`

- evidence_seed_key: "processing-current-system.summary::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "processing-current-system"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "가공 방식과 기본 성공률"
- active: true
- is_active: true

### `processing-current-system.requirement.base-success::processing-guide`

- evidence_seed_key: "processing-current-system.requirement.base-success::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "processing-current-system.base-success"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "기본 성공률 70%"
- active: true
- is_active: true

### `processing-current-system.requirement.level-effects::processing-guide`

- evidence_seed_key: "processing-current-system.requirement.level-effects::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "processing-current-system.level-effects"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "가공 레벨 효과"
- active: true
- is_active: true

### `processing-current-system.requirement.methods::processing-guide`

- evidence_seed_key: "processing-current-system.requirement.methods::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "processing-current-system.methods"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "가공 방식"
- active: true
- is_active: true

### `processing-current-system.requirement.simple-progression::processing-guide`

- evidence_seed_key: "processing-current-system.requirement.simple-progression::processing-guide"
- source_id: "processing-guide"
- title: "가공"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "processing-current-system.simple-progression"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "간이 연금·요리 성장 분리"
- active: true
- is_active: true

### Historical / inactive evidence

- None
