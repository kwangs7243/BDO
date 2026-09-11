# Architecture

## Current system role

BDO Companion is built around a canonical Black Desert Online KR knowledge model.

The local web UI is one consumer of that model. Future AI integrations may become additional consumers, but they should attach through stable service/API boundaries rather than redesigning the canonical database around a specific transport.

See `docs/PRODUCT_DIRECTION.md`.

## Canonical knowledge flow

```text
KR official guides / patches / GM notes
community / measurements when appropriate
        │
        ▼
Research Staging
(raw source + extracted claims + unresolved conflicts)
        │ verification
        ▼
Canonical Knowledge DB
(Content / Requirement / Step / Reward / Section / Relation
 Schedule / Source / Evidence / Project canonical definitions)
        │
        ├──────────────► Knowledge Read Service
        │                   ├─ deterministic lexical search
        │                   ├─ canonical-only Content projection
        │                   ├─ canonical-only Project projection
        │                   └─ canonical-only Recipe projection
        │                              │
        │                              ▼
        │                     GET /api/knowledge/*
        │
        ├──────────────► Existing FastAPI structured/local APIs
        │
        ├──────────────► Prompt Context Builder
        │                   │
        │                   ▼
        │             PromptContextBundle
        │
        └──────────────► Local reference/admin frontend
```

Canonical game knowledge belongs here. Do not independently maintain the same game facts in Notion or another personal-state backend.

## Static AI export surface

```text
Canonical Seed
     │
     ▼
Temporary in-memory DB + existing domain services
     │
     ▼
Deterministic AI Export Builder
     │
     ▼
ai_exports/
     │
     ▼
GitHub / static AI consumer
```

V1.9P generates `ai_exports/` as a disposable canonical projection. It is not a Source of Truth and must not be edited as independently maintained knowledge. The builder imports reviewed seed into an isolated temporary database, uses canonical Content/Project services and the V1.9Q Recipe read service, and excludes personal state, volatile runtime schedule fields, and numeric database identities. V1.9Q adds four recipe pages and a Recipes index; manifest version 2 includes `recipe_count` and `recipes` alongside existing entries.

The committed export can be read without a running BDO server and requires no OpenAI API, MCP hosting, paid cloud, external LLM, or other paid AI dependency. Automated freshness checks fail when the committed generated tree differs from the canonical seed/domain result.

## Personal-state boundary

Current local capabilities include `UserContentState`, checklist state/history, `UserMaterialInventory`, and `UserProjectStageState`.

These remain implemented and supported.

Future domain-scoped personal-state ownership may be external for some workflows. That possibility does not imply an immediate migration of all local state.

Ownership of a personal-state domain must be explicit. Do not silently mirror two writable Sources of Truth.

## Frontend

Current frontend is React + TypeScript + Vite with Content/Life/Project/Weekly/Prompt/Settings features.

It remains supported and may emphasize reference, inspection, Source/Evidence review, debugging, admin/research support, and local operational fallback.

Consumer UX expansion is not an implicit architecture requirement.

## Backend

FastAPI/domain modules include canonical content retrieval, the `knowledge` read service, the deterministic `ai_export` builder, period/reset computation, checklist state, Project and Recipe projection/calculation, Life projections, user/local state, research/evidence flows, and `prompt_bridge`. The knowledge service exposes deterministic lexical search and canonical-only Content/Project/Recipe projections without reading personal-state tables; both stateless calculators consume those canonical projections, and the exporter consumes them through a temporary in-memory database.

## Shared Material and Cooking Recipe foundation (V1.9Q)

`material_seed` synchronizes `seed_materials.json` before `project_seed` and `recipe_seed` resolve Material keys. Only the shared catalog archives missing materials. Without that file, historical embedded Project materials remain a partial compatibility input; supplying both authorities is an error. Neither domain importer owns user inventory.

Recipe → IngredientSlot → IngredientOption expresses AND between slots and OR within a slot. An option references either Material or IngredientGroup; members reference shared Material rows. Groups contain no global quantity multiplier. Quantities mean one cooking attempt, not guaranteed output, mixed substitution or large-cooking batch size. Migration `20260910_0004` adds five tables; existing Material and personal-state schemas are unchanged.

`GET /api/knowledge/recipes/{slug}` and recipe search use typed claim Evidence and stable keys. Exact identity ranks before nested ingredient/member matches, capped at three per result. Official group membership can be verified independently of formula verification. V1.9Q itself included no Recipe calculator, Recipe UI, PromptContextBundle extension or backup version change.

V1.9T and V1.9U expand the same model to 15 verified Cooking Recipes without a schema change. The Recipe seed importer now validates the complete canonical tier vocabulary from `beginner` through `guru`; the database and API continue to store and expose the existing string field. Recipe result Materials may be reused as another Recipe's explicit input identity, but the calculator does not recursively expand dependencies.

