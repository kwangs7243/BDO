# V1.9C — Life Strategy Deep Pack I 완료 보고

## Git 기준

- 기준일: 2026-09-06
- Source of Truth: main @ 50f0d859d25037e98822a6e9ddb7db3bc72668e2
- 작업 branch: feature/v1.9c-life-strategy-deep1
- 구현 commit: 이 파일의 Git history와 최종 작업 보고 참조

## 완료 범위

채집, 낚시, 수렵에 기존 current-system FACT를 복제하지 않는 onboarding/strategy Content를 추가했다.

1. gathering-onboarding-strategy
2. fishing-onboarding-strategy
3. hunting-onboarding-strategy

세 Content는 목적 선택, 첫 세션 준비, 조건부 동선·모드 판단과 다음 단계만 담당한다. 스키마, migration, Project, 사용자 상태 모델, Prompt mode, frontend component는 변경하지 않았다.

## 수치

- Source: 145 → 150, 신규 5
- Content: 259 → 262, 신규 3, 기존 Content 수정 0
- active Content: 262
- FACT requirement: 193 → 193, 신규 0
- STRATEGY requirement: 17 → 23, 신규 6
- MEASUREMENT requirement: 11 → 11, 신규 0
- V1.9C Section: strategy 6, common_mistakes 3
- V1.9C Step: 21
- V1.9C Relation: 14
- 전체 Relation row: 401 → 415
- V1.9C claim 선언: 42
- V1.9C source별 Evidence row: 88
- 전체 Evidence row: 1237 → 1325
- 신규 conflict / superseded: 0 / 0

## FACT 조사 자료

현재 사실은 다음 KR 공식 모험가 가이드를 기준으로 다시 확인했다. 기존 Source row가 있어 재사용했다.

- [채집](https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=97) — gathering-guide
- [낚시 기초](https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=107) — fishing-basic-guide
- [낚시 고급](https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=108) — fishing-advanced-guide
- [수렵](https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=106) — hunting-guide

채집 방식·도구, 낚시 잠재력·방생·처분, 일반·저격·협동 수렵과 처치 후 도축 같은 사실은 기존 current-system 계열 Content의 책임으로 유지했다. 이번 조사에서 해당 current FACT를 고칠 근거가 발견되지 않아 기존 Content와 evidence는 변경하지 않았다.

## STRATEGY 조사 자료

신규 Source row 5개를 community 계열로 명시적으로 분리했다.

