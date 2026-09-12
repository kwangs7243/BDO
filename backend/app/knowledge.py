from __future__ import annotations

import json
import re
from datetime import datetime

from sqlalchemy import and_, or_, select
from sqlalchemy.orm import Session, selectinload

from app.content import (
    PHASE_ORDER,
    _relation_out,
    _schedule_out,
    _source_out,
    aggregate_verification,
)
from app.models import (
    Content,
    ContentRelation,
    Evidence,
    Material,
    Project,
    ProjectMaterial,
    ProjectMaterialSource,
    ProjectStage,
    Recipe, RecipeIngredientSlot, RecipeIngredientOption, IngredientGroup, IngredientGroupMember,
)
from app.schemas import (
    ContentRequirementOut,
    ContentSectionOut,
    ContentStepOut,
    KnowledgeContentOut,
    KnowledgeMaterialGroupRecipeUsageOut,
    KnowledgeMaterialIngredientGroupMembershipOut,
    KnowledgeMaterialOut,
    KnowledgeMaterialProjectRequirementOut,
    KnowledgeMaterialRecipeProducerOut,
    KnowledgeMaterialRecipeUsageOut,
    KnowledgeProjectMaterialOut,
    KnowledgeProjectOut,
    KnowledgeProjectStageOut,
    KnowledgeSearchMatchOut,
    KnowledgeSearchResultOut,
    ProjectMaterialSourceOut,
    RewardOut,
    KnowledgeRecipeOut, KnowledgeRecipeIngredientSlotOut, KnowledgeRecipeIngredientOptionOut,
    KnowledgeIngredientGroupOut, KnowledgeIngredientGroupMemberOut, KnowledgeRecipeEvidenceOut,
)


_WHITESPACE = re.compile(r"\s+")
_MAX_MATCH_TEXT = 240
RESOURCE_ORDER = {"material": 0, "content": 1, "project": 2, "recipe": 3}


def _content_query():
    return select(Content).options(
        selectinload(Content.schedules),
        selectinload(Content.requirements),
        selectinload(Content.steps),
        selectinload(Content.rewards),
        selectinload(Content.sections),
        selectinload(Content.outgoing_relations).selectinload(ContentRelation.to_content),
        selectinload(Content.incoming_relations).selectinload(ContentRelation.from_content),
    )


def _content_search_query():
    return select(Content).options(
        selectinload(Content.requirements),
        selectinload(Content.steps),
        selectinload(Content.rewards),
        selectinload(Content.sections),
    )


def _content_evidence(session: Session, slug: str) -> list[Evidence]:
    return list(
        session.scalars(
            select(Evidence)
            .where(or_(Evidence.entity_id == slug, Evidence.entity_id.like(f"{slug}.%")))
            .options(selectinload(Evidence.source))
            .order_by(Evidence.entity_type, Evidence.entity_id, Evidence.claim_key, Evidence.id)
        ).all()
    )


