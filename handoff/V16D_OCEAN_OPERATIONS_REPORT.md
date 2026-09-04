# V1.6D Ocean Operations, Crew & Panokseon Seed Report

검증일: 2026-09-03 KST

## 1. 결과 요약

V1.6C canonical seed와 안정 ID를 유지하면서 V1.6D 대양 실전 운용·선원·해양 사냥·에벤루스의 놀·판옥선 progression 데이터를 추가했다. 기존 오킬루아 일일 4종·주간 3종은 같은 목적의 새 Content를 만들지 않고 기존 행의 누락 보상만 보강했다.

- Source: 27 → 34
- Content: 41 → 54
- 신규 Content: 13
- 갱신 Content: 9
- Evidence claim 선언: 338 → 411
- Evidence source 연결: 448 → 532
- Relation: 57 → 91
- 실제 `backend/bdo.db`: 미변경
- 스키마·migration·backend API·frontend/UI·디자인·AI/Prompt Bridge·모델 코드: 미변경

## 2. 수정 파일

- `data/seed_sources.json`
- `data/seed_contents.json`
- `handoff/V16D_OCEAN_OPERATIONS_REPORT.md`

최종 seed SHA-256:

- `data/seed_sources.json`: `DE42B1131795F208A193045E7561E2C46AA23A1C9FDB802834EA21DD0BD694D5`
- `data/seed_contents.json`: `0342D73BDC0B01A909861748C9DE21C9DAB45ECB6D5BC7D1EB638ECFBD094D2D`

## 3. Source 변경

신규 공식 Source 7건:

1. `ocean-all-guide` — 대양의 모든 것
2. `ocean-crew-roles-2025` — 부선장과 선원 관리 UI
3. `carrack-sailor-fishing-2025` — 중범선 선원 자동 낚시
4. `hollow-maretta-update-2023-11-22` — 공허한 마레타 출현 간격 변경
5. `treasure-items-guide` — 보물 아이템 만들기
6. `ebenruth-update-2025-02-12` — 바다의 눈물이 담긴 에벤루스의 놀·내구도 제거
7. `panokseon-guide` — 판옥선

기존 Source 중 다음 4건은 중복 생성하지 않고 재사용했다.

- `ocean-quest-rework-2025-02-05`
- `ocean-progression-2026-08-26`
- `life-unification-2026-09-02`
- `sea-crystal-guide`

## 4. Content 변경

신규 Content 13건:

1. `sailor-hiring-growth` — 고용 증서, 고용 실패, 선실 한도, 선원 경험치·성장 표
2. `sailor-role-slots` — 역할별 능력치, 선박별 추가 슬롯, 자동 배치 우선순위
3. `ocean-first-mates` — 프라와·클레이아·트라난 언더포 고용 조건과 고유 효과
4. `sailor-health-food` — 식량 0 상태, 차우더·건포도 빵, 재생의 묘약, 비상 식량
5. `carrack-sailor-fishing` — 활성 조건, 180초 규칙, 3% 고정 확률, 초기화·일시정지
6. `lekrashan-hunting` — 해란의 레크라샨 일일·주간 의뢰와 선택 보상
7. `hollow-maretta` — 현재 1시간 출현, 과거 출현 이력, 전리품 연결
8. `sea-crocodile-hunting` — 현행 위치, 이끼 지도, 화려한 선수상
9. `khan-guild-boss` — 길드 소환, 전용 대포, 회복 저지, 칸의 심장 분기
10. `ebenruth-nol` — 보물 효과, 9종 지도 조각 경로, 루살카 결합, 내구도 제거
11. `panokseon` — 별도 선박 분기, 기본 능력치, 제작소·선체 재료
12. `panokseon-haemo-byeokgye` — 해모 구매·강화와 벽계 제작식
13. `panokseon-cheongun` — 현행 최종 청운 제작식·설계도 교환·+10 세트 능력치

