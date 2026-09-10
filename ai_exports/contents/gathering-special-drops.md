<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 채집 특수 획득물

## Identity

- slug: "gathering-special-drops"
- name_ko: "채집 특수 획득물"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "요정의 숨결은 지정 채집 행동에서 얻어 교환하며, 파묻힌 흔적은 낮은 확률로 발견해 금 열쇠로 의문의 결정 상자를 연다."
- purpose: "요정의 숨결과 파묻힌 흔적의 획득 행동·교환·보상을 추측 없이 기록한다."

## Requirements

### `gathering-special-drops.fairy-breath-actions`

- seed_key: "gathering-special-drops.fairy-breath-actions"
- kind: "item"
- requirement_level: "required"
- title: "요정의 숨결 획득"
- description: "현재 가이드에서 확인되는 획득 행동만 포함한다."
- structured_value:

```json
{
  "actions": [
    "벌목",
    "무두질",
    "수액 채취",
    "호미",
    "채광",
    "물뜨기"
  ],
  "butchering_confirmed_by_current_guide": false
}
```

### `gathering-special-drops.fairy-breath-exchange`

- seed_key: "gathering-special-drops.fairy-breath-exchange"
- kind: "item"
- requirement_level: "required"
- title: "요정의 숨결 교환"
- description: "요정의 숨결 10개 단위의 대표 교환 목록이다."
- structured_value:

```json
{
  "input": {
    "amount": 10,
    "item": "요정의 숨결"
  },
  "options": [
    {
      "amount": 30,
      "item": "야생 들풀"
    },
    {
      "amount": 20,
      "item": "통나무"
    },
    {
      "amount": 12,
      "item": "거친 석재"
    },
    {
      "amount": 1,
      "item": "자연의 열매"
    },
    {
      "amount": 1,
      "item": "자연의 흔적"
    },
    {
      "amount": null,
      "item": "공헌도 경험치 및 채집 경험치"
    }
  ]
}
```

### `gathering-special-drops.buried-trace-discovery`

- seed_key: "gathering-special-drops.buried-trace-discovery"
- kind: "other"
- requirement_level: "required"
- title: "파묻힌 흔적 발견"
- description: "지정 채집 행동에서 낮은 확률로 발견하며 상호작용하면 의문의 결정 상자가 나타난다."
- structured_value:

```json
{
  "actions": [
    "벌목",
    "무두질",
    "수액 채취",
    "호미",
    "채광",
    "도축"
  ],
  "interaction_result": "의문의 결정 상자",
  "probability": "low_unspecified"
}
```

### `gathering-special-drops.buried-trace-key`

- seed_key: "gathering-special-drops.buried-trace-key"
- kind: "item"
- requirement_level: "required"
- title: "금 열쇠"
- description: "의문의 결정 상자를 열려면 금 열쇠가 필요하다."
- structured_value:

```json
{
  "representative_acquisition": [
    {
      "input": {
        "amount": 100,
        "item": "은 열쇠"
      },
      "method": "exchange"
    },
    {
      "method": "central_market"
    }
  ],
  "required_item": "금 열쇠"
}
```

### `gathering-special-drops.buried-trace-rewards`

- seed_key: "gathering-special-drops.buried-trace-rewards"
- kind: "item"
- requirement_level: "required"
- title: "의문의 결정 상자"
- description: "공식 가이드가 안내하는 주요 보상과 확률이다."
- structured_value:

```json
{
  "rewards": [
    {
      "item": "뾰족한 흑결정 조각",
      "max": 22,
      "min": 15,
      "probability_percent": 100
    },
    {
      "item": "고대 정령의 가루",
      "max": 20,
      "min": 5,
      "probability_percent": 50
    },
    {
      "item": "자연의 열매",
      "max": 26,
      "min": 22,
      "probability_percent": 100
    }
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

### `gathering-special-drops.system`

- seed_key: "gathering-special-drops.system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "gathering-current-system"
- content_name_ko: "채집 현재 시스템"
- content_category: "life"
- note: "채집 특수 획득물"
- order_no: 1
- relative_path: "../contents/gathering-current-system.md"
### `gathering-current-system.special-drops`

- seed_key: "gathering-current-system.special-drops"
- direction: "incoming"
- relation_type: "related"
- content_slug: "gathering-current-system"
- content_name_ko: "채집 현재 시스템"
- content_category: "life"
- note: "특수 획득물"
- order_no: 4
- relative_path: "../contents/gathering-current-system.md"

## Evidence and Sources

### Current evidence

### `gathering-special-drops.summary::gathering-guide`

- evidence_seed_key: "gathering-special-drops.summary::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "gathering-special-drops"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "특수 획득물 구조"
- active: true
- is_active: true

### `gathering-special-drops.requirement.buried-trace-discovery::gathering-guide`

- evidence_seed_key: "gathering-special-drops.requirement.buried-trace-discovery::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-special-drops.buried-trace-discovery"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "발견 행동과 상자"
- active: true
- is_active: true

### `gathering-special-drops.requirement.buried-trace-key::gathering-guide`

- evidence_seed_key: "gathering-special-drops.requirement.buried-trace-key::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-special-drops.buried-trace-key"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "금 열쇠 획득 경로"
- active: true
- is_active: true

### `gathering-special-drops.requirement.buried-trace-rewards::gathering-guide`

- evidence_seed_key: "gathering-special-drops.requirement.buried-trace-rewards::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-special-drops.buried-trace-rewards"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주요 보상 수량과 확률"
- active: true
- is_active: true

### `gathering-special-drops.requirement.fairy-breath-actions::gathering-guide`

- evidence_seed_key: "gathering-special-drops.requirement.fairy-breath-actions::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-special-drops.fairy-breath-actions"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "현재 가이드의 획득 행동"
- active: true
- is_active: true

### `gathering-special-drops.requirement.fairy-breath-exchange::gathering-guide`

- evidence_seed_key: "gathering-special-drops.requirement.fairy-breath-exchange::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-special-drops.fairy-breath-exchange"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "10개 단위 교환"
- active: true
- is_active: true

### Historical / inactive evidence

- None