- [노스토스의 별 추천 채집 장소](https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=152319) — 만두집아들I검사학개론, 2026-05-24
- [낚시가이드](https://blackdesertonlineyoutube.tistory.com/176) — 검사학개론, 2024-12-05
- [Can you AFK Fish for a week?](https://www.reddit.com/r/blackdesertonline/comments/1j8fr6g) — Reddit r/blackdesertonline, 2025-03-11
- [사자 수렵의 모든것](https://blackdesertonlineyoutube.tistory.com/167) — 검사학개론, 2024-10-15
- [Shadow Lion Hunting Guide 2026 Edition](https://www.reddit.com/r/blackdesertonline/comments/1ubwz7j/shadow_lion_hunting_guide_2026_edition/) — Reddit r/blackdesertonline, 2026-06-21

검사학개론의 실제 사용 글은 채집 장소 1건, 낚시 입문 1건, 사자 수렵 1건이다. 모두 authoritative FACT가 아니라 supporting STRATEGY로 사용했다. 일반화 가능한 판단은 공식 가이드와 함께 연결했고, 낚시 장시간 세션 병목과 사자 계열 상위 수렵 사례는 서로 다른 Reddit 커뮤니티 자료로 추가 교차 확인했다.

## 제외 및 historical 자료

- 검사학개론의 2023 자동 낚시 감소율 표는 과거 exact 수치이므로 채택하지 않았다.
- 주간 낚시 대회의 특정 주차 어종·장소를 다룬 커뮤니티 자료는 회전 값이므로 정적 seed에서 제외했다.
- 2024 사자 수렵 글의 장비, 수정, 버프 exact 세팅은 2026 current FACT로 복사하지 않았다.
- 동적 거래소 가격, 시간당 수익, 실시간 어종, 효율 순위와 확률 표본은 MEASUREMENT 또는 후속 research 범위로 남겼다.

신규 superseded row는 만들지 않았다. 채택하지 않은 과거 수치가 기존 canonical claim을 대체한 것이 아니므로 research rejection으로만 기록했다.

## Gathering

- 목표 재료·제작/프로젝트 필요·생활 성장 중 목적을 먼저 고른다.
- 대상에 맞는 채집 방식과 도구를 기존 current-system과 gathering-tools에서 확인한다.
- 동선은 개체 밀도만이 아니라 이동 거리, 재생 흐름, 창고 접근, 무게와 캐릭터 이동 편의를 함께 비교한다.
- 커뮤니티 동선을 보편적인 단일 답으로 저장하지 않았다.
- 7개 first-time/preparation/maintenance Step과 3개 전략·실수 Section을 추가했다.

## Fishing

- AFK 자동 낚시, 직접 조작, 주간 대회를 서로 다른 목적으로 구분했다.
- 가방, 낚싯대 내구도, 자동 낚시 시간, 방생 기준과 처분 경로를 세션 병목으로 함께 본다.
- 주간 대회의 현재 회전 어종·장소는 fishing-encyclopedia-and-weekly-contest에서 최신 값을 확인하도록 Relation만 연결했다.
- auto-fishing, fish-freshness-and-trade, imperial-fishing-delivery와 기존 Content를 재사용했다.
- 8개 Step과 3개 전략·실수 Section을 추가했다.

## Hunting

- 일반 개인 수렵, 저격 수렵, 협동 수렵을 준비와 조작이 다른 선택지로 구분했다.
- 개인 수렵에서 장전·사격·이동·회피와 처치 후 도축을 익힌 뒤 다음 모드를 검토한다.
- 사자 수렵은 advanced example이며 입문자에게 공통으로 적용되는 대상이나 순서로 저장하지 않았다.
- hunting-firearms, sniper-hunting, life-mastery-foundation과 기존 Content를 재사용했다.
- 6개 Step과 3개 전략·실수 Section을 추가했다.

## Evidence 전략

- 각 Content의 summary와 purpose에 claim evidence를 연결했다.
- 모든 신규 Requirement, Step, Section에 claim 단위 evidence가 있다.
- Prompt Bridge의 기존 계약에 맞춰 summary, purpose, description, body claim key를 사용했다.
- 공식 자료는 시스템 경계와 준비 사실을, community 자료는 조건부 선택과 실제 운용 맥락을 뒷받침한다.
- 신규 Requirement는 모두 knowledge_role=strategy다.
- community Source를 official source_type으로 저장하지 않았다.

## Life mapping

backend/app/life.py의 presentation mapping만 변경했다.

- gathering getting_started: gathering-current-system 다음에 gathering-onboarding-strategy
- fishing getting_started: fishing-current-system 다음에 fishing-onboarding-strategy
- hunting getting_started: hunting-current-system 다음에 hunting-onboarding-strategy

게임 사실이나 전략 본문은 Python에 하드코딩하지 않았다. GET /api/life와 세 분야 detail에서 신규 Content를 발견하며 10개 생활 분야와 section 중복 제거 규칙은 유지된다.

## Prompt Bridge

새 mode, collector 또는 renderer를 추가하지 않았다. 세 Content는 기존 일반 Content 계약으로 content_onboarding, next_action, verify_latest에서 동작한다. 신규 claim은 현재 evidence가 존재하므로 canonical verified 항목으로 분류되며 unresolved에는 실제 미검증 claim만 들어간다.

## Semantic / import regression

backend/tests/test_life_strategy_deep1_seed.py에 11개 테스트를 추가했다.

- 지시서의 global, Gathering, Fishing, Hunting semantic 검증 25개 항목
- 신규 ID, URL, slug와 source reference 무결성
- seed_key 범위와 모든 Requirement/Step/Section evidence 연결
- FACT/STRATEGY 책임 분리와 동적 값·주간 회전 값 제외
- Life Hub/Detail discovery와 10개 분야 유지
- 기존 Prompt Bridge 세 mode 호환
- migration 0001 → head
- V1.9B baseline import → V1.9C import → 재import
- 기존 Content/Requirement ID와 신규 Content ID 안정성
- checklist history, UserContentState, UserMaterialInventory, UserProjectStageState 보존
- 기존 inactive/archive 의미 보존

전용 결과: 11 passed.

기존 Carrack 테스트의 Source/Content/Evidence/Relation 전체 총량 equality는 V1.9B snapshot이어서 V1.9C 확장을 막았다. Carrack Project 1개, Stage 4개, Material/Projection/Source 각 9개와 나머지 semantic 검증은 유지하고 네 전역 총량만 V1.9B 최소 baseline 이상으로 바꿨다.

## 전체 검증

### Backend

- uv run pytest tests/test_life_strategy_deep1_seed.py -q
  - 11 passed
- uv run pytest -q
  - 244 passed, 1 warning
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

## 다음 Life gap

후속 후보를 V1.9C에서 구현하지 않았다.

- V1.9D 후보: Farming strategy, Processing strategy, Cooking/Alchemy workflow
- 이후: Training, Sailing/Barter practical strategy, Nodes/workers recommendation
- 별도 계층: measurement/economy와 동적 시장 데이터

이 목록은 handoff gap이며 후속 milestone의 확정 범위가 아니다.
