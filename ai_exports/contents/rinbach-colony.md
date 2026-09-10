<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 린바크 군락지

## Identity

- slug: "rinbach-colony"
- name_ko: "린바크 군락지"
- category: "ocean_combat"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "팔라시 제작 재료와 항해 소비품 재료를 얻는 대양 사냥터 및 주간 의뢰."
- purpose: "린바크 전리품, 가공식, 2026-09-02 변경과 주간 보상을 현행 기준으로 관리한다."

## Requirements

### `rinbach-colony.processing.bone`

- seed_key: "rinbach-colony.processing.bone"
- kind: "item"
- requirement_level: "required"
- title: "견고한 산호 지지대 가공"
- description: "린바크의 뼈 1개, 별빛 강화제 1개, 별빛 유화제 1개를 공작해 견고한 산호 지지대 1개를 얻는다."
- structured_value:

```json
{
  "inputs": {
    "린바크의 뼈": 1,
    "별빛 강화제": 1,
    "별빛 유화제": 1
  },
  "mass_process": {
    "input_multiplier": 10,
    "output_multiplier": 10,
    "블랙스톤 가루": 1
  },
  "output": {
    "견고한 산호 지지대": 1
  },
  "process": "공작"
}
```

### `rinbach-colony.processing.scale`

- seed_key: "rinbach-colony.processing.scale"
- kind: "item"
- requirement_level: "required"
- title: "거센 파도가 새겨진 합판 가공"
- description: "린바크의 비늘 1개, 별빛 강화제 1개, 별빛 유화제 1개를 공작해 거센 파도가 새겨진 합판 1개를 얻는다."
- structured_value:

```json
{
  "inputs": {
    "린바크의 비늘": 1,
    "별빛 강화제": 1,
    "별빛 유화제": 1
  },
  "mass_process": {
    "input_multiplier": 10,
    "output_multiplier": 10,
    "블랙스톤 가루": 1
  },
  "output": {
    "거센 파도가 새겨진 합판": 1
  },
  "process": "공작"
}
```

### `rinbach-colony.processing.essence`

- seed_key: "rinbach-colony.processing.essence"
- kind: "item"
- requirement_level: "required"
- title: "진홍빛 산호가 잠든 접착제 가공"
- description: "린바크의 진액 1개, 별빛 강화제 1개, 별빛 유화제 1개를 간이연금해 진홍빛 산호가 잠든 접착제 1개를 얻는다."
- structured_value:

```json
{
  "inputs": {
    "린바크의 진액": 1,
    "별빛 강화제": 1,
    "별빛 유화제": 1
  },
  "mass_process": {
    "input_multiplier": 10,
    "output_multiplier": 10,
    "블랙스톤 가루": 1
  },
  "output": {
    "진홍빛 산호가 잠든 접착제": 1
  },
  "process": "간이연금"
}
```

## Steps

### `rinbach-colony.weekly-hunt`

- seed_key: "rinbach-colony.weekly-hunt"
- phase: "repeat"
- order_no: 1
- title: "[주간] 린바크의 영역 생태 조사"
- description: "청사 섬 나루터지기 강만에게 수주해 린바크 2마리를 처치한다."
- checkable: true

## Schedules

### `rinbach-colony.weekly-reset`

- seed_key: "rinbach-colony.weekly-reset"
- rule_type: "quest_reset"
- recurrence_type: "weekly"
- weekday: 3
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "일반 주간 의뢰 목요일 00:00 KST 재수주 기준"

## Rewards

### `rinbach-colony.horn-choice.support`

- seed_key: "rinbach-colony.horn-choice.support"
- name: "견고한 산호 지지대"
- reward_type: "exchange_choice"
- amount: 125.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "린바크의 뿔 교환"
- recommendation: null
- notes: "린바크의 뿔로 세 후보 중 하나를 선택 교환"
- order_no: 1

### `rinbach-colony.horn-choice.plywood`

- seed_key: "rinbach-colony.horn-choice.plywood"
- name: "거센 파도가 새겨진 합판"
- reward_type: "exchange_choice"
- amount: 75.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "린바크의 뿔 교환"
- recommendation: null
- notes: "린바크의 뿔로 세 후보 중 하나를 선택 교환"
- order_no: 2

### `rinbach-colony.horn-choice.adhesive`

- seed_key: "rinbach-colony.horn-choice.adhesive"
- name: "진홍빛 산호가 잠든 접착제"
- reward_type: "exchange_choice"
- amount: 50.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: true
- choice_group: "린바크의 뿔 교환"
- recommendation: null
- notes: "린바크의 뿔로 세 후보 중 하나를 선택 교환"
- order_no: 3

