<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 아프로돈 신전

## Identity

- slug: "aphrodon-temple"
- name_ko: "아프로돈 신전"
- category: "combat"
- status: "active"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "extreme"

## Overview

- summary: "2026-08-12 추가된 에다니아 내부 사냥터."
- purpose: "에다니아 내부 성장 및 전리품 획득"

## Requirements

### `aphrodon-temple.current-stats`

- seed_key: "aphrodon-temple.current-stats"
- kind: "stat"
- requirement_level: "recommended"
- title: "현재 권장 수치"
- description: "공식 표기·최종 권장 수치. 명시되지 않은 공격력 상한을 추정하지 않는다."
- structured_value:

```json
{
  "explicit_ap_cap": null,
  "final_ap_recommended": 2090,
  "final_dp_recommended": 810,
  "knowledge_role": "fact",
  "launched_at": "2026-08-12",
  "sheet_ap_recommended": 400,
  "sheet_dp_recommended": 470
}
```

### `aphrodon-temple.trash-loot`

- seed_key: "aphrodon-temple.trash-loot"
- kind: "item"
- requirement_level: "optional"
- title: "공식 잡동사니"
- description: "잡동사니 NPC 가격과 확인된 무게."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "trash_item": "풍요 깃든 가지",
  "trash_npc_price": 155127,
  "trash_weight_lt": 0.3
}
```

### `aphrodon-temple.patch-provenance`

- seed_key: "aphrodon-temple.patch-provenance"
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

### `aphrodon-temple.measurement-launch`

- seed_key: "aphrodon-temple.measurement-launch"
- kind: "other"
- requirement_level: "optional"
- title: "출시 주간 커뮤니티 측정"
- description: "시간당 성능값으로 환산하지 않는 기믹·드롭 구성 참고 기록."
- structured_value:

```json
{
  "allowed_use": [
    "mechanic_corroboration",
    "drop_composition"
  ],
  "class_known": false,
  "freshness": "pre_balance_patch",
  "hourly_performance_allowed": false,
  "knowledge_role": "measurement",
  "measured_at": "2026-08-12",
  "measurement_grade": "B",
  "reported_final_ap_max": 2140,
  "reported_final_ap_min": 2100,
  "reported_test_duration_minutes": 120,
  "scope": "individual_reports",
  "second_session": {
    "accumulated_trash": 100000,
    "agris_consumed_total": 20000,
    "duration_complete": false,
    "mobs_killed_approx": 18000,
    "reported_final_ap": 2105
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

### `aphrodon-temple.claim.current-stats::edania-internal-launch-2026-08-12`

- evidence_seed_key: "aphrodon-temple.claim.current-stats::edania-internal-launch-2026-08-12"
- source_id: "edania-internal-launch-2026-08-12"
- title: "8월 12일(수) 업데이트 안내 - 에다니아 내부 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "aphrodon-temple.current-stats"
- claim_key: "requirement:current-stats"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `aphrodon-temple.claim.measurement-launch::v17b-provided-measurement-pack-2026-09-04`

- evidence_seed_key: "aphrodon-temple.claim.measurement-launch::v17b-provided-measurement-pack-2026-09-04"
- source_id: "v17b-provided-measurement-pack-2026-09-04"
- title: "V1.7B Grind Spot Deep Pack - provided measurement records"
- url: "attachment://b902d37c-2b3b-4e3e-b4f3-7c1ccf094a0c/pasted-text.txt"
- publisher: "User-provided research pack"
- source_type: "community_measurement"
- published_at: "2026-09-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "aphrodon-temple.measurement-launch"
- claim_key: "requirement:measurement-launch"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `aphrodon-temple.claim.patch-provenance::edania-internal-balance-2026-08-19`

- evidence_seed_key: "aphrodon-temple.claim.patch-provenance::edania-internal-balance-2026-08-19"
- source_id: "edania-internal-balance-2026-08-19"
- title: "8월 19일(수) 업데이트 안내 - 에다니아 내부 사냥터 조정"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16063"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-19"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "aphrodon-temple.patch-provenance"
- claim_key: "requirement:patch-provenance"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `aphrodon-temple.claim.patch-provenance::edania-internal-launch-2026-08-12`

- evidence_seed_key: "aphrodon-temple.claim.patch-provenance::edania-internal-launch-2026-08-12"
- source_id: "edania-internal-launch-2026-08-12"
- title: "8월 12일(수) 업데이트 안내 - 에다니아 내부 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "aphrodon-temple.patch-provenance"
- claim_key: "requirement:patch-provenance"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `aphrodon-temple.claim.trash-loot::edania-internal-launch-2026-08-12`

- evidence_seed_key: "aphrodon-temple.claim.trash-loot::edania-internal-launch-2026-08-12"
- source_id: "edania-internal-launch-2026-08-12"
- title: "8월 12일(수) 업데이트 안내 - 에다니아 내부 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "aphrodon-temple.trash-loot"
- claim_key: "requirement:trash-loot"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
