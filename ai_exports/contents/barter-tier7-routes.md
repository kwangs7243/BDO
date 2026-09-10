<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 7단계 물물교환 교역로

## Identity

- slug: "barter-tier7-routes"
- name_ko: "7단계 물물교환 교역로"
- category: "ocean_barter"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "6단계 교역품을 7단계 교역품으로 바꾸는 공식 거점과 품목."
- purpose: "7단계 교역의 공식 도착 거점과 품목을 참조한다."

## Requirements

- None

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `barter-tier7-routes.routes`

- seed_key: "barter-tier7-routes.routes"
- section_type: "overview"
- title: "6→7단계 공식 교역 거점과 품목"
- order_no: 1

#### body_markdown

| 영지(거점) | 7단계 교역품 |
|---|---|
| 발레노스(올비아 해안) | 최고급 하이델산 포도주, 금빛 밀가루 포대, 유기농 벌꿀 상자, 발레노스 전통 닻 장식 |
| 칼페온(에페리아 초소) | 황금 독수리 브로치, 칼페온 기사단의 전투 교본, 칼페온 황금 장식 촛대, 칼페온 장인의 진주 목걸이 |
| 메디아(소산 주둔지 선착장) | 소산 군수품 상자, 돌꼬리 당근 건강식 상자, 오마르 용암 가루, 타리프의 마법 항아리 |
| 에다니아(성전 해안 정찰지) | 루살카 가시꽃다발, 단단한 카프라스 목재, 하킨자 최고급 향수, 에다나 권좌의 기록서 |
| 발레노스 군도(일리야 섬) | 장인의 조개 껍질 목걸이, 발레노스 항해사의 망원경, 발레노스 고래 조각상, 발레노스 소금꽃 |
| 발레노스 군도(레마 섬) | 발레노스 별빛 소금, 발레노스 유물 파편, 발레노스 무지개 산호, 무지개빛 해원석 조각 |

## Related Contents

### `barter-tier7-routes.relation.current-system`

- seed_key: "barter-tier7-routes.relation.current-system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "barter-current-system"
- content_name_ko: "현행 물물교환 시스템"
- content_category: "ocean_barter"
- note: "현행 물물교환의 6→7단계 교역"
- order_no: 1
- relative_path: "../contents/barter-current-system.md"
### `barter-tier7-routes.relation.tier6`

- seed_key: "barter-tier7-routes.relation.tier6"
- direction: "outgoing"
- relation_type: "prerequisite"
- content_slug: "barter-tier6-routes"
- content_name_ko: "6단계 물물교환 교역로"
- content_category: "ocean_barter"
- note: "6단계 교역품이 입력으로 필요하다"
- order_no: 2
- relative_path: "../contents/barter-tier6-routes.md"
### `barter-tier6-routes.relation.tier7`

- seed_key: "barter-tier6-routes.relation.tier7"
- direction: "incoming"
- relation_type: "unlocks"
- content_slug: "barter-tier6-routes"
- content_name_ko: "6단계 물물교환 교역로"
- content_category: "ocean_barter"
- note: "6단계 교역품은 7단계 교역의 입력이 된다"
- order_no: 2
- relative_path: "../contents/barter-tier6-routes.md"
### `barter-current-system.relation.tier7`

- seed_key: "barter-current-system.relation.tier7"
- direction: "incoming"
- relation_type: "related"
- content_slug: "barter-current-system"
- content_name_ko: "현행 물물교환 시스템"
- content_category: "ocean_barter"
- note: "6→7단계 교역로"
- order_no: 3
- relative_path: "../contents/barter-current-system.md"
### `barter-route-strategy.relation.tier7`

- seed_key: "barter-route-strategy.relation.tier7"
- direction: "incoming"
- relation_type: "related"
- content_slug: "barter-route-strategy"
- content_name_ko: "물물교환 동선 전략"
- content_category: "ocean_barter"
- note: "7단계 교역 동선 참고"
- order_no: 3
- relative_path: "../contents/barter-route-strategy.md"
### `barter-onboarding-strategy.tier7`

- seed_key: "barter-onboarding-strategy.tier7"
- direction: "incoming"
- relation_type: "related"
- content_slug: "barter-onboarding-strategy"
- content_name_ko: "물물교환 입문 운영 전략"
- content_category: "ocean_barter"
- note: "7단계 공식 항로"
- order_no: 5
- relative_path: "../contents/barter-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `barter-tier7-routes.evidence.routes::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-tier7-routes.evidence.routes::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "barter-tier7-routes.routes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "| 영지(거점) | 7단계 교역품 |\n|---|---|\n| 발레노스(올비아 해안) | 최고급 하이델산 포도주, 금빛 밀가루 포대, 유기농 벌꿀 상자, 발레노스 전통 닻 장식 |\n| 칼페온(에페리아 초소) | 황금 독수리 브로치, 칼페온 기사단의 전투 교본, 칼페온 황금 장식 촛대, 칼페온 장인의 진주 목걸이 |\n| 메디아(소산 주둔지 선착장) | 소산 군수품 상자, 돌꼬리 당근 건강식 상자, 오마르 용암 가루, 타리프의 마법 항아리 |\n| 에다니아(성전 해안 정찰지) | 루살카 가시꽃다발, 단단한 카프라스 목재, 하킨자 최고급 향수, 에다나 권좌의 기록서 |\n| 발레노스 군도(일리야 섬) | 장인의 조개 껍질 목걸이, 발레노스 항해사의 망원경, 발레노스 고래 조각상, 발레노스 소금꽃 |\n| 발레노스 군도(레마 섬) | 발레노스 별빛 소금, 발레노스 유물 파편, 발레노스 무지개 산호, 무지개빛 해원석 조각 |"
- active: true
- is_active: true

### Historical / inactive evidence

- None
