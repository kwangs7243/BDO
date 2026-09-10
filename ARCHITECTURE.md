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
        │                   └─ canonical-only Project projection
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

V1.9P generates `ai_exports/` as a disposable canonical projection. It is not a Source of Truth and must not be edited as independently maintained knowledge. The builder imports reviewed seed into an isolated temporary database, uses the V1.9N canonical Content/Project services, and excludes personal state, volatile runtime schedule fields, and numeric database identities.

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

FastAPI/domain modules include canonical content retrieval, the V1.9N `knowledge` read service, the V1.9P deterministic `ai_export` builder, period/reset computation, checklist state, Project projection/calculation, Life projections, user/local state, research/evidence flows, and `prompt_bridge`. The knowledge service exposes deterministic lexical search and canonical-only Content/Project projections without reading personal-state tables; the exporter consumes those projections through a temporary in-memory database.

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

V1.9N implements server-side lexical search/identity resolution and knowledge-only Content/Project retrieval at `/api/knowledge/*`. V1.9O adds pure deterministic Project shortage calculation with caller-provided quantities at `/api/calculations/projects/{slug}`; transport adapters, external persistence, synchronization, and optimization remain outside this boundary.

## Data update philosophy

Do not make live website scraping a runtime dependency.

Research/import remains separate from runtime retrieval. Stored verified canonical knowledge and existing local functionality must remain usable without external AI services.
