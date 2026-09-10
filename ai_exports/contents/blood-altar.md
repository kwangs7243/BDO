<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 피의 제단

## Identity

- slug: "blood-altar"
- name_ko: "피의 제단"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- party_type: "party"
- difficulty: null

## Overview

- summary: "Lv.56 이상 3인이 도전하는 24단계 콘텐츠. 주간 입장 제한은 없고, 파티당 도전 10회와 일요일 주간 보상 정산, 단계별 최초 클리어 보상을 분리해 관리한다. 심연의 환상 1~3은 2026-09-09 삭제되어 current 난이도에 포함하지 않는다."
- purpose: "주간 최고 단계 기록에 따른 가문 보상을 받기 위해 진행하는 단계형 협동 콘텐츠."

## Requirements

### `blood-altar.party-size`

- seed_key: "blood-altar.party-size"
- kind: "party"
- requirement_level: "required"
- title: "파티 구성"
- description: "3인 콘텐츠다."
- structured_value:

```json
{
  "party_size": 3
}
```

### `blood-altar.level`

- seed_key: "blood-altar.level"
- kind: "level"
- requirement_level: "required"
- title: "레벨"
- description: "캐릭터 레벨 56 이상."
- structured_value:

```json
{
  "minimum_level": 56
}
```

### `blood-altar.stages`

- seed_key: "blood-altar.stages"
- kind: "other"
- requirement_level: "required"
- title: "단계와 기록"
- description: "총 24단계이며 최고 클리어 기록은 초기화되지 않는다."
- structured_value:

```json
{
  "highest_clear_persists": true,
  "stage_count": 24
}
```

### `blood-altar.entry-limit`

- seed_key: "blood-altar.entry-limit"
- kind: "other"
- requirement_level: "required"
- title: "입장 제한"
- description: "주간 입장 횟수 제한이 없다."
- structured_value:

```json
{
  "entry_recurrence": "unlimited",
  "weekly_entry_limit": null
}
```

### `blood-altar.challenge-allowance`

- seed_key: "blood-altar.challenge-allowance"
- kind: "other"
- requirement_level: "required"
- title: "파티당 도전 횟수"
- description: "매칭 또는 결성된 파티당 최대 10회 도전하며, 소진 후 자동 퇴장한 뒤 다시 매칭할 수 있다."
- structured_value:

```json
{
  "can_rematch_after_exhaustion": true,
  "party_challenge_allowance": 10
}
```

### `blood-altar.weekly-reward-rule`

- seed_key: "blood-altar.weekly-reward-rule"
- kind: "other"
- requirement_level: "required"
- title: "주간 보상 기준"
- description: "가문당 주 1회, 한 주 최고 단계만 사용하며 여러 단계 보상은 누적되지 않는다."
- structured_value:

```json
{
  "basis": "highest_stage",
  "cumulative": false,
  "family_weekly_reward_limit": 1
}
```

### `blood-altar.high-tier-current`

- seed_key: "blood-altar.high-tier-current"
- kind: "stat"
- requirement_level: "recommended"
- title: "22~24단계 current 구조"
- description: "2026-09-09 기준 22단계 권장 405/465·최종 2110/810, 23단계 권장 410/470·최종 2200/815, 24단계 권장 415/475·최종 2290/820이며 각 단계에 주간 보상과 최초 클리어 보상이 있다. 심연의 환상 1~3은 같은 날 삭제되었다."
- structured_value:

