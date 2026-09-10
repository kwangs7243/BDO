<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 왕실 공방 일꾼 효과

## Identity

- slug: "royal-workshop-worker-effects"
- name_ko: "왕실 공방 일꾼 효과"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "왕실 공방 생산소와 가공소에는 일부 일꾼 특성·기술만 적용되며 일반 생산거점 규칙을 그대로 복제하지 않는다."
- purpose: "왕실 공방에 적용되는 생산량·행운·재료 반환 효과와 적용되지 않는 이동 속도·조건부 기술을 명시한다."

## Requirements

### `royal-workshop-worker-effects.common-skills`

- seed_key: "royal-workshop-worker-effects.common-skills"
- kind: "other"
- requirement_level: "required"
- title: "공통 능력치 기술"
- description: "작업반장, 단순하게, 럭키가이 등 능력치를 올리는 일꾼 기술은 왕실 공방에 적용된다."
- structured_value:

```json
{
  "applies": true,
  "examples": [
    "작업반장",
    "단순하게",
    "럭키가이"
  ]
}
```

### `royal-workshop-worker-effects.production-turtle`

- seed_key: "royal-workshop-worker-effects.production-turtle"
- kind: "other"
- requirement_level: "required"
- title: "생산소 거북이 일꾼"
- description: "거북이 일꾼의 기본 수확량 +68.4% 효과는 왕실 공방 생산소에 적용된다."
- structured_value:

```json
{
  "applies": true,
  "base_yield_bonus_percent": 68.4,
  "branch": "production",
  "worker_family": "turtle"
}
```

### `royal-workshop-worker-effects.production-luck`

- seed_key: "royal-workshop-worker-effects.production-luck"
- kind: "other"
- requirement_level: "required"
- title: "생산소 행운 보따리"
- description: "일꾼 행운 수치에 따라 농부·광부·어부 보따리류를 추가 획득할 수 있다."
- structured_value:

```json
{
  "branch": "production",
  "exact_probability": null,
  "extra_item_examples": [
    "농부 보따리류",
    "광부 보따리류",
    "어부 보따리류"
  ],
  "luck_affects_extra_acquisition": true
}
```

### `royal-workshop-worker-effects.processing-frugal`

- seed_key: "royal-workshop-worker-effects.processing-frugal"
- kind: "other"
- requirement_level: "required"
- title: "가공소 알뜰살뜰"
- description: "알뜰살뜰 A/B/C는 제작 시 지정 확률로 재료 한 종류의 10%를 반환한다."
- structured_value:

```json
{
  "branch": "processing",
  "exact_probability": null,
  "return_percent": 10,
  "returned_material_types": 1,
  "skills": [
    "알뜰살뜰 A",
    "알뜰살뜰 B",
    "알뜰살뜰 C"
  ]
}
```

### `royal-workshop-worker-effects.movement-speed`

- seed_key: "royal-workshop-worker-effects.movement-speed"
- kind: "other"
- requirement_level: "required"
- title: "일꾼 이동 속도"
- description: "일꾼 이동 속도는 왕실 공방 작업 시간에 영향을 주지 않는다."
- structured_value:

```json
{
  "affects_royal_workshop_time": false
}
```

### `royal-workshop-worker-effects.excluded-conditional-skills`

- seed_key: "royal-workshop-worker-effects.excluded-conditional-skills"
- kind: "other"
- requirement_level: "required"
- title: "미적용 조건부 기술"
- description: "일반 지식, 공방 지식, 숙련 광석 포장 기술 등 일부 조건부 작업 속도·추가 작업 기술은 적용되지 않는다."
- structured_value:

```json
{
  "applies": false,
  "examples": [
    "일반 지식",
    "공방 지식",
    "숙련 광석 포장 기술"
  ],
  "not_exhaustive": true
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

### `royal-workshop-worker-effects.system`

- seed_key: "royal-workshop-worker-effects.system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "royal-workshop-current-system"
- content_name_ko: "왕실 공방 현재 시스템"
- content_category: "life"
- note: "왕실 공방 전용 일꾼 적용 규칙이다."
- order_no: 1
- relative_path: "../contents/royal-workshop-current-system.md"
### `royal-workshop-worker-effects.general-worker-rules`

- seed_key: "royal-workshop-worker-effects.general-worker-rules"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "worker-skills-luck"
- content_name_ko: "일꾼 기술과 행운"
- content_category: "life"
- note: "일반 일꾼 행운·기술 규칙과 연결하되 왕실 공방 적용 범위는 별도로 유지한다."
- order_no: 2
- relative_path: "../contents/worker-skills-luck.md"
### `royal-workshop-current-system.worker-effects`

- seed_key: "royal-workshop-current-system.worker-effects"
- direction: "incoming"
- relation_type: "related"
- content_slug: "royal-workshop-current-system"
- content_name_ko: "왕실 공방 현재 시스템"
- content_category: "life"
- note: "왕실 공방에 적용되는 일꾼 특성과 기술은 별도 콘텐츠에서 정의한다."
- order_no: 3
- relative_path: "../contents/royal-workshop-current-system.md"

## Evidence and Sources

### Current evidence

### `royal-workshop-worker-effects.claim.current::royal-workshop-2024-11-20`

- evidence_seed_key: "royal-workshop-worker-effects.claim.current::royal-workshop-2024-11-20"
- source_id: "royal-workshop-2024-11-20"
- title: "11월 20일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13142"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-11-20"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "royal-workshop-worker-effects"
- claim_key: "requirements:royal-workshop-worker-effects"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
