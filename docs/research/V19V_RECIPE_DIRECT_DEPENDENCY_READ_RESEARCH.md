# V1.9V Recipe Direct Dependency Read Research

- Research owner: ChatGPT
- Research date: 2026-09-11
- External game research required: none
- Codex external research: none
- Region: KR

This milestone derives a read model from the V1.9U canonical Recipe and shared
Material identities. Not performing external research is intentional: no new
game fact, Source, Evidence or seed value is introduced.

## Canonical baseline

- Source 213
- Content 294: FACT 280 / STRATEGY 63 / MEASUREMENT 11
- Relation 521
- Material 78
- IngredientGroup 7 / GroupMember 35
- Recipe 15 / IngredientSlot 60 / IngredientOption 67
- Recipe claims 119 / Recipe Evidence 206 / needs_review 0
- Project 1

All counts remain unchanged because dependency edges are not database entities.

## Derivation rule

A direct edge exists only when:

```text
producer Recipe.result_material_key
==
consumer explicit Material option.material_key
```

Stable Material key equality is the complete identity rule. Labels, Korean
names, similar names and group membership do not participate. The pure builder
loads active canonical Recipe DTOs, indexes producers by result Material, walks
consumer slots/options and emits deterministic upstream/downstream projections.
No relation row, dependency table or dependency seed is maintained.

## Current exact direct graph

| Producer | Consumer | Material | Quantity | Alternative |
| --- | --- | --- | ---: | --- |
| vinegar | pickled-vegetables | vinegar | 4 | false |
| red-sauce | steak | red-sauce | 2 | false |
| red-sauce | frank-sandwich | red-sauce | 1 | false |
| tea-with-fine-scent | sute-tea | tea-with-fine-scent | 2 | true |
| grilled-sausage | ham-sandwich | grilled-sausage | 2 | true |
| grilled-sausage | frank-sandwich | grilled-sausage | 2 | true |

`is_alternative` is true when the consumer slot has more than one active
option. It describes the consumer option's OR status; it does not select or
combine options.

## Exclusion boundaries

- IngredientGroup options create no edge and members are not expanded.
- `smoked-sausage` and `tea-with-strong-scent` have no canonical producer
  Recipe, so no producer is fabricated for them.
- Only direct edges are returned. Grandparents, transitive closure, raw-material
  flattening and recursive quantities are excluded.
- Result/output quantity is not modeled, so producer attempt counts and yield
  are not inferred.
- Personal inventory, shortage, price, cost, profit and other user state are
  neither input nor output.
- Existing Recipe batch calculation semantics remain unchanged.

## API projection

`GET /api/knowledge/recipes/{slug}/dependencies` returns Recipe/result identity
plus ordered `direct_upstream` and `direct_downstream` edge lists. Each edge
includes stable producer/consumer/Material/slot/option identities, consumer
quantity and order, aggregate producer/consumer verification status, and the OR
alternative flag. Numeric database IDs are excluded. An unknown or inactive
Recipe returns `404 Recipe not found`.

## AI export projection

All 15 generated Recipe Markdown pages gain a Direct Recipe Dependencies
section. It records upstream/downstream edges and relative Recipe paths while
stating the Material-only, direct-only, no-recursion and no-yield semantics.
Manifest schema version 2, manifest fields, Recipe count and total file count
remain unchanged.

## Evidence decision

No Source, claim or Evidence row is added. Each edge is a deterministic
projection of canonical identities that already carry Recipe-level
verification. The response exposes producer and consumer aggregate verification
status rather than duplicating Evidence ownership on a derived edge.
