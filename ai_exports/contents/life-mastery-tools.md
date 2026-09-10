<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 생활 숙련도 도구

## Identity

- slug: "life-mastery-tools"
- name_ko: "생활 숙련도 도구"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "낚시·수렵·요리·연금의 생활 숙련도 도구는 초록, 파랑, 마노스 등급 체계로 구성된다."
- purpose: "2025 숙련도 도구 확장과 2026 통합 장비 슬롯 기준을 기록한다."

## Requirements

### `life-mastery-tools.tiers`

- seed_key: "life-mastery-tools.tiers"
- kind: "gear"
- requirement_level: "required"
- title: "분야별 등급"
- description: "낚시 의자, 수렵 가방, 국자, 플라스크에 초록·파랑·마노스 체계가 있다."
- structured_value:

```json
{
  "blue": [
    "크리오 계열 낚시 의자",
    "로바우 수렵 가방",
    "로로주 국자",
    "고르가스 플라스크"
  ],
  "green": [
    "로기아 낚시 의자",
    "로기아 수렵 가방",
    "로기아 국자",
    "로기아 플라스크"
  ],
  "manos": [
    "마노스 낚시 의자",
    "마노스 수렵 가방",
    "마노스 국자",
    "마노스 플라스크"
  ]
}
```

### `life-mastery-tools.fixed-npc-prices`

- seed_key: "life-mastery-tools.fixed-npc-prices"
- kind: "item"
- requirement_level: "required"
- title: "고정 NPC 가격"
- description: "초록과 파랑 등급의 공식 NPC 판매 가격이며 동적 거래소 가격이 아니다."
- structured_value:

```json
{
  "blue": [
    {
      "npc": "게라노아",
      "silver": 10000000
    },
    {
      "npc": "질다",
      "silver": 15000000
    }
  ],
  "dynamic_market_price_included": false,
  "green": [
    {
      "npc": "카멜리아 로기아",
      "silver": 1000000
    },
    {
      "npc": "질다",
      "silver": 1500000
    }
  ],
  "top_tier_acquisition": "manufacture"
}
```

### `life-mastery-tools.integrated-slots`

- seed_key: "life-mastery-tools.integrated-slots"
- kind: "gear"
- requirement_level: "required"
- title: "통합 장비 슬롯"
- description: "도구는 각 실제 생활 분야의 전용 장비 슬롯에 장착한다."
- structured_value:

```json
{
  "alchemy": "플라스크",
  "cooking": "국자",
  "fishing": "낚시 의자",
  "hunting": "수렵 가방",
  "scope": "life_category_specific"
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

### `life-mastery-tools.integrated-equipment`

- seed_key: "life-mastery-tools.integrated-equipment"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "life-common-gear"
- content_name_ko: "생활 통합 장비"
- content_category: "life"
- note: "생활 분야별 장비 슬롯을 사용한다."
- order_no: 1
- relative_path: "../contents/life-common-gear.md"

## Evidence and Sources

### Current evidence

### `life-mastery-tools.summary::life-mastery-prione-2025-01-08`

- evidence_seed_key: "life-mastery-tools.summary::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-mastery-tools"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "도구 등급과 현재 통합 슬롯"
- active: true
- is_active: true

### `life-mastery-tools.summary::life-unification-2026-09-02`

- evidence_seed_key: "life-mastery-tools.summary::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-mastery-tools"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "도구 등급과 현재 통합 슬롯"
- active: true
- is_active: true

### `life-mastery-tools.requirement.fixed-npc-prices::life-mastery-prione-2025-01-08`

- evidence_seed_key: "life-mastery-tools.requirement.fixed-npc-prices::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-mastery-tools.fixed-npc-prices"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "공식 NPC 판매가 및 공작"
- active: true
- is_active: true

### `life-mastery-tools.requirement.integrated-slots::life-unification-2026-09-02`

- evidence_seed_key: "life-mastery-tools.requirement.integrated-slots::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-mastery-tools.integrated-slots"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "분야별 장비 슬롯"
- active: true
- is_active: true

### `life-mastery-tools.requirement.tiers::life-mastery-prione-2025-01-08`

- evidence_seed_key: "life-mastery-tools.requirement.tiers::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-mastery-tools.tiers"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "4개 분야 숙련도 도구 등급"
- active: true
- is_active: true

### Historical / inactive evidence

- None
