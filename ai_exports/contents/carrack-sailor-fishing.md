<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 중범선 선원 낚시

## Identity

- slug: "carrack-sailor-fishing"
- name_ko: "중범선 선원 낚시"
- category: "ocean_guide"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "중범선에 바다를 품은 해달 낚싯대와 낚시 선원을 함께 배치하면 이동 중 180초마다 선원 낚시를 진행한다."
- purpose: "활성 조건, 고정 확률, 초기화와 일시정지 조건을 구분한다."

## Requirements

### `carrack-sailor-fishing.activation`

- seed_key: "carrack-sailor-fishing.activation"
- kind: "other"
- requirement_level: "required"
- title: "활성 조건"
- description: "에페리아 중범선에 바다를 품은 해달 낚싯대를 장착하고 낚시 슬롯에 선원을 배치해야 한다. 낚싯대만 장착하면 활성화되지 않는다."
- structured_value:

```json
{
  "fishing_sailor_required": true,
  "rod": "바다를 품은 해달 낚싯대",
  "ship": "에페리아 중범선"
}
```

### `carrack-sailor-fishing.rod-quest`

- seed_key: "carrack-sailor-fishing.rod-quest"
- kind: "other"
- requirement_level: "required"
- title: "낚싯대 획득 의뢰"
- description: "[대양의 시대] 해달 물물교환원 완료 후 크리오의 [선원 낚시] 모험가는 해달족의 친구를 완료한다. 목표는 까마귀 주화 교환권 200개 전달이다."
- structured_value:

```json
{
  "crow_coin_exchange_coupon": 200,
  "npc": "크리오",
  "prerequisite": "[대양의 시대] 해달 물물교환원",
  "quest": "[선원 낚시] 모험가는 해달족의 친구"
}
```

### `carrack-sailor-fishing.rules`

- seed_key: "carrack-sailor-fishing.rules"
- kind: "other"
- requirement_level: "required"
- title: "낚시 규칙"
- description: "중범선이 이동 중일 때만 180초 타이머가 흐르며 지정 선박 기술 중에도 흐른다. 키를 놓았다 다시 잡아도 초기화되지 않는다."
- structured_value:

```json
{
  "regrip_resets_timer": false,
  "seconds_per_cast": 180,
  "skills_count_as_movement": [
    "충각",
    "급발진",
    "쾌속순항",
    "후퇴기동",
    "급선회",
    "회전기동"
  ],
  "timer_requires_movement": true
}
```

### `carrack-sailor-fishing.loot`

- seed_key: "carrack-sailor-fishing.loot"
- kind: "other"
- requirement_level: "required"
- title: "획득·확률 규칙"
- description: "물고기는 캐릭터 가방 또는 보유 어항으로 들어간다. 낚시 숙련도는 보물 물고기 확률을 올리지 않으며 보물 등급 그룹은 3% 고정이다. 주간 낚시대회·어류도감과 해역 어장 자원에 반영된다."
- structured_value:

```json
{
  "applies_to": [
    "주간 낚시대회",
    "어류도감",
    "해역 어장 자원"
  ],
  "destination": [
    "캐릭터 가방",
    "어항"
  ],
  "mastery_increases_treasure_chance": false,
  "treasure_group_percent": 3
}
```

### `carrack-sailor-fishing.reset`

- seed_key: "carrack-sailor-fishing.reset"
- kind: "other"
- requirement_level: "required"
- title: "시간 초기화 조건"
- description: "낚싯대 해제·교체, 선착장에 선박 맡김, 선박 파괴, 캐릭터 선택 창 이동, 게임 종료 시 낚시 시간이 초기화된다."
- structured_value:

```json
[
  "낚싯대 해제 또는 교체",
  "선박 선착장 보관",
  "선박 파괴",
  "캐릭터 선택 창 이동",
  "게임 종료"
]
```

### `carrack-sailor-fishing.pause`

- seed_key: "carrack-sailor-fishing.pause"
- kind: "other"
- requirement_level: "required"
- title: "일시정지 조건"
- description: "낚싯대 내구도 0, 낚시 선원 질병, 선박 정지 시 낚시가 일시정지된다."
- structured_value:

```json
[
  "낚싯대 내구도 0",
  "낚시 선원 질병",
  "선박 정지"
]
```

### `carrack-sailor-fishing.cabin`

- seed_key: "carrack-sailor-fishing.cabin"
- kind: "other"
- requirement_level: "required"
- title: "중범선 선실 확장"
- description: "낚시 선원 슬롯 추가와 함께 기존 중범선 선실이 100에서 110으로 확장됐다."
- structured_value:

```json
{
  "after": 110,
  "before": 100
}
```

## Steps

### `carrack-sailor-fishing.step.obtain-rod`

- seed_key: "carrack-sailor-fishing.step.obtain-rod"
- phase: "unlock"
- order_no: 1
- title: "해달 낚싯대 획득"
- description: "선행 의뢰와 크리오 의뢰를 완료해 전용 낚싯대를 획득한다."
- checkable: true

### `carrack-sailor-fishing.step.assign-sailor`

- seed_key: "carrack-sailor-fishing.step.assign-sailor"
- phase: "preparation"
- order_no: 2
- title: "낚시 선원 배치"
- description: "중범선 낚시 슬롯에 낚시 선원을 배치한다."
- checkable: true

## Schedules

- None

## Rewards

- None

## Sections

- None

## Related Contents

### `carrack-sailor-fishing.relation.roles`

