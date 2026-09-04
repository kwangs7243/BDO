# V1.6F Life Foundation & Integrated Gear Seed Pack 보고서

기준 시점: 2026-09-03 KR Live  
검증일: 2026-09-03  
결론: 생활 공통 기반 데이터를 현재 schema 안에서 반영하고 임시 SQLite DB에서 검증했다. 실제 `backend/bdo.db`에는 적재하지 않았다.

## 1. 변경 파일

- `data/seed_sources.json`
- `data/seed_contents.json`
- `backend/tests/test_life_foundation_seed.py`
- `handoff/V16F_LIFE_FOUNDATION_REPORT.md`

DB schema, Alembic migration 파일, backend API, frontend/UI, 디자인, 모델 클래스, Prompt Bridge와 AI 기능은 변경하지 않았다.

## 2. 데이터 규모

| 항목 | V1.6E | V1.6F | 증감 |
|---|---:|---:|---:|
| Source | 50 | 57 | +7 |
| Content | 62 | 73 | +11 |
| ScheduleRule | 45 | 46 | +1 |
| Requirement | 145 | 191 | +46 |
| Step | 58 | 58 | 0 |
| Reward | 161 | 161 | 0 |
| Section | 54 | 71 | +17 |
| Relation | 91 | 113 | +22 |
| ChecklistTemplate | 34 | 35 | +1 |
| ChecklistTemplateItem | 45 | 46 | +1 |
| claim 선언 | 501 | 573 | +72 |
| Evidence 행(source 연결 단위) | 636 | 722 | +86 |

한 claim에 여러 source가 연결되면 source별 Evidence 행이 만들어지므로 Evidence 행은 claim 선언보다 많다.

## 3. Source 변경

신규 공식 Source 7개:

- `life-family-levels-2024-04-17`: 생활 레벨 가문 통합, 경험치 합산, 도인 100/50 구분
- `life-mastery-prione-2025-01-08`: 숙련도 3000, 프리오네, 생활 숙련도 도구와 분야별 효과
- `life-mastery-history`: 생활 레벨 누적 숙련도와 도인 50의 800
- `life-client-fix-2026-09-02`: 청명의 보주 가공식 표시 오류 수정
- `floamos-2023-02-15`: 플로아모스 상시 획득·일일 부위 교환
- `energy-profile-guide`: 기운과 생활 정보의 기본 구조
- `energy-advanced-guide`: 최대/현재 기운과 자연 회복

기존 Source 보강:

- `life-unification-2026-09-02`: 게시일·확인일·지역 metadata와 생활 장비/광명석/연금석/청명의 보주/기운 담당 범위를 명시했다.
- `artifact-guide`: 확인일·지역 metadata와 마가한의 유물 담당 범위를 명시했다.

동일 URL의 Source를 중복 생성하지 않았다.

## 4. 신규·보강 Content

신규 Content 11개:

- `life-family-levels`
- `life-mastery-foundation`
- `life-mastery-effects`
- `life-accessory-progression`
- `floamos-accessories`
- `prione-accessories`
- `life-mastery-tools`
- `life-artifacts-lightstones`
- `life-alchemy-stones`
- `cheongmyeong-orb`
- `energy-foundation`

기존 Content 보강 1개:

- `life-common-gear`: 기존 Content와 `life-common-gear.overview`, `life-common-gear.preparation`을 유지하면서 가문 공용 장비, 통합 UI·프리셋, 전역/분야별 슬롯, 전투·생활 장비 동시 활용, 삭제된 방어력·최대 무게 효과, 크론 정식 +250 LT를 추가했다.

권장 후보 `life-integrated-equipment`는 기존 `life-common-gear`와 의미 책임이 같아 새로 만들지 않았다. 기존 항해·교역·조련·황실 제작 납품도 중복 Content 대신 relation으로 연결했다.

## 5. canonical 데이터 범위

### 가문 생활 레벨과 숙련도

