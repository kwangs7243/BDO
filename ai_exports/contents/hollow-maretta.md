<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 공허한 마레타

## Identity

- slug: "hollow-maretta"
- name_ko: "공허한 마레타"
- category: "ocean_guide"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "마고리아에서 선율과 서버 알림으로 위치를 찾는 해양 괴수이며 사망 1시간 뒤 다시 등장한다."
- purpose: "현재 출현 간격과 전리품 연결을 과거 규칙과 구분한다."

## Requirements

### `hollow-maretta.location-signal`

- seed_key: "hollow-maretta.location-signal"
- kind: "other"
- requirement_level: "required"
- title: "탐색 신호"
- description: "마고리아에서 선율과 알림 메시지를 이용해 공허한 마레타의 위치를 찾는다."
- structured_value:

```json
{
  "region": "마고리아",
  "signals": [
    "선율",
    "서버 알림 메시지"
  ]
}
```

### `hollow-maretta.respawn-current`

- seed_key: "hollow-maretta.respawn-current"
- kind: "other"
- requirement_level: "required"
- title: "현재 재등장"
- description: "사망 후 1시간 뒤 다시 등장한다."
- structured_value:

```json
{
  "hours_after_death": 1
}
```

### `hollow-maretta.loot`

- seed_key: "hollow-maretta.loot"
- kind: "other"
- requirement_level: "required"
- title: "주요 전리품"
- description: "선율이 맴도는 기운은 1개를 확정 획득하며, 2026-08-26 이후 대양의 정수 획득처이기도 하다."
- structured_value:

```json
{
  "current_drop": "대양의 정수",
  "guaranteed": {
    "선율이 맴도는 기운": 1
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

### `hollow-maretta.relation.sea-crystals`

- seed_key: "hollow-maretta.relation.sea-crystals"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sea-crystals"
- content_name_ko: "해원석 progression"
- content_category: "ocean_project"
- note: "선율이 맴도는 기운의 해원석 제작 연결"
- order_no: 1
- relative_path: "../contents/sea-crystals.md"
### `hollow-maretta.relation.consumables`

- seed_key: "hollow-maretta.relation.consumables"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "ocean-consumables"
- content_name_ko: "현행 항해·교역 소비품"
- content_category: "ocean_guide"
- note: "대양의 정수 획득처"
- order_no: 2
- relative_path: "../contents/ocean-consumables.md"
### `hollow-maretta.relation.rinbach`

- seed_key: "hollow-maretta.relation.rinbach"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "rinbach-colony"
- content_name_ko: "린바크 군락지"
- content_category: "ocean_combat"
- note: "대양의 정수의 다른 획득 경로"
- order_no: 3
- relative_path: "../contents/rinbach-colony.md"

## Evidence and Sources

### Current evidence

### `hollow-maretta.evidence.location-signal::hollow-maretta-update-2023-11-22`

- evidence_seed_key: "hollow-maretta.evidence.location-signal::hollow-maretta-update-2023-11-22"
- source_id: "hollow-maretta-update-2023-11-22"
- title: "11월 22일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11292"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-11-22"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "hollow-maretta.location-signal"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "마고리아 선율과 서버 알림"
- active: true
- is_active: true

### `hollow-maretta.evidence.location-signal::ocean-all-guide`

- evidence_seed_key: "hollow-maretta.evidence.location-signal::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "hollow-maretta.location-signal"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "마고리아 선율과 서버 알림"
- active: true
- is_active: true

### `hollow-maretta.evidence.loot::hollow-maretta-update-2023-11-22`

- evidence_seed_key: "hollow-maretta.evidence.loot::hollow-maretta-update-2023-11-22"
- source_id: "hollow-maretta-update-2023-11-22"
- title: "11월 22일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11292"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-11-22"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "hollow-maretta.loot"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "선율이 맴도는 기운 확정 1개와 대양의 정수 획득처"
- active: true
- is_active: true

### `hollow-maretta.evidence.loot::ocean-progression-2026-08-26`

- evidence_seed_key: "hollow-maretta.evidence.loot::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "hollow-maretta.loot"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "선율이 맴도는 기운 확정 1개와 대양의 정수 획득처"
- active: true
- is_active: true

### `hollow-maretta.evidence.respawn-current::hollow-maretta-update-2023-11-22`

- evidence_seed_key: "hollow-maretta.evidence.respawn-current::hollow-maretta-update-2023-11-22"
- source_id: "hollow-maretta-update-2023-11-22"
- title: "11월 22일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11292"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-11-22"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "hollow-maretta.respawn-current"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "사망 후 1시간 재등장"
- active: true
- is_active: true

### Historical / inactive evidence

### `hollow-maretta.evidence.respawn-old::hollow-maretta-update-2023-11-22`

- evidence_seed_key: "hollow-maretta.evidence.respawn-old::hollow-maretta-update-2023-11-22"
- source_id: "hollow-maretta-update-2023-11-22"
- title: "11월 22일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=11292"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-11-22"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "hollow-maretta.respawn-old"
- claim_key: "structured_value"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "변경 전 1~5시간 재등장"
- active: false
- is_active: false
