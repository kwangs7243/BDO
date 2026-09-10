<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 해원석 progression

## Identity

- slug: "sea-crystals"
- name_ko: "해원석 progression"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "엘토르부터 루살카까지의 해원석 성장과 루살카 고정 효과·제작식."
- purpose: "대형 선박 해원석의 성장 순서와 루살카 제작 비용을 구조화한다."

## Requirements

### `sea-crystals.lusalka-recipe.magoria`

- seed_key: "sea-crystals.lusalka-recipe.magoria"
- kind: "item"
- requirement_level: "required"
- title: "루살카 원석 제작법 1"
- description: "마고리아의 기원 10개, 오킬루아 적빛담수 1개, 공허의 해원석 1개를 간이연금한다."
- structured_value:

```json
{
  "inputs": {
    "공허의 해원석": 1,
    "마고리아의 기원": 10,
    "오킬루아 적빛담수": 1
  },
  "output": {
    "루살카 원석": 1
  },
  "process": "간이연금"
}
```

### `sea-crystals.lusalka-recipe.lusalka`

- seed_key: "sea-crystals.lusalka-recipe.lusalka"
- kind: "item"
- requirement_level: "required"
- title: "루살카 원석 제작법 2"
- description: "루살카의 기원 3개와 공허의 해원석 1개를 간이연금한다."
- structured_value:

```json
{
  "inputs": {
    "공허의 해원석": 1,
    "루살카의 기원": 3
  },
  "output": {
    "루살카 원석": 1
  },
  "process": "간이연금"
}
```

## Steps

- None

## Schedules

- None

## Rewards

### `sea-crystals.lusalka-effect.speed`

- seed_key: "sea-crystals.lusalka-effect.speed"
- name: "루살카 해원석: 속도"
- reward_type: "fixed_effect"
- amount: 4.5
- min_amount: null
- max_amount: null
- unit: "percent"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "루살카 원석 사용 시 8종 중 지정된 확률로 한 종류를 획득하며, 선택된 효과 수치는 고정"
- order_no: 1

### `sea-crystals.lusalka-effect.accel`

- seed_key: "sea-crystals.lusalka-effect.accel"
- name: "루살카 해원석: 가속도"
- reward_type: "fixed_effect"
- amount: 4.5
- min_amount: null
- max_amount: null
- unit: "percent"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "루살카 원석 사용 시 8종 중 지정된 확률로 한 종류를 획득하며, 선택된 효과 수치는 고정"
- order_no: 2

### `sea-crystals.lusalka-effect.turn`

- seed_key: "sea-crystals.lusalka-effect.turn"
- name: "루살카 해원석: 회전"
- reward_type: "fixed_effect"
- amount: 9.0
- min_amount: null
- max_amount: null
- unit: "percent"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "루살카 원석 사용 시 8종 중 지정된 확률로 한 종류를 획득하며, 선택된 효과 수치는 고정"
- order_no: 3

### `sea-crystals.lusalka-effect.brake`

- seed_key: "sea-crystals.lusalka-effect.brake"
- name: "루살카 해원석: 제동"
- reward_type: "fixed_effect"
- amount: 9.0
- min_amount: null
- max_amount: null
- unit: "percent"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "루살카 원석 사용 시 8종 중 지정된 확률로 한 종류를 획득하며, 선택된 효과 수치는 고정"
- order_no: 4

### `sea-crystals.lusalka-effect.weight`

- seed_key: "sea-crystals.lusalka-effect.weight"
- name: "루살카 해원석: 무게"
- reward_type: "fixed_effect"
- amount: 1350.0
- min_amount: null
- max_amount: null
- unit: "LT"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "루살카 원석 사용 시 8종 중 지정된 확률로 한 종류를 획득하며, 선택된 효과 수치는 고정"
- order_no: 5

### `sea-crystals.lusalka-effect.durability`

- seed_key: "sea-crystals.lusalka-effect.durability"
- name: "루살카 해원석: 내구도"
- reward_type: "fixed_effect"
- amount: 22500.0
- min_amount: null
- max_amount: null
- unit: "point"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "루살카 원석 사용 시 8종 중 지정된 확률로 한 종류를 획득하며, 선택된 효과 수치는 고정"
- order_no: 6