- 11개 생활 분야가 가문 단위이며 모든 캐릭터의 분야별 경험치를 합산한다.
- 최대 진행 레벨은 도인 100, 레벨 기반 숙련도와 기능 효과 상한은 도인 50이다.
- 레벨 자체 누적 숙련도는 도인 50에서 800이며 도인 51~100 추가치는 0이다.
- 최대 유효 생활 숙련도는 현재 3000이다.
- 생활 경험치와 생활 숙련도를 별도 stat 의미로 저장했다.
- 영구 생활 버프를 경험치, 숙련도, 행동 시간, 획득 확률, 기운, 탑승물·선원·교역 경험치 범주로 분리하고 이벤트 버프는 제외했다.

### 통합 장비와 액세서리

- 생활 장비는 가문 공용이다.
- 액세서리·생활 연금석·청명의 보주는 전역 슬롯이며 의복·도구·유물·광명석은 분야별 슬롯이다.
- 플로아모스는 강화 불가, 고(III) 마노스 동일 능력치, 가문당 1회 획득, 일일 1회 부위 교환으로 구조화했다.
- 프리오네는 마노스 단계별 교환, 고정 강화 확률, 비파괴·단계 하락, 크론 방지, failstack 미적용, 내구도 감소와 부위별 아그리스의 정수를 구조화했다.
- 프리오네 강화 10행과 부위별 능력치 11행을 structured value로 저장했다.

### 유물·광명석·연금석·청명의 보주

- 유물 2개, 유물당 소켓 2개, 광명석 총 4개 구조를 저장했다.
- 생활 공통 유물 효과도 장착한 생활 분야에만 적용되도록 명시했다.
- 생활 경험치·숙련도 및 채집·낚시·수렵·요리·연금·가공·조련·항해 대표 조합 10개의 현재 recipe/effect를 2026-09-02 표 기준으로 저장했다.
- 현재 recipe는 풀의 광명석/오색빛 광명석만 사용하며 과거 불·바람 계열 recipe를 섞지 않았다.
- 실제 활동 기준 자동 선택과 수렵 후 도축 시 유효한 채집 획득 확률만 적용되는 구분을 저장했다.
- 생활 연금석은 내구도·충전·수동 활성화가 없는 장착 효과 방식으로 저장했다.
- 청명의 결정 가열 제작, 결정↔보주 간이연금, 100% 강화, 0~15단계 효과·재료 수량을 구조화했다.
- 새벽 생활 경험치 수정 3종의 보상 수량은 신규 획득법이 아니라 2026-09-02 역사적 전환 보상으로 표시했다.

### 기운

- 기본 최대 기운 30과 지식 카테고리 기반 증가를 기록했다.
- 최대 기운은 가문 공유, 현재 보유 기운은 캐릭터별로 분리했다.
- 기본 자연 회복은 접속 중 3분당 1, 미접속 중 1시간당 1이다.
- 채집 기운 무소모 확률은 기존 대비 10%p 상향, 전문 3에서 상한 도달로 저장하고 공식 수치가 없는 정확한 최대 확률은 `null`로 남겼다.

## 6. superseded와 stale-data correction

superseded claim 선언은 7개에서 16개로 증가했다. 신규 9개:

- 과거 숙련도 최대치 2000: 현재 3000으로 대체
- 9월 2일 이전 생활 광명석 recipe: 최신 풀/오색빛 recipe로 대체
- 생활 연금석 내구도·충전 방식: 삭제
- 생활 연금석 수동 활성화 방식: 장착 효과로 대체
- 새벽의 수정 - 생활 경험치 3종: 청명의 보주로 대체
- 청명의 결정→보주를 가열하기로 표시한 설명: 간이연금으로 수정
- 현재 기운을 가문 공용 pool로 보는 해석: 캐릭터별 현재치로 수정
- 캐릭터별 생활 장비 workflow: 가문 공용 장비로 대체
- 생활 장비의 일부 방어력·최대 무게 효과: 삭제

