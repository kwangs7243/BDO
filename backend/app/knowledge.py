from __future__ import annotations

import json
import re
from datetime import datetime

from sqlalchemy import or_, select
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
    Project,
    ProjectMaterial,
    ProjectMaterialSource,
    ProjectStage,
)
from app.schemas import (
    ContentRequirementOut,
    ContentSectionOut,
    ContentStepOut,
    KnowledgeContentOut,
    KnowledgeProjectMaterialOut,
    KnowledgeProjectOut,
    KnowledgeProjectStageOut,
    KnowledgeSearchMatchOut,
    KnowledgeSearchResultOut,
    ProjectMaterialSourceOut,
    RewardOut,
)


_WHITESPACE = re.compile(r"\s+")
_MAX_MATCH_TEXT = 240


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
    """Search current canonical Content and Project rows with stable lexical ranking."""

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

    ranked: list[tuple[int, str, str, str, KnowledgeSearchResultOut]] = []
    for content in contents:
        matches = _collect_matches(normalized_query, _content_search_candidates(content))
        if matches:
            ranked.append(
                (
                    matches[0][0],
                    "content",
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
                    "project",
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

    ranked.sort(key=lambda item: (item[0], item[1], item[2], item[3]))
    return [item[4] for item in ranked[:limit]]