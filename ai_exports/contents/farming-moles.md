<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 재배 두더지와 슈슈

## Identity

- slug: "farming-moles"
- name_ko: "재배 두더지와 슈슈"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "수확·품종개량 중 두더지가 탐내는 먹이를 얻으면 두더지가 등장하며, 보상 최신 기준은 2026-06-17 후속 조정이다."
- purpose: "두더지 발생 구조, 6월 두 차례 변경과 슈슈 진행을 분리한다."

## Requirements

### `farming-moles.spawn`

- seed_key: "farming-moles.spawn"
- kind: "other"
- requirement_level: "required"
- title: "두더지 발생"
- description: "수확 또는 품종개량 중 먹이를 얻으면 텃밭 근처에 두더지가 출현한다."
- structured_value:

```json
{
  "actions": [
    "harvest",
    "breed"
  ],
  "additional_spawn_while_one_active": false,
  "blocked_by_party_summoned_monster": true,
  "magical_or_mysterious_seed_higher_chance": true,
  "trigger_item": "두더지가 탐내는 먹이"
}
```

### `farming-moles.june-04`

- seed_key: "farming-moles.june-04"
- kind: "stat"
- requirement_level: "required"
- title: "2026-06-04 출현 변경"
- description: "기본 출현 확률 2배, 거대 두더지 조정과 전리품·담홍색 잎사귀 상향이 적용됐다."
- structured_value:

```json
{
  "base_spawn_probability_multiplier": 2,
  "giant_mole_probability_relative_to_previous": 2.5,
  "reward_probability_increased": true,
  "types_equalized": true
}
```

### `farming-moles.latest-adjustment`

- seed_key: "farming-moles.latest-adjustment"
- kind: "stat"
- requirement_level: "required"
- title: "2026-06-17 최신 보상"
- description: "두더지 보상과 담홍색 잎사귀 수량이 추가 상향됐다. 상대 증가율로 절대 수량을 역산하지 않는다."
- structured_value:

```json
{
  "absolute_counts": null,
  "blush_leaf_relative_increase_percent": {
    "거대 두더지": 192.5,
    "느림보 두더지": 335.5,
    "배고픈 두더지": 733.3,
    "슈슈": 135.7,
    "통통한 두더지": 173.6
  },
  "latest_evidence_date": "2026-06-17",
  "state": "increased"
}
```

### `farming-moles.shushu`

- seed_key: "farming-moles.shushu"
- kind: "quest"
- requirement_level: "required"
- title: "슈슈 진행"
- description: "거대 두더지 처치 후 낮은 확률로 슈슈가 등장하며 꽃잎 10개로 의뢰를 완료해 슈슈 반려동물을 얻는다."
- structured_value:

```json
{
  "interaction": "drive_away_not_kill",
  "item": "슈슈가 떨어뜨린 꽃잎",
  "quest_npc": "잼카스 웜스베인",
  "required_amount": 10,
  "reward": "슈슈 반려동물",
  "trigger": "low_probability_after_giant_mole"
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

### `farming-moles.harvest`

- seed_key: "farming-moles.harvest"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "farming-seeds-harvest-breeding"
- content_name_ko: "재배 씨앗·수확·품종개량"
- content_category: "life"
- note: "수확·품종개량 발생"
- order_no: 1
- relative_path: "../contents/farming-seeds-harvest-breeding.md"
### `farming-seeds-harvest-breeding.moles`

- seed_key: "farming-seeds-harvest-breeding.moles"
- direction: "incoming"
- relation_type: "related"
- content_slug: "farming-seeds-harvest-breeding"
- content_name_ko: "재배 씨앗·수확·품종개량"
- content_category: "life"
- note: "수확·품종개량 시 두더지 발생"
- order_no: 2
- relative_path: "../contents/farming-seeds-harvest-breeding.md"
### `farming-current-cycle.moles`

- seed_key: "farming-current-cycle.moles"
- direction: "incoming"
- relation_type: "related"
- content_slug: "farming-current-cycle"
- content_name_ko: "재배 현재 주기"
- content_category: "life"
- note: "수확·품종개량 중 두더지"
- order_no: 3
- relative_path: "../contents/farming-current-cycle.md"
### `farming-onboarding-strategy.moles`

- seed_key: "farming-onboarding-strategy.moles"
- direction: "incoming"
- relation_type: "related"
- content_slug: "farming-onboarding-strategy"
- content_name_ko: "재배 입문 전략"
- content_category: "life"
- note: null
- order_no: 5
- relative_path: "../contents/farming-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `farming-moles.summary::farming-guide`

- evidence_seed_key: "farming-moles.summary::farming-guide"
- source_id: "farming-guide"
- title: "재배"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=94"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "farming-moles"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "두더지 구조와 최신 보상"
- active: true
- is_active: true

### `farming-moles.summary::farming-moles-2026-06-17`

- evidence_seed_key: "farming-moles.summary::farming-moles-2026-06-17"
- source_id: "farming-moles-2026-06-17"
- title: "6월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15751"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "farming-moles"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "두더지 구조와 최신 보상"
- active: true
- is_active: true

### `farming-moles.requirement.june-04::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-moles.requirement.june-04::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-moles.june-04"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "6월 4일 출현 확률 변경"
- active: true
- is_active: true

### `farming-moles.requirement.latest-adjustment::farming-moles-2026-06-17`

- evidence_seed_key: "farming-moles.requirement.latest-adjustment::farming-moles-2026-06-17"
- source_id: "farming-moles-2026-06-17"
- title: "6월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15751"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-moles.latest-adjustment"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "6월 17일 최신 보상 상향"
- active: true
- is_active: true

### `farming-moles.requirement.shushu::farming-guide`

- evidence_seed_key: "farming-moles.requirement.shushu::farming-guide"
- source_id: "farming-guide"
- title: "재배"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=94"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-moles.shushu"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "슈슈 획득 흐름"
- active: true
- is_active: true

### `farming-moles.requirement.spawn::farming-guide`

- evidence_seed_key: "farming-moles.requirement.spawn::farming-guide"
- source_id: "farming-guide"
- title: "재배"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=94"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "farming-moles.spawn"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "발생 조건과 동시 출현 제한"
- active: true
- is_active: true

### Historical / inactive evidence

### `farming-moles.legacy.june-04-reward::farming-overhaul-2026-06-04`

- evidence_seed_key: "farming-moles.legacy.june-04-reward::farming-overhaul-2026-06-04"
- source_id: "farming-overhaul-2026-06-04"
- title: "6월 4일(목) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15694"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-04"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "farming-moles"
- claim_key: "legacy.latest_reward_adjustment"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "6월 4일 보상 기준은 6월 17일 후속 조정 이전 상태"
- active: false
- is_active: false
