<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 사건의 지평선

## Identity

- slug: "event-horizon"
- name_ko: "사건의 지평선"
- category: "combat"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "extreme"

## Overview

- summary: "9월 2일 최신 조정을 반영한 에다니아 내부 최상위 사냥터."
- purpose: "에다니아 내부 최상위 전리품 획득"

## Requirements

### `event-horizon.current-stats`

- seed_key: "event-horizon.current-stats"
- kind: "stat"
- requirement_level: "recommended"
- title: "현재 권장 수치"
- description: "표기 420/505, 최종 2570/870. 공식 상한은 확인되지 않아 비워 둔다."
- structured_value:

```json
{
  "explicit_ap_cap": null,
  "final_ap_recommended": 2570,
  "final_dp_recommended": 870,
  "knowledge_role": "fact",
  "sheet_ap_recommended": 420,
  "sheet_dp_recommended": 505
}
```

### `event-horizon.current-2026-09-02`

- seed_key: "event-horizon.current-2026-09-02"
- kind: "item"
- requirement_level: "recommended"
- title: "2026-09-02 최신 전리품 수량"
- description: "9월 2일 이후 잡동사니 범위와 아그리스 소모량."
- structured_value:

```json
{
  "agris_costs": {
    "base_type": 18,
    "guide_of_despair": 36,
    "ibedor": 180,
    "special_lost_object": 198
  },
  "effective_from": "2026-09-02",
  "knowledge_role": "fact",
  "major_loot": [
    "강 떠도는 근원의 수정",
    "강 근원의 결정",
    "이닉스의 불티 - 신발",
    "이닉스의 불티 - 장갑",
    "이닉스의 불티 - 갑옷",
    "이닉스의 불티 - 투구",
    "아페론 귀걸이",
    "아페론 반지"
  ],
  "rare_loot_probability_redistributed": true,
  "trash_item": "부서진 공허의 장갑",
  "trash_npc_price": 196501,
  "trash_ranges": {
    "corrupted_edana_or_lost_object": [
      2,
      4
    ],
    "guide_of_despair": [
      4,
      8
    ],
    "ibedor": [
      25,
      35
    ],
    "special_lost_object": [
      30,
      35
    ]
  },
  "trash_weight_lt": 0.3
}
```

### `event-horizon.measurement-policy`

- seed_key: "event-horizon.measurement-policy"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "측정 최신성 정책"
- description: "9월 2일 이전 시간당 수익 측정은 historical로만 보존하고 현재 비교에서 제외한다."
- structured_value:

```json
{
  "current_as_of": "2026-09-04",
  "knowledge_role": "strategy",
  "reject_pre_2026_09_02_from_current_profit": true,
  "tags": [
    "patch_window_sensitive",
    "market_value_dynamic"
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

### `event-horizon.claim.current-2026-09-02::edania-internal-balance-2026-09-02`

- evidence_seed_key: "event-horizon.claim.current-2026-09-02::edania-internal-balance-2026-09-02"
- source_id: "edania-internal-balance-2026-09-02"
- title: "9월 2일(수) 업데이트 안내 - 사건의 지평선 전리품 조정"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "event-horizon.current-2026-09-02"
- claim_key: "requirement:current-2026-09-02"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `event-horizon.claim.current-2026-09-02::edania-internal-launch-2026-08-12`

- evidence_seed_key: "event-horizon.claim.current-2026-09-02::edania-internal-launch-2026-08-12"
- source_id: "edania-internal-launch-2026-08-12"
- title: "8월 12일(수) 업데이트 안내 - 에다니아 내부 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "event-horizon.current-2026-09-02"
- claim_key: "requirement:current-2026-09-02"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `event-horizon.claim.current-stats::edania-internal-launch-2026-08-12`

- evidence_seed_key: "event-horizon.claim.current-stats::edania-internal-launch-2026-08-12"
- source_id: "edania-internal-launch-2026-08-12"
- title: "8월 12일(수) 업데이트 안내 - 에다니아 내부 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "event-horizon.current-stats"
- claim_key: "requirement:current-stats"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `event-horizon.claim.measurement-policy::edania-internal-balance-2026-09-02`

- evidence_seed_key: "event-horizon.claim.measurement-policy::edania-internal-balance-2026-09-02"
- source_id: "edania-internal-balance-2026-09-02"
- title: "9월 2일(수) 업데이트 안내 - 사건의 지평선 전리품 조정"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "event-horizon.measurement-policy"
- claim_key: "requirement:measurement-policy"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

### `event-horizon.claim.legacy-launch-values::edania-internal-launch-2026-08-12`

- evidence_seed_key: "event-horizon.claim.legacy-launch-values::edania-internal-launch-2026-08-12"
- source_id: "edania-internal-launch-2026-08-12"
- title: "8월 12일(수) 업데이트 안내 - 에다니아 내부 사냥터"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "event-horizon.legacy-launch-values"
- claim_key: "requirement:legacy-launch-values"
- verification_status: "superseded"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: false
- is_active: false
