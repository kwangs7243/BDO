<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 최후의 글라디우스 주간 토벌

## Identity

- slug: "last-gladiius-weekly"
- name_ko: "최후의 글라디우스 주간 토벌"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- party_type: "solo"
- difficulty: "high"

## Overview

- summary: "아토락시온 서사의 최종전인 1인 주간 우두머리 콘텐츠. 붉은 심장의 솔 마기아에게 '[주간] 글라디우스 : 카이벨라 함'을 수주하고 일레즈라와 아토마기아의 심장을 공략한다."
- purpose: "일레즈라 주간 우두머리를 처치하고 글라디우스 : 카이벨라 함 보상을 획득한다."

## Requirements

### `last-gladiius-weekly.weekly-access`

- seed_key: "last-gladiius-weekly.weekly-access"
- kind: "quest"
- requirement_level: "required"
- title: "주간 의뢰 진입"
- description: "고대인의 석실 타리브레의 문을 통해 붉은 심장으로 이동한 뒤 솔 마기아에게 '[주간] 글라디우스 : 카이벨라 함'을 수주한다. 추천 의뢰 완료 여부와 무관하게 주간 토벌과 보상 획득이 가능하다."
- structured_value:

```json
{
  "entry_route": "고대인의 석실 타리브레의 문 → 붉은 심장",
  "knowledge_role": "fact",
  "quest": "[주간] 글라디우스 : 카이벨라 함",
  "quest_npc": "붉은 심장 솔 마기아",
  "recommended_quest_required": false
}
```

### `last-gladiius-weekly.recommended-stats`

- seed_key: "last-gladiius-weekly.recommended-stats"
- kind: "stat"
- requirement_level: "recommended"
- title: "현재 권장 능력치"
- description: "현재 공식 권장 표기 공격력은 330, 추천 방어력은 420이다. 1인 콘텐츠이며 엘비아의 영역에서는 진행할 수 없다."
- structured_value:

```json
{
  "elvia_available": false,
  "knowledge_role": "fact",
  "party_size": 1,
  "recommended_display_ap": 330,
  "recommended_dp": 420
}
```

### `last-gladiius-weekly.weekly-rule`

