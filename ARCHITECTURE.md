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
        ├──────────────► Existing FastAPI structured APIs
        │
        ├──────────────► Prompt Context Builder
        │                   │
        │                   ▼
        │             PromptContextBundle
        │
        └──────────────► Local reference/admin frontend
```

Canonical game knowledge belongs here. Do not independently maintain the same game facts in Notion or another personal-state backend.

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

FastAPI/domain modules include canonical content retrieval, period/reset computation, checklist state, Project projection/calculation, Life projections, user/local state, research/evidence flows, and `prompt_bridge`.

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

The current repository stores some personal project state locally. A future external personal-state integration may provide these values instead, but canonical requirements/formulas must remain reusable regardless of where personal values live.

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

Potential future capability gaps to evaluate only when needed include server-side search/identity resolution, knowledge-only context, and pure deterministic calculations with caller-provided state.

## Data update philosophy

Do not make live website scraping a runtime dependency.

Research/import remains separate from runtime retrieval. Stored verified canonical knowledge and existing local functionality must remain usable without external AI services.