갱신 Content 9건:

- 기존 오킬루아 일일 4건과 주간 3건: 공헌도 경험치와 항해 경험치 보상 추가
- `sea-crystals`: 에벤루스의 놀과 루살카 해원석 관계 추가
- `rinbach-colony`: 판옥선 청운 제작 재료 관계 추가

`oquilla-sea-monster-dailies`, `oquilla-sea-monster-weeklies` 같은 집계형 중복 Content는 만들지 않았다. 기존 7개 퀘스트 Content의 slug와 nested `seed_key`를 그대로 유지했다.

## 5. Canonical row 수

| 종류 | V1.6C | V1.6D | 증감 |
|---|---:|---:|---:|
| Source | 27 | 34 | +7 |
| Content | 41 | 54 | +13 |
| ScheduleRule | 27 | 30 | +3 |
| ContentRequirement | 61 | 116 | +55 |
| ContentStep | 31 | 36 | +5 |
| Reward | 109 | 136 | +27 |
| ContentSection | 36 | 40 | +4 |
| ContentRelation | 57 | 91 | +34 |
| ChecklistTemplate | 23 | 26 | +3 |
| ChecklistTemplateItem | 23 | 26 | +3 |
| Evidence claim 선언 | 338 | 411 | +73 |
| Evidence source 연결(DB row) | 448 | 532 | +84 |

V1.6D import 후 active row는 ContentRequirement 114, Reward 133, Evidence 527, ContentRelation 91이다.

## 6. Supersede 및 archive 처리

의도적으로 비활성인 행:

- 레크라샨 일일 과거 목표 20+20: ContentRequirement 1, Evidence 1
- 공허한 마레타 과거 출현 간격 1~5시간: ContentRequirement 1, Evidence 1
- 린바크의 뼈·비늘·진액 과거 파도의 블랙스톤 교환: Reward 3, Evidence 3

과거 레크라샨과 마레타 Evidence는 `verification_status=superseded`, `active=false`다. 린바크의 기존 3개 superseded Evidence와 DB ID도 V1.6C → V1.6D import 후 유지됐다.

- 의도적 inactive ContentRequirement: 2
- 의도적 inactive Reward: 3
- 의도적 inactive Evidence: 5
- 예상하지 못한 inactive/archive: 0

## 7. 참조 및 구조 검증

통과 항목:

- 두 seed 파일 UTF-8 JSON parse
- Source ID 중복: 0
- Content slug 중복: 0
- content 범위를 벗어난 nested `seed_key`: 0
- DB 길이 제한을 넘는 nested/evidence key: 0
- unknown source reference: 0
- unknown relation target: 0
- unknown evidence entity reference: 0
- importer enum/구조 검증 통과

## 8. Semantic 검사

| 검사 | 결과 |
|---|---|
| 린바크 과거 블랙스톤 교환 active 행 | 0 |
| 레크라샨 현재 일일 목표 | 검은무쇠이빨 5 + 나인샤크 5 |
| 레크라샨 과거 20+20 목표 | inactive/superseded |
| 공허한 마레타 현재 출현 | 사망 후 1시간, active |
| 공허한 마레타 과거 1~5시간 | inactive/superseded |
| 기존 오킬루아 주간 3종 목표 | 각 1마리, active |
| 오킬루아 주간 과거 3마리 active 행 | 0 |
| 판옥선 장비 progression | 해모 → 벽계 → 청운 |
| 판옥선 현행 최종 장비 | 청운 |
| 에벤루스의 놀 현행 내구도·수리비 | 내구도 없음, 수리비 0 |
| 선원 역할 슬롯 | 7종 및 선박별 추가 슬롯 존재 |
| 부선장 | 프라와·클레이아·트라난 언더포 존재 |

## 9. Migration, import 및 멱등성

실제 DB와 분리한 임시 SQLite DB에서 다음을 검증했다.

