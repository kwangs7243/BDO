# V1.6G Gathering / Processing / Farming / Fishing Deep Seed Pack 보고서

기준 시점: **2026-09-03 KR Live**  
검증일: 2026-09-03  
결론: V1.6F 생활 공통 기반 위에 채집·가공·재배·낚시의 실제 행동 규칙을 현재 스키마 범위에서 추가했다. 별도 SQLite DB에서 V1.6F 기준 데이터부터 V1.6G를 두 번 적재해 마이그레이션, 멱등성, 기존 ID와 사용자 이력 보존을 확인했다. 실제 `backend/bdo.db`에는 적재하지 않았다.

## 1. 변경 파일

- `data/seed_sources.json`
- `data/seed_contents.json`
- `backend/tests/test_life_deep1_seed.py`
- `handoff/V16G_LIFE_DEEP1_REPORT.md`

DB schema, Alembic migration, backend API, frontend/UI, 디자인, Prompt Bridge, AI와 모델 코드는 변경하지 않았다.

## 2. 데이터 규모

| 항목 | V1.6F | V1.6G | 증감 |
|---|---:|---:|---:|
| Source | 57 | 72 | +15 |
| Content | 73 | 92 | +19 |
| ScheduleRule | 46 | 50 | +4 |
| Requirement | 191 | 257 | +66 |
| Step | 58 | 58 | 0 |
| Reward | 161 | 161 | 0 |
| Section | 71 | 77 | +6 |
| Relation | 113 | 156 | +43 |
| ChecklistTemplate | 35 | 35 | 0 |
| ChecklistTemplateItem | 46 | 46 | 0 |
| claim 선언 | 573 | 669 | +96 |
| Evidence 행(source 연결 단위) | 722 | 836 | +114 |
| superseded claim 선언 | 16 | 23 | +7 |

하나의 claim에 여러 Source가 연결되면 Source별 Evidence 행이 생성되므로 Evidence 행 수는 claim 선언 수보다 많다.

## 3. Source 변경

신규 공식 Source 15개를 추가했다.

### Gathering

- `gathering-guide`: 현재 채집 가이드(`wikiNo=97`)

### Processing

- `processing-guide`: 현재 가공 가이드(`wikiNo=98`)
- `processing-stone-history`: 통합 가공석 이력
- `life-clothes-2025-08-27`: 은자수 공예가의 옷 제거와 현재 생활복 효과표

### Farming

- `farming-guide`: 현재 재배 가이드(`wikiNo=94`)
- `farming-overhaul-2026-06-04`: 성장 시간, 수분, 비료, 수확량, 울타리와 두더지 개편
- `farming-moles-2026-06-17`: 최신 두더지 보상 조정
- `old-moon-seed-pouch-2025-07-09`: 그믐달 씨앗 가방 도입과 현재 사용 흐름

### Fishing

- `fishing-basic-guide`: 낚시 기초 가이드(`wikiNo=107`)
- `fishing-advanced-guide`: 낚시 고급 가이드(`wikiNo=108`)
- `fish-freshness-2025-05-21`: 물고기 가격 보증 기간 개편
- `fishing-improvement-history`: 보물 등급 물고기 개선 이력
- `mystical-fish-tank-2023-08-02`: 신비한 물고기 어항 도입 이력
- `mystical-fish-tank-rules-2024-08-28`: 어항 보관·5배 보증 기간·판매·이동 제한 규칙
- `fish-encyclopedia-2025-04-16`: 대륙도감 개편

기존 V1.6F Source 가운데 `life-unification-2026-09-02`, `life-mastery-history`, `life-mastery-prione-2025-01-08`, `ocean-quest-rework-2025-02-05`, `ocean-iliya-consolidation-2025-05-14`, `carrack-sailor-fishing-2025`는 중복 생성하지 않고 재사용했다.

## 4. 신규·보강 Content

기존 73개 Content와 의미가 겹치는지 먼저 확인했고, 지시서 후보 19개를 모두 신규 Content로 추가했다. 기존 Content 자체의 필드나 중첩 데이터는 보강하지 않았다.

### Gathering

- `gathering-current-system`
- `gathering-tools`
- `gathering-green-artisan-minigames`
- `gathering-special-drops`

### Processing

- `processing-current-system`
- `mass-processing`
- `processing-stones-and-clothes`

### Farming

