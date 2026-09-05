from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime, tzinfo
from typing import Any

from pydantic import ValidationError
from sqlalchemy import delete, func, select
from sqlalchemy.orm import Session

from app.models import (
    ChecklistInstance,
    ChecklistItemState,
    ChecklistTemplate,
    ChecklistTemplateItem,
    Content,
    Material,
    Project,
    ProjectStage,
    UserContentState,
    UserMaterialInventory,
    UserProjectStageState,
)
from app.periods import KST
from app.schemas import (
    UserBackupChecklistInstance,
    UserBackupChecklistItem,
    UserBackupContentState,
    UserBackupCounts,
    UserBackupData,
    UserBackupEnvelope,
    UserBackupImportMode,
    UserBackupImportResult,
    UserBackupMaterialInventory,
    UserBackupProjectStageState,
    UserBackupValidationReport,
)


BACKUP_FORMAT = "bdo-companion-user-backup"
BACKUP_VERSION = 1


class UserBackupValidationError(ValueError):
    def __init__(self, report: UserBackupValidationReport):
        super().__init__("User backup validation failed")
        self.report = report


@dataclass
class _CanonicalMaps:
    contents: dict[str, Content]
    templates: dict[str, list[ChecklistTemplate]]
    items: dict[tuple[int, str], list[ChecklistTemplateItem]]
    materials: dict[str, Material]
    projects: dict[str, Project]
    stages: dict[tuple[int, str], ProjectStage]


def _as_utc(value: datetime, assumed_timezone: tzinfo = UTC) -> datetime:
    """Normalize DB datetimes while preserving existing SQLite wall-time conventions."""

    aware = value.replace(tzinfo=assumed_timezone) if value.tzinfo is None else value
    return aware.astimezone(UTC)


def _canonical_maps(session: Session) -> _CanonicalMaps:
    contents = {item.slug: item for item in session.scalars(select(Content)).all()}

    templates: dict[str, list[ChecklistTemplate]] = defaultdict(list)
    for template in session.scalars(select(ChecklistTemplate)).all():
        if template.seed_key:
            templates[template.seed_key].append(template)

    items: dict[tuple[int, str], list[ChecklistTemplateItem]] = defaultdict(list)
    for item in session.scalars(select(ChecklistTemplateItem)).all():
        if item.seed_key:
            items[(item.template_id, item.seed_key)].append(item)

    materials = {item.key: item for item in session.scalars(select(Material)).all()}
    projects = {item.slug: item for item in session.scalars(select(Project)).all()}
    stages = {
        (item.project_id, item.seed_key): item
        for item in session.scalars(select(ProjectStage)).all()
    }
    return _CanonicalMaps(
        contents=contents,
        templates=dict(templates),
        items=dict(items),
        materials=materials,
        projects=projects,
        stages=stages,
    )


