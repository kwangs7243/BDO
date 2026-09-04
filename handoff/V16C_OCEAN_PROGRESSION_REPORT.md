# V1.6C Ocean Progression & Barter Seed Report

검증일: 2026-09-03 KST

## 1. 결과 요약

V1.6B canonical seed를 유지한 채 V1.6C Ocean progression 및 물물교환 데이터만 확장했다. DB schema, migration 파일, backend API, frontend/UI, 디자인, AI/Prompt Bridge 및 모델 클래스는 변경하지 않았다.

- Source: 23 → 27
- Content: 27 → 41
- 신규 Content: 14
- 갱신 Content: 1 (`carrack-advance`의 relation 3건 추가)
- 신규 evidence claim 선언: 104
- 갱신 evidence claim 선언: 0
- Evidence source 연결: 343 → 448, 105건 증가
- Relation: 20 → 57, 37건 증가
- Superseded claim: 3
- 실제 `backend/bdo.db`: 미변경

## 2. 수정 파일

- `data/seed_sources.json`
- `data/seed_contents.json`
- `handoff/V16C_OCEAN_PROGRESSION_REPORT.md`

기능 코드, 테스트 코드, 스키마 및 migration 파일은 수정하지 않았다.

최종 seed SHA-256:

- `data/seed_sources.json`: `196941A307E15C6D770218EEB6FFDCEAD8C5B2C4E1578CD22106DD34DDC21EC3`
- `data/seed_contents.json`: `19C441E54FBB4AE0CF9E852B968493EF60073D7C3B370EC507904BB03C0AF806`

## 3. Source 변경

신규 Source 4건:

1. `barter-improvement-2026-04-15`
   - Pearl Abyss KR 2026-04-15 업데이트
   - 물물교환 단계 가격·무게, 교섭력, 수송 제한, 까마귀의 둥지, 돌발 물물교환, 6·7단계 교역
2. `ocean-progression-2026-08-26`
   - Pearl Abyss KR 2026-08-26 업데이트
   - 린바크, 팔라시 장비, 노란색 선박 장비 강화, 항해 음식·영약
3. `sea-crystal-guide`
   - Pearl Abyss KR 모험가 가이드 `해원석`
   - 해원석 progression, 루살카 효과·제작식·상점가
4. `barter-route-distance-community-2026-05-31`
   - 공식 사이트 내 2026-05-31 팁 게시물
   - 날짜와 계산 가정을 명시한 6·7단계 동선 측정

기존 `life-unification-2026-09-02`는 URL과 ID를 유지하고 설명 범위에 린바크 군락지 개선을 추가했다. 기존 `ocean-barter-rework-2024-03-27`과 `carrack-guide`는 중복 Source를 만들지 않고 재사용했다.

## 4. Content 변경

신규 Content 14건:

1. `barter-current-system`
2. `barter-stage-values`
3. `barter-tier6-routes`
4. `barter-tier7-routes`
5. `barter-route-strategy`
6. `crow-coin-material-shop`
7. `carrack-types`
8. `carrack-upgrade-materials`
9. `carrack-chiro-gear`
10. `carrack-palasi-gear`
11. `carrack-palasi-enhancement`
12. `rinbach-colony`
13. `sea-crystals`
14. `ocean-consumables`

기존 `carrack-advance`는 중복 생성하지 않았다. 기존 nested `seed_key`는 모두 유지하고 `carrack-types`, `carrack-upgrade-materials`, `carrack-chiro-gear`로 이어지는 relation만 추가했다.

## 5. Canonical row 수

| 종류 | V1.6B | V1.6C | 증감 |
|---|---:|---:|---:|
| Source | 23 | 27 | +4 |
| Content | 27 | 41 | +14 |
| ScheduleRule | 26 | 27 | +1 |
| ContentRequirement | 22 | 61 | +39 |
| ContentStep | 30 | 31 | +1 |
| Reward | 61 | 109 | +48 |
| ContentSection | 24 | 36 | +12 |
| ContentRelation | 20 | 57 | +37 |
| ChecklistTemplate | 22 | 23 | +1 |
| ChecklistTemplateItem | 22 | 23 | +1 |
| Evidence claim 선언 | 234 | 338 | +104 |
| Evidence source 연결(DB row) | 343 | 448 | +105 |

V1.6C import 후 active row는 Reward 106, Evidence 445다. 차이 3건씩은 삭제된 린바크 교환의 의도적인 이력 보존이다.

## 6. 최신값 및 supersede 처리

### 까마귀 주화 상점

2024-03-27 공식 패치 값을 current canonical로 사용했다. `중범선 만들기` 가이드에 남아 있는 아래 구식 가격은 active claim으로 저장하지 않았다.

- 달의 핏줄이 새겨진 아마포 40
- 짙은 파도빛이 감도는 규격 각목 80
- 화려한 암염 주괴 400
- 화려한 진주 결정 400
- 심해의 눈물 400

Semantic 검사 결과 위 다섯 구식 가격과 일치하는 active 상점 가격은 0건이다.

### 린바크 교환

2026-08-26에 추가됐던 아래 세 교환은 2026-09-02 패치에서 삭제됐다.

