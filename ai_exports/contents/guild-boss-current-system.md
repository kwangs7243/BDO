<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 길드 우두머리 현행 시스템

## Identity

- slug: "guild-boss-current-system"
- name_ko: "길드 우두머리 현행 시스템"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- party_type: null
- difficulty: null

## Overview

- summary: "현행 명단, 권한, 전용 지역, 주간 기본 횟수와 명성 재충전을 구분한 기준이다."
- purpose: "공통 규칙을 개별 전투 정보와 분리해 확인한다."

## Requirements

### `guild-boss-current-system.roster`

- seed_key: "guild-boss-current-system.roster"
- kind: "other"
- requirement_level: "required"
- title: "현행 명단"
- description: "표준 명단은 칸·오르그·모굴리스·페리드·거대한 진흙 괴물이고 구미호·두억시니는 별도 명성 2인조다. 고대의 푸투룸은 2026-01-07 제거됐다."
- structured_value:

```json
{
  "ancient_puturum_current": false,
  "fame_duo": "guild-boss-gumiho-duoksini",
  "knowledge_role": "fact",
  "standard_fragment_bosses": [
    "khan-guild-boss",
    "guild-boss-orgg",
    "guild-boss-mogulis",
    "guild-boss-ferrid",
    "guild-boss-giant-mudster"
  ]
}
```

### `guild-boss-current-system.fragment-flow`

