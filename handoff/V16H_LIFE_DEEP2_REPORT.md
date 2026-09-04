# V1.6H Cooking / Alchemy / Training / Hunting Deep Seed Pack 보고서

기준 시점: **2026-09-03 KR Live**  
검증일: 2026-09-03  
결론: V1.6G 기준 데이터 위에 요리·연금·조련·수렵 28개 Content를 추가했다. 별도 SQLite DB에서 V1.6G baseline부터 V1.6H를 두 번 적재해 migration, 멱등성, 기존 ID와 사용자 이력 보존을 확인했다. 실제 `backend/bdo.db`에는 적재하지 않았다.

단, backend 전체 테스트에는 V1.6G 당시 총량 `72 Source / 92 Content`를 고정 검증하는 과거 테스트 1건이 남아 있다. 현재 V1.6H 총량 `84 / 120`과 충돌하지만 `backend/tests/test_life_deep1_seed.py`는 이번 지시서의 변경 대상이 아니므로 수정하지 않았다. V1.6H 전용 semantic test 17건과 나머지 backend test 86건은 통과했다.

## 1. 변경 파일

- `data/seed_sources.json`
- `data/seed_contents.json`
- `backend/tests/test_life_deep2_seed.py`
- `handoff/V16H_LIFE_DEEP2_REPORT.md`

DB schema, Alembic migration, backend API, frontend/UI, 디자인, Prompt Bridge, AI, 모델과 실제 사용자 DB는 변경하지 않았다.

## 2. 데이터 규모

| 항목 | V1.6G | V1.6H | 증감 |
|---|---:|---:|---:|
| Source | 72 | 84 | +12 |
| Content | 92 | 120 | +28 |
| ScheduleRule | 50 | 50 | 0 |
| Requirement | 257 | 323 | +66 |
| Step | 58 | 58 | 0 |
| Reward | 161 | 161 | 0 |
| Section | 77 | 77 | 0 |
| Relation | 156 | 173 | +17 |
| ChecklistTemplate | 35 | 35 | 0 |
| ChecklistTemplateItem | 46 | 46 | 0 |
| claim 선언 | 669 | 714 | +45 |
| Evidence 행 | 836 | 885 | +49 |
| superseded claim 선언 | 23 | 32 | +9 |

한 claim에 Source가 여러 개 연결되면 Source마다 Evidence 행이 생성되므로 Evidence 행 수는 claim 선언 수보다 많다.

## 3. Source 변경

신규 공식 Source 12개를 추가했다.

### Alchemy

- `alchemy-basic-guide`
- `alchemy-guide`
- `alchemy-stone-guide`
- `alchemy-products-2024-03-20`

### Training

- `training-guide`
- `dream-horse-awakening-guide`
- `rare-wild-horses-2025-12-23`

### Hunting

- `hunting-guide`
- `hunting-enhancement-guide`
- `sniper-reward-rework-2023-05-03`
- `marni-sniper-crafting-2026-03-25`
- `marni-sniper-enhancement-2026-04-01`

중복 URL은 새 Source를 만들지 않고 기존 Source ID를 재사용했다.

- 요리 가이드: `cooking-guide`
- 2026-01-14 패치: `dark-rift-reward-2026-01-14`
- 꿈결 환상마 가이드: `mythical-horse-guide`
- 2026-07-15 패치: `blood-altar-challenge-2026-07-15`
- 생활 숙련도: `life-mastery-prione-2025-01-08`
- 생활 장비·수렵 최신 변경: `life-unification-2026-09-02`
- 2025-05-14 생활 성장 의뢰·황실 연금표: `ocean-iliya-consolidation-2025-05-14`

최종 JSON에서 Source ID와 URL은 각각 84/84 unique이며, 모든 Evidence의 source reference가 존재한다.

## 4. 신규 Content

기존 92개 Content와 의미 중복을 점검한 뒤 지시서 후보 28개를 모두 신규로 추가했다. 기존 Content의 본문과 중첩 데이터는 보강하지 않았다.

### Cooking

