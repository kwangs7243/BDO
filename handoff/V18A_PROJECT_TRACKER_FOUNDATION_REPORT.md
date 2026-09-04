# V1.8A Project Tracker Foundation Report

기준일: 2026-09-05 (Asia/Seoul)

## 결과 요약

V1.7D의 Content/evidence 정본 위에 Project Tracker backend foundation을 추가했다. 첫 fixture는 기존 `carrack-advance` Content를 재사용하는 `에페리아 중범선 : 점진` 한 건이다. 새 게임 정보나 Source/Content/Claim/Evidence는 추가하지 않았다.

## 변경 파일

- `backend/app/models.py`: Project 계열 정본 6개와 사용자 상태 2개 모델
- `backend/alembic/versions/20260905_0003_project_tracker_foundation.py`: 0003 forward migration
- `backend/app/project_seed.py`: 선택적 project seed 동기화와 참조/DAG 검증
- `backend/app/seed.py`: 기존 import 마지막에 선택적 project import 연결
- `backend/app/projects.py`: 조회, shortage, 재고와 단계 상태 서비스
- `backend/app/schemas.py`, `backend/app/main.py`: Project Tracker API schema와 endpoint
- `data/seed_projects.json`: Carrack Advance normalized projection
- `backend/tests/test_project_seed.py`, `backend/tests/test_project_tracker.py`: seed/API/semantic regression
- `backend/tests/test_migration.py`: 0001 → 0002 → 0003과 history 보존 경로
- `README.md`, `docs/specs/001-core/data-model.md`, `docs/data/SEED_FORMAT.md`, `docs/DECISIONS.md`, `docs/specs/001-core/tasks.md`: V1.8A baseline 동기화
- `handoff/V18A_PROJECT_TRACKER_FOUNDATION_REPORT.md`: 이 보고서

## Migration

- 파일: `20260905_0003_project_tracker_foundation.py`
- revision: `20260905_0003`
- down revision: `20260903_0002`
- Alembic head: `20260905_0003`
- 검증 경로: fresh 0001 → 0002 → 0003, `Base.metadata.create_all()` 선행 0001 DB → 0002 → 0003
- 두 경로 모두 기존 checklist item history와 `UserContentState`를 보존했다.

## 신규 테이블

Canonical / seed-managed:

- `project`
- `project_stage`
- `project_stage_dependency`
- `material`
- `project_material`
- `project_material_source`

User-owned:

- `user_material_inventory`
- `user_project_stage_state`

## Seed row 수와 Carrack fixture

| Entity | active rows |
| --- | ---: |
| Project | 1 |
| ProjectStage | 4 |
| ProjectStageDependency | 4 |
| Material | 9 |
| ProjectMaterial | 9 |
| ProjectMaterialSource | 9 |

- Project slug / linked Content: `carrack-advance` / `carrack-advance`
- 본체 재료 5종 요구량은 기존 `carrack-advance.requirement.body-materials` structured value와 일치한다.
- +10 무역선 파란 장비 4종은 기존 `carrack-advance.requirement.blue-gear-plus10`의 4종·+10 조건을 각각 1개로 투영한다.
- 정본 Reward로 수량을 확인할 수 있는 획득처 연결 4개는 기존 Reward amount와 일치한다.
- 까마귀 주화 상점 연결 5개는 교환 가격을 획득량으로 오해하지 않도록 `quantity_per_completion=null`이다.
- 현재 Project 계열 unexpected archive는 0이다.
- 기존 baseline은 Source 145 / Content 259 active / Claim 990 / Evidence 1,237 / Relation 401을 유지한다.

## API와 shortage 계약

- `GET /api/projects`
- `GET /api/projects/{slug}`
- `PUT /api/materials/{material_key}/inventory`
- `PUT /api/projects/{project_slug}/stages/{stage_id}/state`

Project detail은 stage `order_no`, material `order_no`, stable key 순으로 결정적으로 정렬한다. 재료 부족량은 backend에서 다음 식으로 계산한다.

`shortage = max(required_quantity - owned_quantity, 0)`

검증한 경우:

- owned 0 → shortage = required
- 0 < owned < required → shortage = required - owned
- owned > required → shortage = 0
- negative inventory 요청 → HTTP 422
- 완료 처리 → UTC `completed_at`, 미완료 복귀 → `completed_at=null`

## Seed idempotency와 사용자 상태 보존

- 동일 project seed를 3회 재수입해 모든 canonical row count와 Project/Stage/Dependency/Material/ProjectMaterial/MaterialSource ID가 동일했다.
- project seed 파일이 없는 기존 임시 seed directory에서는 project sync를 건너뛴다.
- 제거된 canonical row와 그 하위 source는 hard delete하지 않고 `active=false`로 archive한다.
- 사용자 inventory ID/quantity/note와 stage state ID/completed/completed_at/note는 재수입 및 canonical archive 뒤에도 보존됐다.
- duplicate material key/project slug, unknown Content/stage/source entity, 자기 의존과 DAG cycle은 import 오류다.

## 검증 결과

- Project seed/API/migration 지정 검증: `20 passed`
- backend 전체 수집: `161 tests`
- backend 전체 실행: `161 passed` (`1 warning`, Starlette TestClient의 httpx deprecation)
- `git diff --check`: 통과
- 실제 `backend/bdo.db` migration/import: 실행하지 않음

## DB SHA-256

- 작업 전: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 작업 후: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 결과: 동일

## 알려진 제한과 후속 후보

- frontend Project page와 Carrack detail UI는 구현하지 않았다.
- Prompt Bridge의 project context와 `project_optimizer`는 활성화하지 않았다.
- 실시간 거래소 가격, 자동 최적화, inventory reservation/allocation은 없다.
- Project seed는 Carrack Advance 한 건뿐이며 다른 선박·보물·장비 프로젝트는 추가하지 않았다.
- V1.8B는 현재 정식 scope로 확정하지 않았다. 명시적으로 남은 후보는 Carrack Project frontend이며, 별도 milestone 지시서에서 범위를 결정해야 한다.
