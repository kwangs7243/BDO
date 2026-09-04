from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models import (
    Material,
    Project,
    ProjectMaterial,
    ProjectStage,
    UserMaterialInventory,
    UserProjectStageState,
)
from app.schemas import (
    MaterialInventoryOut,
    MaterialInventoryUpdate,
    ProjectDetailOut,
    ProjectMaterialOut,
    ProjectMaterialSourceOut,
    ProjectStageOut,
    ProjectStageStateOut,
    ProjectStageStateUpdate,
    ProjectSummaryOut,
)


def _aware_utc(value: datetime | None) -> datetime | None:
    if value is not None and value.tzinfo is None:
        return value.replace(tzinfo=UTC)
    return value


def _project_query():
    return select(Project).options(
        selectinload(Project.content),
        selectinload(Project.stages).selectinload(ProjectStage.user_state),
        selectinload(Project.dependencies),
        selectinload(Project.materials).selectinload(ProjectMaterial.material).selectinload(Material.inventory),
        selectinload(Project.materials).selectinload(ProjectMaterial.sources),
    )


def _shortage(required: float, owned: float) -> float:
    return max(required - owned, 0.0)


def list_projects(session: Session) -> list[ProjectSummaryOut]:
    projects = session.scalars(_project_query().where(Project.active.is_(True)).order_by(Project.slug)).all()
    result: list[ProjectSummaryOut] = []
    for project in projects:
        stages = [stage for stage in project.stages if stage.active]
        completed = sum(1 for stage in stages if stage.user_state and stage.user_state.completed)
        shortage_material_ids = {
            item.material_id
            for item in project.materials
            if item.active and _shortage(item.required_quantity, item.material.inventory.quantity if item.material.inventory else 0) > 0
        }
        result.append(
            ProjectSummaryOut(
                slug=project.slug,
                name_ko=project.name_ko,
                content_slug=project.content.slug if project.content else None,
                active=project.active,
                completed_stage_count=completed,
                total_stage_count=len(stages),
                shortage_material_count=len(shortage_material_ids),
            )
        )
    return result


def get_project_detail(session: Session, slug: str) -> ProjectDetailOut | None:
    project = session.scalar(_project_query().where(Project.slug == slug))
    if project is None:
        return None

    dependency_keys: dict[int, list[str]] = {stage.id: [] for stage in project.stages}
    stage_by_id = {stage.id: stage for stage in project.stages}
    for dependency in project.dependencies:
        if dependency.active and dependency.stage_id in dependency_keys:
            prerequisite = stage_by_id.get(dependency.depends_on_stage_id)
            if prerequisite and prerequisite.active:
                dependency_keys[dependency.stage_id].append(prerequisite.seed_key)

    stage_order = {stage.id: stage.order_no for stage in project.stages}
    materials: list[ProjectMaterialOut] = []
    for item in sorted(
        project.materials,
        key=lambda value: (stage_order.get(value.stage_id, 0), value.order_no, value.seed_key),
    ):
        if not item.active:
            continue
        owned = item.material.inventory.quantity if item.material.inventory else 0.0
        sources = [
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
        ]
        materials.append(
            ProjectMaterialOut(
                seed_key=item.seed_key,
                material_key=item.material.key,
                name_ko=item.material.name_ko,
                unit=item.material.unit,
                stage_seed_key=stage_by_id[item.stage_id].seed_key if item.stage_id else None,
                required_quantity=item.required_quantity,
                owned_quantity=owned,
                shortage=_shortage(item.required_quantity, owned),
                notes=item.notes,
                order_no=item.order_no,
                source_entity_type=item.source_entity_type,
                source_entity_seed_key=item.source_entity_seed_key,
                sources=sources,
            )
        )

    stages = []
    for stage in sorted(project.stages, key=lambda value: (value.order_no, value.seed_key)):
        if not stage.active:
            continue
        state = stage.user_state
        stages.append(
            ProjectStageOut(
                id=stage.id,
                seed_key=stage.seed_key,
                name=stage.name,
                description=stage.description,
                order_no=stage.order_no,
                completed=bool(state and state.completed),
                completed_at=_aware_utc(state.completed_at) if state else None,
                note=state.note if state else None,
                dependencies=sorted(dependency_keys.get(stage.id, [])),
            )
        )
    return ProjectDetailOut(
        slug=project.slug,
        name_ko=project.name_ko,
        content_slug=project.content.slug if project.content else None,
        summary=project.summary,
        active=project.active,
        stages=stages,
        materials=materials,
    )


def put_material_inventory(
    session: Session, material_key: str, update: MaterialInventoryUpdate
) -> MaterialInventoryOut:
    material = session.scalar(select(Material).where(Material.key == material_key))
    if material is None:
        raise LookupError(material_key)
    inventory = session.scalar(
        select(UserMaterialInventory).where(UserMaterialInventory.material_id == material.id)
    )
    now = datetime.now(UTC)
    if inventory is None:
        inventory = UserMaterialInventory(material_id=material.id, updated_at=now)
        session.add(inventory)
    inventory.quantity = update.quantity
    inventory.note = update.note
    inventory.updated_at = now
    session.commit()
    session.refresh(inventory)
    return MaterialInventoryOut(
        material_key=material.key,
        quantity=inventory.quantity,
        note=inventory.note,
        updated_at=_aware_utc(inventory.updated_at),
    )


def put_project_stage_state(
    session: Session,
    project_slug: str,
    stage_id: int,
    update: ProjectStageStateUpdate,
) -> ProjectStageStateOut:
    stage = session.scalar(
        select(ProjectStage)
        .join(Project)
        .where(Project.slug == project_slug, ProjectStage.id == stage_id)
    )
    if stage is None:
        raise LookupError(f"{project_slug}:{stage_id}")
    state = session.scalar(
        select(UserProjectStageState).where(UserProjectStageState.stage_id == stage.id)
    )
    now = datetime.now(UTC)
    if state is None:
        state = UserProjectStageState(stage_id=stage.id, updated_at=now)
        session.add(state)
    state.completed = update.completed
    state.completed_at = now if update.completed else None
    state.note = update.note
    state.updated_at = now
    session.commit()
    session.refresh(state)
    return ProjectStageStateOut(
        project_slug=project_slug,
        stage_id=stage.id,
        completed=state.completed,
        completed_at=_aware_utc(state.completed_at),
        note=state.note,
        updated_at=_aware_utc(state.updated_at),
    )
