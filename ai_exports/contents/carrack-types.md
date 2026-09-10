<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 에페리아 중범선 네 종류

## Identity

- slug: "carrack-types"
- name_ko: "에페리아 중범선 네 종류"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "점진·균형·비상·용맹의 기반 선박과 공식 역할."
- purpose: "플레이 목적에 맞는 중범선 분기를 객관적 특성으로 비교한다."

## Requirements

### `carrack-types.advance`

- seed_key: "carrack-types.advance"
- kind: "other"
- requirement_level: "required"
- title: "점진"
- description: "점진: 에페리아 무역선에서 증축하며 최대 적재량 특화, 물물교환 중심."
- structured_value:

```json
{
  "base_ship": "에페리아 무역선",
  "official_roles": [
    "최대 적재량 특화",
    "물물교환 중심"
  ]
}
```

### `carrack-types.balance`

- seed_key: "carrack-types.balance"
- kind: "other"
- requirement_level: "required"
- title: "균형"
- description: "균형: 에페리아 무역선에서 증축하며 균형형."
- structured_value:

```json
{
  "base_ship": "에페리아 무역선",
  "official_roles": [
    "균형형"
  ]
}
```

### `carrack-types.volante`

- seed_key: "carrack-types.volante"
- kind: "other"
- requirement_level: "required"
- title: "비상"
- description: "비상: 에페리아 구축함에서 증축하며 속도 특화, 기동 특화."
- structured_value:

```json
{
  "base_ship": "에페리아 구축함",
  "official_roles": [
    "속도 특화",
    "기동 특화"
  ]
}
```

### `carrack-types.valor`

- seed_key: "carrack-types.valor"
- kind: "other"
- requirement_level: "required"
- title: "용맹"
- description: "용맹: 에페리아 구축함에서 증축하며 전투 특화, 공격 특화."
- structured_value:

```json
{
  "base_ship": "에페리아 구축함",
  "official_roles": [
    "전투 특화",
    "공격 특화"
  ]
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

### `carrack-types.relation.advance-project`

- seed_key: "carrack-types.relation.advance-project"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "carrack-advance"
- content_name_ko: "에페리아 중범선 : 점진"
- content_category: "ocean_project"
- note: "기존 점진 프로젝트 상세"
- order_no: 1
- relative_path: "../contents/carrack-advance.md"
### `carrack-types.relation.materials`

- seed_key: "carrack-types.relation.materials"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "carrack-upgrade-materials"
- content_name_ko: "중범선 분기별 증축 핵심 재료"
- content_category: "ocean_project"
- note: "분기별 증축 핵심 재료"
- order_no: 2
- relative_path: "../contents/carrack-upgrade-materials.md"
### `carrack-types.relation.chiro`

- seed_key: "carrack-types.relation.chiro"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "carrack-chiro-gear"
- content_name_ko: "중범선 치로 장비"
- content_category: "ocean_project"
- note: "중범선 장비 성장"
- order_no: 3
- relative_path: "../contents/carrack-chiro-gear.md"
### `carrack-advance.relation.types`

- seed_key: "carrack-advance.relation.types"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "carrack-advance"
- content_name_ko: "에페리아 중범선 : 점진"
- content_category: "ocean_project"
- note: "점진은 중범선 네 분기 중 무역선 기반 적재 특화 분기"
- order_no: 1
- relative_path: "../contents/carrack-advance.md"
### `carrack-chiro-gear.relation.types`

- seed_key: "carrack-chiro-gear.relation.types"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "carrack-chiro-gear"
- content_name_ko: "중범선 치로 장비"
- content_category: "ocean_project"
- note: "중범선 네 종류의 파란 장비"
- order_no: 1
- relative_path: "../contents/carrack-chiro-gear.md"
### `carrack-upgrade-materials.relation.types`

- seed_key: "carrack-upgrade-materials.relation.types"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "carrack-upgrade-materials"
- content_name_ko: "중범선 분기별 증축 핵심 재료"
- content_category: "ocean_project"
- note: "중범선 네 분기의 증축 요구량"
- order_no: 1
- relative_path: "../contents/carrack-upgrade-materials.md"
### `sailing-onboarding-strategy.carrack-types`

- seed_key: "sailing-onboarding-strategy.carrack-types"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "sailing-onboarding-strategy"
- content_name_ko: "항해 입문 운영 전략"
- content_category: "ocean_guide"
- note: "목적별 중범선 분기 FACT"
- order_no: 1
- relative_path: "../contents/sailing-onboarding-strategy.md"
### `carrack-sailor-fishing.relation.carracks`

- seed_key: "carrack-sailor-fishing.relation.carracks"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "carrack-sailor-fishing"
- content_name_ko: "중범선 선원 낚시"
- content_category: "ocean_guide"
- note: "에페리아 중범선 전용 기능"
- order_no: 3
- relative_path: "../contents/carrack-sailor-fishing.md"
### `ebenruth-nol.relation.carracks`

- seed_key: "ebenruth-nol.relation.carracks"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "ebenruth-nol"
- content_name_ko: "에벤루스의 놀"
- content_category: "ocean_guide"
- note: "에페리아 중범선 장착 보물"
- order_no: 3
- relative_path: "../contents/ebenruth-nol.md"
### `carrack-palasi-gear.relation.types`

- seed_key: "carrack-palasi-gear.relation.types"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "carrack-palasi-gear"
- content_name_ko: "중범선 팔라시 장비"
- content_category: "ocean_project"
- note: "중범선 네 종류별 전용 장비"
- order_no: 4
- relative_path: "../contents/carrack-palasi-gear.md"

## Evidence and Sources

### Current evidence

### `carrack-types.evidence.advance::carrack-guide`

- evidence_seed_key: "carrack-types.evidence.advance::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-types.advance"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진: 에페리아 무역선에서 증축하며 최대 적재량 특화, 물물교환 중심."
- active: true
- is_active: true

### `carrack-types.evidence.balance::carrack-guide`

- evidence_seed_key: "carrack-types.evidence.balance::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-types.balance"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "균형: 에페리아 무역선에서 증축하며 균형형."
- active: true
- is_active: true

### `carrack-types.evidence.valor::carrack-guide`

- evidence_seed_key: "carrack-types.evidence.valor::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-types.valor"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "용맹: 에페리아 구축함에서 증축하며 전투 특화, 공격 특화."
- active: true
- is_active: true

### `carrack-types.evidence.volante::carrack-guide`

- evidence_seed_key: "carrack-types.evidence.volante::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-types.volante"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "비상: 에페리아 구축함에서 증축하며 속도 특화, 기동 특화."
- active: true
- is_active: true

### Historical / inactive evidence

- None
