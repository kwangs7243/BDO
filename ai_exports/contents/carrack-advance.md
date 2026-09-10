<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 에페리아 중범선 : 점진

## Identity

- slug: "carrack-advance"
- name_ko: "에페리아 중범선 : 점진"
- category: "ocean_project"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- party_type: null
- difficulty: null

## Overview

- summary: "에페리아 무역선에서 증축하는 물물교환 특화 중범선. +10 무역선 파란 장비 4종과 점진 전용 본체 재료가 필요하다."
- purpose: "적재량이 높은 중범선 점진을 제작하고 물물교환·대양 콘텐츠의 운용 기반을 완성한다."

## Requirements

### `carrack-advance.starting-ship`

- seed_key: "carrack-advance.starting-ship"
- kind: "item"
- requirement_level: "required"
- title: "출발 선박"
- description: "에페리아 무역선에서 에페리아 중범선 : 점진으로 증축한다."
- structured_value: null

### `carrack-advance.requirement.blue-gear-plus10`

- seed_key: "carrack-advance.requirement.blue-gear-plus10"
- kind: "gear"
- requirement_level: "required"
- title: "+10 무역선 파란 장비 4종"
- description: "흑룡 선수상, 개량형 장갑, 메이나 함포, 비층 바람 돛을 각각 +10까지 강화해야 한다."
- structured_value:

```json
{
  "count": 4,
  "enhancement": 10,
  "items": [
    "에페리아 무역선 : 흑룡 선수상",
    "에페리아 무역선 : 개량형 장갑",
    "에페리아 무역선 : 메이나 함포",
    "에페리아 무역선 : 비층 바람 돛"
  ]
}
```

### `carrack-advance.requirement.body-materials`

- seed_key: "carrack-advance.requirement.body-materials"
- kind: "item"
- requirement_level: "required"
- title: "점진 본체 재료"
- description: "달의 핏줄이 새겨진 아마포 180, 짙은 파도빛이 감도는 규격 각목 144, 화려한 암염 주괴 35, 화려한 진주 결정 35, 심해의 눈물 42가 필요하다."
- structured_value:

```json
{
  "달의 핏줄이 새겨진 아마포": 180,
  "심해의 눈물": 42,
  "짙은 파도빛이 감도는 규격 각목": 144,
  "화려한 암염 주괴": 35,
  "화려한 진주 결정": 35
}
```

## Steps

### `carrack-advance.confirm-upgrade-path`

- seed_key: "carrack-advance.confirm-upgrade-path"
- phase: "preparation"
- order_no: 1
- title: "증축 경로 확인"
- description: "에페리아 무역선에서 중범선 점진으로 이어지는 증축 경로를 확인한다."
- checkable: false

### `carrack-advance.step.prepare-green-gear`

- seed_key: "carrack-advance.step.prepare-green-gear"
- phase: "preparation"
- order_no: 2
- title: "무역선 녹색 장비 4종 +10"
- description: "팔라시에게 구입하는 황동 선수상·강화 장갑·베리샤 함포·하얀 바람 돛을 각각 +10까지 강화한다."
- checkable: true

### `carrack-advance.step.craft-blue-gear`

- seed_key: "carrack-advance.step.craft-blue-gear"
- phase: "preparation"
- order_no: 3
- title: "무역선 파란 장비 4종 제작"
- description: "에페리아 1-4번지 2층 선박 부품 공방 4단계에서 흑룡 선수상·개량형 장갑·메이나 함포·비층 바람 돛을 제작한다."
- checkable: true

### `carrack-advance.step.enhance-blue-gear`

- seed_key: "carrack-advance.step.enhance-blue-gear"
- phase: "preparation"
- order_no: 4
- title: "파란 장비 4종 +10"
- description: "제작한 파란 장비 4종을 파도의 블랙스톤으로 +10까지 강화한다."
- checkable: true

### `carrack-advance.step.collect-body-materials`

- seed_key: "carrack-advance.step.collect-body-materials"
- phase: "preparation"
- order_no: 5
- title: "점진 본체 재료 수집"
- description: "아마포 180, 짙은 각목 144, 화려한 암염 35, 화려한 진주 35, 심해의 눈물 42를 확보한다."
- checkable: true