```json
{
  "current_stage_cap": 24,
  "future_high_tiers_possible": true,
  "knowledge_role": "fact",
  "removed_difficulties": [
    {
      "current": false,
      "key": "abyss_illusion_1",
      "name": "심연의 환상 1"
    },
    {
      "current": false,
      "key": "abyss_illusion_2",
      "name": "심연의 환상 2"
    },
    {
      "current": false,
      "key": "abyss_illusion_3",
      "name": "심연의 환상 3"
    }
  ],
  "removed_effective_date": "2026-09-09",
  "stages": {
    "22": {
      "first_clear_reward": {
        "guaranteed": [
          {
            "amount": 3,
            "contents": {
              "max_amount": 10,
              "min_amount": 3,
              "name": "금괴 1kG",
              "unit": "개"
            },
            "name": "금괴 상자",
            "unit": "개"
          },
          {
            "amount": 2,
            "name": "영롱한 포식의 기원",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "발크스의 조언 (+200)",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "피의 제단 : 제22의 환상",
            "unit": "지식"
          }
        ]
      },
      "recommended_ap": 405,
      "recommended_dp": 465,
      "recommended_final_ap": 2110,
      "recommended_final_dp": 810,
      "weekly_reward": {
        "chance_based": [
          {
            "amount": 14,
            "contents": {
              "max_amount": 10,
              "min_amount": 3,
              "name": "금괴 1kG",
              "unit": "개"
            },
            "name": "금괴 상자",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "발크스의 조언 (+300)",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "발크스의 조언 (+250)",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "발크스의 조언 (+200)",
            "unit": "개"
          },
          {
            "amount": 4,
            "name": "영롱한 포식의 기원",
            "unit": "개"
          },
          {
            "amount": 9,
            "name": "영롱한 포식의 정수",
            "unit": "개"
          }
        ],
        "quantity_guaranteed": [
          {
            "contents": {
              "max_amount": 10,
              "min_amount": 3,
              "name": "금괴 1kG",
              "unit": "개"
            },
            "max_amount": 5,
            "min_amount": 4,
            "name": "금괴 상자",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "영롱한 포식의 기원",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "발크스의 조언 (+100)",
            "unit": "개"
          },
          {
            "max_amount": 30,
            "min_amount": 25,
            "name": "자연의 흔적",
            "unit": "개"
          },
          {
            "max_amount": 65,
            "min_amount": 60,
            "name": "봉인된 검은 마력의 수정",
            "unit": "개"
          },
          {
            "max_amount": 130,
            "min_amount": 125,
            "name": "블랙스톤",
            "unit": "개"
          }
        ]
      }
    },
    "23": {
      "first_clear_reward": {
        "guaranteed": [
          {
            "amount": 3,
            "contents": {
              "max_amount": 10,
              "min_amount": 3,
              "name": "금괴 1kG",
              "unit": "개"
            },
            "name": "금괴 상자",
            "unit": "개"
          },
          {
            "amount": 2,
            "name": "영롱한 포식의 기원",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "발크스의 조언 (+200)",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "피의 제단 : 제23의 환상",
            "unit": "지식"
          }
        ]
      },
      "recommended_ap": 410,
      "recommended_dp": 470,
      "recommended_final_ap": 2200,
      "recommended_final_dp": 815,
      "weekly_reward": {
        "chance_based": [
          {
            "amount": 14,
            "contents": {
              "max_amount": 10,
              "min_amount": 3,
              "name": "금괴 1kG",
              "unit": "개"
            },
            "name": "금괴 상자",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "발크스의 조언 (+300)",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "발크스의 조언 (+250)",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "발크스의 조언 (+200)",
            "unit": "개"
          },
          {
            "amount": 4,
            "name": "영롱한 포식의 기원",
            "unit": "개"
          },
          {
            "amount": 9,
            "name": "영롱한 포식의 정수",
            "unit": "개"
          }
        ],
        "quantity_guaranteed": [
          {
            "amount": 5,
            "contents": {
              "max_amount": 10,
              "min_amount": 3,
              "name": "금괴 1kG",
              "unit": "개"
            },
            "name": "금괴 상자",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "영롱한 포식의 기원",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "발크스의 조언 (+100)",
            "unit": "개"
          },
          {
            "max_amount": 31,
            "min_amount": 26,
            "name": "자연의 흔적",
            "unit": "개"
          },
          {
            "max_amount": 70,
            "min_amount": 65,
            "name": "봉인된 검은 마력의 수정",
            "unit": "개"
          },
          {
            "max_amount": 135,
            "min_amount": 130,
            "name": "블랙스톤",
            "unit": "개"
          }
        ]
      }
    },
    "24": {
      "first_clear_reward": {
        "guaranteed": [
          {
            "amount": 3,
            "contents": {
              "max_amount": 10,
              "min_amount": 3,
              "name": "금괴 1kG",
              "unit": "개"
            },
            "name": "금괴 상자",
            "unit": "개"
          },
          {
            "amount": 2,
            "name": "영롱한 포식의 기원",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "발크스의 조언 (+200)",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "피의 제단 : 제24의 환상",
            "unit": "지식"
          }
        ]
      },
      "recommended_ap": 415,
      "recommended_dp": 475,
      "recommended_final_ap": 2290,
      "recommended_final_dp": 820,
      "weekly_reward": {
        "chance_based": [
          {
            "amount": 14,
            "contents": {
              "max_amount": 10,
              "min_amount": 3,
              "name": "금괴 1kG",
              "unit": "개"
            },
            "name": "금괴 상자",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "발크스의 조언 (+300)",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "발크스의 조언 (+250)",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "발크스의 조언 (+200)",
            "unit": "개"
          },
          {
            "amount": 4,
            "name": "영롱한 포식의 기원",
            "unit": "개"
          },
          {
            "amount": 9,
            "name": "영롱한 포식의 정수",
            "unit": "개"
          }
        ],
        "quantity_guaranteed": [
          {
            "contents": {
              "max_amount": 10,
              "min_amount": 3,
              "name": "금괴 1kG",
              "unit": "개"
            },
            "max_amount": 6,
            "min_amount": 5,
            "name": "금괴 상자",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "영롱한 포식의 기원",
            "unit": "개"
          },
          {
            "amount": 1,
            "name": "발크스의 조언 (+100)",
            "unit": "개"
          },
          {
            "max_amount": 32,
            "min_amount": 27,
            "name": "자연의 흔적",
            "unit": "개"
          },
          {
            "max_amount": 75,
            "min_amount": 70,
            "name": "봉인된 검은 마력의 수정",
            "unit": "개"
          },
          {
            "max_amount": 140,
            "min_amount": 135,
            "name": "블랙스톤",
            "unit": "개"
          }
        ]
      }
    }
  }
}
```

