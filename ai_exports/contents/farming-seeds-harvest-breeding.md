<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 재배 씨앗·수확·품종개량

## Identity

- slug: "farming-seeds-harvest-breeding"
- name_ko: "재배 씨앗·수확·품종개량"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "씨앗은 일반·고급·특상품·마력·신비 등급을 구분하며, 2026-06-04 이후 수확·품종개량 결과 수량과 확률이 크게 조정됐다."
- purpose: "씨앗 등급과 최신 수확·품종개량 배율을 한 흐름으로 연결한다."

## Requirements

### `farming-seeds-harvest-breeding.grades`

- seed_key: "farming-seeds-harvest-breeding.grades"
- kind: "item"
- requirement_level: "required"
- title: "씨앗·균사 등급"
- description: "대표 품질 progression이며 마력과 신비는 별도 씨앗이다."
- structured_value:

```json
{
  "grades": [
    "일반",
    "고급",
    "특상품",
    "마력",
    "신비"
  ],
  "magical_and_mysterious_same_item": false
}
```

### `farming-seeds-harvest-breeding.magical`

- seed_key: "farming-seeds-harvest-breeding.magical"
- kind: "level"
- requirement_level: "required"
- title: "마력이 깃든 씨앗"
- description: "재배 장인 1 이상 캐릭터가 품종개량으로 얻을 수 있고 5배 칸을 쓰며 품종개량 시 최소 1개를 보장한다."
- structured_value:

```json
{
  "breeding_guaranteed_seed_min": 1,
  "minimum_farming_level": "Artisan 1",
  "slot_multiplier": 5
}
```

### `farming-seeds-harvest-breeding.mysterious`

- seed_key: "farming-seeds-harvest-breeding.mysterious"
- kind: "item"
- requirement_level: "required"
- title: "신비한 씨앗"
- description: "품종개량 중 낮은 확률로 얻는 별도 씨앗이며 원작물 씨앗과 흔들어 섞어 사용한다."
- structured_value:

```json
{
  "acquisition": "low_probability_during_breeding",
  "processing": "shake_with_crop_seed",
  "slot_multiplier": 5
}
```

### `farming-seeds-harvest-breeding.output-overhaul`

- seed_key: "farming-seeds-harvest-breeding.output-overhaul"
- kind: "stat"
- requirement_level: "required"
- title: "2026-06-04 결과 배율"
- description: "확정·확률 획득물, 담홍색 잎사귀와 지정 특수 작물의 최신 배율이다."
- structured_value:

```json
{
  "blush_leaf_from_breeding": {
    "probability_multiplier": 2,
    "quantity_multiplier": 2.5
  },
  "designated_special_crops": {
    "families": [
      "신비한 씨앗 작물",
      "송로 버섯 균사",
      "이상하고 아름다운 볍씨"
    ],
    "quantity_multiplier": 3
  },
  "guaranteed_items_quantity_multiplier": 5,
  "probabilistic_items": {
    "probability_multiplier": 2,
    "quantity_multiplier": 2.5
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

### `farming-seeds-harvest-breeding.cycle`

- seed_key: "farming-seeds-harvest-breeding.cycle"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "farming-current-cycle"
- content_name_ko: "재배 현재 주기"
- content_category: "life"
- note: "재배 주기의 심기·수확"
- order_no: 1
- relative_path: "../contents/farming-current-cycle.md"
### `farming-seeds-harvest-breeding.moles`

- seed_key: "farming-seeds-harvest-breeding.moles"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "farming-moles"
- content_name_ko: "재배 두더지와 슈슈"
- content_category: "life"
- note: "수확·품종개량 시 두더지 발생"
- order_no: 2
- relative_path: "../contents/farming-moles.md"
### `farming-seeds-harvest-breeding.pouch`

- seed_key: "farming-seeds-harvest-breeding.pouch"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "old-moon-seed-pouch"
- content_name_ko: "클로의 그믐달 씨앗 주머니"
- content_category: "life"
- note: "씨앗 보관"
- order_no: 3
- relative_path: "../contents/old-moon-seed-pouch.md"
### `farming-moles.harvest`

- seed_key: "farming-moles.harvest"
- direction: "incoming"
- relation_type: "related"
- content_slug: "farming-moles"
- content_name_ko: "재배 두더지와 슈슈"
- content_category: "life"
- note: "수확·품종개량 발생"
- order_no: 1
- relative_path: "../contents/farming-moles.md"
### `old-moon-seed-pouch.seeds`

- seed_key: "old-moon-seed-pouch.seeds"
- direction: "incoming"
- relation_type: "related"
- content_slug: "old-moon-seed-pouch"
- content_name_ko: "클로의 그믐달 씨앗 주머니"
- content_category: "life"
- note: "씨앗 보관"
- order_no: 1
- relative_path: "../contents/old-moon-seed-pouch.md"
### `farming-current-cycle.seeds`

- seed_key: "farming-current-cycle.seeds"
- direction: "incoming"
- relation_type: "related"
- content_slug: "farming-current-cycle"
- content_name_ko: "재배 현재 주기"
- content_category: "life"
- note: "씨앗·수확·품종개량"
- order_no: 2
- relative_path: "../contents/farming-current-cycle.md"
### `farming-onboarding-strategy.seeds`

- seed_key: "farming-onboarding-strategy.seeds"
- direction: "incoming"
- relation_type: "related"
- content_slug: "farming-onboarding-strategy"
- content_name_ko: "재배 입문 전략"
- content_category: "life"
- note: null
- order_no: 3
- relative_path: "../contents/farming-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `farming-seeds-harvest-breeding.summary::farming-guide`

- evidence_seed_key: "farming-seeds-harvest-breeding.summary::farming-guide"
- source_id: "farming-guide"
- title: "재배"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=94"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "farming-seeds-harvest-breeding"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "씨앗 등급과 최신 배율"
- active: true
- is_active: true

### `farming-seeds-harvest-breeding.summary::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-seeds-harvest-breeding.summary::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "farming-seeds-harvest-breeding"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "씨앗 등급과 최신 배율"
- active: true
- is_active: true

### `farming-seeds-harvest-breeding.requirement.grades::farming-guide`

- evidence_seed_key: "farming-seeds-harvest-breeding.requirement.grades::farming-guide"
- source_id: "farming-guide"
- title: "재배"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=94"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-seeds-harvest-breeding.grades"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "씨앗 품질 구분"
- active: true
- is_active: true

### `farming-seeds-harvest-breeding.requirement.magical::farming-guide`

- evidence_seed_key: "farming-seeds-harvest-breeding.requirement.magical::farming-guide"
- source_id: "farming-guide"
- title: "재배"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=94"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-seeds-harvest-breeding.magical"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "마력 씨앗 조건"
- active: true
- is_active: true

### `farming-seeds-harvest-breeding.requirement.mysterious::farming-guide`

- evidence_seed_key: "farming-seeds-harvest-breeding.requirement.mysterious::farming-guide"
- source_id: "farming-guide"
- title: "재배"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=94"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-seeds-harvest-breeding.mysterious"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "신비 씨앗 구분"
- active: true
- is_active: true

### `farming-seeds-harvest-breeding.requirement.output-overhaul::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-seeds-harvest-breeding.requirement.output-overhaul::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-seeds-harvest-breeding.output-overhaul"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "5배·2배·2.5배·3배 최신 결과"
- active: true
- is_active: true

### Historical / inactive evidence

- None
