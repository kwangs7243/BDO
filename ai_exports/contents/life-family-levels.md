<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 가문 통합 생활 레벨

## Identity

- slug: "life-family-levels"
- name_ko: "가문 통합 생활 레벨"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "11개 생활 분야의 경험치는 가문 내 모든 캐릭터가 획득한 값을 합산하며, 최대 레벨은 도인 100이다."
- purpose: "생활 레벨의 가문 공유 범위와 도인 50 이후의 효과 상한을 구분한다."

## Requirements

### `life-family-levels.family-scope`

- seed_key: "life-family-levels.family-scope"
- kind: "other"
- requirement_level: "required"
- title: "가문 통합 대상"
- description: "내 정보에서 확인하는 11개 생활 분야가 가문 단위로 통합된다."
- structured_value:

```json
{
  "scope": "family",
  "skill_count": 11,
  "skills": [
    "채집",
    "낚시",
    "수렵",
    "요리",
    "연금",
    "가공",
    "조련",
    "무역",
    "재배",
    "항해",
    "교역"
  ]
}
```

### `life-family-levels.exp-aggregation`

- seed_key: "life-family-levels.exp-aggregation"
- kind: "other"
- requirement_level: "required"
- title: "경험치 합산 방식"
- description: "가문 내 모든 캐릭터가 각 분야에서 획득한 경험치를 합산한다. 가장 높은 캐릭터만 선택하는 방식이 아니다."
- structured_value:

```json
{
  "aggregation": "sum_all_characters",
  "disallowed_interpretation": "highest_character_only"
}
```

### `life-family-levels.progression-cap`

- seed_key: "life-family-levels.progression-cap"
- kind: "other"
- requirement_level: "required"
- title: "레벨과 효과 상한"
- description: "레벨은 도인 100까지 성장하지만 레벨 기반 숙련도와 분야별 기능 효과는 도인 50까지만 증가한다."
- structured_value:

```json
{
  "guru_51_to_100_additional_effect": false,
  "level_effect_cap": "Guru 50",
  "mastery_growth_cap_by_level": "Guru 50",
  "max_progression_level": "Guru 100"
}
```

### `life-family-levels.shared-skills`

- seed_key: "life-family-levels.shared-skills"
- kind: "other"
- requirement_level: "required"
- title: "가문 공유 생활 기술"
- description: "생활 레벨 통합과 함께 전력질주, 숲의 질주, 쾌속순항 등이 가문 단위로 공유된다."
- structured_value:

```json
{
  "examples": [
    "전력질주",
    "숲의 질주",
    "쾌속순항"
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

### `life-family-levels.scope-note`

- seed_key: "life-family-levels.scope-note"
- section_type: "common_mistakes"
- title: "가장 높은 캐릭터 공유가 아님"
- order_no: 1

#### body_markdown

현재 생활 레벨은 캐릭터별 최고 레벨을 고르는 방식이 아니라 각 캐릭터가 획득한 분야별 생활 경험치를 합산한 결과다.

## Related Contents

### `life-family-levels.mastery-foundation`

- seed_key: "life-family-levels.mastery-foundation"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-mastery-foundation"
- content_name_ko: "생활 숙련도 기반"
- content_category: "life"
- note: "생활 레벨에서 얻는 숙련도와 장비·버프 숙련도를 구분한다."
- order_no: 1
- relative_path: "../contents/life-mastery-foundation.md"
### `life-family-levels.training-routine`

- seed_key: "life-family-levels.training-routine"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "dream-horse-material-routines"
- content_name_ko: "꿈결 환상마 재료 루틴"
- content_category: "life"
- note: "가문 통합 조련 레벨은 기존 조련 반복 콘텐츠의 공통 기반이다."
- order_no: 2
- relative_path: "../contents/dream-horse-material-routines.md"
### `life-family-levels.ocean-sailing`

- seed_key: "life-family-levels.ocean-sailing"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "barter-current-system"
- content_name_ko: "현행 물물교환 시스템"
- content_category: "ocean_barter"
- note: "가문 통합 항해·교역 레벨은 기존 대양 콘텐츠의 공통 기반이다."
- order_no: 3
- relative_path: "../contents/barter-current-system.md"
### `pet-current-system.life-family-levels`

- seed_key: "pet-current-system.life-family-levels"
- direction: "incoming"
- relation_type: "related"
- content_slug: "pet-current-system"
- content_name_ko: "반려동물 현재 시스템"
- content_category: "progression"
- note: "생활 활동 목적별 특기와 기술 구성"
- order_no: 3
- relative_path: "../contents/pet-current-system.md"
### `account-progression-foundation.life`

- seed_key: "account-progression-foundation.life"
- direction: "incoming"
- relation_type: "related"
- content_slug: "account-progression-foundation"
- content_name_ko: "가문 성장 기반"
- content_category: "progression"
- note: null
- order_no: 5
- relative_path: "../contents/account-progression-foundation.md"

## Evidence and Sources

### Current evidence

### `life-family-levels.summary::life-family-levels-2024-04-17`

- evidence_seed_key: "life-family-levels.summary::life-family-levels-2024-04-17"
- source_id: "life-family-levels-2024-04-17"
- title: "4월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12046"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-04-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "life-family-levels"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "11개 분야 가문 통합, 경험치 합산, 도인 100"
- active: true
- is_active: true

### `life-family-levels.requirement.exp-aggregation::life-family-levels-2024-04-17`

- evidence_seed_key: "life-family-levels.requirement.exp-aggregation::life-family-levels-2024-04-17"
- source_id: "life-family-levels-2024-04-17"
- title: "4월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12046"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-04-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-family-levels.exp-aggregation"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "모든 캐릭터 경험치 합산"
- active: true
- is_active: true

### `life-family-levels.requirement.family-scope::life-family-levels-2024-04-17`

- evidence_seed_key: "life-family-levels.requirement.family-scope::life-family-levels-2024-04-17"
- source_id: "life-family-levels-2024-04-17"
- title: "4월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12046"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-04-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-family-levels.family-scope"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "가문 통합 대상 11개 분야"
- active: true
- is_active: true

### `life-family-levels.requirement.progression-cap::life-family-levels-2024-04-17`

- evidence_seed_key: "life-family-levels.requirement.progression-cap::life-family-levels-2024-04-17"
- source_id: "life-family-levels-2024-04-17"
- title: "4월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12046"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-04-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-family-levels.progression-cap"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "도인 100 진행, 도인 50 효과 상한"
- active: true
- is_active: true

### `life-family-levels.requirement.shared-skills::life-family-levels-2024-04-17`

- evidence_seed_key: "life-family-levels.requirement.shared-skills::life-family-levels-2024-04-17"
- source_id: "life-family-levels-2024-04-17"
- title: "4월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12046"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-04-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "life-family-levels.shared-skills"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "가문 공유 기술 예시"
- active: true
- is_active: true

### Historical / inactive evidence

- None