- 린바크의 뼈 1 → 파도의 블랙스톤 8
- 린바크의 비늘 1 → 파도의 블랙스톤 12
- 린바크의 진액 1 → 파도의 블랙스톤 20

세 Reward row는 `active=false`, 대응 Evidence는 `verification_status=superseded`, `active=false`로 보존했다. 각 row에는 2026-09-02 삭제 사실을 별도의 active verified Evidence로 연결했다. 따라서 현재 보상이나 교환으로 집계되지 않는다.

### 치로/팔라시

active claim에서 치로를 현재 최종 또는 최상위 장비로 표현한 항목은 0건이다. 현행 장비 progression은 `토로 → 치로 → 팔라시`이며, 팔라시 16종과 제작·강화 기준을 별도 Content로 구조화했다.

## 7. JSON 및 참조 검증

통과 항목:

- `seed_sources.json` UTF-8 JSON parse
- `seed_contents.json` UTF-8 JSON parse
- Source ID 중복 없음
- Content slug 중복 없음
- nested `seed_key`의 content slug prefix 확인
- unknown source reference: 0
- unknown relation target: 0
- unknown evidence entity reference: 0
- importer enum/구조 검증 통과
- 구식 active 까마귀 주화 가격: 0
- active 린바크 stale exchange: 0
- 치로를 최종 장비로 단정하는 active claim: 0
- 팔라시 progression 존재 확인

Archive 결과:

- 의도적 inactive Reward: 3
- 의도적 inactive Evidence: 3
- 예상하지 못한 inactive/archive: 0

## 8. Migration, import 및 멱등성

실제 DB가 아닌 완전한 임시 SQLite DB에서 다음 순서로 검증했다.

1. Alembic 빈 DB → `20260902_0001`
2. `20260902_0001` → `20260903_0002`
3. 재구성한 V1.6B canonical seed import
4. 기존 checklist instance/state와 `carrack-advance` UserContentState 생성
5. V1.6C seed 1회 import
6. 동일 V1.6C seed 2회 import
7. row 수, stable ID, 사용자 이력 및 archive 비교

최종 revision: `20260903_0002`

첫 번째와 두 번째 V1.6C import 후 row 수:

| 테이블 | 1회 | 2회 |
|---|---:|---:|
| source | 27 | 27 |
| content | 41 | 41 |
| schedule_rule | 27 | 27 |
| content_requirement | 61 | 61 |
| content_step | 31 | 31 |
| reward | 109 | 109 |
| content_section | 36 | 36 |
| content_relation | 57 | 57 |
| checklist_template | 23 | 23 |
| checklist_template_item | 23 | 23 |
| evidence | 448 | 448 |

멱등성 결과: 통과. 두 번째 import 후 모든 canonical 및 active row 수가 동일했다.

## 9. Stable ID 및 사용자 이력 보존

임시 DB에서 확인한 결과:

- V1.6B 기존 Content 27개의 DB ID 모두 유지
- `carrack-advance` DB ID `7` 유지
- 기존 `carrack-advance` requirement/step/section/evidence 32개 DB ID 모두 유지
- 기존 checklist instance ID와 period key 유지
- 기존 checklist item state ID, `completed=true`, 완료 시각 및 메모 유지
- 기존 `carrack-advance` UserContentState ID, `in_progress`, priority 및 메모 유지
- V1.6B 기존 Ocean Content 20건 모두 유지

## 10. 테스트 결과

- seed importer tests: `4 passed`
- backend 전체 tests: `28 passed in 19.45s`
- 임시 DB migration: 통과
- V1.6B → V1.6C import: 통과
- 동일 seed 2회 import: 통과
- history/UserContentState 보존: 통과
- semantic stale 검사: 통과

frontend/UI 및 Prompt Bridge 코드는 변경하지 않았으므로 별도의 frontend build는 수행하지 않았다.

## 11. 실제 DB 미변경 확인

`backend/bdo.db`에는 migration 또는 seed import를 실행하지 않았다.

작업 전후 확인값:

- SHA-256 전: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- SHA-256 후: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 크기: 118,784 bytes
- 마지막 수정 시각(UTC): 2026-09-02 15:37:03

해시, 크기와 수정 시각이 모두 동일하다.

## 12. 의도적으로 제외한 범위

지시서의 V1.6C 범위를 넘는 다음 항목은 추가하지 않았다.

- 모든 선원 성격/개별 스탯 백과
- 모든 섬별 물물교환 좌표
- 실시간 최적 물물교환 계산기
- 해양 보물 전체
- 판옥선 전체 progression
- 해상 PvP
- 길드 갤리선
- 모든 해왕류 사냥터 백과
- UI/디자인/API/Prompt Bridge 변경

## 13. Schema gap

V1.6C 데이터를 저장하고 import하는 데 blocking schema gap은 없었다.

비차단 제약은 한 가지다. DB `Evidence` 모델에는 `superseded_by`가 있지만 현재 seed importer 입력 형식은 이 필드의 seed 연결을 받지 않는다. 이번 pack은 기존 importer가 지원하는 `verification_status=superseded`와 `active=false`를 사용하고, 최신 삭제 근거를 별도 active Evidence로 연결해 동일한 현재 집계 의미를 보장했다. 이 제약 때문에 schema나 importer를 확장하지 않았다.

