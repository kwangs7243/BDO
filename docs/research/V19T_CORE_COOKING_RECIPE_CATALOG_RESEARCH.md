# V1.9T Core Cooking Recipe Catalog Research Packet

- Research owner: ChatGPT
- Research date: 2026-09-11
- Codex role: repository implementation only
- External research performed by Codex: none
- Region: KR

This document records the implementation input supplied for V1.9T. Codex did not
independently browse, replace, or extend the game facts in this packet.

## Source classification

The existing Pearl Abyss cooking-guide remains the official current source for:

- one-cooking-attempt input semantics;
- membership of the meat, flower, and water substitution groups;
- the fact that different substitutes may require Recipe-specific quantities.

It is not used as evidence for a new Recipe's exact formula, skill requirement,
or exact option quantity.

The eight new Sources are all third_party_database, have published_at = null,
retrieved_at = 2026-09-11T13:02:00+09:00, and region = KR.

| Source ID | Publisher | URL | Scope |
| --- | --- | --- | --- |
| weingchicken-dressing-56 | 위잉치킨 | https://apps.weingchicken.com/bd/makings/56 | Dressing formula, skill, quantities, including water 1/1 |
| codex-red-sauce-9004 | BDO Codex | https://bdocodex.com/kr/item/9004/ | Red Sauce base formula and beginner 1 |
| codex-red-sauce-purified-546 | BDO Codex | https://bdocodex.com/kr/recipe/546/?sl=1 | Red Sauce purified-water quantity 1 |
| weingchicken-white-sauce-152 | 위잉치킨 | https://apps.weingchicken.com/bd/makings/152 | White Sauce formula and beginner 1 |
| codex-tea-with-fine-scent-9270 | BDO Codex | https://bdocodex.com/kr/item/9270/ | Tea base formula and apprentice 1 |
| weingchicken-tea-with-fine-scent-218 | 위잉치킨 | https://apps.weingchicken.com/bd/makings/218 | Tea formula, apprentice 1, and water 7/3 |
| weingchicken-omelet-335 | 위잉치킨 | https://apps.weingchicken.com/bd/makings/335 | Omelet formula and apprentice 1 |
| inven-cooking-recipe-db | 검은사막 인벤 | https://black.inven.co.kr/dataninfo/recipe/?nsrc=r | Independent basic-formula and group cross-check for all five Recipes |

The Inven Source does not own the Recipe-specific purified-water values. Those
remain connected only to their explicit Sources.

## Canonical formulas

All quantities are inputs for one cooking attempt. Slots are AND and alternatives
inside one slot are OR.

| Recipe | Skill | One-attempt inputs |
| --- | --- | --- |
| Dressing | beginner 1 | egg 1; olive-oil 1; water group 1; salt 2 |
| Red Sauce | beginner 1 | base-sauce 1; meat group 1; mineral-water 2 OR purified-water 1; sugar 2 |
| White Sauce | beginner 1 | base-sauce 1; fruit group 1; milk 1; cooking-wine 2 |
| Tea With Fine Scent | apprentice 1 | flower group 4; fruit group 4; mineral-water 7 OR purified-water 3; edible-honey 3 |
| Omelet | apprentice 1 | grain group 5; olive-oil 2; egg 5; salt 2 |

### Water quantity differences

- Dressing: mineral-water 1 / purified-water 1, represented by water group quantity 1.
- Red Sauce: mineral-water 2 / purified-water 1, represented as two Material options.
- Tea With Fine Scent: mineral-water 7 / purified-water 3, represented as two Material options.

The unequal pairs are not collapsed into the water group and do not define a
global conversion ratio.

## Ingredient groups

- meat: deer, sheep, fox, rhino, pork, beef, raccoon, weasel, bear, wolf meat.
- flower: rose, tulip, sunflower.
- water: mineral water, purified water.

Membership is sourced from the official current cooking guide. It describes
which Materials belong to a substitution group, not a universal quantity
multiplier. Existing grain and fruit groups are reused by Omelet and White
Sauce/Tea respectively.

## Evidence ownership

- cooking-guide connects only to the three new group membership claims and
  each new Recipe's per_attempt claim.
- Formula, skill, and exact option quantities connect only to the Source sets
  specified by the Research Packet.
- Red Sauce purified-water quantity 1 connects only to
  codex-red-sauce-purified-546.
- Tea With Fine Scent purified-water quantity 3 connects only to
  weingchicken-tea-with-fine-scent-218.
- The existing four Recipe definitions and their provenance remain unchanged.

## Deliberately excluded facts

V1.9T does not canonicalize or calculate:

- result quantity or 1-4 output behavior;
- special cooking proc probability or special-result probability;
- mastery or mass-cooking output;
- quality conversion or mixed substitution;
- market/NPC price, cost, margin, profit, or silver per hour;
- inventory, shortage, automatic option/member choice, or cheapest option;
- recursive Recipe dependencies.

The V1.9S calculator remains a deterministic multiplier over each canonical
option and does not resolve alternatives.
