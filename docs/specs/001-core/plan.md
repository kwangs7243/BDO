# Implementation Plan

## Phase 0 — Repository & quality gates
- Git init
- frontend/backend monorepo
- lint/typecheck/test commands
- env example
- DB migration(Alembic)

## Phase 1 — Core data + reset engine
- SQLAlchemy entities
- source/evidence tables
- period-key service
- daily/Thursday-weekly/custom schedule tests
- seed importer

## Phase 2 — Read-only knowledge UI
- dashboard shell
- content explorer
- content detail
- source badges
- global search

## Phase 3 — User progress
- checklist template/instance
- user content state
- notes
- history
- JSON export/import

## Phase 4 — Project engine
- stages/materials/inventory
- Carrack Advance seed migration
- shortage and next-action computation

## Phase 5 — Life foundation
- life hub
- skill detail template
- current 2026-09-02 unified life gear model
- character-role mapping

## Phase 6 — Research operations
- source registry UI
- claims needing review
- conflict report
- manual/import workflow
- optional URL fetch helper (do not make scraping a runtime dependency)

## Phase 7 — Expand content catalog
- weekly PvE
- world/guild bosses
- growth/internal systems
- treasure projects
- events

## Phase 7.5 — V1.5 Prompt Bridge
- deterministic context bundle builder
- verified/unresolved source-aware serialization
- 5 prompt presets
- content/project/weekly entry points
- copy/download only; no LLM/API calls
- details: `docs/specs/002-prompt-bridge/`

## Phase 8 — polish
- responsive
- keyboard search
- backup snapshots
- install/start scripts for Windows
