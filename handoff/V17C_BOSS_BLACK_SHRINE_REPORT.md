# V1.7C Boss / Black Shrine / World Boss Deep Pack Report

기준 시점: 2026-09-04 KR Live  
작업 범위: 데이터 seed, semantic regression test, 검증 보고서  
실제 `backend/bdo.db` import: 수행하지 않음

## 변경 파일

- `data/seed_sources.json`
- `data/seed_contents.json`
- `backend/tests/test_boss_black_shrine_seed.py`
- `handoff/V17C_BOSS_BLACK_SHRINE_REPORT.md`

Schema, migration 파일, backend API, frontend/UI, Prompt Bridge, AI 기능과 디자인은 변경하지 않았다.

## Seed 규모

| 항목 | V1.7B 기준 | V1.7C 이후 | 증감 |
|---|---:|---:|---:|
| Source | 128 | 137 | +9 |
| Content | 192 | 238 | +46 |
| Claim 선언 | 860 | 943 | +83 |
| Evidence row | 1,081 | 1,176 | +95 |
| Relation | 272 | 343 | +71 |
| superseded Evidence | 52 | 56 | +4 |
| needs_review Evidence | 21 | 36 | +15 |

Claim은 `seed_contents.json`의 claim 선언 수이고, Evidence는 claim별 `source_ids`가 importer에서 개별 row로 확장된 수다.
Relation은 같은 파일의 각 Content에 선언된 `relations` 항목을 직접 합산한 값이다.

지식 역할은 전체 seed 기준 FACT 167, STRATEGY 17, MEASUREMENT 11이다. V1.7C 추가분은 FACT 73, STRATEGY 5, MEASUREMENT 0이며, `announced_not_live` 4건과 `temporary_known_issue` 1건은 별도 역할로 저장했다.

## 신규 및 재사용 Content

신규 Content 46개를 추가했다.

- 공통/동해도 시스템 7개: `boss-content-taxonomy`, `black-shrine-donghae-current-system`, `donghae-light-orb-system`, `donghae-calamity-8-10`, `donghae-reward-ranking`, `donghae-hyperboost-armor-support`, `donghae-boss-strategy`
- 동해도 우두머리 10개: 금돼지왕, 바리, 죽엽군장, 산군, 구미호, 어둑시니, 대창귀, 두억시니, 이무기, 손각시
- 황해도 시스템 5개: `black-shrine-hwanghae-current-system`, `hwanghae-aura-system`, `hwanghae-reward-ranking`, `hwanghae-party-strategy`, `hwanghae-current-roster`
- 황해도 우두머리 7개: 지귀, 우투리, 청의동자, 불가살, 흑봉황, 비형랑, 폐세자
- 월드 우두머리 시스템 5개: `world-boss-current-system`, `world-boss-current-roster`, `world-boss-reward-2025-overhaul`, `morning-land-world-bosses`, `boss-guide-conflicts`
- 월드 우두머리 엔터티 12개: 크자카, 누베르, 카란다, 쿠툼, 귄트, 무라카, 미루목 파괴자 오핀, 산군, 금돼지왕, 우투리, 불가살, 검은 봉황

기존 `garmoth`, `vell`, `black-shrine-donghae-weekly`, `black-shrine-hwanghae-weekly`는 중복 생성하거나 직접 재작성하지 않았다. 새 시스템 Content에서 relation으로 연결해 기존 주기·보상 엔터티를 재사용했다.

## Donghae current facts

- 개인 콘텐츠이며 가문당 주간 보상 획득은 5회다. 같은 우두머리·난이도 재도전은 제한 없이 가능하다.
- 1~7재시니는 빛의 보옥 90%, 장비 능력치 10%를 적용한다.
- 현재 최대 보옥은 6개다. 과거 최대 5개 claim은 inactive/superseded로 보존했다.
- 여섯 번째 보옥은 구미호 설화 지식과 흑정령 의뢰 `[아침의 나라] 설화깨비의 시련 - 육재시니`를 통해 해금한다.
- 보옥당 속성 공격력 +50, 속성 방어력 +100, 추가 배분 3점, 점수당 능력 3을 저장했다.
- 속성 치명타 확률 50%, 우두머리 속성 상태이상 저항 20%를 별도 필드로 저장했다.
- 8~10재시니는 빛의 보옥을 사용하지 않고 장착 장비 능력치 100%로 전투한다.
- 두억시니와 손각시 8/9/10재시니 공격력 기준은 365/375/385다.
- 손각시 2026-07-15 조정과 구미호 2026-07-29 조정을 current fact로 저장했다. 구미호의 과거 공격력 345는 inactive/superseded다.
- 하이퍼 부스트 방어구 지원의 공격력 조건은 우두머리 일반 입장 공격력과 별도 필드로 저장했다: 금돼지왕 8재 305/라브레스카, 9재 315/아토르 선택, 산군 8재 310/죽은신, 구미호 8재 315/단 선택.
- 주간 보상은 일요일 00:00 KST 이후 흑정령의 선물함으로 지급되고 누적되며 소멸하지 않는다.
- 우두머리·난이도·클래스별 일일 순위 갱신과 주간 정산을 분리했다.