## Steps

### `blood-altar.weekly-record`

- seed_key: "blood-altar.weekly-record"
- phase: "repeat"
- order_no: 1
- title: "주간 최고 기록 진행"
- description: "주간 입장 제한 없이 도전하여 이번 주 최고 단계를 기록한다."
- checkable: false

### `blood-altar.reward-delivery`

- seed_key: "blood-altar.reward-delivery"
- phase: "reward"
- order_no: 2
- title: "주간 보상 확인"
- description: "일요일 00:00에 흑정령의 선물함으로 자동 지급되는 최고 단계 보상을 확인한다."
- checkable: false

## Schedules

### `blood-altar.reward-payout`

- seed_key: "blood-altar.reward-payout"
- rule_type: "reward_payout"
- recurrence_type: "weekly"
- weekday: 6
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "주간 최고 기록 보상 지급: 일요일 00:00 KST"

## Rewards

### `blood-altar.weekly-record-reward`

- seed_key: "blood-altar.weekly-record-reward"
- name: "주간 최고 기록 보상"
- reward_type: "weekly_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "가문당 주 1회"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "최고 단계 하나만 산정, 일요일 00:00 흑정령의 선물함 자동 지급"
- order_no: 1

### `blood-altar.first-clear-reward`

- seed_key: "blood-altar.first-clear-reward"
- name: "단계별 최초 클리어 보상"
- reward_type: "first_clear_reward"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "각 난이도 최초 클리어 시 가문당 1회; 주간 보상과 별도"
- order_no: 2

