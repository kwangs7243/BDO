<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 종족 추가 공격력

## Identity

- slug: "race-extra-ap"
- name_ko: "종족 추가 공격력"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "대상 종족에 적용되는 추가 공격력의 현행 명칭과 과거 PvE 제한 규칙을 구분한다."
- purpose: "종족 추가 공격력의 현행 적용을 과거 명칭·제한과 혼동하지 않는다."

## Requirements

### `race-extra-ap.current`

- seed_key: "race-extra-ap.current"
- kind: "stat"
- requirement_level: "required"
- title: "현행 종족 추가 공격력"
- description: "종족 추가 공격력은 최종 공격력 구성에 포함될 수 있으며 현행 명칭을 사용한다."
- structured_value:

```json
{
  "included_in_final_ap": true,
  "knowledge_role": "fact",
  "legacy_pve_reduction_active": false
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

### `race-extra-ap.claim.current::blood-altar-challenge-2026-07-15`

- evidence_seed_key: "race-extra-ap.claim.current::blood-altar-challenge-2026-07-15"
- source_id: "blood-altar-challenge-2026-07-15"
- title: "7월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15878"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "race-extra-ap.current"
- claim_key: "requirement:race-extra-ap.current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `race-extra-ap.claim.current::combat-system-rework-2025-07-23`

- evidence_seed_key: "race-extra-ap.claim.current::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "race-extra-ap.current"
- claim_key: "requirement:race-extra-ap.current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `race-extra-ap.claim.legacy-limit::combat-system-rework-2025-07-23`

- evidence_seed_key: "race-extra-ap.claim.legacy-limit::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "race-extra-ap.legacy-limit"
- claim_key: "legacy:race-extra-ap-pve-20-percent-reduction"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