- seed_key: "guild-boss-current-system.fragment-flow"
- kind: "other"
- requirement_level: "required"
- title: "조각 흐름"
- description: "길드 의뢰로 조각을 확보하고 길드 정보 UI에서 지역과 난이도를 선택한다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "source": "guild_quests",
  "storage": "guild_boss_summon_ui"
}
```

### `guild-boss-current-system.authority`

- seed_key: "guild-boss-current-system.authority"
- kind: "other"
- requirement_level: "required"
- title: "권한"
- description: "길드 대장 또는 권한자가 지역을 만들고 같은 길드원만 입장한다."
- structured_value:

```json
{
  "guild_master_or_authorized": true,
  "knowledge_role": "fact",
  "same_guild_only": true
}
```

### `guild-boss-current-system.region`

- seed_key: "guild-boss-current-system.region"
- kind: "other"
- requirement_level: "required"
- title: "전용 지역"
- description: "전용 지역은 1시간이며 거점·점령전 진행 서버와 아르샤에서는 만들 수 없다."
- structured_value:

```json
{
  "duration_minutes": 60,
  "knowledge_role": "fact",
  "unavailable": [
    "node_or_conquest",
    "arsha"
  ]
}
```

### `guild-boss-current-system.restrictions`

- seed_key: "guild-boss-current-system.restrictions"
- kind: "other"
- requirement_level: "required"
- title: "입장 제한"
- description: "견습·전장의 영웅, 강제 공격·결투·탑승·비대기·엘비아 상태는 공식 제한을 따른다."
- structured_value:

```json
{
  "blocked": [
    "forced_attack",
    "duel",
    "mounted",
    "not_idle",
    "elvia"
  ],
  "excluded_roles": [
    "apprentice",
    "war_hero"
  ],
  "knowledge_role": "fact"
}
```

### `guild-boss-current-system.base-count`

- seed_key: "guild-boss-current-system.base-count"
- kind: "other"
- requirement_level: "required"
- title: "기본 횟수"
- description: "각 표준 우두머리는 기본 주 1회이며 횟수와 조각은 월요일 00:00 KST 초기화다."
- structured_value:

```json
{
  "base_per_boss": 1,
  "fragments_reset": true,
  "knowledge_role": "fact",
  "time": "00:00",
  "timezone": "Asia/Seoul",
  "weekday": 0
}
```

### `guild-boss-current-system.recharge`

- seed_key: "guild-boss-current-system.recharge"
- kind: "other"
- requirement_level: "required"
- title: "명성 재충전"
- description: "명성 25,000으로 표준 우두머리 한 종류를 주 1회 추가한다. 조각 조건도 충족되며 기본 횟수와 별도다."
- structured_value:

```json
{
  "eligible": [
    "khan-guild-boss",
    "guild-boss-orgg",
    "guild-boss-mogulis",
    "guild-boss-ferrid",
    "guild-boss-giant-mudster"
  ],
  "fame_cost": 25000,
  "knowledge_role": "fact",
  "per_boss_weekly": 1,
  "satisfies_fragments": true,
  "separate_from_base": true
}
```

### `guild-boss-current-system.duo-boundary`

- seed_key: "guild-boss-current-system.duo-boundary"
- kind: "other"
- requirement_level: "required"
- title: "명성 2인조"
- description: "구미호·두억시니는 표준 재충전이 아니라 명성 25,000 직접 소환 주간 우두머리다."
- structured_value:

```json
{
  "direct_summon": true,
  "fame_cost": 25000,
  "knowledge_role": "fact",
  "standard_recharge": false,
  "weekly_limit": 1
}
```

## Steps

### `guild-boss-current-system.step.fragments`

- seed_key: "guild-boss-current-system.step.fragments"
- phase: "preparation"
- order_no: 1
- title: "조각 확보"
- description: "길드 의뢰로 조각을 누적한다."
- checkable: false

### `guild-boss-current-system.step.region`

- seed_key: "guild-boss-current-system.step.region"
- phase: "first_time"
- order_no: 2
- title: "전용 지역 생성"
- description: "권한과 상태를 확인해 지역을 만든다."
- checkable: false

### `guild-boss-current-system.step.recharge`

- seed_key: "guild-boss-current-system.step.recharge"
- phase: "first_time"
- order_no: 3
- title: "추가 소환 판단"
- description: "필요하면 우두머리별 명성 재충전을 선택한다."
- checkable: false

## Schedules

### `guild-boss-current-system.weekly-reset`

- seed_key: "guild-boss-current-system.weekly-reset"
- rule_type: "attempt_reset"
- recurrence_type: "weekly"
- weekday: 0
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "표준 우두머리 횟수와 조각 초기화"

## Rewards

- None

## Sections

### `guild-boss-current-system.section.count`

- seed_key: "guild-boss-current-system.section.count"
- section_type: "notes"
- title: "횟수 의미"
- order_no: 1

#### body_markdown

기본 1회와 추가 1회가 분리되어 단일 boolean checklist를 만들지 않는다.

### `guild-boss-current-system.section.identity`

- seed_key: "guild-boss-current-system.section.identity"
- section_type: "notes"
- title: "동명 경계"
- order_no: 2

#### body_markdown

길드 구미호·두억시니는 검은사당 동명 Content와 별도다.

### `guild-boss-current-system.section.unresolved`

- seed_key: "guild-boss-current-system.section.unresolved"
- section_type: "notes"
- title: "미확정"
- order_no: 3

#### body_markdown

명성 2인조의 정확한 reset 시각은 별도 공식 명시가 없어 schedule로 만들지 않았다.

## Related Contents

### `guild-boss-current-system.relation.taxonomy`

- seed_key: "guild-boss-current-system.relation.taxonomy"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "boss-content-taxonomy"
- content_name_ko: "우두머리 콘텐츠 분류"
- content_category: "combat_pve"
- note: "우두머리 분류"
- order_no: 1
- relative_path: "../contents/boss-content-taxonomy.md"
### `guild-boss-current-system.relation.weekly`

- seed_key: "guild-boss-current-system.relation.weekly"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "weekly-quest-framework"
- content_name_ko: "주간 의뢰 공통 규칙"
- content_category: "system"
- note: "일반 목요일 주간과 다른 reset"
- order_no: 2
- relative_path: "../contents/weekly-quest-framework.md"
### `guild-boss-ferrid.relation.system`

- seed_key: "guild-boss-ferrid.relation.system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "guild-boss-ferrid"
- content_name_ko: "페리드"
- content_category: "combat_pve"
- note: "공통 규칙"
- order_no: 1
- relative_path: "../contents/guild-boss-ferrid.md"
### `guild-boss-giant-mudster.relation.system`

- seed_key: "guild-boss-giant-mudster.relation.system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "guild-boss-giant-mudster"
- content_name_ko: "거대한 진흙 괴물"
- content_category: "combat_pve"
- note: "공통 규칙"
- order_no: 1
- relative_path: "../contents/guild-boss-giant-mudster.md"
### `guild-boss-gumiho-duoksini.relation.system`

- seed_key: "guild-boss-gumiho-duoksini.relation.system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "guild-boss-gumiho-duoksini"
- content_name_ko: "길드 우두머리 구미호·두억시니"
- content_category: "combat_pve"
- note: "직접 소환 규칙"
- order_no: 1
- relative_path: "../contents/guild-boss-gumiho-duoksini.md"
### `guild-boss-mogulis.relation.system`

- seed_key: "guild-boss-mogulis.relation.system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "guild-boss-mogulis"
- content_name_ko: "모굴리스"
- content_category: "combat_pve"
- note: "공통 규칙"
- order_no: 1
- relative_path: "../contents/guild-boss-mogulis.md"
### `guild-boss-orgg.relation.system`

- seed_key: "guild-boss-orgg.relation.system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "guild-boss-orgg"
- content_name_ko: "오르그"
- content_category: "combat_pve"
- note: "공통 규칙"
- order_no: 1
- relative_path: "../contents/guild-boss-orgg.md"
### `khan-guild-boss.relation.system`

- seed_key: "khan-guild-boss.relation.system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "khan-guild-boss"
- content_name_ko: "대양의 눈동자 칸"
- content_category: "ocean_guide"
- note: "현행 공통 규칙"
- order_no: 2
- relative_path: "../contents/khan-guild-boss.md"

## Evidence and Sources

### Current evidence

### `guild-boss-current-system.claim.purpose::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-current-system.claim.purpose::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-current-system"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.purpose::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-current-system.claim.purpose::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-current-system"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.purpose::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-current-system.claim.purpose::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-current-system"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.purpose::guild-boss-reset-rework-2019-12-04`