### `carrack-advance.step.upgrade`

- seed_key: "carrack-advance.step.upgrade"
- phase: "reward"
- order_no: 6
- title: "점진 증축"
- description: "나루터지기 증축 메뉴에서 요구 장비와 재료를 투입하여 에페리아 중범선 : 점진으로 증축한다."
- checkable: true

## Schedules

- None

## Rewards

- None

## Sections

### `carrack-advance.why`

- seed_key: "carrack-advance.why"
- section_type: "why"
- title: "왜 점진인가"
- order_no: 1

#### body_markdown

점진은 적재량이 높아 물물교환에 가장 유리한 중범선이다.

### `carrack-advance.section.body-recipe`

- seed_key: "carrack-advance.section.body-recipe"
- section_type: "preparation"
- title: "점진 본체 요구량"
- order_no: 2

#### body_markdown

+10 무역선 파란 장비 4종과 달의 핏줄이 새겨진 아마포 180, 짙은 파도빛이 감도는 규격 각목 144, 화려한 암염 주괴 35, 화려한 진주 결정 35, 심해의 눈물 42가 필요하다.

### `carrack-advance.section.blue-gear-recipes`

- seed_key: "carrack-advance.section.blue-gear-recipes"
- section_type: "preparation"
- title: "무역선 파란 장비 4종 제작식"
- order_no: 3

#### body_markdown

### 흑룡 선수상
- +10 에페리아 무역선 : 황동 선수상 ×1
- 홍조빛 해저단괴 ×50
- 강화된 섬나무 증착합판 ×300
- 심해초 줄기 ×125
- 대양의 견고한 현철 ×150

### 개량형 장갑
- +10 에페리아 무역선 : 강화 장갑 ×1
- 순수한 진주 결정 ×45
- 콕스해적단의 유물(협상 하급) ×60
- 콕스해적단의 유물(전투) ×60
- 달의 비늘이 새겨진 합판 ×200

### 메이나 함포
- +10 에페리아 무역선 : 베리샤 함포 ×1
- 파도빛이 감도는 규격 각목 ×180
- 콕스해적단의 유물(전투) ×60
- 달의 비늘이 새겨진 합판 ×200
- 순수한 암초 조각 ×180

### 비층 바람 돛
- +10 에페리아 무역선 : 하얀 바람 돛 ×1
- 홍조빛 해저단괴 ×40
- 콕스해적단의 유물(협상 상급) ×30
- 심해초 줄기 ×80
- 빛나는 코발트 주괴 ×30

### `carrack-advance.section.blue-gear-aggregate`

- seed_key: "carrack-advance.section.blue-gear-aggregate"
- section_type: "notes"
- title: "파란 장비 재료 총합"
- order_no: 4

#### body_markdown

파란 무역선 장비 4종 전체 기준 재료 합계:

- 홍조빛 해저단괴 90
- 강화된 섬나무 증착합판 300
- 심해초 줄기 205
- 대양의 견고한 현철 150
- 순수한 진주 결정 45
- 콕스해적단의 유물(협상 하급) 60
- 콕스해적단의 유물(전투) 120
- 달의 비늘이 새겨진 합판 400
- 파도빛이 감도는 규격 각목 180
- 순수한 암초 조각 180
- 콕스해적단의 유물(협상 상급) 30
- 빛나는 코발트 주괴 30

### `carrack-advance.section.current-acquisition-warning`

- seed_key: "carrack-advance.section.current-acquisition-warning"
- section_type: "common_mistakes"
- title: "현재 의뢰 보상은 최신 패치를 우선"
- order_no: 5

#### body_markdown

중범선 모험가 가이드의 제작식은 현재 요구량 확인에 사용한다. 다만 일부 의뢰명·일일 획득량 표기는 2025년 이후 개편 이전 정보가 남아 있으므로, 반복 의뢰의 현재 보상 수량은 2025-02-05/2025-05-14 패치를 우선한다.

## Related Contents

### `carrack-advance.relation.types`

- seed_key: "carrack-advance.relation.types"
- direction: "outgoing"
- relation_type: "part_of"
- content_slug: "carrack-types"
- content_name_ko: "에페리아 중범선 네 종류"
- content_category: "ocean_project"
- note: "점진은 중범선 네 분기 중 무역선 기반 적재 특화 분기"
- order_no: 1
- relative_path: "../contents/carrack-types.md"
### `carrack-advance.relation.materials`

