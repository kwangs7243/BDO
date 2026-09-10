<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 채집 도구

## Identity

- slug: "gathering-tools"
- name_ko: "채집 도구"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "마력이 깃든 도구와 데미하르 도구는 비슷한 채집 속도·획득 효과를 가지지만 별도 장비이며, 마력 도구는 숙련도 기반 획득 확률 증가와 중첩되지 않는다."
- purpose: "대표 특수 채집 도구의 효과와 적용 예외를 구분한다."

## Requirements

### `gathering-tools.magic`

- seed_key: "gathering-tools.magic"
- kind: "gear"
- requirement_level: "required"
- title: "마력이 깃든 채집 도구"
- description: "채집 시간 11초 감소와 모든 채집물 획득 확률 80% 증가를 제공한다."
- structured_value:

```json
{
  "item_acquisition_chance_percent": 80,
  "mastery_acquisition_probability_applied": false,
  "mastery_entirely_disabled": false,
  "time_reduction_seconds": 11
}
```

### `gathering-tools.demihar`

- seed_key: "gathering-tools.demihar"
- kind: "gear"
- requirement_level: "required"
- title: "데미하르 채집 도구"
- description: "채집 견습 달성 도전과제 등으로 획득하며 수령 후 14일 동안 사용할 수 있는 기간제 도구다."
- structured_value:

```json
{
  "gathering_exp_percent": 50,
  "item_acquisition_chance_percent": 80,
  "representative_acquisition": "Gathering Apprentice challenge",
  "time_reduction_seconds": 11,
  "valid_days_after_receipt": 14
}
```

### `gathering-tools.distinct-items`

- seed_key: "gathering-tools.distinct-items"
- kind: "other"
- requirement_level: "required"
- title: "도구 구분"
- description: "마력이 깃든 채집 도구와 데미하르 채집 도구는 동일 아이템이 아니다."
- structured_value:

```json
{
  "magic_and_demihar_same_item": false
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

### `gathering-tools.system`

- seed_key: "gathering-tools.system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "gathering-current-system"
- content_name_ko: "채집 현재 시스템"
- content_category: "life"
- note: "채집 현재 시스템의 도구 예외"
- order_no: 1
- relative_path: "../contents/gathering-current-system.md"
### `gathering-onboarding-strategy.tools`

- seed_key: "gathering-onboarding-strategy.tools"
- direction: "incoming"
- relation_type: "related"
- content_slug: "gathering-onboarding-strategy"
- content_name_ko: "채집 입문 전략"
- content_category: "life"
- note: "채집 대상에 맞는 도구를 준비한다."
- order_no: 2
- relative_path: "../contents/gathering-onboarding-strategy.md"
### `gathering-current-system.tools`

- seed_key: "gathering-current-system.tools"
- direction: "incoming"
- relation_type: "related"
- content_slug: "gathering-current-system"
- content_name_ko: "채집 현재 시스템"
- content_category: "life"
- note: "채집 도구 예외"
- order_no: 3
- relative_path: "../contents/gathering-current-system.md"

## Evidence and Sources

### Current evidence

### `gathering-tools.summary::gathering-guide`

- evidence_seed_key: "gathering-tools.summary::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "gathering-tools"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "마력·데미하르 도구 구분"
- active: true
- is_active: true

### `gathering-tools.requirement.demihar::gathering-guide`

- evidence_seed_key: "gathering-tools.requirement.demihar::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-tools.demihar"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "데미하르 효과·획득·기간"
- active: true
- is_active: true

### `gathering-tools.requirement.distinct-items::gathering-guide`

- evidence_seed_key: "gathering-tools.requirement.distinct-items::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-tools.distinct-items"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "별도 장비"
- active: true
- is_active: true

### `gathering-tools.requirement.magic::gathering-guide`

- evidence_seed_key: "gathering-tools.requirement.magic::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-tools.magic"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "마력 도구 효과와 숙련도 획득 확률 미적용"
- active: true
- is_active: true

### Historical / inactive evidence

- None
