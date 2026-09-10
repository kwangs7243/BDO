# V1.9P — Zero-Cost AI Export Surface

기준일: 2026-09-10 KR
Base main: `143f3552699b9cc2f1707ddc6dfb3d293e1104fe`
Branch: `feature/v1.9p-zero-cost-ai-export`
Commit: `feat: add zero-cost AI export surface`

## Purpose

기존 canonical backend를 실행 중인 서버, OpenAI API, MCP hosting 또는 유료 cloud 없이 GitHub와 static AI consumer가 읽을 수 있도록 deterministic generated export를 추가했다. `ai_exports/`는 canonical seed/domain model에서 파생되는 disposable artifact이며 새로운 Source of Truth가 아니다.

## Cost constraint

필요하지 않다.

- OpenAI API 또는 다른 LLM API
- MCP/HTTP hosting, tunnel, paid cloud
- ChatGPT Pro
- vector DB, embedding API
- 외부 데이터 서비스
- 신규 Python dependency

## Exporter

- module: `backend/app/ai_export.py`
- canonical import: `import_seed()`
- Content projection: `get_knowledge_content()`
- Project projection: `get_knowledge_project()`
- default output: repository root `ai_exports/`

### CLI write

```powershell
cd backend
uv run python -m app.ai_export write
```

Expected set을 생성·갱신하고, output directory 내부의 stale/extra generated file만 제거한다. repository 밖 파일은 삭제하지 않는다.

### CLI check

```powershell
cd backend
uv run python -m app.ai_export check
```

파일을 수정하지 않고 expected tree와 disk tree의 changed/missing/extra 경로를 결정적으로 비교한다. 불일치가 있으면 non-zero로 종료한다.

## Canonical source and isolation

- canonical source: reviewed seed + existing domain services
- temporary DB: isolated in-memory SQLite
- actual `backend/bdo.db` used as export source: no
- personal state included: no
- Prompt Bridge user context used: no

Content와 Project slug enumeration만 canonical SQLAlchemy query를 사용한다. 각 실제 payload는 V1.9N service에서 가져오며 local operational `get_content_detail()`과 `get_project_detail()`은 호출하지 않는다.

## Generated tree

```text
ai_exports/
├─ INDEX.md
├─ manifest.json
├─ contents/  (294 Markdown pages)
└─ projects/  (1 Markdown page)
```

- Content pages: 294
- Project pages: 1
- INDEX: 1
- manifest: 1
- total files: 297
- total size at closure: 3,092,237 bytes

모든 Markdown은 generated warning으로 시작한다. INDEX는 사용 순서와 전체 Content/Project discovery 목록을 제공하고, manifest는 schema version, canonical identity, path와 count를 제공한다.

## Determinism

- generated clock/current time: excluded
- `ScheduleOut.next_occurrence`: excluded
- `generated_at`: excluded
- temporary/local path, hostname, DB SHA, random value: excluded
- schedule/evidence/stage numeric DB IDs: excluded
- ordering: explicit slug/category/name/stable-key order
- JSON: UTF-8, `ensure_ascii=False`, `sort_keys=True`, deterministic indent
- newline: LF with one trailing newline
- repeated build: byte-identical
- stale behavior: changed/missing/extra file을 정렬해 보고
- stale write behavior: expected set에 없는 output 내부 파일 제거

## Representative verification

### blood-altar

`ai_exports/contents/blood-altar.md`에서 identity, overview, requirements, steps, schedules, rewards, sections, relations, evidence를 확인했다. current evidence와 historical/inactive evidence가 별도 그룹이며 superseded 근거가 historical 그룹에 유지된다.

### gathering-onboarding-strategy

생활 전략 대표 page에서 `knowledge_role: strategy`를 포함한 canonical `structured_value`, 원문 description과 ordered steps가 그대로 보존됨을 확인했다.

### carrack-advance

`ai_exports/projects/carrack-advance.md`에서 stage dependency DAG, 9개 ProjectMaterial requirement, acquisition sources와 다음 stateless contract를 확인했다.

- caller quantity: ephemeral personal state
- missing quantity: 0
- local inventory fallback: false
- persistence: false
- shortage: `max(required_quantity - provided_quantity, 0)`

## Personal-state independence

임시 DB에 `UserContentState`, `UserMaterialInventory`, `UserProjectStageState`를 추가한 뒤에도 representative Content/Project Markdown byte가 완전히 동일했다. export build 전후 전체 canonical/personal table snapshot도 동일했다.

## Compatibility

- Knowledge API: unchanged
- Calculation API: unchanged
- PromptContextBundle/schema/selector/golden: unchanged
- existing local user state and backup semantics: unchanged
- frontend code/API integration: unchanged
- new REST endpoint: none

## Schema / Migration / Seed / Dependencies

- SQLAlchemy schema: unchanged
- Alembic migration: unchanged
- seed format/data: unchanged
- `backend/pyproject.toml`: unchanged
- `backend/uv.lock`: unchanged
- frontend: unchanged

## Canonical baseline

| Item | V1.9P |
| --- | ---: |
| Source | 183 |
| Content | 294 active |
| FACT | 280 |
| STRATEGY | 63 |
| MEASUREMENT | 11 |
| Relation | 521 |
| Project | 1 active |

기존 exact canonical baseline test가 전체 backend suite에서 통과했다.

## Tests

- V1.9P targeted: 16 passed
- related Knowledge/Project/Prompt Bridge/seed/import/user-state regression: 151 passed
- export freshness check: 297 files current
- backend full: 391 passed, 1 existing Starlette deprecation warning
- frontend typecheck: passed
- frontend lint: passed
- frontend tests: 14 files / 57 passed
- frontend build: passed
- `git diff --check`: passed

## DB SHA

- pre: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- post: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- unchanged: yes
- actual DB migration/seed import: not executed

## ADR-017

Generated AI exports are derived, disposable consumer artifacts. Canonical seed/domain model은 계속 Source of Truth이며, `ai_exports/`는 개인 상태 없이 결정적으로 재생성하고 automated check로 freshness를 강제한다. future MCP/API consumer가 생겨도 generated directory를 canonical store로 승격하지 않는다.

## 범위 밖

추가하지 않았다.

- MCP, Apps SDK, OpenAI/ChatGPT API
- Notion integration/sync
- public server/hosting/tunnel/authentication
- vector DB/embedding/RAG server
- personal-state export/migration
- new REST API
- schema/migration/seed/game research
- frontend integration
