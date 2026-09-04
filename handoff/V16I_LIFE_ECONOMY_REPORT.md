# V1.6I Life Economy / Nodes / Workers / Logistics 결과 보고서

- 기준: 2026-09-04 KR Live
- 작업 범위: 데이터 seed, semantic regression test, 임시 DB import 검증
- 실제 사용자 DB: import하지 않음

## 변경 파일

- `data/seed_sources.json`
- `data/seed_contents.json`
- `backend/tests/test_life_economy_seed.py`
- `backend/tests/test_life_deep2_seed.py`
  - V1.6H의 `Source == 84`, `Content == 120` snapshot equality를 제거했다.
  - V1.6H source/content 존재와 전체 ID·URL·slug 고유성 검증은 유지한다.
- `handoff/V16I_LIFE_ECONOMY_REPORT.md`

스키마, migration, backend API, frontend/UI, 디자인, Prompt Bridge, AI 기능과 실제 `backend/bdo.db`는 변경하지 않았다.

## Seed 증분

| 항목 | V1.6H | V1.6I | 증분 |
|---|---:|---:|---:|
| Source | 84 | 98 | +14 |
| Content | 120 | 140 | +20 |
| Claim 선언 | 714 | 742 | +28 |
| Evidence DB row | 885 | 935 | +50 |
| Relation | 173 | 211 | +38 |
| Superseded claim 선언 | 32 | 38 | +6 |
| Superseded Evidence DB row | 34 | 44 | +10 |

Claim 하나가 여러 Source를 참조하면 importer가 Source별 Evidence row로 펼치므로 Claim과 Evidence 증분은 서로 다르다.

## 신규 Source

기존 `node-guide`, `farming-overhaul-2026-06-04`는 재사용했다. 신규 Source 14개는 다음과 같다.

- `contribution-guide`
- `worker-guide`
- `worker-overhaul-2023-05-24`
- `worker-convenience-2025-01-22`
- `work-management-guide`
- `house-guide`
- `crafting-guide`
- `storage-guide`
- `silver-unification-history`
- `magnus-storage-history`
- `magnus-guide`
- `remote-storage-sale-history`
- `royal-workshop-history`
- `royal-workshop-2024-11-20`

Source ID와 URL은 각각 98개 모두 고유하다.

## 신규 Content

1. `contribution-economy-foundation`
2. `node-network-current-system`
3. `production-node-current-system`
4. `production-node-2026-overhaul`
5. `worker-current-system`
6. `worker-races-grades`
7. `worker-growth-promotion`
8. `worker-skills-luck`
9. `worker-special-delivery`
10. `worker-stamina-auto-recovery`
11. `worker-market`
12. `housing-life-economy`
13. `worker-lodging`
14. `workshop-crafting-logistics`
15. `storage-current-system`
16. `storage-transport`
17. `magnus-remote-storage`
18. `family-silver-unification`
19. `royal-workshop-current-system`
20. `royal-workshop-worker-effects`

기존 Content 본문을 보강하거나 중복 생성한 건은 0건이다. 기존 Processing, Cooking, Alchemy, Farming, Fishing Content는 Relation으로 연결했다.

## 생산 거점 반영

- 2026-06-04 공헌도 변경: 13행
- 현재 생산 거점 slot: 41행
- 같은 산출물의 복수 slot: 합치지 않고 각 slot을 유지
- current canonical 구조화 행: 합계 54행
- pre-2026 공헌도와 산출물: 2개 legacy claim group을 `superseded`, `active=false`로 보존

대표 회귀 검증에는 늑대 언덕, 노인의 다리, 가모스의 둥지, 위니/러니 산장 발굴, 낙시온, 순례자의 성소 4곳, 필라 쿠, 필라 페, 폐허도시 룬이 포함된다.

## Semantic 결과

### Node

