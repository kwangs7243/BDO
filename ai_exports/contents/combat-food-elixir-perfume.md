<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 전투 음식·비약·향수

## Identity

- slug: "combat-food-elixir-perfume"
- name_ko: "전투 음식·비약·향수"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "음식·비약·향수는 서로 다른 소비 버프 범주이며 현행 효과와 사용 맥락을 분리해 검토한다."
- purpose: "과거 아이템 효과를 현행 추천처럼 고정하지 않고 대표 음식의 변경 이력을 보존한다."

## Requirements

### `combat-food-elixir-perfume.categories`

- seed_key: "combat-food-elixir-perfume.categories"
- kind: "item"
- requirement_level: "required"
- title: "소모품 범주"
- description: "음식, 비약, 향수는 별도 버프 범주로 조합 가능 여부와 효과를 아이템별 확인한다."
- structured_value:

```json
{
  "categories": [
    "food",
    "elixir",
    "perfume"
  ],
  "knowledge_role": "fact",
  "verify_per_item": true
}
```

### `combat-food-elixir-perfume.simple-cron-current`

- seed_key: "combat-food-elixir-perfume.simple-cron-current"
- kind: "item"
- requirement_level: "optional"
- title: "간편한 차림의 크론 정식 현행 효과"
- description: "현행 효과에는 백어택 피해량 5%와 치명타 피해량 5%가 포함된다."
- structured_value:

```json
{
  "back_attack_damage_percent": 5,
  "critical_damage_percent": 5,
  "down_attack_damage_percent": null,
  "item": "간편한 차림의 크론 정식",
  "knowledge_role": "fact"
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

### `combat-food-elixir-perfume.foundation`

- seed_key: "combat-food-elixir-perfume.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "combat-buff-foundation"
- content_name_ko: "전투 버프 기초"
- content_category: "combat_pve"
- note: "전투 버프의 소모품 항목이다."
- order_no: 1
- relative_path: "../contents/combat-buff-foundation.md"

## Evidence and Sources

### Current evidence

### `combat-food-elixir-perfume.claim.categories::combat-system-rework-2025-07-23`

- evidence_seed_key: "combat-food-elixir-perfume.claim.categories::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-food-elixir-perfume.categories"
- claim_key: "requirement:combat-food-elixir-perfume.categories"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `combat-food-elixir-perfume.claim.simple-cron-current::combat-system-rework-2025-07-23`

- evidence_seed_key: "combat-food-elixir-perfume.claim.simple-cron-current::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-food-elixir-perfume.simple-cron-current"
- claim_key: "requirement:combat-food-elixir-perfume.simple-cron-current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `combat-food-elixir-perfume.claim.simple-cron-legacy::combat-system-rework-2025-07-23`

- evidence_seed_key: "combat-food-elixir-perfume.claim.simple-cron-legacy::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-food-elixir-perfume.simple-cron-legacy"
- claim_key: "legacy:simple-cron-down-attack-five-percent"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
