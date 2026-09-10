<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 검은 사당 - 황해도 주간 토벌

## Identity

- slug: "black-shrine-hwanghae-weekly"
- name_ko: "검은 사당 - 황해도 주간 토벌"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: "party"
- difficulty: null

## Overview

- summary: "5인 협동 토벌. 가문 통합 주 5회이며 실패 재도전·횟수 소진 뒤 도움 입장과 일요일 보상 정산을 분리한다."
- purpose: "황해도 우두머리 토벌 완료 및 순위 보상을 획득한다."

## Requirements

### `black-shrine-hwanghae-weekly.party`

- seed_key: "black-shrine-hwanghae-weekly.party"
- kind: "party"
- requirement_level: "required"
- title: "파티 구성"
- description: "5인 파티로 진행한다."
- structured_value:

```json
{
  "party_size": 5
}
```

### `black-shrine-hwanghae-weekly.attempts`

- seed_key: "black-shrine-hwanghae-weekly.attempts"
- kind: "other"
- requirement_level: "required"
- title: "주간 토벌 횟수"
- description: "가문 통합 주 5회이며 우두머리·난이도별 성공 시 횟수가 차감된다."
- structured_value:

```json
{
  "consume_on": "success",
  "count_by": [
    "boss",
    "difficulty"
  ],
  "scope": "family",
  "weekly_attempts": 5
}
```

### `black-shrine-hwanghae-weekly.help-entry`

- seed_key: "black-shrine-hwanghae-weekly.help-entry"
- kind: "other"
- requirement_level: "optional"
- title: "도움 입장"
- description: "횟수를 모두 소진해도 도움 입장은 가능하지만 이벤트 의뢰·길드 임무 등의 토벌 카운트에는 반영되지 않는다."
- structured_value:

```json
{
  "counting_after_exhaustion": false,
  "entry_after_exhaustion": true
}
```

## Steps

### `black-shrine-hwanghae-weekly.clear`

- seed_key: "black-shrine-hwanghae-weekly.clear"
- phase: "repeat"
- order_no: 1
- title: "주간 협동 토벌"
- description: "파티로 우두머리와 난이도를 선택해 토벌한다. 실패한 동일 조합은 제한 없이 재도전할 수 있다."
- checkable: true

## Schedules

### `black-shrine-hwanghae-weekly.attempt-reset`

- seed_key: "black-shrine-hwanghae-weekly.attempt-reset"
- rule_type: "attempt_reset"
- recurrence_type: "weekly"
- weekday: 6
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "황해도 주간 토벌 횟수 초기화: 일요일 00:00"

### `black-shrine-hwanghae-weekly.reward-payout`

- seed_key: "black-shrine-hwanghae-weekly.reward-payout"
- rule_type: "reward_payout"
- recurrence_type: "weekly"
- weekday: 6
- time_local: "00:00"
- fixed_datetime: null
- timezone: "Asia/Seoul"
- notes: "토벌 보상 산정·지급: 일요일 00:00~00:10"

## Rewards

### `black-shrine-hwanghae-weekly.loot`

- seed_key: "black-shrine-hwanghae-weekly.loot"
- name: "황해도 주간 토벌 전리품"
- reward_type: "weekly_reward"
- amount: null
- min_amount: null
- max_amount: null
- unit: null
- is_choice: false
- choice_group: null
- recommendation: null
- notes: "일요일 00:00~00:10 산정·지급, 흑정령의 선물함에서 누적"
- order_no: 1

## Sections

### `black-shrine-hwanghae-weekly.help-warning`

- seed_key: "black-shrine-hwanghae-weekly.help-warning"
- section_type: "common_mistakes"
- title: "횟수 소진 뒤 도움 입장"
- order_no: 1

#### body_markdown

입장은 가능하지만 토벌 카운트가 필요한 이벤트 의뢰와 길드 임무에는 반영되지 않는다.

## Related Contents

### `black-shrine-hwanghae-current-system.existing-routine`

