<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 동해도 보상 및 순위

## Identity

- slug: "donghae-reward-ranking"
- name_ko: "동해도 보상 및 순위"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "varies"

## Overview

- summary: "주간 보상, 난이도별 개인 보상, 우두머리·난이도·클래스별 순위를 서로 구분한다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `donghae-reward-ranking.reward-update`

- seed_key: "donghae-reward-ranking.reward-update"
- kind: "knowledge"
- requirement_level: "required"
- title: "2026-06-17 보상 개선"
- description: "2~7재시니 보상에 새벽의 정수와 금괴 보상이 개선되었다."
- structured_value:

```json
{
  "calamity_range": [
    2,
    7
  ],
  "effective_from": "2026-06-17",
  "knowledge_role": "fact",
  "reward_categories": [
    "Dawn Essence",
    "Gold Bars"
  ]
}
```

### `donghae-reward-ranking.ranking`

- seed_key: "donghae-reward-ranking.ranking"
- kind: "knowledge"
- requirement_level: "required"
- title: "순위 집계"
- description: "순위는 우두머리·난이도·클래스별로 집계되며 일일 00:00 갱신과 주간 정산은 별개다."
- structured_value:

```json
{
  "daily_refresh_time": "00:00",
  "dimensions": [
    "boss",
    "calamity",
    "class"
  ],
  "knowledge_role": "fact",
  "timezone": "Asia/Seoul",
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

### `donghae-reward-ranking.existing-routine`

- seed_key: "donghae-reward-ranking.existing-routine"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "black-shrine-donghae-weekly"
- content_name_ko: "검은 사당 - 동해도 주간 토벌"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/black-shrine-donghae-weekly.md"

## Evidence and Sources

### Current evidence

### `donghae-reward-ranking.claim.ranking::black-shrine-donghae-guide`

- evidence_seed_key: "donghae-reward-ranking.claim.ranking::black-shrine-donghae-guide"
- source_id: "black-shrine-donghae-guide"
- title: "검은 사당 - 동해도편"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=315"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "donghae-reward-ranking.ranking"
- claim_key: "requirement:ranking"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### `donghae-reward-ranking.claim.reward-update::farming-moles-2026-06-17`

- evidence_seed_key: "donghae-reward-ranking.claim.reward-update::farming-moles-2026-06-17"
- source_id: "farming-moles-2026-06-17"
- title: "6월 17일(수) 업데이트 안내"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15751"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-06-17"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "donghae-reward-ranking.reward-update"
- claim_key: "requirement:reward-update"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
