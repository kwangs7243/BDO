# V1.9E — Life Strategy Deep Pack II 완료 보고

## Git 기준

- 기준일: 2026-09-06
- 조사 및 검증일: 2026-09-06
- Source of Truth: main @ 7d6b5232892400dc248858064c19d88f4d24c5c0
- 작업 branch: feature/v1.9e-life-strategy-deep2
- 구현 commit: 이 파일의 Git history와 최종 작업 보고 참조

## 완료 범위

재배와 가공의 기존 current-system FACT를 복제하지 않고, 목적과 병목에 따라 다음 행동을 고르는 onboarding/strategy Content를 추가했다.

1. farming-onboarding-strategy
2. processing-onboarding-strategy

기존 farming-current-cycle에는 2026-06-10 공식 후속 패치로 확인한 조류 피해 감소 FACT만 stable seed key로 추가했다. 스키마, migration, Project 모델, Prompt mode, frontend component와 실제 DB는 변경하지 않았다.

## 수치

- Source: 150 → 155, 신규 5
- Content: 262 → 264, 신규 2, 기존 Content 수정 1
- active Content: 264
- FACT requirement: 193 → 194, 신규 1
- STRATEGY requirement: 23 → 31, 신규 8
- MEASUREMENT requirement: 11 → 11, 신규 0
- V1.9E 신규 Content Requirement: 8
- V1.9E 신규 Content Step: 16
- V1.9E 신규 Content Section: 6
- V1.9E 신규 Content Relation: 14
- 전체 Relation row: 415 → 429
- V1.9E 신규 Content claim Evidence: 34
- farming-current-cycle 신규 claim Evidence: 1
- 전체 Evidence status: verified 981, superseded 52, community_consensus 1, needs_review 31, conflict 2
- 신규 conflict / superseded: 0 / 0

## Farming FACT 재검증

현재 재배 기반은 공식 모험가 가이드와 2026년 패치 흐름을 함께 확인했다.