- seed_key: "last-gladiius-weekly.weekly-rule"
- kind: "other"
- requirement_level: "required"
- title: "주간 반복 규칙"
- description: "주간 연속 의뢰는 일주일에 한 번 진행하며 아토락시온 주간 의뢰의 목요일 00:00 KST 초기화 규칙을 따른다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "reset_time_local": "00:00",
  "reset_weekday": 3,
  "timezone": "Asia/Seoul",
  "weekly_completion_limit": 1
}
```

### `last-gladiius-weekly.encounter-mechanics`

- seed_key: "last-gladiius-weekly.encounter-mechanics"
- kind: "other"
- requirement_level: "required"
- title: "현재 핵심 전투 기믹"
- description: "아토마기아의 심장 생명력 90%, 70%, 50%, 30%에 검은 환상이 소환된다. 환상 처치 시 심장에 50초간 방어력 감소가 적용되고 고대 장치가 순차 점등되어 전투 종료까지 유지된다. 모든 환상을 처치하면 추적 고대 병기가 정지하고 심장을 계속 공격할 수 있다."
- structured_value:

```json
{
  "above_limit_effect_percent": 50,
  "all_illusions_defeated_keeps_heart_attackable": true,
  "all_illusions_defeated_stops_tracking_ancient_weapons": true,
  "ancient_device_light_persists_until_battle_end": true,
  "ancient_device_lights_sequentially": true,
  "attack_power_limit": 1000,
  "black_illusion_attack_invulnerability_removed_or_adjusted": true,
  "black_illusion_spawn_heart_hp_percent": [
    90,
    70,
    50,
    30
  ],
  "heart_defense_reduction_seconds_after_illusion": 50,
  "knowledge_role": "fact",
  "monster_defense_increase_percent_from_2025_07_23": 6
}
```

### `last-gladiius-weekly.reward-rule`

- seed_key: "last-gladiius-weekly.reward-rule"
- kind: "item"
- requirement_level: "required"
- title: "주간 보상"
- description: "'[주간] 글라디우스 : 카이벨라 함' 연속 의뢰 완료 시 글라디우스 : 카이벨라 함 1개를 획득한다. 상자는 고정 구성품과 지정된 확률 구성품을 분리해 제공한다."
- structured_value:

```json
{
  "chance_contents": [
    "개량형 나침반 부품",
    "거상의 반지 조각",
    "황금빛 사막의 눈물"
  ],
  "fixed_contents": [
    {
      "amount": 1,
      "item": "데키아의 진귀한 상자"
    },
    {
      "amount": 25,
      "item": "자연의 흔적"
    },
    {
      "amount": 25,
      "item": "고대 정령의 가루"
    },
    {
      "amount": 25,
      "item": "데키마 : 맹약의 증표"
    },
    {
      "amount": 35,
      "item": "마하의 파편"
    }
  ],
  "knowledge_role": "fact",
  "rare_box_chance_content": "0~고(III) 단계 데보레카 액세서리 4종 중 하나",
  "weekly_chest": "글라디우스 : 카이벨라 함",
  "weekly_chest_amount": 1
}
```

## Steps

### `last-gladiius-weekly.step.check-access`

- seed_key: "last-gladiius-weekly.step.check-access"
- phase: "preparation"
- order_no: 1
- title: "붉은 심장 진입 확인"
- description: "고대인의 석실 타리브레의 문을 통해 붉은 심장으로 이동할 수 있는지 확인한다."
- checkable: false

### `last-gladiius-weekly.step.accept-weekly`

- seed_key: "last-gladiius-weekly.step.accept-weekly"
- phase: "repeat"
- order_no: 2
- title: "주간 의뢰 수주"
- description: "붉은 심장의 솔 마기아에게 '[주간] 글라디우스 : 카이벨라 함' 연속 의뢰를 수주한다."
- checkable: false

### `last-gladiius-weekly.step.enter-battle`

- seed_key: "last-gladiius-weekly.step.enter-battle"
- phase: "repeat"
- order_no: 3
- title: "대화로 전투 진입"
- description: "주간 의뢰 수주 후 대화 버튼을 통해 일레즈라 전투에 진입한다."
- checkable: false

### `last-gladiius-weekly.step.begin-encounter`

- seed_key: "last-gladiius-weekly.step.begin-encounter"
- phase: "repeat"
- order_no: 4
- title: "일레즈라와 심장 전투 시작"
- description: "일레즈라를 상대하고 아토마기아의 심장 전투 구간으로 진행한다."
- checkable: false

### `last-gladiius-weekly.step.handle-illusions`

- seed_key: "last-gladiius-weekly.step.handle-illusions"
- phase: "repeat"
- order_no: 5
- title: "검은 환상 우선 처치"
- description: "심장 생명력 90%, 70%, 50%, 30%에 소환되는 일레즈라의 검은 환상을 처치한다."
- checkable: false

### `last-gladiius-weekly.step.use-defense-window`

- seed_key: "last-gladiius-weekly.step.use-defense-window"
- phase: "repeat"
- order_no: 6
- title: "방어력 감소 구간 활용"
- description: "검은 환상 처치 후 아토마기아의 심장에 적용되는 50초 방어력 감소 동안 공격한다."
- checkable: false

### `last-gladiius-weekly.step.light-devices`

- seed_key: "last-gladiius-weekly.step.light-devices"
- phase: "repeat"
- order_no: 7
- title: "고대 장치 점등 진행"
- description: "환상 처치에 따라 고대 장치가 순차 점등되고 전투 종료까지 유지되는 상태를 확인한다."
- checkable: false

### `last-gladiius-weekly.step.open-heart-window`

- seed_key: "last-gladiius-weekly.step.open-heart-window"
- phase: "repeat"
- order_no: 8
- title: "심장 상시 공격 상태 확보"
- description: "모든 검은 환상을 처치해 추적 고대 병기를 정지시키고 아토마기아의 심장을 계속 공격할 수 있는 상태를 만든다."
- checkable: false

### `last-gladiius-weekly.step.defeat-boss`

- seed_key: "last-gladiius-weekly.step.defeat-boss"
- phase: "repeat"
- order_no: 9
- title: "주간 우두머리 처치"
- description: "현재 기믹에 따라 일레즈라와 아토마기아의 심장 전투를 마무리한다."
- checkable: false

### `last-gladiius-weekly.step.claim-reward`

- seed_key: "last-gladiius-weekly.step.claim-reward"
- phase: "reward"
- order_no: 10
- title: "의뢰 완료와 보상 확인"
- description: "주간 연속 의뢰를 완료해 글라디우스 : 카이벨라 함을 받고 이번 주 checklist를 완료한다."
- checkable: true

## Schedules

### `last-gladiius-weekly.quest-reset`

- seed_key: "last-gladiius-weekly.quest-reset"
- rule_type: "quest_reset"
- recurrence_type: "weekly"
- weekday: 3
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "아토락시온 주간 의뢰 공통 기준: 목요일 00:00 KST"

## Rewards

### `last-gladiius-weekly.reward.weekly-chest`

- seed_key: "last-gladiius-weekly.reward.weekly-chest"
- name: "글라디우스 : 카이벨라 함"
- reward_type: "weekly_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "주간 연속 의뢰 직접 보상"
- order_no: 1

### `last-gladiius-weekly.reward.dehkia-rare-box`

- seed_key: "last-gladiius-weekly.reward.dehkia-rare-box"
- name: "데키아의 진귀한 상자"
- reward_type: "weekly_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "카이벨라 함 고정 구성품"
- order_no: 2

### `last-gladiius-weekly.reward.trace-of-nature`

- seed_key: "last-gladiius-weekly.reward.trace-of-nature"
- name: "자연의 흔적"
- reward_type: "weekly_material"
- amount: 25.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "카이벨라 함 고정 구성품"
- order_no: 3

### `last-gladiius-weekly.reward.ancient-spirit-dust`

- seed_key: "last-gladiius-weekly.reward.ancient-spirit-dust"
- name: "고대 정령의 가루"
- reward_type: "weekly_material"
- amount: 25.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "카이벨라 함 고정 구성품"
- order_no: 4

### `last-gladiius-weekly.reward.dekima-token`

- seed_key: "last-gladiius-weekly.reward.dekima-token"
- name: "데키마 : 맹약의 증표"
- reward_type: "weekly_material"
- amount: 25.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "카이벨라 함 고정 구성품"
- order_no: 5

### `last-gladiius-weekly.reward.maha-fragment`

- seed_key: "last-gladiius-weekly.reward.maha-fragment"
- name: "마하의 파편"
- reward_type: "weekly_material"
- amount: 35.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "카이벨라 함 고정 구성품"
- order_no: 6

### `last-gladiius-weekly.reward.compass-part`

- seed_key: "last-gladiius-weekly.reward.compass-part"
- name: "개량형 나침반 부품"
- reward_type: "treasure"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "카이벨라 함에서 지정된 확률로 획득"
- order_no: 7

### `last-gladiius-weekly.reward.rich-merchant-ring-piece`

- seed_key: "last-gladiius-weekly.reward.rich-merchant-ring-piece"
- name: "거상의 반지 조각"
- reward_type: "treasure"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "카이벨라 함에서 지정된 확률로 획득"
- order_no: 8

### `last-gladiius-weekly.reward.golden-desert-tear`

- seed_key: "last-gladiius-weekly.reward.golden-desert-tear"
- name: "황금빛 사막의 눈물"
- reward_type: "treasure"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "카이벨라 함에서 지정된 확률로 획득"
- order_no: 9

### `last-gladiius-weekly.reward.deboreka-accessory`

- seed_key: "last-gladiius-weekly.reward.deboreka-accessory"
- name: "데보레카 액세서리"
- reward_type: "treasure"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "데키아의 진귀한 상자에서 지정된 확률로 0~고(III) 단계 반지·귀걸이·목걸이·허리띠 중 하나 획득"
- order_no: 10

## Sections

### `last-gladiius-weekly.section.quest-boundary`

- seed_key: "last-gladiius-weekly.section.quest-boundary"
- section_type: "overview"
- title: "추천 의뢰와 반복 주간 의뢰 구분"
- order_no: 1

#### body_markdown

추천 의뢰 '[최후의 글라디우스]'는 레벨 60 이상이며 '[아토락시온] 가시나무와 검은 여신'을 완료한 캐릭터가 흑정령에게 '[아토락시온] 일레즈라가 기다리는 곳'을 수주해 시작한다. 추천 의뢰 전투 제한 시간은 50분이고 최초 완료 칭호는 '글라디우스 챔피언'이며, 모든 아토락시온 추천 의뢰 완료 뒤 가문당 1회 '[아토락시온] 최후의 선택' 보상이 있다. 반복 주간은 추천 의뢰 완료 없이도 진행 가능하며 붉은 심장 솔 마기아의 '[주간] 글라디우스 : 카이벨라 함'을 통해 주 1회 보상을 획득한다. 주간 우두머리 승리 1회와 5회 칭호는 각각 '데키아의 의지를 이은', '요새의 후계자'다.

### `last-gladiius-weekly.section.current-mechanics`

- seed_key: "last-gladiius-weekly.section.current-mechanics"
- section_type: "notes"
- title: "현재 공식 전투 흐름"
- order_no: 2

#### body_markdown

검은 환상은 심장 생명력 90%·70%·50%·30%에 등장한다. 환상을 처치하면 심장에 50초 방어력 감소가 적용되고 고대 장치가 하나씩 점등되어 전투 종료까지 유지된다. 모든 환상을 처치하면 추적 고대 병기가 멈추며 심장을 계속 공격할 수 있다. 이는 공식 FACT 흐름이며 클래스별 공략이나 동적 전략은 포함하지 않는다.

### `last-gladiius-weekly.section.common-mistakes`

- seed_key: "last-gladiius-weekly.section.common-mistakes"
- section_type: "common_mistakes"
- title: "추천 의뢰 규칙을 주간에 복사하지 않기"
- order_no: 3

#### body_markdown

추천 의뢰의 레벨·선행 의뢰·50분 제한·최초 1회 보상을 반복 주간 규칙으로 간주하지 않는다. 주간 의뢰는 별도 수주·보상 흐름이며 검은 환상을 처리하지 않고 심장만 공격하면 현재 방어력 감소와 점등 기믹을 활용할 수 없다.

## Related Contents

### `last-gladiius-weekly.atoraxxion-weekly`

- seed_key: "last-gladiius-weekly.atoraxxion-weekly"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "atoraxxion-weekly"
- content_name_ko: "아토락시온 주간 토벌"
- content_category: "combat_pve"
- note: "현재 네 아토락시온 지역의 통합 주간 토벌 Content"
- order_no: 1
- relative_path: "../contents/atoraxxion-weekly.md"
### `last-gladiius-weekly.weekly-framework`

- seed_key: "last-gladiius-weekly.weekly-framework"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "weekly-quest-framework"
- content_name_ko: "주간 의뢰 공통 규칙"
- content_category: "system"
- note: "일반 주간 의뢰 period와 목요일 reset 의미"
- order_no: 2
- relative_path: "../contents/weekly-quest-framework.md"

## Evidence and Sources

### Current evidence

### `last-gladiius-weekly.claim.purpose::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.purpose::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "last-gladiius-weekly"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.summary::gladius-balance-2026`

- evidence_seed_key: "last-gladiius-weekly.claim.summary::gladius-balance-2026"
- source_id: "gladius-balance-2026"
- title: "6월 24일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15783"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-24"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "last-gladiius-weekly"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.summary::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.summary::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "last-gladiius-weekly"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.encounter-mechanics::combat-system-rework-2025-07-23`