- `farming-current-cycle`
- `farming-fences`
- `farming-seeds-harvest-breeding`
- `farming-moles`
- `old-moon-seed-pouch`

### Fishing

- `fishing-current-system`
- `auto-fishing`
- `fish-freshness-and-trade`
- `imperial-fishing-delivery`
- `mystical-fish-tank`
- `treasure-grade-fish`
- `fishing-encyclopedia-and-weekly-contest`

V1.6F의 생활 레벨·숙련도·통합 장비·기운 기반과는 Relation으로 연결했으며, 같은 전체 표를 다시 복제하지 않았다. 일반 자동 낚시와 V1.6D의 중범선 선원 자동 낚시는 서로 다른 시스템으로 유지했다.

## 5. canonical 데이터 범위

### Gathering

- 벌목, 수액 채취, 무두질, 도축, 호미, 채광, 물뜨기의 대상·도구·대표 결과를 구분했다.
- 마력의 채집 도구는 채집 시간 11초 감소와 모든 채집물 획득 확률 +80%를 기록했다. 숙련도에 따른 **아이템 획득 확률 증가만** 적용되지 않으며, 숙련도 전체가 무효라는 해석은 금지했다.
- 데미하르 채집 도구는 시간 11초 감소, 획득 확률 +80%, 채집 경험치 +50%, 유효 기간 14일을 별도 구조로 저장했다.
- 초록 장인 미니게임은 성공 시 기운 10·한 번 채집 결과 10배, 실패 시 기운 1·일반 1회 결과를 저장했다. 발타라의 천안과 발타라의 추억은 10배 대상에서 제외했다.
- 요정의 숨결의 현재 발견 행동과 10개 단위 교환 항목을 저장했다. 최신 공식 수치로 확인되지 않은 획득량·확률은 추정하지 않았다.
- 묻혀진 흔적 보상 중 뾰족한 흑결정 조각 15~22개 100%, 고대 정령의 가루 5~20개 50%, 자연의 열매 22~26개 100%를 구조화했다.

### Processing

- 흔들어 섞기, 빻기, 장작 패기, 말리기, 솎아내기, 가열하기, 간이 연금, 간이 요리, 공작의 현재 가공 방식을 기록했다.
- 기본 가공 성공률은 70%로 유지했다. 전체 기본 성공률이 이후 100% 또는 70% 초과로 바뀌었다는 확인되지 않은 claim은 만들지 않았다.
- 대량 가공은 숙련도 0/500/2000/2500/2700/2800/2900/3000에서 각각 10/35/250/290/300/305/310/315회를 구조화했다.
- 현재는 통합 가공석 하나가 여섯 가공 방식에 쓰이며, 과거 방식별 가공석 6개 필수 흐름은 superseded로 보존했다.
- 현재 가공복 진행은 로기아·카르타·마노스다. 은자수 공예가의 옷을 현재 진행 장비로 취급하지 않았다.
- 강화 V 단계 가공 성공률 효과는 마노스 +40%, 카르타 +33%, 로기아 +28%를 포함해 공식 표 전체를 저장했다.

### Farming

- 2026-06-04 이후 적합/부적합/매우 부적합 온도의 기본 성장 시간을 20/21/22시간으로 저장했다.
- 수분 감소 속도는 기존의 1/5로 기록했다. 삭제된 세 종류 비료의 현재 사용 가능 개수는 0이다.
- 허름한/작은/평범한/단단한/그믐달 울타리의 공헌도와 칸 수를 저장했고, 그믐달 울타리는 재배 명장 1 이상 조건을 분리했다.
- 사용하지 않은 울타리 자동 철거 기준은 현재 28일이며 과거 14일 규칙은 superseded다.
- 확정 획득 아이템 수량 5배, 확률 획득 아이템 확률 2배·수량 2.5배, 지정 특수 작물 수량 3배를 저장했다.
- 두더지는 2026-06-17 조정이 2026-06-04보다 최신이다. 공식 문서가 상대 증가만 제시한 항목은 `increased`와 상대 증가율만 저장하고 최종 절대 개수를 계산하지 않았다.
- 그믐달 씨앗 가방은 최대 50개를 보관한다. 현재 확인된 절차는 씨앗을 캐릭터 가방으로 옮긴 뒤 심는 방식이다.

### Fishing

