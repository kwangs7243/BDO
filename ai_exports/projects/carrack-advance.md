<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 에페리아 중범선 : 점진

## Identity

- slug: "carrack-advance"
- name_ko: "에페리아 중범선 : 점진"
- content_slug: "carrack-advance"
- summary: "검증된 점진 증축 요구량을 단계별로 추적하는 프로젝트다."
- active: true

## Overview

- summary: "검증된 점진 증축 요구량을 단계별로 추적하는 프로젝트다."

## Stages

### `carrack-advance.stage.base-ship`

- seed_key: "carrack-advance.stage.base-ship"
- name: "에페리아 무역선 준비"
- description: "증축 출발 선박인 에페리아 무역선을 준비한다."
- order_no: 1
- dependencies: []

### `carrack-advance.stage.blue-gear`

- seed_key: "carrack-advance.stage.blue-gear"
- name: "+10 무역선 파란 장비 준비"
- description: "검증된 파란 장비 4종을 각각 +10까지 준비한다."
- order_no: 2
- dependencies: ["carrack-advance.stage.base-ship"]

### `carrack-advance.stage.body-materials`

- seed_key: "carrack-advance.stage.body-materials"
- name: "점진 본체 재료 준비"
- description: "점진 증축에 필요한 본체 재료 5종을 준비한다."
- order_no: 3
- dependencies: ["carrack-advance.stage.base-ship"]

### `carrack-advance.stage.upgrade`

- seed_key: "carrack-advance.stage.upgrade"
- name: "점진 증축"
- description: "장비와 본체 재료 준비를 마친 뒤 점진으로 증축한다."
- order_no: 4
- dependencies: ["carrack-advance.stage.blue-gear", "carrack-advance.stage.body-materials"]

## Material Requirements

### `carrack-advance.material.caravel-black-dragon-figurehead-plus10`

- seed_key: "carrack-advance.material.caravel-black-dragon-figurehead-plus10"
- material_key: "caravel-black-dragon-figurehead-plus10"
- name_ko: "+10 에페리아 무역선 : 흑룡 선수상"
- unit: "개"
- stage_seed_key: "carrack-advance.stage.blue-gear"
- required_quantity: 1.0
- notes: "파란 장비 요구사항의 4종 각각 +10 조건을 1개 단위로 투영한다."
- order_no: 6
- source_entity_type: "content_requirement"
- source_entity_seed_key: "carrack-advance.requirement.blue-gear-plus10"

### `carrack-advance.material.caravel-upgraded-plating-plus10`

- seed_key: "carrack-advance.material.caravel-upgraded-plating-plus10"
- material_key: "caravel-upgraded-plating-plus10"
- name_ko: "+10 에페리아 무역선 : 개량형 장갑"
- unit: "개"
- stage_seed_key: "carrack-advance.stage.blue-gear"
- required_quantity: 1.0
- notes: "파란 장비 요구사항의 4종 각각 +10 조건을 1개 단위로 투영한다."
- order_no: 7
- source_entity_type: "content_requirement"
- source_entity_seed_key: "carrack-advance.requirement.blue-gear-plus10"

### `carrack-advance.material.caravel-mayna-cannon-plus10`

- seed_key: "carrack-advance.material.caravel-mayna-cannon-plus10"
- material_key: "caravel-mayna-cannon-plus10"
- name_ko: "+10 에페리아 무역선 : 메이나 함포"
- unit: "개"
- stage_seed_key: "carrack-advance.stage.blue-gear"
- required_quantity: 1.0
- notes: "파란 장비 요구사항의 4종 각각 +10 조건을 1개 단위로 투영한다."
- order_no: 8
- source_entity_type: "content_requirement"
- source_entity_seed_key: "carrack-advance.requirement.blue-gear-plus10"

### `carrack-advance.material.caravel-stratus-wind-sail-plus10`

- seed_key: "carrack-advance.material.caravel-stratus-wind-sail-plus10"
- material_key: "caravel-stratus-wind-sail-plus10"
- name_ko: "+10 에페리아 무역선 : 비층 바람 돛"
- unit: "개"
- stage_seed_key: "carrack-advance.stage.blue-gear"
- required_quantity: 1.0
- notes: "파란 장비 요구사항의 4종 각각 +10 조건을 1개 단위로 투영한다."
- order_no: 9
- source_entity_type: "content_requirement"
- source_entity_seed_key: "carrack-advance.requirement.blue-gear-plus10"

