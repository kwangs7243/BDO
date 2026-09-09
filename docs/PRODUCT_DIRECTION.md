# Current Product Direction

Status: **current product/architecture constraint**
Effective from: 2026-09-09

This document defines the current role of BDO Companion.

It does **not** require an immediate rewrite, schema migration, frontend replacement, MCP implementation, or Notion integration.

Where an older V1 document assumes that the local web UI must be the user's primary daily interface, this document takes precedence for future prioritization.

## 1. Product role

BDO Companion's highest-value long-term role is a **verified Black Desert Online KR knowledge service and deterministic game-domain backend**.

Continue to preserve and expand:

- canonical Content
- Requirements / Steps / Rewards / Sections / Relations
- Schedule and reset semantics
- Projects and canonical dependency/material definitions
- Source / claim-level Evidence
- verification status
- FACT / STRATEGY / MEASUREMENT semantics
- historical and superseded information
- stable seed identity
- deterministic game-domain calculations
- retrieval/context contracts

The existing local web application remains supported, but future work must not assume that improving the consumer UI is automatically the highest-value product work.

## 2. Primary interaction hypothesis

Actual usage has shown that the user often prefers ChatGPT as the interaction surface: ChatGPT reads personal state when needed, reads verified BDO knowledge when needed, performs reasoning, and updates personal state only after user-confirmed actions.

This does not make AI transport part of the current implementation by default.

## 3. Knowledge ownership

BDO Companion remains the Source of Truth for shared Black Desert game-domain knowledge managed by this repository:

- game rules
- current KR content definitions
- requirements
- rewards
- schedules/resets
- recipes and structured game-domain facts when researched
- acquisition sources
- project canonical requirements
- official/community sources
- evidence
- patch history
- current vs historical/superseded boundaries
- deterministic calculations derived from canonical rules

Do not create a second independently maintained canonical copy of this knowledge in Notion or another personal-state system.

## 4. Personal-state ownership

Personal state is information primarily about the user, for example current goal, priority, owned quantity, completed actions, progress, task, plan, decision, and personal note.

Actual use has validated Notion as an effective AI-readable/writable personal-state backend for some life-skill project workflows.

However:

- do not assume every personal-state domain must move to Notion now
- do not migrate hunting/combat/gear/quest/account/checklist/project state without an explicit milestone
- do not delete existing local state tables
- do not silently create two authoritative copies of the same personal state

Ownership may be **domain-scoped and incremental**.

A future milestone must explicitly define which personal-state domain is external-primary, local-primary, mirrored, imported/exported, or fallback-only.

## 5. Existing local user-state

The existing local state model remains supported:

- `UserContentState`
- `ChecklistInstance`
- `ChecklistItemState`
- `UserMaterialInventory`
- `UserProjectStageState`
- backup / restore behavior

Until a specific migration/integration milestone says otherwise, preserve schema, history, backup compatibility, and existing API behavior.

Future work should treat local state as a supported capability, not as proof that every new personal-state feature must be stored locally.

## 6. Frontend role

The existing React frontend remains part of the repository.

Acceptable long-term roles include:

- canonical knowledge inspection
- Content reference
- Source/Evidence review
- verification/conflict review
- search
- project definition inspection
- debugging
- admin/research support
- local operational fallback
- occasional direct user reference

Future milestones should not spend significant effort on consumer-facing dashboard/navigation/polish unless there is an explicit user need.

Do not delete or rewrite the frontend merely because AI becomes the preferred interaction layer.

## 7. Prompt Bridge and retrieval

The existing Prompt Bridge is a reusable retrieval/context asset.

Preserve:

- `PromptContextBundle`
- deterministic selection
- verification-aware serialization
- FACT / STRATEGY / MEASUREMENT roles
- unresolved/conflict separation
- source metadata
- deterministic compaction
- existing API compatibility, including `canonical_facts`

The Markdown renderer and copy/download UI are V1 consumer mechanisms.

Future AI integrations may consume structured Content/Project APIs directly, `PromptContextBundle`, a future knowledge-only projection, or deterministic calculation functions.

Do not require all AI consumers to use rendered Markdown when structured data is more appropriate.

## 8. Future AI adapters

MCP, ChatGPT apps, OpenAI API adapters, or other AI transport layers are future consumers.

Default architectural rule:

```text
canonical DB
    ↓
existing domain services
    ↓
stable API / DTO / context boundary
    ↓
thin adapter
    ↓
AI consumer
```

Do not redesign core canonical models around a specific AI vendor or protocol.

Do not implement an adapter unless the milestone explicitly asks for it.

Likely future gaps may include server-side search/identity resolution, knowledge-only retrieval without local state, and pure deterministic calculations that accept caller-provided personal state. These are future design inputs, not work authorized by this document.

## 9. Project model boundary

BDO Companion should continue to own canonical project knowledge such as stages, dependencies, required materials, acquisition sources, source lineage, and deterministic formulas.

A personal-state backend may eventually own current owned quantity, completion state, goal date, priority, task list, and personal decisions.

Do not duplicate canonical material requirements into a personal-state store as independently maintained game facts.

## 10. Roadmap priority

Future milestone selection should prefer work that strengthens:

1. canonical accuracy
2. source/evidence quality
3. useful knowledge coverage
4. stable deterministic retrieval/calculation
5. compatibility boundaries for future consumers

Consumer UI expansion is lower priority unless explicitly requested.

Large architecture rewrites are not implied by this direction.

Existing content milestones may continue when they improve canonical knowledge.

## 11. Development process

The established workflow remains unchanged.

ChatGPT inspects latest GitHub `main`, verifies Codex work, researches current game facts, defines milestones, writes Codex instructions, and reviews implementation.

Codex modifies the repository, runs tests, updates docs/handoff, and commits/pushes.

GitHub remains the final Source of Truth for repository state.

## 12. Non-goals

This direction does not authorize:

- schema surgery
- dropping user-state tables
- frontend rewrite/deletion
- API replacement
- Prompt Bridge removal
- V2 rebuild
- immediate Notion migration
- immediate MCP/OpenAI integration
- duplication of canonical game knowledge into Notion

The strategy is:

> Preserve the existing system, center future value on the knowledge backend, and change ownership or transport only through narrow explicit milestones.
