# V1.9Q — Cooking Recipe Canonical Foundation

## Baseline and delivery

- Base main: `e8874984905130f07bba404d62c1eab876049577`
- Branch: `feature/v1.9q-cooking-recipe-foundation`
- Commit: this report is included in `feat: add cooking recipe canonical foundation`; resolve its SHA with `git log -1 --format=%H -- handoff/V19Q_COOKING_RECIPE_FOUNDATION_REPORT.md`.
- Status: implementation and full validation complete; results confirmed on 2026-09-11. No main merge performed. Remote delivery SHA is verified after committing this report and recorded in the closing response.

## Research and verification boundary

[Research note](../docs/research/V19Q_COOKING_RECIPE_FOUNDATION_RESEARCH.md) records the 2026-09-10 investigation. The existing official `cooking-guide` Source provides current group membership and one-attempt semantics. A historical official event, two community posts and four BDO Codex item pages supply the seven new Sources. Community content on an official domain is not treated as an official guide.

Four groups' membership and four per-attempt claims are verified. All exact formula, skill and option-quantity claims remain needs_review. In particular, the purified-water and cottonseed-oil alternatives are not promoted to current official KR exact-quantity facts. No global high-quality/special multiplier is inferred.

## Shared Material ownership and legacy compatibility

- Moved the existing nine Carrack Material definitions into `data/seed_materials.json` and added 32 cooking Materials: 41 active in the shared catalog.
- Current `seed_projects.json` contains Project definitions only; its Project subtree is unchanged.
- `material_seed.sync_materials` resolves stable key identities before Project/Recipe import. Existing rows update in place.
- Shared catalog absence preserves existing Materials. Historical embedded Project materials remain a partial fallback only when the shared file is absent; they cannot archive cooking Materials. Shared plus embedded authorities are rejected, including an empty embedded list.
- Only the explicit shared catalog archives missing Materials. Project sync never owns global material archival.
- Legacy → shared → repeated shared → legacy → shared tests compare the original nine Material IDs, ProjectMaterial rows/FKs, canonical Project DTO and user inventory. Removed/reintroduced Recipe keys retain their original IDs.
- User inventory/checklist/content/stage history and backup version 1 remain separate from Recipe seed.

## Schema and importer

Migration `20260910_0004` follows `20260905_0003` and adds exactly five tables:

| Table | Role |
| --- | --- |
| IngredientGroup | stable group key and display identity |
| IngredientGroupMember | Material membership; unique group/material and group/seed_key |
| Recipe | stable slug, result Material, cooking skill and verification date |
| RecipeIngredientSlot | required ingredient slot; unique recipe/seed_key |
| RecipeIngredientOption | one Material or Group, positive quantity; unique slot/seed_key |

Database constraints enforce target XOR, quantity > 0 and positive skill level when present. Pydantic validation also rejects non-finite quantity, unknown references, duplicate identities, unsupported process/skill values and Evidence targets outside the owner. Import is stable upsert with archive/reactivation, not delete/recreate. Existing Material, personal-state and Evidence schemas are unchanged.

Recipe slots are AND; options are OR. Quantities belong to options for **one cooking attempt**. Group membership does not assign a global quantity equivalence. No result_quantity, recipe calculator, mixed replacement optimization or recursive recipe expansion was added.

## Seed and recipe result

| Recipe | 1-attempt options | Skill | Exact formula |
| --- | --- | --- | --- |
| beer | grain 5; mineral-water 6 OR purified-water 3; leavening-agent 2; sugar 1 | beginner 1 | needs_review |
| vinegar | grain 1; fruit 1; leavening-agent 1; sugar 1 | beginner 1 | needs_review |
| pickled-vegetables | vegetable 8; vinegar 4; leavening-agent 2; sugar 2 | apprentice 1 | needs_review |
| grilled-bird-meat | bird-meat 2; deep-frying-oil 6 OR cottonseed-oil 6; cooking-wine 2; salt 1 | beginner 1 | needs_review |

Groups: grain 5 members, fruit 7, vegetable 5, bird-meat 3. Total 20; no membership duplicates.

Recipe-domain Evidence uses typed targets `recipe`, `recipe_ingredient_slot`, `recipe_ingredient_option`, `ingredient_group`. There are 34 new claims producing 39 Source-linked Evidence rows (8 verified, 31 needs_review). Inactive/superseded history remains inspectable; current claims are not silently promoted.

