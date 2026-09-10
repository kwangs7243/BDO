<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 선원 역할 슬롯

## Identity

- slug: "sailor-role-slots"
- name_ko: "선원 역할 슬롯"
- category: "ocean_guide"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "중범선과 판옥선은 부선장·돛·조타·함포·주방·갑판·선실 역할 슬롯을 사용한다."
- purpose: "선원 능력치가 실제로 적용되는 슬롯과 자동 배치 우선순위를 확인한다."

## Requirements

### `sailor-role-slots.effects`

- seed_key: "sailor-role-slots.effects"
- kind: "other"
- requirement_level: "required"
- title: "역할별 효과"
- description: "역할 슬롯마다 두 배 적용 능력치 또는 선실 기반 선박 보너스가 다르다."
- structured_value:

```json
{
  "cabin": "선원 기본 능력치",
  "cannon": {
    "multiplier": 2,
    "stats": [
      "집중",
      "박력",
      "시야"
    ]
  },
  "deck": {
    "durability_per_cabin": 10000
  },
  "first_mate": "부선장 고유 효과",
  "galley": {
    "food_per_cabin": 5000
  },
  "helm": {
    "multiplier": 2,
    "stats": [
      "감각",
      "완력"
    ]
  },
  "sail": {
    "multiplier": 2,
    "stats": [
      "끈기",
      "눈치"
    ]
  }
}
```

### `sailor-role-slots.extra-slots`

- seed_key: "sailor-role-slots.extra-slots"
- kind: "other"
- requirement_level: "required"
- title: "선박별 추가 슬롯"
- description: "중범선 종류와 판옥선은 지정된 역할 슬롯을 추가로 가진다."
- structured_value:

```json
{
  "균형": {
    "sail": 1
  },
  "비상": {
    "sail": 1
  },
  "용맹": {
    "cannon": 1
  },
  "점진": {
    "galley": 1
  },
  "판옥선": {
    "cannon": 2
  }
}
```

### `sailor-role-slots.auto-placement`

- seed_key: "sailor-role-slots.auto-placement"
- kind: "other"
- requirement_level: "required"
- title: "자동 배치 우선순위"
- description: "자동 배치는 부선장, 돛, 조타, 함포, 주방, 갑판, 선실 순서다."
- structured_value:

```json
[
  "부선장",
  "돛",
  "조타",
  "함포",
  "주방",
  "갑판",
  "선실"
]
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

### `sailor-role-slots.relation.first-mates`

- seed_key: "sailor-role-slots.relation.first-mates"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "ocean-first-mates"
- content_name_ko: "대양 부선장"
- content_category: "ocean_guide"
- note: "부선장 슬롯의 고유 효과를 별도 설명한다."
- order_no: 1
- relative_path: "../contents/ocean-first-mates.md"
### `sailor-role-slots.relation.panokseon`

- seed_key: "sailor-role-slots.relation.panokseon"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "panokseon"
- content_name_ko: "판옥선"
- content_category: "ocean_guide"
- note: "판옥선은 함포 슬롯 2칸이 추가된다."
- order_no: 2
- relative_path: "../contents/panokseon.md"
### `carrack-sailor-fishing.relation.roles`

- seed_key: "carrack-sailor-fishing.relation.roles"
- direction: "incoming"
- relation_type: "related"
- content_slug: "carrack-sailor-fishing"
- content_name_ko: "중범선 선원 낚시"
- content_category: "ocean_guide"
- note: "낚시 선원 전용 슬롯"
- order_no: 1
- relative_path: "../contents/carrack-sailor-fishing.md"
### `ocean-first-mates.relation.roles`

- seed_key: "ocean-first-mates.relation.roles"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "ocean-first-mates"
- content_name_ko: "대양 부선장"
- content_category: "ocean_guide"
- note: "부선장 슬롯 규칙"
- order_no: 1
- relative_path: "../contents/ocean-first-mates.md"
### `panokseon.relation.roles`

- seed_key: "panokseon.relation.roles"
- direction: "incoming"
- relation_type: "related"
- content_slug: "panokseon"
- content_name_ko: "판옥선"
- content_category: "ocean_guide"
- note: "판옥선 함포 역할 슬롯 2칸 추가"
- order_no: 1
- relative_path: "../contents/panokseon.md"
### `sailor-hiring-growth.relation.roles`

- seed_key: "sailor-hiring-growth.relation.roles"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "sailor-hiring-growth"
- content_name_ko: "선원 고용과 성장"
- content_category: "ocean_guide"
- note: "성장한 선원을 역할 슬롯에 배치한다."
- order_no: 1
- relative_path: "../contents/sailor-hiring-growth.md"
### `sailing-onboarding-strategy.sailor-roles`

- seed_key: "sailing-onboarding-strategy.sailor-roles"
- direction: "incoming"
- relation_type: "related"
- content_slug: "sailing-onboarding-strategy"
- content_name_ko: "항해 입문 운영 전략"
- content_category: "ocean_guide"
- note: "목적별 선원 역할과 선실"
- order_no: 3
- relative_path: "../contents/sailing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `sailor-role-slots.evidence.auto-placement::ocean-crew-roles-2025`

- evidence_seed_key: "sailor-role-slots.evidence.auto-placement::ocean-crew-roles-2025"
- source_id: "ocean-crew-roles-2025"
- title: "부선장과 선원 관리 UI"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13697"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailor-role-slots.auto-placement"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "자동 배치 우선순위"
- active: true
- is_active: true

### `sailor-role-slots.evidence.effects::ocean-crew-roles-2025`

- evidence_seed_key: "sailor-role-slots.evidence.effects::ocean-crew-roles-2025"
- source_id: "ocean-crew-roles-2025"
- title: "부선장과 선원 관리 UI"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13697"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailor-role-slots.effects"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "역할 슬롯별 적용 능력치"
- active: true
- is_active: true

### `sailor-role-slots.evidence.extra-slots::ocean-crew-roles-2025`

- evidence_seed_key: "sailor-role-slots.evidence.extra-slots::ocean-crew-roles-2025"
- source_id: "ocean-crew-roles-2025"
- title: "부선장과 선원 관리 UI"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13697"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "sailor-role-slots.extra-slots"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "선박별 추가 역할 슬롯"
- active: true
- is_active: true

### Historical / inactive evidence

- None
