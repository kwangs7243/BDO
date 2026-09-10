<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 물물교환 동선 전략

## Identity

- slug: "barter-route-strategy"
- name_ko: "물물교환 동선 전략"
- category: "ocean_barter"
- status: "active"
- verification_status: "community_consensus"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "공식 규칙과 분리해 관리하는 날짜 기반 커뮤니티 거리 측정 및 추천."
- purpose: "변동 가능한 실전 동선을 공식 규칙으로 오인하지 않도록 출처와 측정 시점을 함께 기록한다."

## Requirements

- None

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `barter-route-strategy.distance-2026-05-31`

- seed_key: "barter-route-strategy.distance-2026-05-31"
- section_type: "strategy"
- title: "2026-05-31 거리 측정 기반 추천"
- order_no: 1

#### body_markdown

2026-05-31 작성자의 계산 기준에서는 그란디하→에페리아와 그란디하→일리야가 안정적으로 짧은 루트로 평가됐다. 인도 구간 활용과 연안/대양 거리 환산 가정에 따라 결과가 달라질 수 있는 커뮤니티 측정이며 공식 최적 경로가 아니다.

## Related Contents

### `barter-route-strategy.relation.current-system`

- seed_key: "barter-route-strategy.relation.current-system"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "barter-current-system"
- content_name_ko: "현행 물물교환 시스템"
- content_category: "ocean_barter"
- note: "공식 규칙과 분리된 실전 동선 참고"
- order_no: 1
- relative_path: "../contents/barter-current-system.md"
### `barter-route-strategy.relation.tier6`

- seed_key: "barter-route-strategy.relation.tier6"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "barter-tier6-routes"
- content_name_ko: "6단계 물물교환 교역로"
- content_category: "ocean_barter"
- note: "6단계 교역 동선 참고"
- order_no: 2
- relative_path: "../contents/barter-tier6-routes.md"
### `barter-route-strategy.relation.tier7`

- seed_key: "barter-route-strategy.relation.tier7"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "barter-tier7-routes"
- content_name_ko: "7단계 물물교환 교역로"
- content_category: "ocean_barter"
- note: "7단계 교역 동선 참고"
- order_no: 3
- relative_path: "../contents/barter-tier7-routes.md"
### `barter-onboarding-strategy.advanced-route`

- seed_key: "barter-onboarding-strategy.advanced-route"
- direction: "incoming"
- relation_type: "related"
- content_slug: "barter-onboarding-strategy"
- content_name_ko: "물물교환 입문 운영 전략"
- content_category: "ocean_barter"
- note: "고급 거리 측정·항로 참고"
- order_no: 3
- relative_path: "../contents/barter-onboarding-strategy.md"
### `barter-current-system.relation.strategy`

- seed_key: "barter-current-system.relation.strategy"
- direction: "incoming"
- relation_type: "related"
- content_slug: "barter-current-system"
- content_name_ko: "현행 물물교환 시스템"
- content_category: "ocean_barter"
- note: "공식 규칙과 분리된 커뮤니티 동선 측정"
- order_no: 4
- relative_path: "../contents/barter-current-system.md"

## Evidence and Sources

### Current evidence

### `barter-route-strategy.evidence.distance-2026-05-31::barter-route-distance-community-2026-05-31`

- evidence_seed_key: "barter-route-strategy.evidence.distance-2026-05-31::barter-route-distance-community-2026-05-31"
- source_id: "barter-route-distance-community-2026-05-31"
- title: "6-7단 교역에 대한 거리 정리"
- url: "https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_forumListType=3&_topicNo=152574"
- publisher: "omote23-KR"
- source_type: "community_guide"
- published_at: "2026-05-31"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "barter-route-strategy.distance-2026-05-31"
- claim_key: "body"
- verification_status: "community_consensus"
- last_verified_at: "2026-09-03"
- evidence_note: "2026-05-31 작성자의 계산 기준에서는 그란디하→에페리아와 그란디하→일리야가 안정적으로 짧은 루트로 평가됐다. 인도 구간 활용과 연안/대양 거리 환산 가정에 따라 결과가 달라질 수 있는 커뮤니티 측정이며 공식 최적 경로가 아니다."
- active: true
- is_active: true

### Historical / inactive evidence

- None