def get_knowledge_content(
    session: Session,
    slug: str,
    now: datetime,
) -> KnowledgeContentOut | None:
    """Return canonical Content knowledge without reading or creating personal state."""

    content = session.scalar(_content_query().where(Content.slug == slug))
    if content is None:
        return None

    evidence = _content_evidence(session, slug)
    return KnowledgeContentOut(
        slug=content.slug,
        name_ko=content.name_ko,
        category=content.category,
        summary=content.summary,
        purpose=content.purpose,
        party_type=content.party_type,
        difficulty=content.difficulty,
        status=content.status,
        last_verified_at=content.last_verified_at,
        verification_status=aggregate_verification(evidence),
        requirements=[
            ContentRequirementOut(
                seed_key=item.seed_key,
                kind=item.kind,
                title=item.title,
                description=item.description,
                structured_value=item.structured_value,
                requirement_level=item.requirement_level,
                order_no=item.order_no,
            )
            for item in sorted(
                (row for row in content.requirements if row.active),
                key=lambda row: (row.order_no, row.seed_key),
            )
        ],
        sections=[
            ContentSectionOut(
                seed_key=item.seed_key,
                section_type=item.section_type,
                title=item.title,
                body_markdown=item.body_markdown,
                order_no=item.order_no,
            )
            for item in sorted(
                (row for row in content.sections if row.active),
                key=lambda row: (row.order_no, row.seed_key),
            )
        ],
        steps=[
            ContentStepOut(
                seed_key=item.seed_key,
                phase=item.phase,
                order_no=item.order_no,
                title=item.title,
                description=item.description,
                checkable=item.checkable,
            )
            for item in sorted(
                (row for row in content.steps if row.active),
                key=lambda row: (PHASE_ORDER.get(row.phase, 99), row.order_no, row.seed_key),
            )
        ],
        schedules=[
            _schedule_out(item, now)
            for item in sorted(
                (row for row in content.schedules if row.active),
                key=lambda row: (row.rule_type, row.seed_key or "", row.id),
            )
        ],
        rewards=[
            RewardOut(
                seed_key=item.seed_key,
                name=item.name,
                reward_type=item.reward_type,
                amount=item.amount,
                min_amount=item.min_amount,
                max_amount=item.max_amount,
                unit=item.unit,
                is_choice=item.is_choice,
                choice_group=item.choice_group,
                recommendation=item.recommendation,
                notes=item.notes,
                order_no=item.order_no,
            )
            for item in sorted(
                (row for row in content.rewards if row.active),
                key=lambda row: (row.order_no, row.seed_key),
            )
        ],
        related_contents=[
            *[
                _relation_out(item, "outgoing")
                for item in sorted(
                    (row for row in content.outgoing_relations if row.active),
                    key=lambda row: (row.order_no, row.seed_key),
                )
            ],
            *[
                _relation_out(item, "incoming")
                for item in sorted(
                    (row for row in content.incoming_relations if row.active),
                    key=lambda row: (row.order_no, row.seed_key),
                )
            ],
        ],
        sources=[_source_out(item) for item in evidence],
    )


def _project_query():
    return select(Project).options(
        selectinload(Project.content),
        selectinload(Project.stages),
        selectinload(Project.dependencies),
        selectinload(Project.materials).selectinload(ProjectMaterial.material),
        selectinload(Project.materials)
        .selectinload(ProjectMaterial.sources)
        .selectinload(ProjectMaterialSource.content),
    )


def _project_search_query():
    return select(Project).options(
        selectinload(Project.stages),
        selectinload(Project.materials).selectinload(ProjectMaterial.material),
    )


def get_knowledge_project(session: Session, slug: str) -> KnowledgeProjectOut | None:
    """Return the canonical Project definition without loading local progress."""

    project = session.scalar(_project_query().where(Project.slug == slug))
    if project is None:
        return None

    stage_by_id = {stage.id: stage for stage in project.stages}
    dependency_keys: dict[int, list[str]] = {stage.id: [] for stage in project.stages}
    for dependency in project.dependencies:
        prerequisite = stage_by_id.get(dependency.depends_on_stage_id)
        if (
            dependency.active
            and dependency.stage_id in dependency_keys
            and prerequisite is not None
            and prerequisite.active
        ):
            dependency_keys[dependency.stage_id].append(prerequisite.seed_key)

    stages = [
        KnowledgeProjectStageOut(
            seed_key=stage.seed_key,
            name=stage.name,
            description=stage.description,
            order_no=stage.order_no,
            dependencies=sorted(dependency_keys.get(stage.id, [])),
        )
        for stage in sorted(project.stages, key=lambda item: (item.order_no, item.seed_key))
        if stage.active
    ]
    stage_order = {stage.id: stage.order_no for stage in project.stages}
    materials = [
        KnowledgeProjectMaterialOut(
            seed_key=item.seed_key,
            material_key=item.material.key,
            name_ko=item.material.name_ko,
            unit=item.material.unit,
            stage_seed_key=stage_by_id[item.stage_id].seed_key if item.stage_id else None,
            required_quantity=item.required_quantity,
            notes=item.notes,
            order_no=item.order_no,
            source_entity_type=item.source_entity_type,
            source_entity_seed_key=item.source_entity_seed_key,
            sources=[
                ProjectMaterialSourceOut(
                    seed_key=source.seed_key,
                    content_slug=source.content.slug,
                    content_name_ko=source.content.name_ko,
                    quantity_per_completion=source.quantity_per_completion,
                    notes=source.notes,
                    order_no=source.order_no,
                )
                for source in sorted(item.sources, key=lambda value: (value.order_no, value.seed_key))
                if source.active
            ],
        )
        for item in sorted(
            project.materials,
            key=lambda value: (stage_order.get(value.stage_id, 0), value.order_no, value.seed_key),
        )
        if item.active and item.material.active
    ]
    return KnowledgeProjectOut(
        slug=project.slug,
        name_ko=project.name_ko,
        content_slug=project.content.slug if project.content else None,
        summary=project.summary,
        active=project.active,
        stages=stages,
        materials=materials,
    )