### `carrack-advance.material.moon-vein-flax`

- seed_key: "carrack-advance.material.moon-vein-flax"
- material_key: "moon-vein-flax"
- name_ko: "달의 핏줄이 새겨진 아마포"
- unit: "개"
- stage_seed_key: "carrack-advance.stage.body-materials"
- required_quantity: 180.0
- notes: null
- order_no: 1
- source_entity_type: "content_requirement"
- source_entity_seed_key: "carrack-advance.requirement.body-materials"

### `carrack-advance.material.deep-tide-standardized-timber`

- seed_key: "carrack-advance.material.deep-tide-standardized-timber"
- material_key: "deep-tide-standardized-timber"
- name_ko: "짙은 파도빛이 감도는 규격 각목"
- unit: "개"
- stage_seed_key: "carrack-advance.stage.body-materials"
- required_quantity: 144.0
- notes: null
- order_no: 2
- source_entity_type: "content_requirement"
- source_entity_seed_key: "carrack-advance.requirement.body-materials"

### `carrack-advance.material.brilliant-rock-salt-ingot`

- seed_key: "carrack-advance.material.brilliant-rock-salt-ingot"
- material_key: "brilliant-rock-salt-ingot"
- name_ko: "화려한 암염 주괴"
- unit: "개"
- stage_seed_key: "carrack-advance.stage.body-materials"
- required_quantity: 35.0
- notes: null
- order_no: 3
- source_entity_type: "content_requirement"
- source_entity_seed_key: "carrack-advance.requirement.body-materials"

### `carrack-advance.material.brilliant-pearl-crystal`

- seed_key: "carrack-advance.material.brilliant-pearl-crystal"
- material_key: "brilliant-pearl-crystal"
- name_ko: "화려한 진주 결정"
- unit: "개"
- stage_seed_key: "carrack-advance.stage.body-materials"
- required_quantity: 35.0
- notes: null
- order_no: 4
- source_entity_type: "content_requirement"
- source_entity_seed_key: "carrack-advance.requirement.body-materials"

### `carrack-advance.material.tear-of-the-ocean`

- seed_key: "carrack-advance.material.tear-of-the-ocean"
- material_key: "tear-of-the-ocean"
- name_ko: "심해의 눈물"
- unit: "개"
- stage_seed_key: "carrack-advance.stage.body-materials"
- required_quantity: 42.0
- notes: null
- order_no: 5
- source_entity_type: "content_requirement"
- source_entity_seed_key: "carrack-advance.requirement.body-materials"

## Acquisition Sources

### `carrack-advance.material.moon-vein-flax.source.young-sea-monster`

- project_material_seed_key: "carrack-advance.material.moon-vein-flax"
- seed_key: "carrack-advance.material.moon-vein-flax.source.young-sea-monster"
- content_slug: "oquilla-daily-young-sea-monster-hunter"
- content_name_ko: "[일일] 그믐달 어린 해왕류 사냥꾼"
- quantity_per_completion: 3.0
- notes: null
- order_no: 1
- relative_path: "../contents/oquilla-daily-young-sea-monster-hunter.md"
### `carrack-advance.material.moon-vein-flax.source.crow-shop`

- project_material_seed_key: "carrack-advance.material.moon-vein-flax"
- seed_key: "carrack-advance.material.moon-vein-flax.source.crow-shop"
- content_slug: "crow-coin-material-shop"
- content_name_ko: "까마귀 주화 증축 재료 상점"
- quantity_per_completion: null
- notes: "교환 가격은 정본 Content에 있으며 1회 획득량으로 환산하지 않는다."
- order_no: 2
- relative_path: "../contents/crow-coin-material-shop.md"
### `carrack-advance.material.deep-tide-standardized-timber.source.mutual-benefit`

