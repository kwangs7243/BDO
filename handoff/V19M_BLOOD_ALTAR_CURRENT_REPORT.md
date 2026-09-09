# V1.9M — Blood Altar 22–24 Current System Closure Report

기준일: 2026-09-09 KR Live
Branch: `feature/v1.9m-blood-altar-current`
Source of Truth: `main@559eb2d88664c17eb8af55a8710c298274514f93`

## 결과

기존 `blood-altar` Content와 stable nested identity를 유지하면서 피의 제단을 현재 최대 24단계 기준으로 갱신했다. 22~24단계의 공식 능력치와 주간·최초 클리어 보상을 query 가능한 FACT로 추가했고, 심연의 환상 1~3은 2026-09-09 이후 current 난이도가 아님을 명시했다.

- current max stage: 24
- added stages: 22, 23, 24
- removed current difficulties: abyss_illusion_1, abyss_illusion_2, abyss_illusion_3
- party challenge allowance: 한 파티 세션당 10회
- weekly entry: 제한 없음
- weekly reward: 가문당 주 1회, 해당 주 최고 단계만 산정, 비누적
- payout: 일요일 00:00 KST `reward_payout`
- first-clear reward: 주간 보상과 별도

## 22~24단계 능력치

| 단계 | 권장 AP | 권장 DP | 권장 최종 AP | 권장 최종 DP |
| --- | ---: | ---: | ---: | ---: |
| 22 | 405 | 465 | 2110 | 810 |
| 23 | 410 | 470 | 2200 | 815 |
| 24 | 415 | 475 | 2290 | 820 |

## 보상 모델

정확한 공식 표는 `blood-altar.high-tier-current` Requirement의 `structured_value.stages`에 보존했다.

- 주간 보상은 `chance_based`와 `quantity_guaranteed`를 분리했다.
- 범위형 수량은 `min_amount` / `max_amount`로 보존했다.
- 금괴 상자는 상자 수량과 개봉 시 금괴 1kG 3~10개 범위를 분리했다.
- 최초 클리어는 단계별 확정 보상과 지식을 별도로 보존했다.
- 공식 표에 없는 확률 퍼센트와 기대값은 만들지 않았다.
- 기존 일반 주간·최초 클리어 Reward를 유지하고, 22~24단계용 6개 UI-facing bundle Reward를 추가했다.

## Source와 claim 경계

### 현재 공식 가이드

- ID: `blood-altar-guide`
- URL: https://www.kr.playblackdesert.com/ko-kr/Wiki?wikiNo=168
- 계속 사용하는 범위: 3인 협동, 최고 기록 유지, 주간 입장 제한 없음, 최고 단계 주간 보상, 일요일 00:00 지급, 최초 클리어 보상 등 일반 mechanics
- current 근거로 사용하지 않는 범위: 21단계 상한, 파티당 5회, 심연의 환상 현행 난이도 표기

Source 전체를 superseded 처리하지 않고 Evidence claim을 일반 mechanics로 제한했다.

### 2026-07-15 공식 패치

- ID: `blood-altar-challenge-2026-07-15`
- URL: https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=15878
- 파티당 도전 가능 횟수 5→10, 10회 소진 뒤 자동 퇴장, 주간 입장 제한 없음의 current 근거다.

### 2026-09-09 공식 패치

- ID: `blood-altar-high-tier-2026-09-09`
- URL: https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=16163
- 22~24단계 추가, current max 24, 능력치·보상, 심연의 환상 1~3 삭제의 current 근거다.
- volatile 최종 수정 시각을 Source title에 고정하지 않고 `9월 9일(수) 업데이트 안내`로 저장했다.

## 일회성 전환 조치

2026-09-06 00:00부터 2026-09-09 정기점검 전까지 제거 직전 심연의 환상 완료자에게 적용된 보상 조치는 역사적 전환 정보다. current recurring ScheduleRule, checklist 또는 Reward로 만들지 않았다.

## Baseline

| 항목 | V1.9L | V1.9M |
| --- | ---: | ---: |
| Source | 182 | 183 |
| Content | 294 | 294 |
| FACT | 279 | 280 |
| STRATEGY | 63 | 63 |
| MEASUREMENT | 11 | 11 |
| Relation | 521 | 521 |

- active Content: 294
- 신규 Content: 0
- 신규 Requirement: 1
- 신규 Reward: 6
- schema/migration/frontend architecture 변경: 없음

## Historical import와 identity 보존

임시 SQLite에서 migration `20260902_0001 → head` 후 synthetic V1.9L seed를 import하고 V1.9M을 세 번 연속 적용했다.

- 기존 294 Content ID: 보존
- 기존 `blood-altar` Content ID: 보존
- 기존 Blood Altar Requirement/Step/Reward/Section/Schedule/Checklist/Relation/Evidence ID: 보존
- 기존 checklist history: 보존
- `UserContentState`: 보존
- `UserMaterialInventory`: 보존
- `UserProjectStageState`: 보존
- 신규 Requirement/Reward/Evidence ID: 두 차례 재import 뒤 동일
- unexpected archive: 없음
- unknown Source reference: 없음
- unknown Relation target: 없음

## Prompt Bridge

기존 `PromptContextBundle` 계약과 local-only 경계를 변경하지 않았다.

`content_onboarding`과 `verify_latest`에서 다음을 회귀 검증한다.

- current 24단계
- 22/23/24의 공식 권장·최종 능력치
- 심연의 환상 1~3 삭제 경계
- 파티당 도전 10회
- 21단계를 current FACT로 표시하지 않음

Requirement의 queryable exact table은 `structured_value`에, Prompt Bridge의 기존 description-claim 계약이 사용하는 요약 수치는 `description`에 유지하고 각각 공식 패치 Evidence를 연결했다.

## 검증

- V1.9M semantic: 7 passed
- Blood Altar / Content API / Prompt Bridge / V1.9L 포함 targeted: 35 passed
- backend collect: 331
- backend full: 331 passed, 1 existing warning
- frontend typecheck: passed
- frontend lint: passed
- frontend tests: 14 files / 57 passed
- frontend build: passed
- `git diff --check`: passed
- actual `backend/bdo.db` SHA-256 pre: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- actual `backend/bdo.db` SHA-256 post: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`

## 범위 밖

추가하지 않았다.

- 클래스별 전략, 최적 파티, 클리어 시간, 수익·기대값
- 단계별 사용자 진행 schema
- 새 UI 또는 frontend architecture
- schema/migration
- OpenAI API, MCP, Notion 연동
- recurring 형태의 일회성 전환 보상

## 다음 우선 후보

V1.9M 이후 최우선 후보는 **흑정령의 일정 관리표**다. 이 보고서는 후보만 기록하며 다음 milestone 범위를 정의하거나 구현하지 않는다.