- [재배 가이드](https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=94)
- [2026-05-29 재배 개편 사전 안내](https://www.kr.playblackdesert.com/News/Notice/Detail?groupContentNo=15670&countryType=ko-KR)
- [2026-06-04 재배 개편](https://www.kr.playblackdesert.com/News/Notice/Detail?groupContentNo=15694&countryType=ko-KR)
- [2026-06-10 후속 조정](https://www.kr.playblackdesert.com/News/Notice/Detail?groupContentNo=15720&countryType=ko-KR)
- [2026-06-17 두더지 후속 조정](https://www.kr.playblackdesert.com/News/Notice/Detail?groupContentNo=15751&countryType=ko-KR)

6월 10일 공지의 조류 공격 1회당 작물 건강 감소량 약 4.16% → 약 0.25%를 farming-current-cycle.bird-damage에 현재 FACT와 이전 값을 함께 기록했다. 기존 canonical claim을 교체한 것이 아니라 누락된 후속 규칙을 추가한 것이므로 새 superseded evidence는 만들지 않았다.

7월과 8월 후속 패치도 검색해 재배 의미 변경 여부를 확인했다. 8월 5일의 울타리 목록 정렬 수정 외에는 이번 onboarding 판단을 대체할 더 최신 규칙을 찾지 못했다.

## Farming strategy

커뮤니티 자료는 authoritative FACT가 아니라 실제 운용 맥락을 보조하는 STRATEGY Source로 분리했다.

- [재배 목적과 활용 흐름](https://blackdesertonlineyoutube.tistory.com/223) — 검사학개론, 2025-09-15
- [재배 입문 흐름](https://blackdesertonlineyoutube.tistory.com/226) — 검사학개론, 2025-09-21

다음 판단을 구조화했다.

- 먼저 직접 사용, 요리·연금 재료, 품종 개량, 부산물 등 목적을 고른다.
- 수확과 품종 개량은 목적이 다르므로 보편적인 단일 행동으로 고정하지 않는다.
- 위치는 온도·습도 같은 작물 조건, 접근성, 울타리 회수와 관리 동선을 함께 본다.
- 씨앗, 울타리, 기운, 병충해·가지치기와 수확 주기를 첫 운영 병목으로 점검한다.
- universal_best_crop, universal_best_action, universal_best_location을 모두 false로 명시했다.
- 실시간 거래소 순위, 작물별 현재 수익과 고정 효율 수치는 seed에서 제외했다.

커뮤니티 글의 과거 비료 설명은 2026 공식 개편보다 오래된 값이므로 current FACT로 채택하지 않았다.

## Processing FACT 재검증

가공 기반과 후속 변경은 다음 공식 자료로 확인했다.

- [가공 가이드](https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98)
- [2026-03-18 가공 UI 개선](https://www.kr.playblackdesert.com/News/Notice/Detail?groupContentNo=15332&countryType=ko-KR)
- [2026-07-22 대량 가공식 추가](https://www.kr.playblackdesert.com/News/Notice/Detail?groupContentNo=15905&countryType=ko-KR)
- [2026-09-02 생활 장비 통합](https://www.kr.playblackdesert.com/News/Notice/Detail?groupContentNo=16141&countryType=ko-KR)
- [현재 알려진 문제](https://www.kr.playblackdesert.com/News/Notice/Detail?groupContentNo=2989&countryType=ko-KR)

2026-09-06 기준 현재 알려진 문제에는 가공(L)-공작으로 카나페 매듭 제작 시 요리사의 모자를 사용할 수 없는 문제가 있고, 2026-09-09 수정 예정으로 공지되어 있다. processing-onboarding-strategy에는 현재 알려진 문제와 재확인 시점을 기록했으며, 수정 완료 전 확정된 영구 규칙으로 일반화하지 않았다.

기존 processing-current-system과 mass-processing FACT를 공식 가이드 및 3월·7월 변경과 대조했으며, 이번 범위에서 교체할 상충 current claim은 확인되지 않아 수정하지 않았다. 9월 2일 생활 장비 통합 영향은 기존 life-common-gear와 life-mastery 계열 Content를 재사용하고 onboarding Relation으로 연결했으며 동일 장비 FACT를 복제하지 않았다.

## Processing strategy

- [가공·무역 경로 운용 사례](https://www.inven.co.kr/board/black/3584/58481) — 인벤 커뮤니티, 2026-01-21

다음 판단을 구조화했다.

- 결과물의 직접 사용, Project 재료, 공방 투입, 재고 변환 또는 판매 목적을 먼저 고른다.
- 소량 시험과 경로 확인에는 일반 가공, 지원 레시피와 장비·숙련이 확인된 반복 대량 작업에는 대량 가공을 검토한다.
- 원재료 → 가공 방식 → 결과물 → 후속 사용처를 현재 제작 노트와 가공 UI에서 확인한다.
- 재료 재고, 무게, 가방·창고 공간, 성공과 후속 소비를 세션 병목으로 기록한다.
- 고정 수량 임계값이나 보편적인 최적 모드는 두지 않았다.
- 동적 거래소 가격, 마진, silver/hour와 수익 순위는 제외했다.

2020년 공식 포럼 가공 글은 현재 장비·UI·레시피 판단에 사용하기에는 오래되어 채택하지 않았다.

## Evidence 전략

- 신규 Content의 summary와 purpose, 모든 Requirement, Step, Section에 claim 단위 Evidence를 연결했다.
- Requirement는 description, Step은 description, Section은 body claim key를 사용한다.
- 공식 Source는 현재 시스템 경계와 변경 사실을, community Source는 조건부 선택과 실제 운용 맥락을 담당한다.
- 신규 Requirement 8개는 모두 knowledge_role=strategy다.
- farming-current-cycle.bird-damage만 knowledge_role=fact다.
- 신규 community Source를 official source_type으로 저장하지 않았다.
- 전체 source_id와 content slug는 고유하며, Evidence의 unknown Source 참조는 0이다.

## Life mapping

backend/app/life.py의 presentation mapping만 변경했다.

- farming getting_started: farming-current-cycle 다음에 farming-onboarding-strategy
- processing getting_started: processing-current-system 다음에 processing-onboarding-strategy

게임 사실이나 전략 본문은 Python에 하드코딩하지 않았다. GET /api/life와 두 분야 detail에서 신규 Content를 발견하며 기존 10개 생활 분야와 section 중복 제거 규칙은 유지된다.

## Prompt Bridge

새 mode, collector 또는 renderer를 추가하지 않았다. 두 신규 Content는 V1.9D에서 확정한 일반 Content role semantics에 따라 content_onboarding, next_action, verify_latest에서 동작한다. FACT, STRATEGY와 MEASUREMENT의 역할 분리를 유지하며 현재 Evidence가 있는 strategy claim은 canonical verified 항목으로 분류된다.

## Semantic / import regression

backend/tests/test_life_strategy_deep2_seed.py에 9개 테스트를 추가했다.

- Source ID·URL, Content slug 고유성과 Evidence Source 참조 무결성
- 재배 2026 FACT audit와 조류 피해 후속 패치
- 신규 stable seed key와 Requirement/Step/Section Evidence coverage
- 재배 목적·수확/품종 개량·위치·주기 병목과 universal-best 금지
- 가공 목적·일반/대량 선택·경로 검증·세션 병목·현재 알려진 문제
- official/community source_type 분리와 동적 경제 값 제외
- Life Hub/Detail 노출 순서
- content_onboarding, next_action, verify_latest Prompt role 보존
- migration 0001 → head, baseline import → V1.9E import → 2회 재import
- 기존 Content/nested ID, checklist history, UserContentState, UserMaterialInventory와 UserProjectStageState 보존

V1.7B/C 임시 baseline fixture는 후속 Content가 해당 milestone에서 도입된 Source를 재사용하면 Source만 제거해 참조 무결성이 깨졌다. 원래 milestone Content 제외와 stable ID/history 회귀는 유지하면서, baseline Content가 실제 참조하는 Source는 보존하도록 일반화했다. 대상 회귀 결과는 2 passed다.

## 전체 검증

### Backend

- uv run pytest tests/test_life_strategy_deep2_seed.py -q
  - 9 passed, 1 warning
- uv run pytest -q
  - 268 passed, 1 warning
- warning은 기존 Starlette TestClient의 httpx2 전환 안내다.

### Frontend

- npm.cmd run typecheck — passed
- npm.cmd run lint — passed
- npm.cmd run test -- --run — 14 files / 57 tests passed
- npm.cmd run build — passed, 41 modules transformed

### 공통 및 DB

- git diff --check — passed
- 작업 전 backend/bdo.db SHA-256:
  E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5
- 작업 후 backend/bdo.db SHA-256:
  E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5
- 동일 여부: 동일

## 명시적 제외

- Cooking, Alchemy, Training, Sailing, Barter
- 모든 레시피 catalog
- 실시간 시장 가격, profit calculator, silver/hour, dynamic economy ranking
- schema, migration, 새 Prompt mode, 새 frontend architecture
- runtime scraper, external API, LLM integration, actual DB mutation

## 다음 milestone

V1.9F — Cooking / Alchemy Strategy Deep Pack은 이번 작업에서 구현하지 않았다. 레시피, 대체 재료, 조달, 황실 납품, 생산 시간, 숙련과 연금 재료 체인은 별도 milestone 범위로 유지한다.