- `cooking-current-system`
- `cooking-mastery-effects`
- `cooking-mass-production`
- `witch-delicacy`
- `cooking-growth-surprise-quest`

### Alchemy

- `alchemy-current-system`
- `alchemy-mastery-effects`
- `alchemy-products-and-byproducts`
- `alchemy-growth-surprise-quest`
- `alchemy-imperial-current`
- `alchemy-stone-current-progression`
- `alchemy-stone-growth`

### Training

- `training-current-system`
- `training-mastery-effects`
- `wild-horse-capture`
- `horse-breeding-exchange`
- `horse-imperial-delivery`
- `courser-system`
- `dream-horse-awakening`
- `mythical-dream-horse`
- `training-growth-surprise-quest`

### Hunting

- `hunting-current-system`
- `hunting-mastery-effects`
- `hunting-firearms`
- `sniper-hunting`
- `marni-sniper-rifle`
- `group-hunting-whale-khalk`
- `hunting-growth-surprise-quest`

## 5. 보강 Content와 기존 기반 재사용

기존 Content 자체는 수정하지 않았다. 다음 기반은 Relation으로 재사용했다.

- `life-mastery-foundation`
- `life-common-gear`
- `life-alchemy-stones`
- `imperial-crafting-delivery-daily`
- `dream-horse-material-routines`
- `gathering-current-system`

요리·연금 황실 납품 reset, V1.6F 통합 생활 장비, V1.6F 통합 생명의 연금석, V1.6E 환상마 재료 routine을 복제하지 않았다.

## 6. Cooking semantic 결과

- 실제 요리 시간 하한: 1초
- 대량 요리: 10회 이상 연속 요리에서 발동
- 대량 요리 발동 시 재료 10회분 소비, 결과 10회분 생성, 도구 내구도는 1만 소비
- 숙련도 3000: 대량 요리 100%, 일반 요리 최대 결과물 획득 확률 76.45%
- 상위 요리 획득 확률 증가 24.20%, 상위 요리 최대 결과물 획득 확률 76.45%, 황실 납품 추가 이익 181.25%를 서로 다른 효과로 저장
- 마녀의 별미: 요리 부산물이며 맥주·우유·공헌도 경험치와 요리 경험치 교환 용도
- 성장 깜짝 의뢰: 일일 제한 없음, 같은 요리 분야 동시 진행 1개, 다른 생활 분야와 병행 가능
- 구식 `하이델 병사들을 위한 요리` claim: `superseded`, `active=false`
- 기존 `imperial-crafting-delivery-daily`: active 상태와 ID 유지

## 7. Alchemy semantic 결과

- 주거지 연금술 도구, 재료 투입과 실패 시 재료 소비를 구조화
- 숙련도 3000: 최대 결과 62.50%, 일반 추가 3.83%, 특수 추가 2.98%, 희귀 추가 0.36%
- 2024-03-20 추가 결과물 개편의 대표 상향·신규 품목을 기록하고 2026 연금석 명칭 체계에 우선권 부여
- 성장 깜짝 의뢰: 일일 제한 없음, 같은 연금 분야 동시 진행 1개
- 구식 달리사인의 간단한 시험: `superseded`, `active=false`
- 2025-05-14 이후 황실 연금 apprentice~guru 전체 포장 수량표 저장
- 일반 연금석 현재 단계: imperfect, sturdy, sharp, resplendent, splendid, shining
- rough·polished 단계와 실패 시 하락·파괴 설명: `superseded`, `active=false`
- 성장 실패 시 단계 하락·파괴 없음
- 파괴·수호·생명 유형별 고대의 모루 적용
- 충만한 창공의 정수 제작식과 성장/결합 용도 분리
- 연마도 150% 기준 5개 성장 구간의 성공률·아그리스 정수·충만한 창공의 정수 수량 저장
- 일반 파괴·수호·생명 연금석과 V1.6F 통합 생명의 연금석은 별도 의미로 유지

## 8. Training semantic 결과

