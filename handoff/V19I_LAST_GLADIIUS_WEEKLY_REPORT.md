# V1.9I — Last Gladiius Weekly Content Closure Report

## 기준

- Repository: `kwangs7243/BDO`
- Source of Truth: `main` @ `825e32eee48119ace754a396eaf2d5643e7f7242`
- 작업 branch: `feature/v1.9i-last-gladiius-weekly`
- 기준일: 2026-09-07 KR Live
- 실제 DB baseline SHA-256: `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`

## 완료 범위

신규 active Content `last-gladiius-weekly`를 추가했다. 최초 추천 의뢰와 반복 주간 우두머리를 하나의 규칙으로 합치지 않고, 사용자가 실제 주간 토벌을 시작하고 완료 보상을 기록할 수 있는 공식 FACT 흐름으로 구성했다.

- Requirement: 5개, 모두 `knowledge_role=fact`
- Step: 10개
- Reward: 10개
- Section: 3개
- Schedule: 목요일 00:00 KST `quest_reset` 1개
- Checklist: 주간 보상 획득 template 1개 / item 1개
- Relation: 2개
- claim Evidence 선언: 31개, 모두 current `verified`

## 추천 의뢰와 반복 주간 분리

최초 추천 의뢰는 레벨 60, 선행 의뢰, 50분 제한, 최초 완료 칭호 및 가문 1회 보상 문맥으로만 기록했다. 반복 주간은 붉은 심장의 솔 마기아에게 `[주간] 글라디우스 : 카이벨라 함`을 수주하고 별도 전투·보상 흐름을 진행한다. 추천 의뢰 완료는 반복 주간의 필수 조건으로 저장하지 않았다.

## Current FACT

- 권장 표기 공격력 330 / 추천 방어력 420
- 1인 콘텐츠, 엘비아 영역 진행 불가
- 2025-07-23 기준 공격력 제한 1000, 초과분 50% 적용 및 몬스터 방어력 6% 증가
- 심장 생명력 90%·70%·50%·30%에서 검은 환상 소환
- 환상 처치 후 심장 방어력 50초 감소
- 환상 처치에 따라 고대 장치 순차 점등, 전투 종료까지 유지
- 모든 환상 처치 후 추적 고대 병기 정지 및 심장 지속 공격 가능
- 주간 연속 의뢰 완료 시 `글라디우스 : 카이벨라 함` 1개

보상은 공식 문서의 고정 구성품 5종, 확률 보물 3종, `데키아의 진귀한 상자` 확률 데보레카 액세서리를 직접 보상과 분리해 기록했다. 확률 보상은 선택 보상으로 오분류하지 않았다.

## Source와 Evidence

### 재사용한 stable Source

- `ator-reset-patch` — 아토락시온 주간 의뢰 목요일 00:00 KST 초기화
- `combat-system-rework-2025-07-23` — 2025-07-23 방어력·공격력 제한 변경
- `gladius-2026` — 2026-01-28 고대 장치 점등 유지
- `gladius-balance-2026` — 2026-06-24 권장 공격력 및 환상·방어력 감소 기믹

기존 Source ID와 URL은 유지했다. 세 Gladius 사용처가 더 명확해지도록 발행일·수집일·region·notes를 보완했고, 전체 업데이트 문서인 `combat-system-rework-2025-07-23`의 title은 특정 domain에 종속되지 않는 공식 문서 제목으로 정규화했다.

### 신규 공식 Source

- `gladius-foundation-2025-05-28` — 도입, 추천/주간 분리, 진입, 능력치, 보상
- `gladius-quest-flow-2025-06-04` — 주간 수주 후 대화 진입 및 추천 의뢰 50분 제한
- `gladius-mechanics-2025-10-22` — 검은 환상 무적 조정, 전원 처치 후 병기 정지·심장 공격

동일 URL Source는 추가하지 않았으며 Source ID/URL은 모두 unique다. Requirement Evidence의 claim key는 기존 Content Prompt Bridge가 조회하는 `description`에 연결해 official verified FACT로 분류되도록 했다.

## 후속 패치 audit

2026-06-24 이후부터 2026-09-07까지 공식 KR 공지에서 최후의 글라디우스, 일레즈라, 아토마기아의 심장과 관련된 gameplay 변경을 확인했다. 권장 능력치, 주간 reset, 보상 또는 현재 전투 기믹을 다시 바꾸는 후속 공식 패치는 발견하지 못했다. 2026-08-26 성장 안내의 단순 콘텐츠 언급과 gameplay claim과 무관한 표시 문제는 canonical Source/FACT로 추가하지 않았다.

## Relation

현재 seed에는 바아마키아·시카라키아·요루나키아·오르제키아가 독립 Content slug가 아니라 `atoraxxion-weekly`의 Step으로 존재한다. 존재하지 않는 지역 slug를 만들지 않고 다음 stable Content만 연결했다.

- `atoraxxion-weekly`
- `weekly-quest-framework`

## Prompt Bridge

새 Prompt mode나 런타임 네트워크 호출은 추가하지 않았다.

- `content_onboarding`, `next_action`, `verify_latest`: 신규 summary/purpose/Requirement/Step/Section을 verified FACT로 분류
- `weekly_review`: 신규 주간 checklist 발견
- official Source metadata 유지
- unresolved claim은 없으며 `open_questions_or_conflicts`는 비어 있음

## 제외 범위

- 기존 네 아토락시온 요새 FACT 전체 재작성
- 클래스별 공략과 범용 최적 딜사이클
- 동적 수익, 시간당 효율, 보상 기대값과 확률 추정
- 독립 근거가 부족한 커뮤니티 Strategy
- 새 Prompt mode, UI, schema, migration

## 데이터 변화

- Source: 165 → 168
- Content: 269 → 270 active
- FACT Requirement: 195 → 200
- STRATEGY Requirement: 57 → 57
- MEASUREMENT Requirement: 11 → 11
- Relation: 478 → 480
- 신규 claim Evidence 선언: 31

## 임시 DB 검증

Alembic `20260902_0001` → `head`로 만든 임시 SQLite DB에서 V1.9H baseline seed를 적재하고 사용자/checklist/project marker를 생성한 뒤 V1.9I를 import하고 다시 reimport했다.

- 기존 Content 및 Requirement/Step/Schedule/Checklist stable ID 보존
- 신규 Content/Requirement/Step/Reward/Schedule/Checklist 및 item ID 보존
- Evidence ID와 canonical row count 멱등성 유지
- 기존 Checklist history와 완료 메모 보존
- `UserContentState`, `UserMaterialInventory`, `UserProjectStageState` 보존
- Carrack Project/Stage/Material state 보존
- 실제 `backend/bdo.db` 미사용

## 검증 결과

- V1.9I semantic/import tests: 8 passed
- V1.9H 지정 회귀 포함: 17 passed
- Backend 전체: 303 passed
- Frontend typecheck: passed
- Frontend lint: passed
- Frontend tests: 14 files / 57 passed
- Frontend build: passed
- `git diff --check`: passed
- 실제 DB SHA-256 전후 동일

기존 Starlette `TestClient` deprecation warning 1건 외 신규 warning은 없다.
