<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 마가이아 신전

## Identity

- slug: "magaia-temple"
- name_ko: "마가이아 신전"
- category: "combat"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "extreme"

## Overview

- summary: "2026-08-12 추가된 에다니아 내부 사냥터."
- purpose: "에다니아 내부 성장 및 전리품 획득"

## Requirements

### `magaia-temple.current-stats`

- seed_key: "magaia-temple.current-stats"
- kind: "stat"
- requirement_level: "recommended"
- title: "현재 권장 수치"
- description: "공식 표기·최종 권장 수치. 명시되지 않은 공격력 상한을 추정하지 않는다."
- structured_value:

```json
{
  "explicit_ap_cap": null,
  "final_ap_recommended": 2340,
  "final_dp_recommended": 840,
  "knowledge_role": "fact",
  "launched_at": "2026-08-12",
  "sheet_ap_recommended": 410,
  "sheet_dp_recommended": 490
}
```

### `magaia-temple.trash-loot`

- seed_key: "magaia-temple.trash-loot"
- kind: "item"
- requirement_level: "optional"
- title: "공식 잡동사니"
- description: "잡동사니 NPC 가격과 확인된 무게."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "trash_item": "엘리언 추종자의 투구",
  "trash_npc_price": 181042
}
```

### `magaia-temple.patch-provenance`

- seed_key: "magaia-temple.patch-provenance"
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
  ],
  "update_2026_09_02": {
    "furnace_mechanic_order_changed": true
  }
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

### `magaia-temple.claim.current-stats::edania-internal-launch-2026-08-12`

- evidence_seed_key: "magaia-temple.claim.current-stats::edania-internal-launch-2026-08-12"
- source_id: "edania-internal-launch-2026-08-12"
- title: "8월 12일(수) 업데이트 안내 - 에다니아 내부 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "magaia-temple.current-stats"
- claim_key: "requirement:current-stats"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `magaia-temple.claim.patch-provenance::edania-internal-balance-2026-08-19`

- evidence_seed_key: "magaia-temple.claim.patch-provenance::edania-internal-balance-2026-08-19"
- source_id: "edania-internal-balance-2026-08-19"
- title: "8월 19일(수) 업데이트 안내 - 에다니아 내부 사냥터 조정"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16063"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-19"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "magaia-temple.patch-provenance"
- claim_key: "requirement:patch-provenance"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `magaia-temple.claim.patch-provenance::edania-internal-balance-2026-09-02`

- evidence_seed_key: "magaia-temple.claim.patch-provenance::edania-internal-balance-2026-09-02"
- source_id: "edania-internal-balance-2026-09-02"
- title: "9월 2일(수) 업데이트 안내 - 사건의 지평선 전리품 조정"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "magaia-temple.patch-provenance"
- claim_key: "requirement:patch-provenance"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `magaia-temple.claim.patch-provenance::edania-internal-launch-2026-08-12`

- evidence_seed_key: "magaia-temple.claim.patch-provenance::edania-internal-launch-2026-08-12"
- source_id: "edania-internal-launch-2026-08-12"
- title: "8월 12일(수) 업데이트 안내 - 에다니아 내부 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "magaia-temple.patch-provenance"
- claim_key: "requirement:patch-provenance"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `magaia-temple.claim.trash-loot::edania-internal-launch-2026-08-12`

- evidence_seed_key: "magaia-temple.claim.trash-loot::edania-internal-launch-2026-08-12"
- source_id: "edania-internal-launch-2026-08-12"
- title: "8월 12일(수) 업데이트 안내 - 에다니아 내부 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "magaia-temple.trash-loot"
- claim_key: "requirement:trash-loot"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
