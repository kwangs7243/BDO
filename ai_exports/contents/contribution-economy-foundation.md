<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 공헌도 경제 기반

## Identity

- slug: "contribution-economy-foundation"
- name_ko: "공헌도 경제 기반"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "공헌도는 가문이 공유하며 지역 제한 없이 거점 투자·집 구매·아이템 대여에 사용하는 대부분 회수 가능한 자원이다."
- purpose: "생활 경제를 여는 공헌도의 사용과 회수 규칙을 설명한다."

## Requirements

### `contribution-economy-foundation.uses`

- seed_key: "contribution-economy-foundation.uses"
- kind: "other"
- requirement_level: "required"
- title: "공헌도 사용"
- description: "가문 공유 공헌도의 주요 사용처다."
- structured_value:

```json
{
  "family_shared": true,
  "mostly_recoverable": true,
  "region_restricted": false,
  "uses": [
    "node_investment",
    "house_purchase",
    "contribution_item_rental"
  ]
}
```

### `contribution-economy-foundation.node-recovery`

- seed_key: "contribution-economy-foundation.node-recovery"
- kind: "other"
- requirement_level: "required"
- title: "거점 투자 회수"
- description: "의존 거점이 있으면 연결 말단부터 회수해야 한다."
- structured_value:

```json
{
  "blocked_when_dependent_nodes_disconnect": true,
  "recover_leaf_nodes_first": true,
  "world_map_recovery": true
}
```

### `contribution-economy-foundation.house-sale`

- seed_key: "contribution-economy-foundation.house-sale"
- kind: "other"
- requirement_level: "required"
- title: "집 매각"
- description: "집 매각 시 공헌도와 기타 비용의 반환 범위를 구분한다."
- structured_value:

```json
{
  "contribution_returned": true,
  "conversion_silver_or_cost_returned": false,
  "installed_furniture_destination": "town_storage"
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

### `contribution-economy-foundation.nodes`

- seed_key: "contribution-economy-foundation.nodes"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "node-network-current-system"
- content_name_ko: "거점 네트워크 현재 시스템"
- content_category: "life"
- note: "공헌도 투자가 거점 네트워크를 연다."
- order_no: 1
- relative_path: "../contents/node-network-current-system.md"
### `contribution-economy-foundation.housing`

- seed_key: "contribution-economy-foundation.housing"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "housing-life-economy"
- content_name_ko: "집과 생활 경제"
- content_category: "life"
- note: "공헌도로 집을 구매한다."
- order_no: 2
- relative_path: "../contents/housing-life-economy.md"
### `housing-life-economy.contribution`

- seed_key: "housing-life-economy.contribution"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "housing-life-economy"
- content_name_ko: "집과 생활 경제"
- content_category: "life"
- note: "집 구매에 공헌도를 사용한다."
- order_no: 1
- relative_path: "../contents/housing-life-economy.md"
### `account-progression-foundation.contribution`

- seed_key: "account-progression-foundation.contribution"
- direction: "incoming"
- relation_type: "related"
- content_slug: "account-progression-foundation"
- content_name_ko: "가문 성장 기반"
- content_category: "progression"
- note: null
- order_no: 2
- relative_path: "../contents/account-progression-foundation.md"

## Evidence and Sources

### Current evidence

### `contribution-economy-foundation.claim.current::contribution-guide`

- evidence_seed_key: "contribution-economy-foundation.claim.current::contribution-guide"
- source_id: "contribution-guide"
- title: "공헌도"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=24"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-04T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "contribution-economy-foundation"
- claim_key: "requirements:contribution-economy-foundation"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
