# V1.7A Combat Progression Foundation & Strategy Evidence 결과 보고서

- 기준: 2026-09-04 KR Live
- 작업 범위: 전투 기반 FACT seed, 시점·맥락이 붙은 STRATEGY seed, semantic regression test, 임시 DB import 검증
- 실제 사용자 DB: import하지 않음

## 변경 파일

- `data/seed_sources.json`
- `data/seed_contents.json`
- `backend/tests/test_combat_foundation_seed.py`
- `handoff/V17A_COMBAT_FOUNDATION_REPORT.md`

스키마, Alembic migration, backend API, frontend/UI, 디자인, 체크리스트 엔진, Prompt Bridge와 AI 기능은 변경하지 않았다. 실제 `backend/bdo.db`에도 seed를 적용하지 않았다.

## Seed 증분

| 항목 | V1.6I | V1.7A | 증분 |
|---|---:|---:|---:|
| Source | 98 | 112 | +14 |
| Content | 140 | 166 | +26 |
| Requirement | 385 | 428 | +43 |
| Section | 77 | 81 | +4 |
| Relation | 211 | 236 | +25 |
| Claim 선언 | 742 | 785 | +43 |
| Evidence DB row | 935 | 996 | +61 |
| Superseded claim 선언 | 38 | 44 | +6 |

Claim 하나가 여러 Source를 참조하면 importer가 Source별 Evidence row로 펼치므로 Claim 선언과 Evidence DB row 증분은 다르다. Source ID·URL 112개와 Content slug 166개는 각각 모두 고유하다.

## 신규 Source와 역할

신규 Source 14개는 `official_guide` 6개, `official_patch` 2개, `official_history` 1개, `community_strategy` 4개, `community_index` 1개다.

### FACT 근거

- `combat-stat-bonus-guide`
- `combat-system-rework-2025-07-23`
- `crystal-guide`
- `item-drop-rate-guide`
- `item-drop-applicability-guide`
- `item-drop-benefits-history`
- `agris-fever-guide`
- `church-buff-guide`
- `camp-church-rework-2025-12-30`

기존 `artifact-guide`와 2026-07-15 패치를 가리키는 기존 `blood-altar-challenge-2026-07-15` Source는 중복 생성하지 않고 재사용했다.

### STRATEGY 근거

- `combat-gear-a-to-j-2026-04-22`
- `hyper-boost-gear-strategy-2026-08-19`
- `softcap-strategy-2025-07-29`
- `grind-selection-strategy-2025-11-18`

각 Source에 게시일을 보존했다. 커뮤니티 공략의 정확한 장비 수치나 추천 순서를 공식 시스템 FACT의 유일한 근거로 사용하지 않았다.

### Discovery 전용

- `combat-guide-index-2026-02-28`

이 Source는 원문 탐색용 `community_index`로만 저장했으며 어떤 claim의 Evidence에도 연결하지 않았다.

## 신규 Content

### 전투 능력치와 사냥터 규칙

1. `combat-stat-foundation`
2. `sheet-vs-final-stats`
3. `sheet-ap-bonus-table`
4. `sheet-dp-bonus-table`
5. `monster-extra-ap`
6. `race-extra-ap`
7. `accuracy-evasion-current-system`
8. `special-attack-system`
9. `grind-zone-attack-cap`
10. `grind-zone-recommendation-system`

### 수정·유물·광명석

11. `combat-crystal-system`
12. `pve-crystal-strategy`
13. `combat-artifacts`
14. `combat-lightstones`
15. `pve-lightstone-strategy`

### 전투 버프

16. `combat-buff-foundation`
17. `church-buff-current`
18. `camp-combat-buffs`
19. `combat-food-elixir-perfume`

### 아이템 획득과 아그리스

20. `item-drop-rate-system`
21. `loot-scroll-system`
22. `item-drop-rate-cap`
23. `ecology-family-drop-bonus`
24. `agris-fever`

### 전략 기반

25. `combat-gear-progression-strategy`
26. `grind-setup-strategy-foundation`

## FACT / STRATEGY / MEASUREMENT 분리

현재 스키마에는 전용 역할 컬럼이 없으므로 스키마를 늘리지 않고 Requirement `structured_value.knowledge_role`에 역할을 명시했다.