- project_material_seed_key: "carrack-advance.material.deep-tide-standardized-timber"
- seed_key: "carrack-advance.material.deep-tide-standardized-timber.source.mutual-benefit"
- content_slug: "oquilla-daily-mutual-benefit"
- content_name_ko: "[일일] 너도 좋고, 나도 좋고"
- quantity_per_completion: 4.0
- notes: null
- order_no: 1
- relative_path: "../contents/oquilla-daily-mutual-benefit.md"
### `carrack-advance.material.deep-tide-standardized-timber.source.crow-shop`

- project_material_seed_key: "carrack-advance.material.deep-tide-standardized-timber"
- seed_key: "carrack-advance.material.deep-tide-standardized-timber.source.crow-shop"
- content_slug: "crow-coin-material-shop"
- content_name_ko: "까마귀 주화 증축 재료 상점"
- quantity_per_completion: null
- notes: "교환 가격은 정본 Content에 있으며 1회 획득량으로 환산하지 않는다."
- order_no: 2
- relative_path: "../contents/crow-coin-material-shop.md"
### `carrack-advance.material.brilliant-rock-salt-ingot.source.crow-shop`

- project_material_seed_key: "carrack-advance.material.brilliant-rock-salt-ingot"
- seed_key: "carrack-advance.material.brilliant-rock-salt-ingot.source.crow-shop"
- content_slug: "crow-coin-material-shop"
- content_name_ko: "까마귀 주화 증축 재료 상점"
- quantity_per_completion: null
- notes: "교환 가격은 정본 Content에 있으며 1회 획득량으로 환산하지 않는다."
- order_no: 1
- relative_path: "../contents/crow-coin-material-shop.md"
### `carrack-advance.material.brilliant-pearl-crystal.source.crow-shop`

- project_material_seed_key: "carrack-advance.material.brilliant-pearl-crystal"
- seed_key: "carrack-advance.material.brilliant-pearl-crystal.source.crow-shop"
- content_slug: "crow-coin-material-shop"
- content_name_ko: "까마귀 주화 증축 재료 상점"
- quantity_per_completion: null
- notes: "교환 가격은 정본 Content에 있으며 1회 획득량으로 환산하지 않는다."
- order_no: 1
- relative_path: "../contents/crow-coin-material-shop.md"
### `carrack-advance.material.tear-of-the-ocean.source.young-sea-monster`

- project_material_seed_key: "carrack-advance.material.tear-of-the-ocean"
- seed_key: "carrack-advance.material.tear-of-the-ocean.source.young-sea-monster"
- content_slug: "oquilla-daily-young-sea-monster-hunter"
- content_name_ko: "[일일] 그믐달 어린 해왕류 사냥꾼"
- quantity_per_completion: 1.0
- notes: null
- order_no: 1
- relative_path: "../contents/oquilla-daily-young-sea-monster-hunter.md"
### `carrack-advance.material.tear-of-the-ocean.source.nineshark`

- project_material_seed_key: "carrack-advance.material.tear-of-the-ocean"
- seed_key: "carrack-advance.material.tear-of-the-ocean.source.nineshark"
- content_slug: "oquilla-weekly-nineshark-hunter"
- content_name_ko: "[주간] 그믐달 길드의 나인샤크 사냥꾼"
- quantity_per_completion: 2.0
- notes: null
- order_no: 2
- relative_path: "../contents/oquilla-weekly-nineshark-hunter.md"
### `carrack-advance.material.tear-of-the-ocean.source.crow-shop`

- project_material_seed_key: "carrack-advance.material.tear-of-the-ocean"
- seed_key: "carrack-advance.material.tear-of-the-ocean.source.crow-shop"
- content_slug: "crow-coin-material-shop"
- content_name_ko: "까마귀 주화 증축 재료 상점"
- quantity_per_completion: null
- notes: "교환 가격은 정본 Content에 있으며 1회 획득량으로 환산하지 않는다."
- order_no: 3
- relative_path: "../contents/crow-coin-material-shop.md"

## Stateless Calculation Contract

- caller_quantity: "ephemeral personal state"
- missing_quantity: 0
- local_inventory_fallback: false
- persistence: false
- shortage_formula: "max(required_quantity - provided_quantity, 0)"