### `sea-crystals.lusalka-effect.monster-damage`

- seed_key: "sea-crystals.lusalka-effect.monster-damage"
- name: "루살카 해원석: 대양 몬스터 추가 피해량"
- reward_type: "fixed_effect"
- amount: 900.0
- min_amount: null
- max_amount: null
- unit: "선박별 타격 수당"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "루살카 원석 사용 시 8종 중 지정된 확률로 한 종류를 획득하며, 선택된 효과 수치는 고정"
- order_no: 7

### `sea-crystals.lusalka-effect.ship-damage`

- seed_key: "sea-crystals.lusalka-effect.ship-damage"
- name: "루살카 해원석: 선박 추가 피해량"
- reward_type: "fixed_effect"
- amount: 450.0
- min_amount: null
- max_amount: null
- unit: "선박별 타격 수당"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "루살카 원석 사용 시 8종 중 지정된 확률로 한 종류를 획득하며, 선택된 효과 수치는 고정"
- order_no: 8

### `sea-crystals.shop.red-freshwater`

- seed_key: "sea-crystals.shop.red-freshwater"
- name: "오킬루아 적빛담수"
- reward_type: "shop_price"
- amount: 40.0
- min_amount: null
- max_amount: null
- unit: "까마귀 주화"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "라비니아·리비니아 까마귀 주화 상점"
- order_no: 9

### `sea-crystals.shop.empty-crystal`

- seed_key: "sea-crystals.shop.empty-crystal"
- name: "공허의 해원석"
- reward_type: "shop_price"
- amount: 10.0
- min_amount: null
- max_amount: null
- unit: "까마귀 주화"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "라비니아·리비니아 까마귀 주화 상점"
- order_no: 10

## Sections

### `sea-crystals.progression`

- seed_key: "sea-crystals.progression"
- section_type: "overview"
- title: "해원석 성장 순서"
- order_no: 1

#### body_markdown

엘토르 → 세르니 → 줄라티아 → 마고리아 → 루살카 순서로 성장한다.

### `sea-crystals.ebenruth`

- seed_key: "sea-crystals.ebenruth"
- section_type: "notes"
- title: "바다의 눈물이 담긴 에벤루스의 놀"
- order_no: 2

#### body_markdown

루살카 해원석 1개와 에벤루스의 놀 1개를 공작하면 바다의 눈물이 담긴 에벤루스의 놀을 만들고, 사용한 루살카 해원석 효과를 추가로 적용받는다. 다시 공작하면 두 재료를 돌려받는다.

## Related Contents

### `sea-crystals.relation.rinbach`

- seed_key: "sea-crystals.relation.rinbach"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "rinbach-colony"
- content_name_ko: "린바크 군락지"
- content_category: "ocean_combat"
- note: "세르니·줄라티아·마고리아 원석 획득처 중 하나"
- order_no: 1
- relative_path: "../contents/rinbach-colony.md"
### `sea-crystals.relation.ebenruth`

- seed_key: "sea-crystals.relation.ebenruth"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "ebenruth-nol"
- content_name_ko: "에벤루스의 놀"
- content_category: "ocean_guide"
- note: "루살카 해원석과 에벤루스의 놀 결합"
- order_no: 3
- relative_path: "../contents/ebenruth-nol.md"
### `hollow-maretta.relation.sea-crystals`

- seed_key: "hollow-maretta.relation.sea-crystals"
- direction: "incoming"
- relation_type: "related"
- content_slug: "hollow-maretta"
- content_name_ko: "공허한 마레타"
- content_category: "ocean_guide"
- note: "선율이 맴도는 기운의 해원석 제작 연결"
- order_no: 1
- relative_path: "../contents/hollow-maretta.md"
### `ebenruth-nol.relation.sea-crystals`

- seed_key: "ebenruth-nol.relation.sea-crystals"
- direction: "incoming"
- relation_type: "related"
- content_slug: "ebenruth-nol"
- content_name_ko: "에벤루스의 놀"
- content_category: "ocean_guide"
- note: "루살카 해원석과 결합하며 해원석 데이터는 기존 콘텐츠를 참조"
- order_no: 2
- relative_path: "../contents/ebenruth-nol.md"
### `lekrashan-hunting.relation.sea-crystals`

