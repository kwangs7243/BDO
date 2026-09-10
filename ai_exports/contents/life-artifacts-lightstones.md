<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 생활 유물과 광명석

## Identity

- slug: "life-artifacts-lightstones"
- name_ko: "생활 유물과 광명석"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "유물 2개에 각 2개씩 총 4개 광명석을 장착하며, 생활 공통 효과도 유물을 장착한 생활 분야에만 적용된다."
- purpose: "2026-09-02 이후의 생활 광명석 조합과 실제 활동별 효과 적용 규칙을 제공한다."

## Requirements

### `life-artifacts-lightstones.socket-model`

- seed_key: "life-artifacts-lightstones.socket-model"
- kind: "gear"
- requirement_level: "required"
- title: "유물과 광명석 구조"
- description: "유물은 최대 2개, 유물당 광명석 소켓은 2개이며 총 4개 조합으로 추가 효과를 얻는다."
- structured_value:

```json
{
  "combination_effects": true,
  "max_artifacts": 2,
  "max_lightstones": 4,
  "sockets_per_artifact": 2
}
```

### `life-artifacts-lightstones.category-scope`

- seed_key: "life-artifacts-lightstones.category-scope"
- kind: "gear"
- requirement_level: "required"
- title: "생활 분야 적용 범위"
- description: "생활 공통 숙련도·경험치 효과도 유물이 장착된 생활 분야에만 적용된다."
- structured_value:

```json
{
  "applies_to_all_life_categories_simultaneously": false,
  "common_effect_scope": "equipped_life_category_only"
}
```

### `life-artifacts-lightstones.effect-taxonomy`

- seed_key: "life-artifacts-lightstones.effect-taxonomy"
- kind: "gear"
- requirement_level: "required"
- title: "분야별 허용 효과"
- description: "통합 장비 표에 따른 생활 분야별 효과 분류다."
- structured_value:

```json
{
  "alchemy": [
    "연금 숙련도",
    "연금 경험치",
    "연금 시간 감소"
  ],
  "common": [
    "생활 숙련도",
    "생활 경험치"
  ],
  "cooking": [
    "요리 숙련도",
    "요리 경험치",
    "요리 시간 감소"
  ],
  "farming": [
    "재배 공식 현재 효과"
  ],
  "fishing": [
    "낚시 숙련도",
    "낚시 경험치",
    "낚시 잠재력",
    "자동 낚시 시간 감소",
    "특정 어종 확률"
  ],
  "gathering": [
    "채집 숙련도",
    "채집 경험치",
    "채집 잠재력",
    "모든 채집물 획득 확률"
  ],
  "hunting": [
    "수렵 숙련도",
    "수렵 경험치"
  ],
  "processing": [
    "가공 숙련도",
    "가공 경험치",
    "가공 성공률"
  ],
  "sailing_barter": [
    "항해 숙련도",
    "항해 경험치",
    "교역 경험치",
    "선원 경험치"
  ],
  "trading": [
    "무역 숙련도",
    "무역 경험치"
  ],
  "training": [
    "조련 숙련도",
    "조련 경험치",
    "탑승물 경험치"
  ]
}
```

### `life-artifacts-lightstones.current-combinations`

- seed_key: "life-artifacts-lightstones.current-combinations"
- kind: "gear"
- requirement_level: "required"
- title: "현재 생활 조합 원칙"
- description: "현재 생활 광명석 조합식은 풀의 광명석 또는 오색빛 광명석과 호환되는 9/2 표만 사용한다."
- structured_value:

