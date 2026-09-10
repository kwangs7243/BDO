<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 특수 공격 시스템

## Identity

- slug: "special-attack-system"
- name_ko: "특수 공격 시스템"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "백어택·다운어택 등 특수 공격의 피해 증가 효과는 조건이 겹치면 함께 적용될 수 있다."
- purpose: "특수 공격 발동 조건과 중첩 가능성을 별도로 기록한다."

## Requirements

### `special-attack-system.stacking`

- seed_key: "special-attack-system.stacking"
- kind: "other"
- requirement_level: "required"
- title: "특수 공격 중첩"
- description: "서로 다른 특수 공격 조건을 동시에 만족하면 각 특수 공격 효과가 함께 적용될 수 있다."
- structured_value:

```json
{
  "different_special_attacks_can_stack": true,
  "examples": [
    "back_attack",
    "down_attack",
    "air_attack",
    "counter_attack"
  ],
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

- None

## Evidence and Sources

### Current evidence

### `special-attack-system.claim.stacking::combat-system-rework-2025-07-23`

- evidence_seed_key: "special-attack-system.claim.stacking::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "special-attack-system.stacking"
- claim_key: "requirement:special-attack-system.stacking"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
