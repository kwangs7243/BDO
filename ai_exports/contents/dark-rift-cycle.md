<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 어둠의 틈 주기

## Identity

- slug: "dark-rift-cycle"
- name_ko: "어둠의 틈 주기"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: "solo"
- difficulty: null

## Overview

- summary: "6종 우두머리가 각각 처치 시점부터 120시간 뒤 재생성되는 개인 주기 콘텐츠. 목요일 주간 초기화가 아니다."
- purpose: "개별 생성된 어둠의 틈 우두머리를 처치하고 확정 보상을 획득한다."

## Requirements

### `dark-rift-cycle.level`

- seed_key: "dark-rift-cycle.level"
- kind: "level"
- requirement_level: "required"
- title: "레벨"
- description: "캐릭터 레벨 56 이상."
- structured_value:

```json
{
  "minimum_level": 56
}
```

### `dark-rift-cycle.first-spawn`

- seed_key: "dark-rift-cycle.first-spawn"
- kind: "other"
- requirement_level: "required"
- title: "최초 출현"
- description: "조건 달성 뒤 최초 출현까지 24시간이 걸린다."
- structured_value:

```json
{
  "first_spawn_delay_hours": 24
}
```

### `dark-rift-cycle.bosses`

- seed_key: "dark-rift-cycle.bosses"
- kind: "other"
- requirement_level: "required"
- title: "현재 우두머리"
- description: "빨간코, 비겁한 베그, 머스칸, 우둔한 나무 정령, 페리드, 아히브의 그리폰의 6종이다."
- structured_value:

```json
{
  "boss_count": 6,
  "bosses": [
    "빨간코",
    "비겁한 베그",
    "머스칸",
    "우둔한 나무 정령",
    "페리드",
    "아히브의 그리폰"
  ]
}
```

### `dark-rift-cycle.difficulty-decay`

- seed_key: "dark-rift-cycle.difficulty-decay"
- kind: "other"
- requirement_level: "optional"
- title: "난이도 하락"
- description: "생성 후 처치하지 않으면 24시간마다 난이도가 하락한다."
- structured_value:

```json
{
  "difficulty_decay_hours": 24
}
```

## Steps

### `dark-rift-cycle.kill-and-record`

- seed_key: "dark-rift-cycle.kill-and-record"
- phase: "repeat"
- order_no: 1
- title: "처치 시점 기록"
- description: "각 우두머리 처치 시점을 기준으로 다음 120시간 재생성 시점을 관리한다."
- checkable: true

## Schedules

### `dark-rift-cycle.respawn`

- seed_key: "dark-rift-cycle.respawn"
- rule_type: "respawn"
- recurrence_type: "rolling"
- weekday: null
- time_local: null
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "각 우두머리 처치 시점 +120시간; 고정 요일 reset 아님"

## Rewards

### `dark-rift-cycle.cron-per-boss`

- seed_key: "dark-rift-cycle.cron-per-boss"
- name: "크론석"
- reward_type: "boss_reward"
- amount: 100.0
- min_amount: null
- max_amount: null
- unit: "개/우두머리"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "6종 합계 600은 주간 고정 보상이 아님"
- order_no: 1

### `dark-rift-cycle.dawn-stone-and-gold`

- seed_key: "dark-rift-cycle.dawn-stone-and-gold"
- name: "새벽의 블랙스톤 및 금괴"
- reward_type: "boss_reward"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "2026-01-14 패치로 확정·추가된 보상"
- order_no: 2

## Sections

### `dark-rift-cycle.not-weekly`

- seed_key: "dark-rift-cycle.not-weekly"
- section_type: "common_mistakes"
- title: "주간 초기화가 아님"
- order_no: 1

#### body_markdown

각 우두머리는 독립적으로 처치 후 120시간 뒤 재생성된다. 6종 합계 크론석 600개를 주간 고정 보상으로 해석하지 않는다.

## Related Contents

- None

## Evidence and Sources

### Current evidence

### `dark-rift-cycle.summary::dark-rift-guide`

- evidence_seed_key: "dark-rift-cycle.summary::dark-rift-guide"
- source_id: "dark-rift-guide"
- title: "어둠의 틈"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=244"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "dark-rift-cycle"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "6종 독립 120시간 재생성"
- active: true
- is_active: true

### `dark-rift-cycle.requirement.bosses::dark-rift-guide`

- evidence_seed_key: "dark-rift-cycle.requirement.bosses::dark-rift-guide"
- source_id: "dark-rift-guide"
- title: "어둠의 틈"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=244"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "dark-rift-cycle.bosses"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "현재 6종 우두머리"
- active: true
- is_active: true

### `dark-rift-cycle.requirement.difficulty::dark-rift-guide`

- evidence_seed_key: "dark-rift-cycle.requirement.difficulty::dark-rift-guide"
- source_id: "dark-rift-guide"
- title: "어둠의 틈"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=244"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "dark-rift-cycle.difficulty-decay"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "24시간마다 난이도 하락"
- active: true
- is_active: true

### `dark-rift-cycle.requirement.first-spawn::dark-rift-guide`

- evidence_seed_key: "dark-rift-cycle.requirement.first-spawn::dark-rift-guide"
- source_id: "dark-rift-guide"
- title: "어둠의 틈"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=244"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "dark-rift-cycle.first-spawn"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "최초 출현 24시간"
- active: true
- is_active: true

### `dark-rift-cycle.requirement.level::dark-rift-guide`

- evidence_seed_key: "dark-rift-cycle.requirement.level::dark-rift-guide"
- source_id: "dark-rift-guide"
- title: "어둠의 틈"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=244"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "dark-rift-cycle.level"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "레벨 56 이상"
- active: true
- is_active: true

### `dark-rift-cycle.reward.cron::dark-rift-reward-2026-01-14`

- evidence_seed_key: "dark-rift-cycle.reward.cron::dark-rift-reward-2026-01-14"
- source_id: "dark-rift-reward-2026-01-14"
- title: "1월 14일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15070"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-14"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "dark-rift-cycle.cron-per-boss"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "우두머리별 크론석 100개"
- active: true
- is_active: true

### `dark-rift-cycle.reward.dawn-gold::dark-rift-reward-2026-01-14`

- evidence_seed_key: "dark-rift-cycle.reward.dawn-gold::dark-rift-reward-2026-01-14"
- source_id: "dark-rift-reward-2026-01-14"
- title: "1월 14일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15070"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-01-14"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "dark-rift-cycle.dawn-stone-and-gold"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "새벽의 블랙스톤과 금괴 보상"
- active: true
- is_active: true

### `dark-rift-cycle.schedule.respawn::dark-rift-guide`

- evidence_seed_key: "dark-rift-cycle.schedule.respawn::dark-rift-guide"
- source_id: "dark-rift-guide"
- title: "어둠의 틈"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=244"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "dark-rift-cycle.respawn"
- claim_key: "schedule.respawn"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "처치 후 120시간 rolling cooldown"
- active: true
- is_active: true

### Historical / inactive evidence

- None
