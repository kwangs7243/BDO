from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import (
    Content,
    ContentRequirement,
    ContentSection,
    Material,
    Project,
    ProjectMaterial,
    ProjectMaterialSource,
    ProjectStage,
    ProjectStageDependency,
)


SOURCE_ENTITY_MODELS = {
    "content_requirement": ContentRequirement,
    "content_section": ContentSection,
}


def _unique(rows: list[dict[str, Any]], field: str, scope: str) -> None:
    seen: set[str] = set()
    for row in rows:
        value = str(row.get(field, ""))
        if not value:
            raise ValueError(f"missing {field} in {scope}")
        if value in seen:
            raise ValueError(f"duplicate {field} in {scope}: {value}")
        seen.add(value)


def _project_seed_key(slug: str, row: dict[str, Any]) -> str:
    key = str(row.get("seed_key", ""))
    if not key or not key.startswith(f"{slug}."):
        raise ValueError(f"project seed_key must start with '{slug}.': {key!r}")
    return key


def _validate_dag(
    project_slug: str,
    stages: list[dict[str, Any]],
    dependencies: list[dict[str, Any]],
) -> None:
    nodes = {_project_seed_key(project_slug, row) for row in stages}
    edges: dict[str, list[str]] = {node: [] for node in nodes}
    for row in dependencies:
        stage_key = str(row.get("stage_seed_key", ""))
        prerequisite_key = str(row.get("depends_on_stage_seed_key", ""))
        if stage_key not in nodes:
            raise ValueError(f"unknown stage_seed_key: {stage_key}")
        if prerequisite_key not in nodes:
            raise ValueError(f"unknown depends_on_stage_seed_key: {prerequisite_key}")
        if stage_key == prerequisite_key:
            raise ValueError(f"stage cannot depend on itself: {stage_key}")
        if bool(row.get("active", True)):
            edges[stage_key].append(prerequisite_key)

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visiting:
            raise ValueError(f"project stage dependency cycle: {project_slug}")
        if node in visited:
            return
        visiting.add(node)
        for dependency in edges[node]:
            visit(dependency)
        visiting.remove(node)
        visited.add(node)

    for node in nodes:
        visit(node)


def _sync_materials(session: Session, rows: list[dict[str, Any]]) -> dict[str, Material]:
    _unique(rows, "key", "materials")
    existing = list(session.scalars(select(Material)).all())
    by_key = {item.key: item for item in existing}
    seen: set[str] = set()
    result: dict[str, Material] = {}
    for row in rows:
        key = str(row["key"])
        seen.add(key)
        material = by_key.get(key)
        if material is None:
            material = Material(key=key)
            session.add(material)
        material.name_ko = row["name_ko"]
        material.unit = row.get("unit", "개")
        material.active = bool(row.get("active", True))
        result[key] = material
    for material in existing:
        if material.key not in seen:
            material.active = False
    session.flush()
    return result


def _sync_stages(
    session: Session, project: Project, rows: list[dict[str, Any]]
) -> dict[str, ProjectStage]:
    _unique(rows, "seed_key", f"{project.slug} stages")
    existing = list(session.scalars(select(ProjectStage).where(ProjectStage.project_id == project.id)).all())
    by_key = {item.seed_key: item for item in existing}
    seen: set[str] = set()
    result: dict[str, ProjectStage] = {}
    for index, row in enumerate(rows, start=1):
        key = _project_seed_key(project.slug, row)
        seen.add(key)
        stage = by_key.get(key)
        if stage is None:
            stage = ProjectStage(project_id=project.id, seed_key=key)
            session.add(stage)
        stage.name = row["name"]
        stage.description = row.get("description")
        stage.order_no = int(row.get("order_no", index))
        stage.active = bool(row.get("active", True))
        result[key] = stage
    for stage in existing:
        if stage.seed_key not in seen:
            stage.active = False
    session.flush()
    return result


def _sync_dependencies(
    session: Session,
    project: Project,
    rows: list[dict[str, Any]],
    stages: dict[str, ProjectStage],
) -> None:
    _unique(rows, "seed_key", f"{project.slug} stage dependencies")
    existing = list(
        session.scalars(
            select(ProjectStageDependency).where(ProjectStageDependency.project_id == project.id)
        ).all()
    )
    by_key = {item.seed_key: item for item in existing}
    seen: set[str] = set()
    for row in rows:
        key = _project_seed_key(project.slug, row)
        stage_key = str(row.get("stage_seed_key", ""))
        prerequisite_key = str(row.get("depends_on_stage_seed_key", ""))
        if stage_key not in stages:
            raise ValueError(f"unknown stage_seed_key: {stage_key}")
        if prerequisite_key not in stages:
            raise ValueError(f"unknown depends_on_stage_seed_key: {prerequisite_key}")
        seen.add(key)
        dependency = by_key.get(key)
        if dependency is None:
            dependency = ProjectStageDependency(project_id=project.id, seed_key=key)
            session.add(dependency)
        dependency.stage_id = stages[stage_key].id
        dependency.depends_on_stage_id = stages[prerequisite_key].id
        dependency.active = bool(row.get("active", True))
    for dependency in existing:
        if dependency.seed_key not in seen:
            dependency.active = False


def _validate_source_entity(session: Session, entity_type: str | None, seed_key: str | None) -> None:
    if entity_type is None and seed_key is None:
        return
    model = SOURCE_ENTITY_MODELS.get(str(entity_type))
    if model is None or not seed_key:
        raise ValueError(f"unsupported project material source entity: {entity_type}:{seed_key}")
    if session.scalar(select(model).where(model.seed_key == seed_key)) is None:
        raise ValueError(f"unknown project material source entity: {entity_type}:{seed_key}")