### `blood-altar.reward.stage-22-weekly`

- seed_key: "blood-altar.reward.stage-22-weekly"
- name: "22단계 주간 최고 기록 보상"
- reward_type: "weekly_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "묶음"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "정확한 확률 획득 목록과 수량 보장 범위는 blood-altar.high-tier-current의 22단계 canonical FACT 참조"
- order_no: 3

### `blood-altar.reward.stage-22-first-clear`

- seed_key: "blood-altar.reward.stage-22-first-clear"
- name: "22단계 최초 클리어 보상"
- reward_type: "first_clear_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "묶음"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "가문당 1회; 정확한 구성은 blood-altar.high-tier-current의 22단계 canonical FACT 참조"
- order_no: 4

### `blood-altar.reward.stage-23-weekly`

- seed_key: "blood-altar.reward.stage-23-weekly"
- name: "23단계 주간 최고 기록 보상"
- reward_type: "weekly_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "묶음"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "정확한 확률 획득 목록과 수량 보장 범위는 blood-altar.high-tier-current의 23단계 canonical FACT 참조"
- order_no: 5

### `blood-altar.reward.stage-23-first-clear`

- seed_key: "blood-altar.reward.stage-23-first-clear"
- name: "23단계 최초 클리어 보상"
- reward_type: "first_clear_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "묶음"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "가문당 1회; 정확한 구성은 blood-altar.high-tier-current의 23단계 canonical FACT 참조"
- order_no: 6

### `blood-altar.reward.stage-24-weekly`

- seed_key: "blood-altar.reward.stage-24-weekly"
- name: "24단계 주간 최고 기록 보상"
- reward_type: "weekly_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "묶음"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "정확한 확률 획득 목록과 수량 보장 범위는 blood-altar.high-tier-current의 24단계 canonical FACT 참조"
- order_no: 7

### `blood-altar.reward.stage-24-first-clear`

- seed_key: "blood-altar.reward.stage-24-first-clear"
- name: "24단계 최초 클리어 보상"
- reward_type: "first_clear_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "묶음"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "가문당 1회; 정확한 구성은 blood-altar.high-tier-current의 24단계 canonical FACT 참조"
- order_no: 8

## Sections

### `blood-altar.why`

- seed_key: "blood-altar.why"
- section_type: "why"
- title: "왜 하는가"
- order_no: 1

#### body_markdown

한 주 동안 달성한 최고 단계에 따른 가문 보상을 받기 위해 진행한다.

### `blood-altar.entry-and-challenge`

- seed_key: "blood-altar.entry-and-challenge"
- section_type: "common_mistakes"
- title: "입장과 파티 도전 횟수"
- order_no: 2

#### body_markdown

주간 입장 제한은 없다. 한 번 매칭되거나 결성된 파티는 최대 10회 도전하며, 횟수 소진 뒤 재매칭할 수 있다.

### `blood-altar.payout-warning`

- seed_key: "blood-altar.payout-warning"
- section_type: "common_mistakes"
- title: "입장·도전·보상 구분"
- order_no: 3

#### body_markdown

일요일 00:00 보상 지급은 체크리스트 초기화 규칙과 같은 의미가 아니다. 무제한 입장, 파티당 10회 도전, 가문당 주 1회 최고 단계 보상도 서로 다른 규칙이다.

## Related Contents

### `blood-altar.weekly-framework`

- seed_key: "blood-altar.weekly-framework"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "weekly-quest-framework"
- content_name_ko: "주간 의뢰 공통 규칙"
- content_category: "system"
- note: "일반 주간 reset과 일요일 보상 지급을 구분하기 위한 관련 시스템 항목"
- order_no: 1
- relative_path: "../contents/weekly-quest-framework.md"

## Evidence and Sources

### Current evidence

### `blood-altar.summary::blood-altar-guide`

