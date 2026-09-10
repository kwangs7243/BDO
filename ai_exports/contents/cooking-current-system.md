<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 요리 현재 시스템

## Identity

- slug: "cooking-current-system"
- name_ko: "요리 현재 시스템"
- category: "life"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "주거지에 요리 도구를 설치하고 재료를 넣어 요리하며, 실제 요리 시간은 1회당 최소 1초다."
- purpose: "현재 요리의 시작 조건과 시간 하한을 설명한다."

## Requirements

### `cooking-current-system.setup`

- seed_key: "cooking-current-system.setup"
- kind: "other"
- requirement_level: "required"
- title: "요리 시작 조건"
- description: "요리 시작 조건의 현재 규칙이다."
- structured_value:

```json
{
  "input": "ingredients",
  "installed_tool": "cooking_utensil",
  "location": "residence"
}
```

### `cooking-current-system.minimum-time`

- seed_key: "cooking-current-system.minimum-time"
- kind: "stat"
- requirement_level: "required"
- title: "1회 요리 시간 하한"
- description: "1회 요리 시간 하한의 현재 규칙이다."
- structured_value:

```json
{
  "seconds": 1
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

### `cooking-current-system.common-gear`

- seed_key: "cooking-current-system.common-gear"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "life-common-gear"
- content_name_ko: "생활 통합 장비"
- content_category: "life"
- note: "생활 공통 장비와 생활 숙련도 기반을 사용한다."
- order_no: 1
- relative_path: "../contents/life-common-gear.md"
### `cooking-onboarding-strategy.current-system`

- seed_key: "cooking-onboarding-strategy.current-system"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "cooking-onboarding-strategy"
- content_name_ko: "요리 입문 전략"
- content_category: "life"
- note: null
- order_no: 1
- relative_path: "../contents/cooking-onboarding-strategy.md"
### `group-hunting-whale-khalk.cooking`

- seed_key: "group-hunting-whale-khalk.cooking"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "group-hunting-whale-khalk"
- content_name_ko: "대왕 고래와 도망자 칼크 파티 수렵"
- content_category: "life"
- note: "수렵 고기는 요리 재료 흐름과 연결된다."
- order_no: 1
- relative_path: "../contents/group-hunting-whale-khalk.md"
### `worker-stamina-auto-recovery.cooking`

- seed_key: "worker-stamina-auto-recovery.cooking"
- direction: "incoming"
- relation_type: "related"
- content_slug: "worker-stamina-auto-recovery"
- content_name_ko: "일꾼 행동력과 자동 회복"
- content_category: "life"
- note: "요리로 만드는 회복 음식과 연결된다."
- order_no: 1
- relative_path: "../contents/worker-stamina-auto-recovery.md"
### `housing-life-economy.cooking`

- seed_key: "housing-life-economy.cooking"
- direction: "incoming"
- relation_type: "related"
- content_slug: "housing-life-economy"
- content_name_ko: "집과 생활 경제"
- content_category: "life"
- note: "주거지는 요리 도구 설치 장소다."
- order_no: 2
- relative_path: "../contents/housing-life-economy.md"
### `production-node-current-system.cooking`

- seed_key: "production-node-current-system.cooking"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "production-node-current-system"
- content_name_ko: "생산 거점 현재 시스템"
- content_category: "life"
- note: "생산 거점 재료는 요리 콘텐츠로 이어진다."
- order_no: 3
- relative_path: "../contents/production-node-current-system.md"

## Evidence and Sources

### Current evidence

### `cooking-current-system.claim.minimum-time::cooking-guide`

- evidence_seed_key: "cooking-current-system.claim.minimum-time::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "cooking-current-system"
- claim_key: "requirement:cooking-current-system.minimum-time"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### `cooking-current-system.claim.setup::cooking-guide`

- evidence_seed_key: "cooking-current-system.claim.setup::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "cooking-current-system"
- claim_key: "requirement:cooking-current-system.setup"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### `cooking-current-system.claim.summary::cooking-guide`

- evidence_seed_key: "cooking-current-system.claim.summary::cooking-guide"
- source_id: "cooking-guide"
- title: "요리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: "2026-09-11T00:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "cooking-current-system"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
