# V1.9F — Life Strategy Deep Pack III Report

## Git 기준

- 기준일 및 조사일: 2026-09-06
- Source of Truth: `main @ c947f8ee44ecaa2e4476ce4b9b896afeb20e9ff0`
- 작업 branch: `feature/v1.9f-life-strategy-deep3`
- 구현 commit: 이 보고서를 포함하는 V1.9F commit과 최종 작업 보고 참조

## 완료 범위

요리와 연금의 기존 current-system FACT를 복제하지 않고 실제 첫 행동을 결정하는 onboarding/strategy Content를 추가했다.

1. `cooking-onboarding-strategy`
2. `alchemy-onboarding-strategy`

두 Content의 Requirement는 모두 `knowledge_role=strategy`다. 전체 recipe catalog, 고정 수익표, 실시간 시장값, 새 Prompt mode, schema, migration, frontend component와 실제 DB는 추가하거나 변경하지 않았다.

## 수치

- Source: 155 → 161, 신규 6
- Content: 264 → 266, 신규 2, 기존 Content 수정 0
- active Content: 266
- FACT requirement: 194 → 194, 신규 0
- STRATEGY requirement: 31 → 41, 신규 10
- MEASUREMENT requirement: 11 → 11, 신규 0
- V1.9F 신규 Step: 19
- V1.9F 신규 Section: 6
- V1.9F 신규 Relation: 19
- 전체 Relation row: 429 → 448
- V1.9F 신규 claim Evidence: 39
- 전체 Evidence status: verified 1020, superseded 52, needs_review 31, conflict 2, community_consensus 1
- 신규 conflict / superseded: 0 / 0

## Cooking 기존 FACT audit

다음 기존 canonical Content를 공식 최신 자료와 대조했다.

- `cooking-current-system`: 거주지·요리 도구와 최소 요리 시간
- `cooking-mastery-effects`: 숙련도 효과
- `cooking-mass-production`: 연속 요리 중 대량 요리 발동과 묶음 처리
- `witch-delicacy`: 요리 부산물과 교환
- `cooking-growth-surprise-quest`: 성장 의뢰
- `imperial-crafting-delivery-daily`: 요리·연금 별도 납품, 가문 일일 제한, 포장과 reset 책임

