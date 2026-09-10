<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 청명의 보주

## Identity

- slug: "cheongmyeong-orb"
- name_ko: "청명의 보주"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "청명의 결정으로 제작·강화하는 전역 생활 경험치 장비이며, 삭제된 새벽의 수정 3종을 대체한다."
- purpose: "결정 제작, 결정↔보주 변환, 100% 강화와 단계별 효과를 구분해 제공한다."

## Requirements

### `cheongmyeong-orb.global-slot`

- seed_key: "cheongmyeong-orb.global-slot"
- kind: "gear"
- requirement_level: "required"
- title: "전역 생활 장비"
- description: "청명의 보주는 전역 생활 슬롯에 하나를 장착해 모든 생활 분야에 적용한다."
- structured_value:

```json
{
  "applies_to_all_life_categories": true,
  "max_equipped": 1,
  "slot_scope": "global_life_equipment"
}
```

### `cheongmyeong-orb.crystal-recipe`

- seed_key: "cheongmyeong-orb.crystal-recipe"
- kind: "item"
- requirement_level: "required"
- title: "청명의 결정 제작"
- description: "새벽의 정수 1개, 자연의 흔적 30개, 마력의 광명석 결정 500개를 가열해 청명의 결정 1개를 만든다."
- structured_value:

```json
{
  "ingredients": [
    {
      "amount": 1,
      "item": "새벽의 정수"
    },
    {
      "amount": 30,
      "item": "자연의 흔적"
    },
    {
      "amount": 500,
      "item": "마력의 광명석 결정"
    }
  ],
  "method": "가열하기",
  "output": {
    "amount": 1,
    "item": "청명의 결정"
  }
}
```

### `cheongmyeong-orb.reversible-conversion`

- seed_key: "cheongmyeong-orb.reversible-conversion"
- kind: "item"
- requirement_level: "required"
- title: "결정과 보주 변환"
- description: "청명의 결정 1개와 청명의 보주 1개는 간이연금으로 양방향 변환한다."
- structured_value:

```json
{
  "crystal_amount": 1,
  "heating_for_crystal_to_orb": false,
  "method": "간이연금",
  "orb_amount": 1,
  "reversible": true
}
```

### `cheongmyeong-orb.enhancement`

- seed_key: "cheongmyeong-orb.enhancement"
- kind: "gear"
- requirement_level: "required"
- title: "보주 강화"
- description: "청명의 결정으로 강화하며 모든 단계의 성공 확률은 100%다."
- structured_value:

```json
{
  "material": "청명의 결정",
  "rows": [
    {
      "crystal_count": 1,
      "life_exp_percent": 4,
      "stage": 0
    },
    {
      "crystal_count": 1,
      "life_exp_percent": 8,
      "stage": 1
    },
    {
      "crystal_count": 1,
      "life_exp_percent": 12,
      "stage": 2
    },
    {
      "crystal_count": 1,
      "life_exp_percent": 16,
      "stage": 3
    },
    {
      "crystal_count": 1,
      "life_exp_percent": 20,
      "stage": 4
    },
    {
      "crystal_count": 1,
      "life_exp_percent": 24,
      "stage": 5
    },
    {
      "crystal_count": 6,
      "life_exp_percent": 30,
      "stage": 6
    },
    {
      "crystal_count": 6,
      "life_exp_percent": 36,
      "stage": 7
    },
    {
      "crystal_count": 6,
      "life_exp_percent": 42,
      "stage": 8
    },
    {
      "crystal_count": 6,
      "life_exp_percent": 48,
      "stage": 9
    },
    {
      "crystal_count": 20,
      "life_exp_percent": 55,
      "stage": 10
    },
    {
      "crystal_count": 20,
      "life_exp_percent": 62,
      "stage": 11
    },
    {
      "crystal_count": 20,
      "life_exp_percent": 69,
      "stage": 12
    },
    {
      "crystal_count": 20,
      "life_exp_percent": 76,
      "stage": 13
    },
    {
      "crystal_count": 20,
      "life_exp_percent": 83,
      "stage": 14
    },
    {
      "crystal_count": 20,
      "life_exp_percent": 90,
      "stage": 15
    }
  ],
  "success_percent": 100
}
```

### `cheongmyeong-orb.replacement`

- seed_key: "cheongmyeong-orb.replacement"
- kind: "gear"
- requirement_level: "required"
- title: "삭제 수정 대체"
- description: "진·본·원 새벽의 수정 - 생활 경험치는 삭제됐고 현재 장비는 청명의 보주다."
- structured_value:

```json
{
  "current_equipment": "청명의 보주",
  "removed_current_equipment": [
    "진 새벽의 수정 - 생활 경험치",
    "본 새벽의 수정 - 생활 경험치",
    "원 새벽의 수정 - 생활 경험치"
  ],
  "removed_equipment_active_count": 0
}
```

### `cheongmyeong-orb.migration-compensation`

- seed_key: "cheongmyeong-orb.migration-compensation"
- kind: "item"
- requirement_level: "required"
- title: "2026-09-02 전환 보상"
- description: "삭제 당시 지급된 청명의 결정 수량은 과거 전환 보상이며 현재 일반 획득법이 아니다."
- structured_value:

```json
{
  "compensation": [
    {
      "crystals": 25,
      "removed": "진"
    },
    {
      "crystals": 5,
      "removed": "본"
    },
    {
      "crystals": 1,
      "removed": "원"
    }
  ],
  "general_acquisition_method": false,
  "historical_only": true
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `cheongmyeong-orb.processing-warning`

- seed_key: "cheongmyeong-orb.processing-warning"
- section_type: "common_mistakes"
- title: "가공 방식 분리"
- order_no: 1

#### body_markdown

재료에서 청명의 결정을 만들 때는 가열하기를 사용한다. 청명의 결정과 청명의 보주 사이의 양방향 변환은 간이연금이다.

## Related Contents

### `cheongmyeong-orb.integrated-equipment`

- seed_key: "cheongmyeong-orb.integrated-equipment"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "life-common-gear"
- content_name_ko: "생활 통합 장비"
- content_category: "life"
- note: "청명의 보주는 전체 생활에 적용되는 전역 슬롯이다."
- order_no: 1
- relative_path: "../contents/life-common-gear.md"
### `life-common-gear.cheongmyeong-orb`

- seed_key: "life-common-gear.cheongmyeong-orb"
- direction: "incoming"
- relation_type: "related"
- content_slug: "life-common-gear"
- content_name_ko: "생활 통합 장비"
- content_category: "life"
- note: "전역 청명의 보주 슬롯"
- order_no: 4
- relative_path: "../contents/life-common-gear.md"

## Evidence and Sources

### Current evidence

### `cheongmyeong-orb.summary::life-client-fix-2026-09-02`

- evidence_seed_key: "cheongmyeong-orb.summary::life-client-fix-2026-09-02"
- source_id: "life-client-fix-2026-09-02"
- title: "9월 2일(수) 최신 버전 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16144"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "cheongmyeong-orb"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "청명의 보주 역할과 최신 가공 방식"
- active: true
- is_active: true

### `cheongmyeong-orb.summary::life-unification-2026-09-02`

- evidence_seed_key: "cheongmyeong-orb.summary::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "cheongmyeong-orb"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "청명의 보주 역할과 최신 가공 방식"
- active: true
- is_active: true

### `cheongmyeong-orb.requirement.crystal-recipe::life-unification-2026-09-02`

- evidence_seed_key: "cheongmyeong-orb.requirement.crystal-recipe::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cheongmyeong-orb.crystal-recipe"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "청명의 결정 가열 제작식"
- active: true
- is_active: true

### `cheongmyeong-orb.requirement.enhancement::life-unification-2026-09-02`

- evidence_seed_key: "cheongmyeong-orb.requirement.enhancement::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cheongmyeong-orb.enhancement"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "단계별 효과·재료와 100% 성공"
- active: true
- is_active: true

### `cheongmyeong-orb.requirement.global-slot::life-unification-2026-09-02`

- evidence_seed_key: "cheongmyeong-orb.requirement.global-slot::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cheongmyeong-orb.global-slot"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "전역 생활 장비 슬롯"
- active: true
- is_active: true

### `cheongmyeong-orb.requirement.migration-compensation::life-unification-2026-09-02`

- evidence_seed_key: "cheongmyeong-orb.requirement.migration-compensation::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cheongmyeong-orb.migration-compensation"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "삭제 당시 전환 보상"
- active: true
- is_active: true

### `cheongmyeong-orb.requirement.replacement::life-unification-2026-09-02`

- evidence_seed_key: "cheongmyeong-orb.requirement.replacement::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cheongmyeong-orb.replacement"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "새벽 생활 경험치 수정 3종 삭제"
- active: true
- is_active: true

### `cheongmyeong-orb.requirement.reversible-conversion::life-client-fix-2026-09-02`

- evidence_seed_key: "cheongmyeong-orb.requirement.reversible-conversion::life-client-fix-2026-09-02"
- source_id: "life-client-fix-2026-09-02"
- title: "9월 2일(수) 최신 버전 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16144"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cheongmyeong-orb.reversible-conversion"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "결정과 보주 간이연금 양방향 변환"
- active: true
- is_active: true

### `cheongmyeong-orb.requirement.reversible-conversion::life-unification-2026-09-02`

- evidence_seed_key: "cheongmyeong-orb.requirement.reversible-conversion::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "cheongmyeong-orb.reversible-conversion"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "결정과 보주 간이연금 양방향 변환"
- active: true
- is_active: true

### Historical / inactive evidence

### `cheongmyeong-orb.legacy.crystal-to-orb-heating::life-client-fix-2026-09-02`

- evidence_seed_key: "cheongmyeong-orb.legacy.crystal-to-orb-heating::life-client-fix-2026-09-02"
- source_id: "life-client-fix-2026-09-02"
- title: "9월 2일(수) 최신 버전 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16144"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "cheongmyeong-orb"
- claim_key: "legacy.crystal_to_orb_heating"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "아이템 설명의 가열하기 표시는 수정됐고 현재 변환은 간이연금"
- active: false
- is_active: false

### `cheongmyeong-orb.legacy.dawn-crystals::life-unification-2026-09-02`

- evidence_seed_key: "cheongmyeong-orb.legacy.dawn-crystals::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "cheongmyeong-orb"
- claim_key: "legacy.dawn_life_exp_crystals"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "진·본·원 새벽의 수정 - 생활 경험치는 현재 장비가 아님"
- active: false
- is_active: false