- evidence_seed_key: "guild-boss-current-system.claim.purpose::guild-boss-reset-rework-2019-12-04"
- source_id: "guild-boss-reset-rework-2019-12-04"
- title: "12월 4일 (수) 업데이트 안내 (최종 수정 : 2019-12-19 16:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?boardNo=903&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2019-12-04"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-current-system"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.purpose::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "guild-boss-current-system.claim.purpose::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-current-system"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.summary::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-current-system.claim.summary::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-current-system"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.summary::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-current-system.claim.summary::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-current-system"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.summary::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-current-system.claim.summary::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-current-system"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.summary::guild-boss-reset-rework-2019-12-04`

- evidence_seed_key: "guild-boss-current-system.claim.summary::guild-boss-reset-rework-2019-12-04"
- source_id: "guild-boss-reset-rework-2019-12-04"
- title: "12월 4일 (수) 업데이트 안내 (최종 수정 : 2019-12-19 16:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?boardNo=903&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2019-12-04"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-current-system"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.summary::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "guild-boss-current-system.claim.summary::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "guild-boss-current-system"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.authority::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-current-system.claim.authority::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.authority"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.authority::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-current-system.claim.authority::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.authority"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.authority::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-current-system.claim.authority::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.authority"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.authority::guild-boss-reset-rework-2019-12-04`

- evidence_seed_key: "guild-boss-current-system.claim.authority::guild-boss-reset-rework-2019-12-04"
- source_id: "guild-boss-reset-rework-2019-12-04"
- title: "12월 4일 (수) 업데이트 안내 (최종 수정 : 2019-12-19 16:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?boardNo=903&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2019-12-04"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.authority"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.authority::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "guild-boss-current-system.claim.authority::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.authority"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.base-count::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-current-system.claim.base-count::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.base-count"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.base-count::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-current-system.claim.base-count::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.base-count"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.base-count::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-current-system.claim.base-count::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.base-count"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.base-count::guild-boss-reset-rework-2019-12-04`

- evidence_seed_key: "guild-boss-current-system.claim.base-count::guild-boss-reset-rework-2019-12-04"
- source_id: "guild-boss-reset-rework-2019-12-04"
- title: "12월 4일 (수) 업데이트 안내 (최종 수정 : 2019-12-19 16:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?boardNo=903&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2019-12-04"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.base-count"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.base-count::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "guild-boss-current-system.claim.base-count::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.base-count"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.duo-boundary::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-current-system.claim.duo-boundary::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.duo-boundary"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.duo-boundary::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-current-system.claim.duo-boundary::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.duo-boundary"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.duo-boundary::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-current-system.claim.duo-boundary::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.duo-boundary"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.duo-boundary::guild-boss-reset-rework-2019-12-04`

- evidence_seed_key: "guild-boss-current-system.claim.duo-boundary::guild-boss-reset-rework-2019-12-04"
- source_id: "guild-boss-reset-rework-2019-12-04"
- title: "12월 4일 (수) 업데이트 안내 (최종 수정 : 2019-12-19 16:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?boardNo=903&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2019-12-04"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.duo-boundary"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.duo-boundary::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "guild-boss-current-system.claim.duo-boundary::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.duo-boundary"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.fragment-flow::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-current-system.claim.fragment-flow::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.fragment-flow"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.fragment-flow::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-current-system.claim.fragment-flow::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.fragment-flow"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.fragment-flow::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-current-system.claim.fragment-flow::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.fragment-flow"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.fragment-flow::guild-boss-reset-rework-2019-12-04`

- evidence_seed_key: "guild-boss-current-system.claim.fragment-flow::guild-boss-reset-rework-2019-12-04"
- source_id: "guild-boss-reset-rework-2019-12-04"
- title: "12월 4일 (수) 업데이트 안내 (최종 수정 : 2019-12-19 16:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?boardNo=903&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2019-12-04"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.fragment-flow"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.fragment-flow::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "guild-boss-current-system.claim.fragment-flow::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.fragment-flow"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.recharge::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-current-system.claim.recharge::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.recharge"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.recharge::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-current-system.claim.recharge::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.recharge"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.recharge::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-current-system.claim.recharge::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.recharge"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.recharge::guild-boss-reset-rework-2019-12-04`