- evidence_seed_key: "last-gladiius-weekly.claim.encounter-mechanics::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "last-gladiius-weekly.encounter-mechanics"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.encounter-mechanics::gladius-2026`

- evidence_seed_key: "last-gladiius-weekly.claim.encounter-mechanics::gladius-2026"
- source_id: "gladius-2026"
- title: "1월 28일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15136"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "last-gladiius-weekly.encounter-mechanics"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.encounter-mechanics::gladius-balance-2026`

- evidence_seed_key: "last-gladiius-weekly.claim.encounter-mechanics::gladius-balance-2026"
- source_id: "gladius-balance-2026"
- title: "6월 24일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15783"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-24"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "last-gladiius-weekly.encounter-mechanics"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.encounter-mechanics::gladius-mechanics-2025-10-22`

- evidence_seed_key: "last-gladiius-weekly.claim.encounter-mechanics::gladius-mechanics-2025-10-22"
- source_id: "gladius-mechanics-2025-10-22"
- title: "10월 22일(수) 업데이트 안내 (최종 수정 : 2025-11-03 11:15)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14677"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-10-22"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "last-gladiius-weekly.encounter-mechanics"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.recommended-stats::gladius-balance-2026`

- evidence_seed_key: "last-gladiius-weekly.claim.recommended-stats::gladius-balance-2026"
- source_id: "gladius-balance-2026"
- title: "6월 24일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15783"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-24"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "last-gladiius-weekly.recommended-stats"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.recommended-stats::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.recommended-stats::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "last-gladiius-weekly.recommended-stats"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.reward-rule::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.reward-rule::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "last-gladiius-weekly.reward-rule"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.weekly-access::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.weekly-access::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "last-gladiius-weekly.weekly-access"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.weekly-access::gladius-quest-flow-2025-06-04`

