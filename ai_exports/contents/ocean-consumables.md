<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 현행 항해·교역 소비품

## Identity

- slug: "ocean-consumables"
- name_ko: "현행 항해·교역 소비품"
- category: "ocean_guide"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "2026-08-26 추가된 오킬루아 파도 정식과 대양 영약 3종의 공식 효과·지속시간·제작식."
- purpose: "항해·교역 도핑 효과와 조합을 추측 없이 공식 값으로 참조한다."

## Requirements

### `ocean-consumables.wave-meal`

- seed_key: "ocean-consumables.wave-meal"
- kind: "item"
- requirement_level: "required"
- title: "오킬루아 파도 정식"
- description: "오킬루아 파도 정식의 공식 효과·지속시간·재사용 대기시간과 제작식."
- structured_value:

```json
{
  "effects": {
    "cooldown_minutes": 30,
    "duration_minutes": 600,
    "교역 경험치 획득량_percent": 25,
    "선원 획득 경험치_percent": 10,
    "항해 경험치 획득량_percent": 25,
    "항해 숙련도": 50
  },
  "recipe": {
    "inputs": {
      "고래고기 샐러드": 3,
      "마고리아 해물 특식": 3,
      "테프 빵": 3,
      "해양 괴수의 붉은빛 생선살": 1
    },
    "overwrites": "크론 정식류 버프",
    "process": "간이요리"
  }
}
```

### `ocean-consumables.ocean-elixir`

- seed_key: "ocean-consumables.ocean-elixir"
- kind: "item"
- requirement_level: "required"
- title: "대양의 영약"
- description: "대양의 영약의 공식 효과·지속시간·재사용 대기시간과 제작식."
- structured_value:

```json
{
  "effects": {
    "cooldown_seconds": 10,
    "duration_minutes": 180,
    "교역 경험치 획득량_percent": 20,
    "선원 획득 경험치_percent": 10,
    "항해 경험치 획득량_percent": 20
  },
  "recipe": {
    "inputs": {
      "세월의 비약": 36,
      "숙련의 비약": 36,
      "저무는 달의 눈물": 10,
      "친화의 비약": 36
    },
    "process": "간이연금"
  }
}
```

### `ocean-consumables.wide-ocean-elixir`

- seed_key: "ocean-consumables.wide-ocean-elixir"
- kind: "item"
- requirement_level: "required"
- title: "넓은 대양의 영약"
- description: "넓은 대양의 영약의 공식 효과·지속시간·재사용 대기시간과 제작식."
- structured_value:

```json
{
  "effects": {
    "cooldown_seconds": 10,
    "duration_minutes": 360,
    "교역 경험치 획득량_percent": 20,
    "선원 획득 경험치_percent": 10,
    "항해 경험치 획득량_percent": 20
  },
  "recipe": {
    "inputs": {
      "세월의 비약": 72,
      "숙련의 비약": 72,
      "일렁이는 바람의 조각": 1,
      "저무는 달의 눈물": 20,
      "친화의 비약": 72
    },
    "process": "간이연금"
  }
}
```

### `ocean-consumables.vast-ocean-elixir`

- seed_key: "ocean-consumables.vast-ocean-elixir"
- kind: "item"
- requirement_level: "required"
- title: "드넓은 대양의 영약"
- description: "드넓은 대양의 영약의 공식 효과·지속시간·재사용 대기시간과 제작식."
- structured_value:

```json
{
  "effects": {
    "cooldown_seconds": 10,
    "duration_minutes": 600,
    "교역 경험치 획득량_percent": 25,
    "선원 획득 경험치_percent": 15,
    "항해 경험치 획득량_percent": 25,
    "항해 숙련도": 50
  },
  "recipe": {
    "process": "간이연금",
    "recipes": [
      {
        "대양의 영약": 4,
        "대양의 정수": 1
      },
      {
        "넓은 대양의 영약": 2,
        "대양의 정수": 1
      }
    ]
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

### `ocean-consumables.relation.rinbach`

- seed_key: "ocean-consumables.relation.rinbach"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "rinbach-colony"
- content_name_ko: "린바크 군락지"
- content_category: "ocean_combat"
- note: "붉은빛 생선살과 대양의 정수 획득 경로"
- order_no: 1
- relative_path: "../contents/rinbach-colony.md"
### `hollow-maretta.relation.consumables`

- seed_key: "hollow-maretta.relation.consumables"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "hollow-maretta"
- content_name_ko: "공허한 마레타"
- content_category: "ocean_guide"
- note: "대양의 정수 획득처"
- order_no: 2
- relative_path: "../contents/hollow-maretta.md"
### `rinbach-colony.relation.consumables`

- seed_key: "rinbach-colony.relation.consumables"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "rinbach-colony"
- content_name_ko: "린바크 군락지"
- content_category: "ocean_combat"
- note: "오킬루아 파도 정식 재료인 붉은빛 생선살"
- order_no: 4
- relative_path: "../contents/rinbach-colony.md"
### `sailing-onboarding-strategy.consumables`

- seed_key: "sailing-onboarding-strategy.consumables"
- direction: "incoming"
- relation_type: "related"
- content_slug: "sailing-onboarding-strategy"
- content_name_ko: "항해 입문 운영 전략"
- content_category: "ocean_guide"
- note: "출항 보급품"
- order_no: 5
- relative_path: "../contents/sailing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `ocean-consumables.evidence.ocean-elixir::ocean-progression-2026-08-26`

- evidence_seed_key: "ocean-consumables.evidence.ocean-elixir::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ocean-consumables.ocean-elixir"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "대양의 영약의 공식 효과·지속시간·재사용 대기시간과 제작식."
- active: true
- is_active: true

### `ocean-consumables.evidence.vast-ocean-elixir::ocean-progression-2026-08-26`

- evidence_seed_key: "ocean-consumables.evidence.vast-ocean-elixir::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ocean-consumables.vast-ocean-elixir"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "드넓은 대양의 영약의 공식 효과·지속시간·재사용 대기시간과 제작식."
- active: true
- is_active: true

### `ocean-consumables.evidence.wave-meal::ocean-progression-2026-08-26`

- evidence_seed_key: "ocean-consumables.evidence.wave-meal::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ocean-consumables.wave-meal"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "오킬루아 파도 정식의 공식 효과·지속시간·재사용 대기시간과 제작식."
- active: true
- is_active: true

### `ocean-consumables.evidence.wide-ocean-elixir::ocean-progression-2026-08-26`

- evidence_seed_key: "ocean-consumables.evidence.wide-ocean-elixir::ocean-progression-2026-08-26"
- source_id: "ocean-progression-2026-08-26"
- title: "8월 26일(수) 업데이트 안내 (최종 수정 : 2026-09-02 10:47)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16107"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-26"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ocean-consumables.wide-ocean-elixir"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "넓은 대양의 영약의 공식 효과·지속시간·재사용 대기시간과 제작식."
- active: true
- is_active: true

### Historical / inactive evidence

- None
