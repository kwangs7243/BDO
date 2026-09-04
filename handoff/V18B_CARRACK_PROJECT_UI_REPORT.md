# V1.8B — Carrack Project Experience 보고서

기준일: 2026-09-05 (Asia/Seoul)

## 결과

V1.8A Project Tracker backend를 generic React 화면에 연결했다. 사용자는 Project 메뉴에서 프로젝트 목록을 열고, Carrack Advance 상세에서 단계 상태와 재료 현황을 확인하며, 보유량과 메모를 명시적으로 저장하고, backend가 다시 계산해 반환한 부족량을 확인할 수 있다. Closure에서 저장된 inventory note와 갱신 시각을 Project detail 응답에 추가해 새로고침 후에도 메모를 복원하도록 보완했다.

V1.8A는 main에 merge commit `d9c021571bbfa1927925374c40c27f4d129004ab`로 병합했고, V1.8B는 최신 main에서 만든 `feature/v1.8b-project-ui`에서 구현했다.

## 변경 파일

- `backend/app/schemas.py`: Project material 응답에 nullable inventory note와 갱신 시각을 추가했다.
- `backend/app/projects.py`: 이미 조회한 사용자 inventory를 Project detail material에 투영한다.
- `backend/tests/test_project_tracker.py`: note 저장 후 Project detail 재조회 hydration 회귀 테스트를 추가했다.

- `frontend/src/types.ts`: V1.8A Project 응답/상태 타입을 추가했다.
- `frontend/src/api.ts`: Project 조회, 재고 저장, stage 상태 저장 메서드를 추가했다.
- `frontend/src/App.tsx`: Project 메뉴와 목록/상세 route를 추가했다.
- `frontend/src/features/projects/ProjectListPage.tsx`: generic Project 목록 화면을 추가했다.
- `frontend/src/features/projects/ProjectDetailPage.tsx`: stage와 material을 관리하는 상세 화면을 추가했다.
- `frontend/src/features/projects/ProjectApi.test.ts`: 실제 Project PUT endpoint, method, body 계약 테스트를 추가했다.
- `frontend/src/features/projects/ProjectListPage.test.tsx`: 목록, 링크, loading/error/empty 회귀 테스트를 추가했다.
- `frontend/src/features/projects/ProjectDetailPage.test.tsx`: Carrack 4 stages/9 materials와 저장 동작 회귀 테스트를 추가했다.
- `frontend/src/styles.css`: 기존 CSS 변수와 panel/card 패턴을 따르는 Project 스타일을 추가했다.
- `README.md`: 현재 milestone과 구현 화면 및 검증 수치를 V1.8B로 갱신했다.
- `docs/specs/001-core/tasks.md`: Carrack detail 항목만 실제 완료 상태로 갱신했다.
- `handoff/V18B_CARRACK_PROJECT_UI_REPORT.md`: 이 보고서를 추가했다.

backend API 응답 projection은 additive하게 확장했다. DB schema, migration, seed와 실제 DB는 변경하지 않았다.

## 신규 routes

- `/projects`: 활성 프로젝트 목록
- `/projects/:slug`: 선택한 프로젝트 상세

기존 Dashboard, Weekly, Content, Prompt Bridge routes는 유지했다.

## 신규 frontend components

### ProjectListPage

- backend가 반환한 Project 배열을 일반 목록으로 렌더링한다.
- 프로젝트 이름, 완료 stage 수/전체 stage 수, 부족 재료 종류 수를 표시한다.
- 대응 Content와 Project 상세로 이동하는 링크를 제공한다.
- loading, API error, empty list를 각각 처리한다.

### ProjectDetailPage

- 이름, summary, stage 진행도, 부족 재료 종류 수와 기존 Content 링크를 표시한다.
- active stage의 설명, 완료 여부/시각, note와 dependency를 표시한다.
- dependency는 안내 정보로만 보이며 checkbox를 잠그지 않는다.
- material을 stage별로 그룹화하고 required/owned/shortage/unit/note/source를 표시한다.
- 수량 변경만으로 PUT하지 않고 `재고 저장`을 눌렀을 때 저장한다.
- 저장 성공 뒤 detail을 재조회해 backend의 owned/shortage 값을 반영한다.
- 최초 mount에서는 backend의 persisted inventory note를 입력란에 복원하고, mount 이후 재조회에서는 사용자가 아직 저장하지 않은 현재 draft를 보존한다.
- stage 완료와 완료 해제를 같은 상태 API로 저장한다.
- mutation 실패 시 기존 완료 표시를 그대로 유지하고 오류를 노출한다.

## API 사용 계약

- `GET /api/projects`
- `GET /api/projects/{slug}`
  - 각 material에 nullable `inventory_note`, `inventory_updated_at` 포함
- `PUT /api/materials/{material_key}/inventory`
  - body: `{ quantity, note }`
- `PUT /api/projects/{project_slug}/stages/{stage_id}/state`
  - body: `{ completed, note }`

공통 `request<T>`의 JSON/error 처리를 재사용했다. Project 화면은 `required_quantity`, `owned_quantity`, `shortage`를 응답 그대로 표시하며 `required - owned`를 canonical 값으로 계산하지 않는다.

## Material source 표현

- source Content 이름을 `/content/{content_slug}`에 연결한다.
- `quantity_per_completion`이 있으면 단위와 함께 표시한다.
- 값이 null이면 0으로 바꾸지 않고 `수량 미확인`으로 표시한다.
- source notes가 있으면 함께 표시한다.

## 테스트 및 빌드

### Frontend

- `npm run typecheck`: 통과
- `npm run lint`: 통과
- `npm run test -- --run`: 6 files, 15 passed
- V1.8B Project 전용: 3 files, 11 passed
- `npm run build`: 통과, 36 modules transformed

전용 테스트는 Project 목록, Carrack 4 stages, 9 materials, required/owned/backend shortage, inventory PUT과 명시적 저장, persisted note 최초 hydration과 재조회 draft 보존, stage complete/uncomplete PUT, source Content 링크, null 수량 비-0 표현, loading/error/empty, dependency checkbox 비잠금을 검증한다.

### Backend regression

- `uv run pytest`: 162 passed, 1 deprecation warning
- warning: Starlette TestClient의 현재 httpx 호환 경고이며 V1.8B 변경으로 발생한 실패는 아니다.

## DB 무결성

- 작업 전 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 전체 검증 후 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 결과: 동일, `backend/bdo.db` 변경 없음

backend 테스트는 in-memory SQLite 또는 `tmp_path` DB를 사용했다.

Closure 검증 시점의 실제 DB SHA-256은 작업 전후 모두 `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`로 동일했다.

## 제외 범위

- DB schema/migration/project seed/Carrack 게임 데이터 변경
- 새로운 게임 자료 및 다른 Project 추가
- Prompt Bridge project context와 `project_optimizer`
- 자동 다음 행동, ETA, 거래소 가격, Crow Coin 최적화
- inventory allocation/reservation과 dashboard project widget
- UI framework 추가, 대규모 디자인 개편, LLM/API 연동

## 남은 후속 후보 및 제약

- Project Prompt Bridge와 `project_optimizer`는 계획대로 미구현 상태다.
- Persisted inventory note hydration은 closure에서 해결했다. `ProjectDetailOut.materials`가 저장된 note와 갱신 시각을 반환하며, 새로고침 또는 컴포넌트 재마운트 후 입력란에 복원된다.
- 다른 Project, dashboard widget, 자동 최적화는 이번 milestone에 포함하지 않았다.
