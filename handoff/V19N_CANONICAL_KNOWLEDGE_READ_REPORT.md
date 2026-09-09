# V1.9N — Canonical Knowledge Read Interface

기준일: 2026-09-09 KR
Base main: `8de7f7f1bd40c810e485ab072ad332363899be0f`
Branch: `feature/v1.9n-canonical-knowledge-read`
Commit: `feat: add canonical knowledge read interface`

## 결과

기존 canonical DB와 local-state API를 유지하면서 future API/AI consumer가 개인 상태 없이 재사용할 수 있는 read-only knowledge boundary를 추가했다. MCP, OpenAI API, Notion 연동, frontend 연결은 추가하지 않았다.

## Endpoints

- `GET /api/knowledge/search?q=<query>&limit=<n>`
- `GET /api/knowledge/contents/{slug}`
- `GET /api/knowledge/projects/{slug}`

모든 endpoint는 조회 전용이며 기존 `/api/contents/*`, `/api/projects/*`, `/api/prompt/*` 계약과 분리되어 있다.

## Search

### Fields

Content:

- identity: `name_ko`, `slug`
- overview: `summary`, `purpose`
- active Requirement: `title`, `description`, stable-key-order JSON `structured_value`
- active Step: `title`, `description`
- active Reward: `name`, `recommendation`, `notes`
- active Section: `title`, `body_markdown`

Project:

- identity: `name_ko`, `slug`
- overview: `summary`
- active Stage: `name`, `description`
- active ProjectMaterial/Material: material `name_ko`, `key`, ProjectMaterial `notes`

### Ranking

1. exact identity
2. identity prefix
3. identity contains
4. summary / purpose
5. Requirement / Step / Reward / Stage / Material narrative
6. Section body / notes

동점은 `rank → resource_type → name_ko → slug` 순으로 정렬한다. 사용자 상태나 DB 반환 순서는 ranking에 사용하지 않는다.

### Dedup

Content 또는 Project 하나가 여러 nested field에서 일치해도 resource result는 하나만 반환한다. `matches`는 정렬된 상위 3개 hit evidence만 포함하며 긴 text는 최대 240자로 결정적으로 자른다.

### Validation

- `q`: required, trim/whitespace normalize, casefold, 최대 200자
- missing / empty / whitespace-only `q`: `422`
- `limit`: 기본 20, 최소 1, 최대 50
- 형태소 분석, 초성 검색, fuzzy dependency, FTS/FULLTEXT, embedding/vector/LLM은 사용하지 않는다.

## Content knowledge boundary

Included:

- identity/overview/status/verification metadata
- active Requirement, Section, Step, Schedule, Reward, Relation
- current와 historical/superseded를 함께 추적할 수 있는 Source/Evidence
- 기존 active Evidence 규칙의 aggregate `verification_status`
- 기존 KST schedule 계산 semantics

Excluded:

- `user_state`
- `checklists`

`get_content_detail()`을 호출해 field를 제거하지 않는다. canonical relationship만 eager-load하는 `get_knowledge_content()`가 직접 DTO를 조립하므로 checklist period instance를 생성하지 않는다.

## Project knowledge boundary

Included:

- Project identity, linked Content slug, summary, active flag
- active Stage description/order/dependency seed keys
- active ProjectMaterial/Material identity, unit, required quantity, canonical notes와 lineage
- active acquisition sources

Excluded:

- `owned_quantity`
- `shortage`
- `inventory_note` / `inventory_updated_at`
- stage numeric ID
- `completed` / `completed_at` / personal `note`

`get_project_detail()`을 호출한 뒤 personal field를 숨기지 않는다. `get_knowledge_project()`는 `UserMaterialInventory`와 `UserProjectStageState` relationship을 로드하지 않는다.

## Read-only verification

세 knowledge endpoint 호출 전후 personal-state snapshot을 비교했다.

- ChecklistInstance: 변화 없음
- ChecklistItemState: 변화 없음
- UserContentState: 변화 없음
- UserMaterialInventory: 변화 없음
- UserProjectStageState: 변화 없음

같은 Project의 inventory와 stage completion을 local write API로 변경한 뒤에도 canonical Project knowledge JSON은 변경 전과 완전히 동일했다.

## Existing API compatibility

- Content detail: 기존 `/api/contents/{slug}`에 `user_state`, `checklists` 유지
- Project detail: 기존 `/api/projects/{slug}`에 owned quantity, shortage, inventory note, stage completion 유지
- PromptContextBundle: schema/selector/`canonical_facts`/golden semantic 변경 없음
- 기존 Content/Project/Prompt Bridge/checklist/user-state 관련 회귀 76 passed

## Schema / Migration / Seed / Frontend

- SQLAlchemy schema: 변경 없음
- Alembic migration: 변경 없음
- seed format/data: 변경 없음
- frontend code/API 연결: 변경 없음

## Canonical counts

| 항목 | V1.9N |
| --- | ---: |
| Source | 183 |
| Content | 294 active |
| FACT | 280 |
| STRATEGY | 63 |
| MEASUREMENT | 11 |
| Relation | 521 |

기존 V1.9M exact baseline 및 Source URL/reference integrity test가 전체 suite에서 통과했다.

## Validation

- V1.9N targeted: 22 passed
- related Content/Project/Prompt Bridge/checklist/user-state regression: 76 passed
- backend full: 353 passed, 1 existing Starlette deprecation warning
- frontend typecheck: passed
- frontend lint: passed
- frontend tests: 14 files / 57 passed
- frontend build: passed
- `git diff --check`: passed

## DB protection

- actual `backend/bdo.db` SHA-256 pre: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- actual `backend/bdo.db` SHA-256 post: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- schema/migration/seed import against actual DB: 실행하지 않음

## 범위 밖

추가하지 않았다.

- MCP server / ChatGPT app / OpenAI SDK/API
- Notion integration 또는 external personal-state sync
- caller-provided inventory 계산 API / 새 optimizer
- vector/embedding/fuzzy/FTS search
- frontend search migration/redesign
- schema/migration/seed/game data
- 후속 Content Deep Pack