### `rinbach-colony.npc-sale.bone`

- seed_key: "rinbach-colony.npc-sale.bone"
- name: "린바크의 뼈"
- reward_type: "npc_sale_price"
- amount: 1600000.0
- min_amount: null
- max_amount: null
- unit: "은화"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "2026-09-02 이후 NPC 상점 판매가"
- order_no: 4

### `rinbach-colony.npc-sale.scale`

- seed_key: "rinbach-colony.npc-sale.scale"
- name: "린바크의 비늘"
- reward_type: "npc_sale_price"
- amount: 2400000.0
- min_amount: null
- max_amount: null
- unit: "은화"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "2026-09-02 이후 NPC 상점 판매가"
- order_no: 5

### `rinbach-colony.npc-sale.essence`

- seed_key: "rinbach-colony.npc-sale.essence"
- name: "린바크의 진액"
- reward_type: "npc_sale_price"
- amount: 4000000.0
- min_amount: null
- max_amount: null
- unit: "은화"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "2026-09-02 이후 NPC 상점 판매가"
- order_no: 6

### `rinbach-colony.weekly-reward.contribution`

- seed_key: "rinbach-colony.weekly-reward.contribution"
- name: "공헌도 경험치"
- reward_type: "weekly_reward"
- amount: 1000.0
- min_amount: null
- max_amount: null
- unit: "경험치"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "[주간] 린바크의 영역 생태 조사 기본 보상"
- order_no: 10

### `rinbach-colony.weekly-reward.sailing`

- seed_key: "rinbach-colony.weekly-reward.sailing"
- name: "항해 경험치"
- reward_type: "weekly_reward"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "[주간] 린바크의 영역 생태 조사 기본 보상"
- order_no: 11

### `rinbach-colony.weekly-reward.crow`

- seed_key: "rinbach-colony.weekly-reward.crow"
- name: "까마귀 주화"
- reward_type: "weekly_reward"
- amount: 500.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "[주간] 린바크의 영역 생태 조사 기본 보상"
- order_no: 12

### `rinbach-colony.weekly-reward.red-fish`

- seed_key: "rinbach-colony.weekly-reward.red-fish"
- name: "해양 괴수의 붉은빛 생선살"
- reward_type: "weekly_reward"
- amount: 6.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "[주간] 린바크의 영역 생태 조사 기본 보상"
- order_no: 13

### `rinbach-colony.weekly-reward.ocean-essence`

- seed_key: "rinbach-colony.weekly-reward.ocean-essence"
- name: "대양의 정수"
- reward_type: "weekly_reward"
- amount: 3.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "[주간] 린바크의 영역 생태 조사 기본 보상"
- order_no: 14

## Sections

### `rinbach-colony.loot`

- seed_key: "rinbach-colony.loot"
- section_type: "overview"
- title: "주요 전리품"
- order_no: 1

#### body_markdown

린바크의 뿔, 세르니 원석, 줄라티아 원석, 마고리아 원석, 파도의 손톱, 해양 괴수의 붉은빛 생선살, 산호 결정, 대왕 고래 오일, 해양 괴수의 기괴한 송곳니, 이끼에 뒤덮인 지도, 린바크의 뼈, 린바크의 비늘, 린바크의 진액, 노을빛 산호의 정수.

### `rinbach-colony.current-2026-09-02`

- seed_key: "rinbach-colony.current-2026-09-02"
- section_type: "common_mistakes"
- title: "2026-09-02 현행 변경"
- order_no: 2

#### body_markdown

린바크의 뿔 획득 확률은 기존 대비 2배가 되었고 더 이상 잡동사니가 아니다. 뿔에는 아그리스의 열기와 아이템 획득 수량 증가 효과가 적용되지 않는다. 아그리스 소모는 린바크 100→200, 린부르크 10→30으로 변경됐다.

## Related Contents

### `rinbach-colony.relation.palasi`

- seed_key: "rinbach-colony.relation.palasi"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "carrack-palasi-gear"
- content_name_ko: "중범선 팔라시 장비"
- content_category: "ocean_project"
- note: "팔라시 제작 재료 3종과 노을빛 산호의 정수"
- order_no: 1
- relative_path: "../contents/carrack-palasi-gear.md"
### `rinbach-colony.relation.enhancement`

- seed_key: "rinbach-colony.relation.enhancement"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "carrack-palasi-enhancement"
- content_name_ko: "팔라시 장비 강화"
- content_category: "ocean_project"
- note: "노을진 파도의 블랙스톤 재료인 노을빛 산호의 정수"
- order_no: 2
- relative_path: "../contents/carrack-palasi-enhancement.md"
### `rinbach-colony.relation.crystals`