## Direct Recipe dependency read model (V1.9V)

```text
Canonical Recipe DTOs
      │
      ├─ result Material identity
      └─ explicit Material options
                │
                ▼
Direct Recipe Dependency Builder
                │
                ├─ upstream producers
                └─ downstream consumers
                │
                ▼
GET /api/knowledge/recipes/{slug}/dependencies
```

`recipe_dependencies` derives an edge only when a producer
`result_material_key` equals a consumer option's explicit `material_key`.
The relation is not persisted. IngredientGroup membership is not expanded,
only direct edges are returned, and no personal state is read. The projection
does not infer output/yield, recursive quantities, option selection or
producer attempt counts. AI Recipe exports consume the same builder.

## Stateless Recipe batch calculation (V1.9S)

```text
Canonical Recipe
      +
attempt_count
      │
      ▼
Stateless Recipe Batch Calculation Service
      │
      ▼
POST /api/calculations/recipes/{slug}
```

`recipe_calculations` reuses `get_knowledge_recipe` and multiplies every `RecipeIngredientOption.required_quantity` by the strict positive integer `attempt_count`. It preserves slot AND, option OR, stable slot/option keys, option order, and IngredientGroup identity/member lists. Every alternative is returned independently; the service does not choose, add, mix, or optimize alternatives and does not resolve a group to one member.

The request and response are personal-state-free. The service neither reads nor writes `UserMaterialInventory`, has no inventory fallback, and performs no database mutation. Output quantity, cooking procs, quality conversion, shortage, profitability and optimization semantics remain outside this boundary. No schema, migration, seed, AI export format, PromptContextBundle or frontend change is required.

Existing domain functions are the preferred reuse boundary.

Future adapter code should call domain services/stable DTOs rather than raw SQL.

## Database strategy

SQLite compatibility remains required and MySQL remains optional through `DATABASE_URL`.

No database migration is implied by the current product-direction change.

## Reset engine

Recurring state uses period-scoped instances rather than destructive reset updates.

Keep daily task windows, quest resets, attempt resets, record cutoffs, reward payouts, spawn schedules, and event deadlines distinct.

## Knowledge freshness

Evidence is claim-scoped. Latest effective official KR evidence wins for current factual rules when an older source conflicts. Historical/superseded Evidence remains preserved.

FACT, STRATEGY, and MEASUREMENT semantics remain independent from verification status.

## Project knowledge vs personal project state

Canonical Project data includes project identity, stage DAG, required quantities, acquisition sources, and source lineage.

Personal project state includes owned quantity, completed stage, personal notes, and other user-specific progress.

The current repository stores some personal project state locally. External personal-state consumers may instead provide quantities to the V1.9O stateless calculation boundary without changing ownership or persisting those values.

```text
Canonical Project
      +
Caller-provided quantities
      │
      ▼
Stateless Project Calculation Service
      │
      ▼
POST /api/calculations/projects/{slug}
```

The calculator reuses the canonical-only V1.9N Project projection and the same shortage formula as the local tracker. Caller state is ephemeral request input: it is not written to the database, merged with `UserMaterialInventory`, or replaced by a local fallback when a quantity is missing.

## Prompt Bridge

Current V1 flow:

```text
request / target
      │
      ▼
Context Resolver
  ├─ canonical content
  ├─ schedules
  ├─ local user progress/checklists
  ├─ project shortages
  └─ evidence / unresolved claims
      │
      ▼
Context Budgeter
      │
      ▼
PromptContextBundle
      │
      ├─ structured API response
      └─ Markdown renderer / copy-download UI
```

Preserve the bundle contract and deterministic semantics.

Future AI consumers do not have to consume rendered Markdown if structured data is more appropriate.

## Future adapter boundary

```text
ChatGPT / MCP / API consumer
            │
            ▼
      thin adapter layer
            │
            ▼
existing BDO domain services
 / structured API contracts
 / PromptContextBundle
            │
            ▼
        canonical DB
```

The adapter is not implemented merely because this architecture permits it.

V1.9N implements server-side lexical search/identity resolution and knowledge-only Content/Project/Recipe retrieval at `/api/knowledge/*`. V1.9O adds pure deterministic Project shortage calculation with caller-provided quantities at `/api/calculations/projects/{slug}`. V1.9S adds pure Recipe option scaling at `/api/calculations/recipes/{slug}` while preserving all alternatives. Transport adapters, external persistence, synchronization, option resolution, output/profitability semantics, and optimization remain outside these boundaries.

## Data update philosophy

Do not make live website scraping a runtime dependency.

Research/import remains separate from runtime retrieval. Stored verified canonical knowledge and existing local functionality must remain usable without external AI services.
