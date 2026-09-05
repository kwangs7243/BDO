# V1.9A — Life Hub Experience 완료 보고

## Git 기준

- Source of Truth: `main @ 2626964d7f2b17b932a4600610cc520e0f131adb`
- 작업 branch: `feature/v1.9a-life-hub`
- 구현 commit: `8234fb82007d4163f6503f6f4e41f4a29a78fa7b`
- handoff 문서 commit: 이 파일의 Git history와 최종 작업 보고 참조

## 기존 seed taxonomy 분석

- 현재 전체 seed는 Source 145개, active Content 259개다.
- `category=life` Content는 81개이며, 이 중 요리·연금·조련·수렵과 V1.6I 경제 데이터 일부는 `subcategory`로 직접 구분된다.
- V1.6F-G의 공통 기반 및 채집·낚시·재배·가공 데이터 일부는 `subcategory=null`이므로 category/subcategory만으로 Life UI 역할을 안정적으로 표현할 수 없다.
- 항해·물물교환 데이터는 `ocean_guide`, `ocean_barter`, `ocean_project` 등 해양 category에 분산되어 있다.
- 노드·일꾼·창고·물류 데이터는 독립 생활 skill이 아니라 공통 `생활 기반과 경제` 영역으로 노출했다.
- 새 taxonomy table이나 seed field를 만들지 않고, canonical Content slug를 UI section에 배치하는 read-only presentation mapping을 사용했다.

## 지원 생활 분야

| key | 표시명 | 대표 Content | 분야 내 고유 Content |
| --- | --- | --- | ---: |
| `gathering` | 채집 | `gathering-current-system` | 11 |
| `fishing` | 낚시 | `fishing-current-system` | 15 |
| `farming` | 재배 | `farming-current-cycle` | 10 |
| `processing` | 가공 | `processing-current-system` | 9 |
| `cooking` | 요리 | `cooking-current-system` | 13 |
| `alchemy` | 연금 | `alchemy-current-system` | 15 |
| `training` | 조련 | `training-current-system` | 15 |
| `hunting` | 수렵 | `hunting-current-system` | 13 |
| `sailing` | 항해 | `carrack-types` | 32 |
| `barter` | 교역/물물교환 | `barter-current-system` | 15 |

분야 내 고유 Content 수는 active seed와 현재 presentation mapping을 기준으로 하며, 같은 Content가 한 분야의 여러 section에 중복 표시되지 않도록 첫 section에서만 포함한다.

## 공통 생활 기반

Hub 상단은 V1.6F의 canonical Content 9개를 그대로 사용한다.

1. `life-family-levels` — 가문 생활 레벨
2. `life-mastery-foundation` — 생활 숙련도 기반
3. `life-common-gear` — 공통 생활 장비
4. `life-accessory-progression` — 생활 액세서리 진행
5. `life-mastery-tools` — 생활 숙련도 도구
6. `life-artifacts-lightstones` — 생활 유물과 광명석
7. `life-alchemy-stones` — 생활 연금석
8. `cheongmyeong-orb` — 청명의 보주
9. `energy-foundation` — 기운 기반

V1.6I의 공헌도·거점·생산 거점·일꾼·주거·창고·수송·제작 물류·왕실 공방 계열 Content 20개는 Hub의 `생활 기반과 경제`에서 모두 발견할 수 있다.

## Grouping과 presentation mapping

- backend의 `LifeSkillPresentation`은 Content slug를 `분야 기반`, `시작하기`, `장비와 세팅`, `핵심 시스템`, `반복과 루틴`, `심화 콘텐츠`, `관련 생활 기반과 경제`에 배치한다.
- 이 설정에는 수량·조건·게임 규칙·추천 수익 같은 game fact가 없다.
- 표시 이름, 요약, 검증 상태, 최종 검증일, 사용자 상태는 매 요청 canonical Content/Evidence/UserContentState에서 읽는다.
- active Content만 포함하며, mapping 대상이 seed에 없거나 inactive이면 결과에서 제외한다.
- Content 상세 지식과 evidence는 복제하지 않고 기존 `/content/:slug`를 재사용한다.
- 항해·물물교환의 Carrack 링크는 분야에 포함된 Content ID와 active Project의 `content_id` 관계를 조회해서 생성한다. Project 수량은 Life 코드에 복제하지 않았다.

## API

추가한 endpoint는 모두 read-only DTO/aggregation이다.

- `GET /api/life`
  - 공통 기반, 생활 기반·경제 Content, 10개 분야 요약을 반환한다.
- `GET /api/life/{skill}`
  - 분야별 section, 진행도, 관련 Project를 반환한다.
  - 지원하지 않거나 대표 active Content가 없는 분야는 404를 반환한다.