- seed_key: "rinbach-colony.relation.crystals"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "sea-crystals"
- content_name_ko: "해원석 progression"
- content_category: "ocean_project"
- note: "세르니·줄라티아·마고리아 원석 획득처"
- order_no: 3
- relative_path: "../contents/sea-crystals.md"
### `rinbach-colony.relation.consumables`

- seed_key: "rinbach-colony.relation.consumables"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "ocean-consumables"
- content_name_ko: "현행 항해·교역 소비품"
- content_category: "ocean_guide"
- note: "오킬루아 파도 정식 재료인 붉은빛 생선살"
- order_no: 4
- relative_path: "../contents/ocean-consumables.md"
### `rinbach-colony.relation.panokseon-cheongun`

- seed_key: "rinbach-colony.relation.panokseon-cheongun"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "panokseon-cheongun"
- content_name_ko: "판옥선 청운 장비"
- content_category: "ocean_guide"
- note: "청운 장비 제작 재료 경로"
- order_no: 4
- relative_path: "../contents/panokseon-cheongun.md"
### `ocean-consumables.relation.rinbach`

- seed_key: "ocean-consumables.relation.rinbach"
- direction: "incoming"
- relation_type: "related"
- content_slug: "ocean-consumables"
- content_name_ko: "현행 항해·교역 소비품"
- content_category: "ocean_guide"
- note: "붉은빛 생선살과 대양의 정수 획득 경로"
- order_no: 1
- relative_path: "../contents/ocean-consumables.md"
### `sea-crystals.relation.rinbach`

- seed_key: "sea-crystals.relation.rinbach"
- direction: "incoming"
- relation_type: "related"
- content_slug: "sea-crystals"
- content_name_ko: "해원석 progression"
- content_category: "ocean_project"
- note: "세르니·줄라티아·마고리아 원석 획득처 중 하나"
- order_no: 1
- relative_path: "../contents/sea-crystals.md"
### `carrack-palasi-enhancement.relation.rinbach`

- seed_key: "carrack-palasi-enhancement.relation.rinbach"
- direction: "incoming"
- relation_type: "related"
- content_slug: "carrack-palasi-enhancement"
- content_name_ko: "팔라시 장비 강화"
- content_category: "ocean_project"
- note: "노을빛 산호의 정수 획득처"
- order_no: 2
- relative_path: "../contents/carrack-palasi-enhancement.md"
### `carrack-palasi-gear.relation.rinbach`

- seed_key: "carrack-palasi-gear.relation.rinbach"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "carrack-palasi-gear"
- content_name_ko: "중범선 팔라시 장비"
- content_category: "ocean_project"
- note: "린바크 계열 재료 3종이 제작 재료"
- order_no: 2
- relative_path: "../contents/carrack-palasi-gear.md"
### `hollow-maretta.relation.rinbach`

- seed_key: "hollow-maretta.relation.rinbach"
- direction: "incoming"
- relation_type: "related"
- content_slug: "hollow-maretta"
- content_name_ko: "공허한 마레타"
- content_category: "ocean_guide"
- note: "대양의 정수의 다른 획득 경로"
- order_no: 3
- relative_path: "../contents/hollow-maretta.md"
### `panokseon-cheongun.relation.rinbach`

- seed_key: "panokseon-cheongun.relation.rinbach"
- direction: "incoming"
- relation_type: "related"
- content_slug: "panokseon-cheongun"
- content_name_ko: "판옥선 청운 장비"
- content_category: "ocean_guide"
- note: "청운 제작 재료 획득·가공 경로"
- order_no: 3
- relative_path: "../contents/panokseon-cheongun.md"
### `sea-crocodile-hunting.relation.rinbach`

- seed_key: "sea-crocodile-hunting.relation.rinbach"
- direction: "incoming"
- relation_type: "alternative"
- content_slug: "sea-crocodile-hunting"
- content_name_ko: "바다 악어 사냥"
- content_category: "ocean_guide"
- note: "린바크 추가로 사냥터가 청사 섬 위쪽으로 이동"
- order_no: 3
- relative_path: "../contents/sea-crocodile-hunting.md"

## Evidence and Sources

### Current evidence

### `rinbach-colony.evidence.processing-bone::ocean-progression-2026-08-26`

