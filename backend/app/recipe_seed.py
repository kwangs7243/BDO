"""Validate and synchronize formulation Recipes without touching personal state."""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, FiniteFloat, StrictInt, field_validator, model_validator
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import (Evidence, IngredientGroup, IngredientGroupMember, Material,
                        Recipe, RecipeIngredientSlot, RecipeIngredientOption, Source)


SUPPORTED_RECIPE_PROCESS_TYPES = {"cooking", "alchemy"}

RECIPE_SKILL_TIERS = {
    "beginner",
    "apprentice",
    "skilled",
    "professional",
    "artisan",
    "master",
    "guru",
}

# Backward-compatible import for V1.9U callers; both processes share the same tiers.
COOKING_SKILL_TIERS = RECIPE_SKILL_TIERS


class SeedRow(BaseModel):
    model_config = ConfigDict(extra="forbid")


class EvidenceSeed(SeedRow):
    seed_key: str = Field(min_length=1, max_length=185)
    entity_type: str
    entity_seed_key: str = Field(min_length=1, max_length=128)
    claim_key: str = Field(min_length=1, max_length=128)
    source_ids: list[str] = Field(min_length=1)
    verification_status: str = "unverified"
    last_verified_at: date
    note: str | None = None
    active: bool = True

    @field_validator("verification_status")
    @classmethod
    def status(cls, value):
        if value not in {"verified", "needs_review", "unverified", "conflict", "superseded"}:
            raise ValueError("invalid evidence verification status")
        return value


class MemberSeed(SeedRow):
    seed_key: str = Field(min_length=1, max_length=200)
    material_key: str
    order_no: StrictInt = 1
    active: bool = True


class GroupSeed(SeedRow):
    key: str = Field(min_length=1, max_length=160)
    name_ko: str = Field(min_length=1)
    last_verified_at: date
    active: bool = True
    members: list[MemberSeed] = Field(default_factory=list)
    evidence: list[EvidenceSeed] = Field(default_factory=list)


class OptionSeed(SeedRow):
    seed_key: str = Field(min_length=1, max_length=220)
    material_key: str | None = None
    ingredient_group_key: str | None = None
    required_quantity: FiniteFloat = Field(gt=0)
    order_no: StrictInt = 1
    notes: str | None = None
    active: bool = True

    @model_validator(mode="after")
    def one_target(self):
        if (self.material_key is None) == (self.ingredient_group_key is None):
            raise ValueError("Recipe option must target exactly one Material or IngredientGroup")
        return self


class SlotSeed(SeedRow):
    seed_key: str = Field(min_length=1, max_length=200)
    label: str = Field(min_length=1)
    order_no: StrictInt = 1
    notes: str | None = None
    active: bool = True
    options: list[OptionSeed] = Field(default_factory=list)


