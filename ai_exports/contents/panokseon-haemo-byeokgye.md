<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 판옥선 해모·벽계 장비

## Identity

- slug: "panokseon-haemo-byeokgye"
- name_ko: "판옥선 해모·벽계 장비"
- category: "ocean_guide"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "판옥선 장비는 해모 초록 등급에서 벽계 파란 등급으로 이어지고 최종적으로 청운 노란 등급으로 진행한다."
- purpose: "해모 구매·강화와 벽계 부위별 제작 재료를 확인한다."

## Requirements

### `panokseon-haemo-byeokgye.progression`

- seed_key: "panokseon-haemo-byeokgye.progression"
- kind: "other"
- requirement_level: "required"
- title: "장비 진행 순서"
- description: "판옥선 장비 진행은 해모(초록) → 벽계(파랑) → 청운(노랑) 순서이며 현재 최종 장비는 청운이다."
- structured_value:

```json
[
  "해모",
  "벽계",
  "청운"
]
```

### `panokseon-haemo-byeokgye.haemo`

- seed_key: "panokseon-haemo-byeokgye.haemo"
- kind: "other"
- requirement_level: "required"
- title: "해모 장비"
- description: "함포·돛·선수상·장갑 각 부위를 까마귀 주화 10,000개로 구매한다. +1~+5는 시도당 파도의 블랙스톤 20개, +6~+10은 30개를 사용한다."
- structured_value:

```json
{
  "crow_coins_each": 10000,
  "enhancement_cost_per_attempt": {
    "1-5": 20,
    "6-10": 30
  },
  "material": "파도의 블랙스톤",
  "parts": [
    "함포",
    "돛",
    "선수상",
    "장갑"
  ]
}
```

### `panokseon-haemo-byeokgye.byeokgye`

- seed_key: "panokseon-haemo-byeokgye.byeokgye"
- kind: "other"
- requirement_level: "required"
- title: "벽계 장비 부위별 제작식"
- description: "각 부위에 벽계 설계도면 10개, 동일 부위 +10 해모 1개, 정교하게 다듬어진 소나무 합판 50개, 정교하게 다듬어진 지지대 50개, 파도의 흔적이 담긴 접착제 50개, 판옥선 부품 개조 허가증 1개가 필요하다."
- structured_value:

```json
{
  "+10 동일 부위 해모": 1,
  "설계도면 : 벽계의 판옥선 장비": 10,
  "정교하게 다듬어진 소나무 합판": 50,
  "정교하게 다듬어진 지지대": 50,
  "파도의 흔적이 담긴 접착제": 50,
  "판옥선 부품 개조 허가증": 1
}
```

### `panokseon-haemo-byeokgye.permit-workshops`

- seed_key: "panokseon-haemo-byeokgye.permit-workshops"
- kind: "other"
- requirement_level: "required"
- title: "벽계 허가증과 공방"
- description: "허가증은 남포 무들마을 철옹에게 10억 은화로 구매하며 남포 무들마을 2번지 또는 청사 섬 1번지 선박 부품 공방에서 제작한다."
- structured_value:

```json
{
  "permit_npc": "철옹",
  "permit_silver": 1000000000,
  "workshops": [
    "남포 무들마을 2번지 벽계 선박 부품 공방",
    "청사 섬 1번지 청사 선박 부품 공방"
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

### `panokseon-haemo-byeokgye.relation.panokseon`

- seed_key: "panokseon-haemo-byeokgye.relation.panokseon"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "panokseon"
- content_name_ko: "판옥선"
- content_category: "ocean_guide"
- note: "판옥선 전용 장비"
- order_no: 1
- relative_path: "../contents/panokseon.md"
### `panokseon-haemo-byeokgye.relation.cheongun`

- seed_key: "panokseon-haemo-byeokgye.relation.cheongun"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "panokseon-cheongun"
- content_name_ko: "판옥선 청운 장비"
- content_category: "ocean_guide"
- note: "벽계 +10은 청운 제작의 선행 장비"
- order_no: 2
- relative_path: "../contents/panokseon-cheongun.md"
### `panokseon-cheongun.relation.byeokgye`

- seed_key: "panokseon-cheongun.relation.byeokgye"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "panokseon-cheongun"
- content_name_ko: "판옥선 청운 장비"
- content_category: "ocean_guide"
- note: "동일 부위 +10 벽계 장비 필요"
- order_no: 1
- relative_path: "../contents/panokseon-cheongun.md"
### `panokseon.relation.green-blue-gear`

- seed_key: "panokseon.relation.green-blue-gear"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "panokseon"
- content_name_ko: "판옥선"
- content_category: "ocean_guide"
- note: "판옥선 해모·벽계 장비 진행"
- order_no: 2
- relative_path: "../contents/panokseon.md"

## Evidence and Sources

### Current evidence

### `panokseon-haemo-byeokgye.evidence.byeokgye::panokseon-guide`

- evidence_seed_key: "panokseon-haemo-byeokgye.evidence.byeokgye::panokseon-guide"
- source_id: "panokseon-guide"
- title: "판옥선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=374"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon-haemo-byeokgye.byeokgye"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "벽계 부위별 제작식"
- active: true
- is_active: true

### `panokseon-haemo-byeokgye.evidence.haemo::panokseon-guide`

- evidence_seed_key: "panokseon-haemo-byeokgye.evidence.haemo::panokseon-guide"
- source_id: "panokseon-guide"
- title: "판옥선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=374"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon-haemo-byeokgye.haemo"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "해모 구매가와 강화 재료 수량"
- active: true
- is_active: true

### `panokseon-haemo-byeokgye.evidence.permit-workshops::panokseon-guide`

- evidence_seed_key: "panokseon-haemo-byeokgye.evidence.permit-workshops::panokseon-guide"
- source_id: "panokseon-guide"
- title: "판옥선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=374"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon-haemo-byeokgye.permit-workshops"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "벽계 허가증 가격과 제작 공방"
- active: true
- is_active: true

### `panokseon-haemo-byeokgye.evidence.progression::ocean-progression-2026-08-26`

- evidence_seed_key: "panokseon-haemo-byeokgye.evidence.progression::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon-haemo-byeokgye.progression"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "해모·벽계·청운 장비 단계"
- active: true
- is_active: true

### `panokseon-haemo-byeokgye.evidence.progression::panokseon-guide`

- evidence_seed_key: "panokseon-haemo-byeokgye.evidence.progression::panokseon-guide"
- source_id: "panokseon-guide"
- title: "판옥선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=374"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon-haemo-byeokgye.progression"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "해모·벽계·청운 장비 단계"
- active: true
- is_active: true

### Historical / inactive evidence

- None
