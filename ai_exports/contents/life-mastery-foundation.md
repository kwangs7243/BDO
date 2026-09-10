<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 생활 숙련도 기반

## Identity

- slug: "life-mastery-foundation"
- name_ko: "생활 숙련도 기반"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "현재 생활 숙련도의 최대 유효 수치는 3000이며, 생활 레벨 자체로는 도인 50에서 누적 800을 얻는다."
- purpose: "생활 경험치와 생활 숙련도를 분리하고 현재 상한과 레벨 기여도를 구조화한다."

## Requirements

### `life-mastery-foundation.effective-cap`

- seed_key: "life-mastery-foundation.effective-cap"
- kind: "other"
- requirement_level: "required"
- title: "최대 유효 숙련도"
- description: "현재 최대 유효 생활 숙련도는 3000이다."
- structured_value:

```json
{
  "maximum_effective_mastery": 3000
}
```

### `life-mastery-foundation.level-breakpoints`

- seed_key: "life-mastery-foundation.level-breakpoints"
- kind: "other"
- requirement_level: "required"
- title: "생활 레벨 누적 숙련도"
- description: "생활 레벨에서 얻는 누적 숙련도는 도인 50에서 800이며, 이후 추가 증가가 없다."
- structured_value:

```json
{
  "breakpoints": [
    {
      "level": "Apprentice 1",
      "mastery": 60
    },
    {
      "level": "Skilled 1",
      "mastery": 160
    },
    {
      "level": "Professional 1",
      "mastery": 260
    },
    {
      "level": "Artisan 1",
      "mastery": 355
    },
    {
      "level": "Master 1",
      "mastery": 405
    },
    {
      "level": "Guru 1",
      "mastery": 555
    },
    {
      "level": "Guru 20",
      "mastery": 650
    },
    {
      "level": "Guru 50",
      "mastery": 800
    }
  ],
  "guru_51_to_100_additional_mastery": 0
}
```

### `life-mastery-foundation.stat-distinction`

- seed_key: "life-mastery-foundation.stat-distinction"
- kind: "other"
- requirement_level: "required"
- title: "생활 경험치와 숙련도"
- description: "생활 경험치 증가는 레벨 진행을, 생활 숙련도 증가는 분야별 결과·확률·능력치를 변화시킨다."
- structured_value:

```json
{
  "life_exp_bonus": "level_progression",
  "life_mastery": "activity_specific_effects",
  "same_stat": false
}
```

### `life-mastery-foundation.common-buff-taxonomy`

- seed_key: "life-mastery-foundation.common-buff-taxonomy"
- kind: "other"
- requirement_level: "required"
- title: "공통 생활 버프 분류"
- description: "공통 버프는 경험치, 숙련도, 행동 시간, 획득 확률, 기운과 탑승물·선원·교역 경험치 효과를 서로 다른 의미로 분류한다."
- structured_value:

```json
{
  "categories": [
    "life_exp",
    "specific_life_exp",
    "life_mastery",
    "specific_life_mastery",
    "action_speed_or_time_reduction",
    "gathering_item_acquisition_chance",
    "energy_recovery",
    "mount_exp",
    "sailor_exp",
    "barter_exp"
  ],
  "event_buffs_included": false
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `life-mastery-foundation.legacy-cap`

- seed_key: "life-mastery-foundation.legacy-cap"
- section_type: "common_mistakes"
- title: "2000 상한은 과거 기준"
- order_no: 1

#### body_markdown

생활 숙련도 2000 상한은 2025-01-08 개편 전 기준이며 현재 active 기준은 3000이다.

## Related Contents

### `life-mastery-foundation.effects`

- seed_key: "life-mastery-foundation.effects"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-mastery-effects"
- content_name_ko: "생활 분야별 숙련도 효과"
- content_category: "life"
- note: "분야별 숙련도 효과는 별도 Content에서 설명한다."
- order_no: 1
- relative_path: "../contents/life-mastery-effects.md"
### `alchemy-mastery-effects.foundation`

- seed_key: "alchemy-mastery-effects.foundation"
- direction: "incoming"
- relation_type: "related"
- content_slug: "alchemy-mastery-effects"
- content_name_ko: "연금 숙련도 효과"
- content_category: "life"
- note: "생활 숙련도 공통 기반의 연금별 효과다."
- order_no: 1
- relative_path: "../contents/alchemy-mastery-effects.md"
### `cooking-mastery-effects.foundation`

- seed_key: "cooking-mastery-effects.foundation"
- direction: "incoming"
- relation_type: "related"
- content_slug: "cooking-mastery-effects"
- content_name_ko: "요리 숙련도 효과"
- content_category: "life"
- note: "생활 숙련도 공통 기반의 요리별 효과다."
- order_no: 1
- relative_path: "../contents/cooking-mastery-effects.md"
### `fishing-current-system.mastery-foundation`

- seed_key: "fishing-current-system.mastery-foundation"
- direction: "incoming"
- relation_type: "related"
- content_slug: "fishing-current-system"
- content_name_ko: "낚시 현재 시스템"
- content_category: "life"
- note: "최대 숙련도 3000 재사용"
- order_no: 1
- relative_path: "../contents/fishing-current-system.md"
### `hunting-mastery-effects.foundation`

- seed_key: "hunting-mastery-effects.foundation"
- direction: "incoming"
- relation_type: "related"
- content_slug: "hunting-mastery-effects"
- content_name_ko: "수렵 숙련도 효과"
- content_category: "life"
- note: "생활 숙련도 공통 기반의 수렵별 효과다."
- order_no: 1
- relative_path: "../contents/hunting-mastery-effects.md"
### `life-family-levels.mastery-foundation`

- seed_key: "life-family-levels.mastery-foundation"
- direction: "incoming"
- relation_type: "related"
- content_slug: "life-family-levels"
- content_name_ko: "가문 통합 생활 레벨"
- content_category: "life"
- note: "생활 레벨에서 얻는 숙련도와 장비·버프 숙련도를 구분한다."
- order_no: 1
- relative_path: "../contents/life-family-levels.md"
### `training-mastery-effects.foundation`

- seed_key: "training-mastery-effects.foundation"
- direction: "incoming"
- relation_type: "related"
- content_slug: "training-mastery-effects"
- content_name_ko: "조련 숙련도 효과"
- content_category: "life"
- note: "생활 숙련도 공통 기반의 조련별 효과다."
- order_no: 1
- relative_path: "../contents/training-mastery-effects.md"
### `mass-processing.mastery`

- seed_key: "mass-processing.mastery"
- direction: "incoming"
- relation_type: "related"
- content_slug: "mass-processing"
- content_name_ko: "대량가공"
- content_category: "life"
- note: "최대 숙련도 3000 재사용"
- order_no: 2
- relative_path: "../contents/mass-processing.md"
### `gathering-onboarding-strategy.mastery`

- seed_key: "gathering-onboarding-strategy.mastery"
- direction: "incoming"
- relation_type: "related"
- content_slug: "gathering-onboarding-strategy"
- content_name_ko: "채집 입문 전략"
- content_category: "life"
- note: "현재 숙련도와 장비 상태를 판단할 때 참고한다."
- order_no: 3
- relative_path: "../contents/gathering-onboarding-strategy.md"
### `hunting-onboarding-strategy.mastery`

- seed_key: "hunting-onboarding-strategy.mastery"
- direction: "incoming"
- relation_type: "related"
- content_slug: "hunting-onboarding-strategy"
- content_name_ko: "수렵 입문 전략"
- content_category: "life"
- note: "숙련도 성장과 장비 판단의 공통 기반을 확인한다."
- order_no: 4
- relative_path: "../contents/hunting-onboarding-strategy.md"
### `processing-onboarding-strategy.mastery`

- seed_key: "processing-onboarding-strategy.mastery"
- direction: "incoming"
- relation_type: "related"
- content_slug: "processing-onboarding-strategy"
- content_name_ko: "가공 입문 전략"
- content_category: "life"
- note: null
- order_no: 5
- relative_path: "../contents/processing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `life-mastery-foundation.summary::life-mastery-history`

- evidence_seed_key: "life-mastery-foundation.summary::life-mastery-history"
- source_id: "life-mastery-history"
- title: "생활 숙련도 / 채집물 획득 확률 및 거래소 상한가 개선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=8418"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-mastery-foundation"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "최대 3000과 도인 50 누적 800"
- active: true
- is_active: true

### `life-mastery-foundation.summary::life-mastery-prione-2025-01-08`

- evidence_seed_key: "life-mastery-foundation.summary::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-mastery-foundation"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "최대 3000과 도인 50 누적 800"
- active: true
- is_active: true

### `life-mastery-foundation.requirement.common-buff-taxonomy::life-mastery-prione-2025-01-08`

- evidence_seed_key: "life-mastery-foundation.requirement.common-buff-taxonomy::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-mastery-foundation.common-buff-taxonomy"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "영구 생활 버프의 의미 분류와 이벤트 제외"
- active: true
- is_active: true

### `life-mastery-foundation.requirement.common-buff-taxonomy::life-unification-2026-09-02`

- evidence_seed_key: "life-mastery-foundation.requirement.common-buff-taxonomy::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-mastery-foundation.common-buff-taxonomy"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "영구 생활 버프의 의미 분류와 이벤트 제외"
- active: true
- is_active: true

### `life-mastery-foundation.requirement.effective-cap::life-mastery-prione-2025-01-08`

- evidence_seed_key: "life-mastery-foundation.requirement.effective-cap::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-mastery-foundation.effective-cap"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "2025-01-08 최대 숙련도 3000 확장"
- active: true
- is_active: true

### `life-mastery-foundation.requirement.level-breakpoints::life-family-levels-2024-04-17`

- evidence_seed_key: "life-mastery-foundation.requirement.level-breakpoints::life-family-levels-2024-04-17"
- source_id: "life-family-levels-2024-04-17"
- title: "4월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12046"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-04-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-mastery-foundation.level-breakpoints"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "생활 레벨 누적 숙련도와 도인 50 상한"
- active: true
- is_active: true

### `life-mastery-foundation.requirement.level-breakpoints::life-mastery-history`

- evidence_seed_key: "life-mastery-foundation.requirement.level-breakpoints::life-mastery-history"
- source_id: "life-mastery-history"
- title: "생활 숙련도 / 채집물 획득 확률 및 거래소 상한가 개선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=8418"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-mastery-foundation.level-breakpoints"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "생활 레벨 누적 숙련도와 도인 50 상한"
- active: true
- is_active: true

### `life-mastery-foundation.requirement.stat-distinction::life-mastery-prione-2025-01-08`

- evidence_seed_key: "life-mastery-foundation.requirement.stat-distinction::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-mastery-foundation.stat-distinction"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "생활 경험치와 숙련도 구분"
- active: true
- is_active: true

### Historical / inactive evidence

### `life-mastery-foundation.legacy.cap-2000::life-mastery-prione-2025-01-08`

- evidence_seed_key: "life-mastery-foundation.legacy.cap-2000::life-mastery-prione-2025-01-08"
- source_id: "life-mastery-prione-2025-01-08"
- title: "1월 8일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13398"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-01-08"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-mastery-foundation"
- claim_key: "legacy.maximum_effective_mastery"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "과거 최대 유효 숙련도 2000은 현재 3000으로 대체됨"
- active: false
- is_active: false