- evidence_seed_key: "blood-altar.summary::blood-altar-guide"
- source_id: "blood-altar-guide"
- title: "피의 제단"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "blood-altar"
- claim_key: "general_mechanics"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: "3인 협동, 최고 기록 유지, 무제한 주간 입장과 주간 보상 일반 구조만 사용"
- active: true
- is_active: true

### `blood-altar.purpose::blood-altar-guide`

- evidence_seed_key: "blood-altar.purpose::blood-altar-guide"
- source_id: "blood-altar-guide"
- title: "피의 제단"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "blood-altar"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 최고 단계 보상 목적"
- active: true
- is_active: true

### `blood-altar.summary::blood-altar-challenge-2026-07-15`

- evidence_seed_key: "blood-altar.summary::blood-altar-challenge-2026-07-15"
- source_id: "blood-altar-challenge-2026-07-15"
- title: "7월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15878"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "blood-altar"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: "파티당 10회와 current 24단계, 심연의 환상 1~3 삭제"
- active: true
- is_active: true

### `blood-altar.summary::blood-altar-high-tier-2026-09-09`

- evidence_seed_key: "blood-altar.summary::blood-altar-high-tier-2026-09-09"
- source_id: "blood-altar-high-tier-2026-09-09"
- title: "9월 9일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16163"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-09"
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "blood-altar"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: "파티당 10회와 current 24단계, 심연의 환상 1~3 삭제"
- active: true
- is_active: true

### `blood-altar.requirement.challenge-allowance::blood-altar-challenge-2026-07-15`

- evidence_seed_key: "blood-altar.requirement.challenge-allowance::blood-altar-challenge-2026-07-15"
- source_id: "blood-altar-challenge-2026-07-15"
- title: "7월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15878"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "blood-altar.challenge-allowance"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "최신 패치에서 파티당 10회"
- active: true
- is_active: true

### `blood-altar.requirement.entry-limit::blood-altar-guide`

- evidence_seed_key: "blood-altar.requirement.entry-limit::blood-altar-guide"
- source_id: "blood-altar-guide"
- title: "피의 제단"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "blood-altar.entry-limit"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 입장 제한 없음"
- active: true
- is_active: true

### `blood-altar.requirement.high-tier-current::blood-altar-high-tier-2026-09-09`

- evidence_seed_key: "blood-altar.requirement.high-tier-current::blood-altar-high-tier-2026-09-09"
- source_id: "blood-altar-high-tier-2026-09-09"
- title: "9월 9일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16163"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-09"
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "blood-altar.high-tier-current"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: "Prompt Bridge가 사용하는 22~24단계 능력치·보상·삭제 경계 설명"
- active: true
- is_active: true

### `blood-altar.requirement.high-tier-current.structured::blood-altar-high-tier-2026-09-09`

- evidence_seed_key: "blood-altar.requirement.high-tier-current.structured::blood-altar-high-tier-2026-09-09"
- source_id: "blood-altar-high-tier-2026-09-09"
- title: "9월 9일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16163"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-09"
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "blood-altar.high-tier-current"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: "22~24단계 exact 능력치·보상 구조와 심연의 환상 1~3 삭제 current FACT"
- active: true
- is_active: true

### `blood-altar.requirement.level::blood-altar-guide`

- evidence_seed_key: "blood-altar.requirement.level::blood-altar-guide"
- source_id: "blood-altar-guide"
- title: "피의 제단"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "blood-altar.level"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "레벨 56 이상"
- active: true
- is_active: true

### `blood-altar.requirement.party-size::blood-altar-guide`

- evidence_seed_key: "blood-altar.requirement.party-size::blood-altar-guide"
- source_id: "blood-altar-guide"
- title: "피의 제단"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "blood-altar.party-size"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "3인 콘텐츠"
- active: true
- is_active: true

### `blood-altar.requirement.stages::blood-altar-guide`

