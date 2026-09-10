<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 6단계 물물교환 교역로

## Identity

- slug: "barter-tier6-routes"
- name_ko: "6단계 물물교환 교역로"
- category: "ocean_barter"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "5단계 교역품을 6단계 교역품으로 바꾸는 공식 대륙간 교역 거점과 품목."
- purpose: "6단계 교역의 공식 출발 거점과 품목을 참조한다."

## Requirements

- None

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

### `barter-tier6-routes.routes`

- seed_key: "barter-tier6-routes.routes"
- section_type: "overview"
- title: "5→6단계 공식 교역 거점과 품목"
- order_no: 1

#### body_markdown

| 영지(거점) | 6단계 교역품 |
|---|---|
| 발렌시아(하코번 섬) | 발렌시아 모래 방패, 발렌시아 사막 보검, 화려한 낙타 가죽, 황금 사막의 모래반지 |
| 발렌시아(아레하자 마을) | 최고급 코코넛 시럽, 아레하자 전통 차, 아레하자 등대 조각상, 황금빛 선인장 꽃다발 |
| 카마실비아(그란디하) | 숲의 요정 향수병, 카마실비아 조각상, 달빛 수정 램프, 은빛 나무 이끼 장식 |
| 오딜리타(깊은 밤의 항구) | 검은 장미 꽃다발, 월광 수정 조각, 달빛 그림자 숙성 와인, 그림자 장식 거울 |
| 아침의 나라(해모 섬) | 대나무 수액 상자, 남포 특산품 감 상자, 고급 묵양함, 한짓골 산딸기 상자 |
| 아침의 나라(달래나루) | 최고급 청화백자 상자, 최고급 감투 상자, 놋쇠그릇 상자, 예리한 홍화도 상자 |

## Related Contents

### `barter-tier6-routes.relation.current-system`

- seed_key: "barter-tier6-routes.relation.current-system"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "barter-current-system"
- content_name_ko: "현행 물물교환 시스템"
- content_category: "ocean_barter"
- note: "현행 물물교환의 5→6단계 교역"
- order_no: 1
- relative_path: "../contents/barter-current-system.md"
### `barter-tier6-routes.relation.tier7`

- seed_key: "barter-tier6-routes.relation.tier7"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "barter-tier7-routes"
- content_name_ko: "7단계 물물교환 교역로"
- content_category: "ocean_barter"
- note: "6단계 교역품은 7단계 교역의 입력이 된다"
- order_no: 2
- relative_path: "../contents/barter-tier7-routes.md"
### `barter-current-system.relation.tier6`

- seed_key: "barter-current-system.relation.tier6"
- direction: "incoming"
- relation_type: "related"
- content_slug: "barter-current-system"
- content_name_ko: "현행 물물교환 시스템"
- content_category: "ocean_barter"
- note: "5→6단계 교역로"
- order_no: 2
- relative_path: "../contents/barter-current-system.md"
### `barter-route-strategy.relation.tier6`

- seed_key: "barter-route-strategy.relation.tier6"
- direction: "incoming"
- relation_type: "related"
- content_slug: "barter-route-strategy"
- content_name_ko: "물물교환 동선 전략"
- content_category: "ocean_barter"
- note: "6단계 교역 동선 참고"
- order_no: 2
- relative_path: "../contents/barter-route-strategy.md"
### `barter-tier7-routes.relation.tier6`

- seed_key: "barter-tier7-routes.relation.tier6"
- direction: "incoming"
- relation_type: "prerequisite"
- content_slug: "barter-tier7-routes"
- content_name_ko: "7단계 물물교환 교역로"
- content_category: "ocean_barter"
- note: "6단계 교역품이 입력으로 필요하다"
- order_no: 2
- relative_path: "../contents/barter-tier7-routes.md"
### `barter-onboarding-strategy.tier6`

- seed_key: "barter-onboarding-strategy.tier6"
- direction: "incoming"
- relation_type: "related"
- content_slug: "barter-onboarding-strategy"
- content_name_ko: "물물교환 입문 운영 전략"
- content_category: "ocean_barter"
- note: "6단계 공식 항로"
- order_no: 4
- relative_path: "../contents/barter-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `barter-tier6-routes.evidence.routes::barter-improvement-2026-04-15`

- evidence_seed_key: "barter-tier6-routes.evidence.routes::barter-improvement-2026-04-15"
- source_id: "barter-improvement-2026-04-15"
- title: "4월 15일(수) 업데이트 안내 (최종 수정 : 2026-04-24 20:05)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15451"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2026-04-15"
- retrieved_at: "2026-09-03T12:00:00+00:00"
- region: "KR"
- entity_type: "content_section"
- entity_id: "barter-tier6-routes.routes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "| 영지(거점) | 6단계 교역품 |\n|---|---|\n| 발렌시아(하코번 섬) | 발렌시아 모래 방패, 발렌시아 사막 보검, 화려한 낙타 가죽, 황금 사막의 모래반지 |\n| 발렌시아(아레하자 마을) | 최고급 코코넛 시럽, 아레하자 전통 차, 아레하자 등대 조각상, 황금빛 선인장 꽃다발 |\n| 카마실비아(그란디하) | 숲의 요정 향수병, 카마실비아 조각상, 달빛 수정 램프, 은빛 나무 이끼 장식 |\n| 오딜리타(깊은 밤의 항구) | 검은 장미 꽃다발, 월광 수정 조각, 달빛 그림자 숙성 와인, 그림자 장식 거울 |\n| 아침의 나라(해모 섬) | 대나무 수액 상자, 남포 특산품 감 상자, 고급 묵양함, 한짓골 산딸기 상자 |\n| 아침의 나라(달래나루) | 최고급 청화백자 상자, 최고급 감투 상자, 놋쇠그릇 상자, 예리한 홍화도 상자 |"
- active: true
- is_active: true

### Historical / inactive evidence

- None
