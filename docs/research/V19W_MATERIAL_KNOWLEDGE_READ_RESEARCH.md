# V1.9W Material Knowledge Read Surface - Repository Audit

- Research owner: ChatGPT
- Research date: 2026-09-12
- External game research required: none
- Codex external research: none

## Purpose

Material is already the shared stable identity used by Recipe results,
explicit Recipe ingredient options, IngredientGroup members, and
ProjectMaterial requirements. Before V1.9W it had no first-class canonical
read endpoint, search result, or static AI export page. Consumers therefore
had to discover one Material indirectly through several resource types.

V1.9W adds one derived cross-domain projection. It does not add or change game
facts and does not persist duplicate relationship rows.

## Canonical ownership

`seed_materials.json` continues to own Material `key`, `name_ko`, `unit`,
and `active`. Recipe, IngredientGroup, and Project remain the owners of their
respective relationships. Material identity has no independent claim-level
Evidence, so the Material response has no invented aggregate verification
status.

## Five relation categories

1. Producer: active Recipe rows whose result Material key matches.
2. Explicit usage: active Recipe options that directly target the Material.
3. Group membership: active IngredientGroupMember rows with the group's
   existing Evidence and verification.
4. Group candidate usage: a group membership joined to active Recipe group
   options. This is an allowed candidate, not an explicit Material
   requirement; the quantity belongs to the group option.
5. Project requirement: active ProjectMaterial rows. ProjectMaterialSource
   stays nested under that Project requirement and is not a global acquisition
   catalog.

All projections exclude UserMaterialInventory and every other personal-state
table.

## Current derived counts

| Projection | Count |
| --- | ---: |
| Active Material resources | 78 |
| Producer Recipe links | 15 |
| Explicit Recipe usage links | 51 |
| IngredientGroup memberships | 35 |
| Group candidate Recipe usages | 99 |
| Project requirement links | 9 |
| Scoped ProjectMaterialSource rows | 9 |

The counts are derived from the current seed in an isolated database; no rows
were added to reach them.

## Representative cases

- `red-sauce`: produced by the red-sauce Recipe and explicitly used by steak
  (2) and frank-sandwich (1).
- `beef`: no producer or explicit usage; member of `meat` and therefore an
  allowed group candidate in red-sauce, grilled-sausage, steak, and
  meat-sandwich.
- `mineral-water`: explicit alternative in beer, red-sauce, and
  tea-with-fine-scent; also a `water` member and candidate for dressing's
  group option.
- `smoked-sausage`: explicit alternative in ham-sandwich and
  frank-sandwich, with no fabricated producer.
- `moon-vein-flax`: Carrack project requirement of 180 at the body-materials
  stage. Its two acquisition sources remain scoped to that requirement.

## AI export decision

Manifest schema version 3 preserves all Content, Project, and Recipe fields and
adds 78 Material entries. The generated tree contains 294 Content pages, one
Project page, 15 Recipe pages, 78 Material pages, INDEX, and manifest: 390
files total. Material pages keep explicit usage separate from group-candidate
usage and include stable relative links only.

No recursive graph, output/yield, market price, profitability, optimizer,
global acquisition catalog, frontend Material UI, or external adapter is part
of this milestone.