- evidence_seed_key: "rinbach-colony.evidence.processing-bone::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "rinbach-colony.processing.bone"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "린바크의 뼈 1개, 별빛 강화제 1개, 별빛 유화제 1개를 공작해 견고한 산호 지지대 1개를 얻는다."
- active: true
- is_active: true

### `rinbach-colony.evidence.processing-essence::ocean-progression-2026-08-26`

- evidence_seed_key: "rinbach-colony.evidence.processing-essence::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "rinbach-colony.processing.essence"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "린바크의 진액 1개, 별빛 강화제 1개, 별빛 유화제 1개를 간이연금해 진홍빛 산호가 잠든 접착제 1개를 얻는다."
- active: true
- is_active: true

### `rinbach-colony.evidence.processing-scale::ocean-progression-2026-08-26`

- evidence_seed_key: "rinbach-colony.evidence.processing-scale::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "rinbach-colony.processing.scale"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "린바크의 비늘 1개, 별빛 강화제 1개, 별빛 유화제 1개를 공작해 거센 파도가 새겨진 합판 1개를 얻는다."
- active: true
- is_active: true

### `rinbach-colony.evidence.current-2026-09-02::life-unification-2026-09-02`

- evidence_seed_key: "rinbach-colony.evidence.current-2026-09-02::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "rinbach-colony.current-2026-09-02"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "린바크의 뿔 획득 확률은 기존 대비 2배가 되었고 더 이상 잡동사니가 아니다. 뿔에는 아그리스의 열기와 아이템 획득 수량 증가 효과가 적용되지 않는다. 아그리스 소모는 린바크 100→200, 린부르크 10→30으로 변경됐다."
- active: true
- is_active: true

### `rinbach-colony.evidence.loot::ocean-progression-2026-08-26`

- evidence_seed_key: "rinbach-colony.evidence.loot::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "rinbach-colony.loot"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "린바크의 뿔, 세르니 원석, 줄라티아 원석, 마고리아 원석, 파도의 손톱, 해양 괴수의 붉은빛 생선살, 산호 결정, 대왕 고래 오일, 해양 괴수의 기괴한 송곳니, 이끼에 뒤덮인 지도, 린바크의 뼈, 린바크의 비늘, 린바크의 진액, 노을빛 산호의 정수."
- active: true
- is_active: true

### `rinbach-colony.evidence.weekly-hunt::ocean-progression-2026-08-26`

- evidence_seed_key: "rinbach-colony.evidence.weekly-hunt::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "rinbach-colony.weekly-hunt"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "강만 수주, 린바크 2마리 처치"
- active: true
- is_active: true

### `rinbach-colony.evidence.horn-choice-adhesive::ocean-progression-2026-08-26`

- evidence_seed_key: "rinbach-colony.evidence.horn-choice-adhesive::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "rinbach-colony.horn-choice.adhesive"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "린바크의 뿔로 세 후보 중 하나를 선택 교환"
- active: true
- is_active: true

### `rinbach-colony.evidence.horn-choice-plywood::ocean-progression-2026-08-26`

- evidence_seed_key: "rinbach-colony.evidence.horn-choice-plywood::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "rinbach-colony.horn-choice.plywood"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "린바크의 뿔로 세 후보 중 하나를 선택 교환"
- active: true
- is_active: true

### `rinbach-colony.evidence.horn-choice-support::ocean-progression-2026-08-26`

- evidence_seed_key: "rinbach-colony.evidence.horn-choice-support::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "rinbach-colony.horn-choice.support"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "린바크의 뿔로 세 후보 중 하나를 선택 교환"
- active: true
- is_active: true

### `rinbach-colony.evidence.npc-sale-bone::life-unification-2026-09-02`

- evidence_seed_key: "rinbach-colony.evidence.npc-sale-bone::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "rinbach-colony.npc-sale.bone"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-09-02 이후 NPC 상점 판매가"
- active: true
- is_active: true

### `rinbach-colony.evidence.npc-sale-essence::life-unification-2026-09-02`

- evidence_seed_key: "rinbach-colony.evidence.npc-sale-essence::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "rinbach-colony.npc-sale.essence"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-09-02 이후 NPC 상점 판매가"
- active: true
- is_active: true

### `rinbach-colony.evidence.npc-sale-scale::life-unification-2026-09-02`

- evidence_seed_key: "rinbach-colony.evidence.npc-sale-scale::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "rinbach-colony.npc-sale.scale"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-09-02 이후 NPC 상점 판매가"
- active: true
- is_active: true

### `rinbach-colony.evidence.old-wave-exchange-bone-removed::life-unification-2026-09-02`

