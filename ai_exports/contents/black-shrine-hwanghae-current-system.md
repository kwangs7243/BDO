<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 검은사당 황해도 현재 시스템

## Identity

- slug: "black-shrine-hwanghae-current-system"
- name_ko: "검은사당 황해도 현재 시스템"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "party"
- difficulty: "varies"

## Overview

- summary: "5인 파티, 가문당 주 5회 보상 획득 구조이며 실패는 횟수를 소모하지 않는다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `black-shrine-hwanghae-current-system.core`

- seed_key: "black-shrine-hwanghae-current-system.core"
- kind: "knowledge"
- requirement_level: "required"
- title: "현재 진행 규칙"
- description: "보상 횟수를 소진한 뒤에도 도움 참가가 가능하지만 일부 이벤트·길드 임무 집계는 별도다."
- structured_value:

```json
{
  "event_or_guild_count_may_not_apply": true,
  "failed_attempt_consumes_reward_count": false,
  "help_after_rewards_exhausted": true,
  "knowledge_role": "fact",
  "party_size": 5,
  "retry_allowed": true,
  "scope": "family",
  "weekly_rewarded_clears": 5
}
```

### `black-shrine-hwanghae-current-system.difficulty`

- seed_key: "black-shrine-hwanghae-current-system.difficulty"
- kind: "knowledge"
- requirement_level: "required"
- title: "난이도와 능력치"
- description: "일반은 공격력 300, 도전은 330이며 빛의 보옥 없이 장비 능력치 100%가 적용된다."
- structured_value:

```json
{
  "challenge_recommended_ap": 330,
  "character_gear_stat_percent": 100,
  "knowledge_role": "fact",
  "light_orb_active": false,
  "normal_recommended_ap": 300
}
```

### `black-shrine-hwanghae-current-system.entry`

- seed_key: "black-shrine-hwanghae-current-system.entry"
- kind: "knowledge"
- requirement_level: "required"
- title: "파티 입장과 컷신"
- description: "파티장이 입장하며 5명 중 3명이 동의하면 컷신을 건너뛴다."
- structured_value:

```json
{
  "cutscene_skip_votes_required": 3,
  "knowledge_role": "fact",
  "leader_starts_entry": true,
  "party_size": 5
}
```

### `black-shrine-hwanghae-current-system.healing-buffs`

- seed_key: "black-shrine-hwanghae-current-system.healing-buffs"
- kind: "knowledge"
- requirement_level: "required"
- title: "회복과 버프 제한"
- description: "물약은 비활성화되지만 자연·기술·콘텐츠 구슬 회복은 가능하다. 제거 대상은 일부 클래스 기술 버프와 순수한 마력의 블랙스톤 특수 버프다."
- structured_value:

```json
{
  "all_buffs_removed": false,
  "content_orb_healing_possible": true,
  "knowledge_role": "fact",
  "natural_healing_possible": true,
  "potions_disabled": true,
  "removed_buff_scope": [
    "selected class skill buffs",
    "Pure Magic Black Stone special buffs"
  ],
  "skill_healing_possible": true
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

### `black-shrine-hwanghae-current-system.existing-routine`

- seed_key: "black-shrine-hwanghae-current-system.existing-routine"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "black-shrine-hwanghae-weekly"
- content_name_ko: "검은 사당 - 황해도 주간 토벌"
- content_category: "combat_pve"
- note: "기존 V1.6E 주간 루틴을 재사용한다."
- order_no: 1
- relative_path: "../contents/black-shrine-hwanghae-weekly.md"
### `black-shrine-hwanghae-current-system.taxonomy`

- seed_key: "black-shrine-hwanghae-current-system.taxonomy"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "boss-content-taxonomy"
- content_name_ko: "우두머리 콘텐츠 분류"
- content_category: "combat_pve"
- note: null
- order_no: 2
- relative_path: "../contents/boss-content-taxonomy.md"
### `hwanghae-aura-system.current-system`

- seed_key: "hwanghae-aura-system.current-system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "hwanghae-aura-system"
- content_name_ko: "황해도 기운 선택"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/hwanghae-aura-system.md"
### `hwanghae-party-strategy.current-system`

- seed_key: "hwanghae-party-strategy.current-system"
- direction: "incoming"
- relation_type: "related"
- content_slug: "hwanghae-party-strategy"
- content_name_ko: "황해도 파티 전략"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/hwanghae-party-strategy.md"
### `hwanghae-shrine-bihyung.system`

- seed_key: "hwanghae-shrine-bihyung.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "hwanghae-shrine-bihyung"
- content_name_ko: "비형랑 (황해도 검은사당)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/hwanghae-shrine-bihyung.md"
### `hwanghae-shrine-blue-clad-youth.system`

- seed_key: "hwanghae-shrine-blue-clad-youth.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "hwanghae-shrine-blue-clad-youth"
- content_name_ko: "청의동자 (황해도 검은사당)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/hwanghae-shrine-blue-clad-youth.md"
### `hwanghae-shrine-bulgasal.system`

- seed_key: "hwanghae-shrine-bulgasal.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "hwanghae-shrine-bulgasal"
- content_name_ko: "불가살 (황해도 검은사당)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/hwanghae-shrine-bulgasal.md"
### `hwanghae-shrine-dark-bonghwang.system`

- seed_key: "hwanghae-shrine-dark-bonghwang.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "hwanghae-shrine-dark-bonghwang"
- content_name_ko: "흑봉황 (황해도 검은사당)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/hwanghae-shrine-dark-bonghwang.md"
### `hwanghae-shrine-deposed-crown-prince.system`

- seed_key: "hwanghae-shrine-deposed-crown-prince.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "hwanghae-shrine-deposed-crown-prince"
- content_name_ko: "폐세자 (황해도 검은사당)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/hwanghae-shrine-deposed-crown-prince.md"
### `hwanghae-shrine-jigwi.system`

- seed_key: "hwanghae-shrine-jigwi.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "hwanghae-shrine-jigwi"
- content_name_ko: "지귀 (황해도 검은사당)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/hwanghae-shrine-jigwi.md"
### `hwanghae-shrine-uturi.system`

- seed_key: "hwanghae-shrine-uturi.system"
- direction: "incoming"
- relation_type: "part_of"
- content_slug: "hwanghae-shrine-uturi"
- content_name_ko: "우투리 (황해도 검은사당)"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/hwanghae-shrine-uturi.md"
### `boss-guide-conflicts.hwanghae`

- seed_key: "boss-guide-conflicts.hwanghae"
- direction: "incoming"
- relation_type: "related"
- content_slug: "boss-guide-conflicts"
- content_name_ko: "우두머리 가이드 충돌 및 발표 상태"
- content_category: "combat_pve"
- note: null
- order_no: 2
- relative_path: "../contents/boss-guide-conflicts.md"
### `morning-land-boss-codex.hwanghae`

- seed_key: "morning-land-boss-codex.hwanghae"
- direction: "incoming"
- relation_type: "related"
- content_slug: "morning-land-boss-codex"
- content_name_ko: "우두머리 도감 : 아침의 나라"
- content_category: "progression"
- note: "주간 토벌 Content와 identity 분리"
- order_no: 3
- relative_path: "../contents/morning-land-boss-codex.md"
### `emma-bartali-record-log.hwanghae`

- seed_key: "emma-bartali-record-log.hwanghae"
- direction: "incoming"
- relation_type: "related"
- content_slug: "emma-bartali-record-log"
- content_name_ko: "엠마 바탈리의 기록일지"
- content_category: "progression"
- note: "9~12장 황해도 파티 도전 난이도 토벌 조건"
- order_no: 5
- relative_path: "../contents/emma-bartali-record-log.md"

## Evidence and Sources

### Current evidence

### `black-shrine-hwanghae-current-system.claim.core::black-shrine-hwanghae-guide`

- evidence_seed_key: "black-shrine-hwanghae-current-system.claim.core::black-shrine-hwanghae-guide"
- source_id: "black-shrine-hwanghae-guide"
- title: "검은 사당 - 황해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=404"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "black-shrine-hwanghae-current-system.core"
- claim_key: "requirement:core"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `black-shrine-hwanghae-current-system.claim.difficulty::black-shrine-hwanghae-guide`

- evidence_seed_key: "black-shrine-hwanghae-current-system.claim.difficulty::black-shrine-hwanghae-guide"
- source_id: "black-shrine-hwanghae-guide"
- title: "검은 사당 - 황해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=404"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "black-shrine-hwanghae-current-system.difficulty"
- claim_key: "requirement:difficulty"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `black-shrine-hwanghae-current-system.claim.entry::black-shrine-hwanghae-guide`

- evidence_seed_key: "black-shrine-hwanghae-current-system.claim.entry::black-shrine-hwanghae-guide"
- source_id: "black-shrine-hwanghae-guide"
- title: "검은 사당 - 황해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=404"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "black-shrine-hwanghae-current-system.entry"
- claim_key: "requirement:entry"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `black-shrine-hwanghae-current-system.claim.healing-buffs::black-shrine-hwanghae-guide`

- evidence_seed_key: "black-shrine-hwanghae-current-system.claim.healing-buffs::black-shrine-hwanghae-guide"
- source_id: "black-shrine-hwanghae-guide"
- title: "검은 사당 - 황해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=404"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "black-shrine-hwanghae-current-system.healing-buffs"
- claim_key: "requirement:healing-buffs"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
