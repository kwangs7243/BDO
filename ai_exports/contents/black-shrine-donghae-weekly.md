<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 검은 사당 - 동해도 주간 토벌

## Identity

- slug: "black-shrine-donghae-weekly"
- name_ko: "검은 사당 - 동해도 주간 토벌"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: "solo"
- difficulty: null

## Overview

- summary: "가문당 주 5회 성공 기록을 남기는 개인 토벌. 일요일 00:00 주간 초기화·보상 지급과 매일 00:00 순위 갱신을 구분한다."
- purpose: "동해도 우두머리 토벌 기록과 순위에 따른 주간 보상을 획득한다."

## Requirements

### `black-shrine-donghae-weekly.attempts`

- seed_key: "black-shrine-donghae-weekly.attempts"
- kind: "other"
- requirement_level: "required"
- title: "주간 토벌 횟수"
- description: "가문당 주 5회이며 성공할 때만 횟수가 차감된다."
- structured_value:

```json
{
  "consume_on": "success",
  "scope": "family",
  "weekly_attempts": 5
}
```

### `black-shrine-donghae-weekly.retry`

- seed_key: "black-shrine-donghae-weekly.retry"
- kind: "other"
- requirement_level: "required"
- title: "재도전"
- description: "이미 완료한 동일 우두머리와 동일 난이도는 주간 횟수 차감 뒤에도 재도전할 수 있다."
- structured_value:

```json
{
  "completed_same_boss_difficulty_retry": true
}
```

## Steps

### `black-shrine-donghae-weekly.clear`

- seed_key: "black-shrine-donghae-weekly.clear"
- phase: "repeat"
- order_no: 1
- title: "주간 토벌 기록"
- description: "원하는 우두머리와 난이도에 도전해 성공 기록을 남긴다."
- checkable: true

### `black-shrine-donghae-weekly.reward-check`

- seed_key: "black-shrine-donghae-weekly.reward-check"
- phase: "reward"
- order_no: 2
- title: "주간 보상 확인"
- description: "일요일 00:00 이후 흑정령의 선물함에서 자동 지급된 보상을 확인한다."
- checkable: false

## Schedules

### `black-shrine-donghae-weekly.attempt-reset`

- seed_key: "black-shrine-donghae-weekly.attempt-reset"
- rule_type: "attempt_reset"
- recurrence_type: "weekly"
- weekday: 6
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "동해도 주간 토벌 횟수 초기화: 일요일 00:00"

### `black-shrine-donghae-weekly.rank-refresh`

- seed_key: "black-shrine-donghae-weekly.rank-refresh"
- rule_type: "rank_refresh"
- recurrence_type: "daily"
- weekday: null
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "토벌 순위 갱신: 매일 00:00"

### `black-shrine-donghae-weekly.reward-payout`

- seed_key: "black-shrine-donghae-weekly.reward-payout"
- rule_type: "reward_payout"
- recurrence_type: "weekly"
- weekday: 6
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "기록·순위 보상 자동 지급: 일요일 00:00"

## Rewards

### `black-shrine-donghae-weekly.ranking-reward`

- seed_key: "black-shrine-donghae-weekly.ranking-reward"
- name: "토벌 기록·순위 주간 보상"
- reward_type: "weekly_reward"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "일요일 00:00 흑정령의 선물함 자동 지급, 사라지지 않고 누적"
- order_no: 1

## Sections

### `black-shrine-donghae-weekly.schedule-separation`

- seed_key: "black-shrine-donghae-weekly.schedule-separation"
- section_type: "common_mistakes"
- title: "세 일정의 구분"
- order_no: 1

#### body_markdown

주간 토벌 횟수 초기화와 주간 보상 지급은 일요일 00:00이며, 순위 갱신은 매일 00:00이다. 일반 주간 의뢰의 목요일 초기화를 적용하지 않는다.

## Related Contents

### `black-shrine-donghae-current-system.existing-routine`

- seed_key: "black-shrine-donghae-current-system.existing-routine"
- direction: "incoming"
- relation_type: "related"
- content_slug: "black-shrine-donghae-current-system"
- content_name_ko: "검은사당 동해도 현재 시스템"
- content_category: "combat_pve"
- note: "기존 V1.6E 주간 루틴을 재사용한다."
- order_no: 1
- relative_path: "../contents/black-shrine-donghae-current-system.md"
### `donghae-reward-ranking.existing-routine`

- seed_key: "donghae-reward-ranking.existing-routine"
- direction: "incoming"
- relation_type: "related"
- content_slug: "donghae-reward-ranking"
- content_name_ko: "동해도 보상 및 순위"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/donghae-reward-ranking.md"
### `content-unlock-foundation.black-shrine`

