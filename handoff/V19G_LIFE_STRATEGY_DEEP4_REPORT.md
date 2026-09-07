# V1.9G — Life Strategy Deep Pack IV Report

## Git 기준

- 기준일 및 조사일: 2026-09-07
- Source of Truth: main @ abfe0e6d59b41bd354da1b107aa9be5e147a1843
- 작업 branch: feature/v1.9g-life-strategy-deep4
- 구현 commit: 이 보고서를 포함하는 V1.9G commit과 최종 작업 보고 참조

## 완료 범위

기존 대양 canonical FACT를 복제하지 않고 첫 항해와 물물교환 회차의 조건부 판단을 담당하는 Strategy Content 두 건을 추가했다.

1. sailing-onboarding-strategy
2. barter-onboarding-strategy

두 Content의 Requirement는 모두 knowledge_role=strategy다. 실시간 물물교환 목록, OCR, route optimizer, scheduler 알고리즘, 시세·시간당 수익, 새 ChecklistTemplate, 새 Prompt mode, schema, migration, frontend component와 실제 DB는 추가하거나 변경하지 않았다.

## 수치

- Source: 161 → 164, 신규 3
- Content: 266 → 268, 신규 2, 기존 Content 수정 1
- active Content: 268
- FACT requirement: 194 → 194
- STRATEGY requirement: 41 → 51, 신규 10
- MEASUREMENT requirement: 11 → 11
- V1.9G 신규 Step: 20
- V1.9G 신규 Section: 6
- V1.9G 신규 Relation: 20
- 전체 Relation row: 448 → 468
- V1.9G 신규 claim Evidence declaration: 40
- seed Evidence status: verified 1060, superseded 52, needs_review 31, conflict 2, community_consensus 1
- 신규 conflict / superseded declaration: 0 / 0

## Sailing 기존 FACT audit

다음 기존 Content의 책임과 공식 근거를 재검증했다.

- carrack-types, carrack-advance, carrack-upgrade-materials
- sailor-hiring-growth, sailor-role-slots, ocean-first-mates, sailor-health-food
- ocean-consumables, sea-crystals
- carrack-chiro-gear, carrack-palasi-gear, carrack-palasi-enhancement
- panokseon과 기존 해양 사냥·오킬루아 routine Content

공식 대양의 모든 것 가이드, 중범선 만들기 가이드, 2026-08-26 대양 장비 패치, 2026-09-02 생활 장비 통합과 2026-09-03 임시 점검을 대조했다. 출항 전 보급·식량·포탄·수리·선원·화물 관리와 현재 중범선 progression을 대체하는 상충 FACT는 발견하지 않아 기존 stable Content를 유지했다.

신규 Sailing Strategy는 목적 선택, 출항 준비, 짧은 첫 항해, 병목 관찰, 귀환 후 보급·수리·재고 정리, 다음 세션의 단일 개선만 담당한다. 특정 중범선이나 선원 조합을 universal best로 만들지 않는다.

## Barter 기존 FACT audit

다음 기존 책임을 재검증했다.

- barter-current-system: 2026-04-15 이후 저단 교환, 교섭력, 수송 제한, 까마귀의 둥지와 돌발 교환
- barter-stage-values: 1~7단계 판매 가능 여부·가격·무게
- barter-tier6-routes, barter-tier7-routes: 공식 고단계 경로
- barter-route-strategy: 날짜 기반 커뮤니티 거리 측정
- crow-coin-material-shop: 까마귀 주화 중범선 재료 가격
- ocean-iliya-daily-barter, iliya-weekly-barter: 반복 목표

2026-04-15 공식 교역 개편의 단계·무게·판매가·교섭력·수송 제한은 기존 FACT와 일치했다.

## 2026-04-15 이후 후속 patch audit

2026-05-20 공식 업데이트에서 실제 상충 FACT 한 건을 확인했다. 중범선 제작·증축 재료의 까마귀 주화 요구량이 약 20% 감소했으므로 crow-coin-material-shop의 기존 17개 가격을 최신 공식 값으로 교체했다.

- Source 추가: barter-accessibility-2026-05-20
- Content slug 및 Reward seed_key 유지
- Content/Reward stable ID 유지
- 최신 Evidence는 2026-05-20 공식 Source를 참조
- V1.9F 기준의 2024 Source Evidence는 임시 DB import에서 inactive 이력으로 보존
- 신규 교역로 개방 조건과 상점의 추가 품목은 이번 Strategy milestone의 신규 FACT로 확장하지 않음