별도 캐시나 Life persistence는 없다.

## 진행도 집계 규칙

- 기존 `UserContentState`의 `not_started`, `foundation`, `in_progress`, `completed`, `paused`, `ignore`만 사용한다.
- 상태 행이 없으면 `not_started`로 본다.
- `total`은 분야에 실제 포함된 active 고유 Content 수다.
- `ignore`는 별도 개수로 표시하며 `tracked = total - ignored`로 추적 분모에서 제외한다.
- 나머지 상태 개수는 canonical 사용자 상태를 그대로 합산한다.

## Routes와 UI

- global navigation에 `생활`을 추가했다.
- `/life`
  - 공통 기반 카드
  - 10개 분야 카드와 검증일·검증 badge·Content 수·진행 요약
  - 생활 기반과 경제 링크 목록
- `/life/:skill`
  - 실제 Content가 있는 section만 표시
  - canonical 사용자 상태와 verification 표시
  - 기존 Content Detail 링크
  - 대표 Content를 대상으로 기존 `content_onboarding`, `next_action` Prompt Bridge 재사용
  - 실제 Project-Content 연결이 있는 관련 Project 링크

새 Prompt mode나 Life 전용 prompt collector는 추가하지 않았다.

## 검증 결과

### Backend

- `uv run pytest -q -p no:cacheprovider tests/test_life_hub.py`
  - 7 passed
- `uv run pytest -q -p no:cacheprovider`
  - 210 passed
- canonical 분야·foundation·경제 영역, 채집/낚시/항해 grouping, 고유 active Content, 사용자 진행도와 ignore 정책, canonical verification/date, Project 관계, 404를 검증한다.
- 알려진 경고: 기존 Starlette TestClient의 `httpx2` 전환 안내 1건.

### Frontend

- `npm.cmd run typecheck` — passed
- `npm.cmd run lint` — passed
- `npm.cmd run test -- --run` — 12 files / 45 tests passed
- `npm.cmd run build` — passed, 40 modules transformed
- navigation과 두 route, Hub 기반/분야/검증/진행/링크, Detail grouping/빈 section 숨김/상태/Prompt/Project/error 흐름을 검증했다.

### 공통

- `git diff --check` — passed
- 작업 전 실제 `backend/bdo.db` SHA-256:
  `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
- 구현 후 실제 `backend/bdo.db` SHA-256:
  `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
- 동일 여부: 동일

## 변경하지 않은 영역

- `data/seed_sources.json`, `data/seed_contents.json`, `data/seed_projects.json` 변경 없음
- DB model/schema 및 Alembic migration 변경 없음
- 실제 `backend/bdo.db` 변경 없음
- 기존 game fact 변경 및 신규 game fact 추가 없음
- 외부 웹 조사, 시장 가격, 시간당 수익, 계산기, 새 Project, 외부 API/LLM 추가 없음
- Prompt Bridge 명세와 mode 변경 없음

## 다음 Life research gap

아래는 UI에서 드러난 데이터 공백이며 V1.9A에서 값을 추측하거나 보완하지 않았다.

- 채집: canonical 시스템·도구·특수 채집 데이터는 있으나 실제 입문 동선과 추천 채집처 전략은 부족하다.
- 낚시: 자동 낚시·신선도·황실 납품 등 시스템은 있으나 세팅 전략, 위치별 어종/드롭과 추천 낚시터 데이터가 부족하다.
- 재배: 현재 주기와 핵심 시스템은 있으나 목적별 재배 전략 및 경제 비교 데이터가 부족하다.
- 가공: 현재 시스템과 대량 가공은 있으나 재료별 가공 루트와 수익성 데이터가 부족하다.
- 요리/연금: 기반·숙련·반복 데이터는 있으나 전체 레시피, 확률과 비용 대비 효율 데이터는 범위 밖으로 남아 있다.
- 조련: 현재 시스템과 환상마 progression은 있으나 말 스탯·교배·입문 동선에 대한 심화 데이터가 부족하다.
- 수렵: 공식 기반 시스템은 있으나 초보 실전 동선, 대상별 위치·전리품·효율 데이터가 부족하다.
- 항해/물물교환: 기존 해양 Content와 Carrack Project는 연결되지만 항해 자체의 전용 `*-current-system` 대표 Content와 실전 수익/동선 데이터는 부족하다.
- 생활 경제: 기반 구조는 발견 가능하지만 동적 가격, 주거지 전체 atlas, 추천 거점/일꾼 ranking은 구현·seed 범위 밖이다.

이 목록은 후속 research 입력 후보일 뿐이며, repository에 별도 V1.9B milestone 범위를 정의하지 않는다.