def _sync_material_sources(
    session: Session,
    project: Project,
    project_material: ProjectMaterial,
    rows: list[dict[str, Any]],
) -> None:
    _unique(rows, "seed_key", f"{project_material.seed_key} sources")
    existing = list(
        session.scalars(
            select(ProjectMaterialSource).where(
                ProjectMaterialSource.project_material_id == project_material.id
            )
        ).all()
    )
    by_key = {item.seed_key: item for item in existing}
    seen: set[str] = set()
    for index, row in enumerate(rows, start=1):
        key = _project_seed_key(project.slug, row)
        content = session.scalar(select(Content).where(Content.slug == row.get("content_slug")))
        if content is None:
            raise ValueError(f"unknown project material source content: {row.get('content_slug')}")
        quantity = row.get("quantity_per_completion")
        if quantity is not None and float(quantity) < 0:
            raise ValueError(f"quantity_per_completion must be non-negative: {key}")
        seen.add(key)
        source = by_key.get(key)
        if source is None:
            source = ProjectMaterialSource(project_material_id=project_material.id, seed_key=key)
            session.add(source)
        source.content_id = content.id
        source.quantity_per_completion = float(quantity) if quantity is not None else None
        source.notes = row.get("notes")
        source.order_no = int(row.get("order_no", index))
        source.active = bool(row.get("active", True))
    for source in existing:
        if source.seed_key not in seen:
            source.active = False


def _sync_project_materials(
    session: Session,
    project: Project,
    rows: list[dict[str, Any]],
    stages: dict[str, ProjectStage],
    materials: dict[str, Material],
) -> None:
    _unique(rows, "seed_key", f"{project.slug} project materials")
    existing = list(
        session.scalars(select(ProjectMaterial).where(ProjectMaterial.project_id == project.id)).all()
    )
    by_key = {item.seed_key: item for item in existing}
    seen: set[str] = set()
    for index, row in enumerate(rows, start=1):
        key = _project_seed_key(project.slug, row)
        material_key = str(row.get("material_key", ""))
        stage_key = row.get("stage_seed_key")
        if material_key not in materials:
            raise ValueError(f"unknown material_key: {material_key}")
        if stage_key is not None and stage_key not in stages:
            raise ValueError(f"unknown stage_seed_key: {stage_key}")
        required_quantity = float(row["required_quantity"])
        if required_quantity < 0:
            raise ValueError(f"required_quantity must be non-negative: {key}")
        source_entity_type = row.get("source_entity_type")
        source_entity_seed_key = row.get("source_entity_seed_key")
        _validate_source_entity(session, source_entity_type, source_entity_seed_key)
        seen.add(key)
        item = by_key.get(key)
        if item is None:
            item = ProjectMaterial(project_id=project.id, seed_key=key)
            session.add(item)
        item.stage_id = stages[stage_key].id if stage_key is not None else None
        item.material_id = materials[material_key].id
        item.required_quantity = required_quantity
        item.order_no = int(row.get("order_no", index))
        item.notes = row.get("notes")
        item.source_entity_type = source_entity_type
        item.source_entity_seed_key = source_entity_seed_key
        item.active = bool(row.get("active", True))
        session.flush()
        _sync_material_sources(session, project, item, row.get("sources", []))
    for item in existing:
        if item.seed_key not in seen:
            item.active = False
            for source in item.sources:
                source.active = False


def sync_projects(session: Session, directory: Path) -> None:
    """Synchronize optional canonical project data without touching user-owned rows."""

    path = directory / "seed_projects.json"
    if not path.exists():
        return
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("seed_projects.json must contain an object")
    material_rows = payload.get("materials", [])
    project_rows = payload.get("projects", [])
    if not isinstance(material_rows, list) or not isinstance(project_rows, list):
        raise ValueError("seed_projects.json materials/projects must be lists")
    _unique(project_rows, "slug", "projects")
    materials = _sync_materials(session, material_rows)

    existing_projects = list(session.scalars(select(Project)).all())
    by_slug = {item.slug: item for item in existing_projects}
    seen_projects: set[str] = set()
    for row in project_rows:
        slug = str(row["slug"])
        content_slug = row.get("content_slug")
        content = None
        if content_slug is not None:
            content = session.scalar(select(Content).where(Content.slug == content_slug))
            if content is None:
                raise ValueError(f"unknown project content_slug: {content_slug}")
        stage_rows = row.get("stages", [])
        dependency_rows = row.get("stage_dependencies", [])
        _validate_dag(slug, stage_rows, dependency_rows)
        seen_projects.add(slug)
        project = by_slug.get(slug)
        if project is None:
            project = Project(
                slug=slug,
                name_ko=row["name_ko"],
                content_id=content.id if content else None,
                summary=row.get("summary"),
                active=bool(row.get("active", True)),
            )
            session.add(project)
            session.flush()
        else:
            project.name_ko = row["name_ko"]
            project.content_id = content.id if content else None
            project.summary = row.get("summary")
            project.active = bool(row.get("active", True))
        stages = _sync_stages(session, project, stage_rows)
        _sync_dependencies(session, project, dependency_rows, stages)
        _sync_project_materials(
            session,
            project,
            row.get("project_materials", []),
            stages,
            materials,
        )

    for project in existing_projects:
        if project.slug in seen_projects:
            continue
        project.active = False
        for stage in project.stages:
            stage.active = False
        for dependency in project.dependencies:
            dependency.active = False
        for item in project.materials:
            item.active = False
            for source in item.sources:
                source.active = False
