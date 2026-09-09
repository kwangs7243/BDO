# BDO Companion Agent Map

BDO Companion is a **Black Desert Online KR canonical knowledge service with an existing local reference/operational web app**.

Do not invent game data.

## Document precedence

Read in this order for future work:

1. `docs/PRODUCT_DIRECTION.md`
2. `docs/CONSTITUTION.md`
3. `ARCHITECTURE.md`
4. `docs/DECISIONS.md`
5. latest relevant `handoff/`
6. relevant `docs/specs/`
7. `docs/research/SOURCE_POLICY.md`
8. `docs/research/SEED_CATALOG.md`

`docs/specs/001-core/` and `docs/specs/002-prompt-bridge/` contain implemented contracts and V1 history, but their old consumer-UI product assumptions do not override `docs/PRODUCT_DIRECTION.md`.

GitHub `main` remains Source of Truth for implemented state.

## Current product boundary

The repository's highest-value asset is the verified game-domain backend:

- canonical Content
- Requirements / Steps / Rewards / Sections / Relations
- Schedule/reset semantics
- Source / claim-level Evidence
- FACT / STRATEGY / MEASUREMENT
- historical / superseded preservation
- Project canonical definitions
- deterministic calculations
- retrieval/context contracts

The React frontend remains supported as reference / inspection / admin / local operational UI.

Do not assume consumer-facing UI polish or new dashboards are a default priority.

## Personal state

Canonical game knowledge and personal state must remain separate.

Existing local state remains supported and must not be deleted or migrated without an explicit milestone:

- `UserContentState`
- checklist instances/item state
- `UserMaterialInventory`
- `UserProjectStageState`
- backup/restore history

Some personal-state domains may later use an external store such as Notion. Do not assume all domains are external or all domains are local. Ownership changes must be explicit and domain-scoped.

Never duplicate BDO canonical game knowledge into an external personal-state store as a second independently maintained Source of Truth.

## AI / adapter boundary

The existing `PromptContextBundle` and structured APIs are reusable contracts.

Future MCP/OpenAI/ChatGPT/other adapters should normally be thin consumers behind existing domain services.

Do not add OpenAI SDK, MCP server, Notion integration, LLM runtime, embedding/vector DB unless the current milestone explicitly requires it.

Do not break existing API or PromptContextBundle compatibility as speculative preparation.

## Development principles

- KR region / Asia-Seoul.
- Accuracy over feature count.
- Latest official KR evidence wins when current official sources conflict.
- Do not collapse `quest_reset`, `attempt_reset`, `record_cutoff`, `reward_payout`, and `spawn_schedule`.
- Do not expose unresolved data as verified fact.
- Update source/evidence and `last_verified_at` with rule changes.
- Preserve historical canonical rows and user history.
- Stable `seed_key` identity must survive text/order changes.
- DB code remains SQLAlchemy dialect-independent for SQLite/MySQL compatibility.
- Deterministic calculations belong in backend/domain logic, not LLM reasoning.
- Local core behavior must remain usable without an external AI service.

## Before a new milestone

1. fetch latest `main`
2. read the latest relevant handoff
3. inspect current code/data/tests
4. classify the requested value as canonical knowledge, deterministic domain logic, personal state, reference/admin UI, or future adapter/transport
5. make the smallest compatible change

Do not turn a product-direction discussion into a large rewrite unless the milestone explicitly authorizes one.

## Test invariants

Preserve tests for KST boundaries, custom reset boundaries, reward payout semantics, stale/superseded Evidence, stable seed identity, historical import, Project calculations, checklist/user-state history, Prompt Bridge deterministic output/knowledge roles, and current content-specific semantic regressions.
