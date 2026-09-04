# V1.7D Account & Progression Foundation Report

기준 시점: 2026-09-04 KR Live
작업 범위: progression seed, semantic regression test, 검증 보고서
실제 `backend/bdo.db` import: 수행하지 않음

## 범위

V1.7D는 계정 성장 전체 백과사전이 아니라 다음 정보를 상태 추적 가능한 Content graph로 만든 Foundation이다.

- Account Progression 최상위 허브
- Main Quest, Content Unlock, Permanent Family Reward, Permanent Stat, Family Convenience 하위 기반
- 마그누스 전체 진행의 큰 체크포인트
- 공식 자료로 안정적으로 구분되는 지역·사가 단위 메인 의뢰
- Adventure Log Foundation과 대표 실데이터인 이고르 바탈리의 모험일지·마가한의 서
- 카마실비아·오드락시아 후속 일회성 가문 능력치 보상

Schema, migration, backend API, frontend/UI, Prompt Bridge와 AI 기능은 변경하지 않았다.

## Seed 규모

| 항목 | V1.7C 기준 | V1.7D 이후 | 증감 |
|---|---:|---:|---:|
| Source | 137 | 145 | +8 |
| Content | 238 | 259 | +21 |
| Active Content | 238 | 259 | +21 |
| Claim 선언 | 943 | 990 | +47 |
| Evidence row | 1,176 | 1,237 | +61 |
| Relation | 343 | 401 | +58 |

Claim은 `seed_contents.json`의 claim 선언 수이고 Evidence row는 claim별 `source_ids`가 importer에서 개별 row로 확장된 수다. V1.7D Relation 58개 중 19개는 기존 Content를 대상으로 한다.

지식 역할은 전체 seed 기준 FACT 193, STRATEGY 17, MEASUREMENT 11이다. V1.7D 추가분은 FACT 26, STRATEGY 0, MEASUREMENT 0이다. 과거 구조 2건은 `historical` requirement와 inactive/superseded Evidence로 분리했다.

## Source

신규 Source 8개는 모두 검은사막 한국 공식 자료다.

- `adventure-log-bookshelf-guide`: 현재 모험일지 책장, 해금 조건, 가문 보상 구조
- `new-adventurer-main-quest-guide`: 시작 분기와 메디아 이후 주요 지역 진행
- `quest-system-guide`: 메인 의뢰와 의뢰 조건의 일반 구조
- `morning-land-main-quest-guide`: 아침의 나라 진입 조건과 설화 일지 구조
- `jordaine-saga-update-2024-02-07`: 세렌디아·칼페온 메인 의뢰의 조르다인 사가 개편
- `family-stat-quest-history`: 카마실비아 방어력·오드락시아 공격력 가문 의뢰
- `hyperboost-progression-2026`: 현재 메인 의뢰·이고르 바탈리 가문 능력치 보상 요약
- `morning-land-launch-2023-03-29`: 설화 완료와 검은 사당 우두머리 해금

기존 공식 `magnus-guide`, `agris-fever-guide`, `pit-weekly-2025`도 재사용했다. 현재 가이드와 과거 상태가 충돌하는 모험일지 능력치 배치는 2025-07-23 변경을 current로 두고 이전 분산 배치를 superseded로 보존했다.

## Content

신규 Content 21개를 추가했다.

### Foundation

- `account-progression-foundation`
- `main-quest-progression-foundation`
- `content-unlock-foundation`
- `permanent-family-reward-foundation`
- `permanent-stat-progression`
- `family-convenience-unlock-foundation`
- `adventure-log-foundation`

### 대표 Questline과 Adventure Log

- `magnus-progression`
- `igor-bartali-adventure-log`
- `book-of-margahan`

### Main Quest checkpoint

- `main-quest-balenos`
- `main-quest-jordaine-saga`
- `main-quest-mediah`
- `main-quest-valencia`
- `main-quest-kamasylvia`
- `main-quest-drieghan`
- `main-quest-odyllita`
- `main-quest-morning-land`
- `main-quest-mountain-of-eternal-winter`

### 일회성 가문 보상

- `kamasylvia-family-defense-quest`
- `odyllita-family-attack-quest`

## 기존 Content 재사용

다음 기존 Content를 복제하지 않고 Relation 대상으로 재사용했다.

- 기반 성장: `energy-foundation`, `contribution-economy-foundation`, `ecology-family-drop-bonus`
- 전투: `combat-gear-progression-strategy`, `combat-stat-foundation`, `grind-zone-recommendation-system`
- 생활: `life-family-levels`
- 대양: `carrack-advance`, `panokseon`, `barter-current-system`
- 편의: `magnus-remote-storage`, `storage-current-system`, `family-silver-unification`
- 기존 시스템: `agris-fever`, `black-shrine-donghae-weekly`

마그누스는 기존 원격 창고 Content를 새로 만들지 않고 `unlocks`로 연결했다. 마가한의 서는 아그리스를 해금하는 것으로 표현하지 않고, 이미 56레벨에 열리는 기존 `agris-fever`를 강화하는 `related` 관계로 연결했다.

## Claims / Evidence

- V1.7D Claim: 47
- V1.7D Evidence row: 61
- verified Evidence row: 59
- superseded Evidence row: 2
- FACT: +26
- STRATEGY: +0
- MEASUREMENT: +0

활성 FACT requirement, Step와 Reward는 모두 claim별 verified Evidence를 가진다. 이고르 바탈리의 과거 보상 분산 구조와 모험일지 Foundation의 과거 구조는 inactive `historical` + `superseded`로만 남겼다.

## Adventure Log

