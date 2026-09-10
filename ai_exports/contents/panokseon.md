<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 판옥선

## Identity

- slug: "panokseon"
- name_ko: "판옥선"
- category: "ocean_guide"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "판옥선은 중범선과 별개의 느리고 무거운 전투·다선원 운용 선박으로 높은 방어력과 충각 피해를 지향한다."
- purpose: "판옥선의 성격, 기본 능력치, 제작소와 선체 재료를 확인한다."

## Requirements

### `panokseon.identity`

- seed_key: "panokseon.identity"
- kind: "other"
- requirement_level: "required"
- title: "운용 성격"
- description: "판옥선은 중범선의 상·하위가 아닌 별도 분기다. 일반 성능은 중범선보다 낮지만 많은 선원, 높은 방어력과 충각 피해를 활용하는 전투형 선박이다."
- structured_value:

```json
{
  "branch": "distinct_from_carrack",
  "traits": [
    "느리고 무거움",
    "다선원 운용",
    "높은 방어력",
    "높은 충각 피해",
    "전투 지향"
  ]
}
```

### `panokseon.base-stats`

- seed_key: "panokseon.base-stats"
- kind: "other"
- requirement_level: "required"
- title: "기본 능력치"
- description: "판옥선 기본 능력치다."
- structured_value:

```json
{
  "acceleration_percent": 100,
  "braking_percent": 115,
  "cabin": 150,
  "cannon_cooldown_seconds": 13,
  "cannonballs": 2000,
  "cannons_per_side": 9,
  "durability": 2000000,
  "food": 1300000,
  "inventory_slots": 20,
  "speed_percent": 105,
  "turning_percent": 110,
  "weight_lt": 12500
}
```

### `panokseon.shipyards`

- seed_key: "panokseon.shipyards"
- kind: "other"
- requirement_level: "required"
- title: "제작소"
- description: "남포 무들마을 4번지 조선소 1단계 또는 청사 섬 1번지 조선소 1단계에서 제작한다."
- structured_value:

```json
[
  "남포 무들마을 4번지 조선소 1단계",
  "청사 섬 1번지 조선소 1단계"
]
```

### `panokseon.materials`

- seed_key: "panokseon.materials"
- kind: "other"
- requirement_level: "required"
- title: "선체 제작 재료"
- description: "도면 30개, 바닷물을 머금은 나무못 250개, 정교하게 다듬어진 소나무 합판 300개, 짙은 파도의 흔적이 담긴 접착제 200개가 필요하다."
- structured_value:

```json
{
  "도면 : 판옥선": 30,
  "바닷물을 머금은 나무못": 250,
  "정교하게 다듬어진 소나무 합판": 300,
  "짙은 파도의 흔적이 담긴 접착제": 200
}
```

### `panokseon.material-sources`

- seed_key: "panokseon.material-sources"
- kind: "other"
- requirement_level: "required"
- title: "재료 획득"
- description: "도면은 [주간] 가로막는 해적들에서 2개, 나무못은 골드몬트 소·중·대형 전투함, 합판은 유안에게 상평통보 10개당 1개, 접착제는 까마귀 주화 상점 500개당 1개다."
- structured_value:

```json
{
  "adhesive_exchange": {
    "output": 1,
    "까마귀 주화": 500
  },
  "blueprint_weekly_reward": 2,
  "minimum_weekly_completions": 15,
  "nail_source": [
    "골드몬트 소형 전투함",
    "골드몬트 중형 전투함",
    "골드몬트 대형 전투함"
  ],
  "plywood_exchange": {
    "npc": "유안",
    "output": 1,
    "상평통보": 10
  }
}
```

## Steps

### `panokseon.step.weekly-blueprints`

- seed_key: "panokseon.step.weekly-blueprints"
- phase: "repeat"
- order_no: 1
- title: "판옥선 도면 주간 의뢰"
- description: "[주간] 가로막는 해적들을 완료해 도면 2개를 모은다."
- checkable: true

## Schedules

### `panokseon.weekly-reset`

- seed_key: "panokseon.weekly-reset"
- rule_type: "quest_reset"
- recurrence_type: "weekly"
- weekday: 3
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "일반 주간 의뢰 목요일 00:00 KST 초기화"

## Rewards

- None

## Sections

- None

## Related Contents

### `panokseon.relation.roles`

