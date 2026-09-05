# V1.9B — User Data Backup & Restore 완료 보고

기준일: 2026-09-06

Source of Truth: `main @ cea841ad48ab0c4b255df0c5da80312a712c1b9b`

작업 브랜치: `feature/v1.9b-user-backup`

구현 커밋: `d382ecff143e9819cd9bd453bc95eeb67bd180a5`

## 완료 범위

- 사용자가 만든 상태만 JSON으로 내보내고 다시 가져오는 V1 형식을 구현했다.
- 백업 envelope는 `format=bdo-companion-user-backup`, `version=1`을 사용한다.
- 내보내기 순서는 stable key 기준으로 고정되어 동일 상태에서 결정적인 JSON 구조를 만든다.
- 모든 datetime은 timezone-aware 값만 허용하며 export 결과는 UTC로 정규화한다.
- import는 전체 payload를 먼저 검증한 뒤 한 transaction에서 수행한다.
- 신규 DB schema, migration, seed, game fact, Prompt Bridge 변경은 없다.

## 백업 포함 및 제외

포함하는 사용자 소유 상태:

1. `UserContentState`
2. 전체 `ChecklistInstance` 및 `ChecklistItemState` 이력
3. `UserMaterialInventory`
4. `UserProjectStageState`

제외하는 canonical 데이터:

- Content, Requirement, Section, Step, Reward, Schedule, Relation, Evidence
- ChecklistTemplate 및 ChecklistItem 정의
- Material, Project 및 ProjectStage 정의
- Source와 seed 원본
- DB numeric ID

## Stable identity 연결

| 사용자 상태 | 백업 identity |
| --- | --- |
| Content 상태 | `content_slug` |
| Checklist instance | `template_seed_key + period_key` |
| Checklist item 상태 | `item_seed_key` |
| Material inventory | `material_key` |
| Project stage 상태 | `project_slug + stage_seed_key` |

숫자 DB ID는 export하지 않는다. Import 시 현재 canonical table에서 stable key를 다시 해석한다. Archived canonical identity도 유효한 참조로 해석하지만 active로 되돌리지는 않으며 validation warning으로 알린다.

## Validation 규칙

다음 오류가 하나라도 있으면 write를 시작하지 않고 payload 전체를 거부한다.

- 알 수 없는 format 또는 version
- 존재하지 않는 Content, Checklist template/item, Material, Project/stage stable key
- Checklist item이 지정 template에 속하지 않는 경우
- 중복 Content 상태, checklist period/item, material inventory, project stage identity
- 음수 inventory 수량
- timezone 정보가 없는 datetime
- `period_start >= period_end`
- schema에 정의되지 않은 필드

Validation API는 영역별 개수, 오류와 warning을 반환한다. Import API도 같은 전체 검증을 통과한 payload만 처리한다.

## Merge / Replace 의미

### Merge

- 백업에 포함된 stable identity의 사용자 상태는 백업 값을 authoritative 값으로 upsert한다.
- 백업에 없는 로컬 사용자 상태와 과거 checklist 이력은 보존한다.
- 동일 백업을 반복 import해도 중복 행이 생기지 않는 idempotent 동작을 보장한다.

### Replace

- 네 사용자 상태 영역의 기존 행을 foreign-key 순서에 맞춰 제거한 뒤 백업 상태를 정확히 복원한다.
- Settings UI에서 replace 모드 선택만으로는 실행되지 않으며 별도 확인 checkbox가 필요하다.
- 응답에는 적용 개수와 삭제 개수를 함께 표시한다.

두 모드 모두 하나의 transaction에서 실행한다. Validation 또는 write 중 오류가 나면 rollback하며 부분 반영을 남기지 않는다.

## API

- `GET /api/settings/backup`
  - 현재 사용자 상태를 V1 backup envelope로 반환한다.
- `POST /api/settings/backup/validate`
  - write 없이 전체 payload와 stable identity를 검증한다.
- `POST /api/settings/backup/import`
  - `backup`과 `mode=merge|replace`를 받아 원자적으로 복원한다.

## Settings UI

- 전역 navigation과 `/settings` route를 추가했다.
- 사용자 상태만 포함되고 canonical game data는 제외됨을 화면에서 설명한다.
- JSON 파일을 로컬 브라우저에서 선택하고 서버 validation 결과를 먼저 표시한다.
- 기본 import 모드는 merge다.
- Replace는 명시적 확인 후에만 활성화된다.
- 성공 결과는 영역별 적용 개수와 replace 삭제 개수를 표시한다.
- Backup JSON은 외부 서비스로 업로드하지 않고 로컬 파일로 다운로드한다.

## Round-trip 및 canonical 불변성

- 네 사용자 상태 영역을 export한 뒤 replace import하고 다시 export했을 때 `exported_at`을 제외한 데이터가 동일함을 검증했다.
- Merge 재실행 시 결과가 중복 없이 동일함을 검증했다.
- 잘못된 payload import 후 사용자 상태가 부분 변경되지 않음을 검증했다.
- Import 전후 canonical row count와 stable identity가 동일함을 검증했다.
- Archived canonical 참조를 import해도 archived 상태는 그대로 유지됨을 검증했다.

## 검증 결과

### Backend

- `cd backend; uv run pytest -q -p no:cacheprovider tests/test_user_backup.py`
  - 23 passed
- `cd backend; uv run pytest -q -p no:cacheprovider`
  - 233 passed, 1 warning
  - warning은 기존 Starlette TestClient의 `httpx2` 전환 안내다.

### Frontend

- `cd frontend; npm.cmd run typecheck` — passed
- `cd frontend; npm.cmd run lint` — passed
- `cd frontend; npm.cmd run test -- --run` — 14 files / 57 tests passed
- `cd frontend; npm.cmd run build` — passed, 41 modules transformed

### 공통

- `git diff --check` — passed
- 작업 전 `backend/bdo.db` SHA-256:
  `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
- 구현 및 전체 테스트 후 SHA-256:
  `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
- 동일 여부: 동일

## 변경하지 않은 영역

- `data/seed_sources.json`, `data/seed_contents.json`, `data/seed_projects.json`
- SQLAlchemy DB model과 Alembic migration
- 실제 `backend/bdo.db`
- canonical game data와 evidence
- Prompt Bridge 계약과 동작
- 외부 API/LLM 호출

## Milestone 상태

V1.9B User Data Backup & Restore 범위는 완료되었다. Milestone B에 정의된 JSON export/import 항목은 stable-key validation, merge/replace, 원자성, history 보존, Settings UI와 회귀 테스트까지 구현되었다.