- seed_key: "lekrashan-hunting.relation.sea-crystals"
- direction: "incoming"
- relation_type: "related"
- content_slug: "lekrashan-hunting"
- content_name_ko: "레크라샨 해왕류 의뢰"
- content_category: "ocean_guide"
- note: "담수 선택 보상 사용처"
- order_no: 2
- relative_path: "../contents/lekrashan-hunting.md"
### `life-artifacts-lightstones.ocean-crystals`

- seed_key: "life-artifacts-lightstones.ocean-crystals"
- direction: "incoming"
- relation_type: "related"
- content_slug: "life-artifacts-lightstones"
- content_name_ko: "생활 유물과 광명석"
- content_category: "life"
- note: "생활 광명석과 선박용 해원석은 서로 다른 장비 체계다."
- order_no: 2
- relative_path: "../contents/life-artifacts-lightstones.md"
### `rinbach-colony.relation.crystals`

- seed_key: "rinbach-colony.relation.crystals"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "rinbach-colony"
- content_name_ko: "린바크 군락지"
- content_category: "ocean_combat"
- note: "세르니·줄라티아·마고리아 원석 획득처"
- order_no: 3
- relative_path: "../contents/rinbach-colony.md"
### `sailing-onboarding-strategy.sea-crystals`

- seed_key: "sailing-onboarding-strategy.sea-crystals"
- direction: "incoming"
- relation_type: "related"
- content_slug: "sailing-onboarding-strategy"
- content_name_ko: "항해 입문 운영 전략"
- content_category: "ocean_guide"
- note: "상위 장비 선택지"
- order_no: 7
- relative_path: "../contents/sailing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `sea-crystals.evidence.lusalka-recipe-lusalka::sea-crystal-guide`

- evidence_seed_key: "sea-crystals.evidence.lusalka-recipe-lusalka::sea-crystal-guide"
- source_id: "sea-crystal-guide"
- title: "해원석"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=376"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sea-crystals.lusalka-recipe.lusalka"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "루살카의 기원 3개와 공허의 해원석 1개를 간이연금한다."
- active: true
- is_active: true

### `sea-crystals.evidence.lusalka-recipe-magoria::sea-crystal-guide`

- evidence_seed_key: "sea-crystals.evidence.lusalka-recipe-magoria::sea-crystal-guide"
- source_id: "sea-crystal-guide"
- title: "해원석"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=376"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sea-crystals.lusalka-recipe.magoria"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "마고리아의 기원 10개, 오킬루아 적빛담수 1개, 공허의 해원석 1개를 간이연금한다."
- active: true
- is_active: true

### `sea-crystals.evidence.ebenruth::sea-crystal-guide`

- evidence_seed_key: "sea-crystals.evidence.ebenruth::sea-crystal-guide"
- source_id: "sea-crystal-guide"
- title: "해원석"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=376"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "sea-crystals.ebenruth"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "루살카 해원석 1개와 에벤루스의 놀 1개를 공작하면 바다의 눈물이 담긴 에벤루스의 놀을 만들고, 사용한 루살카 해원석 효과를 추가로 적용받는다. 다시 공작하면 두 재료를 돌려받는다."
- active: true
- is_active: true

### `sea-crystals.evidence.progression::sea-crystal-guide`

- evidence_seed_key: "sea-crystals.evidence.progression::sea-crystal-guide"
- source_id: "sea-crystal-guide"
- title: "해원석"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=376"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "sea-crystals.progression"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "엘토르 → 세르니 → 줄라티아 → 마고리아 → 루살카 순서로 성장한다."
- active: true
- is_active: true

### `sea-crystals.evidence.lusalka-effect-accel::sea-crystal-guide`

- evidence_seed_key: "sea-crystals.evidence.lusalka-effect-accel::sea-crystal-guide"
- source_id: "sea-crystal-guide"
- title: "해원석"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=376"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "sea-crystals.lusalka-effect.accel"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "루살카 원석 사용 시 8종 중 지정된 확률로 한 종류를 획득하며, 선택된 효과 수치는 고정"
- active: true
- is_active: true

### `sea-crystals.evidence.lusalka-effect-brake::sea-crystal-guide`