## Hwanghae current facts

- 5인 파티, 가문당 주 5회 보상이며 실패는 횟수를 소모하지 않는다.
- 횟수 소진 후 도움 참가는 가능하되 일부 이벤트·길드 임무 집계는 별도 조건일 수 있음을 보존했다.
- 일반 권장 공격력 300, 도전 330, 빛의 보옥 미적용, 장비 능력치 100%다.
- 파티장이 입장하며 5명 중 3명이 동의하면 컷신을 건너뛴다.
- 물약은 비활성화되지만 자연 회복, 기술 회복, 콘텐츠 회복 구슬은 가능하다.
- 제거되는 버프를 일부 클래스 기술 버프와 순수한 마력의 블랙스톤 특수 버프로 제한했다. 모든 버프 제거라는 일반화는 만들지 않았다.
- 해/달/땅 기운을 속도/생존/재도전 지원 역할로 저장했다.
- 현재 명단은 7종이며 과거 외부 6종 표기는 inactive/conflict다.
- 2026-06-17 이후 도전 보상의 새벽의 정수 상자 1개, 일일 순위와 주간 정산, 동일 길드 5인 추가 보상 구조를 저장했다.

## World Boss current facts

- 올비아·아르샤를 제외한 일반 서버에서 생명력을 공유하고 최대 2마리가 동시에 등장할 수 있다.
- 일반 퇴장 시간은 30분, 귄트·무라카는 15분이다.
- 피해 기여도는 중요하지만 전리품 결정의 유일한 조건은 아니다.
- 공식 가이드의 실제 열거 항목 기준 현재 명단은 14개 엔터티다.
- 2025-12-23 기준 크자카·누베르·카란다·쿠툼 보상 가치 +75%, 강화형 등장 확률은 기존 대비 상대 +100%이며 확정 등장은 아니다.
- 아침의 나라 과거 주간 의뢰는 inactive/superseded이고, 현재는 직접 전리품 지급 구조다.
- 2026-02-04 기준 불가살·우투리·산군·금돼지왕 생명력은 각각 1.5배다.
- 크자카·불가살·우투리의 과거 완전 무적은 inactive/superseded이며 현재 피해 감소 상태로 저장했다.
- 산군의 등장 위치가 궁궐에 더 가까워진 변경을 저장했다.
- 검은 봉황은 2026-08-05 live이며 별도 고정 시간표가 아니라 산군·우투리·불가살·금돼지왕 예정 시간에 확률적으로 대체 등장한다.
- 벨은 목요일 00:15/일요일 17:00 KST, 대포 기반, 파티·부대 대포 기여도 공유, 사망 불이익 없음으로 연결했다.
- 가모스는 기존 Content의 주간 최대 3회 보상과 목요일 00:00 초기화를 재사용한다.
- 검은 그림자는 월드 우두머리가 아니라 토요일 17:00 필드 우두머리이며 현재 삭제 완료로 처리하지 않았다.

## Community strategy provenance

전략 Source 5개를 추가했다.

- 최근 Reddit 논의 4개: 황해도 2026-07-27, 2026-07-30, 2026-07-31 및 동해도 고재시니 2026-06-30
- third-party mechanics guide 1개: Black Desert Foundry

2026-07 이후 전략 Source는 3개다. 황해도 전략은 서로 다른 Source 유형인 커뮤니티 논의와 third-party guide를 교차 연결했고 모두 FACT가 아닌 STRATEGY, Evidence는 `needs_review`로 저장했다. 불가살·지귀·우투리의 초행 파티 후보, 비형랑·흑봉황의 협업 요구, 폐세자·청의동자의 조직 파티 선호는 절대 난이도 순위가 아닌 최근 의견 범위다. clear-time anecdote와 보편적 숫자 난이도는 생성하지 않았다.

## CURRENT GUIDE CONFLICTS