- 공헌도는 가문 공유이며 지역 제한이 없다.
- 탐험 거점과 생산 거점을 별도 개념으로 유지한다.
- 생산 거점은 상위 탐험 거점과 해당 생산 거점 투자가 모두 필요하다.
- 원격 마을 일꾼은 연결된 네트워크에서 사용할 수 있다.
- 밸류 패키지 원격 투자는 거점당 기운 10을 사용하며 무료 투자가 아니다.
- 미연결 수송은 가능하나 비용 3배, 미연결 무역 판매는 기준가 30%다.
- 2026-06-04 이후 플로린 관문, 티티움 계곡, 라이칼 폭포 채집, 쿠니드의 쉼터 채집의 현재 공헌도 1을 검증했다.

### Worker

- 일꾼 보기와 다시 보기는 각각 기운 5다.
- 일꾼 감독관 지식이 있으면 현재 위치와 다른 마을의 일꾼을 선택해 고용할 수 있다.
- 최대 레벨 40, 레벨 40 총 기술 10개다.
- 기술 변경은 레벨 30 이상, 경험치 20% 이상에서 경험치 20%를 소모한다.
- 승급 확률은 일반→숙련 90%, 숙련→전문 70%, 전문→장인 50%다.
- 특송은 모든 일꾼이 레벨 1부터 기본 보유한다. 과거 레벨 40 claim은 비활성 superseded 상태다.
- 작업 반복 최대 입력은 50,000회이며 실제 반복은 행동력에 제한된다.
- 일꾼 거래소 판매 수수료는 30%다.
- 고블린 계열은 작업·이동, 자이언트 계열은 기본 생산량, 인간 계열은 행운 특성을 중심으로 구분한다. 특정 특수 일꾼의 최종 능력치로 일반화하지 않는다.
- 자동 행동력 회복은 설정 시 행동력 3 이하에서 가문 가방 회복 아이템을 사용하며 재배 일꾼에도 적용된다.

### Logistics

서로 다른 네 가지 흐름을 합치지 않았다.

1. 생산 거점 특송: 생산물 도착 마을 창고 선택
2. 공방 제작: 선택한 일꾼 소속 마을 창고에서 재료 사용
3. 일반 창고 수송: 최대 40꾸러미, 경로 이동 시간이 필요한 비즉시 수송, 미연결 비용 3배
4. 마그누스 원격 창고: 진행·지식·지도 조건과 제한 품목이 있는 원격 접근

### Storage / Silver

- 창고 기본 슬롯은 8이다.
- 주거지 창고 단계당 일반 안내 기준 추가 슬롯은 3이며 집별 효율은 별도다.
- 물고기 가격 보증 시간과 유효기간 아이템 시간은 창고에서 멈추지 않는다.
- 마그누스 전체 의뢰 완료 후 다른 마을 창고 아이템 판매와 통합거래소 창고 이동을 지원하되 제한 품목 규칙은 유지한다.
- 캐릭터와 모든 마을 창고 은화는 가문 `내 은화`로 통합되며 통합거래소 보관 은화는 별도다.
- 과거 마을별·캐릭터별 은화 잔액 claim은 비활성 superseded 상태다.

### Royal Workshop

- 시작 공헌도: 5
- 위치: 아침의 나라 서울
- 사용 자원: 육조거리 일꾼과 육조거리 창고
- 생산 거점 한 곳의 공방 수: 5
- 무료 갱신 획득: 하루 1회, 최대 보유 1회
- 추가 갱신: 현재 10펄이며 변경 가능한 정책값으로 Source를 연결
- 자동 품목 갱신: Asia/Seoul 매일 00:00
- 과거 01:00 claim: 비활성 superseded
- 생산소 거북이 일꾼 기본 수확량 +68.4% 적용
- 행운에 따른 농부·광부·어부 보따리류 추가 획득 가능
- 가공소 알뜰살뜰 A/B/C는 지정 확률로 재료 한 종류 10% 반환
- 일꾼 이동 속도는 왕실 공방 작업 시간에 영향 없음

## CURRENT GUIDE CONFLICTS