```json
{
  "allowed_families": [
    "풀의 광명석",
    "오색빛 광명석"
  ],
  "deleted_combinations": [
    "송곳니",
    "대장장이의 축복",
    "개운한 꿈"
  ],
  "old_fire_wind_recipes_current": false,
  "representative_categories": [
    "생활 경험치",
    "생활 숙련도",
    "채집",
    "낚시",
    "수렵",
    "요리",
    "연금",
    "가공",
    "조련",
    "항해"
  ],
  "representative_current_recipes": [
    {
      "category": "생활 경험치",
      "effect": [
        "생활 경험치 획득량 +17%"
      ],
      "name": "델로티아",
      "recipe": [
        "풀의 광명석 : 야생",
        "풀의 광명석 : 야생",
        "풀의 광명석 : 야생",
        "오색빛 광명석"
      ]
    },
    {
      "category": "생활 숙련도",
      "effect": [
        "생활 숙련도 +30"
      ],
      "name": "마노스의 손",
      "recipe": [
        "풀의 광명석 : 낙원",
        "풀의 광명석 : 낙원",
        "풀의 광명석 : 낙원",
        "오색빛 광명석"
      ]
    },
    {
      "category": "채집",
      "effect": [
        "모든 채집물 획득 확률 증가 +10%",
        "채집 경험치 획득량 +10%",
        "채집 숙련도 +20",
        "채집 속도 잠재력 +1단계"
      ],
      "name": "하품하는 고슴도치",
      "recipe": [
        "풀의 광명석 : 초원",
        "풀의 광명석 : 숲",
        "풀의 광명석 : 야생",
        "오색빛 광명석"
      ]
    },
    {
      "category": "낚시",
      "effect": [
        "자동 낚시 시간 -15%",
        "낚시 경험치 획득량 +10%",
        "낚시 숙련도 +20",
        "낚시 속도 잠재력 +1단계"
      ],
      "name": "신의 입질",
      "recipe": [
        "풀의 광명석 : 기회",
        "풀의 광명석 : 세월",
        "풀의 광명석 : 기회",
        "오색빛 광명석"
      ]
    },
    {
      "category": "수렵",
      "effect": [
        "화승총 재장전 속도 +10%",
        "수렵 경험치 획득량 +10%",
        "수렵 숙련도 +20"
      ],
      "name": "눈 깜짝할 사이",
      "recipe": [
        "풀의 광명석 : 덫",
        "풀의 광명석 : 추적",
        "풀의 광명석 : 추적",
        "오색빛 광명석"
      ]
    },
    {
      "category": "요리",
      "effect": [
        "요리 시간 -2초",
        "요리 경험치 획득량 +10%",
        "요리 숙련도 +25"
      ],
      "name": "요리의 정석",
      "recipe": [
        "풀의 광명석 : 비법",
        "풀의 광명석 : 배합",
        "풀의 광명석 : 배합",
        "오색빛 광명석"
      ]
    },
    {
      "category": "연금",
      "effect": [
        "연금 시간 -2초",
        "연금 경험치 획득량 +10%",
        "연금 숙련도 +25"
      ],
      "name": "별 한 조각, 달 한 스푼",
      "recipe": [
        "풀의 광명석 : 시간",
        "풀의 광명석 : 연성",
        "풀의 광명석 : 연성",
        "오색빛 광명석"
      ]
    },
    {
      "category": "가공",
      "effect": [
        "가공 성공률 +20%",
        "가공 경험치 획득량 +10%",
        "가공 숙련도 +25"
      ],
      "name": "뚝딱뚝딱",
      "recipe": [
        "풀의 광명석 : 도구",
        "풀의 광명석 : 재량",
        "풀의 광명석 : 재량",
        "오색빛 광명석"
      ]
    },
    {
      "category": "조련",
      "effect": [
        "조련 숙련도 -500",
        "조련 경험치 획득량 +35%"
      ],
      "name": "선택과 집중 : 조련",
      "recipe": [
        "풀의 광명석 : 질주",
        "풀의 광명석 : 질주",
        "풀의 광명석 : 야생",
        "오색빛 광명석"
      ]
    },
    {
      "category": "항해",
      "effect": [
        "항해 숙련도 -500",
        "항해 경험치 획득량 +35%"
      ],
      "name": "선택과 집중 : 항해",
      "recipe": [
        "풀의 광명석 : 미지",
        "풀의 광명석 : 미지",
        "풀의 광명석 : 야생",
        "오색빛 광명석"
      ]
    }
  ],
  "yawning_hedgehog_energy_regeneration_removed": true
}
```

### `life-artifacts-lightstones.activity-selection`

- seed_key: "life-artifacts-lightstones.activity-selection"
- kind: "gear"
- requirement_level: "required"
- title: "실제 활동별 자동 적용"
- description: "현재 수행 중인 활동에 맞는 유물 효과가 자동 적용되며 수렵 후 도축에는 유효한 채집 획득 확률만 적용된다."
- structured_value:

```json
{
  "hunting_butchering": {
    "invalid": [
      "gathering_exp",
      "gathering_mastery"
    ],
    "valid": [
      "gathering_item_acquisition_rate"
    ]
  },
  "hunting_kill": "hunting_effects",
  "selection_basis": "actual_activity"
}
```

### `life-artifacts-lightstones.magahan`

- seed_key: "life-artifacts-lightstones.magahan"
- kind: "item"
- requirement_level: "required"
- title: "마가한의 유물"
- description: "생활 특화 유물이며 통합 거래소 거래가 가능하고 공식 재료로 공작한다."
- structured_value:

```json
{
  "ingredients": [
    {
      "amount": 100,
      "item": "마가한의 파편"
    },
    {
      "amount": 100,
      "item": "순수한 자철석 결정"
    },
    {
      "amount": 100,
      "item": "순수한 대리석"
    }
  ],
  "marketplace_tradeable": true,
  "method": "공작"
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `life-artifacts-lightstones.stale-recipes`

- seed_key: "life-artifacts-lightstones.stale-recipes"
- section_type: "common_mistakes"
- title: "9월 2일 이전 조합식 주의"
- order_no: 1

#### body_markdown

불·바람 등 비생활 계열 광명석이 들어간 과거 생활 조합식을 현재 recipe로 병합하지 않는다. 송곳니, 대장장이의 축복, 개운한 꿈은 삭제된 조합이다.

### `life-artifacts-lightstones.activity-example`

- seed_key: "life-artifacts-lightstones.activity-example"
- section_type: "strategy"
- title: "수렵과 도축의 적용 구분"
- order_no: 2

#### body_markdown

수렵 몬스터 처치는 수렵 효과를 사용한다. 처치 후 도축은 채집 영역 중 해당 행위에 유효한 모든 채집물 획득 확률은 적용하지만 채집 경험치·숙련도를 적용하지 않는다.

## Related Contents

### `life-artifacts-lightstones.integrated-equipment`

- seed_key: "life-artifacts-lightstones.integrated-equipment"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "life-common-gear"
- content_name_ko: "생활 통합 장비"
- content_category: "life"
- note: "유물·광명석은 생활 분야별 장비다."
- order_no: 1
- relative_path: "../contents/life-common-gear.md"
### `life-artifacts-lightstones.ocean-crystals`

- seed_key: "life-artifacts-lightstones.ocean-crystals"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sea-crystals"
- content_name_ko: "해원석 progression"
- content_category: "ocean_project"
- note: "생활 광명석과 선박용 해원석은 서로 다른 장비 체계다."
- order_no: 2
- relative_path: "../contents/sea-crystals.md"
### `combat-artifacts.life-system`

- seed_key: "combat-artifacts.life-system"
- direction: "incoming"
- relation_type: "related"
- content_slug: "combat-artifacts"
- content_name_ko: "전투 유물"
- content_category: "combat_pve"
- note: "생활 유물과 같은 장착 기반을 쓰지만 전투 수치와 조합을 별도 관리한다."
- order_no: 1
- relative_path: "../contents/combat-artifacts.md"
### `energy-foundation.artifact-effects`

- seed_key: "energy-foundation.artifact-effects"
- direction: "incoming"
- relation_type: "related"
- content_slug: "energy-foundation"
- content_name_ko: "기운 기반"
- content_category: "life"
- note: "9월 2일 삭제·변경된 기운 관련 광명석 효과와 연결한다."
- order_no: 1
- relative_path: "../contents/energy-foundation.md"
### `life-common-gear.artifacts`

- seed_key: "life-common-gear.artifacts"
- direction: "incoming"
- relation_type: "related"
- content_slug: "life-common-gear"
- content_name_ko: "생활 통합 장비"
- content_category: "life"
- note: "분야별 생활 유물·광명석 슬롯"
- order_no: 2
- relative_path: "../contents/life-common-gear.md"

## Evidence and Sources

### Current evidence

### `life-artifacts-lightstones.summary::artifact-guide`

- evidence_seed_key: "life-artifacts-lightstones.summary::artifact-guide"
- source_id: "artifact-guide"
- title: "유물/광명석"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=272"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-artifacts-lightstones"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "유물 기본 구조와 최신 분야 적용"
- active: true
- is_active: true

### `life-artifacts-lightstones.summary::life-unification-2026-09-02`

- evidence_seed_key: "life-artifacts-lightstones.summary::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-artifacts-lightstones"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "유물 기본 구조와 최신 분야 적용"
- active: true
- is_active: true

### `life-artifacts-lightstones.requirement.activity-selection::life-unification-2026-09-02`

- evidence_seed_key: "life-artifacts-lightstones.requirement.activity-selection::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-artifacts-lightstones.activity-selection"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "실제 활동 기준 자동 적용"
- active: true
- is_active: true

### `life-artifacts-lightstones.requirement.category-scope::life-unification-2026-09-02`

- evidence_seed_key: "life-artifacts-lightstones.requirement.category-scope::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-artifacts-lightstones.category-scope"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "장착 생활 분야 한정"
- active: true
- is_active: true

### `life-artifacts-lightstones.requirement.current-combinations::life-unification-2026-09-02`

- evidence_seed_key: "life-artifacts-lightstones.requirement.current-combinations::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-artifacts-lightstones.current-combinations"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "풀·오색빛 계열 조합과 삭제 조합"
- active: true
- is_active: true

### `life-artifacts-lightstones.requirement.effect-taxonomy::life-unification-2026-09-02`

- evidence_seed_key: "life-artifacts-lightstones.requirement.effect-taxonomy::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-artifacts-lightstones.effect-taxonomy"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "공식 장착 가능 효과 표"
- active: true
- is_active: true

### `life-artifacts-lightstones.requirement.magahan::artifact-guide`

- evidence_seed_key: "life-artifacts-lightstones.requirement.magahan::artifact-guide"
- source_id: "artifact-guide"
- title: "유물/광명석"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=272"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-artifacts-lightstones.magahan"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "마가한의 유물 거래·공작 재료"
- active: true
- is_active: true

### `life-artifacts-lightstones.requirement.socket-model::artifact-guide`

- evidence_seed_key: "life-artifacts-lightstones.requirement.socket-model::artifact-guide"
- source_id: "artifact-guide"
- title: "유물/광명석"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=272"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-artifacts-lightstones.socket-model"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "유물 2개와 광명석 4개"
- active: true
- is_active: true

### Historical / inactive evidence

### `life-artifacts-lightstones.legacy.pre-september-recipes::life-unification-2026-09-02`

- evidence_seed_key: "life-artifacts-lightstones.legacy.pre-september-recipes::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-artifacts-lightstones"
- claim_key: "legacy.lightstone_recipes"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "9월 2일 이전 불·바람 포함 생활 조합식은 현재 표로 대체됨"
- active: false
- is_active: false
