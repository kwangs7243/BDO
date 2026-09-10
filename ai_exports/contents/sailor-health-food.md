<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 선원 건강과 식량

## Identity

- slug: "sailor-health-food"
- name_ko: "선원 건강과 식량"
- category: "ocean_guide"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "선원 식량이 0이면 선박이 느려지고 기술을 쓰지 못하며 건강 악화와 질병 위험이 생긴다."
- purpose: "선원의 정상·질병 상태에 맞는 회복 아이템과 비상 식량 수치를 확인한다."

## Requirements

### `sailor-health-food.zero-food`

- seed_key: "sailor-health-food.zero-food"
- kind: "other"
- requirement_level: "required"
- title: "식량 0 상태"
- description: "선박 식량이 0이면 속도가 느려지고 항해 기술을 사용할 수 없으며 선원 건강이 악화되어 병에 걸릴 수 있다."
- structured_value:

```json
{
  "health_degrades": true,
  "illness_possible": true,
  "sailing_skills_disabled": true,
  "ship_slows": true
}
```

### `sailor-health-food.healthy-food`

- seed_key: "sailor-health-food.healthy-food"
- kind: "other"
- requirement_level: "required"
- title: "건강한 선원 회복"
- description: "건강한 선원은 차우더 또는 건포도 빵으로 건강을 회복한다."
- structured_value:

```json
{
  "chowder_recipe": {
    "돼지고기": 2,
    "말린 진주 조갯살": 1,
    "우유": 1,
    "테프빵": 1,
    "후추": 2
  },
  "items": [
    "차우더",
    "건포도 빵"
  ]
}
```

### `sailor-health-food.illness-cure`

- seed_key: "sailor-health-food.illness-cure"
- kind: "other"
- requirement_level: "required"
- title: "질병 치료"
- description: "병든 선원은 재생의 묘약으로 치료할 수 있다."
- structured_value:

```json
{
  "item": "재생의 묘약",
  "process": "간이연금",
  "recipe": {
    "마력의 정수": 1,
    "만드라고라의 정수": 1,
    "재생의 오일": 1,
    "트롤 피": 2,
    "포도": 4
  }
}
```

### `sailor-health-food.emergency-food`

- seed_key: "sailor-health-food.emergency-food"
- kind: "other"
- requirement_level: "required"
- title: "비상 식량 환산"
- description: "선원 식량으로 허용되는 등급별 음식의 비상 회복량이다. 일꾼 행동력 음식과 거래 불가 음식은 대상에서 제외한다."
- structured_value:

```json
{
  "blue": 240,
  "excluded": [
    "일꾼 행동력 회복 음식",
    "거래 불가 음식"
  ],
  "green": 100,
  "orange": 22000,
  "white": 80,
  "yellow": 4000
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

### `sailor-health-food.relation.hiring`

- seed_key: "sailor-health-food.relation.hiring"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sailor-hiring-growth"
- content_name_ko: "선원 고용과 성장"
- content_category: "ocean_guide"
- note: "고용한 선원의 유지 관리"
- order_no: 1
- relative_path: "../contents/sailor-hiring-growth.md"
### `sailor-health-food.relation.fishing`

- seed_key: "sailor-health-food.relation.fishing"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "carrack-sailor-fishing"
- content_name_ko: "중범선 선원 낚시"
- content_category: "ocean_guide"
- note: "낚시 선원이 병들면 선원 낚시가 일시정지된다."
- order_no: 2
- relative_path: "../contents/carrack-sailor-fishing.md"
### `carrack-sailor-fishing.relation.health`

- seed_key: "carrack-sailor-fishing.relation.health"
- direction: "incoming"
- relation_type: "related"
- content_slug: "carrack-sailor-fishing"
- content_name_ko: "중범선 선원 낚시"
- content_category: "ocean_guide"
- note: "선원 질병 시 낚시 일시정지"
- order_no: 2
- relative_path: "../contents/carrack-sailor-fishing.md"
### `sailor-hiring-growth.relation.health`

- seed_key: "sailor-hiring-growth.relation.health"
- direction: "incoming"
- relation_type: "related"
- content_slug: "sailor-hiring-growth"
- content_name_ko: "선원 고용과 성장"
- content_category: "ocean_guide"
- note: "선원 건강과 식량 관리가 필요하다."
- order_no: 2
- relative_path: "../contents/sailor-hiring-growth.md"
### `sailing-onboarding-strategy.sailor-health`

- seed_key: "sailing-onboarding-strategy.sailor-health"
- direction: "incoming"
- relation_type: "related"
- content_slug: "sailing-onboarding-strategy"
- content_name_ko: "항해 입문 운영 전략"
- content_category: "ocean_guide"
- note: "선원 건강과 식량"
- order_no: 4
- relative_path: "../contents/sailing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `sailor-health-food.evidence.emergency-food::ocean-all-guide`

- evidence_seed_key: "sailor-health-food.evidence.emergency-food::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailor-health-food.emergency-food"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "음식 등급별 비상 식량과 제외 대상"
- active: true
- is_active: true

### `sailor-health-food.evidence.healthy-food::ocean-all-guide`

- evidence_seed_key: "sailor-health-food.evidence.healthy-food::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailor-health-food.healthy-food"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "건강 회복 음식과 차우더 조리식"
- active: true
- is_active: true

### `sailor-health-food.evidence.illness-cure::ocean-all-guide`

- evidence_seed_key: "sailor-health-food.evidence.illness-cure::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailor-health-food.illness-cure"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "재생의 묘약 간이연금식"
- active: true
- is_active: true

### `sailor-health-food.evidence.zero-food::ocean-all-guide`

- evidence_seed_key: "sailor-health-food.evidence.zero-food::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailor-health-food.zero-food"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "식량 고갈 시 선박·선원 상태"
- active: true
- is_active: true

### Historical / inactive evidence

- None
