<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 2025-12-23 월드 우두머리 보상 개편

## Identity

- slug: "world-boss-reward-2025-overhaul"
- name_ko: "2025-12-23 월드 우두머리 보상 개편"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "open_world"
- difficulty: "varies"

## Overview

- summary: "기존 4대 우두머리 보상 가치와 강화형 등장 확률이 상향되었다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `world-boss-reward-2025-overhaul.base-four`

- seed_key: "world-boss-reward-2025-overhaul.base-four"
- kind: "knowledge"
- requirement_level: "required"
- title: "기존 4대 보상"
- description: "크자카·누베르·카란다·쿠툼 보상 가치가 75% 상향되었다."
- structured_value:

```json
{
  "bosses": [
    "Kzarka",
    "Nouver",
    "Karanda",
    "Kutum"
  ],
  "effective_from": "2025-12-23",
  "knowledge_role": "fact",
  "reward_value_change_percent": 75
}
```

### `world-boss-reward-2025-overhaul.enhanced-probability`

- seed_key: "world-boss-reward-2025-overhaul.enhanced-probability"
- kind: "knowledge"
- requirement_level: "required"
- title: "강화형 등장 확률"
- description: "강화형 우두머리 등장 확률은 기존 대비 100% 상대 증가이며 확정 등장을 뜻하지 않는다."
- structured_value:

```json
{
  "effective_from": "2025-12-23",
  "guaranteed": false,
  "knowledge_role": "fact",
  "relative_probability_change_percent": 100
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

### `world-boss-reward-2025-overhaul.current-system`

- seed_key: "world-boss-reward-2025-overhaul.current-system"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "world-boss-current-system"
- content_name_ko: "월드 우두머리 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-current-system.md"

## Evidence and Sources

### Current evidence

### `world-boss-reward-2025-overhaul.claim.base-four::rare-wild-horses-2025-12-23`

- evidence_seed_key: "world-boss-reward-2025-overhaul.claim.base-four::rare-wild-horses-2025-12-23"
- source_id: "rare-wild-horses-2025-12-23"
- title: "12월 23일(화) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14989"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-23"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "world-boss-reward-2025-overhaul.base-four"
- claim_key: "requirement:base-four"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `world-boss-reward-2025-overhaul.claim.enhanced-probability::rare-wild-horses-2025-12-23`

- evidence_seed_key: "world-boss-reward-2025-overhaul.claim.enhanced-probability::rare-wild-horses-2025-12-23"
- source_id: "rare-wild-horses-2025-12-23"
- title: "12월 23일(화) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14989"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-23"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "world-boss-reward-2025-overhaul.enhanced-probability"
- claim_key: "requirement:enhanced-probability"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