def _recipe_query():
    options = selectinload(Recipe.ingredient_slots).selectinload(RecipeIngredientSlot.options)
    return select(Recipe).options(
        selectinload(Recipe.result_material),
        options.selectinload(RecipeIngredientOption.material),
        options.selectinload(RecipeIngredientOption.ingredient_group)
        .selectinload(IngredientGroup.members).selectinload(IngredientGroupMember.material),
    )


def _recipe_evidence(session, recipe):
    """Resolve typed stable targets, including archived children, without slug-prefix ambiguity."""
    targets = [and_(Evidence.entity_type == "recipe", Evidence.entity_id == recipe.slug)]
    slot_keys = [s.seed_key for s in recipe.ingredient_slots]
    option_keys = [o.seed_key for s in recipe.ingredient_slots for o in s.options]
    targets.extend([
        and_(Evidence.entity_type == "recipe_ingredient_slot", Evidence.entity_id.in_(slot_keys)),
        and_(Evidence.entity_type == "recipe_ingredient_option", Evidence.entity_id.in_(option_keys)),
    ])
    return list(session.scalars(select(Evidence).where(or_(*targets))
                               .options(selectinload(Evidence.source))
                               .order_by(Evidence.entity_type, Evidence.entity_id, Evidence.claim_key,
                                         Evidence.seed_key, Evidence.source_id)))


def _recipe_source_out(item):
    return KnowledgeRecipeEvidenceOut.model_validate(
        _source_out(item).model_dump(exclude={"evidence_id"})
    )


def _ingredient_group_out(
    session: Session,
    group: IngredientGroup,
) -> KnowledgeIngredientGroupOut:
    sources = list(
        session.scalars(
            select(Evidence)
            .where(
                Evidence.entity_type == "ingredient_group",
                Evidence.entity_id == group.key,
            )
            .options(selectinload(Evidence.source))
            .order_by(
                Evidence.claim_key,
                Evidence.seed_key,
                Evidence.source_id,
            )
        )
    )
    return KnowledgeIngredientGroupOut(
        key=group.key,
        name_ko=group.name_ko,
        last_verified_at=group.last_verified_at,
        verification_status=aggregate_verification(sources),
        members=[
            KnowledgeIngredientGroupMemberOut(
                material_key=member.material.key,
                name_ko=member.material.name_ko,
                unit=member.material.unit,
                order_no=member.order_no,
            )
            for member in sorted(
                group.members,
                key=lambda member: (member.order_no, member.seed_key),
            )
            if member.active and member.material.active
        ],
        sources=[_recipe_source_out(source) for source in sources],
    )


def get_knowledge_recipe(session: Session, slug: str) -> KnowledgeRecipeOut | None:
    """Read canonical cooking knowledge, with typed evidence and no personal-state query."""
    recipe = session.scalar(_recipe_query().where(Recipe.slug == slug, Recipe.active.is_(True)))
    if recipe is None:
        return None
    evidence = _recipe_evidence(session, recipe)
    groups = {}
    slots = []
    for slot in sorted(recipe.ingredient_slots, key=lambda s: (s.order_no, s.seed_key)):
        if not slot.active:
            continue
        options = []
        for option in sorted(slot.options, key=lambda o: (o.order_no, o.seed_key)):
            if not option.active:
                continue
            values = dict(seed_key=option.seed_key, required_quantity=option.required_quantity,
                          order_no=option.order_no, notes=option.notes)
            if option.material is not None:
                if not option.material.active:
                    continue
                values.update(target_type="material", material_key=option.material.key,
                              material_name_ko=option.material.name_ko, unit=option.material.unit)
            else:
                group = option.ingredient_group
                if group is None or not group.active:
                    continue
                if group.key not in groups:
                    groups[group.key] = _ingredient_group_out(session, group)
                values.update(target_type="ingredient_group", ingredient_group=groups[group.key])
            options.append(KnowledgeRecipeIngredientOptionOut(**values))
        slots.append(KnowledgeRecipeIngredientSlotOut(
            seed_key=slot.seed_key, label=slot.label, order_no=slot.order_no,
            notes=slot.notes, options=options))
    return KnowledgeRecipeOut(
        slug=recipe.slug, name_ko=recipe.name_ko, process_type=recipe.process_type,
        summary=recipe.summary, result_material_key=recipe.result_material.key,
        result_material_name_ko=recipe.result_material.name_ko, result_unit=recipe.result_material.unit,
        required_skill_tier=recipe.required_skill_tier, required_skill_level=recipe.required_skill_level,
        last_verified_at=recipe.last_verified_at, verification_status=aggregate_verification(evidence),
        ingredient_slots=slots, sources=[_recipe_source_out(e) for e in evidence])