- seed_key: "carrack-advance.relation.materials"
- direction: "outgoing"
- relation_type: "related"
- content_slug: "carrack-upgrade-materials"
- content_name_ko: "중범선 분기별 증축 핵심 재료"
- content_category: "ocean_project"
- note: "점진 증축 핵심 재료의 공통 비교표"
- order_no: 2
- relative_path: "../contents/carrack-upgrade-materials.md"
### `carrack-advance.relation.chiro`

- seed_key: "carrack-advance.relation.chiro"
- direction: "outgoing"
- relation_type: "unlocks"
- content_slug: "carrack-chiro-gear"
- content_name_ko: "중범선 치로 장비"
- content_category: "ocean_project"
- note: "중범선 완성 후 토로→치로→팔라시 장비 성장"
- order_no: 3
- relative_path: "../contents/carrack-chiro-gear.md"
### `carrack-types.relation.advance-project`

- seed_key: "carrack-types.relation.advance-project"
- direction: "incoming"
- relation_type: "related"
- content_slug: "carrack-types"
- content_name_ko: "에페리아 중범선 네 종류"
- content_category: "ocean_project"
- note: "기존 점진 프로젝트 상세"
- order_no: 1
- relative_path: "../contents/carrack-types.md"
### `iliya-weekly-barter.relation.carrack-advance`

- seed_key: "iliya-weekly-barter.relation.carrack-advance"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "iliya-weekly-barter"
- content_name_ko: "[물물교환][주간] 교역의 중심 일리야 섬"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/iliya-weekly-barter.md"
### `ocean-event-frico-wish-stone-2026.relation.carrack-advance`

- seed_key: "ocean-event-frico-wish-stone-2026.relation.carrack-advance"
- direction: "incoming"
- relation_type: "project_link"
- content_slug: "ocean-event-frico-wish-stone-2026"
- content_name_ko: "[이벤트] 프리코의 항해 기원석 연계 의뢰"
- content_category: "ocean_project"
- note: "이벤트 기간 항해/교역 진행 가속"
- order_no: 1
- relative_path: "../contents/ocean-event-frico-wish-stone-2026.md"
### `ocean-event-weekly-terror-2026.relation.carrack-advance`

- seed_key: "ocean-event-weekly-terror-2026.relation.carrack-advance"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "ocean-event-weekly-terror-2026"
- content_name_ko: "[이벤트][주간] 바다의 질서를 위협하는 공포"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/ocean-event-weekly-terror-2026.md"
### `ocean-event-weekly-threat-2026.relation.carrack-advance`

- seed_key: "ocean-event-weekly-threat-2026.relation.carrack-advance"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "ocean-event-weekly-threat-2026"
- content_name_ko: "[이벤트][주간] 바닷길을 가로막는 위협"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/ocean-event-weekly-threat-2026.md"
### `ocean-iliya-daily-barter.relation.carrack-advance`

- seed_key: "ocean-iliya-daily-barter.relation.carrack-advance"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "ocean-iliya-daily-barter"
- content_name_ko: "[물물교환][일일] 활기찬 일리야 섬"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/ocean-iliya-daily-barter.md"
### `ocean-supply-transport-oquilla.relation.carrack-advance`

- seed_key: "ocean-supply-transport-oquilla.relation.carrack-advance"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "ocean-supply-transport-oquilla"
- content_name_ko: "[일일] 보급물자 운송 (오킬루아의 눈)"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/ocean-supply-transport-oquilla.md"
### `oquilla-daily-black-rust-hunter.relation.carrack-advance`

- seed_key: "oquilla-daily-black-rust-hunter.relation.carrack-advance"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "oquilla-daily-black-rust-hunter"
- content_name_ko: "[일일] 그믐달 길드의 검은무쇠이빨 사냥꾼"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/oquilla-daily-black-rust-hunter.md"
### `oquilla-daily-candidum-hunter.relation.carrack-advance`