- evidence_seed_key: "blood-altar.requirement.stages::blood-altar-guide"
- source_id: "blood-altar-guide"
- title: "피의 제단"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "blood-altar.stages"
- claim_key: "highest_clear_persists"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: "최고 클리어 기록 유지 근거만 사용; 가이드의 21단계 상한은 current 근거가 아님"
- active: true
- is_active: true

### `blood-altar.requirement.stages::blood-altar-high-tier-2026-09-09`

- evidence_seed_key: "blood-altar.requirement.stages::blood-altar-high-tier-2026-09-09"
- source_id: "blood-altar-high-tier-2026-09-09"
- title: "9월 9일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16163"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-09"
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "blood-altar.stages"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: "22~24단계 추가에 따른 current stage_count 24"
- active: true
- is_active: true

### `blood-altar.requirement.weekly-reward::blood-altar-guide`

- evidence_seed_key: "blood-altar.requirement.weekly-reward::blood-altar-guide"
- source_id: "blood-altar-guide"
- title: "피의 제단"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "blood-altar.weekly-reward-rule"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "가문당 주 1회 최고 단계만 산정"
- active: true
- is_active: true

### `blood-altar.section.entry-and-challenge::blood-altar-challenge-2026-07-15`

- evidence_seed_key: "blood-altar.section.entry-and-challenge::blood-altar-challenge-2026-07-15"
- source_id: "blood-altar-challenge-2026-07-15"
- title: "7월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15878"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "blood-altar.entry-and-challenge"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: "파티당 10회 도전과 소진 뒤 재매칭"
- active: true
- is_active: true

### `blood-altar.section.entry-and-challenge::blood-altar-guide`

- evidence_seed_key: "blood-altar.section.entry-and-challenge::blood-altar-guide"
- source_id: "blood-altar-guide"
- title: "피의 제단"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "blood-altar.entry-and-challenge"
- claim_key: "entry_rule"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: "주간 입장 제한 없음 근거만 사용; 가이드의 파티당 5회 표기는 current 근거가 아님"
- active: true
- is_active: true

### `blood-altar.section.payout-warning::blood-altar-challenge-2026-07-15`

- evidence_seed_key: "blood-altar.section.payout-warning::blood-altar-challenge-2026-07-15"
- source_id: "blood-altar-challenge-2026-07-15"
- title: "7월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15878"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "blood-altar.payout-warning"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: "파티당 10회 current 도전 규칙"
- active: true
- is_active: true

### `blood-altar.section.payout-warning::blood-altar-guide`

- evidence_seed_key: "blood-altar.section.payout-warning::blood-altar-guide"
- source_id: "blood-altar-guide"
- title: "피의 제단"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "blood-altar.payout-warning"
- claim_key: "general_rules"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: "무제한 입장, 최고 기록 보상과 일요일 지급의 분리 근거"
- active: true
- is_active: true

### `blood-altar.section.why::blood-altar-guide`

- evidence_seed_key: "blood-altar.section.why::blood-altar-guide"
- source_id: "blood-altar-guide"
- title: "피의 제단"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "blood-altar.why"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 최고 기록 보상 목적"
- active: true
- is_active: true

### `blood-altar.step.weekly-record::blood-altar-guide`

- evidence_seed_key: "blood-altar.step.weekly-record::blood-altar-guide"
- source_id: "blood-altar-guide"
- title: "피의 제단"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "blood-altar.weekly-record"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 최고 기록 기반"
- active: true
- is_active: true

### `blood-altar.reward.first-clear::blood-altar-guide`

- evidence_seed_key: "blood-altar.reward.first-clear::blood-altar-guide"
- source_id: "blood-altar-guide"
- title: "피의 제단"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "blood-altar.first-clear-reward"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "최초 클리어 보상은 주간 보상과 별도"
- active: true
- is_active: true

### `blood-altar.reward.stage-22-first-clear::blood-altar-high-tier-2026-09-09`

