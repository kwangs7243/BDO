# V1.6E Daily / Weekly Routine Seed Pack 보고서

기준 시점: 2026-09-03 KR Live  
검증일: 2026-09-03  
결론: V1.6E 데이터 팩을 임시 SQLite DB에서 검증했으며 실제 `backend/bdo.db`에는 적재하지 않았다.

## 1. 변경 파일

- `data/seed_sources.json`
- `data/seed_contents.json`
- `backend/tests/test_routine_seed.py`
- `handoff/V16E_ROUTINE_PACK_REPORT.md`

DB schema, Alembic migration 파일, backend API, frontend/UI, 디자인, 모델 클래스, Prompt Bridge 구현은 변경하지 않았다.

## 2. 데이터 규모

| 항목 | V1.6D | V1.6E | 증감 |
|---|---:|---:|---:|
| Source | 34 | 50 | +16 |
| Content | 54 | 62 | +8 |
| ScheduleRule | 30 | 45 | +15 |
| Requirement | 116 | 145 | +29 |
| Step | 36 | 58 | +22 |
| Reward | 136 | 161 | +25 |
| Section | 40 | 54 | +14 |
| Relation | 91 | 91 | 0 |
| ChecklistTemplate | 26 | 34 | +8 |
| ChecklistTemplateItem | 26 | 45 | +19 |
| claim 선언 | 411 | 501 | +90 |
| Evidence 행(source 연결 단위) | 532 | 636 | +104 |

Evidence는 한 claim에 여러 source가 연결되면 source별 DB 행이 생기므로 claim 선언 수보다 많다.

## 3. 신규·보강 Content

신규 Content 8개:

- `black-shrine-donghae-weekly`
- `black-shrine-hwanghae-weekly`
- `atoraxxion-weekly`
- `dark-rift-cycle`
- `edania-boss-weekly`
- `infinite-potion-weeklies`
- `dream-horse-material-routines`
- `imperial-crafting-delivery-daily`

기존 Content 보강 3개:

- `blood-altar`: 주간 입장 무제한, 파티당 10회, 최고 단계 보상 주 1회, 일요일 정산을 분리했다.
- `pit-of-undying`: 주간 콘텐츠, 접근 선행 의뢰, 크론석 최대 500개, 목요일 주간 주기를 보강했다.
- `garmoth`: 자동 지역 의뢰, 주 3회 보상 한도, 목요일 초기화, 정시 출현 분리를 보강했다.

후보의 `blood-altar-weekly-reward`, `pit-of-undying-weekly`, `garmoth-weekly-reward`는 기존 logical Content와 중복이므로 새 Content로 만들지 않았다. V1.6D 대양 일일/주간 Content도 그대로 재사용했으며 집계용 중복 Content를 추가하지 않았다.

## 4. Routine schedule 유형

아래 수치는 전체 active seed의 의미별 집계다. 한 schedule이 `weekly Sunday`와 `reward settlement`에 동시에 포함될 수 있으므로 행 합계와 일치할 필요는 없다.

| 의미 | V1.6D | V1.6E | 대표 항목 |
|---|---:|---:|---|
| daily | 10 | 13 | 동해도 순위 갱신, 조련 일일, 황실 개인 한도 |
| weekly Thursday | 14 | 19 | 불멸의 나락, 아토락시온, 에다니아, 정령수 재료, 조련 주간 |
| weekly Sunday | 1 | 5 | 피의 제단 정산, 검은 사당 횟수·보상 |
| rolling cooldown | 0 | 1 | 어둠의 틈 처치 후 120시간 |
| scheduled spawn | 0 | 1 | 가모스 공식 시간표 출현 |
| reward settlement | 1 | 3 | 피의 제단, 동해도, 황해도 |

황실 제작 납품의 서버 재고 갱신은 별도 `stock_refresh / interval` schedule 1개로 저장했다. 개인 일일 한도 초기화와 합치지 않았다.

## 5. stale·superseded 처리와 semantic regression

superseded claim 선언은 5개에서 7개로 증가했다. 새 이력 2개는 다음과 같다.

- 피의 제단 가이드의 파티당 5회: 2026-07-15 패치의 10회로 대체, inactive/superseded
- 검은 사당 동해도의 과거 직접 수령·미수령 소멸 방식: 2026-04-15 자동 지급·누적으로 대체, inactive/superseded

추가한 semantic regression 11개는 다음을 고정한다.

- 동해도·황해도 주 5회, 일요일 주기, 흑정령의 선물함 자동 지급·누적
- 피의 제단 주간 입장 제한 없음, 파티당 10회, 최고 단계 보상 1회, 일요일 정산
- 아토락시온 지역별 주간 보상 1회, 시즌 보상 분기·새벽의 열쇠 요구 없음
- 어둠의 틈 6종, 우두머리별 120시간, 우두머리별 크론석 100개, 목요일 reset 없음
- 가모스 주 3회 보상과 목요일 reset, scheduled spawn 분리
- 아침의 나라 월드 우두머리 현재 주간 의뢰 Content 0개
- 에다니아 주 1개 우두머리와 목요일 reset
- 정령수 재료 6종 모두 가능 및 최신 목표 수치
- 고비 뿌리 주간 택 1 보상 총 50개
- 황실 요리·연금 독립 한도와 개인/서버 주기 분리
- importer 이후 superseded 이력 상태

## 6. 참조·archive·안정 ID 검증

임시 DB에서 V1.6D seed를 먼저 적재하고 V1.6E를 적재했다.