- Foundation은 책장 단위 해금과 가문 공통 영구 보상을 설명한다.
- 이고르 바탈리는 51레벨 및 공식 선행 조건, 2025-07-23 이후 핵심 능력치 통합, 현재 가문 공격력 6·방어력 6을 기록한다.
- 마가한의 서는 58레벨 해금, 1·2권의 큰 진행 단계와 아그리스 최대 포인트 +50,000, 일일 회복 +5,000, 잡동사니 수량 효과 +50%p를 기록한다.
- 모든 모험일지, 모든 권·장, 장별 목표와 최적 동선은 추가하지 않았다.

## Main Quest

NPC별 개별 의뢰 대신 시작 분기, 지역, 사가, 중요한 해금 지점만 Content로 만들었다. 발레노스, 조르다인 사가, 메디아, 발렌시아, 카마실비아, 드리간, 오드락시아, 아침의 나라와 끝없는 겨울의 산 시작 분기를 포함한다.

간소화 진행의 시점 의존 조건, 시즌별 분기, NPC별 대화·전투·이동 순서, 개별 의뢰 수백 개는 제외했다. 공식 가이드가 단순 진행 흐름으로 제시하는 지역 사이에는 강제 prerequisite를 추정하지 않고 `related`를 사용했다.

## Magnus

- 현재 공식 가이드의 경로별 시작 조건을 하나의 Requirement에 alternative entry path로 표현했다.
- 세렌디아·칼페온 진행 관문과 `[마그누스] 도움의 대가`를 큰 체크포인트로만 저장했다.
- 최종 동(V) 우두머리 방어구는 기존 Reward 필드의 `quest_reward`, 수량 1, 선택 보상으로 표현했다.
- 원격 창고와 창고 시스템은 기존 Content를 Relation으로 재사용했다.
- 세부 심연 퍼즐, NPC별 동선, 지역별 모든 보상과 이동 비용은 입력하지 않았다.
- 확인한 current guide 범위에서 현재 모델에 보존해야 할 별도 Magnus 충돌 이력은 발견하지 않았다.

## Permanent Family Reward

별도 schema 없이 기존 Reward 필드만 사용했다. 가문 범위·영구성·비반복성은 연결된 Requirement의 `structured_value`에 기록했다.

- 이고르 바탈리: 가문 공격력 +6, 방어력 +6
- 마가한의 서: 아그리스 최대 포인트 +50,000, 일일 회복 +5,000, 잡동사니 수량 효과 +50%p
- 카마실비아 후속 의뢰: 가문 방어력 +1
- 오드락시아 후속 의뢰: 가문 공격력 +1
- 아침의 나라 메인 의뢰: 가문 공격력 +1, 방어력 +1

V1.7D Content에는 반복 schedule이나 checklist를 만들지 않아 일회성 영구 보상과 반복 보상을 혼합하지 않았다.

## Unresolved 및 의도적 제외

- 이고르 바탈리의 공격력·방어력 외 정확한 현재 영구 능력치 총합은 이번 공식 근거 조합에서 안전하게 확정하지 않아 Reward로 만들지 않았다.
- 모든 모험일지 및 이고르 바탈리·마가한의 서의 권/장별 목표, 개별 보상과 최적 동선은 Adventure Log Deep Pack 범위로 남겼다.
- 일반·간소화·시즌 진행의 모든 분기와 각 분기의 세부 해금 동등성은 시점 의존성이 있어 완전 모델링하지 않았다.
- 발렌시아 이후 지역 나열은 공식 가이드 흐름만 기록하고, 자료가 강제 선행조건이라고 명시하지 않은 지역 사이는 `prerequisite`로 만들지 않았다.
- 마그누스 지역별 모든 심연의 혈관, 퍼즐, 이동 비용과 예외 아이템은 기존 상세 Content 또는 후속 범위로 남겼다.
- 시즌별 보상, 이벤트 성장 지원, 올비아 아카데미, 클래스별 레벨링, 강화·사냥터·Boss·Life·Ocean Deep Pack은 추가하지 않았다.
- 영구 능력치 전체 합계 계산, 장별 완료율과 Growth UI/API는 구현하지 않았다.

## Tests

- V1.7D semantic tests: `9 passed in 28.62s`
- V1.7D + V1.7C 재검증: `19 passed in 67.61s`
- 전체 backend tests: `143 passed in 418.16s`

전체 실행에는 V1.7A/B/C, Routine, V1.6F/G/H/I semantic regression이 모두 포함된다.

## Import 및 보존 검증

- `seed_sources.json`, `seed_contents.json` UTF-8 JSON parse: 통과
- Source ID/URL, Content slug, V1.7D nested seed_key uniqueness: 통과
- unknown source/evidence/relation target: 0 (전체 seed import 성공)
- unexpected archive: 0 (V1.7C baseline nested ID와 active 상태 비교)
- 임시 SQLite migration: `20260902_0001` → `20260903_0002` 통과
- V1.7C baseline import → V1.7D import → 동일 seed 2회 추가 재import: 통과
- 세 번의 V1.7D seed import 후 canonical row count 변화: 0
- 기존 238 Content stable ID: 보존
- 기존 nested stable ID와 active 상태: 보존
- 신규 Content와 nested stable ID: 보존
- ChecklistInstance, ChecklistItemState와 완료 이력: 보존
- UserContentState: 보존

## DB integrity

- 작업 전 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 작업 후 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 결과: 동일. 실제 `backend/bdo.db`는 import하거나 수정하지 않았다.

## 후속 후보

후속 버전 번호는 확정하지 않는다. 별도 설계가 필요한 후보는 Adventure Log Deep Pack, Main Quest Deep Pack, 영구 능력치 합계 계산과 장별 완료율 기능이다.