- evidence_seed_key: "guild-boss-current-system.claim.recharge::guild-boss-reset-rework-2019-12-04"
- source_id: "guild-boss-reset-rework-2019-12-04"
- title: "12월 4일 (수) 업데이트 안내 (최종 수정 : 2019-12-19 16:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?boardNo=903&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2019-12-04"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.recharge"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.recharge::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "guild-boss-current-system.claim.recharge::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.recharge"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.region::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-current-system.claim.region::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.region"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.region::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-current-system.claim.region::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.region"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.region::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-current-system.claim.region::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.region"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.region::guild-boss-reset-rework-2019-12-04`

- evidence_seed_key: "guild-boss-current-system.claim.region::guild-boss-reset-rework-2019-12-04"
- source_id: "guild-boss-reset-rework-2019-12-04"
- title: "12월 4일 (수) 업데이트 안내 (최종 수정 : 2019-12-19 16:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?boardNo=903&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2019-12-04"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.region"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.region::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "guild-boss-current-system.claim.region::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.region"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.restrictions::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-current-system.claim.restrictions::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.restrictions"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.restrictions::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-current-system.claim.restrictions::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.restrictions"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.restrictions::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-current-system.claim.restrictions::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.restrictions"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.restrictions::guild-boss-reset-rework-2019-12-04`

- evidence_seed_key: "guild-boss-current-system.claim.restrictions::guild-boss-reset-rework-2019-12-04"
- source_id: "guild-boss-reset-rework-2019-12-04"
- title: "12월 4일 (수) 업데이트 안내 (최종 수정 : 2019-12-19 16:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?boardNo=903&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2019-12-04"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.restrictions"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.restrictions::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "guild-boss-current-system.claim.restrictions::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.restrictions"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.roster::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-current-system.claim.roster::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.roster"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.roster::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-current-system.claim.roster::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.roster"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.roster::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-current-system.claim.roster::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.roster"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.roster::guild-boss-reset-rework-2019-12-04`

- evidence_seed_key: "guild-boss-current-system.claim.roster::guild-boss-reset-rework-2019-12-04"
- source_id: "guild-boss-reset-rework-2019-12-04"
- title: "12월 4일 (수) 업데이트 안내 (최종 수정 : 2019-12-19 16:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?boardNo=903&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2019-12-04"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.roster"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.roster::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "guild-boss-current-system.claim.roster::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "guild-boss-current-system.roster"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.section.count::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-current-system.claim.section.count::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-current-system.section.count"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.section.count::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-current-system.claim.section.count::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-current-system.section.count"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.section.count::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-current-system.claim.section.count::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-current-system.section.count"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.section.count::guild-boss-reset-rework-2019-12-04`

- evidence_seed_key: "guild-boss-current-system.claim.section.count::guild-boss-reset-rework-2019-12-04"
- source_id: "guild-boss-reset-rework-2019-12-04"
- title: "12월 4일 (수) 업데이트 안내 (최종 수정 : 2019-12-19 16:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?boardNo=903&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2019-12-04"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-current-system.section.count"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.section.count::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "guild-boss-current-system.claim.section.count::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-current-system.section.count"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.section.identity::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-current-system.claim.section.identity::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-current-system.section.identity"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.section.identity::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-current-system.claim.section.identity::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-current-system.section.identity"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.section.identity::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-current-system.claim.section.identity::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-current-system.section.identity"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.section.identity::guild-boss-reset-rework-2019-12-04`

- evidence_seed_key: "guild-boss-current-system.claim.section.identity::guild-boss-reset-rework-2019-12-04"
- source_id: "guild-boss-reset-rework-2019-12-04"
- title: "12월 4일 (수) 업데이트 안내 (최종 수정 : 2019-12-19 16:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?boardNo=903&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2019-12-04"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-current-system.section.identity"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.section.identity::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "guild-boss-current-system.claim.section.identity::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-current-system.section.identity"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.section.unresolved::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-current-system.claim.section.unresolved::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-current-system.section.unresolved"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.section.unresolved::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-current-system.claim.section.unresolved::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-current-system.section.unresolved"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.section.unresolved::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-current-system.claim.section.unresolved::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-current-system.section.unresolved"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.section.unresolved::guild-boss-reset-rework-2019-12-04`