- unknown source: 0
- unknown relation: 0
- unknown evidence reference: 0
- unknown entity: 0
- importer가 거부한 unknown reference: 0
- 예상하지 않은 archive: 0
- 기존 54 Content ID 유지: 통과
- 기존 schedule/requirement/step/reward/section/relation/checklist/evidence ID 유지: 통과
- V1.6C Rinbach superseded 이력 및 V1.6D Ocean 행: archive/recreate 없음
- `carrack-advance`를 포함한 기존 Content: ID 유지

신규 routine에서 공통 weekly framework로 향하는 중복 relation은 만들지 않았다. 주기 연결은 각 Content의 schedule과 checklist `period_rule_seed_key`로 표현했고 기존 relation 수 91개를 유지했다.

## 7. 체크리스트·사용자 이력 보존

V1.6D 적재 뒤 임시 DB에 실제 fixture를 만들고 V1.6E를 적재했다.

- 기존 주간 checklist instance: 보존
- 기존 `ChecklistItemState` ID와 template item 연결: 보존
- 완료 상태, 완료 시각, note: 보존
- 기존 `UserContentState` ID, Content 연결, 상태, note: 보존
- 새 routine 때문에 기존 Ocean checklist가 archive/recreate된 항목: 0

검증 fixture를 포함한 V1.6E 첫 적재와 재적재의 측정값은 각각 checklist instance 16, item state 16, user content state 1로 동일했다.

## 8. Migration·import·멱등성

실제 DB가 아닌 `D:/BOD/.tmp_v16e_verify/v16e.db`에서 다음 순서를 실행했다.

1. 빈 SQLite DB에 `20260902_0001` 적용
2. `20260903_0002` 적용
3. V1.6D 기준 seed 34 Source / 54 Content 적재
4. 완료 체크 이력과 UserContentState fixture 생성
5. V1.6E 적재
6. 동일 V1.6E 재적재

첫 번째와 두 번째 V1.6E 적재 후 모든 canonical 및 사용자 행 수가 동일했다. 결과: idempotent.

## 9. 테스트 결과

실행 명령:

```powershell
cd backend
.\.venv\Scripts\python.exe -m pytest -q --basetemp D:\BOD\.tmp_pytest_final
```

결과:

- 전체 backend: **39 passed**
- V1.6E semantic 및 seed/importer 대상: **15 passed**
- 실패: 0
- 경고: sandbox 권한 때문에 기존 `backend/.pytest_cache`에 쓸 수 없다는 PytestCacheWarning 1건. 테스트 결과와 임시 DB에는 영향 없음.

## 10. 실제 DB 보호

`backend/bdo.db`:

- 작업 전 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 작업 후 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 크기: 118,784 bytes
- 수정 시각(UTC): 2026-09-02 15:37:03

실제 DB는 변경되지 않았다.

최종 seed 파일 SHA-256:

- `data/seed_sources.json`: `56B6F864CF9049A1CEEFC2DC7183B981FC2EE5CCBECC7B5B01FD1C157F399721`
- `data/seed_contents.json`: `A53A0AE013134D2CFBC3D7527C6FDC4EC0E5F282251D2A25C64B039FA47BC62A`

## 11. unresolved factual details

낡은 값이나 추정값을 넣지 않기 위해 다음은 의도적으로 미확정으로 남겼다.

- 불멸의 나락 등급별 세부 토큰 보상표
- 조련 등급별 일일 고비 뿌리 수량
- 최대 공헌도 ÷ 2의 홀수 공헌도 정수 처리 방식
- 가모스의 요일·시각별 실제 출현표: 정시 출현 유형만 모델링하고 live 시간표는 고정하지 않음
- 에다나 도전의 증표가 연결되는 권좌 PvP 전체 규칙: 별도 Content가 없어 relation을 억지로 만들지 않음

아침의 나라 월드 우두머리는 2025-12-23 이후 주간 의뢰가 삭제되고 직접 전리품 방식이므로 현재 weekly Content를 만들지 않았다.

## 12. 의도적 제외 범위

- 이벤트 daily/weekly, 로그인 보상, 핫타임, 이벤트 추가 재료·우두머리
- 사소한 마을 공헌도 반복 의뢰
- 시즌 한정 콘텐츠와 시즌 교환량
- PvP 시즌 보상·교환표, 붉은 전장 및 솔라레 전체 보상
- 모든 길드 임무, 특수 소환서, 생활 일일 의뢰 전수
- 왕실 공방 상세, 재배 세부 루프
- UI, API, Prompt Bridge, 디자인 및 기능 확장

## 13. schema gap

schema 변경 금지 범위를 지켰다. 다만 현재 `ScheduleRule`에는 rolling 기준 시점/간격, interval 시간 수, scheduled timetable, 지급 종료 시각을 위한 전용 컬럼이 없다.

- 어둠의 틈: `respawn / rolling`과 notes의 120시간, Requirement structured value로 표현
- 가모스: `spawn / scheduled`로 유형만 표현
- 황실 서버 재고: `stock_refresh / interval`과 Requirement의 3시간 값으로 표현
- 황해도 정산 종료: 시작 시각 00:00과 notes의 00:00~00:10으로 표현

이 schedule들은 checklist period driver로 연결하지 않았다. 현재 period engine은 `quest_reset`과 `attempt_reset`의 daily/weekly만 계산하므로 기존 기능 동작에는 영향을 주지 않는다. 향후 이 비정형 일정을 계산·알림에 사용하려면 별도 milestone에서 schema/API 설계가 필요하다.