def export_user_backup(
    session: Session,
    *,
    exported_at: datetime | None = None,
) -> UserBackupEnvelope:
    """Export user-owned state with portable canonical identities only."""

    content_states = [
        UserBackupContentState(
            content_slug=content.slug,
            state=state.state,
            priority=state.priority,
            note=state.note,
            updated_at=_as_utc(state.updated_at),
        )
        for state, content in session.execute(
            select(UserContentState, Content)
            .join(Content, UserContentState.content_id == Content.id)
            .order_by(Content.slug)
        ).all()
    ]

    checklist_instances: list[UserBackupChecklistInstance] = []
    instance_rows = session.execute(
        select(ChecklistInstance, ChecklistTemplate)
        .join(ChecklistTemplate, ChecklistInstance.template_id == ChecklistTemplate.id)
        .order_by(ChecklistTemplate.seed_key, ChecklistInstance.period_key)
    ).all()
    for instance, template in instance_rows:
        if not template.seed_key:
            raise ValueError(
                f"Checklist template {template.id} has no stable seed_key"
            )
        items: list[UserBackupChecklistItem] = []
        state_rows = session.execute(
            select(ChecklistItemState, ChecklistTemplateItem)
            .join(
                ChecklistTemplateItem,
                ChecklistItemState.template_item_id == ChecklistTemplateItem.id,
            )
            .where(ChecklistItemState.instance_id == instance.id)
            .order_by(ChecklistTemplateItem.seed_key)
        ).all()
        for state, item in state_rows:
            if item.template_id != template.id:
                raise ValueError(
                    f"Checklist item {item.id} does not belong to template {template.seed_key}"
                )
            if not item.seed_key:
                raise ValueError(
                    f"Checklist item {item.id} has no stable seed_key"
                )
            items.append(
                UserBackupChecklistItem(
                    item_seed_key=item.seed_key,
                    completed=state.completed,
                    completed_at=(
                        _as_utc(state.completed_at)
                        if state.completed_at is not None
                        else None
                    ),
                    note=state.note,
                )
            )
        checklist_instances.append(
            UserBackupChecklistInstance(
                template_seed_key=template.seed_key,
                period_key=instance.period_key,
                period_start=_as_utc(instance.period_start, KST),
                period_end=_as_utc(instance.period_end, KST),
                generated_at=_as_utc(instance.generated_at),
                items=items,
            )
        )

    material_inventory = [
        UserBackupMaterialInventory(
            material_key=material.key,
            quantity=inventory.quantity,
            note=inventory.note,
            updated_at=_as_utc(inventory.updated_at),
        )
        for inventory, material in session.execute(
            select(UserMaterialInventory, Material)
            .join(Material, UserMaterialInventory.material_id == Material.id)
            .order_by(Material.key)
        ).all()
    ]

    project_stage_states = [
        UserBackupProjectStageState(
            project_slug=project.slug,
            stage_seed_key=stage.seed_key,
            completed=state.completed,
            completed_at=(
                _as_utc(state.completed_at)
                if state.completed_at is not None
                else None
            ),
            note=state.note,
            updated_at=_as_utc(state.updated_at),
        )
        for state, stage, project in session.execute(
            select(UserProjectStageState, ProjectStage, Project)
            .join(ProjectStage, UserProjectStageState.stage_id == ProjectStage.id)
            .join(Project, ProjectStage.project_id == Project.id)
            .order_by(Project.slug, ProjectStage.seed_key)
        ).all()
    ]

    backup = UserBackupEnvelope(
        format=BACKUP_FORMAT,
        version=BACKUP_VERSION,
        exported_at=_as_utc(exported_at or datetime.now(UTC)),
        data=UserBackupData(
            content_states=content_states,
            checklist_instances=checklist_instances,
            material_inventory=material_inventory,
            project_stage_states=project_stage_states,
        ),
    )
    report, _ = validate_user_backup(session, backup)
    if not report.valid:
        raise ValueError(
            "Backup export validation failed: " + "; ".join(report.errors)
        )
    return backup


def _validation_error_messages(error: ValidationError) -> list[str]:
    messages = []
    for item in error.errors(include_url=False):
        location = ".".join(str(part) for part in item["loc"])
        messages.append(f"{location}: {item['msg']}")
    return messages


def _header_value(payload: Any, key: str, expected_type: type) -> Any | None:
    if not isinstance(payload, dict):
        return None
    value = payload.get(key)
    if expected_type is int and isinstance(value, bool):
        return None
    return value if isinstance(value, expected_type) else None


def _append_duplicate_error(
    errors: list[str],
    seen: set[Any],
    identity: Any,
    label: str,
) -> None:
    if identity in seen:
        errors.append(f"duplicate {label}: {identity}")
    else:
        seen.add(identity)


