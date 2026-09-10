<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 바다 악어 사냥

## Identity

- slug: "sea-crocodile-hunting"
- name_ko: "바다 악어 사냥"
- category: "ocean_guide"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "바다 악어 사냥은 에벤루스의 놀과 트라난 부선장 고용 재료의 획득 경로다."
- purpose: "현재 사냥터 위치와 두 희귀 재료의 용도를 연결한다."

## Requirements

### `sea-crocodile-hunting.location`

- seed_key: "sea-crocodile-hunting.location"
- kind: "other"
- requirement_level: "required"
- title: "현재 사냥터"
- description: "2026-08-26 업데이트로 바다 악어 사냥터가 청사 섬 위쪽으로 이동했다."
- structured_value:

```json
{
  "effective_from": "2026-08-26",
  "region": "청사 섬 위쪽"
}
```

### `sea-crocodile-hunting.moss-map`

- seed_key: "sea-crocodile-hunting.moss-map"
- kind: "other"
- requirement_level: "required"
- title: "이끼에 뒤덮인 지도"
- description: "바다 악어 사냥에서 문양이 새겨진 놀 제작 경로의 이끼에 뒤덮인 지도를 획득한다."
- structured_value:

```json
{
  "item": "이끼에 뒤덮인 지도",
  "use": "문양이 새겨진 놀 제작 경로"
}
```

### `sea-crocodile-hunting.figurehead`

- seed_key: "sea-crocodile-hunting.figurehead"
- kind: "other"
- requirement_level: "required"
- title: "화려한 선수상"
- description: "바다 악어에게서 지정 확률로 화려한 선수상을 획득하며 트라난 언더포 고용 의뢰를 연다."
- structured_value:

```json
{
  "acquisition": "지정 확률",
  "item": "화려한 선수상",
  "use": "트라난 언더포 고용"
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

### `sea-crocodile-hunting.relation.ebenruth`

- seed_key: "sea-crocodile-hunting.relation.ebenruth"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "ebenruth-nol"
- content_name_ko: "에벤루스의 놀"
- content_category: "ocean_guide"
- note: "문양이 새겨진 놀 재료 경로"
- order_no: 1
- relative_path: "../contents/ebenruth-nol.md"
### `sea-crocodile-hunting.relation.first-mates`

- seed_key: "sea-crocodile-hunting.relation.first-mates"
- direction: "outgoing"
- relation_type: "source_for"
- content_slug: "ocean-first-mates"
- content_name_ko: "대양 부선장"
- content_category: "ocean_guide"
- note: "트라난 고용 재료 경로"
- order_no: 2
- relative_path: "../contents/ocean-first-mates.md"
### `sea-crocodile-hunting.relation.rinbach`

- seed_key: "sea-crocodile-hunting.relation.rinbach"
- direction: "outgoing"
- relation_type: "alternative"
- content_slug: "rinbach-colony"
- content_name_ko: "린바크 군락지"
- content_category: "ocean_combat"
- note: "린바크 추가로 사냥터가 청사 섬 위쪽으로 이동"
- order_no: 3
- relative_path: "../contents/rinbach-colony.md"
### `ebenruth-nol.relation.sea-crocodile`

- seed_key: "ebenruth-nol.relation.sea-crocodile"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "ebenruth-nol"
- content_name_ko: "에벤루스의 놀"
- content_category: "ocean_guide"
- note: "문양이 새겨진 놀 재료 획득처"
- order_no: 1
- relative_path: "../contents/ebenruth-nol.md"
### `ocean-first-mates.relation.sea-crocodile`

- seed_key: "ocean-first-mates.relation.sea-crocodile"
- direction: "incoming"
- relation_type: "related"
- content_slug: "ocean-first-mates"
- content_name_ko: "대양 부선장"
- content_category: "ocean_guide"
- note: "트라난 고용 재료 획득처"
- order_no: 3
- relative_path: "../contents/ocean-first-mates.md"
### `sailing-onboarding-strategy.ocean-hunting`

- seed_key: "sailing-onboarding-strategy.ocean-hunting"
- direction: "incoming"
- relation_type: "related"
- content_slug: "sailing-onboarding-strategy"
- content_name_ko: "항해 입문 운영 전략"
- content_category: "ocean_guide"
- note: "해양 사냥 목적"
- order_no: 9
- relative_path: "../contents/sailing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `sea-crocodile-hunting.evidence.figurehead::ocean-crew-roles-2025`

- evidence_seed_key: "sea-crocodile-hunting.evidence.figurehead::ocean-crew-roles-2025"
- source_id: "ocean-crew-roles-2025"
- title: "부선장과 선원 관리 UI"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13697"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sea-crocodile-hunting.figurehead"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "화려한 선수상과 트라난 고용"
- active: true
- is_active: true

### `sea-crocodile-hunting.evidence.location::ocean-progression-2026-08-26`

- evidence_seed_key: "sea-crocodile-hunting.evidence.location::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sea-crocodile-hunting.location"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "청사 섬 위쪽으로 사냥터 이동"
- active: true
- is_active: true

### `sea-crocodile-hunting.evidence.moss-map::treasure-items-guide`

- evidence_seed_key: "sea-crocodile-hunting.evidence.moss-map::treasure-items-guide"
- source_id: "treasure-items-guide"
- title: "보물 아이템 만들기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=194"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sea-crocodile-hunting.moss-map"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "이끼에 뒤덮인 지도 획득처"
- active: true
- is_active: true

### Historical / inactive evidence

- None
