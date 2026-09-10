<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 황해도 기운 선택

## Identity

- slug: "hwanghae-aura-system"
- name_ko: "황해도 기운 선택"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "varies"

## Overview

- summary: "해·달·땅 기운은 파티 역할과 재도전 운영을 조정하는 선택 체계다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `hwanghae-aura-system.current`

- seed_key: "hwanghae-aura-system.current"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 기운"
- description: "공식 안내 역할을 속도·생존·재도전 관점으로 보존한다."
- structured_value:

```json
{
  "auras": [
    {
      "name": "Sun",
      "role": "speed"
    },
    {
      "name": "Moon",
      "role": "survival"
    },
    {
      "name": "Earth",
      "role": "retry_support"
    }
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

### `hwanghae-aura-system.current-system`

- seed_key: "hwanghae-aura-system.current-system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "black-shrine-hwanghae-current-system"
- content_name_ko: "검은사당 황해도 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/black-shrine-hwanghae-current-system.md"

## Evidence and Sources

### Current evidence

### `hwanghae-aura-system.claim.current::black-shrine-hwanghae-guide`

- evidence_seed_key: "hwanghae-aura-system.claim.current::black-shrine-hwanghae-guide"
- source_id: "black-shrine-hwanghae-guide"
- title: "검은 사당 - 황해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=404"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "hwanghae-aura-system.current"
- claim_key: "requirement:current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
