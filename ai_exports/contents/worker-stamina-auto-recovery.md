<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 일꾼 행동력과 자동 회복

## Identity

- slug: "worker-stamina-auto-recovery"
- name_ko: "일꾼 행동력과 자동 회복"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "자동 회복을 켜면 일꾼 행동력이 3 이하일 때 가문 가방의 회복 음식을 자동 사용하며 텃밭 일꾼에도 적용된다."
- purpose: "자동 회복과 수동 회복을 분리한다."

## Requirements

### `worker-stamina-auto-recovery.items`

- seed_key: "worker-stamina-auto-recovery.items"
- kind: "item"
- requirement_level: "required"
- title: "행동력 회복 음식"
- description: "가문 가방에 보관 가능한 대표 회복 음식이다."
- structured_value:

```json
{
  "examples": [
    "맥주",
    "새구이",
    "치즈 파이"
  ],
  "family_inventory_supported": true
}
```

### `worker-stamina-auto-recovery.automatic`

- seed_key: "worker-stamina-auto-recovery.automatic"
- kind: "other"
- requirement_level: "required"
- title: "자동 회복"
- description: "행동력 임계값과 재료 출처를 기록한다."
- structured_value:

```json
{
  "applies_to_farm_workers": true,
  "enabled_by_user": true,
  "item_source": "family_inventory",
  "trigger_at_or_below_stamina": 3
}
```

### `worker-stamina-auto-recovery.manual`

- seed_key: "worker-stamina-auto-recovery.manual"
- kind: "other"
- requirement_level: "required"
- title: "수동 회복"
- description: "일꾼 관리에서 직접 회복하는 별도 방식이다."
- structured_value:

```json
{
  "available": true,
  "same_mechanic_as_auto_recovery": false
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

### `worker-stamina-auto-recovery.cooking`

- seed_key: "worker-stamina-auto-recovery.cooking"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "cooking-current-system"
- content_name_ko: "요리 현재 시스템"
- content_category: "life"
- note: "요리로 만드는 회복 음식과 연결된다."
- order_no: 1
- relative_path: "../contents/cooking-current-system.md"

## Evidence and Sources

### Current evidence

### `worker-stamina-auto-recovery.claim.current::worker-guide`

- evidence_seed_key: "worker-stamina-auto-recovery.claim.current::worker-guide"
- source_id: "worker-guide"
- title: "일꾼"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=95"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-stamina-auto-recovery"
- claim_key: "requirements:worker-stamina-auto-recovery"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `worker-stamina-auto-recovery.claim.current::worker-overhaul-2023-05-24`

- evidence_seed_key: "worker-stamina-auto-recovery.claim.current::worker-overhaul-2023-05-24"
- source_id: "worker-overhaul-2023-05-24"
- title: "5월 24일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=10369"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-05-24"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-stamina-auto-recovery"
- claim_key: "requirements:worker-stamina-auto-recovery"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
