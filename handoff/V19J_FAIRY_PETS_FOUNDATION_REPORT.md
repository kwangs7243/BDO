# V1.9J Fairy / Pets Foundation & Practical Setup Closure Report

## 기준

- Repository: `kwangs7243/BDO`
- Base: `main @ 6540f95ff1828877b857fe7073f52a0506399d27`
- Branch: `feature/v1.9j-fairy-pets-foundation`
- Commit: 이 보고서를 포함하는 branch HEAD
- 조사일: `2026-09-07` (Asia/Seoul)
- 작업 범위: Fairy / Pets current FACT와 조건부 초기 설정 STRATEGY
- 변경하지 않은 영역: schema, migration, backend/frontend 기능, 전용 UI, 실제 `backend/bdo.db`

## Existing seed audit

기존 seed에서 `fairy`, `pet`, `companion`, `convenience`, `family convenience` 책임을 감사했다.

- `account-progression-foundation`, `family-convenience-unlock-foundation`은 가문 성장과 편의 해금의 상위 책임만 가진다.
- `life-family-levels`, `energy-foundation`, `training-onboarding-strategy`에는 활동별 연결 가능성이 있으나 Fairy/Pet current system 책임은 없다.
- 재배 보상의 반려동물, 낚시의 같은 효과 비중첩, 사냥터의 전리품 획득 병목 등은 부분 언급이며 시스템 정본이 아니다.
- workers/nodes는 V1.6I의 기존 책임을 그대로 유지했다.
- 따라서 FACT 3개와 STRATEGY 1개를 새 stable Content로 분리했다. Fairy와 Pet FACT를 하나의 Content에 섞지 않았다.

## Fairy current guide audit

`요정 레이라` 현재 공식 가이드에서 다음을 확인했다.

- 레벨 53과 현재 가이드가 제시하는 메인 의뢰 대체 조건 중 하나를 충족한 뒤 `[모험 지원] 요정, 신비스러운 동행`을 진행한다.
- 봉인된 요정의 날개를 의뢰로 얻거나 레이라의 꽃잎 2개를 봉인된 요정의 날개 1개로 교환할 수 있다.
- 등급별 최대 레벨은 희미한 10, 선명한 20, 영롱한 30, 찬란한 50이다.
- 오네테아 흑벌꿀주, 달콤한 벌꿀주, 초록색 등급 장비를 성장 재료로 사용할 수 있다. 전체 EXP 표는 포함하지 않았다.
- 날개돋이, 성장/인격 환생, 테이아의 구슬을 이용한 기술 변경을 서로 다른 수명주기로 구조화했다.
- 기술 변경에 필요한 구슬 수는 현재 배운 기술 수와 같고 결과 확률은 게임 내 UI에서 확인한다. 목표 기술을 보장한다고 표현하지 않았다.
- 신비한 응원, 아낌없는 손길, 깃털같은 발걸음, 요정의 눈물, 마르지 않는 우물, 샛별, 간지러운 숨결은 기능 역할만 기록했다.

## 2026-08-19 appearance / skill change

공식 2026-08-19 업데이트에 따라 현재는 보유한 요정 외형과 사용할 고유 기술을 각각 선택한다. 선택할 기술은 현재 보유한 요정의 기술이어야 한다. 외형 때문에 특정 고유 기술을 포기해야 한다는 과거 공략은 current FACT에서 제외했다.

## CURRENT GUIDE CONFLICT — 아낌없는 손길

동일한 공식 `요정 레이라` 가이드에 서로 다른 표기가 존재한다.

- 충돌하는 상단 표: I~V `7 / 10 / 15 / 20 / 30`
- 2022-08-10 공식 도입 패치: I~V `5 / 8 / 12 / 16 / 20`
- 현재 상세 성장표: I~V `5 / 8 / 12 / 16 / 25`
- 같은 페이지 설명: 최대 `25`
- 공식 2025-09-17 패치: V 사용 가능 아이템 수 `20 → 25`