- seed_key: "oquilla-daily-candidum-hunter.relation.carrack-advance"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "oquilla-daily-candidum-hunter"
- content_name_ko: "[일일] 그믐달 길드의 칸디둠 사냥꾼"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/oquilla-daily-candidum-hunter.md"
### `oquilla-daily-guild-charity.relation.carrack-advance`

- seed_key: "oquilla-daily-guild-charity.relation.carrack-advance"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "oquilla-daily-guild-charity"
- content_name_ko: "[일일] 길드는 자선단체가 아니다"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/oquilla-daily-guild-charity.md"
### `oquilla-daily-mutual-benefit.relation.carrack-advance`

- seed_key: "oquilla-daily-mutual-benefit.relation.carrack-advance"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "oquilla-daily-mutual-benefit"
- content_name_ko: "[일일] 너도 좋고, 나도 좋고"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/oquilla-daily-mutual-benefit.md"
### `oquilla-daily-nineshark-hunter.relation.carrack-advance`

- seed_key: "oquilla-daily-nineshark-hunter.relation.carrack-advance"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "oquilla-daily-nineshark-hunter"
- content_name_ko: "[일일] 그믐달 길드의 나인샤크 사냥꾼"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/oquilla-daily-nineshark-hunter.md"
### `oquilla-daily-self-defense.relation.carrack-advance`

- seed_key: "oquilla-daily-self-defense.relation.carrack-advance"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "oquilla-daily-self-defense"
- content_name_ko: "[일일] 제 몸 하나는 스스로 지켜야"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/oquilla-daily-self-defense.md"
### `oquilla-daily-young-sea-monster-hunter.relation.carrack-advance`

- seed_key: "oquilla-daily-young-sea-monster-hunter.relation.carrack-advance"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "oquilla-daily-young-sea-monster-hunter"
- content_name_ko: "[일일] 그믐달 어린 해왕류 사냥꾼"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/oquilla-daily-young-sea-monster-hunter.md"
### `oquilla-weekly-black-rust-hunter.relation.carrack-advance`

- seed_key: "oquilla-weekly-black-rust-hunter.relation.carrack-advance"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "oquilla-weekly-black-rust-hunter"
- content_name_ko: "[주간] 그믐달 길드의 검은무쇠이빨 사냥꾼"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/oquilla-weekly-black-rust-hunter.md"
### `oquilla-weekly-candidum-hunter.relation.carrack-advance`

- seed_key: "oquilla-weekly-candidum-hunter.relation.carrack-advance"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "oquilla-weekly-candidum-hunter"
- content_name_ko: "[주간] 그믐달 길드의 칸디둠 사냥꾼"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/oquilla-weekly-candidum-hunter.md"
### `oquilla-weekly-nineshark-hunter.relation.carrack-advance`

- seed_key: "oquilla-weekly-nineshark-hunter.relation.carrack-advance"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "oquilla-weekly-nineshark-hunter"
- content_name_ko: "[주간] 그믐달 길드의 나인샤크 사냥꾼"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/oquilla-weekly-nineshark-hunter.md"
### `oquilla-weekly-population-report.relation.carrack-advance`

- seed_key: "oquilla-weekly-population-report.relation.carrack-advance"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "oquilla-weekly-population-report"
- content_name_ko: "[주간] 개체수 증가 보고"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/oquilla-weekly-population-report.md"
### `oquilla-weekly-young-otters.relation.carrack-advance`

- seed_key: "oquilla-weekly-young-otters.relation.carrack-advance"
- direction: "incoming"
- relation_type: "source_for"
- content_slug: "oquilla-weekly-young-otters"
- content_name_ko: "[주간] 어린 해달 상인들을 위해"
- content_category: "ocean_project"
- note: "점진 제작/파란 무역선 장비 재료 획득과 관련"
- order_no: 1
- relative_path: "../contents/oquilla-weekly-young-otters.md"
### `sailing-special-pass-2026.relation.carrack-advance`

- seed_key: "sailing-special-pass-2026.relation.carrack-advance"
- direction: "incoming"
- relation_type: "project_link"
- content_slug: "sailing-special-pass-2026"
- content_name_ko: "항해 스페셜 패스 (2026)"
- content_category: "ocean_project"
- note: "중범선 제작 가속용 기간제 패스"
- order_no: 1
- relative_path: "../contents/sailing-special-pass-2026.md"
### `carrack-upgrade-materials.relation.advance`