- seed_key: "content-unlock-foundation.black-shrine"
- direction: "incoming"
- relation_type: "related"
- content_slug: "content-unlock-foundation"
- content_name_ko: "콘텐츠 해금 기반"
- content_category: "progression"
- note: null
- order_no: 3
- relative_path: "../contents/content-unlock-foundation.md"
### `main-quest-morning-land.black-shrine`

- seed_key: "main-quest-morning-land.black-shrine"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "main-quest-morning-land"
- content_name_ko: "아침의 나라 메인 의뢰"
- content_category: "progression"
- note: null
- order_no: 3
- relative_path: "../contents/main-quest-morning-land.md"

## Evidence and Sources

### Current evidence

### `black-shrine-donghae-weekly.summary::barter-improvement-2026-04-15`

- evidence_seed_key: "black-shrine-donghae-weekly.summary::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "black-shrine-donghae-weekly"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주 5회·일요일 주기·자동 누적 보상"
- active: true
- is_active: true

### `black-shrine-donghae-weekly.summary::black-shrine-donghae-guide`

- evidence_seed_key: "black-shrine-donghae-weekly.summary::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "black-shrine-donghae-weekly"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "주 5회·일요일 주기·자동 누적 보상"
- active: true
- is_active: true

### `black-shrine-donghae-weekly.requirement.attempts::black-shrine-donghae-guide`

- evidence_seed_key: "black-shrine-donghae-weekly.requirement.attempts::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "black-shrine-donghae-weekly.attempts"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "가문당 주 5회, 성공 시 차감"
- active: true
- is_active: true

### `black-shrine-donghae-weekly.requirement.retry::black-shrine-donghae-guide`

- evidence_seed_key: "black-shrine-donghae-weekly.requirement.retry::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "black-shrine-donghae-weekly.retry"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "완료한 동일 우두머리·난이도 재도전"
- active: true
- is_active: true

### `black-shrine-donghae-weekly.reward.ranking::barter-improvement-2026-04-15`

- evidence_seed_key: "black-shrine-donghae-weekly.reward.ranking::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "black-shrine-donghae-weekly.ranking-reward"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일요일 자동 지급 및 선물함 누적"
- active: true
- is_active: true

### `black-shrine-donghae-weekly.reward.ranking::black-shrine-donghae-guide`

- evidence_seed_key: "black-shrine-donghae-weekly.reward.ranking::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "black-shrine-donghae-weekly.ranking-reward"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일요일 자동 지급 및 선물함 누적"
- active: true
- is_active: true

### `black-shrine-donghae-weekly.schedule.attempt-reset::black-shrine-donghae-guide`

- evidence_seed_key: "black-shrine-donghae-weekly.schedule.attempt-reset::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "black-shrine-donghae-weekly.attempt-reset"
- claim_key: "schedule.attempt_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일요일 00:00 횟수 초기화"
- active: true
- is_active: true

### `black-shrine-donghae-weekly.schedule.rank-refresh::black-shrine-donghae-guide`

- evidence_seed_key: "black-shrine-donghae-weekly.schedule.rank-refresh::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "black-shrine-donghae-weekly.rank-refresh"
- claim_key: "schedule.rank_refresh"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "매일 00:00 순위 갱신"
- active: true
- is_active: true

### `black-shrine-donghae-weekly.schedule.reward-payout::barter-improvement-2026-04-15`

- evidence_seed_key: "black-shrine-donghae-weekly.schedule.reward-payout::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "black-shrine-donghae-weekly.reward-payout"
- claim_key: "schedule.reward_payout"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일요일 00:00 자동 지급"
- active: true
- is_active: true

### `black-shrine-donghae-weekly.schedule.reward-payout::black-shrine-donghae-guide`

- evidence_seed_key: "black-shrine-donghae-weekly.schedule.reward-payout::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "black-shrine-donghae-weekly.reward-payout"
- claim_key: "schedule.reward_payout"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일요일 00:00 자동 지급"
- active: true
- is_active: true

### Historical / inactive evidence

### `black-shrine-donghae-weekly.history.manual-expiry::black-shrine-donghae-guide`

- evidence_seed_key: "black-shrine-donghae-weekly.history.manual-expiry::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "black-shrine-donghae-weekly.ranking-reward"
- claim_key: "historical_delivery"
- verification_status: "superseded"
- last_verified_at: "2026-09-03"
- evidence_note: "과거 직접 수령·미수령 소멸 안내는 2026-04-15 변경으로 대체됨"
- active: false
- is_active: false