처리 결과:

- active FACT에는 2022 도입 패치로 I~IV를 교차 검증하고, 현재 상세 성장표와 2025 상향 패치가 함께 지지하는 `5 / 8 / 12 / 16 / 25`만 저장했다.
- `continuous_care_v_capacity == 25`와 `!= 30`을 semantic test로 고정했다.
- stale 수치 문자열은 verified Prompt FACT에 포함하지 않고 이 handoff에만 충돌 이력으로 남겼다.
- 전체 기술별 획득 확률과 날개돋이 확률 matrix는 저장하지 않았다. 확률이 게임 내 공식 UI에서 확인 가능하다는 경계만 기록했다.

## Pet current guide audit

`반려동물` 현재 공식 가이드에서 다음을 확인했다.

- 의뢰 획득과 가문당 1회 추천 의뢰 범위, 등록증을 사용한 등록 절차
- 행동 방식 `신중함 / 보통 / 기민함`과 전리품 획득 주기·배고픔 소모의 연결
- 배고픔 0에서 전리품 획득과 특기가 중단되는 규칙
- 특기와 고유/주 기술의 구분, 특기의 중첩 가능/불가능 범위
- 목적별 그룹과 그룹 단위 맡기기/찾기
- 최대 5마리 등록, 최대 4세대 결과, 외형/기술 계승, 같은 교환 유형 제약

무료 반려동물 의뢰 전체 목록, 반려동물별 기술 catalog와 교환 확률 matrix는 포함하지 않았다.

## 5th-generation audit

`5세대 반려동물 훈련` 현재 공식 가이드에서 다음을 확인했다.

- 4세대 반려동물과 제왕의 깃털로 5세대 훈련
- 제왕의 깃털 간이 연금식: 성장의 시약 10, 마력의 파편 40, 상급 가벼운 깃털 800
- 훈련 뒤 일반 반려동물 교환 불가, 외형·기술 교환은 훈련 전에 완료
- 5세대 중 대장은 한 마리이며 변경 가능
- 대장과 함께 꺼낸 반려동물의 전리품 획득 시간 15% 감소
- 대장 자신의 고유 기술 레벨 +1, 특기 상승 없음
- 비대장 5세대는 일반 4세대와 같은 능력 적용

현재 가격과 재료별 시장 효율은 저장하지 않았다.

## Sources

### Official

- `fairy-guide-current` — `wikiNo=181`
- `fairy-probability-guide-current` — `wikiNo=338`
- `fairy-continuous-care-introduction-2022-08-10` — `groupContentNo=8708`
- `fairy-continuous-care-update-2025-09-17` — `groupContentNo=14554`
- `fairy-appearance-skill-update-2026-08-19` — `groupContentNo=16063`
- `pet-guide-current` — `wikiNo=180`
- `pet-fifth-generation-guide-current` — `wikiNo=296`

### Community Strategy

- `fairy-beginner-strategy-2026-08-20` — 최근 입문자가 신비한 응원과 아낌없는 손길을 먼저 검토하되 초기에 멈추고 점진적으로 개선하는 사례만 사용했다.
- `pet-exchange-decisions-2026-06-04` — 교환 선택이 보유 반려동물과 위험 선호에 따라 달라지는 사례만 사용했다.

Community 자료의 종결 기술 세트, 이벤트 재화, 거래소 상황, 확률 계산과 특정 교환 효율 결론은 FACT 또는 universal strategy로 승격하지 않았다.

## Rejected / stale sources and data

- 공식 Fairy 가이드의 `아낌없는 손길 V=30` 상충 표기: current FACT에서 제외
- 외형과 고유 기술을 종속시키는 2026-08-19 이전 공략: stale
- 현재 펄 가격, 할인율, 판매 패키지, reroll 평균 현금 비용: 상업·동적 데이터로 제외
- 이벤트 찬란한 요정 상자, 이벤트 반려동물, 테이아의 구슬 지급: permanent canonical unlock에서 제외
- 모든 Fairy 확률표, 모든 Pet catalog와 교환 확률표: milestone 범위 밖

