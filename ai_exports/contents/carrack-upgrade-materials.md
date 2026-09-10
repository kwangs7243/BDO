<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 중범선 분기별 증축 핵심 재료

## Identity

- slug: "carrack-upgrade-materials"
- name_ko: "중범선 분기별 증축 핵심 재료"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "점진·균형·비상·용맹의 공식 증축 핵심 재료 요구량과 +10 파란 장비 조건."
- purpose: "중범선 분기별 재료 차이를 구조화해 준비량을 계산한다."

## Requirements

### `carrack-upgrade-materials.balance`

- seed_key: "carrack-upgrade-materials.balance"
- kind: "item"
- requirement_level: "required"
- title: "균형 증축"
- description: "균형 증축 핵심 재료와 에페리아 무역선 전용 +10 파란 장비 4부위가 필요하다."
- structured_value:

```json
{
  "base_ship": "에페리아 무역선",
  "blue_gear": {
    "enhancement": 10,
    "parts": 4
  },
  "materials": {
    "달의 핏줄이 새겨진 아마포": 180,
    "심해의 눈물": 50,
    "짙은 파도빛이 감도는 규격 각목": 144,
    "화려한 암염 주괴": 30,
    "화려한 진주 결정": 30
  }
}
```

### `carrack-upgrade-materials.advance`

- seed_key: "carrack-upgrade-materials.advance"
- kind: "item"
- requirement_level: "required"
- title: "점진 증축"
- description: "점진 증축 핵심 재료와 에페리아 무역선 전용 +10 파란 장비 4부위가 필요하다."
- structured_value:

```json
{
  "base_ship": "에페리아 무역선",
  "blue_gear": {
    "enhancement": 10,
    "parts": 4
  },
  "materials": {
    "달의 핏줄이 새겨진 아마포": 180,
    "심해의 눈물": 42,
    "짙은 파도빛이 감도는 규격 각목": 144,
    "화려한 암염 주괴": 35,
    "화려한 진주 결정": 35
  }
}
```

### `carrack-upgrade-materials.volante`

- seed_key: "carrack-upgrade-materials.volante"
- kind: "item"
- requirement_level: "required"
- title: "비상 증축"
- description: "비상 증축 핵심 재료와 에페리아 구축함 전용 +10 파란 장비 4부위가 필요하다."
- structured_value:

```json
{
  "base_ship": "에페리아 구축함",
  "blue_gear": {
    "enhancement": 10,
    "parts": 4
  },
  "materials": {
    "달의 핏줄이 새겨진 아마포": 210,
    "심해의 눈물": 42,
    "짙은 파도빛이 감도는 규격 각목": 144,
    "화려한 암염 주괴": 30,
    "화려한 진주 결정": 30
  }
}
```

### `carrack-upgrade-materials.valor`

- seed_key: "carrack-upgrade-materials.valor"
- kind: "item"
- requirement_level: "required"
- title: "용맹 증축"
- description: "용맹 증축 핵심 재료와 에페리아 구축함 전용 +10 파란 장비 4부위가 필요하다."
- structured_value:

```json
{
  "base_ship": "에페리아 구축함",
  "blue_gear": {
    "enhancement": 10,
    "parts": 4
  },
  "materials": {
    "달의 핏줄이 새겨진 아마포": 180,
    "심해의 눈물": 42,
    "짙은 파도빛이 감도는 규격 각목": 170,
    "화려한 암염 주괴": 30,
    "화려한 진주 결정": 30
  }
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

### `carrack-upgrade-materials.relation.types`

- seed_key: "carrack-upgrade-materials.relation.types"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "carrack-types"
- content_name_ko: "에페리아 중범선 네 종류"
- content_category: "ocean_project"
- note: "중범선 네 분기의 증축 요구량"
- order_no: 1
- relative_path: "../contents/carrack-types.md"
### `carrack-upgrade-materials.relation.crow-shop`

- seed_key: "carrack-upgrade-materials.relation.crow-shop"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "crow-coin-material-shop"
- content_name_ko: "까마귀 주화 증축 재료 상점"
- content_category: "ocean_project"
- note: "일부 재료의 까마귀 주화 구매 가격"
- order_no: 2
- relative_path: "../contents/crow-coin-material-shop.md"
### `carrack-upgrade-materials.relation.advance`

- seed_key: "carrack-upgrade-materials.relation.advance"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "carrack-advance"
- content_name_ko: "에페리아 중범선 : 점진"
- content_category: "ocean_project"
- note: "기존 점진 상세 프로젝트"
- order_no: 3
- relative_path: "../contents/carrack-advance.md"
### `crow-coin-material-shop.relation.carrack-materials`

- seed_key: "crow-coin-material-shop.relation.carrack-materials"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "crow-coin-material-shop"
- content_name_ko: "까마귀 주화 증축 재료 상점"
- content_category: "ocean_project"
- note: "중범선 증축 재료의 주화 구매 가격"
- order_no: 1
- relative_path: "../contents/crow-coin-material-shop.md"
### `carrack-advance.relation.materials`

- seed_key: "carrack-advance.relation.materials"
- direction: "incoming"
- relation_type: "related"
- content_slug: "carrack-advance"
- content_name_ko: "에페리아 중범선 : 점진"
- content_category: "ocean_project"
- note: "점진 증축 핵심 재료의 공통 비교표"
- order_no: 2
- relative_path: "../contents/carrack-advance.md"
### `carrack-types.relation.materials`

- seed_key: "carrack-types.relation.materials"
- direction: "incoming"
- relation_type: "related"
- content_slug: "carrack-types"
- content_name_ko: "에페리아 중범선 네 종류"
- content_category: "ocean_project"
- note: "분기별 증축 핵심 재료"
- order_no: 2
- relative_path: "../contents/carrack-types.md"
### `sailing-onboarding-strategy.upgrade-materials`

- seed_key: "sailing-onboarding-strategy.upgrade-materials"
- direction: "incoming"
- relation_type: "related"
- content_slug: "sailing-onboarding-strategy"
- content_name_ko: "항해 입문 운영 전략"
- content_category: "ocean_guide"
- note: "중범선 증축 재료"
- order_no: 6
- relative_path: "../contents/sailing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `carrack-upgrade-materials.evidence.advance::carrack-guide`

- evidence_seed_key: "carrack-upgrade-materials.evidence.advance::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-upgrade-materials.advance"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진 증축 핵심 재료와 에페리아 무역선 전용 +10 파란 장비 4부위가 필요하다."
- active: true
- is_active: true

### `carrack-upgrade-materials.evidence.balance::carrack-guide`

- evidence_seed_key: "carrack-upgrade-materials.evidence.balance::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-upgrade-materials.balance"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "균형 증축 핵심 재료와 에페리아 무역선 전용 +10 파란 장비 4부위가 필요하다."
- active: true
- is_active: true

### `carrack-upgrade-materials.evidence.valor::carrack-guide`

- evidence_seed_key: "carrack-upgrade-materials.evidence.valor::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-upgrade-materials.valor"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "용맹 증축 핵심 재료와 에페리아 구축함 전용 +10 파란 장비 4부위가 필요하다."
- active: true
- is_active: true

### `carrack-upgrade-materials.evidence.volante::carrack-guide`

- evidence_seed_key: "carrack-upgrade-materials.evidence.volante::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-upgrade-materials.volante"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "비상 증축 핵심 재료와 에페리아 구축함 전용 +10 파란 장비 4부위가 필요하다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
