<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 적중과 회피 현행 시스템

## Identity

- slug: "accuracy-evasion-current-system"
- name_ko: "적중과 회피 현행 시스템"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "적중과 회피는 현행 수치 체계로 통합되었고 독립 퍼센트 능력치로 취급하지 않는다."
- purpose: "개편 전 퍼센트 표기와 현행 수치를 분리한다."

## Requirements

### `accuracy-evasion-current-system.current`

- seed_key: "accuracy-evasion-current-system.current"
- kind: "stat"
- requirement_level: "required"
- title: "현행 통합 수치"
- description: "적중률·회피율 퍼센트는 독립 능력치가 아니며 적중력·회피력 수치로 통합되었다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "legacy_one_percent_converted_to_points": 4,
  "standalone_accuracy_percent": false,
  "standalone_evasion_percent": false
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

### `accuracy-evasion-current-system.claim.current::combat-system-rework-2025-07-23`

- evidence_seed_key: "accuracy-evasion-current-system.claim.current::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "accuracy-evasion-current-system.current"
- claim_key: "requirement:accuracy-evasion-current-system.current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `accuracy-evasion-current-system.claim.legacy-percent::combat-system-rework-2025-07-23`

- evidence_seed_key: "accuracy-evasion-current-system.claim.legacy-percent::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "accuracy-evasion-current-system.legacy-percent"
- claim_key: "legacy:standalone-accuracy-evasion-percent"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