- seed_key: "black-shrine-hwanghae-current-system.existing-routine"
- direction: "incoming"
- relation_type: "related"
- content_slug: "black-shrine-hwanghae-current-system"
- content_name_ko: "검은사당 황해도 현재 시스템"
- content_category: "combat_pve"
- note: "기존 V1.6E 주간 루틴을 재사용한다."
- order_no: 1
- relative_path: "../contents/black-shrine-hwanghae-current-system.md"
### `hwanghae-reward-ranking.existing-routine`

- seed_key: "hwanghae-reward-ranking.existing-routine"
- direction: "incoming"
- relation_type: "related"
- content_slug: "hwanghae-reward-ranking"
- content_name_ko: "황해도 보상 및 순위"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/hwanghae-reward-ranking.md"

## Evidence and Sources

### Current evidence

### `black-shrine-hwanghae-weekly.summary::black-shrine-hwanghae-guide`

- evidence_seed_key: "black-shrine-hwanghae-weekly.summary::black-shrine-hwanghae-guide"
- source_id: "black-shrine-hwanghae-guide"
- title: "검은 사당 - 황해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=404"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "black-shrine-hwanghae-weekly"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "5인·주 5회·도움 입장"
- active: true
- is_active: true

### `black-shrine-hwanghae-weekly.requirement.attempts::black-shrine-hwanghae-guide`

- evidence_seed_key: "black-shrine-hwanghae-weekly.requirement.attempts::black-shrine-hwanghae-guide"
- source_id: "black-shrine-hwanghae-guide"
- title: "검은 사당 - 황해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=404"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "black-shrine-hwanghae-weekly.attempts"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "현재 주간 5회 및 실패 재도전"
- active: true
- is_active: true

### `black-shrine-hwanghae-weekly.requirement.help-entry::black-shrine-hwanghae-guide`

- evidence_seed_key: "black-shrine-hwanghae-weekly.requirement.help-entry::black-shrine-hwanghae-guide"
- source_id: "black-shrine-hwanghae-guide"
- title: "검은 사당 - 황해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=404"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "black-shrine-hwanghae-weekly.help-entry"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "횟수 소진 뒤 도움 입장과 카운트 제외"
- active: true
- is_active: true

### `black-shrine-hwanghae-weekly.requirement.party::black-shrine-hwanghae-guide`

- evidence_seed_key: "black-shrine-hwanghae-weekly.requirement.party::black-shrine-hwanghae-guide"
- source_id: "black-shrine-hwanghae-guide"
- title: "검은 사당 - 황해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=404"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "black-shrine-hwanghae-weekly.party"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "5인 파티"
- active: true
- is_active: true

### `black-shrine-hwanghae-weekly.reward.loot::black-shrine-hwanghae-guide`

- evidence_seed_key: "black-shrine-hwanghae-weekly.reward.loot::black-shrine-hwanghae-guide"
- source_id: "black-shrine-hwanghae-guide"
- title: "검은 사당 - 황해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=404"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "reward"
- entity_id: "black-shrine-hwanghae-weekly.loot"
- claim_key: "reward"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "흑정령의 선물함 지급 및 누적"
- active: true
- is_active: true

### `black-shrine-hwanghae-weekly.schedule.attempt-reset::black-shrine-hwanghae-guide`

- evidence_seed_key: "black-shrine-hwanghae-weekly.schedule.attempt-reset::black-shrine-hwanghae-guide"
- source_id: "black-shrine-hwanghae-guide"
- title: "검은 사당 - 황해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=404"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "black-shrine-hwanghae-weekly.attempt-reset"
- claim_key: "schedule.attempt_reset"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일요일 초기화"
- active: true
- is_active: true

### `black-shrine-hwanghae-weekly.schedule.reward-payout::black-shrine-hwanghae-guide`

- evidence_seed_key: "black-shrine-hwanghae-weekly.schedule.reward-payout::black-shrine-hwanghae-guide"
- source_id: "black-shrine-hwanghae-guide"
- title: "검은 사당 - 황해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=404"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "schedule_rule"
- entity_id: "black-shrine-hwanghae-weekly.reward-payout"
- claim_key: "schedule.reward_payout"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "일요일 00:00~00:10 산정·지급"
- active: true
- is_active: true

### Historical / inactive evidence

- None