이 중 2026-09-02 최신 패치 또는 같은 날 client fix에 직접 연결한 stale correction은 8개다. 나머지 1개는 2025-01-08의 숙련도 2000→3000 변경이다. superseded Evidence는 이력으로 남지만 모두 `active=false`라 현재 검증 집계에 참여하지 않는다.

## 7. CURRENT GUIDE CONFLICTS

최신 패치를 우선해 다음 충돌을 현재 active 규칙과 분리했다.

1. 채집 가이드의 생활 연금석 장착 후 별도 사용 설명: 2026-09-02 이후 내구도 없이 장착 시 효과 방식이 canonical이다.
2. Dawn Life EXP crystal 구형 설명: 진·본·원 새벽의 수정 - 생활 경험치는 현재 장비가 아니며 청명의 보주가 대체한다.
3. 과거 캐릭터별 life gear workflow: 현재 모든 생활 장비는 가문 장비이며 통합 UI에서 공유한다.
4. 과거 생활 숙련도 2000 상한: 2025-01-08 이후 최대 유효 수치는 3000이다.
5. 9월 2일 이전 불·바람 광명석 포함 생활 recipe: 현재 생활 조합은 풀/오색빛 광명석만 사용하는 교체표를 따른다.
6. 생활 장비의 과거 방어력·최대 소지 무게 효과: 2026-09-02에 명시적으로 삭제된 효과를 현재 stat으로 유지하지 않았다.

추가로 `<송곳니>`, `<대장장이의 축복>`, `<개운한 꿈>`은 삭제된 조합이고 `<하품하는 고슴도치>`의 기운 회복 효과는 제거된 상태로 저장했다.

## 8. 참조·archive·stable ID

임시 DB에서 V1.6E seed를 먼저 재구성해 적재한 뒤 V1.6F를 적재했다.

- unknown source: 0
- unknown relation: 0
- unknown evidence: 0
- unknown entity: 0
- 예상하지 않은 archive: 0
- 기존 62개 Content ID 유지: 통과
- 기존 schedule/requirement/step/reward/section/relation/checklist/evidence ID 유지: 통과
- `carrack-advance`, Ocean progression, V1.6D routine, V1.6E schedule/reset 데이터: archive/recreate 없음
- V1.6C Rinbach superseded Evidence: 상태와 ID 보존

## 9. 체크리스트·사용자 이력 보존

V1.6E 적재 후 임시 DB에 현재 daily/weekly checklist instance와 item state를 생성하고 완료 상태·시각·note를 기록했다. `carrack-advance`에는 `UserContentState` fixture를 만들었다.

V1.6F 1차·2차 적재 후:

- checklist instance 34개 유지
- checklist item state 45개 유지
- 기존 state ID와 template item 연결 유지
- 완료 상태, 완료 시각, note 유지
- `UserContentState` ID, Content 연결, 상태, priority, note 유지

플로아모스 일일 부위 교환은 새 `quest_reset / daily / 00:00 / Asia-Seoul` schedule과 기본 비활성 checklist 1개로 추가했으며 기존 checklist 이력에는 영향을 주지 않았다.

## 10. Migration·import·idempotency

실제 DB가 아닌 작업공간 내 일회성 임시 SQLite DB에서 다음 순서로 검증했다.

1. 빈 DB에 `20260902_0001` 적용
2. `20260903_0002` 적용
3. V1.6E 기준 50 Source / 62 Content 적재
4. checklist 완료 이력과 `UserContentState` fixture 생성
5. V1.6F 적재
6. 동일 V1.6F 두 번째 적재

V1.6F 첫 적재와 두 번째 적재의 전체 canonical 및 사용자 행 수가 같았다. 결과: idempotent.

최종 임시 DB 행 수:

- Source 57, Content 73
- ScheduleRule 46, Requirement 191, Step 58, Reward 161, Section 71, Relation 113
- ChecklistTemplate 35, ChecklistTemplateItem 46
- Evidence 722
- 검증 fixture 포함 ChecklistInstance 34, ChecklistItemState 45, UserContentState 1