- 숙련도 3000 기여분: 포획 +43.75%, 탑승물 경험치 +93.75%, 높은 세대 결과 +13%
- 해당 값은 최종 절대 확률이 아닌 숙련도 증가 효과로 저장
- 현재 주요 야생마 세대 6~8, 2026-07-15 개체 수 증가 근거 연결
- 2025-12-23 희귀 수·암말 가치, 성장 속도, 암말 교배 3회와 8세대 준마 특화 개체 기록
- 교배와 두 부모 말이 사라지는 교환을 분리
- 황실 말 납품: 말 Lv.15 이상, 은화·황금빛 보답 인장-[황실 조련]·망념의 꽃
- 8세대 준마 필수 기술 7개
- 환상마 각성: 30레벨 8세대 준마, 기술·기품·체력 합계 200%, 각 항목 최대 180%
- 100% 초과 구간 재료 1개당 0.5, 크로그달로의 근원석 1개
- 실패 시 기본 훈련 초기화, 크론석 사용 시 훈련 수치 50% 소실, 실패 누적 확률 증가를 구분
- 환상마: 아두아나트·디네·둠
- 꿈결 환상마: 꿈결 아두아나트·디네·둠, 기본 3%, 실패마다 +0.2%p, 가문 공유
- 구식 꿈결 둠 미지원 claim: `superseded`, `active=false`
- 성장 의뢰: 야생마 포획 또는 지정 황실 말 납품 trigger와 선택 보상 기록

## 9. Hunting semantic 결과

- 일반 전투 무기와 수렵용 화승총·저격총을 구분하고 처치 후 도축용 칼 사용을 기록
- 숙련도 2000/3000 수렵 채집물 수량 증가: +300%/+375%
- 화승총 강화 실패 하락: +1~6 0%, 7→8 10%, 8→9 50%, 9→10 100%
- 저격 수렵 보상은 2023-05-03 이후 누적 손상도 0%, 1~40%, 41~80% 구간 사용
- 구식 숙련도 250/500/900만으로 희귀 보상을 판정하는 claim: `superseded`, `active=false`
- 마르니 저격총 제작: 응축된 마력의 검은 결정 10
- 마르니 저격총 최신 강화: 응축된 마력의 블랙스톤
- 사르는 태양의 원석 제작식과 2026-03-25의 구형 강화 재료 claim: `superseded`, `active=false`
- 2026-09-02: 수렵복 전용 방어 제거, 전투 장비 방어 적용
- 아침의 나라 저격 수렵 몬스터 HP +10%, 라우라우·산발바닥·대왕고래 제외 대부분 수렵 몬스터 +20%
- 대왕 고래 상위 20개 파티와 해당 파티원별 도축 기회, 도망자 칼크 상위 5개 파티 규칙 저장
- 낡은 전체 드롭 확률표는 만들지 않고 대표 전리품 범주와 요리·연금 재료 Relation만 저장
- 수렵 성장 의뢰 대상 4개 지역/그룹, 대표 보상 범주와 사냥꾼의 새벽 30분 효과 저장
- 구식 수렵 돌발 의뢰 claim: `superseded`, `active=false`

## 10. CURRENT GUIDE CONFLICTS

최신 KR Live patch와 전용 가이드를 일반·과거 가이드보다 우선했다.

### A. 연금석

과거 연금석 가이드의 거친·다듬어진 단계를 현재 단계로 사용하지 않았다. 2026-01-14 패치의 6단계 체계, 실패 시 무하락·무파괴, 고대의 모루, 충만한 창공의 정수를 current로 적용했다.

### B. 통합 생명의 연금석

2026-09-02의 통합 생명의 연금석은 내구도·수동 활성화가 제거된 장착 효과다. 이를 모든 일반 파괴·수호 연금석에 확대 적용하지 않았다.

### C. 조련 가이드

일반 가이드의 꿈결 둠 누락 가능성과 특정 NPC만 가능한 것처럼 보이는 설명보다 전용 현행 가이드를 우선했다. 꿈결 둠을 current type에 포함했고, 준마 훈련 위치는 굴라·히아신스·멜러비를 안내하되 하나의 NPC만 가능하다고 제한하지 않았다.

