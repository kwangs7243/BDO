<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 에다니아 우두머리 주간

## Identity

- slug: "edania-boss-weekly"
- name_ko: "에다니아 우두머리 주간"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: "solo"
- difficulty: null

## Overview

- summary: "에다니아 외부·내부 우두머리를 통틀어 한 주에 하나의 주간 의뢰만 수주·완료할 수 있다."
- purpose: "선택한 에다니아 우두머리를 토벌해 보상 함과 에다나 도전의 증표를 획득한다."

## Requirements

### `edania-boss-weekly.one-boss`

- seed_key: "edania-boss-weekly.one-boss"
- kind: "other"
- requirement_level: "required"
- title: "주간 선택 제한"
- description: "외부·내부 우두머리를 포함해 한 주에 하나의 우두머리 의뢰만 수주 및 완료할 수 있다."
- structured_value:

```json
{
  "scope": "all_edania_bosses",
  "weekly_boss_limit": 1
}
```

### `edania-boss-weekly.inner-stats`

- seed_key: "edania-boss-weekly.inner-stats"
- kind: "stat"
- requirement_level: "required"
- title: "내부 우두머리 최소 능력치"
- description: "2026-08-12 기준 내부 우두머리별 최소 공격력/방어력."
- structured_value:

```json
{
  "마크타난": {
    "ap": 410,
    "dp": 490
  },
  "아그리스": {
    "ap": 405,
    "dp": 485
  },
  "아알": {
    "ap": 420,
    "dp": 505
  },
  "엘리언": {
    "ap": 415,
    "dp": 495
  }
}
```

### `edania-boss-weekly.token-validity`

- seed_key: "edania-boss-weekly.token-validity"
- kind: "other"
- requirement_level: "required"
- title: "도전의 증표 유효시간"
- description: "에다나 도전의 증표는 획득 직후 3시간 동안 유효하며 해당 주 도전 신청 기간에만 사용할 수 있다."
- structured_value:

```json
{
  "use_window": "weekly_challenge_application",
  "valid_hours": 3
}
```

## Steps

### `edania-boss-weekly.choose-and-clear`

- seed_key: "edania-boss-weekly.choose-and-clear"
- phase: "repeat"
- order_no: 1
- title: "우두머리 하나 선택 및 토벌"
- description: "이번 주 외부·내부 우두머리 중 하나의 주간 의뢰를 선택해 완료한다."
- checkable: true

## Schedules

### `edania-boss-weekly.quest-reset`

- seed_key: "edania-boss-weekly.quest-reset"
- rule_type: "quest_reset"
- recurrence_type: "weekly"
- weekday: 3
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "에다니아 주간 우두머리 의뢰 초기화: 목요일 00:00"

## Rewards

### `edania-boss-weekly.challenge-token`

- seed_key: "edania-boss-weekly.challenge-token"
- name: "에다나 도전의 증표"
- reward_type: "weekly_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "획득 직후 3시간 유효"
- order_no: 1

### `edania-boss-weekly.boss-box`

- seed_key: "edania-boss-weekly.boss-box"
- name: "선택한 우두머리 보상 함"
- reward_type: "weekly_reward"
- amount: 1.0
- min_amount: null
- max_amount: null
- unit: "개"
- is_choice: false
- choice_group: null
- recommendation: null
- notes: null
- order_no: 2

## Sections

### `edania-boss-weekly.throne-boundary`

- seed_key: "edania-boss-weekly.throne-boundary"
- section_type: "notes"
- title: "권좌 도전과의 연결"
- order_no: 1

#### body_markdown

증표는 에다나의 권좌 도전 신청에 연결되지만, 권좌 PvP 진행 규칙은 이번 데이터 팩 범위에 포함하지 않는다.

## Related Contents

- None

## Evidence and Sources

### Current evidence

### `edania-boss-weekly.summary::edania-throne-guide`

- evidence_seed_key: "edania-boss-weekly.summary::edania-throne-guide"
- source_id: "edania-throne-guide"
- title: "에다나의 권좌"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=417"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "edania-boss-weekly"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "한 주에 우두머리 하나"
- active: true
- is_active: true

### `edania-boss-weekly.requirement.inner-stats::edania-inner-boss-2026-08-12`

- evidence_seed_key: "edania-boss-weekly.requirement.inner-stats::edania-inner-boss-2026-08-12"
- source_id: "edania-inner-boss-2026-08-12"
- title: "8월 12일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16025"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-08-12"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "edania-boss-weekly.inner-stats"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "내부 4종 최소 능력치"
- active: true
- is_active: true

### `edania-boss-weekly.requirement.one-boss::edania-throne-guide`

- evidence_seed_key: "edania-boss-weekly.requirement.one-boss::edania-throne-guide"
- source_id: "edania-throne-guide"
- title: "에다나의 권좌"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=417"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "edania-boss-weekly.one-boss"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "외부·내부 통합 주 1개"
- active: true
- is_active: true

### `edania-boss-weekly.requirement.token-validity::edania-throne-guide`

- evidence_seed_key: "edania-boss-weekly.requirement.token-validity::edania-throne-guide"
- source_id: "edania-throne-guide"
- title: "에다나의 권좌"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=417"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "edania-boss-weekly.token-validity"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "증표 3시간 및 신청 기간 제한"
- active: true
- is_active: true

### `edania-boss-weekly.reward.boss-box::edania-throne-guide`

- evidence_seed_key: "edania-boss-weekly.reward.boss-box::edania-throne-guide"
- source_id: "edania-throne-guide"
- title: "에다나의 권좌"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=417"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "edania-boss-weekly.boss-box"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "우두머리 보상 함"
- active: true
- is_active: true

### `edania-boss-weekly.reward.challenge-token::edania-throne-guide`

- evidence_seed_key: "edania-boss-weekly.reward.challenge-token::edania-throne-guide"
- source_id: "edania-throne-guide"
- title: "에다나의 권좌"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=417"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "edania-boss-weekly.challenge-token"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "에다나 도전의 증표"
- active: true
- is_active: true

### `edania-boss-weekly.schedule.quest-reset::edania-throne-guide`

- evidence_seed_key: "edania-boss-weekly.schedule.quest-reset::edania-throne-guide"
- source_id: "edania-throne-guide"
- title: "에다나의 권좌"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=417"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "edania-boss-weekly.quest-reset"
- claim_key: "schedule.quest_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "목요일 00:00"
- active: true
- is_active: true

### Historical / inactive evidence

- None