## 11. 테스트 결과

실행:

```powershell
cd backend
uv run pytest tests/test_life_foundation_seed.py -q
uv run pytest -q -p no:cacheprovider
uv run python .tmp_v16f_verify.py  # 일회성 검증 script, 검증 후 삭제
```

결과:

- V1.6F semantic regression: **13 passed**
- 전체 backend: **52 passed**
- migration `0001 → 0002`: 통과
- V1.6E → V1.6F import: 통과
- V1.6F 두 번째 import: 행 수 불변
- 실패: 0

semantic test는 가문 생활 레벨, 숙련도 상한, 경험치/숙련도 구분, 통합 장비, 플로아모스, 프리오네, 광명석 최신 recipe, 연금석, 청명의 보주, 새벽 수정, 기운과 기존 V1.6E Content 보존을 검사한다.

## 12. 실제 DB 보호와 seed hash

`backend/bdo.db`:

- 작업 전 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 작업 후 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 크기: 118,784 bytes

실제 DB는 변경되지 않았다.

최종 seed SHA-256:

- `data/seed_sources.json`: `180BED2AD37B262C124E63A1F17AD93E2CC65C0117ECA5EAFC864BE2C3988A8A`
- `data/seed_contents.json`: `3ECD984C5E0A072BC780739ABFA85DCE31E21DFA8317FB49F832E3FF1C949B75`

## 13. unresolved facts

추정값을 만들지 않기 위해 다음은 미확정 또는 후속 팩 범위로 남겼다.

- 채집 레벨의 기운 무소모 확률이 전문 3에서 도달하는 정확한 최대 percentage: 9월 2일 source에 수치가 없어 `null`
- 생활 숙련도 0~3000 전체 50단위 효과표: foundation에는 cap과 효과 taxonomy만 저장
- 생활 광명석 전체 조합표: 이번 버전에는 분야별 대표 current recipe/effect 10개만 저장
- 재배 유물/광명석의 구체적인 current effect 목록: 최신 공식 장착표에서 확인 가능한 범위를 넘어 추정하지 않음
- 각 생활 도구 최상위 공작의 전체 재료식과 동적 거래소 가격
- 전체 음식·비약·향수·펄 버프 수치

## 14. schema gap

schema 변경 금지 범위를 지켰다. 현재 schema에서 확인된 제한:

- relation vocabulary에 `contributes_to`, `applies_to`, `equivalent_stats_to`, `obtained_from`, `replaces`, `contains`, `affects`가 없어 `related`와 `part_of` 및 relation note로 의미를 보존했다.
- 강화표, 단계별 능력치, 제작 재료와 효과 taxonomy를 전용 typed table로 표현할 모델이 없어 `ContentRequirement.structured_value`에 저장했다.
- 2026-09-03 현재 금색 산호 허리띠의 `사용/거래 중단 + 9월 9일 삭제 예정` 같은 전이 상태를 명확히 나타내는 status/effective transition 필드가 없다. 이번 pack에는 별도 Content를 만들지 않았다.
- Evidence에는 별도 `superseded_by` 컬럼이 없어 `verification_status=superseded`, `active=false`, note와 최신 Source 연결로 대체 관계를 기록했다.

## 15. 의도적 제외 범위

- 채집 장소·루트·미니게임·수익, 가공식·계산기, 요리/연금 전체 레시피
- 낚시 어종·낚시터·자낚 세팅, 재배·조련·수렵 deep progression
- Worker/Node economy, 모든 음식·비약·향수 백과
- 뉴비 구매 순위, 가성비 단계, 특정 캐릭터 추천 같은 Strategy 데이터
- 2026-09 이벤트 핫타임·패스·이벤트 숙련도/경험치 보너스
- 금색 산호 허리띠 삭제 예정 전이 Content
- UI, API, Prompt Bridge, AI, schema 및 migration 확장