- evidence_seed_key: "last-gladiius-weekly.claim.weekly-access::gladius-quest-flow-2025-06-04"
- source_id: "gladius-quest-flow-2025-06-04"
- title: "6월 4일(수) 업데이트 안내 (최종 수정 : 2025-06-04 18:45)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14063"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-06-04"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "last-gladiius-weekly.weekly-access"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.weekly-rule::ator-reset-patch`

- evidence_seed_key: "last-gladiius-weekly.claim.weekly-rule::ator-reset-patch"
- source_id: "ator-reset-patch"
- title: "2월 16일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=7543"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "last-gladiius-weekly.weekly-rule"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.weekly-rule::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.weekly-rule::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "last-gladiius-weekly.weekly-rule"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.section.common-mistakes::gladius-balance-2026`

- evidence_seed_key: "last-gladiius-weekly.claim.section.common-mistakes::gladius-balance-2026"
- source_id: "gladius-balance-2026"
- title: "6월 24일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15783"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-24"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "last-gladiius-weekly.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.section.common-mistakes::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.section.common-mistakes::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "last-gladiius-weekly.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.section.common-mistakes::gladius-quest-flow-2025-06-04`

- evidence_seed_key: "last-gladiius-weekly.claim.section.common-mistakes::gladius-quest-flow-2025-06-04"
- source_id: "gladius-quest-flow-2025-06-04"
- title: "6월 4일(수) 업데이트 안내 (최종 수정 : 2025-06-04 18:45)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14063"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-06-04"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "last-gladiius-weekly.section.common-mistakes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.section.current-mechanics::combat-system-rework-2025-07-23`

- evidence_seed_key: "last-gladiius-weekly.claim.section.current-mechanics::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "last-gladiius-weekly.section.current-mechanics"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.section.current-mechanics::gladius-2026`

