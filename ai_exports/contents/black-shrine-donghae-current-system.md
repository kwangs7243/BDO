<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 검은사당 동해도 현재 시스템

## Identity

- slug: "black-shrine-donghae-current-system"
- name_ko: "검은사당 동해도 현재 시스템"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "varies"

## Overview

- summary: "개인 전투이며 가문당 주 5회 보상 획득, 같은 우두머리·난이도 재도전은 제한 없이 가능하다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `black-shrine-donghae-current-system.core`

- seed_key: "black-shrine-donghae-current-system.core"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 진행 규칙"
- description: "주 5회는 입장 제한이 아니라 보상 획득 가능 횟수다."
- structured_value:

```json
{
  "failed_attempt_consumes_reward_count": false,
  "knowledge_role": "fact",
  "same_boss_difficulty_retry": "unlimited",
  "scope": "family",
  "solo": true,
  "weekly_rewarded_clears": 5
}
```

### `black-shrine-donghae-current-system.weekly-payout`

- seed_key: "black-shrine-donghae-current-system.weekly-payout"
- kind: "knowledge"
- requirement_level: "required"
- title: "주간 보상 지급"
- description: "보상은 일요일 00:00 KST 이후 흑정령의 선물함으로 지급되고 누적되며 소멸 기한이 없다."
- structured_value:

