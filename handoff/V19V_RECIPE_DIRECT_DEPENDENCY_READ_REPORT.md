# V1.9V — Direct Recipe Dependency Read Interface

## Baseline and delivery

- Base main: `3fa50462caacfdcb5b8071e87564470475c94095`
- Branch: `feature/v1.9v-recipe-direct-dependencies`
- Implementation commit: included in `feat: add direct recipe dependency reads`; resolve with `git log -1 --format=%H -- handoff/V19V_RECIPE_DIRECT_DEPENDENCY_READ_REPORT.md`.
- Delivery verification: local/remote branch SHA equality and clean working tree are checked after the implementation commit and recorded in the delivery response.
- Main merge: not performed.
- Research owner: ChatGPT.
- External game research required: none.
- Codex external research: none.

## Architecture

`recipe_dependencies.build_recipe_dependency_index` accepts active canonical
`KnowledgeRecipeOut` DTOs and derives direct edges from:

```text
producer result_material_key == consumer explicit Material option material_key
```

`get_recipe_dependencies` loads active Recipe DTOs through
`get_knowledge_recipe`, builds the deterministic index and returns one
Recipe's direct upstream/downstream projection. No dependency table, row, seed
or migration was added. The endpoint reads no personal state and performs no DB
mutation.

ADR-020 records this derived/not-persisted decision.

## API and DTO

New additive endpoint:

```http
GET /api/knowledge/recipes/{slug}/dependencies
```

It returns Recipe/result identity and ordered `direct_upstream` /
`direct_downstream` edge lists. Each edge includes stable producer, consumer,
Material, consumer slot and option identities; consumer quantity and order;
producer/consumer aggregate verification status; and `is_alternative`.
Numeric DB IDs are not exposed. Unknown or inactive slugs return `404` with
`Recipe not found`.

## Current exact dependency graph

| Producer | Consumer | Material | Quantity | Alternative |
| --- | --- | --- | ---: | --- |
| vinegar | pickled-vegetables | vinegar | 4 | false |
| red-sauce | steak | red-sauce | 2 | false |
| red-sauce | frank-sandwich | red-sauce | 1 | false |
| tea-with-fine-scent | sute-tea | tea-with-fine-scent | 2 | true |
| grilled-sausage | ham-sandwich | grilled-sausage | 2 | true |
| grilled-sausage | frank-sandwich | grilled-sausage | 2 | true |

The six edges are runtime projections, not canonical entity rows.

## Semantic boundaries

- Only explicit Material options create edges.
- `is_alternative` is true when the consumer slot has multiple active options.
- IngredientGroup membership is not expanded and no member is selected.
- No producer is fabricated for `smoked-sausage` or
  `tea-with-strong-scent`.
- Dependencies are direct only. No transitive closure, raw-material flattening
  or recursive quantity propagation is performed.
- No output/yield, producer attempt count, special proc, mastery or mass-cooking
  behavior is inferred.
- Inventory, shortage, price, cost and profit are outside this read model.
- No Source, claim or Evidence row was added.

## AI export

All 15 Recipe Markdown pages include a Direct Recipe Dependencies section with
upstream/downstream edges, relative Recipe paths and explicit no-group,
direct-only, no-recursion and no-yield wording. Export manifest schema version
2 and its fields are unchanged.

- Content pages: 294
- Project pages: 1
- Recipe pages: 15
- Total files: 312

## Canonical counts

All canonical counts remain unchanged:

| Entity | Count |
| --- | ---: |
| Source | 213 |
| Content active | 294 |
| FACT | 280 |
| STRATEGY | 63 |
| MEASUREMENT | 11 |
| Relation | 521 |
| Material active | 78 |
| IngredientGroup active | 7 |
| GroupMember active | 35 |
| Recipe active | 15 |
| IngredientSlot active | 60 |
| IngredientOption active | 67 |
| Recipe claim definitions | 119 |
| Recipe Evidence | 206 |
| needs_review | 0 |
| Project | 1 |

## Tests and validation

- New V1.9V dependency tests: `8 passed`.
- Targeted Recipe seed/catalog/knowledge/calculation/export regression:
  `138 passed`.
- Backend full: `493 passed`.
- Frontend typecheck: passed.
- Frontend lint: passed.
- Frontend tests: 14 files / 57 passed.
- Frontend build: passed.
- AI export write/check: schema version 2, 312 files current.
- Existing Starlette TestClient/httpx deprecation warning: 1; no new warning introduced.
- `git diff --check`: passed.

## DB safety

- Pre SHA-256: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- Post SHA-256: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- Actual `backend/bdo.db` was not used for migration, seed import, export generation or tests and was not modified.