- FACT Requirement: 39개
- STRATEGY Requirement: 4개
- MEASUREMENT Requirement: 0개

이번 팩에는 재현 가능한 측정 데이터가 없으므로 MEASUREMENT를 추정 생성하지 않았다. STRATEGY에는 `current_as_of`, 비교해야 할 맥락 차원, 단일 영구 정답이 아니라는 표시를 넣었다. 커뮤니티 전략 claim은 가능한 경우 관련 공식 시스템 Source와 함께 교차 연결했다.

## 핵심 semantic 결과

### 공격력과 방어력

- AP 309의 몬스터 추가 공격력 0, AP 310은 8, AP 401은 744, AP 450은 1,528을 경계값으로 검증한다.
- AP 401의 표기 공격력 구간 보너스는 249다.
- DP 401의 피해 감소율은 30%, DP 400의 추가 피해 감소는 81이다.
- 추가 피해 감소 DP 481=91, 486=92, 531=101을 검증한다.
- 공식 표의 병합 구간을 임의의 개별 행으로 추측 확장하지 않고 시작 경계값과 공식 구간식으로 저장했다.

### 전투 시스템

- 독립 적중률·회피율 퍼센트는 현행 능력치가 아니며, 개편 당시 1%가 4포인트로 전환된 이력을 보존한다.
- 종족 추가 공격력의 과거 PvE 최대 20% 감소 규칙은 현행이 아니다.
- 서로 다른 특수 공격 조건은 동시에 만족할 때 함께 적용될 수 있다.
- 사냥터 공격력 제한 초과분은 5%만 적용된다.
- 사냥터 추천은 최종 공격력 ±50 범위이며 몬스터·종족 추가 공격력을 포함하고 방어력을 필터 조건으로 쓰지 않는다.

### 수정·유물·광명석

- 수정 가방 50개, 프리셋 5개, 수정 그룹별 장착 제한을 분리해 저장했다.
- 추출은 수정을 보존하고 직접 제거는 파괴한다.
- 수정 파괴 방지 이벤트를 영구 규칙으로 만들지 않고 `needs_review`, `active=false`로 저장했다.
- 유물 2개, 유물당 광명석 2개, 총 광명석 슬롯 4개를 검증한다.
- 카부아의 유물 AP 7/적중 20/HP 100/지구력 75, 인도하는 불빛 계열 대표 수치 추가 AP 3/적중 5/HP 250을 공식 Source에 연결했다.

### 전투 버프

- 현행 교회 버프: AP 8, 적중 8, 피해 감소 8, HP 150, 전투·기술 경험치 각 15%.
- 120분/300만 은화, 300분/1,000만 은화 선택을 검증한다.
- 과거 공격·보호·경험 3종 교회 버프는 `superseded`, `active=false`다.
- 간편한 차림의 크론 정식 현행 대표 효과는 백어택 피해 5%, 치명타 피해 5%다.
- 과거 다운어택 피해 5% claim은 `superseded`, `active=false`다.
- 야영지와 음식·비약·향수는 서로 다른 버프 출처로 유지하며, 이번 팩에서 검증하지 않은 전체 아이템 효과를 추정하지 않았다.

### 획득 확률과 아그리스

- 아이템 획득 확률 증가와 획득 수량 증가는 별도 효과다.
- 아이템 획득 증가 주문서 1·2단계의 확률 증가는 같고 수량 증가는 각각 50%, 100%다. 이 팩에서 공식 현행값으로 확정하지 않은 정확한 확률 증가 퍼센트는 `null`이다.
- 전체 아이템 획득 확률 증가 상한 400%와 일반 상한 300%를 분리했다.
- 과거 전체 300% 상한은 `superseded`, `active=false`다.
- 생태 지식 보너스는 500점 5%부터 10,000점 30%까지 공식 경계값을 저장했다.
- 가문 명성 7,000의 아이템 획득 확률 증가 10%를 별도 Requirement로 저장했다.
- 아그리스는 56레벨, 가문 공유, 기본 최대 50,000/일일 회복 15,000, 강화 후 최대 100,000/일일 회복 20,000, 매일 Asia/Seoul 06:00 회복을 검증한다.
- 강화 후 잡동사니 수량 증가는 150%이며 희귀 아이템 획득 확률 증가는 아니다.