## 신규 canonical data

### Source

- `168 → 177` (`+9`)
- official 7 / community strategy 2

### Content

- `270 → 274`, 모두 active (`+4`)
- FACT: `fairy-current-system`
- FACT: `pet-current-system`
- FACT: `pet-fifth-generation`
- STRATEGY: `fairy-pet-setup-strategy`

### Knowledge role

- FACT: `200 → 220` (`+20`)
- STRATEGY: `57 → 63` (`+6`)
- MEASUREMENT: `11 → 11` (`+0`)

### Relation

- `480 → 490` (`+10`)
- Fairy는 account progression / family convenience에 연결했다.
- Pet은 account progression / family convenience / life family levels / energy foundation에 연결했다.
- 5세대는 일반 Pet current system을 prerequisite로 사용한다.
- Setup strategy는 세 신규 FACT Content만 prerequisite로 참조한다.

## Strategy semantics

`fairy-pet-setup-strategy`는 다음 의미를 명시한다.

- `universal_best_skill_set = false`
- `paid_reroll_required = false`
- `beginner_can_stop_early = true`
- `skill_priority_depends_on_activity = true`
- `universal_best_pet = false`
- `universal_best_group = false`
- `all_pets_need_fifth_generation = false`
- `exchange_before_fifth_generation_when_needed = true`

## Prompt role validation

기존 mode만 사용했다.

- `content_onboarding`
- `next_action`
- `verify_latest`

세 FACT Content의 summary/purpose/Requirement/Step/Section은 FACT로, setup strategy의 동일 구조는 STRATEGY로 직렬화되는지 검증했다. Community recommendation은 FACT로 승격되지 않았으며 stale Fairy 수치는 verified current prompt에 나타나지 않는다. 새 Prompt mode나 runtime web search는 추가하지 않았다.

## Import idempotency and history preservation

V1.9I baseline 임시 SQLite DB에서 다음 순서로 검증했다.

1. Alembic `20260902_0001 → head`
2. V1.9I seed import
3. 기존 Content/nested ID, checklist marker, UserContentState, UserMaterialInventory, UserProjectStageState 기록
4. V1.9J seed import
5. V1.9J seed 재import

검증 결과:

- 기존 Content와 nested ID 보존
- 신규 Content와 Requirement/Step/Section/Evidence ID 보존
- canonical row count 재import 전후 동일
- ChecklistInstance와 완료/메모 이력 보존
- UserContentState 보존
- UserMaterialInventory 보존
- UserProjectStageState 및 Project canonical row 보존
- unknown Source 0 / unknown Relation target 0

## Tests

- V1.9J semantic + V1.9I + V1.7D historical regression: `18 passed`
- Backend full: `312 passed`, 기존 Starlette deprecation warning 1건
- Frontend typecheck: `passed`
- Frontend lint: `passed`
- Frontend tests: `14 files / 57 passed`
- Frontend build: `passed`
- `git diff --check`: `passed`

## Actual DB integrity

- Before SHA-256: `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
- After SHA-256: `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
- SHA-256 unchanged: `yes`
- 실제 `backend/bdo.db`를 migration/import 테스트에 사용하지 않았다.

## Tasks closure

Milestone C의 `fairy/pets/workers/nodes`는 다음 근거로 완료 처리했다.

- workers/nodes: 기존 V1.6I 구현 유지
- Fairy: current acquisition / grade / growth / lifecycle / major skills / 2026 appearance-skill separation
- Pets: current action / hunger / specialty / skills / groups / exchange
- 5th generation: training / exchange lock / captain / non-captain semantics
- setup strategy: 활동별 조건부 판단, universal best와 all-pets-fifth 목표 금지

Adventure Log Deep Pack, Magnus Deep Pack, guild bosses와 remaining life recipe/measurement/economy는 변경하지 않았다.
