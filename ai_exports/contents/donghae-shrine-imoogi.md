<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 이무기 (동해도 검은사당)

## Identity

- slug: "donghae-shrine-imoogi"
- name_ko: "이무기 (동해도 검은사당)"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "varies"

## Overview

- summary: "이무기의 동해도 검은사당 맥락을 다른 동명 우두머리와 분리한 canonical 엔터티."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `donghae-shrine-imoogi.context`

- seed_key: "donghae-shrine-imoogi.context"
- kind: "knowledge"
- requirement_level: "required"
- title: "엔터티 맥락"
- description: "동해도 개인 검은사당 우두머리다."
- structured_value:

```json
{
  "boss_name": "이무기",
  "context": "black_shrine_donghae",
  "knowledge_role": "fact",
  "solo": true
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

### `donghae-shrine-imoogi.system`

- seed_key: "donghae-shrine-imoogi.system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "black-shrine-donghae-current-system"
- content_name_ko: "검은사당 동해도 현재 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/black-shrine-donghae-current-system.md"

## Evidence and Sources

### Current evidence

### `donghae-shrine-imoogi.claim.context::black-shrine-donghae-guide`

- evidence_seed_key: "donghae-shrine-imoogi.claim.context::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "donghae-shrine-imoogi.context"
- claim_key: "requirement:context"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