- evidence_seed_key: "guild-boss-current-system.claim.section.unresolved::guild-boss-reset-rework-2019-12-04"
- source_id: "guild-boss-reset-rework-2019-12-04"
- title: "12월 4일 (수) 업데이트 안내 (최종 수정 : 2019-12-19 16:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?boardNo=903&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2019-12-04"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-current-system.section.unresolved"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.section.unresolved::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "guild-boss-current-system.claim.section.unresolved::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "guild-boss-current-system.section.unresolved"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.step.fragments::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-current-system.claim.step.fragments::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-current-system.step.fragments"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.step.fragments::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-current-system.claim.step.fragments::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-current-system.step.fragments"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.step.fragments::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-current-system.claim.step.fragments::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-current-system.step.fragments"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.step.fragments::guild-boss-reset-rework-2019-12-04`

- evidence_seed_key: "guild-boss-current-system.claim.step.fragments::guild-boss-reset-rework-2019-12-04"
- source_id: "guild-boss-reset-rework-2019-12-04"
- title: "12월 4일 (수) 업데이트 안내 (최종 수정 : 2019-12-19 16:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?boardNo=903&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2019-12-04"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-current-system.step.fragments"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.step.fragments::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "guild-boss-current-system.claim.step.fragments::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-current-system.step.fragments"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.step.recharge::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-current-system.claim.step.recharge::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-current-system.step.recharge"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.step.recharge::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-current-system.claim.step.recharge::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-current-system.step.recharge"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.step.recharge::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-current-system.claim.step.recharge::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-current-system.step.recharge"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.step.recharge::guild-boss-reset-rework-2019-12-04`

- evidence_seed_key: "guild-boss-current-system.claim.step.recharge::guild-boss-reset-rework-2019-12-04"
- source_id: "guild-boss-reset-rework-2019-12-04"
- title: "12월 4일 (수) 업데이트 안내 (최종 수정 : 2019-12-19 16:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?boardNo=903&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2019-12-04"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-current-system.step.recharge"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.step.recharge::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "guild-boss-current-system.claim.step.recharge::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-current-system.step.recharge"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.step.region::edania-inner-boss-2026-08-12`

- evidence_seed_key: "guild-boss-current-system.claim.step.region::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-current-system.step.region"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.step.region::guild-boss-guide-current`

- evidence_seed_key: "guild-boss-current-system.claim.step.region::guild-boss-guide-current"
- source_id: "guild-boss-guide-current"
- title: "길드 소환 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=171"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-current-system.step.region"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.step.region::guild-boss-overhaul-2026-01-07`

- evidence_seed_key: "guild-boss-current-system.claim.step.region::guild-boss-overhaul-2026-01-07"
- source_id: "guild-boss-overhaul-2026-01-07"
- title: "1월 7일(수) 업데이트 안내 (최종 수정 : 2026-01-07 18:46)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15054"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-07"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-current-system.step.region"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.step.region::guild-boss-reset-rework-2019-12-04`

- evidence_seed_key: "guild-boss-current-system.claim.step.region::guild-boss-reset-rework-2019-12-04"
- source_id: "guild-boss-reset-rework-2019-12-04"
- title: "12월 4일 (수) 업데이트 안내 (최종 수정 : 2019-12-19 16:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?boardNo=903&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2019-12-04"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-current-system.step.region"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.step.region::marni-combat-analyzer-2026-08-05`

- evidence_seed_key: "guild-boss-current-system.claim.step.region::marni-combat-analyzer-2026-08-05"
- source_id: "marni-combat-analyzer-2026-08-05"
- title: "8월 5일(수) 업데이트 안내(최종 수정 : 2026-08-06 18:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15998"
- publisher: "Pearl Abyss"
- source_type: "official_patch_notes"
- published_at: "2026-08-05"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content_step"
- entity_id: "guild-boss-current-system.step.region"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### `guild-boss-current-system.claim.schedule::guild-boss-reset-rework-2019-12-04`

- evidence_seed_key: "guild-boss-current-system.claim.schedule::guild-boss-reset-rework-2019-12-04"
- source_id: "guild-boss-reset-rework-2019-12-04"
- title: "12월 4일 (수) 업데이트 안내 (최종 수정 : 2019-12-19 16:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?boardNo=903&countryType=ko-KR"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2019-12-04"
- retrieved_at: "2026-09-08T12:00:00+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "guild-boss-current-system.weekly-reset"
- claim_key: "schedule.attempt_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-08"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