```json
{
  "accumulates": true,
  "destination": "Black Spirit Safe",
  "expires": false,
  "knowledge_role": "fact",
  "payout_time": "00:00",
  "payout_weekday": 6,
  "timezone": "Asia/Seoul"
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

### `black-shrine-donghae-current-system.existing-routine`

- seed_key: "black-shrine-donghae-current-system.existing-routine"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "black-shrine-donghae-weekly"
- content_name_ko: "검은 사당 - 동해도 주간 토벌"
- content_category: "combat_pve"
- note: "기존 V1.6E 주간 루틴을 재사용한다."
- order_no: 1
- relative_path: "../contents/black-shrine-donghae-weekly.md"
### `black-shrine-donghae-current-system.taxonomy`

- seed_key: "black-shrine-donghae-current-system.taxonomy"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "boss-content-taxonomy"
- content_name_ko: "우두머리 콘텐츠 분류"
- content_category: "combat_pve"
- note: null
- order_no: 2
- relative_path: "../contents/boss-content-taxonomy.md"
### `boss-guide-conflicts.donghae`

- seed_key: "boss-guide-conflicts.donghae"
- direction: "incoming"
- relation_type: "related"
- content_slug: "boss-guide-conflicts"
- content_name_ko: "우두머리 가이드 충돌 및 발표 상태"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/boss-guide-conflicts.md"
### `donghae-calamity-8-10.current-system`

- seed_key: "donghae-calamity-8-10.current-system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "donghae-calamity-8-10"
- content_name_ko: "동해도 팔·구·십재시니"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/donghae-calamity-8-10.md"
### `donghae-hyperboost-armor-support.current-system`

- seed_key: "donghae-hyperboost-armor-support.current-system"
- direction: "incoming"
- relation_type: "related"
- content_slug: "donghae-hyperboost-armor-support"
- content_name_ko: "동해도 하이퍼 부스트 방어구 지원"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/donghae-hyperboost-armor-support.md"
### `donghae-light-orb-system.current-system`

- seed_key: "donghae-light-orb-system.current-system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "donghae-light-orb-system"
- content_name_ko: "동해도 빛의 보옥 시스템"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/donghae-light-orb-system.md"
### `donghae-shrine-apex-changui.system`

- seed_key: "donghae-shrine-apex-changui.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "donghae-shrine-apex-changui"
- content_name_ko: "대창귀 우두머리 (동해도 검은사당)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/donghae-shrine-apex-changui.md"
### `donghae-shrine-bamboo-legion-lieutenant.system`

- seed_key: "donghae-shrine-bamboo-legion-lieutenant.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "donghae-shrine-bamboo-legion-lieutenant"
- content_name_ko: "죽엽군장 (동해도 검은사당)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/donghae-shrine-bamboo-legion-lieutenant.md"
### `donghae-shrine-bari.system`

- seed_key: "donghae-shrine-bari.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "donghae-shrine-bari"
- content_name_ko: "바리 (동해도 검은사당)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/donghae-shrine-bari.md"
### `donghae-shrine-duoksini.system`

- seed_key: "donghae-shrine-duoksini.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "donghae-shrine-duoksini"
- content_name_ko: "두억시니 (동해도 검은사당)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/donghae-shrine-duoksini.md"
### `donghae-shrine-golden-pig-king.system`

- seed_key: "donghae-shrine-golden-pig-king.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "donghae-shrine-golden-pig-king"
- content_name_ko: "금돼지왕 (동해도 검은사당)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/donghae-shrine-golden-pig-king.md"
### `donghae-shrine-gumiho.system`

- seed_key: "donghae-shrine-gumiho.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "donghae-shrine-gumiho"
- content_name_ko: "구미호 (동해도 검은사당)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/donghae-shrine-gumiho.md"
### `donghae-shrine-imoogi.system`

- seed_key: "donghae-shrine-imoogi.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "donghae-shrine-imoogi"
- content_name_ko: "이무기 (동해도 검은사당)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/donghae-shrine-imoogi.md"
### `donghae-shrine-oduksini.system`

- seed_key: "donghae-shrine-oduksini.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "donghae-shrine-oduksini"
- content_name_ko: "어둑시니 (동해도 검은사당)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/donghae-shrine-oduksini.md"
### `donghae-shrine-sangoon.system`

- seed_key: "donghae-shrine-sangoon.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "donghae-shrine-sangoon"
- content_name_ko: "산군 (동해도 검은사당)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/donghae-shrine-sangoon.md"
### `donghae-shrine-songakshi.system`

- seed_key: "donghae-shrine-songakshi.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "donghae-shrine-songakshi"
- content_name_ko: "손각시 (동해도 검은사당)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/donghae-shrine-songakshi.md"
### `morning-land-boss-codex.donghae`

- seed_key: "morning-land-boss-codex.donghae"
- direction: "incoming"
- relation_type: "related"
- content_slug: "morning-land-boss-codex"
- content_name_ko: "우두머리 도감 : 아침의 나라"
- content_category: "progression"
- note: "주간 토벌 Content와 identity 분리"
- order_no: 2
- relative_path: "../contents/morning-land-boss-codex.md"
### `emma-bartali-record-log.donghae`

- seed_key: "emma-bartali-record-log.donghae"
- direction: "incoming"
- relation_type: "related"
- content_slug: "emma-bartali-record-log"
- content_name_ko: "엠마 바탈리의 기록일지"
- content_category: "progression"
- note: "7~8장 동해도 개인 구재시니 토벌 조건"
- order_no: 4
- relative_path: "../contents/emma-bartali-record-log.md"

## Evidence and Sources

### Current evidence

### `black-shrine-donghae-current-system.claim.core::black-shrine-donghae-guide`

- evidence_seed_key: "black-shrine-donghae-current-system.claim.core::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "black-shrine-donghae-current-system.core"
- claim_key: "requirement:core"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `black-shrine-donghae-current-system.claim.weekly-payout::black-shrine-donghae-guide`

- evidence_seed_key: "black-shrine-donghae-current-system.claim.weekly-payout::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "black-shrine-donghae-current-system.weekly-payout"
- claim_key: "requirement:weekly-payout"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `black-shrine-donghae-current-system.claim.weekly-payout::blood-altar-challenge-2026-07-15`

- evidence_seed_key: "black-shrine-donghae-current-system.claim.weekly-payout::blood-altar-challenge-2026-07-15"
- source_id: "blood-altar-challenge-2026-07-15"
- title: "7월 15일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15878"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-07-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "black-shrine-donghae-current-system.weekly-payout"
- claim_key: "requirement:weekly-payout"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
