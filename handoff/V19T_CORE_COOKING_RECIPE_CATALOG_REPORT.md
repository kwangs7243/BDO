# V1.9T — Core Cooking Recipe Catalog Expansion

## Baseline and delivery

- Base main: `9b745f31ba20958210154f5bc242cbde359ce933`
- Branch: `feature/v1.9t-core-cooking-recipe-catalog`
- Implementation commit: included in `data: expand core cooking recipe catalog`; resolve with `git log -1 --format=%H -- handoff/V19T_CORE_COOKING_RECIPE_CATALOG_REPORT.md`.
- Main merge: not performed.
- Research owner: ChatGPT.
- Codex role: supplied Research Packet implementation and repository-local validation only; no external research or unsupported game fact generation.

## Catalog expansion

Five verified Cooking Recipes were added:

- `dressing` — 드레싱, 요리 초급 1
- `red-sauce` — 레드소스, 요리 초급 1
- `white-sauce` — 화이트소스, 요리 초급 1
- `tea-with-fine-scent` — 향이 좋은 차, 요리 견습 1
- `omelet` — 오믈렛, 요리 견습 1

The catalog now contains 9 active Recipes. Existing beer, vinegar, pickled vegetables and grilled bird meat identities and semantics remain unchanged.

## Canonical formulas

- Dressing: egg 1 + olive oil 1 + water group 1 + salt 2.
- Red Sauce: base sauce 1 + meat group 1 + mineral water 2 OR purified water 1 + sugar 2.
- White Sauce: base sauce 1 + fruit group 1 + milk 1 + cooking wine 2.
- Tea with Fine Scent: flower group 4 + fruit group 4 + mineral water 7 OR purified water 3 + edible honey 3.
- Omelet: grain group 5 + olive oil 2 + egg 5 + salt 2.

Recipe slots retain AND semantics, while options within a slot retain OR semantics. The Red Sauce and Tea water alternatives are separate Material options because their quantities differ. No global water conversion ratio was introduced.

## Ingredient groups

Three groups were added:

- `meat`: deer, sheep, fox, rhino, pork, beef, raccoon, weasel, bear and wolf meat.
- `flower`: rose, tulip and sunflower.
- `water`: mineral water and purified water.

Group membership is reference metadata only. It does not define a global quantity conversion and does not authorize automatic member selection.

## Evidence boundary

- Eight third-party database Sources were added with the stable IDs and URLs supplied by the Research Packet.
- The official `cooking-guide` Source is used only for new IngredientGroup membership and Recipe `per_attempt` semantics.
- Exact formula, skill and quantity claims do not use the official guide when the guide does not establish those values.
- Red Sauce purified-water quantity is owned only by `codex-red-sauce-purified-546`.
- Tea purified-water quantity is owned only by `weingchicken-tea-with-fine-scent-218`.
- All 74 Recipe-domain claim definitions have verified Source-linked Evidence; no `needs_review` claim was introduced.

## Deliberate exclusions

V1.9T does not add:

- a complete Cooking catalog
- result/output quantities or proc rates
- quality or white-grade conversion
- global ingredient conversion ratios
- inventory, shortage, economics or profitability logic
- optimizer, automatic option selection or recursive sub-recipe expansion
- Recipe frontend UI

## Canonical counts

| Entity | Before | After |
| --- | ---: | ---: |
| Source | 191 | 199 |
| Content active | 294 | 294 |
| FACT | 280 | 280 |
| STRATEGY | 63 | 63 |
| MEASUREMENT | 11 | 11 |
| Relation | 521 | 521 |
| Material active | 41 | 64 |
| IngredientGroup active | 4 | 7 |
| GroupMember active | 20 | 35 |
| Recipe active | 4 | 9 |
| IngredientSlot active | 16 | 36 |
| IngredientOption active | 18 | 40 |
| Recipe claim definitions | 34 | 74 |
| Source-linked Recipe Evidence | 44 | 115 |
| Project | 1 | 1 |

All 9 Recipes and all related Recipe Evidence are active and verified.

## Compatibility

- Existing Recipe read/search and stateless batch calculation contracts remain unchanged.
- AND/OR ordering and stable string identities remain unchanged.
- Existing Project, Content, Prompt Bridge, AI export schema version 2 and backup contracts remain compatible.
- Application code, frontend code, schema and migrations were not changed.
- Seed reimport remains idempotent and preserves stable IDs and existing user inventory history.

## Tests and validation

- New V1.9T semantic tests: `9 passed`.
- Targeted Recipe/knowledge/calculation/export regression: `107 passed`.
- Backend full: `460 passed`.
- Frontend typecheck: passed.
- Frontend lint: passed.
- Frontend tests: 14 files / 57 passed.
- Frontend build: passed.
- AI export check: schema version 2, Content 294 / Project 1 / Recipe 9, 306 files current.
- Existing Starlette TestClient/httpx deprecation warning: 1; no new warning introduced.
- `git diff --check`: passed.

## DB safety

- Pre SHA-256: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- Post SHA-256: `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- Actual `backend/bdo.db` was not used for migration or seed import and was not modified.
