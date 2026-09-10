<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 가공석과 가공복

## Identity

- slug: "processing-stones-and-clothes"
- name_ko: "가공석과 가공복"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "현재는 통합 가공석 하나로 6종 대량가공을 처리하며 로기아·카르타·마노스 가공복이 현재 숙련도 가공복 진행이다."
- purpose: "구식 6종 가공석과 삭제된 은자수 공예가의 옷을 현재 장비에서 배제한다."

## Requirements

### `processing-stones-and-clothes.integrated-stone`

- seed_key: "processing-stones-and-clothes.integrated-stone"
- kind: "gear"
- requirement_level: "required"
- title: "통합 가공석"
- description: "하나의 현재 가공석으로 6종 대량가공을 수행한다."
- structured_value:

```json
{
  "integrated": true,
  "methods": [
    "흔들어 섞기",
    "빻기",
    "장작 패기",
    "말리기",
    "솎아내기",
    "가열하기"
  ],
  "old_six_separate_stones_required": false,
  "progression": [
    "로기아 가공석",
    "테크톤 가공석",
    "마노스 가공석"
  ]
}
```

### `processing-stones-and-clothes.current-clothes`

- seed_key: "processing-stones-and-clothes.current-clothes"
- kind: "gear"
- requirement_level: "required"
- title: "현재 숙련도 가공복"
- description: "현재 주요 가공복 진행은 로기아·카르타·마노스다."
- structured_value:

```json
{
  "progression": [
    "로기아",
    "카르타",
    "마노스"
  ],
  "silver_embroidered_craftsman_clothes_active": false
}
```

### `processing-stones-and-clothes.success-table`

- seed_key: "processing-stones-and-clothes.success-table"
- kind: "stat"
- requirement_level: "required"
- title: "가공복 성공률"
- description: "2025-08-27 공식 표의 강화 단계별 가공 성공률 증가 수치다."
- structured_value:

