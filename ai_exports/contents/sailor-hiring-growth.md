<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 선원 고용과 성장

## Identity

- slug: "sailor-hiring-growth"
- name_ko: "선원 고용과 성장"
- category: "ocean_guide"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "선원은 선원 고용 증서로 고용하며 해양 괴수 처치와 물물교환으로 경험치를 얻는다."
- purpose: "선원 고용 비용·실패 규칙과 레벨별 성장 구조를 확인한다."

## Requirements

### `sailor-hiring-growth.hiring`

- seed_key: "sailor-hiring-growth.hiring"
- kind: "other"
- requirement_level: "required"
- title: "선원 고용"
- description: "선원 고용 증서는 300만 은화이며 고용 실패 시에도 증서가 소모된다."
- structured_value:

```json
{
  "capacity_rule": "선박 선실 한도와 선원의 선실 비용을 함께 확인",
  "contract_consumed_on_failure": true,
  "contract_silver": 3000000,
  "known_vendors": [
    "필라베르토 팔라시",
    "여관 주인 이슬린 바탈리",
    "프라와",
    "각 지역 선원 중개인·나루터지기"
  ]
}
```

### `sailor-hiring-growth.levels-1-10`

- seed_key: "sailor-hiring-growth.levels-1-10"
- kind: "other"
- requirement_level: "required"
- title: "레벨 1~10 성장"
- description: "해양 괴수 처치와 물물교환으로 경험치를 얻고, 최대 10레벨까지 성장할 때 능력치가 확률에 따라 증가한다."
- structured_value:

```json
{
  "cumulative_percent": {
    "1": 100,
    "10": 370,
    "2": 130,
    "3": 160,
    "4": 190,
    "5": 220,
    "6": 250,
    "7": 280,
    "8": 310,
    "9": 340
  },
  "experience_sources": [
    "해양 괴수 처치",
    "물물교환"
  ],
  "growth_is_probability_based": true,
  "max_level": 10,
  "per_level_required_percent": {
    "1": 100,
    "10": 37,
    "2": 65,
    "3": 53.3,
    "4": 47.5,
    "5": 44,
    "6": 41.7,
    "7": 40,
    "8": 38.8,
    "9": 37.8
  }
}
```

### `sailor-hiring-growth.levels-11-plus`

- seed_key: "sailor-hiring-growth.levels-11-plus"
- kind: "other"
- requirement_level: "required"
- title: "레벨 11 이상 경험치 풀"
- description: "11레벨 이상 구간의 총 필요 경험치 풀은 400%이며 레벨마다 균등 배분된다. 30레벨 기준 약 13.3%다."
- structured_value:

```json
{
  "distribution": "equal",
  "level_30_approx_percent": 13.3,
  "total_pool_percent": 400
}
```

## Steps

### `sailor-hiring-growth.step.buy-contract`

- seed_key: "sailor-hiring-growth.step.buy-contract"
- phase: "preparation"
- order_no: 1
- title: "고용 증서 준비"
- description: "고용 NPC에게서 선원 고용 증서를 준비한다."
- checkable: true

### `sailor-hiring-growth.step.gain-exp`

- seed_key: "sailor-hiring-growth.step.gain-exp"
- phase: "repeat"
- order_no: 2
- title: "선원 경험치 획득"
- description: "해양 괴수 처치 또는 물물교환으로 선원 경험치를 누적한다."
- checkable: false

## Schedules

- None

## Rewards

- None

## Sections

### `sailor-hiring-growth.random-growth`

- seed_key: "sailor-hiring-growth.random-growth"
- section_type: "common_mistakes"
- title: "성장 수치 주의"
- order_no: 1

#### body_markdown

선원 능력치는 성장 때 확률에 따라 증가하므로 개인별 최종 수치를 고정값으로 간주하지 않는다.

## Related Contents

### `sailor-hiring-growth.relation.roles`

- seed_key: "sailor-hiring-growth.relation.roles"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "sailor-role-slots"
- content_name_ko: "선원 역할 슬롯"
- content_category: "ocean_guide"
- note: "성장한 선원을 역할 슬롯에 배치한다."
- order_no: 1
- relative_path: "../contents/sailor-role-slots.md"
### `sailor-hiring-growth.relation.health`

- seed_key: "sailor-hiring-growth.relation.health"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sailor-health-food"
- content_name_ko: "선원 건강과 식량"
- content_category: "ocean_guide"
- note: "선원 건강과 식량 관리가 필요하다."
- order_no: 2
- relative_path: "../contents/sailor-health-food.md"
### `sailor-health-food.relation.hiring`

- seed_key: "sailor-health-food.relation.hiring"
- direction: "incoming"
- relation_type: "related"
- content_slug: "sailor-health-food"
- content_name_ko: "선원 건강과 식량"
- content_category: "ocean_guide"
- note: "고용한 선원의 유지 관리"
- order_no: 1
- relative_path: "../contents/sailor-health-food.md"
### `sailing-onboarding-strategy.sailor-growth`

- seed_key: "sailing-onboarding-strategy.sailor-growth"
- direction: "incoming"
- relation_type: "related"
- content_slug: "sailing-onboarding-strategy"
- content_name_ko: "항해 입문 운영 전략"
- content_category: "ocean_guide"
- note: "선원 고용과 성장"
- order_no: 2
- relative_path: "../contents/sailing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `sailor-hiring-growth.evidence.hiring::ocean-all-guide`

- evidence_seed_key: "sailor-hiring-growth.evidence.hiring::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailor-hiring-growth.hiring"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "고용 증서 가격, 실패 소모, 고용처와 선실 규칙"
- active: true
- is_active: true

### `sailor-hiring-growth.evidence.levels-1-10::ocean-all-guide`

- evidence_seed_key: "sailor-hiring-growth.evidence.levels-1-10::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailor-hiring-growth.levels-1-10"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "레벨 1~10 경험치 표와 확률 성장"
- active: true
- is_active: true

### `sailor-hiring-growth.evidence.levels-11-plus::ocean-all-guide`

- evidence_seed_key: "sailor-hiring-growth.evidence.levels-11-plus::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailor-hiring-growth.levels-11-plus"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "11레벨 이상 400% 균등 경험치 풀"
- active: true
- is_active: true

### Historical / inactive evidence

- None
