<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 월드 우두머리 현재 시스템

## Identity

- slug: "world-boss-current-system"
- name_ko: "월드 우두머리 현재 시스템"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "open_world"
- difficulty: "varies"

## Overview

- summary: "일반 서버에서 서버군 간 생명력을 공유하며 최대 2마리가 동시에 등장할 수 있다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `world-boss-current-system.core`

- seed_key: "world-boss-current-system.core"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 공통 규칙"
- description: "올비아·아르샤를 제외한 일반 서버에서 생명력을 공유한다."
- structured_value:

```json
{
  "excluded_server_groups": [
    "Olvia",
    "Arsha"
  ],
  "knowledge_role": "fact",
  "max_simultaneous_bosses": 2,
  "shared_hp_across_servers": true
}
```

### `world-boss-current-system.despawn`

- seed_key: "world-boss-current-system.despawn"
- kind: "knowledge"
- requirement_level: "required"
- title: "퇴장 시간"
- description: "일반 월드 우두머리는 30분, 귄트와 무라카는 15분 뒤 퇴장한다."
- structured_value:

```json
{
  "exceptions": {
    "Muraka": 15,
    "Quint": 15
  },
  "generic_minutes": 30,
  "knowledge_role": "fact"
}
```

### `world-boss-current-system.loot`

- seed_key: "world-boss-current-system.loot"
- kind: "knowledge"
- requirement_level: "required"
- title: "전리품 기여도"
- description: "피해 기여도는 중요하지만 전리품 획득을 결정하는 유일한 조건은 아니다."
- structured_value:

```json
{
  "damage_contribution_matters": true,
  "damage_is_only_factor": false,
  "knowledge_role": "fact"
}
```

### `world-boss-current-system.vell`

- seed_key: "world-boss-current-system.vell"
- kind: "knowledge"
- requirement_level: "required"
- title: "벨 현재 운영"
- description: "벨은 목요일 00:15와 일요일 17:00에 등장하며 대포 기반 전투, 파티·부대 대포 기여도 공유, 사망 불이익 없음 규칙을 가진다."
- structured_value:

```json
{
  "cannon_based": true,
  "death_penalty": false,
  "knowledge_role": "fact",
  "party_or_platoon_cannon_contribution_shared": true,
  "spawn_times": [
    {
      "time": "00:15",
      "weekday": 3
    },
    {
      "time": "17:00",
      "weekday": 6
    }
  ],
  "timezone": "Asia/Seoul"
}
```

### `world-boss-current-system.garmoth`

- seed_key: "world-boss-current-system.garmoth"
- kind: "knowledge"
- requirement_level: "required"
- title: "가모스 기존 주간 보상 연동"
- description: "기존 가모스 루틴의 가문당 주간 보상 최대 3회와 목요일 00:00 초기화를 재사용한다."
- structured_value:

```json
{
  "knowledge_role": "fact",
  "reset_time": "00:00",
  "reset_weekday": 3,
  "reuses_existing_routine": true,
  "timezone": "Asia/Seoul",
  "weekly_reward_max": 3
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

### `world-boss-current-system.taxonomy`

- seed_key: "world-boss-current-system.taxonomy"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "boss-content-taxonomy"
- content_name_ko: "우두머리 콘텐츠 분류"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/boss-content-taxonomy.md"
### `world-boss-current-system.vell-existing`

- seed_key: "world-boss-current-system.vell-existing"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "vell"
- content_name_ko: "벨"
- content_category: "world_boss"
- note: "기존 벨 Content를 재사용한다."
- order_no: 2
- relative_path: "../contents/vell.md"
### `world-boss-current-system.garmoth-existing`

- seed_key: "world-boss-current-system.garmoth-existing"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "garmoth"
- content_name_ko: "가모스"
- content_category: "world_boss"
- note: "기존 가모스 주간 루틴을 재사용한다."
- order_no: 3
- relative_path: "../contents/garmoth.md"
### `morning-land-world-bosses.current-system`

- seed_key: "morning-land-world-bosses.current-system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "morning-land-world-bosses"
- content_name_ko: "아침의 나라 월드 우두머리"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/morning-land-world-bosses.md"
### `world-boss-black-phoenix.current-system`

- seed_key: "world-boss-black-phoenix.current-system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "world-boss-black-phoenix"
- content_name_ko: "검은 봉황 (월드 우두머리)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-black-phoenix.md"
### `world-boss-bulgasal.system`

- seed_key: "world-boss-bulgasal.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "world-boss-bulgasal"
- content_name_ko: "불가살 (월드 우두머리)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-bulgasal.md"
### `world-boss-golden-pig-king.system`

- seed_key: "world-boss-golden-pig-king.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "world-boss-golden-pig-king"
- content_name_ko: "금돼지왕 (월드 우두머리)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-golden-pig-king.md"
### `world-boss-karanda.system`

- seed_key: "world-boss-karanda.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "world-boss-karanda"
- content_name_ko: "카란다 (월드 우두머리)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-karanda.md"
### `world-boss-kutum.system`

- seed_key: "world-boss-kutum.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "world-boss-kutum"
- content_name_ko: "쿠툼 (월드 우두머리)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-kutum.md"
### `world-boss-kzarka.system`

- seed_key: "world-boss-kzarka.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "world-boss-kzarka"
- content_name_ko: "크자카 (월드 우두머리)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-kzarka.md"
### `world-boss-muraka.system`

- seed_key: "world-boss-muraka.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "world-boss-muraka"
- content_name_ko: "무라카 (월드 우두머리)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-muraka.md"
### `world-boss-nouver.system`

- seed_key: "world-boss-nouver.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "world-boss-nouver"
- content_name_ko: "누베르 (월드 우두머리)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-nouver.md"
### `world-boss-offin.system`

- seed_key: "world-boss-offin.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "world-boss-offin"
- content_name_ko: "미루목 파괴자 오핀 (월드 우두머리)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-offin.md"
### `world-boss-quint.system`

- seed_key: "world-boss-quint.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "world-boss-quint"
- content_name_ko: "귄트 (월드 우두머리)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-quint.md"
### `world-boss-reward-2025-overhaul.current-system`

- seed_key: "world-boss-reward-2025-overhaul.current-system"
- direction: "incoming"
- relation_type: "related"
- content_slug: "world-boss-reward-2025-overhaul"
- content_name_ko: "2025-12-23 월드 우두머리 보상 개편"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-reward-2025-overhaul.md"
### `world-boss-sangoon.system`

- seed_key: "world-boss-sangoon.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "world-boss-sangoon"
- content_name_ko: "산군 (월드 우두머리)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-sangoon.md"
### `world-boss-uturi.system`

- seed_key: "world-boss-uturi.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "world-boss-uturi"
- content_name_ko: "우투리 (월드 우두머리)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/world-boss-uturi.md"
### `boss-guide-conflicts.world-boss`

- seed_key: "boss-guide-conflicts.world-boss"
- direction: "incoming"
- relation_type: "related"
- content_slug: "boss-guide-conflicts"
- content_name_ko: "우두머리 가이드 충돌 및 발표 상태"
- content_category: "combat_pve"
- note: null
- order_no: 3
- relative_path: "../contents/boss-guide-conflicts.md"

## Evidence and Sources

### Current evidence

### `world-boss-current-system.claim.core::rare-wild-horses-2025-12-23`

- evidence_seed_key: "world-boss-current-system.claim.core::rare-wild-horses-2025-12-23"
- source_id: "rare-wild-horses-2025-12-23"
- title: "12월 23일(화) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14989"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-12-23"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "world-boss-current-system.core"
- claim_key: "requirement:core"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `world-boss-current-system.claim.core::world-boss-guide`

- evidence_seed_key: "world-boss-current-system.claim.core::world-boss-guide"
- source_id: "world-boss-guide"
- title: "월드 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=89"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "world-boss-current-system.core"
- claim_key: "requirement:core"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `world-boss-current-system.claim.despawn::world-boss-guide`

- evidence_seed_key: "world-boss-current-system.claim.despawn::world-boss-guide"
- source_id: "world-boss-guide"
- title: "월드 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=89"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "world-boss-current-system.despawn"
- claim_key: "requirement:despawn"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `world-boss-current-system.claim.garmoth::garmoth-reward-2024-05-29`

- evidence_seed_key: "world-boss-current-system.claim.garmoth::garmoth-reward-2024-05-29"
- source_id: "garmoth-reward-2024-05-29"
- title: "5월 29일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=12254"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2024-05-29"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "world-boss-current-system.garmoth"
- claim_key: "requirement:garmoth"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `world-boss-current-system.claim.garmoth::world-boss-guide`

- evidence_seed_key: "world-boss-current-system.claim.garmoth::world-boss-guide"
- source_id: "world-boss-guide"
- title: "월드 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=89"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "world-boss-current-system.garmoth"
- claim_key: "requirement:garmoth"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `world-boss-current-system.claim.loot::world-boss-guide`

- evidence_seed_key: "world-boss-current-system.claim.loot::world-boss-guide"
- source_id: "world-boss-guide"
- title: "월드 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=89"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "world-boss-current-system.loot"
- claim_key: "requirement:loot"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `world-boss-current-system.claim.vell::world-boss-guide`

- evidence_seed_key: "world-boss-current-system.claim.vell::world-boss-guide"
- source_id: "world-boss-guide"
- title: "월드 우두머리 레이드"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=89"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "world-boss-current-system.vell"
- claim_key: "requirement:vell"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