2026-08-26부터 2026-09-03까지의 대양 장비·생활 장비·known issue 후속 자료에서는 기존 항해 FACT를 추가로 교체해야 할 충돌을 확인하지 못했다.

## barter-route-strategy responsibility 판정

A안인 Advanced route optimization / measurement responsibility로 판정했다.

- 기존 Content는 2026-05-31 거리 측정과 고단계 경로 참고를 계속 담당한다.
- 신규 barter-onboarding-strategy는 현재 목록·보유 재고·화물·목적을 보고 route를 어떻게 판단할지만 담당한다.
- Life mapping에서 기존 route Content는 advanced에 유지한다.
- scheduler 알고리즘, 점수, 거리 순위와 현재 최적 경로는 복제하지 않았다.

## 신규 Source

### 공식

- barter-accessibility-2026-05-20
  - Pearl Abyss 2026-05-20 업데이트
  - 교역로 접근성 및 까마귀 주화 상점 가격 조정의 current FACT 정본

### Community Strategy

- barter-scheduler-strategy-2026-06-06
  - 현재 목록, 보유 교역품, 적재 상태, 섬 묶음과 거리 입력에 따라 경로가 달라진다는 조건부 판단만 사용
- sailing-academy-community-2026-06-14
  - 출항 전 보급·수리·화물 확인과 첫 교환 흐름만 Strategy discovery로 사용

공식과 community Source type을 분리했다. Academy 보상·지급 선박·정확한 수량은 community 글만으로 FACT화하지 않았다.

## Measurement 및 거절한 데이터

다음은 V1.9G static seed에서 제외했다.

- 실시간 barter list와 섬별 현재 교환품
- 현재 남은 교환 횟수
- scheduler 알고리즘·OCR·다운로드 파일·외부 executable
- scheduler 점수와 route ranking
- 특정 배 속도의 이동 시간
- silver/hour, crow coin/hour와 동적 시장 가격
- universal best ship, sailor build, island 또는 route
- community 글의 Academy 보상·지급 선박 FACT

오래된 중범선 가이드와 2024 패치의 까마귀 주화 재료 가격은 current 가격 근거로 거절하고 2026-05-20 공식 패치를 우선했다.

## Life mapping

- Sailing getting_started:
  - carrack-types
  - sailing-onboarding-strategy
  - sailor-hiring-growth
- Barter getting_started:
  - barter-current-system
  - barter-onboarding-strategy
- barter-route-strategy는 advanced_contents에 유지

Python에는 FACT/Strategy 본문을 추가하지 않았고 presentation slug 순서만 변경했다.

## Relations

Sailing Strategy는 기존 carrack-types, 선원 성장·역할·건강, 보급품, 증축 재료, 해원석, Carrack Advance Project, 해양 사냥과 판옥선에 10개 관계를 연결했다.

Barter Strategy는 현행 규칙, 단계별 값, advanced route, Tier 6/7, 까마귀 주화 상점, Carrack Advance Project, 창고, 일일·주간 물물교환에 10개 관계를 연결했다.

## Prompt role 검증

content_onboarding, next_action, verify_latest에서 신규 Content의 summary, purpose, Requirement, Step, strategy Section과 common_mistakes가 모두 STRATEGY로 직렬화되고 unresolved 영역에 잘못 들어가지 않는 것을 검증했다. 새 Prompt mode와 PromptSection은 만들지 않았다.

## Seed import와 이력 보존

V1.9F baseline 임시 SQLite DB를 migration한 뒤 사용자 marker를 생성하고 V1.9G seed를 두 번 import했다.

- 기존 crow-coin-material-shop Content ID 유지
- 기존 Reward stable ID 유지
- 과거 2024 가격 Evidence ID와 Source를 inactive 이력으로 보존
- 신규 Strategy Content ID 재import 유지
- canonical row count와 Evidence count 멱등
- ChecklistInstance/ChecklistItemState 유지
- UserContentState 유지
- UserMaterialInventory 유지
- UserProjectStageState 유지
- Carrack Project canonical Material/Stage 상태 유지

실제 backend/bdo.db는 사용하지 않았다.

## 검증 결과

- V1.9G semantic/import tests: 9 passed
- Backend 전체: 286 passed
- Frontend typecheck: passed
- Frontend lint: passed
- Frontend tests: 14 files / 57 passed
- Frontend build: passed
- git diff --check: passed
- 기존 Starlette httpx deprecation warning 1건
- schema/migration: 변경 없음
- backend/bdo.db SHA-256 before/after:
  - E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5
  - E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5