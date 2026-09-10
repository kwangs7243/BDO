<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 황실 연금 현재 상자표

## Identity

- slug: "alchemy-imperial-current"
- name_ko: "황실 연금 현재 상자표"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "현재 황실 연금 포장에 필요한 비약 수량을 숙련 단계와 품목별로 기록한다."
- purpose: "2025년 5월 조정 이후의 전체 황실 연금 포장 수량을 제공한다."

## Requirements

### `alchemy-imperial-current.table`

- seed_key: "alchemy-imperial-current.table"
- kind: "other"
- requirement_level: "required"
- title: "현재 황실 연금 상자표"
- description: "현재 황실 연금 상자표의 현재 규칙이다."
- structured_value:

```json
{
  "tiers": {
    "apprentice": [
      [
        "resurrection_elixir",
        18
      ],
      [
        "strong_resurrection_elixir",
        6
      ],
      [
        "hp_elixir",
        9
      ],
      [
        "strong_hp_elixir",
        3
      ],
      [
        "seal_elixir",
        9
      ],
      [
        "agile_seal_elixir",
        3
      ],
      [
        "vitality_elixir",
        9
      ],
      [
        "overflowing_vitality_elixir",
        3
      ],
      [
        "mental_elixir",
        12
      ],
      [
        "clear_mental_elixir",
        4
      ],
      [
        "will_elixir",
        9
      ],
      [
        "firm_will_elixir",
        3
      ]
    ],
    "artisan": [
      [
        "swiftness_elixir",
        12
      ],
      [
        "exhilarating_swiftness_elixir",
        4
      ],
      [
        "concentration_elixir",
        24
      ],
      [
        "advanced_concentration_elixir",
        8
      ],
      [
        "looney_spirit_elixir",
        9
      ],
      [
        "strong_looney_spirit_elixir",
        3
      ],
      [
        "spell_elixir",
        12
      ],
      [
        "nimble_spell_elixir",
        4
      ],
      [
        "affinity_elixir",
        12
      ],
      [
        "enhanced_affinity_elixir",
        4
      ],
      [
        "energy_elixir",
        21
      ],
      [
        "overflowing_energy_elixir",
        7
      ],
      [
        "plunder_elixir",
        15
      ],
      [
        "powerful_plunder_elixir",
        5
      ],
      [
        "labor_elixir",
        15
      ],
      [
        "rough_labor_elixir",
        5
      ]
    ],
    "guru": [
      [
        "death_elixir",
        6
      ],
      [
        "harsh_death_elixir",
        2
      ],
      [
        "reaper_elixir",
        6
      ],
      [
        "soul_reaping_elixir",
        2
      ],
      [
        "griffon_elixir",
        6
      ],
      [
        "powerful_griffon_elixir",
        2
      ],
      [
        "frenzy_elixir",
        6
      ],
      [
        "endless_frenzy_elixir",
        2
      ],
      [
        "sky_elixir",
        6
      ],
      [
        "merciless_sky_elixir",
        2
      ],
      [
        "detection_elixir",
        6
      ],
      [
        "sharp_detection_elixir",
        2
      ],
      [
        "metal_armor_elixir",
        6
      ],
      [
        "fallen_metal_armor_elixir",
        2
      ]
    ],
    "master": [
      [
        "wing_elixir",
        24
      ],
      [
        "soaring_wing_elixir",
        8
      ],
      [
        "assassin_elixir",
        12
      ],
      [
        "lethal_assassin_elixir",
        4
      ],
      [
        "golden_hand_elixir",
        9
      ],
      [
        "splendid_golden_hand_elixir",
        3
      ],
      [
        "spiral_elixir",
        9
      ],
      [
        "shining_spiral_elixir",
        3
      ],
      [
        "marking_reagent",
        9
      ],
      [
        "penetration_elixir",
        6
      ],
      [
        "harsh_penetration_elixir",
        2
      ],
      [
        "massacre_elixir",
        6
      ],
      [
        "cruel_massacre_elixir",
        2
      ],
      [
        "skill_elixir",
        6
      ],
      [
        "infinite_skill_elixir",
        2
      ],
      [
        "mastery_elixir",
        6
      ],
      [
        "enhanced_mastery_elixir",
        2
      ],
      [
        "destruction_elixir",
        6
      ],
      [
        "lethal_destruction_elixir",
        2
      ],
      [
        "persistence_elixir",
        6
      ],
      [
        "endless_persistence_elixir",
        2
      ],
      [
        "strength_elixir",
        6
      ],
      [
        "solid_strength_elixir",
        2
      ]
    ],
    "professional": [
      [
        "anger_elixir",
        12
      ],
      [
        "endless_anger_elixir",
        4
      ],
      [
        "fisher_elixir",
        12
      ],
      [
        "skilled_fisher_elixir",
        4
      ],
      [
        "defense_elixir",
        12
      ],
      [
        "steel_defense_elixir",
        4
      ],
      [
        "wind_elixir",
        12
      ],
      [
        "flowing_wind_elixir",
        4
      ],
      [
        "training_elixir",
        12
      ],
      [
        "experienced_training_elixir",
        4
      ],
      [
        "time_elixir",
        12
      ],
      [
        "flowing_time_elixir",
        4
      ],
      [
        "winnie_spirit_elixir",
        12
      ],
      [
        "springing_winnie_spirit_elixir",
        4
      ]
    ],
    "skilled": [
      [
        "experience_elixir",
        18
      ],
      [
        "shining_experience_elixir",
        6
      ],
      [
        "shock_elixir",
        15
      ],
      [
        "strong_shock_elixir",
        5
      ],
      [
        "demi_human_hunt_elixir",
        15
      ],
      [
        "fierce_demi_human_hunt_elixir",
        5
      ],
      [
        "worker_elixir",
        21
      ],
      [
        "skilled_worker_elixir",
        7
      ],
      [
        "human_hunt_elixir",
        15
      ],
      [
        "perfect_human_hunt_elixir",
        5
      ],
      [
        "resistance_elixir",
        9
      ],
      [
        "tenacious_resistance_elixir",
        3
      ]
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

### `alchemy-imperial-current.delivery`

- seed_key: "alchemy-imperial-current.delivery"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "imperial-crafting-delivery-daily"
- content_name_ko: "황실 제작 납품 일일"
- content_category: "life"
- note: "공통 황실 제작 납품 규칙의 연금 품목표다."
- order_no: 1
- relative_path: "../contents/imperial-crafting-delivery-daily.md"
### `alchemy-onboarding-strategy.imperial`

- seed_key: "alchemy-onboarding-strategy.imperial"
- direction: "incoming"
- relation_type: "related"
- content_slug: "alchemy-onboarding-strategy"
- content_name_ko: "연금 입문 전략"
- content_category: "life"
- note: null
- order_no: 4
- relative_path: "../contents/alchemy-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `alchemy-imperial-current.claim.table::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "alchemy-imperial-current.claim.table::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "alchemy-imperial-current"
- claim_key: "requirement:alchemy-imperial-current.table"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
