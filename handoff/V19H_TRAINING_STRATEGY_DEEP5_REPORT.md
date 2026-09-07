# V1.9H — Training Practical Strategy Deep Pack Report

## 기준

- 조사 및 구현 기준일: 2026-09-07 (KR)
- Source of Truth: `main` @ `8a51610648ed4b87bec222e14863eb21187912b9`
- 작업 branch: `feature/v1.9h-training-strategy`
- 신규 schema / migration / frontend 기능: 없음

## 완료 범위

기존 조련 canonical FACT를 복제하지 않고, 현재 목표와 보유 말·마구간 상태를 기준으로 다음 행동을 고르는 입문 Strategy Content를 추가했다.

- 신규 Content: `training-onboarding-strategy`
- 기존 Content 보완: `dream-horse-material-routines`
- Life Hub 조련 `getting_started` 순서에 신규 Strategy 연결
- V1.9G historical snapshot 회귀가 후속 pack 확장을 허용하도록 최소값 및 V1.9G 고유 semantic assertion으로 정리

새 Strategy는 다음 판단 흐름을 담당한다.

1. 현재 목표와 말·마구간 상태를 먼저 기록한다.
2. 야생마 포획이 필요한지, 보유 말 육성이 먼저인지 구분한다.
3. 교배·교환·황실 납품 중 현재 목표에 맞는 출구를 선택한다.
4. 준마·환상마·꿈결 환상마 progression은 입문 기본값이 아닌 조건부 상위 단계로 분리한다.
5. 직접 조작과 장시간 이동 같은 세션 성격을 구분한다.
6. 한 번에 하나의 병목만 개선하고 다음 세션에서 다시 판단한다.

## Source와 FACT audit

### 2026-07-15 야생마 개체 수 증가

공식 업데이트에서 야생마 서식지의 개체 수 증가를 확인했다. 기존 `wild-horse-capture`가 이미 `population_increased_at=2026-07-15`와 공식 Evidence를 소유하므로 stable Content를 변경하지 않았다.

### 2026-07-22 고비 뿌리 교환

기존 stable Source `processing-mass-recipes-2026-07-22`의 ID와 URL을 유지하고, 공식 업데이트의 복수 역할을 드러내도록 notes만 domain-neutral하게 보완했다.

`dream-horse-material-routines`에는 남는 고비 뿌리 3개를 와프라에게 다음 중 하나로 교환하는 FACT Requirement를 추가했다.

- 돌꼬리 여물 1개
- 바람결 소라해초 1개
- 짙푸른 발굽뿌리 1개

Requirement는 현재 환상마 재료가 더 필요한 경우의 조건부 선택으로 표현했다. 기존 Content 및 nested stable identity는 유지했다.

### 2026-09-02 생활 장비 통합

기존 `life-common-gear`와 `life-artifacts-lightstones`의 current FACT와 Evidence가 최신 공식 패치를 이미 반영하고 있어 변경하지 않았다.

### 커뮤니티 Strategy Source

신규 Source `training-beginner-decisions-2026-02-05`는 초보자가 포획·육성·교배·납품 사이에서 겪는 선택 문제를 확인하는 용도로만 사용했다. 답변의 정확한 수치, 특정 세대·레벨 결론 또는 범용 추천은 FACT로 채택하지 않았다.

## Evidence와 지식 역할

- 신규 Content의 Requirement 6개는 모두 `knowledge_role=strategy`
- 신규 claim Evidence declaration: 21
- expanded Source links: 40
- 공식 Source는 기존 시스템·선행조건·보상 및 교환 FACT의 lineage에 사용
- 커뮤니티 Source는 조건부 의사결정 Strategy에만 사용
- `content_onboarding`, `next_action`, `verify_latest` Prompt mode에서 신규 Requirement·Step·Section이 STRATEGY로 유지되는 것을 검증
- 임시 이벤트 보너스와 종료일은 canonical seed에서 제외

## Relations

신규 Strategy를 다음 기존 Content 10개와 연결했다.

- `training-current-system`
- `training-mastery-effects`
- `wild-horse-capture`
- `horse-breeding-exchange`
- `horse-imperial-delivery`
- `courser-system`
- `dream-horse-awakening`
- `mythical-dream-horse`
- `training-growth-surprise-quest`
- `dream-horse-material-routines`

## 수치

- Source: 164 → 165
- Content: 268 → 269
- active Content: 269
- FACT Requirement: 194 → 195
- STRATEGY Requirement: 51 → 57
- MEASUREMENT Requirement: 11 → 11
- Relation: 468 → 478
- 신규 Content Step: 10
- 신규 Content Section: 3
- 신규 Content Relation: 10

## Seed import와 이력 보존

V1.9G baseline 임시 SQLite DB에 사용자 및 checklist/project marker를 만든 뒤 V1.9H seed를 import하고 다시 한 번 재import했다.

- 기존 Content와 nested ID 보존
- 신규 Content/Requirement/Step/Section/Relation ID 재import 시 보존
- 기존 Evidence 및 사용자 이력 보존
- ChecklistInstance / ChecklistItemState 보존
- UserContentState 보존
- UserMaterialInventory / UserProjectStageState 보존
- Carrack Project canonical Material/Stage 보존
- canonical row 수와 Evidence 수 멱등
- 실제 `backend/bdo.db`는 사용하거나 변경하지 않음

## 제외 및 남은 조사 부채

이번 milestone에는 다음을 넣지 않았다.

- 임시 조련 이벤트의 경험치 보너스·보상·기간
- 실시간 시장가, 수익, 시간당 경험치 또는 효율
- 교배 기대값·스킬 습득 확률·각성 확률 계산기
- 범용 최적 말, 장소, 세대, 레벨 또는 장비 조합
- 전체 조련 recipe / measurement / economy 심화
- 새 checklist, schedule, reward, schema, migration, UI, Prompt mode

## 검증 결과

- V1.9H semantic/import tests: 9 passed
- V1.9C/E/F/G/H 지정 회귀: 47 passed
- Backend 전체: 295 passed
- Frontend typecheck: passed
- Frontend lint: passed
- Frontend tests: 14 files / 57 passed
- Frontend build: passed
- `git diff --check`: passed
- 기존 Starlette httpx deprecation warning 1건
- schema/migration: 변경 없음
- `backend/bdo.db` SHA-256 before/after:
  - `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
  - `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`