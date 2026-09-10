<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 조르다인 사가

## Identity

- slug: "main-quest-jordaine-saga"
- name_ko: "조르다인 사가"
- category: "progression"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "발레노스 이후 세렌디아와 칼페온의 이야기를 하나로 잇는 메인 의뢰 사가다."
- purpose: "개편 전 지역별 명칭과 혼동하지 않고 현재 사가 완료 지점을 기록한다."

## Requirements

### `main-quest-jordaine-saga.current-structure`

- seed_key: "main-quest-jordaine-saga.current-structure"
- kind: "quest"
- requirement_level: "required"
- title: "세렌디아·칼페온 통합 사가"
- description: "2024년 2월 7일 개편으로 세렌디아와 칼페온 메인 의뢰가 조르다인 사가로 통합되었다."
- structured_value:

```json
{
  "effective_date": "2024-02-07",
  "knowledge_role": "fact",
  "prerequisite_checkpoint": "Balenos",
  "regions": [
    "Serendia",
    "Calpheon"
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

- None

## Related Contents

### `main-quest-jordaine-saga.foundation`

- seed_key: "main-quest-jordaine-saga.foundation"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "main-quest-progression-foundation"
- content_name_ko: "메인 의뢰 성장 기반"
- content_category: "progression"
- note: null
- order_no: 1
- relative_path: "../contents/main-quest-progression-foundation.md"
### `main-quest-jordaine-saga.balenos`

- seed_key: "main-quest-jordaine-saga.balenos"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "main-quest-balenos"
- content_name_ko: "발레노스 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/main-quest-balenos.md"
### `main-quest-mediah.jordaine`

- seed_key: "main-quest-mediah.jordaine"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "main-quest-mediah"
- content_name_ko: "메디아 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/main-quest-mediah.md"

## Evidence and Sources

### Current evidence

### `main-quest-jordaine-saga.claim.current-structure::jordaine-saga-update-2024-02-07`

- evidence_seed_key: "main-quest-jordaine-saga.claim.current-structure::jordaine-saga-update-2024-02-07"
- source_id: "jordaine-saga-update-2024-02-07"
- title: "2024-02-07 Update - Jordine Saga"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=11714"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-02-07"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "main-quest-jordaine-saga.current-structure"
- claim_key: "requirement:current-structure"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