- seed_key: "carrack-upgrade-materials.relation.advance"
- direction: "incoming"
- relation_type: "related"
- content_slug: "carrack-upgrade-materials"
- content_name_ko: "중범선 분기별 증축 핵심 재료"
- content_category: "ocean_project"
- note: "기존 점진 상세 프로젝트"
- order_no: 3
- relative_path: "../contents/carrack-upgrade-materials.md"
### `account-progression-foundation.carrack`

- seed_key: "account-progression-foundation.carrack"
- direction: "incoming"
- relation_type: "related"
- content_slug: "account-progression-foundation"
- content_name_ko: "가문 성장 기반"
- content_category: "progression"
- note: null
- order_no: 7
- relative_path: "../contents/account-progression-foundation.md"
### `barter-onboarding-strategy.advance-project`

- seed_key: "barter-onboarding-strategy.advance-project"
- direction: "incoming"
- relation_type: "project_link"
- content_slug: "barter-onboarding-strategy"
- content_name_ko: "물물교환 입문 운영 전략"
- content_category: "ocean_barter"
- note: "중범선 점진 재료 목적"
- order_no: 7
- relative_path: "../contents/barter-onboarding-strategy.md"
### `sailing-onboarding-strategy.advance-project`

- seed_key: "sailing-onboarding-strategy.advance-project"
- direction: "incoming"
- relation_type: "project_link"
- content_slug: "sailing-onboarding-strategy"
- content_name_ko: "항해 입문 운영 전략"
- content_category: "ocean_guide"
- note: "점진 프로젝트 진행도"
- order_no: 8
- relative_path: "../contents/sailing-onboarding-strategy.md"

## Evidence and Sources

### Current evidence

### `carrack-advance.purpose::carrack-guide`

- evidence_seed_key: "carrack-advance.purpose::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "carrack-advance"
- claim_key: "purpose"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "적재량이 높은 중범선 점진을 제작하고 물물교환·대양 콘텐츠의 운용 기반을 완성한다."
- active: true
- is_active: true

### `carrack-advance.summary::carrack-guide`

- evidence_seed_key: "carrack-advance.summary::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content"
- entity_id: "carrack-advance"
- claim_key: "summary"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "에페리아 무역선에서 증축하는 물물교환 특화 중범선. +10 무역선 파란 장비 4종과 점진 전용 본체 재료가 필요하다."
- active: true
- is_active: true

### `carrack-advance.evidence.requirement.blue-gear-plus10::carrack-guide`

- evidence_seed_key: "carrack-advance.evidence.requirement.blue-gear-plus10::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-advance.requirement.blue-gear-plus10"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진에 +10 무역선 파란 장비 4종 필요"
- active: true
- is_active: true

### `carrack-advance.evidence.requirement.body-materials::carrack-guide`

- evidence_seed_key: "carrack-advance.evidence.requirement.body-materials::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-advance.requirement.body-materials"
- claim_key: "structured_value"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진 본체 재료 수량"
- active: true
- is_active: true

### `carrack-advance.requirement.starting-ship::carrack-guide`

- evidence_seed_key: "carrack-advance.requirement.starting-ship::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_requirement"
- entity_id: "carrack-advance.starting-ship"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "무역선에서 점진으로 증축"
- active: true
- is_active: true

### `carrack-advance.evidence.section.blue-gear-aggregate::carrack-guide`

- evidence_seed_key: "carrack-advance.evidence.section.blue-gear-aggregate::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "carrack-advance.section.blue-gear-aggregate"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "4종 제작식을 합산한 파란 장비 재료 총합"
- active: true
- is_active: true

### `carrack-advance.evidence.section.blue-gear-recipes::carrack-guide`

- evidence_seed_key: "carrack-advance.evidence.section.blue-gear-recipes::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "carrack-advance.section.blue-gear-recipes"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "무역선 파란 장비 4종 제작식"
- active: true
- is_active: true

### `carrack-advance.evidence.section.body-recipe::carrack-guide`

- evidence_seed_key: "carrack-advance.evidence.section.body-recipe::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "carrack-advance.section.body-recipe"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진 본체 요구량"
- active: true
- is_active: true

