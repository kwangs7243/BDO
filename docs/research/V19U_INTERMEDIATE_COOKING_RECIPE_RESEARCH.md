# V1.9U Intermediate Cooking Recipe Research Packet

- Research owner: ChatGPT
- Research date: 2026-09-11
- Codex role: repository implementation only
- External research performed by Codex: none
- Region: KR

This document records the supplied implementation input for V1.9U. Codex did not
browse externally, alter the researched game facts, or add recipes beyond the
packet.

## Official skill-tier vocabulary

The Pearl Abyss Source `life-level-experience-guide` supports the current life
skill tier vocabulary:

| Canonical value | Korean |
| --- | --- |
| beginner | 초급 |
| apprentice | 견습 |
| skilled | 숙련 |
| professional | 전문 |
| artisan | 장인 |
| master | 명장 |
| guru | 도인 |

This Source establishes vocabulary only. It is not connected to any individual
Recipe formula, required-skill, per-option quantity, or per-attempt Evidence.

## Canonical recipes

All quantities are inputs for one cooking attempt. Slots are AND; alternatives
inside a slot are OR.

| Recipe | Required skill | One-attempt inputs |
| --- | --- | --- |
| Grilled Sausage | beginner 6 | meat group 6; onion 1; salt 2; pepper 2 |
| Steak | apprentice 1 | meat group 8; garlic 2; red-sauce 2; salt 2 |
| Sute Tea | skilled 1 | tea-with-fine-scent 2 OR tea-with-strong-scent 1; milk 3; salt 1; butter 2 |
| Meat Sandwich | apprentice 6 | meat group 7; soft-bread 1; vegetable group 6; cheese 3 |
| Ham Sandwich | skilled 1 | grilled-sausage 2 OR smoked-sausage 1; soft-bread 2; vegetable group 5; egg 4 |
| Frank Sandwich | professional 1 | grilled-sausage 2 OR smoked-sausage 1; soft-bread 1; cabbage 2; red-sauce 1 |

The six result identities plus onion, pepper, garlic, butter,
tea-with-strong-scent, soft-bread, cheese and smoked-sausage add 14 shared
Materials. Existing meat and vegetable groups are reused without membership
changes.

## Source classification and ownership

Fourteen new Sources are added: one Pearl Abyss `official_guide` for tier
vocabulary and thirteen `third_party_database` Recipe Sources. The existing
`inven-cooking-recipe-db` is reused for Meat Sandwich and Ham Sandwich. The
existing `cooking-guide` is connected only to the six `per_attempt` claims.

Each Recipe formula, skill and quantity uses exactly the Source set supplied in
the V1.9U Research Packet. In particular:

- the conflicting BDO Codex `/kr/recipe/591/` Steak page is neither cataloged
  nor used as Evidence;
- `recipe.sute-tea.skill` is owned only by `codex-sute-tea-117`;
- `codex-sute-tea-special-560` supports the strong-tea alternative and common
  quantities, not the base Recipe skill;
- `weingchicken-healthy-sute-tea-222` supports the two tea alternatives and
  common quantities, not the base Recipe skill;
- smoked-sausage and tea-with-strong-scent are Material identities only where
  they are explicit Recipe input alternatives.

The packet estimated 203 total Source-linked Recipe Evidence rows. Applying its
exact source sets to the importer rule of one Evidence row per Source ID yields
91 new rows, so the actual verified total is 206 (115 + 91). No Source was
removed or added to force the estimate.

## Explicit exclusions

No canonical model or calculation is added for:

- result quantity, special-result probability, cooking proc, mastery or mass
  cooking output;
- global quality, special-food, green-to-white or normal-to-special conversion;
- automatic option selection, mixed substitution, or IngredientGroup member
  selection;
- recursive Recipe/DAG expansion or automatic sub-recipe attempt derivation;
- inventory-aware calculation, cost, price, profit or imperial profitability.

Grain-flour and grain-dough IngredientGroups are also excluded. The supplied
research notes that the official current substitution list defines grain itself
but does not directly establish those derived groups under the same semantics.
They remain deferred until a separate Research Packet.