공식 [요리 가이드](https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102), [황실 납품 가이드](https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=109), [황금 인장 가이드](https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=110), [황실 제작 납품 개선 이력](https://www.kr.playblackdesert.com/ko-KR/Adventure/History?_groupMasterNo=13111)을 확인했다. 기존 FACT를 교체해야 할 상충 current claim은 확인되지 않아 stable key와 Evidence를 그대로 유지했다.

## Alchemy 기존 FACT audit

다음 기존 canonical Content를 재검증했다.

- `alchemy-current-system`: 도구, 투입 수량과 결과 분류
- `alchemy-mastery-effects`: 숙련도 효과
- `alchemy-products-and-byproducts`: 결과물과 부산물 분류
- `alchemy-growth-surprise-quest`: 성장 의뢰
- `alchemy-imperial-current`: 현재 황실 연금 포장 기준
- `alchemy-stone-current-progression`, `alchemy-stone-growth`, `life-alchemy-stones`: 일반 연금 생산과 분리된 연금석 progression

공식 [연금 기초 가이드](https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=99), [연금 가이드](https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=100), [연금석 가이드](https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=101), [2025-05-14 업데이트](https://www.kr.playblackdesert.com/ko-kr/News/Detail?countryType=ko-kr&groupContentNo=13955), [2026-01-14 업데이트](https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15070)를 확인했다. 기존 FACT를 교체할 상충 current claim은 확인되지 않았다.

## 2026-09-02 equipment integration 영향

[2026-09-02 생활 장비 통합 업데이트](https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-kr&groupContentNo=16141)를 current equipment 기준으로 사용했다. 신규 Strategy에는 과거 장비 slot이나 정확한 gear build를 복제하지 않고 기존 `life-common-gear`, `life-artifacts-lightstones`, `life-alchemy-stones` 책임을 유지했다. 2023 커뮤니티 광명석 글의 `숙련도 +20`, `최대 소지 무게 +30LT` 같은 과거 exact 수치는 current recommendation으로 채택하지 않았다.

## 황실 납품 current rule audit

요리와 연금은 별도 납품 분야이며 한쪽 납품이 다른 쪽 가능 수량을 소비하지 않는 현재 구조, 가문 일일 제한, 00:00 reset, 대량 포장 지식과 노끈 지원을 기존 canonical Content에서 유지했다. 신규 Strategy는 어떤 상자를 선택할지 판단하는 조건만 다루며 reset, reward 또는 checklist를 중복 생성하지 않는다.

## Cooking strategy

- 직접 사용, 생활 레벨, 마녀의 별미·공헌도, 황실 납품, 후속 제작, 판매 중 목적을 먼저 고른다.
- 현재 제작 노트에서 recipe와 대체 재료를 확인하고 결과물 하나를 소량 검증한다.
- NPC, 생산 노드·일꾼, 재배, 채집, 가공, 거래소, 부산물·교환을 재료별 공급 후보로 비교한다.
- 재료 재고, 요리 시간, 도구 내구도, 가방·창고, 포장·이동 중 실제 병목 하나를 다음 세션에서 개선한다.
- 황실 납품은 레벨·상자 단계·재료·일일 가능 수량·현재 시장 조건을 확인하는 독립 일일 출구로 판단한다.
- `single_default_goal`, `universal_best_recipe`, `universal_best_box`, `mastery_solves_all`을 false로 두고 `fixed_profit_threshold`는 null로 유지했다.

## Alchemy strategy

- 직접 사용, 중간재, Project 재료, 황실 납품, 판매, 경험치 성장 중 목적을 고른다.
- 최종 결과물 → 중간 연금재 → 혈액·오일·시약·흔적·수액·식물 → 확보 경로 순서로 역산한다.
- 현재 제작식과 정확한 비율을 확인하고 실패 시 재료 소비 위험 때문에 첫 제작을 작은 묶음으로 검증한다.
- 채집, 수렵, 노드, 재배, 거래소, 교환·인장, 보유 재고를 recipe별로 비교한다.
- 결과물 출구와 황실 판단을 공급 상태에 맞춰 선택하고 연금석 progression은 advanced Content로 분리한다.
- `universal_bottleneck_material`, `universal_best_product`를 false로 두고 `fixed_margin_threshold`는 null로 유지했다.

## 공식 Source

신규 Source 2건은 Pearl Abyss `official_guide`다.

- [황실 납품](https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=109)
- [황금 인장](https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=110)

기존 `cooking-guide`, `alchemy-basic-guide`, `alchemy-guide`, `alchemy-stone-guide`, `imperial-delivery-history`, `ocean-iliya-consolidation-2025-05-14`, `dark-rift-reward-2026-01-14`, `life-unification-2026-09-02` Source도 stable ID로 재사용했다.

## Community Strategy Source

신규 4건은 모두 `community_strategy`이며 공식 FACT로 취급하지 않는다.

- [요리 황납 운용 사례](https://blackdesertonlineyoutube.tistory.com/186) — 검사학개론, 2025-01-30
- [연금 황납 운용 사례](https://blackdesertonlineyoutube.tistory.com/169) — 검사학개론, 2024-11-09
- [요리 황납 방향 토론](https://www.inven.co.kr/board/black/3584/50504) — 검은사막 인벤, 2025-12-25
- [연금 재료 노드 운용 사례](https://www.kr.playblackdesert.com/ko-kr/Forum/ForumTopic/Detail?_opinionNo=0&_topicNo=142101) — 새별-KR, 2025-10-28

단일 작성자의 결론을 보편 규칙으로 일반화하지 않고, 독립 커뮤니티 자료는 공급 경로·병목·조건부 선택의 교차 참고에만 사용했다.

## Measurement로 제외한 Source와 값

- 검사학개론 `/186`, `/169`의 현재 평균가, 품목별 마진, 숙련도별 손익표와 고정 threshold
- 황실 연금 인장 효율 `/203`, 황실 요리 인장 효율 `/103`의 정적 은화 환산값
- Inven 글의 특정 recipe 고정 추천과 당시 경제 수치
- 노드 글의 노드 순위, 가격과 수익 수치
- 현재 거래소 가격, box별 수익, silver/hour, 품목 수익 ranking과 오늘의 최고 효율

자료는 발견 또는 전략 맥락에만 사용했고 MEASUREMENT requirement를 추가하지 않았다.

## Stale / rejected community source

검사학개론 `/85`는 2023년 생활 광명석·장비 글이므로 2026-09-02 통합 이후 current exact 세팅 근거에서 제외했다. `/203`, `/103`은 durable FACT가 아니라 시장 의존 계산이므로 Source row나 canonical 값을 추가하지 않았다.

2026-09-06 현재 알려진 문제에서 올비아 아카데미 공용 요리·연금 도구 사용 문제와 장원 도구의 주거지 점수 표시 문제를 확인했다. 일반 거주지 도구 기반 core onboarding을 막는 영구 규칙이 아니고 단기 수정 대상이므로 신규 Strategy에 넣지 않았다.

## Relations와 Life mapping

Cooking은 current system, mastery, mass production, Witch's Delicacy, 황실 제작 납품, 성장 의뢰, 재배 전략, 생산 노드, 창고와 연결했다. Alchemy는 current system, mastery, 결과물·부산물, 황실 연금, 성장 의뢰, 채집·재배 전략, 생산 노드, 창고와 연금석 advanced progression에 연결했다.

`backend/app/life.py`의 presentation mapping만 확장했다.

- cooking getting_started: `cooking-current-system` → `cooking-onboarding-strategy`
- alchemy getting_started: `alchemy-current-system` → `alchemy-onboarding-strategy`

Python에는 게임 FACT나 Strategy 본문을 넣지 않았다.

## Prompt role validation

새 Prompt mode, collector 또는 renderer를 추가하지 않았다. V1.9D의 일반 역할 파생 규칙으로 두 신규 Content의 summary, purpose, Requirements, Steps, strategy와 common mistakes Section이 `content_onboarding`, `next_action`, `verify_latest`에서 모두 `knowledge_role=strategy`로 직렬화됨을 검증했다. unresolved claim은 없으며 기존 Cooking/Alchemy FACT와 MEASUREMENT 수치는 변하지 않았다.

## Seed idempotency와 user-history preservation

`backend/tests/test_life_strategy_deep3_seed.py`에 9개 semantic/import 테스트를 추가했다.

- Source ID·URL, Content slug와 신규 stable seed key 고유성
- unknown Evidence Source 0, 모든 Requirement/Step/Section claim Evidence coverage
- 기존 Cooking/Alchemy/황실/연금석 FACT 소유권과 stable key 유지
- dynamic economy와 stale 2023 exact gear 수치 배제
- Cooking/Alchemy 목적·공급·소량 검증·병목·황실 판단과 relation integrity
- Life API discovery 순서
- 3개 Prompt mode의 strategy role
- migration `20260902_0001` → head
- V1.9E baseline import → 사용자 marker 생성 → V1.9F import → V1.9F 재import
- 기존 Content/nested ID, inactive/superseded Evidence, checklist history, UserContentState, UserMaterialInventory, UserProjectStageState 보존
- 신규 Content ID와 canonical row count의 2회 import 멱등성

전체 회귀에서 V1.9C/E historical baseline fixture가 후속 Content의 relation 때문에 당시 Content를 제거한 뒤 참조가 끊기는 문제를 확인했다. 특정 V1.9F slug를 하드코딩하지 않고, 제외 대상에 의존하는 후속 Content를 재귀적으로 제외하며 남은 Evidence가 실제 참조하는 Source는 보존하도록 두 fixture를 일반화했다. 기존 stable ID와 사용자 이력 검증은 유지했다.

모든 import 검증은 `tmp_path` SQLite에서 수행하며 실제 `backend/bdo.db`를 사용하지 않는다.

## 전체 검증

### Backend

- `uv run pytest tests/test_life_strategy_deep3_seed.py -q`: 9 passed, 기존 Starlette TestClient deprecation warning 1건
- `uv run pytest -q`: 277 passed, 기존 warning 1건

### Frontend

- `npm run typecheck`: passed
- `npm run lint`: passed
- `npm run test -- --run`: 14 files / 57 tests passed
- `npm run build`: passed, 41 modules transformed

### 공통

- `git diff --check`: passed
- 작업 전 `backend/bdo.db` SHA-256: `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
- 작업 후 `backend/bdo.db` SHA-256: `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
- 실제 DB 변경: 없음

## 명시적 제외

전체 Cooking/Alchemy recipe catalog, recipe search, market API, profit calculator, silver/hour, 현재 box 수익·margin ranking, 인장 은화 가치표, 장비 optimizer, 연금석 architecture 변경, schema/migration, 새 user state, 새 Prompt mode/section, frontend architecture, scraper, runtime web search, LLM/API integration, Training, Sailing, Barter는 구현하지 않았다.

## 다음 milestone

V1.9F 결과를 기준으로 최신 main과 handoff를 다시 검토한 뒤 별도로 결정한다. Training practical strategy, Sailing/Barter practical strategy와 나머지 Milestone C content는 후보일 뿐 이 보고서에서 다음 버전 범위를 확정하지 않는다.