- evidence_seed_key: "last-gladiius-weekly.claim.section.current-mechanics::gladius-2026"
- source_id: "gladius-2026"
- title: "1월 28일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15136"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "last-gladiius-weekly.section.current-mechanics"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.section.current-mechanics::gladius-balance-2026`

- evidence_seed_key: "last-gladiius-weekly.claim.section.current-mechanics::gladius-balance-2026"
- source_id: "gladius-balance-2026"
- title: "6월 24일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15783"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-24"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "last-gladiius-weekly.section.current-mechanics"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.section.current-mechanics::gladius-mechanics-2025-10-22`

- evidence_seed_key: "last-gladiius-weekly.claim.section.current-mechanics::gladius-mechanics-2025-10-22"
- source_id: "gladius-mechanics-2025-10-22"
- title: "10월 22일(수) 업데이트 안내 (최종 수정 : 2025-11-03 11:15)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14677"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-10-22"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "last-gladiius-weekly.section.current-mechanics"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.section.quest-boundary::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.section.quest-boundary::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "last-gladiius-weekly.section.quest-boundary"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.section.quest-boundary::gladius-quest-flow-2025-06-04`

- evidence_seed_key: "last-gladiius-weekly.claim.section.quest-boundary::gladius-quest-flow-2025-06-04"
- source_id: "gladius-quest-flow-2025-06-04"
- title: "6월 4일(수) 업데이트 안내 (최종 수정 : 2025-06-04 18:45)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14063"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-06-04"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "last-gladiius-weekly.section.quest-boundary"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.step.accept-weekly::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.step.accept-weekly::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "last-gladiius-weekly.step.accept-weekly"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.step.begin-encounter::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.step.begin-encounter::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "last-gladiius-weekly.step.begin-encounter"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.step.begin-encounter::gladius-mechanics-2025-10-22`

- evidence_seed_key: "last-gladiius-weekly.claim.step.begin-encounter::gladius-mechanics-2025-10-22"
- source_id: "gladius-mechanics-2025-10-22"
- title: "10월 22일(수) 업데이트 안내 (최종 수정 : 2025-11-03 11:15)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14677"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-10-22"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "last-gladiius-weekly.step.begin-encounter"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.step.check-access::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.step.check-access::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "last-gladiius-weekly.step.check-access"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.step.claim-reward::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.step.claim-reward::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "last-gladiius-weekly.step.claim-reward"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.step.defeat-boss::gladius-balance-2026`