- evidence_seed_key: "sea-crystals.evidence.lusalka-effect-brake::sea-crystal-guide"
- source_id: "sea-crystal-guide"
- title: "해원석"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=376"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "sea-crystals.lusalka-effect.brake"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "루살카 원석 사용 시 8종 중 지정된 확률로 한 종류를 획득하며, 선택된 효과 수치는 고정"
- active: true
- is_active: true

### `sea-crystals.evidence.lusalka-effect-durability::sea-crystal-guide`

- evidence_seed_key: "sea-crystals.evidence.lusalka-effect-durability::sea-crystal-guide"
- source_id: "sea-crystal-guide"
- title: "해원석"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=376"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "sea-crystals.lusalka-effect.durability"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "루살카 원석 사용 시 8종 중 지정된 확률로 한 종류를 획득하며, 선택된 효과 수치는 고정"
- active: true
- is_active: true

### `sea-crystals.evidence.lusalka-effect-monster-damage::sea-crystal-guide`

- evidence_seed_key: "sea-crystals.evidence.lusalka-effect-monster-damage::sea-crystal-guide"
- source_id: "sea-crystal-guide"
- title: "해원석"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=376"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "sea-crystals.lusalka-effect.monster-damage"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "루살카 원석 사용 시 8종 중 지정된 확률로 한 종류를 획득하며, 선택된 효과 수치는 고정"
- active: true
- is_active: true

### `sea-crystals.evidence.lusalka-effect-ship-damage::sea-crystal-guide`

- evidence_seed_key: "sea-crystals.evidence.lusalka-effect-ship-damage::sea-crystal-guide"
- source_id: "sea-crystal-guide"
- title: "해원석"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=376"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "sea-crystals.lusalka-effect.ship-damage"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "루살카 원석 사용 시 8종 중 지정된 확률로 한 종류를 획득하며, 선택된 효과 수치는 고정"
- active: true
- is_active: true

### `sea-crystals.evidence.lusalka-effect-speed::sea-crystal-guide`

- evidence_seed_key: "sea-crystals.evidence.lusalka-effect-speed::sea-crystal-guide"
- source_id: "sea-crystal-guide"
- title: "해원석"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=376"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "sea-crystals.lusalka-effect.speed"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "루살카 원석 사용 시 8종 중 지정된 확률로 한 종류를 획득하며, 선택된 효과 수치는 고정"
- active: true
- is_active: true

### `sea-crystals.evidence.lusalka-effect-turn::sea-crystal-guide`

- evidence_seed_key: "sea-crystals.evidence.lusalka-effect-turn::sea-crystal-guide"
- source_id: "sea-crystal-guide"
- title: "해원석"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=376"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "sea-crystals.lusalka-effect.turn"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "루살카 원석 사용 시 8종 중 지정된 확률로 한 종류를 획득하며, 선택된 효과 수치는 고정"
- active: true
- is_active: true

### `sea-crystals.evidence.lusalka-effect-weight::sea-crystal-guide`

- evidence_seed_key: "sea-crystals.evidence.lusalka-effect-weight::sea-crystal-guide"
- source_id: "sea-crystal-guide"
- title: "해원석"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=376"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "sea-crystals.lusalka-effect.weight"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "루살카 원석 사용 시 8종 중 지정된 확률로 한 종류를 획득하며, 선택된 효과 수치는 고정"
- active: true
- is_active: true

### `sea-crystals.evidence.shop-empty-crystal::sea-crystal-guide`

- evidence_seed_key: "sea-crystals.evidence.shop-empty-crystal::sea-crystal-guide"
- source_id: "sea-crystal-guide"
- title: "해원석"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=376"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "sea-crystals.shop.empty-crystal"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "라비니아·리비니아 까마귀 주화 상점"
- active: true
- is_active: true

### `sea-crystals.evidence.shop-red-freshwater::sea-crystal-guide`

- evidence_seed_key: "sea-crystals.evidence.shop-red-freshwater::sea-crystal-guide"
- source_id: "sea-crystal-guide"
- title: "해원석"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=376"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "sea-crystals.shop.red-freshwater"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "라비니아·리비니아 까마귀 주화 상점"
- active: true
- is_active: true

### Historical / inactive evidence

- None
