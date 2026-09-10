<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 생활 연금석

## Identity

- slug: "life-alchemy-stones"
- name_ko: "생활 연금석"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "생활 연금석의 내구도는 삭제됐으며, 현재는 생활 장비 슬롯에 장착하면 아이템 효과가 적용된다."
- purpose: "충전·수동 활성화 중심의 과거 설명을 최신 장착 효과 방식과 분리한다."

## Requirements

### `life-alchemy-stones.current-behavior`

- seed_key: "life-alchemy-stones.current-behavior"
- kind: "gear"
- requirement_level: "required"
- title: "현재 적용 방식"
- description: "2026-09-02 이후 생활 연금석은 내구도 없이 장착 시 효과가 적용된다."
- structured_value:

```json
{
  "durability_removed": true,
  "effect_mode": "on_equip",
  "manual_activation_required": false,
  "recharge_required": false,
  "slot_scope": "global_life_equipment"
}
```

### `life-alchemy-stones.representative-items`

- seed_key: "life-alchemy-stones.representative-items"
- kind: "gear"
- requirement_level: "required"
- title: "대표 대상"
- description: "생활 연금석 통합 대상의 대표 목록이다."
- structured_value:

```json
{
  "items": [
    "생명의 정령석",
    "불완전한 생명의 연금석",
    "견고한 생명의 연금석",
    "예리한 생명의 연금석",
    "영롱한 생명의 연금석",
    "화려한 생명의 연금석",
    "빛나는 생명의 연금석",
    "엔트의 눈물",
    "칸의 심장 : 생명",
    "상위 칸의 심장 : 생명"
  ]
}
```

### `life-alchemy-stones.legacy-removals`

- seed_key: "life-alchemy-stones.legacy-removals"
- kind: "other"
- requirement_level: "required"
- title: "삭제된 과거 구조"
- description: "정령석 관련 일부 제작식, 정령 친화의 시약, 반복 의뢰와 충전 관련 아이템은 삭제됐다."
- structured_value:

```json
{
  "current_acquisition_guidance": false,
  "removed_categories": [
    "일부 정령석 제작식",
    "정령 친화의 시약",
    "관련 반복 의뢰",
    "충전 관련 아이템"
  ]
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `life-alchemy-stones.guide-conflict`

- seed_key: "life-alchemy-stones.guide-conflict"
- section_type: "common_mistakes"
- title: "과거 가이드보다 최신 패치 우선"
- order_no: 1

#### body_markdown

연금석 부위에 장착 후 별도로 사용하거나 내구도를 충전하라는 구형 생활 가이드 설명은 현재 생활 연금석 baseline이 아니다.

## Related Contents

### `life-alchemy-stones.integrated-equipment`

- seed_key: "life-alchemy-stones.integrated-equipment"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "life-common-gear"
- content_name_ko: "생활 통합 장비"
- content_category: "life"
- note: "생활 연금석은 전체 생활에 적용되는 전역 슬롯이다."
- order_no: 1
- relative_path: "../contents/life-common-gear.md"
### `alchemy-stone-current-progression.integrated-life-stone`

- seed_key: "alchemy-stone-current-progression.integrated-life-stone"
- direction: "incoming"
- relation_type: "related"
- content_slug: "alchemy-stone-current-progression"
- content_name_ko: "연금석 현재 성장 체계"
- content_category: "life"
- note: "일반 파괴·수호·생명 연금석 개편과 통합 생명의 연금석은 별개다."
- order_no: 1
- relative_path: "../contents/alchemy-stone-current-progression.md"
### `life-common-gear.alchemy-stone`

- seed_key: "life-common-gear.alchemy-stone"
- direction: "incoming"
- relation_type: "related"
- content_slug: "life-common-gear"
- content_name_ko: "생활 통합 장비"
- content_category: "life"
- note: "전역 생활 연금석 슬롯"
- order_no: 3
- relative_path: "../contents/life-common-gear.md"

## Evidence and Sources

### Current evidence

### `life-alchemy-stones.summary::life-unification-2026-09-02`

- evidence_seed_key: "life-alchemy-stones.summary::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-alchemy-stones"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "내구도 삭제와 장착 효과 방식"
- active: true
- is_active: true

### `life-alchemy-stones.requirement.current-behavior::life-unification-2026-09-02`

- evidence_seed_key: "life-alchemy-stones.requirement.current-behavior::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-alchemy-stones.current-behavior"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "현재 생활 연금석 적용 방식"
- active: true
- is_active: true

### `life-alchemy-stones.requirement.legacy-removals::life-unification-2026-09-02`

- evidence_seed_key: "life-alchemy-stones.requirement.legacy-removals::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-alchemy-stones.legacy-removals"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "삭제된 정령석 관련 구조"
- active: true
- is_active: true

### `life-alchemy-stones.requirement.representative-items::life-unification-2026-09-02`

- evidence_seed_key: "life-alchemy-stones.requirement.representative-items::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-alchemy-stones.representative-items"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "생활 연금석 통합 대상 대표"
- active: true
- is_active: true

### Historical / inactive evidence

### `life-alchemy-stones.legacy.durability::life-unification-2026-09-02`

- evidence_seed_key: "life-alchemy-stones.legacy.durability::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-alchemy-stones"
- claim_key: "legacy.durability_recharge"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "생활 연금석 내구도·충전 방식 삭제"
- active: false
- is_active: false

### `life-alchemy-stones.legacy.manual-activation::life-unification-2026-09-02`

- evidence_seed_key: "life-alchemy-stones.legacy.manual-activation::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-alchemy-stones"
- claim_key: "legacy.manual_activation"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "별도 사용 활성화 방식이 장착 효과로 대체됨"
- active: false
- is_active: false