- 낚시 레벨, 낚시 잠재력 최대 5단계, 자원 상태가 입질 대기 시간에 영향을 주는 시스템을 분리했다. 실시간 지역 자원 상태는 영구 seed에 넣지 않았다.
- 낚시 숙련도 3000의 보물 등급 그룹 획득 확률 기여분은 6.25%다. 모든 지역의 최종 보물 물고기 확률로 해석하지 않도록 표시했다.
- 일반 자동 낚시는 기본 완료 대기 180초, 최소 60초다. +10 발레노스 낚싯대의 감소 효과 25%와 같은 종류 반려동물 효과 비중첩을 기록했다.
- 자동 낚시 버리기 등급은 기본 흰색에서 생활 레벨에 따라 초록색·파란색·노란색까지 확장되는 현재 표를 저장했다.
- 일반 물고기 가격 보증 기간은 48시간, 오딜리타산은 60시간이다. 영원의 겨울산은 최신 공식 수치를 직접 확인하지 못해 `null`로 남겼다. 보증 기간 종료 시 판매 가치는 원가의 30%가 된다.
- 황실 낚시 납품은 주요 파란색·노란색 등급 물고기를 원가의 250%에 판매하며 서버별 한도가 3시간마다 갱신된다.
- 신비한 물고기 어항은 최대 50마리 자동 보관과 가격 보증 기간 5배를 기록했다. 2025-02-05 이후 오색빛 조개 4개 요구는 제거된 이력으로 보존했다.
- 보물 등급 물고기 45종 그룹은 일반 판매 대상이지만 황실 낚시 납품은 불가능하다는 규칙을 저장했다. 전체 45종 item atlas는 만들지 않았다.
- 주간 낚시대회의 기록, 정산, 보상 지급을 하나의 reset으로 합치지 않았다. 월요일~토요일 기록과 일요일 정산·보상 지급을 서로 다른 ScheduleRule로 저장했다.

## 6. superseded와 stale-data 방지

superseded claim 선언은 16개에서 23개로 늘었다. 신규 7개는 다음 과거 규칙을 현재 집계에서 제외한다.

- 방식별 개별 가공석 6개 필수
- 은자수 공예가의 옷을 현재 가공 진행 장비로 사용
- 울타리 미사용 철거 14일
- 2026-06-04 두더지 보상을 최종 최신 보상으로 사용
- 일반 물고기 가격 보증 24시간
- 오딜리타산 물고기 가격 보증 36시간
- 신비한 물고기 어항 획득에 오색빛 조개 4개 필수

또한 V1.6F의 구형 생활 연금석 내구도·수동 활성화 Evidence가 여전히 `superseded`, `active=false`인지 회귀 테스트로 확인했다. 현재 Source를 추가하면서 이 데이터를 다시 활성화하지 않았다.

## 7. Gathering semantic tests

- 마력 도구: 11초, +80%, 숙련도 기반 획득 확률만 미적용
- 초록 장인: 성공 기운 10·10배, 실패 기운 1·일반 1회
- 발타라 특수 아이템: 초록 장인 10배 제외
- 묻혀진 흔적: 뾰족한 흑결정 조각 15~22 확정, 고대 정령의 가루 확률 보상
- 구형 생활 연금석 활성화 흐름: `active=false`

## 8. Processing semantic tests

- 기본 성공률 70%
- 현재 통합 가공석, 구형 여섯 가공석 필수 `active=false`
- 은자수 공예가의 옷 현재 진행 장비 `false`
- 대량 가공 숙련도 2000=250, 3000=315
- 현재 가공복 로기아·카르타·마노스와 V 단계 효과 28/33/40%
- 기본 성공률이 전역적으로 70%보다 높아졌다는 미지원 claim `false`

## 9. Farming semantic tests

- 성장 시간 20/21/22시간
- 비료 현재 사용 가능 개수 0
- 확정 수량 5배, 확률 2배·수량 2.5배, 지정 특수 작물 3배
- 울타리 미사용 철거 28일, 과거 14일 `active=false`
- 수분 감소 속도 기존 대비 1/5
- 두더지 근거 우선순위 `2026-06-17 > 2026-06-04`, 절대 보상량 미추정
- 그믐달 씨앗 가방 직접 심기 `active=false`, 현재는 일반 가방으로 이동 후 심기

## 10. Fishing semantic tests