- evidence_seed_key: "blood-altar.reward.stage-22-first-clear::blood-altar-high-tier-2026-09-09"
- source_id: "blood-altar-high-tier-2026-09-09"
- title: "9월 9일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16163"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-09"
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "blood-altar.reward.stage-22-first-clear"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: "22단계 최초 클리어 보상 묶음"
- active: true
- is_active: true

### `blood-altar.reward.stage-22-weekly::blood-altar-high-tier-2026-09-09`

- evidence_seed_key: "blood-altar.reward.stage-22-weekly::blood-altar-high-tier-2026-09-09"
- source_id: "blood-altar-high-tier-2026-09-09"
- title: "9월 9일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16163"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-09"
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "blood-altar.reward.stage-22-weekly"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: "22단계 주간 최고 기록 보상 묶음"
- active: true
- is_active: true

### `blood-altar.reward.stage-23-first-clear::blood-altar-high-tier-2026-09-09`

- evidence_seed_key: "blood-altar.reward.stage-23-first-clear::blood-altar-high-tier-2026-09-09"
- source_id: "blood-altar-high-tier-2026-09-09"
- title: "9월 9일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16163"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-09"
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "blood-altar.reward.stage-23-first-clear"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: "23단계 최초 클리어 보상 묶음"
- active: true
- is_active: true

### `blood-altar.reward.stage-23-weekly::blood-altar-high-tier-2026-09-09`

- evidence_seed_key: "blood-altar.reward.stage-23-weekly::blood-altar-high-tier-2026-09-09"
- source_id: "blood-altar-high-tier-2026-09-09"
- title: "9월 9일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16163"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-09"
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "blood-altar.reward.stage-23-weekly"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: "23단계 주간 최고 기록 보상 묶음"
- active: true
- is_active: true

### `blood-altar.reward.stage-24-first-clear::blood-altar-high-tier-2026-09-09`

- evidence_seed_key: "blood-altar.reward.stage-24-first-clear::blood-altar-high-tier-2026-09-09"
- source_id: "blood-altar-high-tier-2026-09-09"
- title: "9월 9일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16163"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-09"
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "blood-altar.reward.stage-24-first-clear"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: "24단계 최초 클리어 보상 묶음"
- active: true
- is_active: true

### `blood-altar.reward.stage-24-weekly::blood-altar-high-tier-2026-09-09`

- evidence_seed_key: "blood-altar.reward.stage-24-weekly::blood-altar-high-tier-2026-09-09"
- source_id: "blood-altar-high-tier-2026-09-09"
- title: "9월 9일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16163"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-09"
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "blood-altar.reward.stage-24-weekly"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-09"
- evidence_note: "24단계 주간 최고 기록 보상 묶음"
- active: true
- is_active: true

### `blood-altar.reward.weekly-record::blood-altar-guide`

- evidence_seed_key: "blood-altar.reward.weekly-record::blood-altar-guide"
- source_id: "blood-altar-guide"
- title: "피의 제단"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "blood-altar.weekly-record-reward"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주간 최고 단계 보상"
- active: true
- is_active: true

### `blood-altar.schedule.reward-payout::blood-altar-guide`

- evidence_seed_key: "blood-altar.schedule.reward-payout::blood-altar-guide"
- source_id: "blood-altar-guide"
- title: "피의 제단"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "blood-altar.reward-payout"
- claim_key: "schedule.reward_payout"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일요일 00:00 자동 지급"
- active: true
- is_active: true

### Historical / inactive evidence

### `blood-altar.history.challenge-five::blood-altar-guide`

- evidence_seed_key: "blood-altar.history.challenge-five::blood-altar-guide"
- source_id: "blood-altar-guide"
- title: "피의 제단"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-09T15:08:14+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "blood-altar.challenge-allowance"
- claim_key: "historical_value"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "가이드의 5회는 2026-07-15 패치로 대체됨"
- active: false
- is_active: false