def list_knowledge_materials(session: Session) -> list[KnowledgeMaterialOut]:
    """Project active Material rows through existing Recipe and Project contracts."""

    materials = list(
        session.scalars(
            select(Material)
            .where(Material.active.is_(True))
            .order_by(Material.name_ko, Material.key)
        )
    )
    recipes = [
        recipe
        for slug in session.scalars(
            select(Recipe.slug)
            .where(Recipe.active.is_(True))
            .order_by(Recipe.slug)
        )
        if (recipe := get_knowledge_recipe(session, slug)) is not None
    ]
    projects = [
        project
        for slug in session.scalars(
            select(Project.slug)
            .where(Project.active.is_(True))
            .order_by(Project.slug)
        )
        if (project := get_knowledge_project(session, slug)) is not None
    ]
    groups = list(
        session.scalars(
            select(IngredientGroup)
            .where(IngredientGroup.active.is_(True))
            .options(
                selectinload(IngredientGroup.members).selectinload(
                    IngredientGroupMember.material
                )
            )
            .order_by(IngredientGroup.key)
        )
    )
    group_outputs = {group.key: _ingredient_group_out(session, group) for group in groups}

    rows: dict[str, dict[str, list]] = {
        material.key: {
            "producers": [],
            "explicit": [],
            "memberships": [],
            "group_usages": [],
            "projects": [],
        }
        for material in materials
    }

    for group in groups:
        group_output = group_outputs[group.key]
        for member in sorted(
            group.members,
            key=lambda item: (item.order_no, item.seed_key),
        ):
            if not member.active or not member.material.active:
                continue
            rows[member.material.key]["memberships"].append(
                KnowledgeMaterialIngredientGroupMembershipOut(
                    group_key=group.key,
                    group_name_ko=group.name_ko,
                    member_seed_key=member.seed_key,
                    member_order_no=member.order_no,
                    group_verification_status=group_output.verification_status,
                    group_last_verified_at=group_output.last_verified_at,
                    sources=group_output.sources,
                )
            )

    for recipe in recipes:
        if recipe.result_material_key in rows:
            rows[recipe.result_material_key]["producers"].append(
                KnowledgeMaterialRecipeProducerOut(
                    recipe_slug=recipe.slug,
                    recipe_name_ko=recipe.name_ko,
                    process_type=recipe.process_type,
                    required_skill_tier=recipe.required_skill_tier,
                    required_skill_level=recipe.required_skill_level,
                    verification_status=recipe.verification_status,
                    last_verified_at=recipe.last_verified_at,
                )
            )
        for slot in recipe.ingredient_slots:
            is_alternative = len(slot.options) > 1
            for option in slot.options:
                if option.target_type == "material" and option.material_key in rows:
                    rows[option.material_key]["explicit"].append(
                        KnowledgeMaterialRecipeUsageOut(
                            recipe_slug=recipe.slug,
                            recipe_name_ko=recipe.name_ko,
                            process_type=recipe.process_type,
                            recipe_verification_status=recipe.verification_status,
                            recipe_last_verified_at=recipe.last_verified_at,
                            slot_seed_key=slot.seed_key,
                            slot_label=slot.label,
                            slot_order_no=slot.order_no,
                            option_seed_key=option.seed_key,
                            option_order_no=option.order_no,
                            required_quantity=option.required_quantity,
                            is_alternative=is_alternative,
                        )
                    )
                group = option.ingredient_group
                if option.target_type != "ingredient_group" or group is None:
                    continue
                for member in group.members:
                    if member.material_key not in rows:
                        continue
                    rows[member.material_key]["group_usages"].append(
                        KnowledgeMaterialGroupRecipeUsageOut(
                            usage_semantics="ingredient_group_candidate",
                            group_key=group.key,
                            group_name_ko=group.name_ko,
                            group_verification_status=group.verification_status,
                            group_last_verified_at=group.last_verified_at,
                            recipe_slug=recipe.slug,
                            recipe_name_ko=recipe.name_ko,
                            process_type=recipe.process_type,
                            slot_seed_key=slot.seed_key,
                            slot_label=slot.label,
                            slot_order_no=slot.order_no,
                            option_seed_key=option.seed_key,
                            option_order_no=option.order_no,
                            group_required_quantity=option.required_quantity,
                            is_alternative=is_alternative,
                            recipe_verification_status=recipe.verification_status,
                            recipe_last_verified_at=recipe.last_verified_at,
                        )
                    )

    for project in projects:
        stage_names = {stage.seed_key: stage.name for stage in project.stages}
        for material in project.materials:
            if material.material_key not in rows:
                continue
            rows[material.material_key]["projects"].append(
                KnowledgeMaterialProjectRequirementOut(
                    project_slug=project.slug,
                    project_name_ko=project.name_ko,
                    project_material_seed_key=material.seed_key,
                    stage_seed_key=material.stage_seed_key,
                    stage_name=stage_names.get(material.stage_seed_key),
                    required_quantity=material.required_quantity,
                    order_no=material.order_no,
                    notes=material.notes,
                    source_entity_type=material.source_entity_type,
                    source_entity_seed_key=material.source_entity_seed_key,
                    sources=material.sources,
                )
            )

    return [
        KnowledgeMaterialOut(
            key=material.key,
            name_ko=material.name_ko,
            unit=material.unit,
            produced_by_recipes=sorted(
                rows[material.key]["producers"],
                key=lambda item: item.recipe_slug,
            ),
            explicit_recipe_usages=sorted(
                rows[material.key]["explicit"],
                key=lambda item: (
                    item.recipe_slug,
                    item.slot_order_no,
                    item.option_order_no,
                    item.option_seed_key,
                ),
            ),
            ingredient_group_memberships=sorted(
                rows[material.key]["memberships"],
                key=lambda item: (item.group_key, item.member_order_no),
            ),
            group_recipe_usages=sorted(
                rows[material.key]["group_usages"],
                key=lambda item: (
                    item.recipe_slug,
                    item.group_key,
                    item.slot_order_no,
                    item.option_order_no,
                ),
            ),
            project_requirements=rows[material.key]["projects"],
        )
        for material in materials
    ]