def validate_user_backup(
    session: Session,
    payload: Any,
) -> tuple[UserBackupValidationReport, UserBackupEnvelope | None]:
    """Validate the complete payload and every canonical reference without writes."""

    format_value = _header_value(payload, "format", str)
    version_value = _header_value(payload, "version", int)
    try:
        backup = UserBackupEnvelope.model_validate(payload)
    except ValidationError as error:
        report = UserBackupValidationReport(
            valid=False,
            format=format_value,
            version=version_value,
            errors=_validation_error_messages(error),
        )
        return report, None

    errors: list[str] = []
    warnings: list[str] = []
    if backup.format != BACKUP_FORMAT:
        errors.append(f"unsupported backup format: {backup.format}")
    if backup.version != BACKUP_VERSION:
        errors.append(f"unsupported backup version: {backup.version}")

    maps = _canonical_maps(session)
    data = backup.data

    seen_content: set[str] = set()
    for row in data.content_states:
        _append_duplicate_error(
            errors, seen_content, row.content_slug, "content_slug"
        )
        content = maps.contents.get(row.content_slug)
        if content is None:
            errors.append(f"unknown content_slug: {row.content_slug}")
        elif content.status != "active":
            warnings.append(f"archived content resolved: {row.content_slug}")

    seen_instances: set[tuple[str, str]] = set()
    for instance in data.checklist_instances:
        identity = (instance.template_seed_key, instance.period_key)
        _append_duplicate_error(
            errors, seen_instances, identity, "checklist instance"
        )
        if instance.period_start >= instance.period_end:
            errors.append(
                "invalid checklist period range: "
                f"{instance.template_seed_key}/{instance.period_key}"
            )
        templates = maps.templates.get(instance.template_seed_key, [])
        if not templates:
            errors.append(
                f"unknown template_seed_key: {instance.template_seed_key}"
            )
            continue
        if len(templates) != 1:
            errors.append(
                f"ambiguous template_seed_key: {instance.template_seed_key}"
            )
            continue
        template = templates[0]
        if not template.active:
            warnings.append(
                f"archived checklist template resolved: {instance.template_seed_key}"
            )
        seen_items: set[str] = set()
        for item in instance.items:
            _append_duplicate_error(
                errors, seen_items, item.item_seed_key, "item_seed_key"
            )
            matches = maps.items.get((template.id, item.item_seed_key), [])
            if not matches:
                errors.append(
                    "unknown checklist item for template: "
                    f"{instance.template_seed_key}/{item.item_seed_key}"
                )
            elif len(matches) != 1:
                errors.append(
                    "ambiguous checklist item for template: "
                    f"{instance.template_seed_key}/{item.item_seed_key}"
                )
            elif not matches[0].active:
                warnings.append(
                    "archived checklist item resolved: "
                    f"{instance.template_seed_key}/{item.item_seed_key}"
                )

    seen_materials: set[str] = set()
    for row in data.material_inventory:
        _append_duplicate_error(
            errors, seen_materials, row.material_key, "material_key"
        )
        material = maps.materials.get(row.material_key)
        if material is None:
            errors.append(f"unknown material_key: {row.material_key}")
        elif not material.active:
            warnings.append(f"archived material resolved: {row.material_key}")

    seen_stages: set[tuple[str, str]] = set()
    for row in data.project_stage_states:
        identity = (row.project_slug, row.stage_seed_key)
        _append_duplicate_error(
            errors, seen_stages, identity, "project stage"
        )
        project = maps.projects.get(row.project_slug)
        if project is None:
            errors.append(f"unknown project_slug: {row.project_slug}")
            continue
        stage = maps.stages.get((project.id, row.stage_seed_key))
        if stage is None:
            errors.append(
                "unknown project stage: "
                f"{row.project_slug}/{row.stage_seed_key}"
            )
            continue
        if not project.active or not stage.active:
            warnings.append(
                "archived project stage resolved: "
                f"{row.project_slug}/{row.stage_seed_key}"
            )

    checklist_items = sum(
        len(instance.items) for instance in data.checklist_instances
    )
    report = UserBackupValidationReport(
        valid=not errors,
        format=backup.format,
        version=backup.version,
        content_states=len(data.content_states),
        checklist_instances=len(data.checklist_instances),
        checklist_items=checklist_items,
        material_inventory=len(data.material_inventory),
        project_stage_states=len(data.project_stage_states),
        errors=errors,
        warnings=warnings,
    )
    return report, backup


def _row_count(session: Session, model: type) -> int:
    return session.scalar(select(func.count()).select_from(model)) or 0


def _resolve_template(
    maps: _CanonicalMaps, template_seed_key: str
) -> ChecklistTemplate:
    return maps.templates[template_seed_key][0]


