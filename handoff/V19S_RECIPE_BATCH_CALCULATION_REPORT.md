# V1.9S — Stateless Recipe Batch Calculation Interface

## Baseline and delivery

- Base main: `38bbf8d38a81a01ca0b016946334fa9d9a59addf`
- Branch: `feature/v1.9s-recipe-batch-calculation`
- Implementation commit: included in `feat: add stateless recipe batch calculation`; resolve with `git log -1 --format=%H -- handoff/V19S_RECIPE_BATCH_CALCULATION_REPORT.md`.
- Delivery verification: local/remote branch SHA equality and clean working tree are checked after the single implementation commit and recorded in the delivery response.
- Main merge: not performed.

## API contract

```http
POST /api/calculations/recipes/{slug}
Content-Type: application/json

{"attempt_count": 100}
```

- `attempt_count` is a strict integer greater than or equal to 1.
- Float, numeric string, bool, zero, negative values and extra fields return FastAPI/Pydantic `422`.
- Unknown or inactive Recipe returns `404` with `Recipe not found`.
- Response includes Recipe/result identity, skill, verification metadata and ordered slot/option identities.
- Each option distinguishes `per_attempt_quantity` from `total_required_quantity`.
- Numeric database IDs and full Evidence lists are not exposed. Evidence remains available from `GET /api/knowledge/recipes/{slug}`.

## Calculation semantics

The only formula is:

```text
total_required_quantity = per_attempt_quantity * attempt_count
```

`per_attempt_quantity` comes from canonical `RecipeIngredientOption.required_quantity`. `recipe_calculations.scale_recipe_requirements` is a pure deterministic transformation of `KnowledgeRecipeOut`; `calculate_recipe` only resolves the canonical DTO through `get_knowledge_recipe`.

### AND / OR and IngredientGroup preservation

- Recipe slots remain AND.
- Options within one slot remain OR.
- Every alternative is returned in canonical order and scaled independently.
- Alternatives are not selected, added, mixed, merged or optimized.
- IngredientGroup remains the option target. Current members are projected for reference without member-level required quantities or automatic member selection.

Beer 100 attempts therefore returns mineral water 600 and purified water 300 as two alternatives, not 900 as one requirement. Grilled bird meat preserves deep-frying oil and cottonseed oil as separate alternatives.

## State and compatibility boundary

- Personal-state independence: no `UserMaterialInventory` or other user-state read/write.
- Database mutation: none.
- Inventory fallback and shortage calculation: none.
- Result/output quantity, cooking proc, quality conversion, profitability and optimizer: not implemented.
- Existing Project calculation semantics: unchanged.
- Knowledge Content/Project/Recipe, search, PromptContextBundle and backup version 1: unchanged.
- Frontend feature/UI change: none.

## Schema and canonical data

- Schema change: none.
- Migration: none.
- Seed/Source/Evidence change: none.
- Recipe structure or value change: none.

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
| Recipe claim definitions | 34 |
| Source-linked Recipe Evidence | 44 verified / 0 needs_review |
| Project | 1 |

## Tests and validation

- New V1.9S semantic tests: `22 passed`.
- Targeted Recipe/calculation/knowledge/Project/export regression: `120 passed`.
- Backend full: `451 passed`.
- Frontend typecheck: passed.
- Frontend lint: passed.
- Frontend tests: 14 files / 57 passed.
- Frontend build: passed.
- AI export check: schema version 2, Content 294 / Project 1 / Recipe 4, 301 files current.
- Existing Starlette TestClient deprecation warning: 1; no new warning introduced.
- `git diff --check`: passed.

## DB safety

- Pre SHA-256: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- Post SHA-256: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- Actual `backend/bdo.db` was not used for migration, seed import, export generation or calculation tests.
