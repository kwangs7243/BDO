# V1.9X Alchemy Recipe Foundation Report

- Date: 2026-09-12
- Region: KR
- Branch: `feature/v1.9x-alchemy-recipe-foundation`
- Source of Truth baseline: `main` at
  `437636e3a12de6e267db34161eafd07eb666e0d9`
- Research owner: ChatGPT
- Implementation owner: Codex
- External web research: not performed

## Result

The existing formulation-style Recipe pipeline now supports `cooking` and
`alchemy` without a schema or migration change. Four verified Alchemy
Recipes and thirteen shared Materials were added. Existing canonical read,
search, stateless calculation, direct dependency, Material knowledge, and AI
export services consume the new process type.

Added Recipes:

- `clear-liquid-reagent` — 맑은 액체 시약
- `pure-powder-reagent` — 순수한 가루 시약
- `defense-elixir` — 방어의 비약
- `concentration-elixir` — 집중의 비약

## Canonical baseline

| Domain | Before | After | Change |
| --- | ---: | ---: | ---: |
| Source | 213 | 220 | +7 |
| Content | 294 | 294 | 0 |
| FACT / STRATEGY / MEASUREMENT | 280 / 63 / 11 | 280 / 63 / 11 | 0 |
| Content Relation | 521 | 521 | 0 |
| Material | 78 | 91 | +13 |
| IngredientGroup / member | 7 / 35 | 7 / 35 | 0 |
| Recipe | 15 | 19 | +4 |
| Recipe slot / option | 60 / 67 | 76 / 87 | +16 / +20 |
| Recipe claim definitions | 119 | 151 | +32 |
| Recipe Evidence rows | 206 | 292 | +86 |
| Recipe needs_review | 0 | 0 | 0 |
| Direct dependency edges | 6 | 8 | +2 |
| Material producer links | 15 | 19 | +4 |
| Material explicit usages | 51 | 71 | +20 |
| Group membership / candidate usages | 35 / 99 | 35 / 99 | 0 |
| Project requirements | 9 | 9 | 0 |
| AI export files | 390 | 407 | +17 |

All 294 Content rows remain active. AI export manifest schema remains version
3 and contains 294 Content, one Project, 19 Recipe, and 91 Material resources.

## Source identity deviation

The initial packet treated both official Alchemy guides as new. Repository
audit found that `alchemy-basic-guide` (Wiki 99) and `alchemy-guide`
(Wiki 100) already existed before V1.9X and were referenced by historical
Content Evidence.

V1.9X reuses and refreshes both stable official Source identities. The
tracking-parameter alias `alchemy-advanced-guide` was removed, all new BDO
Codex URLs were normalized without tracking parameters, and only seven BDO
Codex Sources are new. The canonical result is 220 unique Source IDs and 220
unique canonical URLs.

## Evidence boundaries

- `alchemy-basic-guide` owns full-formulation and one-attempt semantics only,
  not individual exact formulas.
- `alchemy-guide` owns the packet-approved formulas and selected
  alternatives for Clear Liquid Reagent, Defense Elixir, and Concentration
  Elixir.
- For Pure Powder Reagent, `alchemy-guide` owns only
  `required_skill`. It is excluded from the `ingredients` claim and every
  `required_quantity` claim because the packet identifies its exact formula
  row as conflicting.
- BDO Codex and the existing Inven Recipe DB own only their packet-assigned
  formula, skill, and option quantity claims.
- Wild grass and weed are Recipe-local OR options. No herb, blood, sap,
  mushroom, or alchemy-water IngredientGroup was created.
- Pig blood and bear blood remain exact explicit inputs; no blood
  substitution was inferred.

## API and derived surfaces

- `GET /api/knowledge/recipes/{slug}` returns Alchemy Recipes with
  `process_type="alchemy"`.
- `POST /api/calculations/recipes/{slug}` returns `process_type` and scales
  every option independently from the canonical full one-attempt quantity.
- Dependency edges expose `producer_process_type` and
  `consumer_process_type`.
- Two direct edges are derived:
  `clear-liquid-reagent -> defense-elixir` and
  `clear-liquid-reagent -> concentration-elixir`.
- Material knowledge derives Alchemy producers and explicit usages without
  persisted duplicate relations or personal inventory.
- Search keeps resource type `recipe` and uses category `alchemy`; exact
  Material identity ranks before the same-named Recipe.
- Recipe AI export headings and one-attempt wording are process-neutral.
  Alchemy pages explicitly state the unmodeled reduced-input, output,
  special-result, and mastery boundaries.

## Compatibility and exclusions

The legacy `COOKING_SKILL_TIERS` import remains available while the importer
uses the shared `RECIPE_SKILL_TIERS` vocabulary. Existing Cooking DTOs,
formulas, evidence, calculations, search, dependencies, and exports remain
supported.

Not implemented:

- Processing, simple alchemy/cooking, heating, grinding, shaking,
  manufacturing, or imperial alchemy Recipe types
- reduced-input probabilistic success
- result/output quantity, proc or special-result probability
- Alchemy level/mastery output effects
- global blood/herb/material substitution
- recursive production planning
- profitability, market/economy, or optimizer logic
- personal inventory integration
- frontend feature or redesign
- schema, migration, Project seed, Content seed, or PromptContextBundle change

## Tests and validation

- V1.9X focused semantic:
  `14 passed`
- Related Recipe/Material/Evidence/export regression:
  `95 passed`
- Backend full:
  `519 passed, 1 existing Starlette deprecation warning`
- Frontend typecheck: passed
- Frontend lint: passed
- Frontend tests: `14 files / 57 passed`
- Frontend build: passed
- AI export write: `407 files`
- AI export freshness: passed
- Source IDs / URLs: `220 / 220 unique`

The V1.9X tests cover exact formulas and skill tiers, explicit OR semantics,
Pure Powder Source exclusion, no blood substitution, process-aware read,
search, export, ten-attempt stateless calculations, two new dependency edges,
Material projections, unsupported process rejection, personal-state
independence, read-only behavior, existing Cooking compatibility, and
double-reimport stable numeric IDs.

## Database integrity

- Before SHA-256:
  `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- After SHA-256:
  `7B8FDD06902A2C1FB8FF9003E6904788BC4822EA23728A67D0D43A87266AD191`
- Result: unchanged

All imports and reimports used isolated in-memory test databases. The actual
`backend/bdo.db` was not migrated or seeded.