- seed_key: "carrack-sailor-fishing.relation.roles"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sailor-role-slots"
- content_name_ko: "선원 역할 슬롯"
- content_category: "ocean_guide"
- note: "낚시 선원 전용 슬롯"
- order_no: 1
- relative_path: "../contents/sailor-role-slots.md"
### `carrack-sailor-fishing.relation.health`

- seed_key: "carrack-sailor-fishing.relation.health"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sailor-health-food"
- content_name_ko: "선원 건강과 식량"
- content_category: "ocean_guide"
- note: "선원 질병 시 낚시 일시정지"
- order_no: 2
- relative_path: "../contents/sailor-health-food.md"
### `carrack-sailor-fishing.relation.carracks`

- seed_key: "carrack-sailor-fishing.relation.carracks"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "carrack-types"
- content_name_ko: "에페리아 중범선 네 종류"
- content_category: "ocean_project"
- note: "에페리아 중범선 전용 기능"
- order_no: 3
- relative_path: "../contents/carrack-types.md"
### `auto-fishing.sailor`

- seed_key: "auto-fishing.sailor"
- direction: "incoming"
- relation_type: "related"
- content_slug: "auto-fishing"
- content_name_ko: "일반 자동 낚시"
- content_category: "life"
- note: "서로 다른 자동 낚시 mechanic"
- order_no: 2
- relative_path: "../contents/auto-fishing.md"
### `sailor-health-food.relation.fishing`

- seed_key: "sailor-health-food.relation.fishing"
- direction: "incoming"
- relation_type: "related"
- content_slug: "sailor-health-food"
- content_name_ko: "선원 건강과 식량"
- content_category: "ocean_guide"
- note: "낚시 선원이 병들면 선원 낚시가 일시정지된다."
- order_no: 2
- relative_path: "../contents/sailor-health-food.md"
### `fishing-encyclopedia-and-weekly-contest.sailor`

- seed_key: "fishing-encyclopedia-and-weekly-contest.sailor"
- direction: "incoming"
- relation_type: "related"
- content_slug: "fishing-encyclopedia-and-weekly-contest"
- content_name_ko: "어류 도감과 주간 낚시 대회"
- content_category: "life"
- note: "선원 낚시 기록도 도감·대회에 반영"
- order_no: 3
- relative_path: "../contents/fishing-encyclopedia-and-weekly-contest.md"

## Evidence and Sources

### Current evidence

### `carrack-sailor-fishing.evidence.activation::carrack-sailor-fishing-2025`

- evidence_seed_key: "carrack-sailor-fishing.evidence.activation::carrack-sailor-fishing-2025"
- source_id: "carrack-sailor-fishing-2025"
- title: "중범선 선원 자동 낚시"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13994"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-sailor-fishing.activation"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "전용 낚싯대와 낚시 선원 동시 필요"
- active: true
- is_active: true

### `carrack-sailor-fishing.evidence.cabin::carrack-sailor-fishing-2025`

- evidence_seed_key: "carrack-sailor-fishing.evidence.cabin::carrack-sailor-fishing-2025"
- source_id: "carrack-sailor-fishing-2025"
- title: "중범선 선원 자동 낚시"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13994"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-sailor-fishing.cabin"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "중범선 선실 100에서 110 확장"
- active: true
- is_active: true

### `carrack-sailor-fishing.evidence.loot::carrack-sailor-fishing-2025`

- evidence_seed_key: "carrack-sailor-fishing.evidence.loot::carrack-sailor-fishing-2025"
- source_id: "carrack-sailor-fishing-2025"
- title: "중범선 선원 자동 낚시"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13994"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-sailor-fishing.loot"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "획득 위치, 3% 고정 확률과 관련 콘텐츠 반영"
- active: true
- is_active: true

### `carrack-sailor-fishing.evidence.pause::carrack-sailor-fishing-2025`

- evidence_seed_key: "carrack-sailor-fishing.evidence.pause::carrack-sailor-fishing-2025"
- source_id: "carrack-sailor-fishing-2025"
- title: "중범선 선원 자동 낚시"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13994"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-sailor-fishing.pause"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "낚시 일시정지 조건"
- active: true
- is_active: true

### `carrack-sailor-fishing.evidence.reset::carrack-sailor-fishing-2025`

- evidence_seed_key: "carrack-sailor-fishing.evidence.reset::carrack-sailor-fishing-2025"
- source_id: "carrack-sailor-fishing-2025"
- title: "중범선 선원 자동 낚시"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13994"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-sailor-fishing.reset"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "낚시 시간 초기화 조건"
- active: true
- is_active: true

### `carrack-sailor-fishing.evidence.rod-quest::carrack-sailor-fishing-2025`

- evidence_seed_key: "carrack-sailor-fishing.evidence.rod-quest::carrack-sailor-fishing-2025"
- source_id: "carrack-sailor-fishing-2025"
- title: "중범선 선원 자동 낚시"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13994"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-sailor-fishing.rod-quest"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "낚싯대 의뢰와 교환권 200개"
- active: true
- is_active: true

### `carrack-sailor-fishing.evidence.rules::carrack-sailor-fishing-2025`

- evidence_seed_key: "carrack-sailor-fishing.evidence.rules::carrack-sailor-fishing-2025"
- source_id: "carrack-sailor-fishing-2025"
- title: "중범선 선원 자동 낚시"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13994"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-sailor-fishing.rules"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "180초·이동 중 진행·기술·재승선 규칙"
- active: true
- is_active: true

### Historical / inactive evidence

- None
