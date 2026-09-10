<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 현행 교회 버프

## Identity

- slug: "church-buff-current"
- name_ko: "현행 교회 버프"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "현행 교회 버프는 전투 능력치와 경험치 효과를 하나의 선택으로 제공한다."
- purpose: "현행 통합 효과·가격·지속 시간을 과거 3종 버프와 구분한다."

## Requirements

### `church-buff-current.effects`

- seed_key: "church-buff-current.effects"
- kind: "stat"
- requirement_level: "required"
- title: "현행 효과"
- description: "공격력 8, 적중력 8, 피해 감소 8, 최대 생명력 150, 전투·기술 경험치 각 15%를 제공한다."
- structured_value:

```json
{
  "accuracy": 8,
  "ap": 8,
  "combat_exp_percent": 15,
  "damage_reduction": 8,
  "knowledge_role": "fact",
  "max_hp": 150,
  "skill_exp_percent": 15
}
```

### `church-buff-current.duration-price`

- seed_key: "church-buff-current.duration-price"
- kind: "item"
- requirement_level: "required"
- title: "시간과 비용"
- description: "120분은 은화 300만, 300분은 은화 1,000만이다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "options": [
    {
      "duration_minutes": 120,
      "silver": 3000000
    },
    {
      "duration_minutes": 300,
      "silver": 10000000
    }
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

### `church-buff-current.foundation`

- seed_key: "church-buff-current.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "combat-buff-foundation"
- content_name_ko: "전투 버프 기초"
- content_category: "combat_pve"
- note: "전투 버프의 교회 항목이다."
- order_no: 1
- relative_path: "../contents/combat-buff-foundation.md"

## Evidence and Sources

### Current evidence

### `church-buff-current.claim.duration-price::camp-church-rework-2025-12-30`

- evidence_seed_key: "church-buff-current.claim.duration-price::camp-church-rework-2025-12-30"
- source_id: "camp-church-rework-2025-12-30"
- title: "2025년 12월 30일 야영지 및 교회 버프 개편"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15012"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-30"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "church-buff-current.duration-price"
- claim_key: "requirement:church-buff-current.duration-price"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `church-buff-current.claim.duration-price::church-buff-guide`

- evidence_seed_key: "church-buff-current.claim.duration-price::church-buff-guide"
- source_id: "church-buff-guide"
- title: "교회 버프"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=375"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "church-buff-current.duration-price"
- claim_key: "requirement:church-buff-current.duration-price"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `church-buff-current.claim.effects::camp-church-rework-2025-12-30`

- evidence_seed_key: "church-buff-current.claim.effects::camp-church-rework-2025-12-30"
- source_id: "camp-church-rework-2025-12-30"
- title: "2025년 12월 30일 야영지 및 교회 버프 개편"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15012"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-30"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "church-buff-current.effects"
- claim_key: "requirement:church-buff-current.effects"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `church-buff-current.claim.effects::church-buff-guide`

- evidence_seed_key: "church-buff-current.claim.effects::church-buff-guide"
- source_id: "church-buff-guide"
- title: "교회 버프"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=375"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "church-buff-current.effects"
- claim_key: "requirement:church-buff-current.effects"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `church-buff-current.claim.legacy-three::camp-church-rework-2025-12-30`

- evidence_seed_key: "church-buff-current.claim.legacy-three::camp-church-rework-2025-12-30"
- source_id: "camp-church-rework-2025-12-30"
- title: "2025년 12월 30일 야영지 및 교회 버프 개편"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15012"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-30"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "church-buff-current.legacy-three"
- claim_key: "legacy:church-three-separate-buffs"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
