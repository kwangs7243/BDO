# V1.9X Alchemy Recipe Foundation Research

- Research owner: ChatGPT
- Research date: 2026-09-12
- Implementation owner: Codex
- Region: KR
- Source boundary: supplied V1.9X Research Packet only; Codex performed no web research

## Decision boundary

V1.9X reuses the existing formulation-style Recipe pipeline for `cooking`
and `alchemy`. A Recipe is the canonical full-input formulation for one
attempt. Ingredient slots are AND and options in the same slot are OR.

Alchemy `required_quantity` is not a minimum reduced-input quantity that may
succeed probabilistically. The milestone does not model reduced-input success,
output quantity, special-result probability, level/mastery output effects,
profitability, optimization, recursive production planning, personal
inventory, or a frontend feature.

Processing remains a separate future domain. The packet supplied the official
Processing guide reference
<https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=98&utm_source=chatgpt.com>
only to document why method, knowledge-condition, mass-processing,
success-probability, and result-quantity semantics must not be forced into the
current Recipe contract. It is not imported as V1.9X Recipe Evidence.

## Source ownership

| Source | Authority in V1.9X |
| --- | --- |
| `alchemy-basic-guide` | Full-formulation, one-attempt/continuous-production, underfilled failure possibility and variable output semantics; never an individual exact formula |
| `alchemy-advanced-guide` | Alchemy similarity, beginner skill vocabulary, Clear Liquid Reagent, Defense Elixir, Concentration Elixir and selected alternatives |
| BDO Codex Recipe pages | Exact named formula, skill and option quantity only where the packet assigns ownership |
| `inven-cooking-recipe-db` | Exact displayed formula cross-check; not skill or undocumented substitution authority |
| `life-level-experience-guide` | Existing general skill-tier vocabulary provenance; not attached to individual Recipe claims |

The packet called `alchemy-basic-guide` one of nine new Sources, but that
stable ID and official URL already existed and were referenced by Content
Evidence. V1.9X preserves and refreshes that identity instead of inserting a
duplicate or rewriting historical Evidence. Therefore eight Source rows are
new and the actual Source total is 221 rather than the packet's arithmetic
target of 222.

### Pure Powder conflict boundary

The packet identifies the official advanced guide's Pure Powder row as
conflicting with independent recipe databases. Therefore
`alchemy-advanced-guide` owns only the Pure Powder `required_skill` claim.
It owns neither the Recipe `ingredients` claim nor any Pure Powder
`required_quantity` claim. No convenient value is promoted from the
conflicting row.

## Canonical Recipes

| Recipe | Skill | Full formulation for one attempt |
| --- | --- | --- |
| Clear Liquid Reagent | beginner 1 | purified water 1 OR distilled water 1; salt 1; dawn herb 1; wild grass 1 OR weed 1 |
| Pure Powder Reagent | beginner 1 | purified water 1; sugar 1; silver azalea 1; wild grass 1 OR weed 1 |
| Defense Elixir | beginner 1 | clear liquid reagent 1; ash sap 6; pig blood 5; purified water 3 |
| Concentration Elixir | beginner 1 | clear liquid reagent 1; cloud mushroom 3; bear blood 3; wild grass 2 OR weed 8 |

Wild grass and weed alternatives are explicit Recipe-local options. No global
herb, blood, sap, mushroom, or alchemy-water IngredientGroup is introduced.
Pig blood and bear blood remain exact inputs; no undocumented blood
substitution is inferred.

## Evidence ownership counts

| Recipe | Claim definitions | Evidence rows |
| --- | ---: | ---: |
| Clear Liquid Reagent | 9 | 26 |
| Pure Powder Reagent | 8 | 19 |
| Defense Elixir | 7 | 17 |
| Concentration Elixir | 8 | 24 |
| Total added | 32 | 86 |

All 32 new claims are verified from the packet-assigned Sources. V1.9X adds no
`needs_review`, `conflict`, or `superseded` Recipe Evidence row; the Pure
Powder conflict is handled by excluding the conflicting Source from exact
claims.

## Derived integration

- Stateless Recipe calculation scales every option independently and returns
  `process_type`.
- Direct dependency projection adds
  `clear-liquid-reagent -> defense-elixir` and
  `clear-liquid-reagent -> concentration-elixir`, both
  `alchemy -> alchemy`.
- Material knowledge derives four new producer links and twenty explicit
  usages from the canonical Recipes. Existing group and Project projections
  remain unchanged.
- Search continues to use resource type `recipe` with category `alchemy`;
  exact Material identity ranks before the same-named Recipe.
- AI exports remain schema version 3 and include process type on Recipe and
  dependency data. Alchemy pages state the full-formulation and unmodeled
  probability/output/mastery boundaries.

## Expected canonical counts

| Domain | V1.9W | V1.9X |
| --- | ---: | ---: |
| Source | 213 | 221 |
| Content | 294 | 294 |
| Material | 78 | 91 |
| IngredientGroup / member | 7 / 35 | 7 / 35 |
| Recipe | 15 | 19 |
| Slot / option | 60 / 67 | 76 / 87 |
| Recipe claim definitions | 119 | 151 |
| Recipe Evidence rows | 206 | 292 |
| Direct dependency edges | 6 | 8 |
| Material producer links | 15 | 19 |
| Material explicit usages | 51 | 71 |
| Group candidate usages | 99 | 99 |
| Project requirements | 9 | 9 |
| AI export files | 390 | 407 |

Content knowledge roles remain FACT 280 / STRATEGY 63 / MEASUREMENT 11 and
Content Relation remains 521. Schema, migration, Project seed, Content seed,
frontend, PromptContextBundle, and personal-state ownership are unchanged.
