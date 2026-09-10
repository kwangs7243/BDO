<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 채집 현재 시스템

## Identity

- slug: "gathering-current-system"
- name_ko: "채집 현재 시스템"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "대상에 맞는 채집 도구를 사용하고 기본적으로 기운을 소비하며, 채집 숙련도는 채집물 획득 확률과 수량에 관여한다."
- purpose: "V1.6F 기운·숙련도 기반을 실제 채집 행동에 연결한다."

## Requirements

### `gathering-current-system.action-map`

- seed_key: "gathering-current-system.action-map"
- kind: "gear"
- requirement_level: "required"
- title: "행동·대상·도구"
- description: "대표 채집 행동별 대상, 도구와 결과물이다."
- structured_value:

```json
{
  "actions": [
    {
      "action": "벌목",
      "representative_outputs": [
        "통나무",
        "원목"
      ],
      "targets": [
        "나무"
      ],
      "tool": "벌목 도끼"
    },
    {
      "action": "수액 채취",
      "representative_outputs": [
        "수액",
        "동물 피"
      ],
      "targets": [
        "나무",
        "동물"
      ],
      "tool": "수액 채취 도구"
    },
    {
      "action": "무두질",
      "representative_outputs": [
        "가죽",
        "깃털"
      ],
      "targets": [
        "동물"
      ],
      "tool": "무두질용 칼"
    },
    {
      "action": "도축",
      "representative_outputs": [
        "고기"
      ],
      "targets": [
        "동물"
      ],
      "tool": "도축용 칼"
    },
    {
      "action": "호미 채집",
      "representative_outputs": [
        "약초",
        "버섯",
        "씨앗",
        "균사"
      ],
      "targets": [
        "약초",
        "버섯"
      ],
      "tool": "호미"
    },
    {
      "action": "채광",
      "representative_outputs": [
        "광석"
      ],
      "targets": [
        "광석"
      ],
      "tool": "곡괭이"
    },
    {
      "action": "물뜨기",
      "representative_outputs": [
        "물로 채운 병"
      ],
      "targets": [
        "강물"
      ],
      "tool": "빈 병"
    }
  ]
}
```

### `gathering-current-system.energy`

- seed_key: "gathering-current-system.energy"
- kind: "stat"
- requirement_level: "required"
- title: "기운 소비"
- description: "채집 행동은 기본적으로 기운을 소비하며 채집 레벨은 기운 미소모 확률과 관련된다."
- structured_value:

```json
{
  "current_max_reached_at": "Professional 3",
  "exact_current_max_percent": null,
  "no_consumption_bonus_percentage_points": 10,
  "normally_consumes_energy": true
}
```

### `gathering-current-system.mastery-effects`

- seed_key: "gathering-current-system.mastery-effects"
- kind: "stat"
- requirement_level: "required"
- title: "채집 숙련도 효과"
- description: "숙련도는 기본·특수·희귀 채집물의 획득 확률 및 수량에 영향을 준다."
- structured_value:

```json
{
  "affects": [
    "basic",
    "special",
    "rare"
  ],
  "dimensions": [
    "acquisition_probability",
    "quantity"
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

### `gathering-current-system.scope`

- seed_key: "gathering-current-system.scope"
- section_type: "notes"
- title: "범위"
- order_no: 1

#### body_markdown

개별 채집 루트, 지역, 시간당 은화와 숙련도별 손익은 포함하지 않는다.

## Related Contents

### `gathering-current-system.energy-foundation`

- seed_key: "gathering-current-system.energy-foundation"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "energy-foundation"
- content_name_ko: "기운 기반"
- content_category: "life"
- note: "기운 범위와 회복 규칙 재사용"
- order_no: 1
- relative_path: "../contents/energy-foundation.md"
### `gathering-current-system.mastery-foundation`

- seed_key: "gathering-current-system.mastery-foundation"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-mastery-effects"
- content_name_ko: "생활 분야별 숙련도 효과"
- content_category: "life"
- note: "생활 숙련도 공통 효과 재사용"
- order_no: 2
- relative_path: "../contents/life-mastery-effects.md"
### `gathering-current-system.tools`

- seed_key: "gathering-current-system.tools"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "gathering-tools"
- content_name_ko: "채집 도구"
- content_category: "life"
- note: "채집 도구 예외"
- order_no: 3
- relative_path: "../contents/gathering-tools.md"
### `gathering-current-system.special-drops`

- seed_key: "gathering-current-system.special-drops"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "gathering-special-drops"
- content_name_ko: "채집 특수 획득물"
- content_category: "life"
- note: "특수 획득물"
- order_no: 4
- relative_path: "../contents/gathering-special-drops.md"
### `gathering-green-artisan-minigames.system`

- seed_key: "gathering-green-artisan-minigames.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "gathering-green-artisan-minigames"
- content_name_ko: "초록 장인 채집 미니게임"
- content_category: "life"
- note: "채집 확률 미니게임"
- order_no: 1
- relative_path: "../contents/gathering-green-artisan-minigames.md"
### `gathering-onboarding-strategy.current-system`

- seed_key: "gathering-onboarding-strategy.current-system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "gathering-onboarding-strategy"
- content_name_ko: "채집 입문 전략"
- content_category: "life"
- note: "채집 방식과 기운 등 사실 규칙은 현재 시스템에서 확인한다."
- order_no: 1
- relative_path: "../contents/gathering-onboarding-strategy.md"
### `gathering-special-drops.system`

- seed_key: "gathering-special-drops.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "gathering-special-drops"
- content_name_ko: "채집 특수 획득물"
- content_category: "life"
- note: "채집 특수 획득물"
- order_no: 1
- relative_path: "../contents/gathering-special-drops.md"
### `gathering-tools.system`

- seed_key: "gathering-tools.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "gathering-tools"
- content_name_ko: "채집 도구"
- content_category: "life"
- note: "채집 현재 시스템의 도구 예외"
- order_no: 1
- relative_path: "../contents/gathering-tools.md"
### `hunting-current-system.gathering`

- seed_key: "hunting-current-system.gathering"
- direction: "incoming"
- relation_type: "related"
- content_slug: "hunting-current-system"
- content_name_ko: "수렵 현재 시스템"
- content_category: "life"
- note: "수렵 처치 후 도축과 일반 동물 자원 채집은 구분한다."
- order_no: 1
- relative_path: "../contents/hunting-current-system.md"

## Evidence and Sources

### Current evidence

### `gathering-current-system.summary::gathering-guide`

- evidence_seed_key: "gathering-current-system.summary::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "gathering-current-system"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "채집 행동과 도구"
- active: true
- is_active: true

### `gathering-current-system.requirement.action-map::gathering-guide`

- evidence_seed_key: "gathering-current-system.requirement.action-map::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-current-system.action-map"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "대상·도구·대표 결과"
- active: true
- is_active: true

### `gathering-current-system.requirement.energy::gathering-guide`

- evidence_seed_key: "gathering-current-system.requirement.energy::gathering-guide"
- source_id: "gathering-guide"
- title: "채집"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-current-system.energy"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "기운 소비와 최신 무소모 확률 변경"
- active: true
- is_active: true

### `gathering-current-system.requirement.energy::life-unification-2026-09-02`

- evidence_seed_key: "gathering-current-system.requirement.energy::life-unification-2026-09-02"
- source_id: "life-unification-2026-09-02"
- title: "9월 2일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-09-02"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-current-system.energy"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "기운 소비와 최신 무소모 확률 변경"
- active: true
- is_active: true

### `gathering-current-system.requirement.mastery-effects::life-mastery-history`

- evidence_seed_key: "gathering-current-system.requirement.mastery-effects::life-mastery-history"
- source_id: "life-mastery-history"
- title: "생활 숙련도 / 채집물 획득 확률 및 거래소 상한가 개선"
- url: "https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=8418"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "gathering-current-system.mastery-effects"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "채집 숙련도 효과 분류"
- active: true
- is_active: true

### Historical / inactive evidence

- None