### `carrack-advance.evidence.section.current-acquisition-warning::carrack-guide`

- evidence_seed_key: "carrack-advance.evidence.section.current-acquisition-warning::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "carrack-advance.section.current-acquisition-warning"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "모험가 가이드의 일부 반복 의뢰 표기가 최신 패치와 불일치하므로 최신 패치를 우선"
- active: true
- is_active: true

### `carrack-advance.evidence.section.current-acquisition-warning::ocean-iliya-consolidation-2025-05-14`

- evidence_seed_key: "carrack-advance.evidence.section.current-acquisition-warning::ocean-iliya-consolidation-2025-05-14"
- source_id: "ocean-iliya-consolidation-2025-05-14"
- title: "5월 14일(수) 업데이트 안내 (최종 수정 : 2025-05-19 18:55)"
- url: "https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-05-14"
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "carrack-advance.section.current-acquisition-warning"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "모험가 가이드의 일부 반복 의뢰 표기가 최신 패치와 불일치하므로 최신 패치를 우선"
- active: true
- is_active: true

### `carrack-advance.evidence.section.current-acquisition-warning::ocean-quest-rework-2025-02-05`

- evidence_seed_key: "carrack-advance.evidence.section.current-acquisition-warning::ocean-quest-rework-2025-02-05"
- source_id: "ocean-quest-rework-2025-02-05"
- title: "2월 5일(수) 업데이트 안내 (최종 수정 : 2025-04-28 17:08)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=13508"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-02-05"
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "carrack-advance.section.current-acquisition-warning"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "모험가 가이드의 일부 반복 의뢰 표기가 최신 패치와 불일치하므로 최신 패치를 우선"
- active: true
- is_active: true

### `carrack-advance.section.why::carrack-guide`

- evidence_seed_key: "carrack-advance.section.why::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_section"
- entity_id: "carrack-advance.why"
- claim_key: "body"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진은 높은 적재량으로 물물교환에 유리"
- active: true
- is_active: true

### `carrack-advance.step.confirm-path::carrack-guide`

- evidence_seed_key: "carrack-advance.step.confirm-path::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "carrack-advance.confirm-upgrade-path"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "무역선에서 점진으로 이어지는 증축 경로"
- active: true
- is_active: true

### `carrack-advance.evidence.step.collect-body-materials::carrack-guide`

- evidence_seed_key: "carrack-advance.evidence.step.collect-body-materials::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "carrack-advance.step.collect-body-materials"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "점진 본체 재료 요구량"
- active: true
- is_active: true

### `carrack-advance.evidence.step.craft-blue-gear::carrack-guide`

- evidence_seed_key: "carrack-advance.evidence.step.craft-blue-gear::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "carrack-advance.step.craft-blue-gear"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "에페리아 1-4번지 2층 공방 4단계 제작"
- active: true
- is_active: true

### `carrack-advance.evidence.step.enhance-blue-gear::carrack-guide`

- evidence_seed_key: "carrack-advance.evidence.step.enhance-blue-gear::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "carrack-advance.step.enhance-blue-gear"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "파란 장비 +10 강화"
- active: true
- is_active: true

### `carrack-advance.evidence.step.prepare-green-gear::carrack-guide`

- evidence_seed_key: "carrack-advance.evidence.step.prepare-green-gear::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "carrack-advance.step.prepare-green-gear"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "파란 장비 제작 전 +10 녹색 장비 준비"
- active: true
- is_active: true

### `carrack-advance.evidence.step.upgrade::carrack-guide`

- evidence_seed_key: "carrack-advance.evidence.step.upgrade::carrack-guide"
- source_id: "carrack-guide"
- title: "중범선 만들기"
- url: "https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=295"
- publisher: "Pearl Abyss"
- source_type: "official_guide"
- published_at: null
- retrieved_at: null
- region: "KR"
- entity_type: "content_step"
- entity_id: "carrack-advance.step.upgrade"
- claim_key: "description"
- verification_status: "verified"
- last_verified_at: "2026-09-03"
- evidence_note: "나루터지기 증축 메뉴"
- active: true
- is_active: true

### Historical / inactive evidence

- None
