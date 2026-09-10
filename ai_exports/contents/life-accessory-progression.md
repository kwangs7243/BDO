<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 생활 액세서리 진행 체계

## Identity

- slug: "life-accessory-progression"
- name_ko: "생활 액세서리 진행 체계"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "주요 생활 액세서리 단계는 로기아·게라노아, 플로아모스, 마노스, 프리오네로 구분한다."
- purpose: "액세서리군의 역할을 비교하되 공식적이지 않은 구매 우선순위는 제시하지 않는다."

## Requirements

### `life-accessory-progression.families`

- seed_key: "life-accessory-progression.families"
- kind: "other"
- requirement_level: "required"
- title: "주요 액세서리군"
- description: "플로아모스는 별도 고정형 액세서리이며 프리오네만 강화된 마노스를 쓰는 공식 교환 경로가 있다."
- structured_value:

```json
{
  "families": [
    "로기아",
    "게라노아",
    "플로아모스",
    "마노스",
    "프리오네"
  ],
  "floamos_directly_upgrades_to_manos": false,
  "prione_has_enhanced_manos_exchange": true
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `life-accessory-progression.no-strategy-ranking`

- seed_key: "life-accessory-progression.no-strategy-ranking"
- section_type: "notes"
- title: "사실과 추천 분리"
- order_no: 1

#### body_markdown

어떤 부위를 먼저 사야 하는지, 특정 단계의 가성비 같은 추천은 공식 시스템 사실이 아니므로 이 기반 데이터에 포함하지 않는다.

## Related Contents

### `life-accessory-progression.floamos`

- seed_key: "life-accessory-progression.floamos"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "floamos-accessories"
- content_name_ko: "플로아모스 액세서리"
- content_category: "life"
- note: "고(III) 마노스와 동일 능력치의 강화 불가 액세서리"
- order_no: 1
- relative_path: "../contents/floamos-accessories.md"
### `life-accessory-progression.prione`

- seed_key: "life-accessory-progression.prione"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "prione-accessories"
- content_name_ko: "프리오네 액세서리"
- content_category: "life"
- note: "강화된 마노스를 통해 교환하는 상위 액세서리"
- order_no: 2
- relative_path: "../contents/prione-accessories.md"
### `life-accessory-progression.integrated-equipment`

- seed_key: "life-accessory-progression.integrated-equipment"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "life-common-gear"
- content_name_ko: "생활 통합 장비"
- content_category: "life"
- note: "생활 액세서리는 전역 생활 장비 슬롯을 사용한다."
- order_no: 3
- relative_path: "../contents/life-common-gear.md"
### `floamos-accessories.accessory-progression`

- seed_key: "floamos-accessories.accessory-progression"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "floamos-accessories"
- content_name_ko: "플로아모스 액세서리"
- content_category: "life"
- note: "생활 액세서리 진행 체계의 고정형 선택지다."
- order_no: 1
- relative_path: "../contents/floamos-accessories.md"
### `life-common-gear.accessories`

- seed_key: "life-common-gear.accessories"
- direction: "incoming"
- relation_type: "related"
- content_slug: "life-common-gear"
- content_name_ko: "생활 통합 장비"
- content_category: "life"
- note: "전역 생활 액세서리 슬롯"
- order_no: 1
- relative_path: "../contents/life-common-gear.md"
### `prione-accessories.accessory-progression`

- seed_key: "prione-accessories.accessory-progression"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "prione-accessories"
- content_name_ko: "프리오네 액세서리"
- content_category: "life"
- note: "강화된 마노스를 공식 교환 경로로 사용하는 상위 생활 액세서리다."
- order_no: 1
- relative_path: "../contents/prione-accessories.md"

## Evidence and Sources

### Current evidence

### `life-accessory-progression.summary::floamos-2023-02-15`

- evidence_seed_key: "life-accessory-progression.summary::floamos-2023-02-15"
- source_id: "floamos-2023-02-15"
- title: "2월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=9834"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-02-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-accessory-progression"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "현재 주요 생활 액세서리군"
- active: true
- is_active: true

### `life-accessory-progression.summary::life-mastery-prione-2025-01-08`

- evidence_seed_key: "life-accessory-progression.summary::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-accessory-progression"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "현재 주요 생활 액세서리군"
- active: true
- is_active: true

### `life-accessory-progression.summary::life-unification-2026-09-02`

- evidence_seed_key: "life-accessory-progression.summary::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-accessory-progression"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "현재 주요 생활 액세서리군"
- active: true
- is_active: true

### `life-accessory-progression.requirement.families::floamos-2023-02-15`

- evidence_seed_key: "life-accessory-progression.requirement.families::floamos-2023-02-15"
- source_id: "floamos-2023-02-15"
- title: "2월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=9834"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-02-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-accessory-progression.families"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "플로아모스와 프리오네의 진행 방식 구분"
- active: true
- is_active: true

### `life-accessory-progression.requirement.families::life-mastery-prione-2025-01-08`

- evidence_seed_key: "life-accessory-progression.requirement.families::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-accessory-progression.families"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "플로아모스와 프리오네의 진행 방식 구분"
- active: true
- is_active: true

### Historical / inactive evidence

- None
