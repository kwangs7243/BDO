<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 중범선 팔라시 장비

## Identity

- slug: "carrack-palasi-gear"
- name_ko: "중범선 팔라시 장비"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "2026-08-26 추가된 중범선별 노란색 최상위 장비 16종과 한 부위 제작식."
- purpose: "중범선별 팔라시 장비 제작 재료와 획득 경로를 관리한다."

## Requirements

### `carrack-palasi-gear.recipe.cannon`

- seed_key: "carrack-palasi-gear.recipe.cannon"
- kind: "item"
- requirement_level: "required"
- title: "팔라시의 함포 한 부위 제작"
- description: "같은 중범선 종류에 맞는 팔라시의 함포 한 부위 제작식."
- structured_value:

```json
{
  "+10 치로의 함포": 1,
  "거센 파도가 새겨진 합판": 75,
  "견고한 산호 지지대": 125,
  "중범선 부품 개조 허가증": 1,
  "진홍빛 산호가 잠든 접착제": 50,
  "팔라시 설계도면": 10
}
```

### `carrack-palasi-gear.recipe.sail`

- seed_key: "carrack-palasi-gear.recipe.sail"
- kind: "item"
- requirement_level: "required"
- title: "팔라시의 돛 한 부위 제작"
- description: "같은 중범선 종류에 맞는 팔라시의 돛 한 부위 제작식."
- structured_value:

```json
{
  "+10 치로의 돛": 1,
  "거센 파도가 새겨진 합판": 75,
  "견고한 산호 지지대": 125,
  "중범선 부품 개조 허가증": 1,
  "진홍빛 산호가 잠든 접착제": 50,
  "팔라시 설계도면": 10
}
```

### `carrack-palasi-gear.recipe.figurehead`

- seed_key: "carrack-palasi-gear.recipe.figurehead"
- kind: "item"
- requirement_level: "required"
- title: "팔라시의 선수상 한 부위 제작"
- description: "같은 중범선 종류에 맞는 팔라시의 선수상 한 부위 제작식."
- structured_value:

```json
{
  "+10 치로의 선수상": 1,
  "거센 파도가 새겨진 합판": 75,
  "견고한 산호 지지대": 125,
  "중범선 부품 개조 허가증": 1,
  "진홍빛 산호가 잠든 접착제": 50,
  "팔라시 설계도면": 10
}
```

### `carrack-palasi-gear.recipe.armor`

- seed_key: "carrack-palasi-gear.recipe.armor"
- kind: "item"
- requirement_level: "required"
- title: "팔라시의 장갑 한 부위 제작"
- description: "같은 중범선 종류에 맞는 팔라시의 장갑 한 부위 제작식."
- structured_value:

```json
{
  "+10 치로의 흑장갑": 1,
  "거센 파도가 새겨진 합판": 75,
  "견고한 산호 지지대": 125,
  "중범선 부품 개조 허가증": 1,
  "진홍빛 산호가 잠든 접착제": 50,
  "팔라시 설계도면": 10
}
```

### `carrack-palasi-gear.permit`

- seed_key: "carrack-palasi-gear.permit"
- kind: "item"
- requirement_level: "required"
- title: "중범선 부품 개조 허가증"
- description: "필라베르토 팔라시에게 중범선 종류별 부품 개조 허가증을 50억 은화에 구매한다."
- structured_value:

```json
{
  "amount": 1,
  "npc": "필라베르토 팔라시",
  "price_silver": 5000000000
}
```

### `carrack-palasi-gear.blueprint`

- seed_key: "carrack-palasi-gear.blueprint"
- kind: "item"
- requirement_level: "required"
- title: "팔라시 설계도면 교환"
- description: "팔라시 부위별 설계도면 1장을 노을빛 산호의 정수 2개로 교환한다."
- structured_value:

```json
{
  "blueprint_amount": 1,
  "npc": "필라베르토 팔라시",
  "노을빛 산호의 정수": 2
}
```

### `carrack-palasi-gear.blueprint-derived`

- seed_key: "carrack-palasi-gear.blueprint-derived"
- kind: "item"
- requirement_level: "required"
- title: "한 부위 설계도면용 정수 합계"
- description: "설계도면 10장 × 장당 노을빛 산호의 정수 2개의 단순 계산으로 한 부위당 20개가 필요하다."
- structured_value:

```json
{
  "derived": true,
  "formula": "10 * 2",
  "노을빛 산호의 정수": 20
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `carrack-palasi-gear.variants`

- seed_key: "carrack-palasi-gear.variants"
- section_type: "overview"
- title: "중범선 전용 팔라시 장비 16종"
- order_no: 1

#### body_markdown

점진·균형·비상·용맹 각 중범선에 함포·돛·선수상·장갑 4부위가 있으며 선박 종류에 맞는 장비만 착용할 수 있다. 총 16종이다.

## Related Contents

### `carrack-palasi-gear.relation.chiro`

- seed_key: "carrack-palasi-gear.relation.chiro"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "carrack-chiro-gear"
- content_name_ko: "중범선 치로 장비"
- content_category: "ocean_project"
- note: "+10 치로의 동일 부위가 제작 재료"
- order_no: 1
- relative_path: "../contents/carrack-chiro-gear.md"
### `carrack-palasi-gear.relation.rinbach`

- seed_key: "carrack-palasi-gear.relation.rinbach"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "rinbach-colony"
- content_name_ko: "린바크 군락지"
- content_category: "ocean_combat"
- note: "린바크 계열 재료 3종이 제작 재료"
- order_no: 2
- relative_path: "../contents/rinbach-colony.md"
### `carrack-palasi-gear.relation.enhancement`

- seed_key: "carrack-palasi-gear.relation.enhancement"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "carrack-palasi-enhancement"
- content_name_ko: "팔라시 장비 강화"
- content_category: "ocean_project"
- note: "제작 후 노을진 파도의 블랙스톤으로 강화"
- order_no: 3
- relative_path: "../contents/carrack-palasi-enhancement.md"
### `carrack-palasi-gear.relation.types`

- seed_key: "carrack-palasi-gear.relation.types"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "carrack-types"
- content_name_ko: "에페리아 중범선 네 종류"
- content_category: "ocean_project"
- note: "중범선 네 종류별 전용 장비"
- order_no: 4
- relative_path: "../contents/carrack-types.md"
### `carrack-palasi-enhancement.relation.palasi`

- seed_key: "carrack-palasi-enhancement.relation.palasi"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "carrack-palasi-enhancement"
- content_name_ko: "팔라시 장비 강화"
- content_category: "ocean_project"
- note: "팔라시 장비의 강화 규칙"
- order_no: 1
- relative_path: "../contents/carrack-palasi-enhancement.md"
### `rinbach-colony.relation.palasi`

- seed_key: "rinbach-colony.relation.palasi"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "rinbach-colony"
- content_name_ko: "린바크 군락지"
- content_category: "ocean_combat"
- note: "팔라시 제작 재료 3종과 노을빛 산호의 정수"
- order_no: 1
- relative_path: "../contents/rinbach-colony.md"
### `carrack-chiro-gear.relation.palasi`

- seed_key: "carrack-chiro-gear.relation.palasi"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "carrack-chiro-gear"
- content_name_ko: "중범선 치로 장비"
- content_category: "ocean_project"
- note: "+10 치로 장비가 팔라시 제작의 선행 재료"
- order_no: 2
- relative_path: "../contents/carrack-chiro-gear.md"

## Evidence and Sources

### Current evidence

### `carrack-palasi-gear.evidence.blueprint::ocean-progression-2026-08-26`

- evidence_seed_key: "carrack-palasi-gear.evidence.blueprint::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-palasi-gear.blueprint"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "팔라시 부위별 설계도면 1장을 노을빛 산호의 정수 2개로 교환한다."
- active: true
- is_active: true

### `carrack-palasi-gear.evidence.blueprint-derived::ocean-progression-2026-08-26`

- evidence_seed_key: "carrack-palasi-gear.evidence.blueprint-derived::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-palasi-gear.blueprint-derived"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "설계도면 10장 × 장당 노을빛 산호의 정수 2개의 단순 계산으로 한 부위당 20개가 필요하다."
- active: true
- is_active: true

### `carrack-palasi-gear.evidence.permit::ocean-progression-2026-08-26`

- evidence_seed_key: "carrack-palasi-gear.evidence.permit::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-palasi-gear.permit"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "필라베르토 팔라시에게 중범선 종류별 부품 개조 허가증을 50억 은화에 구매한다."
- active: true
- is_active: true

### `carrack-palasi-gear.evidence.recipe-armor::ocean-progression-2026-08-26`

- evidence_seed_key: "carrack-palasi-gear.evidence.recipe-armor::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-palasi-gear.recipe.armor"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "같은 중범선 종류에 맞는 팔라시의 장갑 한 부위 제작식."
- active: true
- is_active: true

### `carrack-palasi-gear.evidence.recipe-cannon::ocean-progression-2026-08-26`

- evidence_seed_key: "carrack-palasi-gear.evidence.recipe-cannon::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-palasi-gear.recipe.cannon"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "같은 중범선 종류에 맞는 팔라시의 함포 한 부위 제작식."
- active: true
- is_active: true

### `carrack-palasi-gear.evidence.recipe-figurehead::ocean-progression-2026-08-26`

- evidence_seed_key: "carrack-palasi-gear.evidence.recipe-figurehead::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-palasi-gear.recipe.figurehead"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "같은 중범선 종류에 맞는 팔라시의 선수상 한 부위 제작식."
- active: true
- is_active: true

### `carrack-palasi-gear.evidence.recipe-sail::ocean-progression-2026-08-26`

- evidence_seed_key: "carrack-palasi-gear.evidence.recipe-sail::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-palasi-gear.recipe.sail"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "같은 중범선 종류에 맞는 팔라시의 돛 한 부위 제작식."
- active: true
- is_active: true

### `carrack-palasi-gear.evidence.variants::ocean-progression-2026-08-26`

- evidence_seed_key: "carrack-palasi-gear.evidence.variants::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "carrack-palasi-gear.variants"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진·균형·비상·용맹 각 중범선에 함포·돛·선수상·장갑 4부위가 있으며 선박 종류에 맞는 장비만 착용할 수 있다. 총 16종이다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
