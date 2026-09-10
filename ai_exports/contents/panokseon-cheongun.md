<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 판옥선 청운 장비

## Identity

- slug: "panokseon-cheongun"
- name_ko: "판옥선 청운 장비"
- category: "ocean_guide"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "청운은 2026-08-26 추가된 판옥선 현행 최종 노란색 등급 장비다."
- purpose: "청운 부위별 제작식, 설계도 교환, 강화 연결과 +10 세트 능력치를 확인한다."

## Requirements

### `panokseon-cheongun.workshop`

- seed_key: "panokseon-cheongun.workshop"
- kind: "other"
- requirement_level: "required"
- title: "제작 공방"
- description: "청사 섬 1번지 청사 선박 부품 공방 2단계에서 제작한다."
- structured_value:

```json
{
  "effective_from": "2026-08-26",
  "level": 2,
  "workshop": "청사 섬 1번지 청사 선박 부품 공방"
}
```

### `panokseon-cheongun.recipe`

- seed_key: "panokseon-cheongun.recipe"
- kind: "other"
- requirement_level: "required"
- title: "부위별 제작식"
- description: "각 부위에 견고한 산호 지지대 125개, 거센 파도가 새겨진 합판 75개, 진홍빛 산호가 잠든 접착제 50개, 판옥선 부품 개조 허가증 1개, 동일 부위 +10 벽계 1개, 청운 설계도면 10개가 필요하다."
- structured_value:

```json
{
  "+10 동일 부위 벽계": 1,
  "거센 파도가 새겨진 합판": 75,
  "견고한 산호 지지대": 125,
  "설계도면 : 청운": 10,
  "진홍빛 산호가 잠든 접착제": 50,
  "판옥선 부품 개조 허가증": 1
}
```

### `panokseon-cheongun.permit-blueprint`

- seed_key: "panokseon-cheongun.permit-blueprint"
- kind: "other"
- requirement_level: "required"
- title: "허가증과 설계도"
- description: "판옥선 부품 개조 허가증은 강만에게 50억 은화로 구매한다. 청운 설계도 1개는 노을빛 산호의 정수 4개로 교환하며 팔라시 설계도의 2개와 구분한다."
- structured_value:

```json
{
  "blueprint_exchange": {
    "output": 1,
    "노을빛 산호의 정수": 4
  },
  "palasi_blueprint_exchange_for_comparison": {
    "output": 1,
    "노을빛 산호의 정수": 2
  },
  "permit_npc": "강만",
  "permit_silver": 5000000000
}
```

### `panokseon-cheongun.plus10-set`

- seed_key: "panokseon-cheongun.plus10-set"
- kind: "other"
- requirement_level: "required"
- title: "+10 4부위 세트 능력치"
- description: "청운 +10 4부위 세트의 합산 능력치다."
- structured_value:

```json
{
  "acceleration_percent": 17,
  "additional_damage": 72600,
  "braking_percent": 18,
  "damage_reduction_percent": 38.6,
  "defense": 190,
  "food": 300000,
  "gear_durability": 200,
  "ship_durability": 350000,
  "speed_percent": 25,
  "turning_percent": 18,
  "weight_lt": 7400
}
```

### `panokseon-cheongun.market`

- seed_key: "panokseon-cheongun.market"
- kind: "other"
- requirement_level: "required"
- title: "거래 제한"
- description: "판옥선의 모든 장비는 통합 거래소 등록과 거래가 불가능하다."
- structured_value:

```json
{
  "central_market_tradeable": false
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `panokseon-cheongun.enhancement-reference`

- seed_key: "panokseon-cheongun.enhancement-reference"
- section_type: "notes"
- title: "노란 장비 강화 규칙"
- order_no: 1

#### body_markdown

청운의 노란색 선박 장비 강화 규칙은 기존 `중범선 팔라시 장비` 콘텐츠를 참조한다. 동일 강화표를 이 콘텐츠에 복제하지 않는다.

## Related Contents

### `panokseon-cheongun.relation.byeokgye`

- seed_key: "panokseon-cheongun.relation.byeokgye"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "panokseon-haemo-byeokgye"
- content_name_ko: "판옥선 해모·벽계 장비"
- content_category: "ocean_guide"
- note: "동일 부위 +10 벽계 장비 필요"
- order_no: 1
- relative_path: "../contents/panokseon-haemo-byeokgye.md"
### `panokseon-cheongun.relation.palasi`

- seed_key: "panokseon-cheongun.relation.palasi"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "carrack-palasi-enhancement"
- content_name_ko: "팔라시 장비 강화"
- content_category: "ocean_project"
- note: "노란색 선박 장비 강화 규칙 공유"
- order_no: 2
- relative_path: "../contents/carrack-palasi-enhancement.md"
### `panokseon-cheongun.relation.rinbach`

- seed_key: "panokseon-cheongun.relation.rinbach"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "rinbach-colony"
- content_name_ko: "린바크 군락지"
- content_category: "ocean_combat"
- note: "청운 제작 재료 획득·가공 경로"
- order_no: 3
- relative_path: "../contents/rinbach-colony.md"
### `panokseon-haemo-byeokgye.relation.cheongun`

- seed_key: "panokseon-haemo-byeokgye.relation.cheongun"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "panokseon-haemo-byeokgye"
- content_name_ko: "판옥선 해모·벽계 장비"
- content_category: "ocean_guide"
- note: "벽계 +10은 청운 제작의 선행 장비"
- order_no: 2
- relative_path: "../contents/panokseon-haemo-byeokgye.md"
### `rinbach-colony.relation.panokseon-cheongun`

- seed_key: "rinbach-colony.relation.panokseon-cheongun"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "rinbach-colony"
- content_name_ko: "린바크 군락지"
- content_category: "ocean_combat"
- note: "청운 장비 제작 재료 경로"
- order_no: 4
- relative_path: "../contents/rinbach-colony.md"

## Evidence and Sources

### Current evidence

### `panokseon-cheongun.evidence.market::ocean-progression-2026-08-26`

- evidence_seed_key: "panokseon-cheongun.evidence.market::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon-cheongun.market"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "판옥선 장비 거래소 등록 불가"
- active: true
- is_active: true

### `panokseon-cheongun.evidence.market::panokseon-guide`

- evidence_seed_key: "panokseon-cheongun.evidence.market::panokseon-guide"
- source_id: "panokseon-guide"
- title: "판옥선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=374"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon-cheongun.market"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "판옥선 장비 거래소 등록 불가"
- active: true
- is_active: true

### `panokseon-cheongun.evidence.permit-blueprint::ocean-progression-2026-08-26`

- evidence_seed_key: "panokseon-cheongun.evidence.permit-blueprint::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon-cheongun.permit-blueprint"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "허가증 50억과 청운 설계도 교환비"
- active: true
- is_active: true

### `panokseon-cheongun.evidence.permit-blueprint::panokseon-guide`

- evidence_seed_key: "panokseon-cheongun.evidence.permit-blueprint::panokseon-guide"
- source_id: "panokseon-guide"
- title: "판옥선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=374"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon-cheongun.permit-blueprint"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "허가증 50억과 청운 설계도 교환비"
- active: true
- is_active: true

### `panokseon-cheongun.evidence.plus10-set::ocean-progression-2026-08-26`

- evidence_seed_key: "panokseon-cheongun.evidence.plus10-set::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon-cheongun.plus10-set"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "청운 +10 4부위 세트 능력치"
- active: true
- is_active: true

### `panokseon-cheongun.evidence.plus10-set::panokseon-guide`

- evidence_seed_key: "panokseon-cheongun.evidence.plus10-set::panokseon-guide"
- source_id: "panokseon-guide"
- title: "판옥선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=374"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon-cheongun.plus10-set"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "청운 +10 4부위 세트 능력치"
- active: true
- is_active: true

### `panokseon-cheongun.evidence.recipe::ocean-progression-2026-08-26`

- evidence_seed_key: "panokseon-cheongun.evidence.recipe::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon-cheongun.recipe"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "청운 부위별 제작식"
- active: true
- is_active: true

### `panokseon-cheongun.evidence.recipe::panokseon-guide`

- evidence_seed_key: "panokseon-cheongun.evidence.recipe::panokseon-guide"
- source_id: "panokseon-guide"
- title: "판옥선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=374"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon-cheongun.recipe"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "청운 부위별 제작식"
- active: true
- is_active: true

### `panokseon-cheongun.evidence.workshop::ocean-progression-2026-08-26`

- evidence_seed_key: "panokseon-cheongun.evidence.workshop::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon-cheongun.workshop"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "청사 섬 공방 2단계와 청운 추가일"
- active: true
- is_active: true

### `panokseon-cheongun.evidence.workshop::panokseon-guide`

- evidence_seed_key: "panokseon-cheongun.evidence.workshop::panokseon-guide"
- source_id: "panokseon-guide"
- title: "판옥선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=374"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon-cheongun.workshop"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "청사 섬 공방 2단계와 청운 추가일"
- active: true
- is_active: true

### Historical / inactive evidence

- None