| 영역 | 과거/단순 안내 | V1.6I current canonical | 우선 Source |
|---|---|---|---|
| Worker Special Delivery | 2023: 레벨 40 확정 습득 | 2025 이후 모든 일꾼 레벨 1 기본 보유 | `worker-convenience-2025-01-22` |
| Node output destination | 생산물이 일꾼 소속 마을 창고로 이동 | 생산 거점 결과는 특송으로 도착 마을 창고 선택 가능 | current Worker guide/update |
| Workshop logistics | 특송과 같은 물류로 오해 가능 | 공방 재료는 선택한 일꾼 소속 마을 창고에서 사용 | current Work Management guide |
| Storage silver | 마을 창고별 은화 입출금 | 가문 `내 은화` 통합, 통합거래소 은화 별도 | `silver-unification-history` |
| Royal Workshop refresh | 초기 01:00 | 2024-11-20 이후 00:00 | `royal-workshop-2024-11-20` |
| Production node output/CP | 2026-06-04 이전 값 | 2026-06-04 개편표의 13 CP행·41 slot | `farming-overhaul-2026-06-04` |

최신 패치가 과거 가이드나 이력보다 우선되는 모든 경우에 현재 claim은 verified/active, 과거 claim은 superseded/inactive로 분리했다.

## 미확정 및 의도적 제외

### Unresolved facts

- 일꾼 거래소 등록 일꾼의 남은 승급 기회: `null`, `needs_review`
- 일반 생산 거점 행운 추가 아이템의 정확한 확률: `null`
- 왕실 공방 행운 보따리의 정확한 확률: `null`
- 왕실 공방 알뜰살뜰 A/B/C의 발동 확률: `null`
- 집별 숙소·창고 exact capacity와 효율: 집에 따라 달라 별도 atlas 필요

### Deliberately excluded scope

- Full Trade Deep Pack
- 일꾼/거점 최적화와 ROI 추천
- 전 세계 Housing Atlas
- 전체 공방 recipe와 가공무역 수익성
- 왕실 공방 전체 제품 가격·시간당 수익
- 동적 거래소 가격
- 일꾼별 exact final stat와 작업 시간 역산값

### Schema gaps

- 동적 시세와 시점별 경제성 snapshot을 정규화하는 전용 모델은 없다.
- 집 주소별 슬롯·용도·단계 전체 atlas와 공방 recipe를 전용 구조로 대량 수록하는 모델은 이번 범위에서 추가하지 않았다.
- 불확실한 확률은 현재 `structured_value`의 `null`과 Evidence 상태로 표현한다.

이 gap을 해소하기 위한 schema 변경은 V1.6I 범위 밖이므로 수행하지 않았다.

## Import / 보존 검증

임시 SQLite DB에서만 다음 순서로 실행했다.

1. Alembic `20260902_0001`
2. Alembic `20260903_0002` (`head`)
3. V1.6H baseline Source 84 / Content 120 import
4. ChecklistInstance, ChecklistItemState, UserContentState 보존 fixture 생성
5. V1.6I Source 98 / Content 140 import
6. 동일 V1.6I seed 재import

결과:

- migration `0001 → 0002`: 성공
- 두 번째 V1.6I import 후 모든 canonical table count: 첫 번째와 동일
- 기존 Content ID: 120/120 유지
- 기존 stable nested ID: 1,808/1,808 유지
- ChecklistInstance: 유지
- ChecklistItemState와 완료 상태·note: 유지
- UserContentState: 유지
- completion history: 유지
- unknown source: 0
- unknown relation: 0
- unknown evidence reference: 0
- unknown entity scope: 0
- unexpected archive: 0

주요 임시 DB count:

| Table | V1.6H baseline | V1.6I 1차 | V1.6I 2차 |
|---|---:|---:|---:|
| source | 84 | 98 | 98 |
| content | 120 | 140 | 140 |
| content_requirement | 323 | 385 | 385 |
| content_relation | 173 | 211 | 211 |
| evidence | 885 | 935 | 935 |
| schedule_rule | 50 | 50 | 50 |
| checklist_template | 35 | 35 | 35 |
| checklist_template_item | 46 | 46 | 46 |

## 테스트 결과

- V1.6G + V1.6H + V1.6I semantic tests: **51 passed** (`128.24s`)
- backend 전체 tests: **103 passed** (`190.63s`)
- seed JSON parse: 성공
- seed importer 및 idempotence: 성공

## 실제 DB 불변 검증

- before SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- after SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 결과: 동일, 실제 `backend/bdo.db` 미변경