class RecipeSeed(SeedRow):
    slug: str = Field(min_length=1, max_length=120, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    name_ko: str = Field(min_length=1)
    process_type: str
    result_material_key: str
    summary: str | None = None
    required_skill_tier: str | None = None
    required_skill_level: StrictInt | None = Field(default=None, gt=0)
    last_verified_at: date
    active: bool = True
    ingredients: list[SlotSeed] = Field(default_factory=list)
    evidence: list[EvidenceSeed] = Field(default_factory=list)

    @field_validator("process_type")
    @classmethod
    def supported_process_type(cls, value):
        if value not in SUPPORTED_RECIPE_PROCESS_TYPES:
            raise ValueError("unsupported Recipe process type")
        return value

    @field_validator("required_skill_tier")
    @classmethod
    def skill_tier(cls, value):
        if value is not None and value not in RECIPE_SKILL_TIERS:
            raise ValueError("unsupported Recipe skill tier")
        return value


class RecipeCatalog(SeedRow):
    ingredient_groups: list[GroupSeed] = Field(default_factory=list)
    recipes: list[RecipeSeed] = Field(default_factory=list)


DOMAIN_TYPES = {"recipe", "recipe_ingredient_slot", "recipe_ingredient_option", "ingredient_group"}


def _unique(values, label):
    values = list(values)
    if len(set(values)) != len(values):
        raise ValueError(f"duplicate {label}")


def _validate(catalog: RecipeCatalog, materials: dict[str, Material], source_ids: set[str]) -> None:
    _unique((g.key for g in catalog.ingredient_groups), "IngredientGroup key")
    _unique((r.slug for r in catalog.recipes), "Recipe slug")
    group_keys = {g.key for g in catalog.ingredient_groups}
    evidence_keys = []
    for owner in [*catalog.ingredient_groups, *catalog.recipes]:
        if isinstance(owner, GroupSeed):
            targets = {("ingredient_group", owner.key)}
            _unique((m.seed_key for m in owner.members), "group member seed_key")
            _unique((m.material_key for m in owner.members), "group member material")
            for member in owner.members:
                if not member.seed_key.startswith(f"ingredient-group.{owner.key}."):
                    raise ValueError("group member seed_key outside owner")
                if member.material_key not in materials:
                    raise ValueError(f"unknown Material key: {member.material_key}")
        else:
            if owner.result_material_key not in materials:
                raise ValueError(f"unknown result Material: {owner.result_material_key}")
            targets = {("recipe", owner.slug)}
            _unique((s.seed_key for s in owner.ingredients), "Recipe slot seed_key")
            # Evidence.entity_id is a stable string, so nested identities must also be unambiguous.
            _unique((o.seed_key for s in owner.ingredients for o in s.options), "Recipe option seed_key")
            for slot in owner.ingredients:
                if not slot.seed_key.startswith(f"{owner.slug}."):
                    raise ValueError("slot seed_key outside owner")
                targets.add(("recipe_ingredient_slot", slot.seed_key))
                for option in slot.options:
                    if not option.seed_key.startswith(f"{slot.seed_key}."):
                        raise ValueError("option seed_key outside slot")
                    if option.material_key is not None and option.material_key not in materials:
                        raise ValueError(f"unknown Material key: {option.material_key}")
                    if option.ingredient_group_key is not None and option.ingredient_group_key not in group_keys:
                        raise ValueError(f"unknown IngredientGroup key: {option.ingredient_group_key}")
                    targets.add(("recipe_ingredient_option", option.seed_key))
        for evidence in owner.evidence:
            if (evidence.entity_type, evidence.entity_seed_key) not in targets:
                raise ValueError("invalid Evidence entity target")
            if not set(evidence.source_ids) <= source_ids:
                raise ValueError("unknown Source ID")
            _unique(evidence.source_ids, "Evidence Source ID")
            evidence_keys.append(evidence.seed_key)
    _unique(evidence_keys, "Recipe-domain Evidence seed_key")


def _sync_rows(session, model, rows, identity, values, scope=None):
    """Update rows within one owner; archive omissions while preserving all IDs."""
    query = select(model)
    if scope is not None:
        query = query.where(scope)
    existing = {getattr(item, identity): item for item in session.scalars(query)}
    seen = set()
    result = {}
    for row in rows:
        key = getattr(row, identity)
        seen.add(key)
        item = existing.get(key)
        fields = values(row)
        if item is None:
            item = model(**{identity: key}, **fields)
            session.add(item)
        else:
            for field, value in fields.items():
                setattr(item, field, value)
        result[key] = item
    for key, item in existing.items():
        if key not in seen:
            item.active = False
    session.flush()
    return result


def sync_recipes(session: Session, directory: Path, materials: dict[str, Material]) -> None:
    """Optional recipe catalog sync. Absence means historical import, not mass archive."""
    path = directory / "seed_recipes.json"
    if not path.exists():
        return
    catalog = RecipeCatalog.model_validate(json.loads(path.read_text(encoding="utf-8")))
    _validate(catalog, materials, set(session.scalars(select(Source.id))))
    groups = _sync_rows(session, IngredientGroup, catalog.ingredient_groups, "key",
                        lambda g: g.model_dump(exclude={"key", "members", "evidence"}))
    for group in catalog.ingredient_groups:
        _sync_rows(session, IngredientGroupMember, group.members, "seed_key",
                   lambda m: dict(group_id=groups[group.key].id, material_id=materials[m.material_key].id,
                                  order_no=m.order_no, active=group.active and m.active),
                   IngredientGroupMember.group_id == groups[group.key].id)
    recipes = _sync_rows(session, Recipe, catalog.recipes, "slug",
                         lambda r: {**r.model_dump(exclude={"slug", "result_material_key", "ingredients", "evidence"}),
                                    "result_material_id": materials[r.result_material_key].id})
    for recipe in catalog.recipes:
        slots = _sync_rows(session, RecipeIngredientSlot, recipe.ingredients, "seed_key",
                           lambda s: {**s.model_dump(exclude={"seed_key", "options", "active"}),
                                      "recipe_id": recipes[recipe.slug].id,
                                      "active": recipe.active and s.active},
                           RecipeIngredientSlot.recipe_id == recipes[recipe.slug].id)
        for slot in recipe.ingredients:
            _sync_rows(session, RecipeIngredientOption, slot.options, "seed_key",
                       lambda o: {**o.model_dump(exclude={"seed_key", "material_key", "ingredient_group_key", "active"}),
                                  "slot_id": slots[slot.seed_key].id,
                                  "material_id": materials[o.material_key].id if o.material_key else None,
                                  "ingredient_group_id": groups[o.ingredient_group_key].id if o.ingredient_group_key else None,
                                  "active": recipe.active and slot.active and o.active},
                       RecipeIngredientOption.slot_id == slots[slot.seed_key].id)
    session.expire_all()
    # Removed parents deactivate their children, never delete them or reassign identities.
    for member in session.scalars(select(IngredientGroupMember)):
        if not member.group.active:
            member.active = False
    for slot in session.scalars(select(RecipeIngredientSlot)):
        if not slot.recipe.active:
            slot.active = False
        for option in slot.options:
            if not slot.active:
                option.active = False
    session.flush()
    targets = {}
    for g in session.scalars(select(IngredientGroup)):
        targets[("ingredient_group", g.key)] = g.active
    for r in session.scalars(select(Recipe)):
        targets[("recipe", r.slug)] = r.active
        for s in r.ingredient_slots:
            targets[("recipe_ingredient_slot", s.seed_key)] = s.active
            for o in s.options:
                targets[("recipe_ingredient_option", o.seed_key)] = o.active
    seen = set()
    for owner in [*catalog.ingredient_groups, *catalog.recipes]:
        for claim in owner.evidence:
            for source_id in claim.source_ids:
                key = f"{claim.seed_key}::{source_id}"
                seen.add(key)
                item = session.scalar(select(Evidence).where(Evidence.seed_key == key))
                if item is not None and item.entity_type not in DOMAIN_TYPES:
                    raise ValueError("Evidence stable key collides with another domain")
                if item is None:
                    item = Evidence(seed_key=key)
                    session.add(item)
                item.entity_type = claim.entity_type
                item.entity_id = claim.entity_seed_key
                item.claim_key = claim.claim_key
                item.source_id = source_id
                item.evidence_note = claim.note
                item.verification_status = claim.verification_status
                item.last_verified_at = claim.last_verified_at
                item.active = claim.active and targets[(claim.entity_type, claim.entity_seed_key)]
    for item in session.scalars(select(Evidence).where(Evidence.entity_type.in_(DOMAIN_TYPES))):
        if item.seed_key not in seen:
            item.active = False
    session.flush()
