<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 동해도 우두머리 전략

## Identity

- slug: "donghae-boss-strategy"
- name_ko: "동해도 우두머리 전략"
- category: "combat_pve"
- status: "active"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- party_type: "solo"
- difficulty: "varies"

## Overview

- summary: "고재시니 공략은 클래스·장비·패치 시점에 민감한 전략 정보로 저장한다."
- purpose: "현재 규칙, 전략, 이력을 출처와 함께 구분해 확인한다."

## Requirements

### `donghae-boss-strategy.high-calamity`

- seed_key: "donghae-boss-strategy.high-calamity"
- kind: "other"
- requirement_level: "recommended"
- title: "고재시니 준비 전략"
- description: "공격력 컷만으로 성공을 보장하지 않으며 클래스, 생존 장비와 기믹 숙련을 함께 점검한다."
- structured_value:

```json
{
  "class_and_gear_sensitive": true,
  "knowledge_role": "strategy",
  "scope": "community_strategy",
  "source_date": "2026-06-30",
  "universal_clear_claim": false
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

### `donghae-boss-strategy.high-calamity-system`

- seed_key: "donghae-boss-strategy.high-calamity-system"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "donghae-calamity-8-10"
- content_name_ko: "동해도 팔·구·십재시니"
- content_category: "combat_pve"
- note: null
- order_no: 1
- relative_path: "../contents/donghae-calamity-8-10.md"

## Evidence and Sources

### Current evidence

### `donghae-boss-strategy.claim.high-calamity::donghae-c8-strategy-2026-06-30`

- evidence_seed_key: "donghae-boss-strategy.claim.high-calamity::donghae-c8-strategy-2026-06-30"
- source_id: "donghae-c8-strategy-2026-06-30"
- title: "C8 Black Shrine tips - post high-Calamity discussion"
- url: "https://www.reddit.com/r/blackdesertonline/comments/1ujgdoc/c8_black_shrine_tips/"
- publisher: "Reddit / r/blackdesertonline"
- source_type: "community_discussion"
- published_at: "2026-06-30"
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "global"
- entity_type: "content_requirement"
- entity_id: "donghae-boss-strategy.high-calamity"
- claim_key: "requirement:high-calamity"
- verification_status: "needs_review"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