def get_knowledge_material(
    session: Session,
    key: str,
) -> KnowledgeMaterialOut | None:
    """Return one active canonical Material projection without personal state."""

    return next(
        (material for material in list_knowledge_materials(session) if material.key == key),
        None,
    )


def _recipe_search_candidates(recipe):
    candidates = [
        ("recipe.name_ko", recipe.name_ko, 0, True),
        ("recipe.slug", recipe.slug, 0, True),
        ("recipe.result_material.name_ko", recipe.result_material.name_ko, 0, True),
        ("recipe.result_material.key", recipe.result_material.key, 0, True),
        ("recipe.summary", recipe.summary, 3, False),
    ]
    for slot in sorted(recipe.ingredient_slots, key=lambda s: (s.order_no, s.seed_key)):
        if not slot.active:
            continue
        candidates.append(("recipe_slot.label", slot.label, 4, False))
        for option in sorted(slot.options, key=lambda o: (o.order_no, o.seed_key)):
            if not option.active:
                continue
            candidates.append(("recipe_option.notes", option.notes, 5, False))
            if option.material is not None and option.material.active:
                candidates.extend([("ingredient.name_ko", option.material.name_ko, 4, False),
                                   ("ingredient.key", option.material.key, 4, False)])
            group = option.ingredient_group
            if group is not None and group.active:
                candidates.extend([("ingredient_group.name_ko", group.name_ko, 4, False),
                                   ("ingredient_group.key", group.key, 4, False)])
                for member in sorted(group.members, key=lambda m: (m.order_no, m.seed_key)):
                    if member.active and member.material.active:
                        candidates.extend([("group_member.name_ko", member.material.name_ko, 4, False),
                                           ("group_member.key", member.material.key, 4, False)])
    return candidates


