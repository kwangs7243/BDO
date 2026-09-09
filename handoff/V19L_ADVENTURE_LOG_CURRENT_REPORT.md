# V1.9L — Adventure Log Current Catalog & Reward Reconciliation

기준일: 2026-09-09 (KR live)

## 결과

V1.7D의 `adventure-log-foundation`, `igor-bartali-adventure-log`, `book-of-margahan` stable identity를 유지하면서 공식 모험일지 책장의 현행 카탈로그와 대표 progression·보상 정보를 보완했다. 스키마, migration, backend/frontend application code와 UI는 변경하지 않았다.

## 데이터 변화

| 항목 | V1.9K | V1.9L | 변화 |
| --- | ---: | ---: | ---: |
| Source | 180 | 182 | +2 |
| Content | 280 | 294 | +14 |
| active Content | 280 | 294 | +14 |
| FACT | 250 | 279 | +29 |
| STRATEGY | 63 | 63 | 0 |
| MEASUREMENT | 11 | 11 | 0 |
| Relation | 500 | 521 | +21 |

## Source 처리

신규 Source는 `emma-bartali-log-update-2026-07-29`, `justin-bartali-log-update-2025-11-19` 두 건이다. 기존 stable Source ID와 URL은 유지했다.

- `adventure-log-bookshelf-guide`: [모험일지 책장](https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=313). 현재 책장 10개 그룹, 대표 해금 조건과 공식 보상 표의 기준이다.
- `combat-system-rework-2025-07-23`: [2025-07-23 업데이트 안내](https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=14289). 이벤트 일지를 제외한 핵심 능력치 보상이 이고르 바탈리의 모험일지로 통합된 변경의 기준이다.
- `hyperboost-progression-2026`: [2026 하이퍼 부스트](https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15920). 현재 이고르 바탈리 AP +6 / DP +6과 엠마 강화 지원의 보조 근거다.
- `emma-bartali-log-update-2026-07-29`: [2026-07-29 업데이트 안내](https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=15966). 엠마 바탈리 기록일지 13장 선행 조건과 보상의 직접 근거다.
- `justin-bartali-log-update-2025-11-19`: [2025-11-19 업데이트 안내](https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=14803). 저스틴 바탈리의 해금 조건, I~XVII의 17개 진행 단위, 장별 보상과 최종 완료 보상의 직접 근거다.
- `known-issues-current-2026-09-04`: [알려진 문제점](https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=2989). 엠마 바탈리 기록일지의 구미호 9재시니 위치 표기 문제만 별도 `needs_review` claim으로 소유한다.

현재 책장 가이드의 권별 과거 능력치 배치는 2025-07-23 통합 이전 정보가 섞여 있으므로 현재 AP/DP 총량 근거로 사용하지 않았다. 이 충돌 경계를 Source notes와 superseded Evidence에 기록했다.

## 기존 Content 갱신

- `adventure-log-foundation`: 공식 책장 기준 10개 그룹(상시 9개, 이벤트 1개)과 그룹 목록을 반영했다.
- `igor-bartali-adventure-log`: 15권, 현재 AP +6 / DP +6, 2025-07-23 능력치 통합을 current FACT로 유지했다. 과거 분산 배치는 inactive/superseded 상태로 보존했다.
- `book-of-margahan`: 아그리스 열기 강화 역할과 기존 stable 요구사항·단계·보상 ID를 유지하고 현재 공식 Evidence를 연결했다.

기존 Content ID, nested seed key와 기존 Evidence Source 연결은 임시 V1.9K → V1.9L import 회귀에서 보존됨을 확인했다.

## 신규 Content

- `rulupee-travel-log`
- `lamute-gang-adventure-log`
- `caphras-record`
- `fughar-success-era`
- `herald-journal`
- `pavino-greko-miscellany`
- `deve-encyclopedia`
- `alustin-alchemy-journal`
- `dorin-morgrim-secret-journal`
- `morning-land-boss-codex`
- `morning-land-story-codex`
- `adventurer-strange-scenery`
- `justin-bartali-adventure-log`
- `emma-bartali-record-log`

각 Content는 summary/purpose, 대표 해금 조건, 최소 lifecycle step, 확인 가능한 보상, Relation과 claim별 Evidence를 갖는다. 저스틴 바탈리는 2025-11-19 공식 패치에 따라 I~XVII의 17개 진행 단위와 아이템 획득 증가 주문서 12개, 플로린 비법서 9개, 중간 칭호 7종, 봉인된 전투·생활의 서(각 7일), 크론석 300개를 집계 Reward로 반영했다. 최종 완료 보상인 칭호 `집 나간 자식`과 `저스틴 바탈리의 보증서`도 별도 Reward로 기록했다. 아침의 나라 우두머리 도감은 검은사당 주간 시도/보상 Content와 분리했고, 이야기 도감은 능력치 progression이 아닌 story replay/archive 성격을 명시했다.

엠마 바탈리 기록일지는 공식 패치의 13장 선행 progression과 8개 보상 행을 구조화했다. 구미호 9재시니 위치 표기 오류는 progression FACT를 덮지 않고 `common_mistakes` Section의 `needs_review` Evidence로 분리했다.

## 의도적으로 제외한 범위

- 이벤트 모험일지의 전체 목록과 종료된 보상
- 모든 모험일지의 장별 공략·좌표·NPC 동선
- 공식 근거가 부족한 수치, 동적 가치와 효율 순위
- Justin Bartali와 Olvia Academy의 별도 Deep Pack
- 아침의 나라 이야기 도감의 모든 분기·지식 목록
- schema, migration, UI, Prompt Bridge 기능 변경

따라서 `adventure logs` 전체 Deep Pack task는 완료 처리하지 않았다.

## 검증

- V1.9L semantic tests: 8 passed
- Backend: 324 passed
- Frontend typecheck: passed
- Frontend lint: passed
- Frontend tests: 14 files / 57 passed
- Frontend production build: passed
- migration 0001 → 0002 → 0003, V1.9K baseline import, V1.9L import와 2회 재import: passed
- 기존 Content/nested ID, Justin Reward ID, checklist history, UserContentState, UserMaterialInventory, UserProjectStageState 보존: passed
- unknown Source/Content relation reference: 0
- active Content: 294 / 294

## 실제 DB 보호

작업 시작 시 실제 `backend/bdo.db` SHA-256은 `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`였다. 지시서에 기록된 `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`와는 작업 전부터 달랐으므로 사용자 상태를 되돌리거나 덮어쓰지 않았다. 모든 import 검증은 임시 DB에서 수행했으며 작업 후에도 시작 시 실제 SHA `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`가 그대로 유지되었다.
