# Codex Bootstrap — Current Repository

This file is a general repository bootstrap, not a milestone implementation request.

Always follow the explicit current task while respecting repository invariants.

## Read first

1. `AGENTS.md`
2. `docs/PRODUCT_DIRECTION.md`
3. `docs/CONSTITUTION.md`
4. `ARCHITECTURE.md`
5. `docs/DECISIONS.md`
6. latest relevant `handoff/`
7. relevant spec/data/research files

GitHub `main` is Source of Truth for implemented state. Do not infer current implementation from old milestone prompts.

## Current product boundary

The central asset is the verified BDO KR knowledge backend: canonical Content, structured requirements/rewards/relations, schedules, Source/Evidence, knowledge roles, historical preservation, Project canonical definitions, deterministic calculations, and retrieval/context contracts.

The local React frontend remains supported as reference, inspection, admin, and local operational UI. Do not assume consumer UI expansion is automatically the next priority.

## Personal state

Existing local personal-state tables/APIs remain valid and must be preserved.

Do not delete them, migrate them to Notion, create automatic two-way sync, or reinterpret all personal state as external unless the current milestone explicitly says so.

Future domain ownership must be explicit and domain-scoped.

## AI integration

Current repository contains Prompt Bridge and `PromptContextBundle`. These are reusable retrieval/context assets.

Do not add MCP/OpenAI/Notion/LLM runtime dependencies unless the current milestone explicitly asks for them.

If a future adapter is requested, prefer a thin adapter behind existing domain services and stable contracts.

## Game-data rules

- KR / Asia-Seoul
- no invented game facts
- latest effective official KR rule wins
- keep claim-level Evidence
- preserve historical/superseded information
- distinguish FACT / STRATEGY / MEASUREMENT
- keep reset/payout/cutoff/spawn concepts distinct
- do not use old guides to overwrite newer patches
- do not store unverified exact quantities as facts

## Git/data safety

Before work, verify branch/HEAD and working tree, inspect the latest handoff, and read current code/tests before editing.

For seed/import work, preserve stable `seed_key`, use temporary DBs for import regression, and do not modify the user's real `backend/bdo.db`.

Do not force a historical expected DB hash onto current user state.

## Compatibility

Do not casually break public FastAPI contracts, `PromptContextBundle`, `canonical_facts`, backup format, stable canonical identities, or local user history.

A compatibility-breaking change needs an explicit migration milestone.

## Validation

Run the validation required by the current milestone. For documentation-only work, do not make unrelated code/seed changes.

Always run `git diff --check` before completion.
