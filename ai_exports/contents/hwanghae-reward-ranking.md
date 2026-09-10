<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 황해도 보상 및 순위

## Identity

- slug: "hwanghae-reward-ranking"
- name_ko: "황해도 보상 및 순위"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "party"
- difficulty: "varies"

## Overview

- summary: "주간 보상 지급, 도전 난이도 보상, 일일 순위와 주간 정산을 분리한다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `hwanghae-reward-ranking.payout`

- seed_key: "hwanghae-reward-ranking.payout"
- kind: "knowledge"
- requirement_level: "required"
- title: "주간 보상 지급"
- description: "일요일 00:00~00:10 KST 사이 흑정령의 선물함으로 지급된다."
- structured_value:

```json
{
  "destination": "Black Spirit Safe",
  "knowledge_role": "fact",
  "timezone": "Asia/Seoul",
  "weekday": 6,
  "window_end": "00:10",
  "window_start": "00:00"
}
```

### `hwanghae-reward-ranking.challenge-current`

- seed_key: "hwanghae-reward-ranking.challenge-current"
- kind: "knowledge"
- requirement_level: "required"
- title: "도전 보상 최신값"
- description: "2026-06-17 이후 도전 난이도 보상에 새벽의 정수 상자 1개가 포함된다."
- structured_value:

```json
{
  "amount": 1,
  "difficulty": "challenge",
  "effective_from": "2026-06-17",
  "knowledge_role": "fact",
  "reward": "Dawn Essence Box"
}
```

### `hwanghae-reward-ranking.ranking`

- seed_key: "hwanghae-reward-ranking.ranking"
- kind: "knowledge"
- requirement_level: "required"
- title: "순위와 길드 보상"
- description: "일일 순위 갱신과 주간 정산이 별개이며 동일 길드 5인 구성에는 길드 추가 보상 구조가 있다."
- structured_value:

```json
{
  "daily_refresh_time": "00:00",
  "guild_bonus_reward": true,
  "knowledge_role": "fact",
  "same_guild_members_required": 5,
  "weekly_settlement_separate": true
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

### `hwanghae-reward-ranking.existing-routine`

- seed_key: "hwanghae-reward-ranking.existing-routine"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "black-shrine-hwanghae-weekly"
- content_name_ko: "검은 사당 - 황해도 주간 토벌"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/black-shrine-hwanghae-weekly.md"

## Evidence and Sources

### Current evidence

### `hwanghae-reward-ranking.claim.challenge-current::farming-moles-2026-06-17`

- evidence_seed_key: "hwanghae-reward-ranking.claim.challenge-current::farming-moles-2026-06-17"
- source_id: "farming-moles-2026-06-17"
- title: "6월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15751"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "hwanghae-reward-ranking.challenge-current"
- claim_key: "requirement:challenge-current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `hwanghae-reward-ranking.claim.challenge-current::gladius-balance-2026`

- evidence_seed_key: "hwanghae-reward-ranking.claim.challenge-current::gladius-balance-2026"
- source_id: "gladius-balance-2026"
- title: "6월 24일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15783"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-24"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "hwanghae-reward-ranking.challenge-current"
- claim_key: "requirement:challenge-current"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `hwanghae-reward-ranking.claim.payout::black-shrine-hwanghae-guide`

- evidence_seed_key: "hwanghae-reward-ranking.claim.payout::black-shrine-hwanghae-guide"
- source_id: "black-shrine-hwanghae-guide"
- title: "검은 사당 - 황해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=404"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "hwanghae-reward-ranking.payout"
- claim_key: "requirement:payout"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `hwanghae-reward-ranking.claim.ranking::black-shrine-hwanghae-guide`

- evidence_seed_key: "hwanghae-reward-ranking.claim.ranking::black-shrine-hwanghae-guide"
- source_id: "black-shrine-hwanghae-guide"
- title: "검은 사당 - 황해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=404"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "hwanghae-reward-ranking.ranking"
- claim_key: "requirement:ranking"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