### D. 수렵 가이드

2025 계열 수렵 가이드보다 2026-04-01 마르니 저격총 강화 재료와 2026-09-02 전투 장비 방어·수렵 몬스터 HP 조정을 우선했다.

### E. 요리 장비 흐름

요리 가이드에 2026-09-02 이전 생활 장비 흐름이 남아 있더라도 V1.6F 통합 생활 장비가 우선한다. 이번 Pack에서 별도 구형 장비 progression을 만들지 않았다.

## 11. current patch > guide 적용 사례

- 연금석: `2026-01-14 patch > wikiNo=101`
- 마르니 저격총 강화: `2026-04-01 patch > 2026-03-25 patch > 일반 수렵 guide`
- 수렵 방어·HP: `2026-09-02 patch > 일반 수렵 guide`
- 희귀 야생마와 서식 개체 수: `2025-12-23 / 2026-07-15 patch > 일반 조련 guide`
- 꿈결 환상마 종류·실패 누적: 전용 꿈결 환상마 guide > 일반 조련 guide
- 생활 장비: `2026-09-02 patch > 요리/연금/수렵 일반 guide의 과거 장비 표현`

## 12. superseded와 archive

superseded claim 선언은 23개에서 32개로 늘었다. 신규 9개 이력은 다음과 같다.

- 하이델 병사들을 위한 구식 요리 의뢰
- 달리사인의 간단한 시험
- 연금석 거친·다듬어진 포함 과거 단계
- 연금석 성장 실패 하락·파괴
- 꿈결 둠 미지원
- 저격 희귀 보상을 숙련도 구간만으로 판정
- 마르니 저격총 사르는 태양의 원석 제작
- 마르니 저격총의 2026-03-25 강화 재료
- 구식 수렵 돌발 의뢰

모두 `verification_status=superseded`, `active=false`이며 current verification 집계에 참여하지 않는다. 임시 DB 비교에서 기존 active row가 비활성화된 예상 밖 archive는 0건이다.

## 13. 참조·stable ID·이력 검증

V1.6G 72 Source / 92 Content를 임시 DB에 먼저 적재한 후 V1.6H를 적재했다.

- unknown source: 0
- duplicate source ID: 0
- duplicate source URL: 0
- unknown relation target: 0
- unknown evidence source: 0
- unknown entity: 0
- 예상하지 않은 archive: 0
- 기존 Content stable ID: 92/92 유지
- 기존 seed-key 중첩 ID: 1,676/1,676 유지
- ChecklistInstance: 35/35 유지
- ChecklistItemState: 46/46 유지
- 완료 여부·완료 시각·note fixture: 유지
- UserContentState: 1/1 유지
- UserContentState의 ID, Content 연결, `in_progress`, priority, note: 유지

V1.6H Content에는 반복 주기를 추정해 ChecklistTemplate이나 ScheduleRule을 추가하지 않았다.

## 14. Migration·import·idempotence

실제 DB가 아닌 일회성 임시 SQLite DB에서 다음 순서로 검증했다.

1. 빈 DB에 `20260902_0001` 적용
2. `20260903_0002` head 적용
3. V1.6G 기준 72 Source / 92 Content 적재
4. 기존 ChecklistInstance 35개, ItemState 46개, UserContentState 1개 fixture 생성
5. V1.6H 적재
6. 동일 V1.6H 재적재
7. 1차와 2차 canonical row count 비교

1차와 2차 적재 후 행 수는 완전히 같았다.

- Source 84, Content 120
- ScheduleRule 50, Requirement 323, Step 58, Reward 161, Section 77, Relation 173
- ChecklistTemplate 35, ChecklistTemplateItem 46
- Evidence 885
- fixture 포함 ChecklistInstance 35, ChecklistItemState 46, UserContentState 1

임시 검증 DB와 일회성 스크립트는 검증 후 제거했다.

## 15. 테스트 결과

실행:

```powershell
cd backend
uv run pytest -q -p no:cacheprovider tests/test_life_deep2_seed.py
uv run pytest -q -p no:cacheprovider
uv run python .tmp_v16h_verify.py  # 일회성 검증 후 삭제
```

결과:

- V1.6H semantic regression: **17 passed in 29.91s**
- backend 전체: **86 passed, 1 failed in 103.17s**
- 실패한 테스트: `test_life_deep1_seed.py::test_v16g_seed_json_and_logical_content_are_unique`
- 실패 원인: V1.6G snapshot test가 전체 파일의 Source/Content 수를 과거 값 72/92로 고정 검증하지만 현재 V1.6H는 84/120임
- seed importer tests: **4 passed**
- migration `0001 -> 0002`: 통과
- V1.6G baseline → V1.6H import: 통과
- 동일 V1.6H 두 번째 import: canonical 행 수 불변
- 데이터·import·보존 관련 실패: 0

과거 테스트 수정은 V1.6H 변경 대상 네 파일 밖이므로 수행하지 않았다.

## 16. 실제 DB 보호와 hash

`backend/bdo.db`:

- 작업 전 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 작업 후 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 크기: 118,784 bytes

실제 사용자 DB는 변경되지 않았다.

최종 seed SHA-256:

- `data/seed_sources.json`: `E22CF919C5F5805C078053A6B78E9FBC653DC9103CDBDCB9C0FDCB6A959CCF4C`
- `data/seed_contents.json`: `2A96D3E9C1F1CB0D163A080830CFF6AC4B7820781D7EFF51B04D7863E92F1E46`

## 17. unresolved facts

공식 근거가 부족한 값은 추정하지 않았다.

- 공식 source로 확정되지 않은 개별 요리·연금 recipe 확률
- 환상마 각성의 기본 성공 확률
- 야생마 정확한 respawn 시간
- 말 개별 품종별 최종 성장 stat
- 시간당 조련·수렵 수익
- 대왕 고래·도망자 칼크의 모든 드롭 확률과 수량
- 모든 수렵 몬스터의 절대 HP
- 모든 요리·연금 거래소 ROI
- 2026-07-15 야생마 증가의 전체 위치표

community 측정값을 canonical fact로 넣지 않았다.

## 18. intentionally excluded scope

- 모든 요리·연금 recipe를 포함하는 Full Recipe Database
- 모든 황실 상자의 수익성 계산
- 교배 확률 전체 matrix와 말 성장 simulator
- 스킬 변경권 효율과 마구 전체 백과
- 수렵터 시간당 수익, 저격 rotation과 지역별 고기 수익
- 모든 대왕 고래·칼크 drop table
- UI, API, 디자인, Prompt Bridge, AI, schema와 migration 확장
- 실제 `backend/bdo.db` import

## 19. schema gaps

- 요리·연금 recipe, 연금석 성장표, 말 progression과 수렵 보상표 전용 typed table이 없어 `ContentRequirement.structured_value`에 저장했다.
- `ContentRelation.relation_type`의 도메인별 어휘가 제한적이어서 `related`, `part_of`, `source_for`와 note를 사용했다.
- 아이템·말 품종·수렵 몬스터를 독립 catalogue로 다루는 모델이 없어 현재 Pack의 핵심 규칙과 대표 범주만 저장했다.
- 확률 증가와 최종 절대 확률을 타입 수준에서 강제하는 필드가 없어 structured value에 `absolute_probability=false`를 명시했다.
- DB의 `Evidence.superseded_by`를 seed importer가 직접 연결하지 않아 `verification_status=superseded`, `active=false`와 최신 Evidence로 교체 이력을 보존했다.
- 생활 성장 깜짝 의뢰의 “같은 분야 하나만 동시 진행”을 공통 정책 객체로 재사용하는 모델이 없어 각 Content requirement에 동일 의미를 명시했다.
- V1.6G snapshot test가 전체 seed 총량을 고정하는 구조라 후속 Pack 확장 시 stale해진다. 이번 변경 범위에서는 해당 테스트를 수정하지 않았다.
