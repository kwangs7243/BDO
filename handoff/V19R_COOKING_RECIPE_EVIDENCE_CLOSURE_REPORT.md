# V1.9R — Cooking Recipe Evidence Verification Closure

## Baseline and delivery

- Base main: `fbbea7294c59fe4ee5dffe21b5f6cca566094221`
- Branch: `feature/v1.9r-cooking-recipe-evidence-closure`
- Commit: this report is included in `data: verify initial cooking recipe evidence`; resolve its SHA with `git log -1 --format=%H -- handoff/V19R_COOKING_RECIPE_EVIDENCE_CLOSURE_REPORT.md`.
- Research date: 2026-09-11 (KR)
- Status: implementation and validation complete. No main merge performed.

## Verification meaning

Recipe `verified` means the canonical value was cross-checked sufficiently for current use. It does not mean a current Pearl Abyss webpage directly lists every exact number. Official, community and third-party provenance remains represented independently by Source metadata under ADR-014 and ADR-018.

Detailed source assessment: [V1.9R research](../docs/research/V19R_COOKING_RECIPE_EVIDENCE_CLOSURE_RESEARCH.md). The V1.9Q research note remains unchanged as historical context.

## Recipe results

### Beer

- Formula: grain 5; mineral-water 6 OR purified-water 3; leavening-agent 2; sugar 1; beginner 1.
- Source hierarchy: current BDO Codex plus a Pearl Abyss-domain `community_guide`; current official guide supports grain/water grouping and one-attempt semantics, not an official current 6-to-3 table.
- Final aggregate verification: `verified`.

### Vinegar

- Formula: grain 1; fruit 1; leavening-agent 1; sugar 1; beginner 1.
- Source hierarchy: current BDO Codex plus a Pearl Abyss-domain `community_guide`; the user post remains community evidence.
- Final aggregate verification: `verified`.

### Pickled Vegetables

- Formula: vegetable 8; vinegar 4; leavening-agent 2; sugar 2; apprentice 1.
- Official evidence: 2021 Pearl Abyss event directly records cabbage 8 and the exact remaining formula/skill.
- Current cross-check: current BDO Codex matches; current official guide supports cabbage membership in the vegetable group.
- Final aggregate verification: `verified`.

### Grilled Bird Meat

- Formula: bird-meat 2; deep-frying-oil 6 OR cottonseed-oil 6; cooking-wine 2; salt 1; beginner 1.
- Official evidence: new `cooking-grilled-bird-meat-official-2018` directly supports chicken 2, deep-frying oil 6, cooking wine 2, salt 1 and beginner 1.
- Current cross-check: current BDO Codex supports the complete current option set.
- Cottonseed boundary: the 2018 official Source is not connected to cottonseed-oil quantity or the whole formula claim; cottonseed-oil 6 remains supported by current BDO Codex only.
- Final aggregate verification: `verified`.

## Canonical baseline

| Entity | Current |
| --- | ---: |
| Source | 191 |
| Content active | 294 |
| FACT | 280 |
| STRATEGY | 63 |
| MEASUREMENT | 11 |
| Relation | 521 |
| Material active | 41 |
| IngredientGroup / GroupMember active | 4 / 20 |
| Recipe / IngredientSlot / IngredientOption active | 4 / 16 / 18 |
| Project | 1 |

Recipe Evidence remains 34 claim definitions. Adding the five valid 2018 official Source connections yields 44 Source-linked rows: `verified` 44, `needs_review` 0.

## AI export

- Manifest `schema_version`: 2, unchanged.
- Content 294 / Project 1 / Recipe 4 pages plus INDEX and manifest: 301 files.
- Four Recipe pages now expose aggregate `verification_status: "verified"` while preserving each Source's `official_patch`, `official_event`, `official_guide`, `community_guide` or `third_party_database` type.

## Validation

- V1.9R targeted Recipe/import/migration/export: `54 passed`.
- Backend full: `429 passed`.
- AI export write/check: `301 files`, current.
- Frontend typecheck: passed.
- Frontend lint: passed.
- Frontend tests: 14 files / 57 passed.
- Frontend build: passed.
- `git diff --check`: passed.
- Existing Starlette TestClient deprecation warning remains.

## Compatibility and non-goals

- Schema change: none.
- Migration: none.
- Recipe structural change: none; all existing materials, quantities, slots, options and skill values are unchanged.
- Calculator: not implemented.
- Project API/calculation, PromptContextBundle, backup version 1, personal inventory/checklist/progress and frontend behavior are unchanged.

## DB safety

- Pre: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- Post: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- Actual `backend/bdo.db` was not used for migration, seed import or export generation.
