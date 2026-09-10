<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 심판의 천칭

## Identity

- slug: "judgment-scales"
- name_ko: "심판의 천칭"
- category: "combat"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "party"
- difficulty: "extreme"

## Overview

- summary: "2026-08-12 추가된 에다니아 내부 사냥터."
- purpose: "에다니아 내부 성장 및 전리품 획득"

## Requirements

### `judgment-scales.current-stats`

- seed_key: "judgment-scales.current-stats"
- kind: "stat"
- requirement_level: "recommended"
- title: "현재 권장 수치"
- description: "공식 표기·최종 권장 수치. 명시되지 않은 공격력 상한을 추정하지 않는다."
- structured_value:

```json
{
  "explicit_ap_cap": null,
  "final_ap_recommended": 2455,
  "final_dp_recommended": 860,
  "knowledge_role": "fact",
  "launched_at": "2026-08-12",
  "party_size": 3,
  "sheet_ap_recommended": 415,
  "sheet_dp_recommended": 500
}
```

### `judgment-scales.trash-loot`

- seed_key: "judgment-scales.trash-loot"
- kind: "item"
- requirement_level: "optional"
- title: "공식 잡동사니"
- description: "잡동사니 NPC 가격과 확인된 무게."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "trash_item": "엘리언 추종자의 표식",
  "trash_npc_price": 186458
}
```

### `judgment-scales.patch-provenance`

- seed_key: "judgment-scales.patch-provenance"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "패치 적용 구간"
- description: "측정은 적용 패치 구간과 함께 해석한다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "measurement_patch_window_required": true,
  "patch_windows": [
    "2026-08-12",
    "2026-08-19"
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

- None

## Evidence and Sources

### Current evidence

### `judgment-scales.claim.current-stats::edania-internal-launch-2026-08-12`

- evidence_seed_key: "judgment-scales.claim.current-stats::edania-internal-launch-2026-08-12"
- source_id: "edania-internal-launch-2026-08-12"
- title: "8월 12일(수) 업데이트 안내 - 에다니아 내부 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "judgment-scales.current-stats"
- claim_key: "requirement:current-stats"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `judgment-scales.claim.patch-provenance::edania-internal-balance-2026-08-19`

- evidence_seed_key: "judgment-scales.claim.patch-provenance::edania-internal-balance-2026-08-19"
- source_id: "edania-internal-balance-2026-08-19"
- title: "8월 19일(수) 업데이트 안내 - 에다니아 내부 사냥터 조정"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16063"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-19"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "judgment-scales.patch-provenance"
- claim_key: "requirement:patch-provenance"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `judgment-scales.claim.patch-provenance::edania-internal-launch-2026-08-12`

- evidence_seed_key: "judgment-scales.claim.patch-provenance::edania-internal-launch-2026-08-12"
- source_id: "edania-internal-launch-2026-08-12"
- title: "8월 12일(수) 업데이트 안내 - 에다니아 내부 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "judgment-scales.patch-provenance"
- claim_key: "requirement:patch-provenance"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `judgment-scales.claim.trash-loot::edania-internal-launch-2026-08-12`

- evidence_seed_key: "judgment-scales.claim.trash-loot::edania-internal-launch-2026-08-12"
- source_id: "edania-internal-launch-2026-08-12"
- title: "8월 12일(수) 업데이트 안내 - 에다니아 내부 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "judgment-scales.trash-loot"
- claim_key: "requirement:trash-loot"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
