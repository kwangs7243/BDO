# V1.9O — Stateless Project Calculation Interface

기준일: 2026-09-10 KR
Base main: `329d4f4e7421845a265e81611d08c0db48c52393`
Branch: `feature/v1.9o-stateless-project-calculation`
Commit: `feat: add stateless project calculation interface`

## 결과

V1.9N canonical Project read boundary 위에 caller가 요청마다 제공한 재료 수량만 사용하는 deterministic shortage 계산 API를 추가했다. 요청 수량은 ephemeral input이며 local DB에 저장하거나 `UserMaterialInventory`와 병합하지 않는다. frontend, Prompt Bridge, schema, migration, seed는 변경하지 않았다.

## Endpoint

- `POST /api/calculations/projects/{slug}`

POST는 request payload를 받기 위한 transport 선택이며 persistence를 뜻하지 않는다.

## Request contract

```json
{
  "inventory": [
    {
      "material_key": "moon-vein-flax",
      "quantity": 75
    }
  ]
}
```

- `inventory`: 생략하거나 빈 배열 사용 가능
- identity: stable `Material.key`
- missing quantity: 항상 `0`
- duplicate key: 전체 요청 `422`
- unknown target Project material key: 정렬된 deterministic detail로 전체 요청 `422`
- quantity: 0 이상인 finite number만 허용
- unknown Project slug: `404 Project not found`

## Calculation

- 공식: `shortage = max(required_quantity - provided_quantity, 0)`
- `satisfied`: shortage가 0이면 `true`
- ordering: V1.9N `KnowledgeProjectOut.materials` canonical order 유지
- row identity: `project_material_seed_key`
- repeated Material: 같은 caller quantity를 각 ProjectMaterial row에 적용
- summary: unique material이 아닌 ProjectMaterial requirement row 기준

기존 local Project tracker도 같은 `calculate_shortage()` pure helper를 사용하므로 0, 75, 200 입력에서 각각 180, 105, 0으로 동일하게 계산된다.

## Ownership

- canonical owner: BDO DB의 active ProjectMaterial 및 active Material
- caller state: 요청 처리 동안만 존재하는 ephemeral input
- local fallback: 없음
- persistence: 없음
- canonical source: V1.9N `get_knowledge_project()`
- 금지한 우회: personal state를 포함하는 `get_project_detail()`을 calculator에서 호출하지 않음

## Read/write verification

계산 호출 전후 다음 personal-state 및 canonical table snapshot이 동일함을 테스트했다.

- `UserMaterialInventory`: 변화 없음
- `UserProjectStageState`: 변화 없음
- `UserContentState`: 변화 없음
- `ChecklistInstance`: 변화 없음
- `ChecklistItemState`: 변화 없음
- `Project`: 변화 없음
- `Material`: 변화 없음
- `ProjectMaterial`: 변화 없음

## Local independence

빈 caller inventory의 응답을 저장한 뒤 기존 local inventory API로 `moon-vein-flax = 100`을 저장하고 같은 stateless 요청을 다시 호출해도 응답은 완전히 동일했다. caller payload를 0에서 75로 바꿀 때만 해당 shortage가 180에서 105로 변경된다.

## Existing compatibility

- Project API: 기존 목록·상세·재고 저장·stage 상태 계약 유지
- Knowledge API: V1.9N search 및 canonical Content/Project DTO 유지
- PromptContextBundle: schema, selector, golden output 변경 없음
- archived/inactive ProjectMaterial은 V1.9N canonical projection과 동일하게 계산 대상에서 제외
- related regression: 128 passed

## ADR-016

Caller-provided personal state는 deterministic calculation input으로 사용할 수 있지만 local user-state table에 자동 저장하지 않는다. canonical requirement ownership은 BDO DB에 유지하고, 누락 수량은 local fallback이 아닌 0으로 처리한다. persistence/sync는 별도 명시적 milestone으로 남긴다.

## Schema / Migration / Seed / Frontend

- SQLAlchemy schema: 변경 없음
- Alembic migration: 변경 없음
- seed format/data: 변경 없음
- frontend code/API 연결: 변경 없음

## Canonical baseline

| 항목 | V1.9O |
| --- | ---: |
| Source | 183 |
| Content | 294 active |
| FACT | 280 |
| STRATEGY | 63 |
| MEASUREMENT | 11 |
| Relation | 521 |

기존 V1.9M exact baseline test가 전체 backend suite에서 통과했다.

## Tests

- V1.9O targeted: 22 passed
- related Project/Knowledge/Prompt Bridge/checklist/user-state regression: 128 passed
- backend full: 375 passed, 1 existing Starlette deprecation warning
- frontend typecheck: passed
- frontend lint: passed
- frontend tests: 14 files / 57 passed
- frontend build: passed
- `git diff --check`: passed

## DB SHA

- pre: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- post: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- unchanged: yes
- schema/migration/seed import against actual DB: 실행하지 않음

## 범위 밖

추가하지 않았다.

- Notion/MCP/ChatGPT/OpenAI SDK 연동
- personal-state persistence 또는 external/local state sync
- frontend integration
- recipe, price, profit, run-count 계산
- stage completion filtering/optimizer/next-action 추천
- schema/migration/seed/game data
