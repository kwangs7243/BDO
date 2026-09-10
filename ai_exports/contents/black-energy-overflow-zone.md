<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 검은 기운 범람지

## Identity

- slug: "black-energy-overflow-zone"
- name_ko: "검은 기운 범람지"
- category: "combat"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "party"
- difficulty: "very_high"

## Overview

- summary: "에다니아 여러 지역에 분산된 3인 파티 사냥터."
- purpose: "상위 에다니아 사냥터로 가는 파티 성장 구간"

## Requirements

### `black-energy-overflow-zone.current-stats`

- seed_key: "black-energy-overflow-zone.current-stats"
- kind: "stat"
- requirement_level: "recommended"
- title: "현재 권장 수치"
- description: "표기 385/450, 최종 1850/760, 공격력 상한 1880."
- structured_value:

```json
{
  "ap_cap": 1880,
  "crowd_control": [
    "knockdown",
    "bound"
  ],
  "final_ap_recommended": 1850,
  "final_dp_recommended": 760,
  "initial_regions": [
    "Orbita",
    "Zephyros"
  ],
  "knowledge_role": "fact",
  "launched_at": "2026-03-18",
  "marni_realm_available": false,
  "party_size": 3,
  "sheet_ap_recommended": 385,
  "sheet_dp_recommended": 450
}
```

### `black-energy-overflow-zone.mechanic`

- seed_key: "black-energy-overflow-zone.mechanic"
- kind: "knowledge"
- requirement_level: "recommended"
- title: "검은 기운 원천 기믹"
- description: "검은 기운의 원천, 타락한 실패한 에다나, 지역 에다나 영향으로 구성된다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "mechanic": [
    "Black Energy Source",
    "corrupted failed Edanas",
    "regional Edana influence"
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

### `black-energy-overflow-zone.attack-cap`

- seed_key: "black-energy-overflow-zone.attack-cap"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "grind-zone-attack-cap"
- content_name_ko: "사냥터 공격력 제한"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/grind-zone-attack-cap.md"
### `black-energy-overflow-zone.orbita`

- seed_key: "black-energy-overflow-zone.orbita"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "orbita"
- content_name_ko: "오르비타 성"
- content_category: "combat"
- note: null
- order_no: 2
- relative_path: "../contents/orbita.md"
### `black-energy-overflow-zone.zephyros`

- seed_key: "black-energy-overflow-zone.zephyros"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "zephyros"
- content_name_ko: "제피로스 성"
- content_category: "combat"
- note: null
- order_no: 3
- relative_path: "../contents/zephyros.md"

## Evidence and Sources

### Current evidence

### `black-energy-overflow-zone.claim.current-stats::black-energy-overflow-2026-03-18`

- evidence_seed_key: "black-energy-overflow-zone.claim.current-stats::black-energy-overflow-2026-03-18"
- source_id: "black-energy-overflow-2026-03-18"
- title: "3월 18일(수) 업데이트 안내 - 검은 기운의 범람지"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15332"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-03-18"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "black-energy-overflow-zone.current-stats"
- claim_key: "requirement:current-stats"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `black-energy-overflow-zone.claim.mechanic::black-energy-overflow-2026-03-18`

- evidence_seed_key: "black-energy-overflow-zone.claim.mechanic::black-energy-overflow-2026-03-18"
- source_id: "black-energy-overflow-2026-03-18"
- title: "3월 18일(수) 업데이트 안내 - 검은 기운의 범람지"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15332"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-03-18"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "black-energy-overflow-zone.mechanic"
- claim_key: "requirement:mechanic"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