```json
{
  "rows": [
    {
      "Karta": 4,
      "Loggia": 3,
      "Manos": 5,
      "enhancement": "+0"
    },
    {
      "Karta": 4,
      "Loggia": 3,
      "Manos": 5,
      "enhancement": "+1"
    },
    {
      "Karta": 4,
      "Loggia": 3,
      "Manos": 5,
      "enhancement": "+2"
    },
    {
      "Karta": 4,
      "Loggia": 3,
      "Manos": 5,
      "enhancement": "+3"
    },
    {
      "Karta": 8,
      "Loggia": 6,
      "Manos": 10,
      "enhancement": "+4~+10"
    },
    {
      "Karta": 12,
      "Loggia": 9,
      "Manos": 15,
      "enhancement": "+11~+15"
    },
    {
      "Karta": 16,
      "Loggia": 12,
      "Manos": 20,
      "enhancement": "I"
    },
    {
      "Karta": 16,
      "Loggia": 12,
      "Manos": 20,
      "enhancement": "II"
    },
    {
      "Karta": 20,
      "Loggia": 15,
      "Manos": 25,
      "enhancement": "III"
    },
    {
      "Karta": 25,
      "Loggia": 20,
      "Manos": 30,
      "enhancement": "IV"
    },
    {
      "Karta": 33,
      "Loggia": 28,
      "Manos": 40,
      "enhancement": "V"
    }
  ],
  "unit": "percent"
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `processing-stones-and-clothes.legacy`

- seed_key: "processing-stones-and-clothes.legacy"
- section_type: "common_mistakes"
- title: "구식 장비 제외"
- order_no: 1

#### body_markdown

호수·원기·기운·태양·바람·용암 가공석을 각각 장착하는 구조와 은자수 공예가의 옷은 현재 progression이 아니다.

## Related Contents

### `processing-stones-and-clothes.mass`

- seed_key: "processing-stones-and-clothes.mass"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "mass-processing"
- content_name_ko: "대량가공"
- content_category: "life"
- note: "가공석은 대량가공과 연결"
- order_no: 1
- relative_path: "../contents/mass-processing.md"
### `mass-processing.stones`

- seed_key: "mass-processing.stones"
- direction: "incoming"
- relation_type: "related"
- content_slug: "mass-processing"
- content_name_ko: "대량가공"
- content_category: "life"
- note: "대량가공용 통합 가공석"
- order_no: 3
- relative_path: "../contents/mass-processing.md"
### `processing-current-system.gear`

- seed_key: "processing-current-system.gear"
- direction: "incoming"
- relation_type: "related"
- content_slug: "processing-current-system"
- content_name_ko: "가공 현재 시스템"
- content_category: "life"
- note: "가공석·가공복"
- order_no: 3
- relative_path: "../contents/processing-current-system.md"
### `processing-onboarding-strategy.gear`

- seed_key: "processing-onboarding-strategy.gear"
- direction: "incoming"
- relation_type: "related"
- content_slug: "processing-onboarding-strategy"
- content_name_ko: "가공 입문 전략"
- content_category: "life"
- note: null
- order_no: 3
- relative_path: "../contents/processing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `processing-stones-and-clothes.summary::life-clothes-2025-08-27`

- evidence_seed_key: "processing-stones-and-clothes.summary::life-clothes-2025-08-27"
- source_id: "life-clothes-2025-08-27"
- title: "8월 27일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14434"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-08-27"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "processing-stones-and-clothes"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "현재 가공석·가공복"
- active: true
- is_active: true

### `processing-stones-and-clothes.summary::processing-stone-history`

- evidence_seed_key: "processing-stones-and-clothes.summary::processing-stone-history"
- source_id: "processing-stone-history"
- title: "가공석 통합"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=8452"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "processing-stones-and-clothes"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "현재 가공석·가공복"
- active: true
- is_active: true

### `processing-stones-and-clothes.requirement.current-clothes::life-clothes-2025-08-27`

- evidence_seed_key: "processing-stones-and-clothes.requirement.current-clothes::life-clothes-2025-08-27"
- source_id: "life-clothes-2025-08-27"
- title: "8월 27일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14434"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-08-27"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "processing-stones-and-clothes.current-clothes"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "은자수 삭제와 현재 3종"
- active: true
- is_active: true

### `processing-stones-and-clothes.requirement.integrated-stone::processing-stone-history`

- evidence_seed_key: "processing-stones-and-clothes.requirement.integrated-stone::processing-stone-history"
- source_id: "processing-stone-history"
- title: "가공석 통합"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=8452"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "processing-stones-and-clothes.integrated-stone"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "가공석 통합과 6종 방식"
- active: true
- is_active: true

### `processing-stones-and-clothes.requirement.success-table::life-clothes-2025-08-27`

- evidence_seed_key: "processing-stones-and-clothes.requirement.success-table::life-clothes-2025-08-27"
- source_id: "life-clothes-2025-08-27"
- title: "8월 27일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14434"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-08-27"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "processing-stones-and-clothes.success-table"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "강화 단계별 성공률 표"
- active: true
- is_active: true

### Historical / inactive evidence

### `processing-stones-and-clothes.legacy.separate-stones::processing-stone-history`

- evidence_seed_key: "processing-stones-and-clothes.legacy.separate-stones::processing-stone-history"
- source_id: "processing-stone-history"
- title: "가공석 통합"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=8452"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "processing-stones-and-clothes"
- claim_key: "legacy.separate_processing_stones_required"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "방식별 6종 가공석 필요 규칙은 통합으로 대체"
- active: false
- is_active: false

### `processing-stones-and-clothes.legacy.silver-clothes::life-clothes-2025-08-27`

- evidence_seed_key: "processing-stones-and-clothes.legacy.silver-clothes::life-clothes-2025-08-27"
- source_id: "life-clothes-2025-08-27"
- title: "8월 27일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14434"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-08-27"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "processing-stones-and-clothes"
- claim_key: "legacy.silver_embroidered_current_progression"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "은자수 공예가의 옷은 삭제되어 현재 진행이 아님"
- active: false
- is_active: false
