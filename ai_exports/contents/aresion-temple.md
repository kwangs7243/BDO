<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 아레시온 신전

## Identity

- slug: "aresion-temple"
- name_ko: "아레시온 신전"
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

### `aresion-temple.current-stats`

- seed_key: "aresion-temple.current-stats"
- kind: "stat"
- requirement_level: "recommended"
- title: "현재 권장 수치"
- description: "공식 표기·최종 권장 수치. 명시되지 않은 공격력 상한을 추정하지 않는다."
- structured_value:

```json
{
  "explicit_ap_cap": null,
  "final_ap_recommended": 2455,
  "final_dp_recommended": 850,
  "knowledge_role": "fact",
  "launched_at": "2026-08-12",
  "sheet_ap_recommended": 415,
  "sheet_dp_recommended": 495
}
```

### `aresion-temple.trash-loot`

- seed_key: "aresion-temple.trash-loot"
- kind: "item"
- requirement_level: "optional"
- title: "공식 잡동사니"
- description: "잡동사니 NPC 가격과 확인된 무게."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "trash_item": "그을린 허리띠 장식",
  "trash_npc_price": 182049
}
```

### `aresion-temple.patch-provenance`

- seed_key: "aresion-temple.patch-provenance"
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

### `aresion-temple.measurement-2026-08-31`

- seed_key: "aresion-temple.measurement-2026-08-31"
- kind: "other"
- requirement_level: "optional"
- title: "2026-08-31 커뮤니티 측정"
- description: "제한된 표본의 동적 경제 기록이며 공식 기대 수익이 아니다."
- structured_value:

```json
{
  "class_known": false,
  "freshness": "current",
  "knowledge_role": "measurement",
  "market_value_dynamic": true,
  "measured_at": "2026-08-31",
  "measurement_grade": "B",
  "reported_final_ap_min": 2485,
  "reported_rare_twilight_items_per_hour_max": 3,
  "reported_rare_twilight_items_per_hour_min": 2,
  "reported_trash_silver_per_hour_max": 2700000000,
  "reported_trash_silver_per_hour_min": 2600000000,
  "scope": "limited_aggregate_by_one_reporter",
  "sheet_ap_min": 413,
  "total_observation_hours_approx": 10
}
```

### `aresion-temple.economy-context`

- seed_key: "aresion-temple.economy-context"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "수익 비교의 시점 의존성"
- description: "시간당 은화는 거래소 가격·세금·희귀 전리품 평가에 따라 변하므로 영구 사실로 사용하지 않는다."
- structured_value:

```json
{
  "current_as_of": "2026-09-04",
  "knowledge_role": "strategy",
  "tags": [
    "market_value_dynamic",
    "patch_window_sensitive"
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

### `aresion-temple.claim.current-stats::edania-internal-launch-2026-08-12`

- evidence_seed_key: "aresion-temple.claim.current-stats::edania-internal-launch-2026-08-12"
- source_id: "edania-internal-launch-2026-08-12"
- title: "8월 12일(수) 업데이트 안내 - 에다니아 내부 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "aresion-temple.current-stats"
- claim_key: "requirement:current-stats"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `aresion-temple.claim.economy-context::silver-at-1600ap-2026-08-14`

- evidence_seed_key: "aresion-temple.claim.economy-context::silver-at-1600ap-2026-08-14"
- source_id: "silver-at-1600ap-2026-08-14"
- title: "Silver per hour at 1600 AP discussion"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1volo6a/silver_per_hour_at_1600ap/"
- publisher: "Reddit r/blackdesertonline"
- source_type: "community_strategy"
- published_at: "2026-08-14"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "GLOBAL"
- entity_type: "content"
- entity_id: "aresion-temple.economy-context"
- claim_key: "requirement:economy-context"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `aresion-temple.claim.measurement-2026-08-31::v17b-provided-measurement-pack-2026-09-04`

- evidence_seed_key: "aresion-temple.claim.measurement-2026-08-31::v17b-provided-measurement-pack-2026-09-04"
- source_id: "v17b-provided-measurement-pack-2026-09-04"
- title: "V1.7B Grind Spot Deep Pack - provided measurement records"
- url: "attachment://b902d37c-2b3b-4e3e-b4f3-7c1ccf094a0c/pasted-text.txt"
- publisher: "User-provided research pack"
- source_type: "community_measurement"
- published_at: "2026-09-04"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "aresion-temple.measurement-2026-08-31"
- claim_key: "requirement:measurement-2026-08-31"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `aresion-temple.claim.patch-provenance::edania-internal-balance-2026-08-19`

- evidence_seed_key: "aresion-temple.claim.patch-provenance::edania-internal-balance-2026-08-19"
- source_id: "edania-internal-balance-2026-08-19"
- title: "8월 19일(수) 업데이트 안내 - 에다니아 내부 사냥터 조정"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16063"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-19"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "aresion-temple.patch-provenance"
- claim_key: "requirement:patch-provenance"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `aresion-temple.claim.patch-provenance::edania-internal-launch-2026-08-12`

- evidence_seed_key: "aresion-temple.claim.patch-provenance::edania-internal-launch-2026-08-12"
- source_id: "edania-internal-launch-2026-08-12"
- title: "8월 12일(수) 업데이트 안내 - 에다니아 내부 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "aresion-temple.patch-provenance"
- claim_key: "requirement:patch-provenance"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `aresion-temple.claim.trash-loot::edania-internal-launch-2026-08-12`

- evidence_seed_key: "aresion-temple.claim.trash-loot::edania-internal-launch-2026-08-12"
- source_id: "edania-internal-launch-2026-08-12"
- title: "8월 12일(수) 업데이트 안내 - 에다니아 내부 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "aresion-temple.trash-loot"
- claim_key: "requirement:trash-loot"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
