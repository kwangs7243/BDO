# V1.9W Material Knowledge Read Surface Report

## Git baseline

- Base main: `91c387d76ad5173daaccdcd01731ade33dceb620`
- Branch: `feature/v1.9w-material-knowledge-read`
- Implementation commit: `feat: add material knowledge read surface`
- Research owner: ChatGPT
- External game research: none
- Codex external research: none

## Implemented

- Added `GET /api/knowledge/materials/{key}` with active-only lookup and the
  stable 404 detail `Material not found`.
- Added `KnowledgeMaterialOut` and typed relation DTOs without numeric DB IDs
  or a fabricated Material-level verification status.
- Added Material `name_ko` and `key` as first-class search identities.
  Material exact identity sorts before nested Content, Project, and Recipe
  matches; unit is not searchable.
- Reused canonical Recipe, IngredientGroup Evidence, and Project projections.
  No relationship rows are persisted.

## Relation semantics and counts

| Projection | Count |
| --- | ---: |
| Active Material resources | 78 |
| Producer Recipe links | 15 |
| Explicit Recipe usage links | 51 |
| IngredientGroup memberships | 35 |
| Group candidate Recipe usages | 99 |
| Project requirement links | 9 |
| Scoped ProjectMaterialSource rows | 9 |

Recipe verification stays with Recipe relationships, IngredientGroup
verification and sources stay with memberships/candidate usages, and
ProjectMaterialSource remains nested below its Project requirement. Group
candidate usage is explicitly labeled `ingredient_group_candidate`; its
quantity belongs to the Recipe group option and is not a Material conversion.

The red-sauce, beef, mineral-water, smoked-sausage, and moon-vein-flax cases
are covered by semantic regressions. All 78 active Materials are projectable.

## Personal state and compatibility

- No UserMaterialInventory or other personal state is read by Material
  knowledge.
- GET, search, and export do not mutate canonical or personal tables.
- V1.9V direct Recipe dependency semantics remain a separate read projection;
  the existing six edges are unchanged.
- No seed, Source/Evidence, schema, migration, PromptContextBundle, frontend
  source, recursive graph, output/yield, market/economy, or optimizer change.

## AI export

- Manifest schema: 3
- Content pages: 294
- Project pages: 1
- Recipe pages: 15
- Material pages: 78
- Total files: 390

Each Material Markdown page contains Identity, Produced By Recipes, Explicit
Recipe Usages, Ingredient Group Memberships, Ingredient Group Candidate Recipe
Usages, Project Requirements, and Semantics. Recipe, Project, and exported
Content references use stable relative links.

## Validation

- V1.9W Material semantic tests: 10 passed
- Targeted backend regressions: 113 passed
- Backend full: 505 passed, with one existing Starlette deprecation warning
- Frontend typecheck: passed
- Frontend lint: passed
- Frontend tests: 14 files / 57 passed
- Frontend build: passed
- AI export write/check: passed, 390 files
- `git diff --check`: passed
- DB SHA before: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- DB SHA after: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- DB unchanged: yes

The actual `backend/bdo.db` is not an export/import source and must remain
unchanged.