- 일반/오딜리타 가격 보증 48/60시간, 과거 24/36시간 `active=false`
- 일반 자동 낚시 180초, 최소 60초
- 어항 보증 기간 5배, 과거 조개 4개 요구 `false`
- 황실 낚시 납품 250%, 한도 3시간 간격
- 보물 등급 물고기 황실 납품 불가
- 낚시 숙련도 3000 기여분 6.25%
- V1.6D 선원 자동 낚시와 일반 자동 낚시 타이머를 병합하지 않음
- 주간 대회의 기록·정산·보상 지급 ScheduleRule 분리

## 11. CURRENT GUIDE CONFLICTS

최신 KR Live patch를 현재 가이드 또는 과거 설명보다 우선했다.

### Gathering

- 현재 채집 가이드에는 생활 연금석의 충전·내구도·수동 활성화 설명이 남아 있으나, 2026-09-02 이후 생활 연금석은 장착 효과 방식이다. 구형 흐름은 active claim으로 복원하지 않았다.

### Processing

- 과거에는 여섯 방식별 가공석과 은자수 공예가의 옷을 진행 장비로 사용했으나 현재는 통합 가공석과 로기아·카르타·마노스 가공복을 사용한다.

### Farming

- 오래된 가이드의 작물별 고정 성장 시간, 비료 사용, 과거 수확량, 울타리 14일 철거 규칙 대신 2026-06-04의 20/21/22시간, 비료 삭제, 수확량 개편, 28일 규칙을 적용했다.
- 두더지 보상은 2026-06-17 문서를 2026-06-04보다 우선했다.

### Fishing

- 과거 일반 물고기 24시간과 오딜리타산 36시간 대신 2025-05-21 이후 48시간과 60시간을 적용했다.

## 12. ANNOUNCED BUT NOT CONFIRMED LIVE

### Old Moon Seed Pouch direct planting

2026-06-04 개편 예고에는 씨앗 가방에서 씨앗을 꺼내지 않고 바로 심는 기능이 포함됐지만, 2026-09-03 기준 실제 적용을 입증하는 최신 KR Live 문서를 확인하지 못했다.

- 현재 canonical: 씨앗을 캐릭터 가방으로 옮긴 뒤 심기
- 직접 심기 Requirement: `active=false`
- 확인 상태: `unconfirmed_live`
- Evidence: `needs_review`, `active=false`

추후 적용을 명시한 공식 패치가 발견될 때만 현재 claim으로 승격해야 한다.

## 13. 참조·archive·ID·이력 검증

V1.6F 데이터 57 Source / 73 Content를 임시 DB에 먼저 적재한 후 V1.6G를 적재했다.

- unknown source: 0
- unknown relation: 0
- unknown evidence source: 0
- unknown entity: 0
- 예상하지 않은 archive: 0
- 기존 Content stable ID: 73/73 유지
- 기존 nested stable ID: 1,443/1,443 유지
- ChecklistInstance: 34개 유지
- ChecklistItemState: 45개 유지
- 완료 여부와 note fixture: 유지
- UserContentState: 1개 유지
- UserContentState의 ID, Content 연결, 상태 `in_progress`, priority, note: 유지

새 V1.6G Content에는 반복 숙제를 추측해 ChecklistTemplate을 추가하지 않았다. 따라서 기존 체크리스트 수와 이력은 변하지 않았다.

## 14. Migration·import·idempotency

실제 DB가 아닌 임시 SQLite DB에서 다음 순서로 검증했다.

1. 빈 DB에 `20260902_0001` 적용
2. `20260903_0002` 적용
3. V1.6F 기준 57 Source / 73 Content 적재
4. 현재 daily/weekly 체크리스트 이력과 `UserContentState` fixture 생성
5. V1.6G 적재
6. 동일 V1.6G 재적재

1차와 2차 적재 뒤 모든 canonical/seed-managed 테이블 행 수가 같아 멱등성을 확인했다. 최종 임시 DB 행 수는 다음과 같다.

- Source 72, Content 92
- ScheduleRule 50, Requirement 257, Step 58, Reward 161, Section 77, Relation 156
- ChecklistTemplate 35, ChecklistTemplateItem 46
- Evidence 836
- 검증 fixture 포함 ChecklistInstance 34, ChecklistItemState 45, UserContentState 1

임시 검증 DB와 일회성 검증 스크립트는 검증 후 제거했다.

## 15. 테스트 결과

실행:

```powershell
cd backend
uv run pytest -q -p no:cacheprovider tests/test_life_deep1_seed.py
uv run pytest -q -p no:cacheprovider
uv run python .tmp_v16g_verify.py  # 일회성 검증 후 삭제
```

결과:

- V1.6G semantic regression: **18 passed in 33.24s**
- backend 전체: **70 passed in 87.35s**
- migration `0001 -> 0002`: 통과
- V1.6F 기준 -> V1.6G import: 통과
- 동일 V1.6G 두 번째 import: 행 수 불변
- 실패: 0

## 16. 실제 DB 보호와 seed hash

`backend/bdo.db`:

- 작업 전 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 작업 후 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 크기: 118,784 bytes

실제 사용자 DB는 변경되지 않았다.

최종 seed SHA-256:

- `data/seed_sources.json`: `4BF74BEECA278600B9BC4C3653687A65EE7791B9E17D993E50263BE8CEFC1102`
- `data/seed_contents.json`: `9428463F4C3D826829AB2265923B208DB1E93C270F240F967C956793CC82A75A`

## 17. unresolved factual details

공식 근거가 부족한 값은 추정하지 않고 다음처럼 남겼다.

- 채집 기운 미소모 확률의 정확한 현재 최대 수치: V1.6F의 `null` 유지
- 요정의 숨결의 최신 행동별 획득 확률·수량: 현재 가이드에서 직접 확인 가능한 범위만 저장
- 가공 레벨별 일반 결과량 증가와 희귀 결과 획득 확률의 전체 수치표
- 두더지 보상의 최종 절대 개수: 2026-06-17 문서가 상대 증가만 제공하므로 미계산
- 슈슈 획득까지의 세부 단계: 불완전한 공략으로 임의의 Step을 만들지 않음
- 영원의 겨울산 물고기 가격 보증 기간의 정확한 현재 시간: `null`
- 주간 낚시대회의 영구 보상 수량 전체 표와 월요일 00:00~00:20 집계 공백의 별도 수치 모델
- 보물 등급 물고기 45종의 개별 이름·가격·좌표

## 18. schema gap

이번 작업에서는 스키마를 변경하지 않고 다음 제약을 현행 구조 안에서 표현했다.

- `ContentRelation.relation_type`의 도메인별 관계 어휘가 제한적이어서 `related`, `part_of`와 note를 사용했다.
- 채집 도구 효과, 대량 가공 표, 재배 배율, 낚시 숙련도 표를 전용 typed table이 아닌 `ContentRequirement.structured_value`에 저장했다.
- `ScheduleRule`은 `recurrence_type=interval`을 지원하지만 간격 숫자 전용 필드가 없어 황실 낚시 납품의 3시간 값은 Requirement와 schedule notes에 함께 저장했다.
- 주간 낚시대회의 기록 구간·정산 구간·보상 지급을 서로 다른 ScheduleRule로 나눌 수는 있지만, 기록 창의 종료와 짧은 집계 공백을 하나의 기간 객체로 정밀 표현하는 필드는 없다.
- 어종별 등급·가격·출현 지역·좌표를 자연스럽게 담는 item/fish catalogue 모델이 없다. 따라서 이번에는 보물 물고기 그룹까지만 저장했다.
- DB에는 `Evidence.superseded_by`가 있으나 현재 seed 입력/importer는 해당 연결을 설정하지 않는다. `verification_status=superseded`, `active=false`, note와 최신 Source 연결로 교체 관계를 보존했다.
- 발표됐지만 적용 미확인인 기능의 상태 전이를 위한 전용 필드가 없어 비활성 Requirement와 Evidence로 보존했다.

## 19. 의도적으로 제외한 범위

- 시간당 채집 수익, 채집 루트와 지역·수풀·도구 추천, 숙련도별 수익 분기
- 모든 가공 recipe, 재료별 수익·거래소 마진 계산
- 씨앗 수익성, 울타리 최적 배치, 부산물 시간 효율 등 재배 경제·전략
- 모든 물고기 위치·드롭 풀·보물 물고기 좌표를 포함한 Full Fish Atlas
- 버리는 등급·낚싯대·물고기 종류별 ROI, 낚시터 추천과 지도
- 실제 시세, 이벤트성 수치와 보상, 커뮤니티 추정치
- UI, API, 디자인, Prompt Bridge, AI, schema와 migration 확장
- 실제 `backend/bdo.db` import