def import_user_backup(
    session: Session,
    payload: Any,
    mode: UserBackupImportMode,
) -> UserBackupImportResult:
    """Restore a fully validated backup and commit all user-state changes once."""

    report, backup = validate_user_backup(session, payload)
    if not report.valid or backup is None:
        raise UserBackupValidationError(report)

    maps = _canonical_maps(session)
    deleted_counts = UserBackupCounts()
    try:
        if mode == UserBackupImportMode.REPLACE:
            deleted_counts = UserBackupCounts(
                content_states=_row_count(session, UserContentState),
                checklist_instances=_row_count(session, ChecklistInstance),
                checklist_items=_row_count(session, ChecklistItemState),
                material_inventory=_row_count(session, UserMaterialInventory),
                project_stage_states=_row_count(session, UserProjectStageState),
            )
            session.execute(delete(ChecklistItemState))
            session.execute(delete(ChecklistInstance))
            session.execute(delete(UserContentState))
            session.execute(delete(UserMaterialInventory))
            session.execute(delete(UserProjectStageState))
            session.flush()

        content_states = {
            item.content_id: item
            for item in session.scalars(select(UserContentState)).all()
        }
        for row in backup.data.content_states:
            content = maps.contents[row.content_slug]
            state = content_states.get(content.id)
            if state is None:
                state = UserContentState(
                    content_id=content.id,
                    updated_at=row.updated_at.astimezone(UTC),
                )
                session.add(state)
                content_states[content.id] = state
            state.state = row.state.value
            state.priority = row.priority
            state.note = row.note
            state.updated_at = row.updated_at.astimezone(UTC)

        instances = {
            (item.template_id, item.period_key): item
            for item in session.scalars(select(ChecklistInstance)).all()
        }
        item_states = {
            (item.instance_id, item.template_item_id): item
            for item in session.scalars(select(ChecklistItemState)).all()
        }
        for row in backup.data.checklist_instances:
            template = _resolve_template(maps, row.template_seed_key)
            identity = (template.id, row.period_key)
            instance = instances.get(identity)
            if instance is None:
                instance = ChecklistInstance(
                    template_id=template.id,
                    period_key=row.period_key,
                    period_start=row.period_start.astimezone(KST),
                    period_end=row.period_end.astimezone(KST),
                    generated_at=row.generated_at.astimezone(UTC),
                )
                session.add(instance)
                session.flush()
                instances[identity] = instance
            else:
                instance.period_start = row.period_start.astimezone(KST)
                instance.period_end = row.period_end.astimezone(KST)
                instance.generated_at = row.generated_at.astimezone(UTC)
            for item_row in row.items:
                template_item = maps.items[
                    (template.id, item_row.item_seed_key)
                ][0]
                state_identity = (instance.id, template_item.id)
                item_state = item_states.get(state_identity)
                if item_state is None:
                    item_state = ChecklistItemState(
                        instance_id=instance.id,
                        template_item_id=template_item.id,
                    )
                    session.add(item_state)
                    item_states[state_identity] = item_state
                item_state.completed = item_row.completed
                item_state.completed_at = (
                    item_row.completed_at.astimezone(UTC)
                    if item_row.completed_at is not None
                    else None
                )
                item_state.note = item_row.note

        inventories = {
            item.material_id: item
            for item in session.scalars(select(UserMaterialInventory)).all()
        }
        for row in backup.data.material_inventory:
            material = maps.materials[row.material_key]
            inventory = inventories.get(material.id)
            if inventory is None:
                inventory = UserMaterialInventory(
                    material_id=material.id,
                    updated_at=row.updated_at.astimezone(UTC),
                )
                session.add(inventory)
                inventories[material.id] = inventory
            inventory.quantity = row.quantity
            inventory.note = row.note
            inventory.updated_at = row.updated_at.astimezone(UTC)

        stage_states = {
            item.stage_id: item
            for item in session.scalars(select(UserProjectStageState)).all()
        }
        for row in backup.data.project_stage_states:
            project = maps.projects[row.project_slug]
            stage = maps.stages[(project.id, row.stage_seed_key)]
            state = stage_states.get(stage.id)
            if state is None:
                state = UserProjectStageState(
                    stage_id=stage.id,
                    updated_at=row.updated_at.astimezone(UTC),
                )
                session.add(state)
                stage_states[stage.id] = state
            state.completed = row.completed
            state.completed_at = (
                row.completed_at.astimezone(UTC)
                if row.completed_at is not None
                else None
            )
            state.note = row.note
            state.updated_at = row.updated_at.astimezone(UTC)

        session.flush()
        session.commit()
    except Exception:
        session.rollback()
        raise

    return UserBackupImportResult(
        mode=mode,
        content_states_upserted=len(backup.data.content_states),
        checklist_instances_upserted=len(backup.data.checklist_instances),
        checklist_items_upserted=sum(
            len(instance.items)
            for instance in backup.data.checklist_instances
        ),
        material_inventory_upserted=len(backup.data.material_inventory),
        project_stage_states_upserted=len(backup.data.project_stage_states),
        deleted_counts=deleted_counts,
    )