- Donghae Light Orb: 현재 1~7재시니 보옥 적용과 향후 보옥 제거 발표를 분리했다.
- 최대 보옥 5 vs 6: 6개를 current로, 5개를 inactive/superseded로 보존했다.
- Hwanghae 6 vs 7: 공식 현재 엔터티 7개를 canonical로, 외부 6종 표기를 inactive/conflict로 저장했다.
- World Boss 13 vs 14: 공식 가이드의 ‘13종’ 문구는 같은 페이지가 실제 14개를 열거하므로 inactive/conflict다. 현재 roster는 열거된 14개 엔터티다.
- Morning Land weekly quests: 2025-12-23 이후 direct loot를 current로, 과거 주간 의뢰를 inactive/superseded로 저장했다.
- Kzarka/Bulgasal/Uturi invulnerability: 과거 완전 무적을 inactive/superseded로, 현재 피해 감소 상태를 active fact로 저장했다.
- Heidel Ball announcements: 발표 사실은 보존하되 KR Live current canonical로 승격하지 않았다.

## ANNOUNCED_NOT_LIVE

다음 4건은 requirement와 Evidence 모두 current 집계에 참여하지 않도록 inactive로 저장했다.

- 동해도 빛의 보옥 제거 및 장비 전환 계획
- 황해도 난이도 개편 계획
- 라우라우 월드 우두머리 전환 계획
- 검은 그림자 제거 계획

따라서 라우라우는 현재 14개 월드 우두머리 명단에 들어가지 않으며 검은 그림자도 삭제 완료로 처리하지 않는다.

## TEMPORARY_KNOWN_ISSUES

구미호의 부활·재사망·여우굴 관련 현상 1건을 `temporary_known_issue` + `needs_review`로 저장했다. 영구 FACT로 사용하지 않는다.

## Entity separation

`hwanghae-shrine-dark-bonghwang`은 황해도 검은사당 5인 파티 엔터티이고, `world-boss-black-phoenix`는 확률적 대체 등장 월드 우두머리 엔터티다. 이름이 유사해도 ID, context, relation을 공유하지 않는다. 산군·금돼지왕·우투리·불가살도 검은사당과 월드 우두머리 slug를 분리했다.

## 미해결 및 의도적 제외

- 아침의 나라 우두머리 인장 교환의 전체 품목·정확한 한글 아이템명은 이 팩에서 확정하지 않았다. 근거가 충분한 current 값만 저장한다는 원칙에 따라 임의 생성하지 않았다.
- 황해도 도움 참가 시 제외되는 이벤트/길드 임무의 전체 목록은 nullable 범위로 남겼다.
- 모든 우두머리 절대 HP, 피해 계수, CC frame, 클래스별 tier list, 전체 월드 우두머리 Schedule UI는 제외했다.
- 에다니아 심층 우두머리와 피의 제단 deep pack은 제외했다.

## Schema gaps

- Claim은 독립 테이블이 아니라 seed claim 선언이 Source별 Evidence row로 확장되는 구조다.
- FACT/STRATEGY/MEASUREMENT, `announced_not_live`, `temporary_known_issue`는 `structured_value.knowledge_role`에 저장되며 DB enum 제약은 없다.
- 발표/임시 이슈의 lifecycle도 structured JSON과 `active` 조합으로 표현한다.

이번 milestone에서는 지시대로 schema를 확장하지 않았다.

## Import 및 보존 검증

- `seed_sources.json`, `seed_contents.json` UTF-8 JSON parse: 통과
- Source ID/URL, Content slug uniqueness: 통과
- unknown source/relation/evidence/entity reference: 0 (전체 seed import 성공)
- unexpected archive: 0 (V1.7B baseline nested row의 ID와 active 상태 비교)
- 임시 SQLite migration: `20260902_0001` → `20260903_0002` 통과
- V1.7B baseline import → V1.7C import → 동일 V1.7C 재import: 통과
- 두 번째 import 후 canonical row count 변화: 0
- 기존 192 Content stable ID: 보존
- 기존 nested stable ID: 보존
- ChecklistInstance, ChecklistItemState와 완료 이력: 보존
- UserContentState: 보존

## 테스트 결과

- V1.7C semantic tests: `10 passed`
- V1.7C + V1.7A combat + V1.7B grind + V1.6G/H/I 지정 회귀 묶음: `82 passed`
- backend 전체 tests: `134 passed in 383.15s`

테스트는 `--basetemp=D:\BOD\... -p no:cacheprovider`를 사용해 작업공간 내 임시 DB에서 실행했다.

## 실제 DB 무변경 확인

- 작업 전 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 작업 후 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 결과: 동일. 실제 `backend/bdo.db`는 import하거나 수정하지 않았다.