## Knowledge and AI export

- `GET /api/knowledge/recipes/{slug}`: ordered canonical Recipe/result/slot/option/group/member DTO, claim-level Source/Evidence, no numeric DB identities or user state. Missing or archived Recipe returns 404.
- Existing knowledge search discovers Recipe identity and nested ingredient/group/member names and keys. Exact recipe identity outranks nested matches; at most three matches per result.
- Canonical read and recipe Markdown stay identical after adding beer inventory 999, wheat inventory 12345, checklist history, Content state and Project stage state.
- Export uses temporary in-memory DB → import_seed → knowledge service → renderer, never raw JSON rendering or actual user DB.
- Manifest schema version 2 preserves Content/Project fields and adds `recipe_count`/`recipes`; INDEX has Recipes.
- Content pages 294 / Project pages 1 / Recipe pages 4; INDEX + manifest = **301 files**.
- Stable ordering, historical evidence, no personal state/numeric IDs, deterministic output and LF freshness remain tested.

## Compatibility and regression fixture maintenance

Existing Project API and stateless Project calculation, PromptContextBundle and golden outputs, user backup v1 and frontend behavior are preserved.

Ten historical test fixtures that copy the current Project file now copy its separate shared Material catalog too. Their stable-ID and user-history assertions remain intact. V1.9M's Source-count equality is changed to a minimum to allow Recipe-only Sources; Content count, roles, relations and specific semantic checks remain unchanged. Project tests distinguish nine referenced Carrack Materials from 41 global Materials.

## Migration validation

Temporary SQLite only: upgrade through 0003 → 0004; five tables and constraints; invalid zero/negative/XOR inserts rejected; downgrade → 0003 preserves existing table set and Material row; upgrade again. A create_all-precreated Recipe schema also accepts the new migration. Actual local DB was not migrated.

## Canonical baseline

| Entity | Current |
| --- | ---: |
| Source | 190 |
| Content active | 294 |
| FACT | 280 |
| STRATEGY | 63 |
| MEASUREMENT | 11 |
| Relation | 521 |
| Material active | 41 |
| IngredientGroup active | 4 |
| GroupMember active | 20 |
| Recipe active | 4 |
| IngredientSlot active | 16 |
| IngredientOption active | 18 |
| Project / Stage / referenced Materials | 1 / 4 / 9 |

Content seed and existing Content Evidence/roles/relations are unchanged. Recipe claims are separate typed entities, not extra Content FACT requirements.

## Validation

- Collection: 428 tests.
- V1.9Q targeted (Recipe/import + migration + export): `uv run pytest tests/test_recipe_seed.py tests/test_recipe_migration.py tests/test_ai_export.py -q --tb=short` — 53 passed (212.80s), including two migration tests.
- Related regression: 169 collected tests in Knowledge/AI export/Project/import/calculation/backup/Prompt Bridge/seed modules pass within the full suite; historical canonical semantic tests also pass. No separate 169-test execution is claimed.
- Backend full: `uv run pytest -q --tb=short` — 428 passed (1633.58s). Initial fixture failures were corrected before this final full run.
- AI export: `uv run python -m app.ai_export write` and `uv run python -m app.ai_export check` — 301 files, current.
- Frontend: typecheck passed; lint passed; 14 files / 57 tests passed; build passed.
- Frontend commands: `npm.cmd run typecheck`, `npm.cmd run lint`, `npm.cmd run test`, `npm.cmd run build`.
- git diff --check: passed; staged diff is checked again before commit.
- Existing Starlette TestClient deprecation warning remains.

## DB safety

- Pre: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- Interim: same.
- Post: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191` — unchanged after all tests, confirmed 2026-09-11.
- Actual `backend/bdo.db` was not opened as the import/migration/export target. Do not restore any older hash.

## Documentation / non-goals

ADR-018, README, ARCHITECTURE, PRODUCT_DIRECTION, SEED_FORMAT, core data-model/tasks and the research note are synchronized with this foundation.

No frontend changes, Recipe personal-state UI, recipe calculator, N-craft/max-craftable/shortage logic, profit/price engine, full recipe catalog, Alchemy/Processing/House recipe expansion, Notion/MCP/OpenAI integration or runtime LLM dependency.

Push target: `origin/feature/v1.9q-cooking-recipe-foundation`. Final local/remote SHA and clean-tree verification are performed after the feature commit and reported in the delivery response; this report does not imply a main merge.