1. 빈 DB → `20260902_0001`
2. `20260902_0001` → `20260903_0002 (head)`
3. V1.6D seed 1회 import
4. 같은 V1.6D seed 2회 import
5. canonical row 수와 모든 stable ID 비교

1회와 2회 import 후 row 수는 모두 동일했다.

| 테이블 | 1회 | 2회 |
|---|---:|---:|
| source | 34 | 34 |
| content | 54 | 54 |
| schedule_rule | 30 | 30 |
| content_requirement | 116 | 116 |
| content_step | 36 | 36 |
| reward | 136 | 136 |
| content_section | 40 | 40 |
| content_relation | 91 | 91 |
| checklist_template | 26 | 26 |
| checklist_template_item | 26 | 26 |
| evidence | 532 | 532 |

멱등성 결과: 통과.

## 10. V1.6C 회귀 및 이력 보존

현재 seed에서 V1.6D 추가분만 제외해 V1.6C canonical 27 Source·41 Content를 임시 DB에 재구성한 다음 V1.6D를 두 번 import했다.

- V1.6C 기존 Content 41개의 ID 유지
- V1.6C 14개 신규 Content의 ID 유지
- `carrack-advance`를 포함한 기존 canonical nested entity ID 유지
- 린바크 superseded Evidence 3건의 ID·상태 유지
- 기존 checklist instance 14건과 item state 14건 유지
- 테스트용 `carrack-advance` UserContentState 1건의 ID·상태·priority·note 유지

실제 `bdo.db` 복제본도 `0001 → 0002` migration 후 V1.6D seed를 두 번 import했다.

- 실제 DB에 있던 기존 Content 7개의 ID 유지
- 기존 checklist instance 4건 유지
- 기존 checklist item state 4건 유지
- 실제 DB에는 UserContentState가 0건이어서 보존 대상이 없었음

## 11. 테스트 결과

- seed importer tests: 4개 포함, 전체 통과
- backend 전체: `28 passed in 19.61s`
- 빈 임시 DB migration `0001 → 0002`: 통과
- V1.6C → V1.6D import: 통과
- 동일 seed 2회 import: 통과
- stable ID 및 checklist/UserContentState 이력 보존: 통과
- semantic stale 검사: 통과

frontend/UI 및 Prompt Bridge 코드는 변경하지 않았으므로 frontend build와 별도 AI 검증은 수행하지 않았다.

## 12. 실제 DB 미변경 확인

`backend/bdo.db`에는 migration 또는 seed import를 실행하지 않았다.

- 작업 전 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 작업 후 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 크기: 118,784 bytes
- 마지막 수정 시각(UTC): 2026-09-02 15:37:03

해시, 크기와 수정 시각이 모두 동일하다.

## 13. Schema gap

V1.6D seed 저장·import에 blocking schema gap은 없었다.

비차단 제약:

- `ScheduleRule`은 처치 시점을 기준으로 한 상대 간격을 직접 표현하지 않으므로 공허한 마레타의 “사망 후 1시간”은 claim 근거가 연결된 structured Requirement로 저장했다. 고정 시각 출현 일정으로 오인하지 않도록 ScheduleRule을 만들지 않았다.
- DB `Evidence.superseded_by`를 seed key로 연결하는 importer 입력은 아직 없다. 과거값은 기존 지원 방식인 `verification_status=superseded`, `active=false`로 보존했다.

이번 milestone은 데이터 import 범위이므로 스키마나 importer를 확장하지 않았다.

## 14. 의도적으로 제외한 범위

- 모든 선원 성격과 개인별 최종 성장 수치 백과
- 고정된 최적 선원 조합·전략 추천
- 모든 해양 괴수 사냥터 백과
- 길드 갤리선·해상 PvP
- 스키마·migration·API·UI·디자인 변경
- AI/Prompt Bridge 기능 변경
- 실제 사용자 DB migration 또는 seed import

