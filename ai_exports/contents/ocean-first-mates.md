<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 대양 부선장

## Identity

- slug: "ocean-first-mates"
- name_ko: "대양 부선장"
- category: "ocean_guide"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "프라와·클레이아·트라난 언더포는 중범선 4종과 판옥선의 부선장 슬롯에 탑승한다."
- purpose: "부선장 공통 규칙과 세 부선장의 고용 조건·효과를 구분한다."

## Requirements

### `ocean-first-mates.common`

- seed_key: "ocean-first-mates.common"
- kind: "other"
- requirement_level: "required"
- title: "공통 규칙"
- description: "부선장은 중범선 4종과 판옥선 전용 슬롯에 탑승하고 선실을 차지하지 않으며, 함장 조종 중 대양 위치 확인·길 찾기를 제공한다. 병에 걸리면 효과가 중단되고 해고할 수 없다."
- structured_value:

```json
{
  "dismissible": false,
  "illness_disables_effect": true,
  "navigation_while_captain_controls": true,
  "ships": [
    "중범선 점진",
    "중범선 균형",
    "중범선 비상",
    "중범선 용맹",
    "판옥선"
  ],
  "uses_cabin": false
}
```

### `ocean-first-mates.praoa`

- seed_key: "ocean-first-mates.praoa"
- kind: "other"
- requirement_level: "required"
- title: "프라와"
- description: "[대양의 시대] 달의 눈, 칸의 심장을 찾아 완료 후 프라와의 연계 의뢰를 완료하면 고용하며, 지속시간이 향상된 쾌속순항 효과를 제공한다."
- structured_value:

```json
{
  "effect": "지속시간이 향상된 쾌속순항",
  "prerequisite": "[대양의 시대] 달의 눈, 칸의 심장을 찾아",
  "quests": [
    "[부선장] 재회",
    "[부선장] 만담",
    "[부선장] 마음에 따라"
  ]
}
```

### `ocean-first-mates.kleia`

- seed_key: "ocean-first-mates.kleia"
- kind: "other"
- requirement_level: "required"
- title: "클레이아"
- description: "돌발 물물교환에서 금빛 회중시계를 확률 획득한 뒤 연계 의뢰를 완료하면 고용하며, 물물교환 교섭력 소모를 10% 줄인다."
- structured_value:

```json
{
  "parley_reduction_percent": 10,
  "quests": [
    "[부선장] 추억",
    "[부선장] 결단",
    "[부선장] 새로운 무대를 향하여"
  ],
  "trigger": "돌발 물물교환 확률 획득",
  "trigger_item": "금빛 회중시계"
}
```

### `ocean-first-mates.tranan`

- seed_key: "ocean-first-mates.tranan"
- kind: "other"
- requirement_level: "required"
- title: "트라난 언더포"
- description: "바다 악어에게서 화려한 선수상을 확률 획득한 뒤 연계 의뢰를 완료하면 고용한다. 함장 운전 중 선박 가방에 수리 물품 3종 중 하나가 있으면 자동 수리를 사용할 수 있다."
- structured_value:

```json
{
  "quests": [
    "[부선장] 어느 모험가의 이야기",
    "[부선장] 간직해온 꿈",
    "[부선장] 설득"
  ],
  "repair_items": [
    "함선 수리 자재",
    "함선 수리 키트",
    "긴급 함선 수리 키트"
  ],
  "trigger": "바다 악어 확률 획득",
  "trigger_item": "화려한 선수상"
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `ocean-first-mates.no-cannon-fire`

- seed_key: "ocean-first-mates.no-cannon-fire"
- section_type: "notes"
- title: "부선장의 역할"
- order_no: 1

#### body_markdown

부선장은 선박을 직접 운전하거나 함포를 발사하는 별도 선원이 아니라 부선장 슬롯에서 고유 효과를 제공한다.

## Related Contents

### `ocean-first-mates.relation.roles`

- seed_key: "ocean-first-mates.relation.roles"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "sailor-role-slots"
- content_name_ko: "선원 역할 슬롯"
- content_category: "ocean_guide"
- note: "부선장 슬롯 규칙"
- order_no: 1
- relative_path: "../contents/sailor-role-slots.md"
### `ocean-first-mates.relation.sudden-barter`

- seed_key: "ocean-first-mates.relation.sudden-barter"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "barter-current-system"
- content_name_ko: "현행 물물교환 시스템"
- content_category: "ocean_barter"
- note: "클레이아 고용 재료 획득처"
- order_no: 2
- relative_path: "../contents/barter-current-system.md"
### `ocean-first-mates.relation.sea-crocodile`

- seed_key: "ocean-first-mates.relation.sea-crocodile"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sea-crocodile-hunting"
- content_name_ko: "바다 악어 사냥"
- content_category: "ocean_guide"
- note: "트라난 고용 재료 획득처"
- order_no: 3
- relative_path: "../contents/sea-crocodile-hunting.md"
### `khan-guild-boss.relation.oquilla`

- seed_key: "khan-guild-boss.relation.oquilla"
- direction: "incoming"
- relation_type: "related"
- content_slug: "khan-guild-boss"
- content_name_ko: "대양의 눈동자 칸"
- content_category: "ocean_guide"
- note: "오킬루아의 눈 접근과 대양 의뢰 흐름"
- order_no: 1
- relative_path: "../contents/khan-guild-boss.md"
### `sailor-role-slots.relation.first-mates`

- seed_key: "sailor-role-slots.relation.first-mates"
- direction: "incoming"
- relation_type: "related"
- content_slug: "sailor-role-slots"
- content_name_ko: "선원 역할 슬롯"
- content_category: "ocean_guide"
- note: "부선장 슬롯의 고유 효과를 별도 설명한다."
- order_no: 1
- relative_path: "../contents/sailor-role-slots.md"
### `sea-crocodile-hunting.relation.first-mates`

- seed_key: "sea-crocodile-hunting.relation.first-mates"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "sea-crocodile-hunting"
- content_name_ko: "바다 악어 사냥"
- content_category: "ocean_guide"
- note: "트라난 고용 재료 경로"
- order_no: 2
- relative_path: "../contents/sea-crocodile-hunting.md"

## Evidence and Sources

### Current evidence

### `ocean-first-mates.evidence.common::ocean-all-guide`

- evidence_seed_key: "ocean-first-mates.evidence.common::ocean-all-guide"
- source_id: "ocean-all-guide"
- title: "대양의 모든 것"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=243"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ocean-first-mates.common"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "부선장 공통 탑승·선실·질병·항법 규칙"
- active: true
- is_active: true

### `ocean-first-mates.evidence.common::ocean-crew-roles-2025`

- evidence_seed_key: "ocean-first-mates.evidence.common::ocean-crew-roles-2025"
- source_id: "ocean-crew-roles-2025"
- title: "부선장과 선원 관리 UI"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13697"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ocean-first-mates.common"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "부선장 공통 탑승·선실·질병·항법 규칙"
- active: true
- is_active: true

### `ocean-first-mates.evidence.kleia::ocean-crew-roles-2025`

- evidence_seed_key: "ocean-first-mates.evidence.kleia::ocean-crew-roles-2025"
- source_id: "ocean-crew-roles-2025"
- title: "부선장과 선원 관리 UI"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13697"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ocean-first-mates.kleia"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "클레이아 고용 조건과 교섭력 10% 감소"
- active: true
- is_active: true

### `ocean-first-mates.evidence.praoa::ocean-crew-roles-2025`

- evidence_seed_key: "ocean-first-mates.evidence.praoa::ocean-crew-roles-2025"
- source_id: "ocean-crew-roles-2025"
- title: "부선장과 선원 관리 UI"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13697"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ocean-first-mates.praoa"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "프라와 고용 의뢰와 효과"
- active: true
- is_active: true

### `ocean-first-mates.evidence.tranan::ocean-crew-roles-2025`

- evidence_seed_key: "ocean-first-mates.evidence.tranan::ocean-crew-roles-2025"
- source_id: "ocean-crew-roles-2025"
- title: "부선장과 선원 관리 UI"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13697"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ocean-first-mates.tranan"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "트라난 고용 조건과 자동 수리 준비물"
- active: true
- is_active: true

### Historical / inactive evidence

- None
