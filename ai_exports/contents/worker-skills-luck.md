<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 일꾼 기술과 행운

## Identity

- slug: "worker-skills-luck"
- name_ko: "일꾼 기술과 행운"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "일반 생산거점에서는 일꾼 행운에 따라 생산 종류별 추가 아이템을 획득할 수 있으나 정확한 확률은 공개되지 않았다."
- purpose: "행운 추가 획득 범주와 적용 예외를 추정 확률 없이 기록한다."

## Requirements

### `worker-skills-luck.additional-items`

- seed_key: "worker-skills-luck.additional-items"
- kind: "stat"
- requirement_level: "required"
- title: "행운 추가 획득군"
- description: "생산거점 종류별 대표 추가 획득군이다."
- structured_value:

```json
{
  "applies_to_general_production_nodes": true,
  "exact_probability": null,
  "exceptions": [
    "asset_management",
    "some_special_production_nodes"
  ],
  "groups": {
    "excavation": [
      "traces"
    ],
    "fish_drying_yard": [
      "coral_piece",
      "corals"
    ],
    "gathering_and_farming": [
      "fruits"
    ],
    "logging": [
      "spirit_leaf",
      "old_tree_bark",
      "monks_branch",
      "bloody_tree_knot",
      "red_tree_lump"
    ],
    "mining": [
      "ruby_rough",
      "sapphire_rough",
      "topaz_rough",
      "emerald_rough",
      "diamond_rough",
      "opal_rough"
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

### `royal-workshop-worker-effects.general-worker-rules`

- seed_key: "royal-workshop-worker-effects.general-worker-rules"
- direction: "incoming"
- relation_type: "related"
- content_slug: "royal-workshop-worker-effects"
- content_name_ko: "왕실 공방 일꾼 효과"
- content_category: "life"
- note: "일반 일꾼 행운·기술 규칙과 연결하되 왕실 공방 적용 범위는 별도로 유지한다."
- order_no: 2
- relative_path: "../contents/royal-workshop-worker-effects.md"

## Evidence and Sources

### Current evidence

### `worker-skills-luck.claim.current::worker-overhaul-2023-05-24`

- evidence_seed_key: "worker-skills-luck.claim.current::worker-overhaul-2023-05-24"
- source_id: "worker-overhaul-2023-05-24"
- title: "5월 24일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=10369"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2023-05-24"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "worker-skills-luck"
- claim_key: "requirement:worker-skills-luck.additional-items"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
