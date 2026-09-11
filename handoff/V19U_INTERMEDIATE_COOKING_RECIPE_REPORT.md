# V1.9U — Intermediate Cooking Recipe & Skill Tier Expansion

## Baseline and delivery

- Base main: `073ca3f9c2907e9c5aa4351fa856f907802dfda8`
- Branch: `feature/v1.9u-intermediate-cooking-recipes`
- Implementation commit: included in `data: expand intermediate cooking recipe catalog`; resolve with `git log -1 --format=%H -- handoff/V19U_INTERMEDIATE_COOKING_RECIPE_REPORT.md`.
- Main merge: not performed.
- Research owner: ChatGPT.
- Codex role: supplied Research Packet implementation and repository-local validation only; no external research or unsupported game fact generation.

## Catalog expansion

Six verified Cooking Recipes were added:

- `grilled-sausage` — 구운 소시지, 요리 초급 6
- `steak` — 스테이크, 요리 견습 1
- `sute-tea` — 수테차, 요리 숙련 1
- `meat-sandwich` — 미트 샌드위치, 요리 견습 6
- `ham-sandwich` — 햄 샌드위치, 요리 숙련 1
- `frank-sandwich` — 프랭크 샌드위치, 요리 전문 1

The catalog now contains 15 active Recipes. The importer accepts the canonical
Cooking skill vocabulary `beginner`, `apprentice`, `skilled`,
`professional`, `artisan`, `master` and `guru`. Unsupported or
localized tier strings remain invalid.

## Canonical formulas

- Grilled Sausage: meat group 6 + onion 1 + salt 2 + pepper 2.
- Steak: meat group 8 + garlic 2 + red sauce 2 + salt 2.
- Sute Tea: tea with fine scent 2 OR tea with strong scent 1 + milk 3 + salt 1 + butter 2.
- Meat Sandwich: meat group 7 + soft bread 1 + vegetable group 6 + cheese 3.
- Ham Sandwich: grilled sausage 2 OR smoked sausage 1 + soft bread 2 + vegetable group 5 + egg 4.
- Frank Sandwich: grilled sausage 2 OR smoked sausage 1 + soft bread 1 + cabbage 2 + red sauce 1.

Every slot remains required and options inside a slot remain alternatives. No
global ingredient conversion, automatic option selection, output/proc model or
recursive sub-recipe calculation was introduced.

## Evidence boundary

- Fourteen supplied Sources and fourteen Materials were added.
- The official `cooking-guide` Source is used only for new Recipe
  `per_attempt` claims.
- `life-level-experience-guide` records skill-tier vocabulary research
  provenance but owns no Recipe claim Evidence.
- The unavailable Steak `/kr/recipe/591/` candidate was not used.
- Sute Tea's skill claim is owned only by `codex-sute-tea-117`.
- Formula, skill and quantity claims retain the exact source ownership supplied
  by the Research Packet.
- No `needs_review` claim was introduced.

The Research Packet estimated 203 Recipe Evidence rows. Expanding its exact
per-claim source sets yields 91 new rows (13 + 13 + 18 + 12 + 19 + 16), so the
verified repository total is 206 (115 + 91). No Source was added or removed to
force the estimate.

## Deliberate exclusions

V1.9U does not add:

- output quantities, special-result quantities or proc rates
- quality conversion or white-grade substitution
- global ingredient conversion ratios
- grain flour or dough IngredientGroups
- inventory, shortage, economics or profitability logic
- optimizer, automatic option selection or recursive sub-recipe expansion
- Recipe frontend UI

## Canonical counts

| Entity | Before | After |
| --- | ---: | ---: |
| Source | 199 | 213 |
| Content active | 294 | 294 |
| FACT | 280 | 280 |
| STRATEGY | 63 | 63 |
| MEASUREMENT | 11 | 11 |
| Relation | 521 | 521 |
| Material active | 64 | 78 |
| IngredientGroup active | 7 | 7 |
| GroupMember active | 35 | 35 |
| Recipe active | 9 | 15 |
| IngredientSlot active | 36 | 60 |
| IngredientOption active | 40 | 67 |
| Recipe claim definitions | 74 | 119 |
| Source-linked Recipe Evidence | 115 | 206 |
| Project | 1 | 1 |

All 15 Recipes and related Recipe Evidence are active and verified.

## Compatibility

- Existing Recipe read/search and stateless batch calculation contracts remain unchanged.
- Existing nine Recipe identities, DTO semantics and ordering remain unchanged.
- Existing Project, Content, Prompt Bridge, backup and AI export schema version 2 contracts remain compatible.
- No model, schema, migration, API contract or frontend feature was changed.
- Seed reimport remains idempotent and preserves stable IDs and existing user inventory history.

## Tests and validation

- New V1.9U semantic tests: `24 passed`.
- Targeted Recipe/knowledge/calculation/export regression: `131 passed`.
- Backend full: `484 passed`.
- Frontend typecheck: passed.
- Frontend lint: passed.
- Frontend tests: 14 files / 57 passed.
- Frontend build: passed.
- AI export check: schema version 2, Content 294 / Project 1 / Recipe 15, 312 files current.
- Existing Starlette TestClient/httpx deprecation warning: 1; no new warning introduced.
- `git diff --check`: passed.

## DB safety

- Pre SHA-256: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- Post SHA-256: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- Actual `backend/bdo.db` was not used for migration or seed import and was not modified.