## 현행/과거 충돌 처리

| 영역 | 과거 또는 임시 안내 | V1.7A current canonical | 상태 |
|---|---|---|---|
| AP 구간표 | 현행 공식 표 이전 값 | 2026-09-04 공식 가이드 경계값·구간식 | 과거 claim superseded/inactive |
| 종족 추가 공격력 | PvE 최대 20% 감소 | 제한 제거 후 최종 공격력 구성에 포함 | 과거 claim superseded/inactive |
| 적중·회피 | 독립 퍼센트 능력치 | 적중력·회피력 수치로 통합 | 과거 claim superseded/inactive |
| 교회 버프 | 공격·보호·경험 3종 | 현행 통합 버프 | 과거 claim superseded/inactive |
| 크론 정식 | 다운어택 피해 5% | 백어택 피해 5%, 치명타 피해 5% | 과거 claim superseded/inactive |
| 획득 확률 상한 | 전체 300% | 전체 400%, 일반 300% | 과거 claim superseded/inactive |
| 수정 파괴 방지 | 기간 한정 이벤트 | 영구 규칙으로 확정하지 않음 | needs_review/inactive |

## 의도적 미확정과 다음 범위

- 직업별 콤보·스킬·밸런스와 사냥터별 상세 공략은 V1.7A 범위 밖이다.
- 전체 사냥터 공격력 제한표, 적중 요구치, 수익 및 시간당 효율은 V1.7B 또는 측정 팩 대상이다.
- 모든 수정·광명석 조합의 순위와 단일 추천 세팅은 만들지 않았다.
- 전체 음식·비약·향수·야영지 버프 카탈로그와 동적 가격은 만들지 않았다.
- 주문서의 정확한 획득 확률 증가 퍼센트는 이번 검증 근거로 확정하지 않아 `null`로 남겼다.
- 클래스·장비·사냥터별 실측값은 측정 조건과 원자료가 없으므로 생성하지 않았다.
- 현재 모델에는 FACT/STRATEGY/MEASUREMENT 전용 컬럼과 시점별 측정 snapshot 모델이 없다. 이번 범위에서는 `structured_value`와 Source type으로 역할을 표현했으며 스키마는 변경하지 않았다.

## Import / 멱등성 / 이력 보존 검증

실제 DB가 아닌 새 임시 SQLite DB에서 다음 순서로 실행했다.

1. Alembic `20260902_0001`
2. Alembic `20260903_0002` (`head`)
3. V1.6I baseline Source 98 / Content 140 import
4. ChecklistInstance, 완료된 ChecklistItemState와 UserContentState 보존 fixture 생성
5. V1.7A Source 112 / Content 166 import
6. 동일 V1.7A seed 재import

결과:

- migration `0001 → 0002`: 성공
- 두 번째 V1.7A import 후 canonical table count: 첫 번째와 동일
- 기존 Content ID: 140/140 유지
- 기존 stable nested ID: 1,958/1,958 유지
- 기존 nested active/archive 상태: 유지
- ChecklistInstance: 유지
- ChecklistItemState 완료 상태와 note: 유지
- UserContentState 상태·우선순위·note: 유지
- unknown Source/Relation/Evidence/entity reference: 0 (importer 검증 통과)
- unexpected archive: 0

주요 임시 DB count:

| Table | V1.6I baseline | V1.7A 1차 | V1.7A 2차 |
|---|---:|---:|---:|
| source | 98 | 112 | 112 |
| content | 140 | 166 | 166 |
| content_requirement | 385 | 428 | 428 |
| content_section | 77 | 81 | 81 |
| content_relation | 211 | 236 | 236 |
| evidence | 935 | 996 | 996 |
| schedule_rule | 50 | 50 | 50 |
| checklist_template | 35 | 35 | 35 |
| checklist_template_item | 46 | 46 | 46 |

## 테스트 결과

- V1.7A semantic tests: **12 passed**
- backend 전체 tests: **115 passed**
- seed JSON parse 및 ID/URL/slug 고유성: 성공
- seed importer 및 2회 import 멱등성: 성공

## 실제 DB 불변 검증

- before SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- after SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 결과: 동일, 실제 `backend/bdo.db` 미변경
