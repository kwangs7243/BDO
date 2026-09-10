<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 전투 버프 기초

## Identity

- slug: "combat-buff-foundation"
- name_ko: "전투 버프 기초"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "교회·야영지·음식·비약·향수 등 전투 버프를 출처와 지속 시간별로 구분한다."
- purpose: "서로 다른 버프 묶음과 과거 효과를 섞지 않고 준비 항목으로 관리한다."

## Requirements

### `combat-buff-foundation.categories`

- seed_key: "combat-buff-foundation.categories"
- kind: "item"
- requirement_level: "required"
- title: "버프 범주"
- description: "전투 준비 버프는 교회, 야영지, 음식, 비약, 향수 범주를 별도로 확인한다."
- structured_value:

```json
{
  "categories": [
    "church",
    "camp",
    "food",
    "elixir",
    "perfume"
  ],
  "effects_must_be_verified_per_item": true,
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

### `camp-combat-buffs.foundation`

- seed_key: "camp-combat-buffs.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "camp-combat-buffs"
- content_name_ko: "야영지 전투 버프"
- content_category: "combat_pve"
- note: "전투 버프의 야영지 항목이다."
- order_no: 1
- relative_path: "../contents/camp-combat-buffs.md"
### `church-buff-current.foundation`

- seed_key: "church-buff-current.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "church-buff-current"
- content_name_ko: "현행 교회 버프"
- content_category: "combat_pve"
- note: "전투 버프의 교회 항목이다."
- order_no: 1
- relative_path: "../contents/church-buff-current.md"
### `combat-food-elixir-perfume.foundation`

- seed_key: "combat-food-elixir-perfume.foundation"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "combat-food-elixir-perfume"
- content_name_ko: "전투 음식·비약·향수"
- content_category: "combat_pve"
- note: "전투 버프의 소모품 항목이다."
- order_no: 1
- relative_path: "../contents/combat-food-elixir-perfume.md"
### `grind-setup-strategy-foundation.buffs`

- seed_key: "grind-setup-strategy-foundation.buffs"
- direction: "incoming"
- relation_type: "related"
- content_slug: "grind-setup-strategy-foundation"
- content_name_ko: "사냥 세팅 전략 기초"
- content_category: "combat_pve"
- note: "전투 버프 준비 항목을 연결한다."
- order_no: 4
- relative_path: "../contents/grind-setup-strategy-foundation.md"

## Evidence and Sources

### Current evidence

### `combat-buff-foundation.claim.categories::camp-church-rework-2025-12-30`

- evidence_seed_key: "combat-buff-foundation.claim.categories::camp-church-rework-2025-12-30"
- source_id: "camp-church-rework-2025-12-30"
- title: "2025년 12월 30일 야영지 및 교회 버프 개편"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15012"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-30"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-buff-foundation.categories"
- claim_key: "requirement:combat-buff-foundation.categories"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `combat-buff-foundation.claim.categories::church-buff-guide`

- evidence_seed_key: "combat-buff-foundation.claim.categories::church-buff-guide"
- source_id: "church-buff-guide"
- title: "교회 버프"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=375"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-buff-foundation.categories"
- claim_key: "requirement:combat-buff-foundation.categories"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `combat-buff-foundation.claim.categories::combat-system-rework-2025-07-23`

- evidence_seed_key: "combat-buff-foundation.claim.categories::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "combat-buff-foundation.categories"
- claim_key: "requirement:combat-buff-foundation.categories"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