- seed_key: "panokseon.relation.roles"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sailor-role-slots"
- content_name_ko: "선원 역할 슬롯"
- content_category: "ocean_guide"
- note: "판옥선 함포 역할 슬롯 2칸 추가"
- order_no: 1
- relative_path: "../contents/sailor-role-slots.md"
### `panokseon.relation.green-blue-gear`

- seed_key: "panokseon.relation.green-blue-gear"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "panokseon-haemo-byeokgye"
- content_name_ko: "판옥선 해모·벽계 장비"
- content_category: "ocean_guide"
- note: "판옥선 해모·벽계 장비 진행"
- order_no: 2
- relative_path: "../contents/panokseon-haemo-byeokgye.md"
### `panokseon.relation.weekly-framework`

- seed_key: "panokseon.relation.weekly-framework"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "weekly-quest-framework"
- content_name_ko: "주간 의뢰 공통 규칙"
- content_category: "system"
- note: "도면 주간 의뢰 초기화"
- order_no: 3
- relative_path: "../contents/weekly-quest-framework.md"
### `panokseon-haemo-byeokgye.relation.panokseon`

- seed_key: "panokseon-haemo-byeokgye.relation.panokseon"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "panokseon-haemo-byeokgye"
- content_name_ko: "판옥선 해모·벽계 장비"
- content_category: "ocean_guide"
- note: "판옥선 전용 장비"
- order_no: 1
- relative_path: "../contents/panokseon-haemo-byeokgye.md"
### `sailor-role-slots.relation.panokseon`

- seed_key: "sailor-role-slots.relation.panokseon"
- direction: "incoming"
- relation_type: "related"
- content_slug: "sailor-role-slots"
- content_name_ko: "선원 역할 슬롯"
- content_category: "ocean_guide"
- note: "판옥선은 함포 슬롯 2칸이 추가된다."
- order_no: 2
- relative_path: "../contents/sailor-role-slots.md"
### `account-progression-foundation.panokseon`

- seed_key: "account-progression-foundation.panokseon"
- direction: "incoming"
- relation_type: "related"
- content_slug: "account-progression-foundation"
- content_name_ko: "가문 성장 기반"
- content_category: "progression"
- note: null
- order_no: 8
- relative_path: "../contents/account-progression-foundation.md"
### `sailing-onboarding-strategy.panokseon`

- seed_key: "sailing-onboarding-strategy.panokseon"
- direction: "incoming"
- relation_type: "related"
- content_slug: "sailing-onboarding-strategy"
- content_name_ko: "항해 입문 운영 전략"
- content_category: "ocean_guide"
- note: "판옥선·상위 선박 목적"
- order_no: 10
- relative_path: "../contents/sailing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `panokseon.evidence.base-stats::panokseon-guide`

- evidence_seed_key: "panokseon.evidence.base-stats::panokseon-guide"
- source_id: "panokseon-guide"
- title: "판옥선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=374"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon.base-stats"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "판옥선 기본 능력치"
- active: true
- is_active: true

### `panokseon.evidence.identity::panokseon-guide`

- evidence_seed_key: "panokseon.evidence.identity::panokseon-guide"
- source_id: "panokseon-guide"
- title: "판옥선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=374"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon.identity"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "판옥선의 전투·다선원 운용 성격"
- active: true
- is_active: true

### `panokseon.evidence.material-sources::panokseon-guide`

- evidence_seed_key: "panokseon.evidence.material-sources::panokseon-guide"
- source_id: "panokseon-guide"
- title: "판옥선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=374"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon.material-sources"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "도면·나무못·합판·접착제 획득처"
- active: true
- is_active: true

### `panokseon.evidence.materials::panokseon-guide`

- evidence_seed_key: "panokseon.evidence.materials::panokseon-guide"
- source_id: "panokseon-guide"
- title: "판옥선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=374"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon.materials"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "판옥선 선체 제작 재료"
- active: true
- is_active: true

### `panokseon.evidence.shipyards::ocean-progression-2026-08-26`

- evidence_seed_key: "panokseon.evidence.shipyards::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon.shipyards"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "두 조선소 제작 위치"
- active: true
- is_active: true

### `panokseon.evidence.shipyards::panokseon-guide`

- evidence_seed_key: "panokseon.evidence.shipyards::panokseon-guide"
- source_id: "panokseon-guide"
- title: "판옥선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=374"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "panokseon.shipyards"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "두 조선소 제작 위치"
- active: true
- is_active: true

### Historical / inactive evidence

- None