def _normalize(value: str) -> str:
    return _WHITESPACE.sub(" ", value).strip().casefold()


def _stable_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _excerpt(value: str, query: str) -> str:
    text = _WHITESPACE.sub(" ", value).strip()
    if len(text) <= _MAX_MATCH_TEXT:
        return text
    index = text.casefold().find(query)
    start = max(index - 80, 0) if index >= 0 else 0
    end = min(start + _MAX_MATCH_TEXT, len(text))
    start = max(end - _MAX_MATCH_TEXT, 0)
    return f"{'…' if start else ''}{text[start:end]}{'…' if end < len(text) else ''}"


def _collect_matches(
    query: str,
    candidates: list[tuple[str, str | None, int, bool]],
) -> list[tuple[int, int, KnowledgeSearchMatchOut]]:
    matches: list[tuple[int, int, KnowledgeSearchMatchOut]] = []
    seen: set[tuple[str, str]] = set()
    for field_order, (field, value, base_rank, identity) in enumerate(candidates):
        if value is None:
            continue
        normalized = _normalize(value)
        if query not in normalized:
            continue
        if identity:
            rank = 0 if normalized == query else 1 if normalized.startswith(query) else 2
        else:
            rank = base_rank
        key = (field, value)
        if key in seen:
            continue
        seen.add(key)
        matches.append(
            (
                rank,
                field_order,
                KnowledgeSearchMatchOut(field=field, text=_excerpt(value, query)),
            )
        )
    matches.sort(key=lambda item: (item[0], item[1], _normalize(item[2].text), item[2].text))
    return matches


def _content_search_candidates(content: Content) -> list[tuple[str, str | None, int, bool]]:
    candidates: list[tuple[str, str | None, int, bool]] = [
        ("content.name_ko", content.name_ko, 0, True),
        ("content.slug", content.slug, 0, True),
        ("content.summary", content.summary, 3, False),
        ("content.purpose", content.purpose, 3, False),
    ]
    for requirement in sorted(content.requirements, key=lambda item: (item.order_no, item.seed_key)):
        if not requirement.active:
            continue
        candidates.extend(
            [
                ("requirement.title", requirement.title, 4, False),
                ("requirement.description", requirement.description, 4, False),
                (
                    "requirement.structured_value",
                    _stable_json(requirement.structured_value)
                    if requirement.structured_value is not None
                    else None,
                    4,
                    False,
                ),
            ]
        )
    for step in sorted(content.steps, key=lambda item: (item.order_no, item.seed_key)):
        if step.active:
            candidates.extend(
                [
                    ("step.title", step.title, 4, False),
                    ("step.description", step.description, 4, False),
                ]
            )
    for reward in sorted(content.rewards, key=lambda item: (item.order_no, item.seed_key)):
        if reward.active:
            candidates.extend(
                [
                    ("reward.name", reward.name, 4, False),
                    ("reward.recommendation", reward.recommendation, 4, False),
                    ("reward.notes", reward.notes, 5, False),
                ]
            )
    for section in sorted(content.sections, key=lambda item: (item.order_no, item.seed_key)):
        if section.active:
            candidates.extend(
                [
                    ("section.title", section.title, 4, False),
                    ("section.body_markdown", section.body_markdown, 5, False),
                ]
            )
    return candidates


def _project_search_candidates(project: Project) -> list[tuple[str, str | None, int, bool]]:
    candidates: list[tuple[str, str | None, int, bool]] = [
        ("project.name_ko", project.name_ko, 0, True),
        ("project.slug", project.slug, 0, True),
        ("project.summary", project.summary, 3, False),
    ]
    for stage in sorted(project.stages, key=lambda item: (item.order_no, item.seed_key)):
        if stage.active:
            candidates.extend(
                [
                    ("project_stage.name", stage.name, 4, False),
                    ("project_stage.description", stage.description, 4, False),
                ]
            )
    stage_order = {stage.id: stage.order_no for stage in project.stages}
    for material in sorted(
        project.materials,
        key=lambda item: (stage_order.get(item.stage_id, 0), item.order_no, item.seed_key),
    ):
        if not material.active or not material.material.active:
            continue
        candidates.extend(
            [
                ("material.name_ko", material.material.name_ko, 0, True),
                ("material.key", material.material.key, 0, True),
                ("project_material.notes", material.notes, 5, False),
            ]
        )
    return candidates


