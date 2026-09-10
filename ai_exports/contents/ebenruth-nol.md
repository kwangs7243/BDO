<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 에벤루스의 놀

## Identity

- slug: "ebenruth-nol"
- name_ko: "에벤루스의 놀"
- category: "ocean_guide"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "중범선에 장착해 지구력 소모 없이 쾌속순항을 한 번 더 사용하고 추가 사용 거리를 50% 늘리는 대양 보물이다."
- purpose: "문양이 새겨진 놀과 에벤루스 제작 경로, 현행 내구도 규칙을 확인한다."

## Requirements

### `ebenruth-nol.effect`

- seed_key: "ebenruth-nol.effect"
- kind: "other"
- requirement_level: "required"
- title: "보물 효과"
- description: "에페리아 중범선에 장착하면 쾌속순항을 지구력 소모 없이 한 번 더 사용하며 추가 쾌속순항 거리는 일반보다 50% 길다."
- structured_value:

```json
{
  "extra_breezy_sail": 1,
  "extra_distance_percent": 50,
  "ship": "에페리아 중범선",
  "stamina_cost": 0
}
```

### `ebenruth-nol.final-recipe`

- seed_key: "ebenruth-nol.final-recipe"
- kind: "other"
- requirement_level: "required"
- title: "최종 조합"
- description: "문양이 새겨진 놀과 에벤루스를 조합해 에벤루스의 놀을 만든다."
- structured_value:

```json
{
  "문양이 새겨진 놀": 1,
  "에벤루스": 1
}
```

### `ebenruth-nol.patterned-path`

- seed_key: "ebenruth-nol.patterned-path"
- kind: "other"
- requirement_level: "required"
- title: "문양이 새겨진 놀 경로"
- description: "바다 악어의 이끼에 뒤덮인 지도를 리비니아의 이끼 제거 용액과 간이연금해 9종 찢어진 보물지도 조각을 모은다. 어느 선원의 보물지도를 완성해 의뢰로 보물상자를 받고, 상자에서 확률로 문양이 새겨진 놀을 얻는다. 간이연금 시 낮은 확률로 완성 지도를 바로 얻을 수도 있다."
- structured_value:

```json
{
  "assembled_map": "어느 선원의 보물지도",
  "direct_complete_map_chance": "낮은 확률",
  "drop": "이끼에 뒤덮인 지도",
  "monster": "바다 악어",
  "piece_types": 9,
  "process": "간이연금",
  "quest_reward": "어느 선원의 보물상자",
  "random_reward": "문양이 새겨진 놀",
  "reagent": "리비니아의 이끼 제거 용액"
}
```

### `ebenruth-nol.ebenruth-material`

- seed_key: "ebenruth-nol.ebenruth-material"
- kind: "other"
- requirement_level: "required"
- title: "에벤루스 재료"
- description: "오킬루아의 꽃 1,000개와 오킬루아의 눈물 1개를 간이연금해 에벤루스를 만든다. 꽃은 물물교환·까마귀 둥지 상점·어느 선원의 보물상자, 눈물은 까마귀 둥지 상점에서 얻는다."
- structured_value:

```json
{
  "flower_sources": [
    "물물교환",
    "까마귀 둥지 상점",
    "어느 선원의 보물상자"
  ],
  "process": "간이연금",
  "recipe": {
    "오킬루아의 꽃": 1000,
    "오킬루아의 눈물": 1
  },
  "tear_source": "까마귀 둥지 상점"
}
```

### `ebenruth-nol.sea-tear`

- seed_key: "ebenruth-nol.sea-tear"
- kind: "other"
- requirement_level: "required"
- title: "바다의 눈물이 담긴 에벤루스의 놀"
- description: "에벤루스의 놀 1개와 루살카 해원석 1개를 공작하면 양쪽 효과를 함께 받는다. 다시 공작하면 두 재료로 분해된다."
- structured_value:

```json
{
  "effects": [
    "에벤루스의 놀",
    "루살카 해원석"
  ],
  "process": "공작",
  "recipe": {
    "루살카 해원석": 1,
    "에벤루스의 놀": 1
  },
  "same_process_disassembles": true
}
```

### `ebenruth-nol.durability-current`

- seed_key: "ebenruth-nol.durability-current"
- kind: "other"
- requirement_level: "required"
- title: "현재 내구도 규칙"
- description: "2025-02-12부터 에벤루스의 놀 내구도가 제거되어 운항 중 내구도 감소와 수리 비용이 발생하지 않는다."
- structured_value:

```json
{
  "durability_removed": true,
  "effective_from": "2025-02-12",
  "repair_cost": 0
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

### `ebenruth-nol.relation.sea-crocodile`

- seed_key: "ebenruth-nol.relation.sea-crocodile"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "sea-crocodile-hunting"
- content_name_ko: "바다 악어 사냥"
- content_category: "ocean_guide"
- note: "문양이 새겨진 놀 재료 획득처"
- order_no: 1
- relative_path: "../contents/sea-crocodile-hunting.md"
### `ebenruth-nol.relation.sea-crystals`

- seed_key: "ebenruth-nol.relation.sea-crystals"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "sea-crystals"
- content_name_ko: "해원석 progression"
- content_category: "ocean_project"
- note: "루살카 해원석과 결합하며 해원석 데이터는 기존 콘텐츠를 참조"
- order_no: 2
- relative_path: "../contents/sea-crystals.md"
### `ebenruth-nol.relation.carracks`

- seed_key: "ebenruth-nol.relation.carracks"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "carrack-types"
- content_name_ko: "에페리아 중범선 네 종류"
- content_category: "ocean_project"
- note: "에페리아 중범선 장착 보물"
- order_no: 3
- relative_path: "../contents/carrack-types.md"
### `sea-crocodile-hunting.relation.ebenruth`

- seed_key: "sea-crocodile-hunting.relation.ebenruth"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "sea-crocodile-hunting"
- content_name_ko: "바다 악어 사냥"
- content_category: "ocean_guide"
- note: "문양이 새겨진 놀 재료 경로"
- order_no: 1
- relative_path: "../contents/sea-crocodile-hunting.md"
### `sea-crystals.relation.ebenruth`

- seed_key: "sea-crystals.relation.ebenruth"
- direction: "incoming"
- relation_type: "related"
- content_slug: "sea-crystals"
- content_name_ko: "해원석 progression"
- content_category: "ocean_project"
- note: "루살카 해원석과 에벤루스의 놀 결합"
- order_no: 3
- relative_path: "../contents/sea-crystals.md"

## Evidence and Sources

### Current evidence

### `ebenruth-nol.evidence.durability::ebenruth-update-2025-02-12`

- evidence_seed_key: "ebenruth-nol.evidence.durability::ebenruth-update-2025-02-12"
- source_id: "ebenruth-update-2025-02-12"
- title: "2월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13537"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ebenruth-nol.durability-current"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "내구도 제거와 수리 비용 없음"
- active: true
- is_active: true

### `ebenruth-nol.evidence.material::treasure-items-guide`

- evidence_seed_key: "ebenruth-nol.evidence.material::treasure-items-guide"
- source_id: "treasure-items-guide"
- title: "보물 아이템 만들기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=194"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ebenruth-nol.ebenruth-material"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "꽃 1,000개와 눈물 1개 간이연금"
- active: true
- is_active: true

### `ebenruth-nol.evidence.effect::treasure-items-guide`

- evidence_seed_key: "ebenruth-nol.evidence.effect::treasure-items-guide"
- source_id: "treasure-items-guide"
- title: "보물 아이템 만들기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=194"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ebenruth-nol.effect"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "추가 쾌속순항과 거리 50%"
- active: true
- is_active: true

### `ebenruth-nol.evidence.final-recipe::treasure-items-guide`

- evidence_seed_key: "ebenruth-nol.evidence.final-recipe::treasure-items-guide"
- source_id: "treasure-items-guide"
- title: "보물 아이템 만들기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=194"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ebenruth-nol.final-recipe"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "최종 조합 재료"
- active: true
- is_active: true

### `ebenruth-nol.evidence.patterned-path::treasure-items-guide`

- evidence_seed_key: "ebenruth-nol.evidence.patterned-path::treasure-items-guide"
- source_id: "treasure-items-guide"
- title: "보물 아이템 만들기"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=194"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ebenruth-nol.patterned-path"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "문양이 새겨진 놀 9조각 제작 경로"
- active: true
- is_active: true

### `ebenruth-nol.evidence.sea-tear::ebenruth-update-2025-02-12`

- evidence_seed_key: "ebenruth-nol.evidence.sea-tear::ebenruth-update-2025-02-12"
- source_id: "ebenruth-update-2025-02-12"
- title: "2월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13537"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ebenruth-nol.sea-tear"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "루살카 해원석 결합·효과·분해"
- active: true
- is_active: true

### `ebenruth-nol.evidence.sea-tear::sea-crystal-guide`

- evidence_seed_key: "ebenruth-nol.evidence.sea-tear::sea-crystal-guide"
- source_id: "sea-crystal-guide"
- title: "해원석"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=376"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "ebenruth-nol.sea-tear"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "루살카 해원석 결합·효과·분해"
- active: true
- is_active: true

### Historical / inactive evidence

- None