- evidence_seed_key: "last-gladiius-weekly.claim.step.defeat-boss::gladius-balance-2026"
- source_id: "gladius-balance-2026"
- title: "6월 24일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15783"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-24"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "last-gladiius-weekly.step.defeat-boss"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.step.defeat-boss::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.step.defeat-boss::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "last-gladiius-weekly.step.defeat-boss"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.step.enter-battle::gladius-quest-flow-2025-06-04`

- evidence_seed_key: "last-gladiius-weekly.claim.step.enter-battle::gladius-quest-flow-2025-06-04"
- source_id: "gladius-quest-flow-2025-06-04"
- title: "6월 4일(수) 업데이트 안내 (최종 수정 : 2025-06-04 18:45)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14063"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-06-04"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "last-gladiius-weekly.step.enter-battle"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.step.handle-illusions::gladius-balance-2026`

- evidence_seed_key: "last-gladiius-weekly.claim.step.handle-illusions::gladius-balance-2026"
- source_id: "gladius-balance-2026"
- title: "6월 24일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15783"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-24"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "last-gladiius-weekly.step.handle-illusions"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.step.light-devices::gladius-2026`

- evidence_seed_key: "last-gladiius-weekly.claim.step.light-devices::gladius-2026"
- source_id: "gladius-2026"
- title: "1월 28일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15136"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "last-gladiius-weekly.step.light-devices"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.step.open-heart-window::gladius-mechanics-2025-10-22`

- evidence_seed_key: "last-gladiius-weekly.claim.step.open-heart-window::gladius-mechanics-2025-10-22"
- source_id: "gladius-mechanics-2025-10-22"
- title: "10월 22일(수) 업데이트 안내 (최종 수정 : 2025-11-03 11:15)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14677"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-10-22"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "last-gladiius-weekly.step.open-heart-window"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.step.use-defense-window::gladius-balance-2026`

- evidence_seed_key: "last-gladiius-weekly.claim.step.use-defense-window::gladius-balance-2026"
- source_id: "gladius-balance-2026"
- title: "6월 24일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15783"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-24"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "last-gladiius-weekly.step.use-defense-window"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.reward.ancient-spirit-dust::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.reward.ancient-spirit-dust::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "last-gladiius-weekly.reward.ancient-spirit-dust"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.reward.compass-part::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.reward.compass-part::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "last-gladiius-weekly.reward.compass-part"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.reward.deboreka-accessory::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.reward.deboreka-accessory::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "last-gladiius-weekly.reward.deboreka-accessory"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.reward.dehkia-rare-box::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.reward.dehkia-rare-box::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "last-gladiius-weekly.reward.dehkia-rare-box"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.reward.dekima-token::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.reward.dekima-token::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "last-gladiius-weekly.reward.dekima-token"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.reward.golden-desert-tear::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.reward.golden-desert-tear::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "last-gladiius-weekly.reward.golden-desert-tear"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.reward.maha-fragment::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.reward.maha-fragment::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "last-gladiius-weekly.reward.maha-fragment"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.reward.rich-merchant-ring-piece::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.reward.rich-merchant-ring-piece::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "last-gladiius-weekly.reward.rich-merchant-ring-piece"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.reward.trace-of-nature::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.reward.trace-of-nature::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "last-gladiius-weekly.reward.trace-of-nature"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.reward.weekly-chest::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.reward.weekly-chest::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "last-gladiius-weekly.reward.weekly-chest"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: null
- active: true
- is_active: true

### `last-gladiius-weekly.claim.schedule.quest-reset::ator-reset-patch`

- evidence_seed_key: "last-gladiius-weekly.claim.schedule.quest-reset::ator-reset-patch"
- source_id: "ator-reset-patch"
- title: "2월 16일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=7543"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "last-gladiius-weekly.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: "아토락시온 주간 의뢰 목요일 00:00 초기화와 글라디우스 주 1회 진행 근거"
- active: true
- is_active: true

### `last-gladiius-weekly.claim.schedule.quest-reset::gladius-foundation-2025-05-28`

- evidence_seed_key: "last-gladiius-weekly.claim.schedule.quest-reset::gladius-foundation-2025-05-28"
- source_id: "gladius-foundation-2025-05-28"
- title: "5월 28일(수) 업데이트 안내 (최종 수정 : 2025-06-30 16:33)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14029"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-28"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "last-gladiius-weekly.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-07"
- evidence_note: "아토락시온 주간 의뢰 목요일 00:00 초기화와 글라디우스 주 1회 진행 근거"
- active: true
- is_active: true

### Historical / inactive evidence

- None