def search_knowledge(
    session: Session,
    query: str,
    limit: int = 20,
) -> list[KnowledgeSearchResultOut]:
    """Search current canonical knowledge resources with stable lexical ranking."""

    normalized_query = _normalize(query)
    if not normalized_query:
        raise ValueError("Knowledge search query must not be blank")
    if len(normalized_query) > 200:
        raise ValueError("Knowledge search query must be at most 200 characters")
    if not 1 <= limit <= 50:
        raise ValueError("Knowledge search limit must be between 1 and 50")

    contents = list(
        session.scalars(
            _content_search_query().where(Content.status == "active").order_by(Content.name_ko, Content.slug)
        ).all()
    )
    evidence_by_slug: dict[str, list[Evidence]] = {}
    for evidence in session.scalars(select(Evidence).order_by(Evidence.entity_id, Evidence.id)).all():
        root_slug = evidence.entity_id.split(".", 1)[0]
        evidence_by_slug.setdefault(root_slug, []).append(evidence)

    ranked: list[tuple[int, int, str, str, KnowledgeSearchResultOut]] = []
    materials = list(
        session.scalars(
            select(Material)
            .where(Material.active.is_(True))
            .order_by(Material.name_ko, Material.key)
        )
    )
    for material in materials:
        matches = _collect_matches(
            normalized_query,
            [
                ("material.name_ko", material.name_ko, 0, True),
                ("material.key", material.key, 0, True),
            ],
        )
        if matches:
            ranked.append(
                (
                    matches[0][0],
                    RESOURCE_ORDER["material"],
                    material.name_ko,
                    material.key,
                    KnowledgeSearchResultOut(
                        resource_type="material",
                        slug=material.key,
                        name_ko=material.name_ko,
                        category="material",
                        summary=None,
                        verification_status=None,
                        matches=[item[2] for item in matches[:3]],
                    ),
                )
            )
    for content in contents:
        matches = _collect_matches(normalized_query, _content_search_candidates(content))
        if matches:
            ranked.append(
                (
                    matches[0][0],
                    RESOURCE_ORDER["content"],
                    content.name_ko,
                    content.slug,
                    KnowledgeSearchResultOut(
                        resource_type="content",
                        slug=content.slug,
                        name_ko=content.name_ko,
                        category=content.category,
                        summary=content.summary,
                        verification_status=aggregate_verification(
                            evidence_by_slug.get(content.slug, [])
                        ),
                        matches=[item[2] for item in matches[:3]],
                    ),
                )
            )

    projects = list(
        session.scalars(
            _project_search_query().where(Project.active.is_(True)).order_by(Project.name_ko, Project.slug)
        ).all()
    )
    for project in projects:
        matches = _collect_matches(normalized_query, _project_search_candidates(project))
        if matches:
            ranked.append(
                (
                    matches[0][0],
                    RESOURCE_ORDER["project"],
                    project.name_ko,
                    project.slug,
                    KnowledgeSearchResultOut(
                        resource_type="project",
                        slug=project.slug,
                        name_ko=project.name_ko,
                        category=None,
                        summary=project.summary,
                        verification_status=None,
                        matches=[item[2] for item in matches[:3]],
                    ),
                )
            )

    for recipe in session.scalars(_recipe_query().where(Recipe.active.is_(True)).order_by(Recipe.slug)):
        matches = _collect_matches(normalized_query, _recipe_search_candidates(recipe))
        if matches:
            ranked.append((matches[0][0], RESOURCE_ORDER["recipe"], recipe.name_ko, recipe.slug,
                           KnowledgeSearchResultOut(
                               resource_type="recipe", slug=recipe.slug, name_ko=recipe.name_ko,
                               category=recipe.process_type, summary=recipe.summary,
                               verification_status=aggregate_verification(_recipe_evidence(session, recipe)),
                               matches=[item[2] for item in matches[:3]])))
    ranked.sort(key=lambda item: (item[0], item[1], item[2], item[3]))
    return [item[4] for item in ranked[:limit]]