- evidence_seed_key: "rinbach-colony.evidence.old-wave-exchange-bone-removed::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "rinbach-colony.old-wave-exchange.bone"
- claim_key: "availability.current"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-09-02부터 까마귀 주화 교환원에게 이 교환을 할 수 없다."
- active: true
- is_active: true

### `rinbach-colony.evidence.old-wave-exchange-essence-removed::life-unification-2026-09-02`

- evidence_seed_key: "rinbach-colony.evidence.old-wave-exchange-essence-removed::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "rinbach-colony.old-wave-exchange.essence"
- claim_key: "availability.current"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-09-02부터 까마귀 주화 교환원에게 이 교환을 할 수 없다."
- active: true
- is_active: true

### `rinbach-colony.evidence.old-wave-exchange-scale-removed::life-unification-2026-09-02`

- evidence_seed_key: "rinbach-colony.evidence.old-wave-exchange-scale-removed::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "rinbach-colony.old-wave-exchange.scale"
- claim_key: "availability.current"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-09-02부터 까마귀 주화 교환원에게 이 교환을 할 수 없다."
- active: true
- is_active: true

### `rinbach-colony.evidence.weekly-reward-contribution::ocean-progression-2026-08-26`

- evidence_seed_key: "rinbach-colony.evidence.weekly-reward-contribution::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "rinbach-colony.weekly-reward.contribution"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "[주간] 린바크의 영역 생태 조사 기본 보상"
- active: true
- is_active: true

### `rinbach-colony.evidence.weekly-reward-crow::ocean-progression-2026-08-26`

- evidence_seed_key: "rinbach-colony.evidence.weekly-reward-crow::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "rinbach-colony.weekly-reward.crow"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "[주간] 린바크의 영역 생태 조사 기본 보상"
- active: true
- is_active: true

### `rinbach-colony.evidence.weekly-reward-ocean-essence::ocean-progression-2026-08-26`

- evidence_seed_key: "rinbach-colony.evidence.weekly-reward-ocean-essence::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "rinbach-colony.weekly-reward.ocean-essence"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "[주간] 린바크의 영역 생태 조사 기본 보상"
- active: true
- is_active: true

### `rinbach-colony.evidence.weekly-reward-red-fish::ocean-progression-2026-08-26`

- evidence_seed_key: "rinbach-colony.evidence.weekly-reward-red-fish::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "rinbach-colony.weekly-reward.red-fish"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "[주간] 린바크의 영역 생태 조사 기본 보상"
- active: true
- is_active: true

### `rinbach-colony.evidence.weekly-reward-sailing::ocean-progression-2026-08-26`

- evidence_seed_key: "rinbach-colony.evidence.weekly-reward-sailing::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "rinbach-colony.weekly-reward.sailing"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "[주간] 린바크의 영역 생태 조사 기본 보상"
- active: true
- is_active: true

### `rinbach-colony.evidence.weekly-reset::daily-weekly-reset-gm-2023`

- evidence_seed_key: "rinbach-colony.evidence.weekly-reset::daily-weekly-reset-gm-2023"
- source_id: "daily-weekly-reset-gm-2023"
- title: "검은사막이 처음인 모험가 여러분을 위해 준비한 A to Z!"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=10577"
- publisher: "Pearl Abyss"
- source_type: "official_gm"
- published_at: "2023-07-25"
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "rinbach-colony.weekly-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일반 주간 의뢰 목요일 00:00 KST 재수주"
- active: true
- is_active: true

### Historical / inactive evidence

### `rinbach-colony.evidence.old-wave-exchange-bone::ocean-progression-2026-08-26`

- evidence_seed_key: "rinbach-colony.evidence.old-wave-exchange-bone::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "rinbach-colony.old-wave-exchange.bone"
- claim_key: "reward"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-08-26 추가됐으나 2026-09-02 삭제된 과거 교환"
- active: false
- is_active: false

### `rinbach-colony.evidence.old-wave-exchange-essence::ocean-progression-2026-08-26`

- evidence_seed_key: "rinbach-colony.evidence.old-wave-exchange-essence::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "rinbach-colony.old-wave-exchange.essence"
- claim_key: "reward"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-08-26 추가됐으나 2026-09-02 삭제된 과거 교환"
- active: false
- is_active: false

### `rinbach-colony.evidence.old-wave-exchange-scale::ocean-progression-2026-08-26`

- evidence_seed_key: "rinbach-colony.evidence.old-wave-exchange-scale::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "rinbach-colony.old-wave-exchange.scale"
- claim_key: "reward"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-08-26 추가됐으나 2026-09-02 삭제된 과거 교환"
- active: false
- is_active: false
