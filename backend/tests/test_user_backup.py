from __future__ import annotations

from copy import deepcopy
from datetime import UTC, datetime, timedelta
from typing import Any

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import func, select
from sqlalchemy.orm import selectinload

from app.database import get_session
from app.main import app
from app.models import (
    ChecklistInstance,
    ChecklistItemState,
    ChecklistTemplate,
    ChecklistTemplateItem,
    Content,
    Evidence,
    Material,
    Project,
    ProjectStage,
    Source,
    UserContentState,
    UserMaterialInventory,
    UserProjectStageState,
)
from app.periods import KST
from app.schemas import UserBackupImportMode
from app.user_backup import (
    UserBackupValidationError,
    export_user_backup,
    import_user_backup,
    validate_user_backup,
)


NOW = datetime(2026, 9, 6, 3, 0, tzinfo=UTC)


def _empty_backup() -> dict[str, Any]:
    return {
        "format": "bdo-companion-user-backup",
        "version": 1,
        "exported_at": NOW.isoformat(),
        "data": {
            "content_states": [],
            "checklist_instances": [],
            "material_inventory": [],
            "project_stage_states": [],
        },
    }


def _content_state(
    slug: str,
    *,
    state: str = "in_progress",
    note: str | None = "복원 메모",
) -> dict[str, Any]:
    return {
        "content_slug": slug,
        "state": state,
        "priority": 2,
        "note": note,
        "updated_at": NOW.isoformat(),
    }


def _template_with_item(session):
    return session.scalar(
        select(ChecklistTemplate)
        .where(ChecklistTemplate.seed_key.is_not(None))
        .options(selectinload(ChecklistTemplate.items))
        .order_by(ChecklistTemplate.seed_key)
    )


def _checklist_payload(session) -> dict[str, Any]:
    template = _template_with_item(session)
    assert template is not None
    item = next(value for value in template.items if value.seed_key)
    return {
        "template_seed_key": template.seed_key,
        "period_key": "W:2026-09-03T00:00:00+09:00",
        "period_start": "2026-09-02T15:00:00+00:00",
        "period_end": "2026-09-09T15:00:00+00:00",
        "generated_at": NOW.isoformat(),
        "items": [
            {
                "item_seed_key": item.seed_key,
                "completed": False,
                "completed_at": None,
                "note": "아직 미완료",
            }
        ],
    }


def _populate_all_user_state(session) -> None:
    contents = list(
        session.scalars(
            select(Content)
            .where(Content.slug.in_(["gathering-current-system", "fishing-current-system"]))
            .order_by(Content.slug.desc())
        ).all()
    )
    for index, content in enumerate(contents):
        session.add(
            UserContentState(
                content_id=content.id,
                state="completed" if index == 0 else "in_progress",
                priority=index + 1,
                note=f"content-{index}",
                updated_at=NOW + timedelta(minutes=index),
            )
        )

    template = _template_with_item(session)
    assert template is not None
    item = next(value for value in template.items if value.seed_key)
    for index, period_key in enumerate(
        ["W:2026-08-27T00:00:00+09:00", "W:2026-09-03T00:00:00+09:00"]
    ):
        start = datetime(2026, 8, 27, tzinfo=KST) + timedelta(days=index * 7)
        instance = ChecklistInstance(
            template_id=template.id,
            period_key=period_key,
            period_start=start,
            period_end=start + timedelta(days=7),
            generated_at=NOW + timedelta(minutes=index),
        )
        session.add(instance)
        session.flush()
        session.add(
            ChecklistItemState(
                instance_id=instance.id,
                template_item_id=item.id,
                completed=index == 0,
                completed_at=NOW if index == 0 else None,
                note="완료 기록" if index == 0 else "미완료 기록",
            )
        )

    material = session.scalar(select(Material).where(Material.key == "moon-vein-flax"))
    assert material is not None
    session.add(
        UserMaterialInventory(
            material_id=material.id,
            quantity=123,
            note="창고 포함",
            updated_at=NOW,
        )
    )

    project = session.scalar(select(Project).where(Project.slug == "carrack-advance"))
    assert project is not None
    stage = session.scalar(
        select(ProjectStage)
        .where(ProjectStage.project_id == project.id)
        .order_by(ProjectStage.order_no)
    )
    assert stage is not None
    session.add(
        UserProjectStageState(
            stage_id=stage.id,
            completed=True,
            completed_at=NOW,
            note="단계 완료",
            updated_at=NOW,
        )
    )
    session.commit()


def _client(session) -> TestClient:
    def override_session():
        yield session

    app.dependency_overrides[get_session] = override_session
    return TestClient(app)


def _all_keys(value: Any) -> set[str]:
    if isinstance(value, dict):
        return set(value) | {
            key
            for child in value.values()
            for key in _all_keys(child)
        }
    if isinstance(value, list):
        return {key for child in value for key in _all_keys(child)}
    return set()


def _canonical_counts(session) -> dict[str, int]:
    return {
        "sources": session.scalar(select(func.count()).select_from(Source)) or 0,
        "contents": session.scalar(select(func.count()).select_from(Content)) or 0,
        "evidence": session.scalar(select(func.count()).select_from(Evidence)) or 0,
        "checklist_templates": (
            session.scalar(select(func.count()).select_from(ChecklistTemplate)) or 0
        ),
        "checklist_template_items": (
            session.scalar(select(func.count()).select_from(ChecklistTemplateItem)) or 0
        ),
        "projects": session.scalar(select(func.count()).select_from(Project)) or 0,
        "project_stages": (
            session.scalar(select(func.count()).select_from(ProjectStage)) or 0
        ),
        "materials": session.scalar(select(func.count()).select_from(Material)) or 0,
    }


def test_empty_user_database_exports_versioned_envelope(session) -> None:
    backup = export_user_backup(session, exported_at=NOW)

    assert backup.format == "bdo-companion-user-backup"
    assert backup.version == 1
    assert backup.exported_at == NOW
    assert backup.data.model_dump() == {
        "content_states": [],
        "checklist_instances": [],
        "material_inventory": [],
        "project_stage_states": [],
    }


def test_export_preserves_all_user_state_history_and_portable_identity(session) -> None:
    _populate_all_user_state(session)

    backup = export_user_backup(session, exported_at=NOW)
    payload = backup.model_dump(mode="json")

    assert [row["content_slug"] for row in payload["data"]["content_states"]] == [
        "fishing-current-system",
        "gathering-current-system",
    ]
    assert len(payload["data"]["checklist_instances"]) == 2
    assert [row["period_key"] for row in payload["data"]["checklist_instances"]] == [
        "W:2026-08-27T00:00:00+09:00",
        "W:2026-09-03T00:00:00+09:00",
    ]
    assert payload["data"]["checklist_instances"][0]["items"][0] == {
        "item_seed_key": payload["data"]["checklist_instances"][0]["items"][0][
            "item_seed_key"
        ],
        "completed": True,
        "completed_at": "2026-09-06T03:00:00Z",
        "note": "완료 기록",
    }
    assert payload["data"]["checklist_instances"][1]["items"][0][
        "completed"
    ] is False
    assert payload["data"]["material_inventory"][0]["material_key"] == "moon-vein-flax"
    assert payload["data"]["project_stage_states"][0]["stage_seed_key"].startswith(
        "carrack-advance.stage."
    )
    forbidden = {
        "id",
        "content_id",
        "template_id",
        "template_item_id",
        "material_id",
        "project_id",
        "stage_id",
        "shortage",
        "sources",
        "evidence",
    }
    assert not (_all_keys(payload) & forbidden)
    assert payload["exported_at"].endswith("Z")
    assert payload["data"]["checklist_instances"][0]["period_start"].endswith("Z")


def test_export_data_order_is_deterministic_when_export_time_changes(session) -> None:
    _populate_all_user_state(session)

    first = export_user_backup(session, exported_at=NOW)
    second = export_user_backup(session, exported_at=NOW + timedelta(days=1))

    assert first.exported_at != second.exported_at
    assert first.data.model_dump(mode="json") == second.data.model_dump(mode="json")


def test_export_rejects_checklist_history_without_stable_key(session) -> None:
    template = _template_with_item(session)
    assert template is not None
    instance = ChecklistInstance(
        template_id=template.id,
        period_key="legacy",
        period_start=NOW,
        period_end=NOW + timedelta(days=1),
        generated_at=NOW,
    )
    session.add(instance)
    session.flush()
    template.seed_key = None
    session.flush()

    with pytest.raises(ValueError, match="no stable seed_key"):
        export_user_backup(session)


@pytest.mark.parametrize(
    ("mutate", "expected_error"),
    [
        (lambda payload: payload.update(format="other"), "unsupported backup format"),
        (lambda payload: payload.update(version=2), "unsupported backup version"),
        (
            lambda payload: payload["data"]["content_states"].append(
                _content_state("unknown-content")
            ),
            "unknown content_slug: unknown-content",
        ),
        (
            lambda payload: payload["data"]["material_inventory"].append(
                {
                    "material_key": "unknown-material",
                    "quantity": 1,
                    "note": None,
                    "updated_at": NOW.isoformat(),
                }
            ),
            "unknown material_key: unknown-material",
        ),
        (
            lambda payload: payload["data"]["project_stage_states"].append(
                {
                    "project_slug": "carrack-advance",
                    "stage_seed_key": "carrack-advance.stage.unknown",
                    "completed": False,
                    "completed_at": None,
                    "note": None,
                    "updated_at": NOW.isoformat(),
                }
            ),
            "unknown project stage",
        ),
        (
            lambda payload: payload["data"]["content_states"].extend(
                [_content_state("garmoth"), _content_state("garmoth")]
            ),
            "duplicate content_slug: garmoth",
        ),
        (
            lambda payload: payload["data"]["material_inventory"].append(
                {
                    "material_key": "moon-vein-flax",
                    "quantity": -1,
                    "note": None,
                    "updated_at": NOW.isoformat(),
                }
            ),
            "greater than or equal to 0",
        ),
        (
            lambda payload: payload["data"]["content_states"].append(
                {
                    **_content_state("garmoth"),
                    "updated_at": "2026-09-06T03:00:00",
                }
            ),
            "datetime must be timezone-aware",
        ),
    ],
)
def test_validation_rejects_invalid_payloads(session, mutate, expected_error) -> None:
    payload = _empty_backup()
    mutate(payload)

    report, _ = validate_user_backup(session, payload)

    assert report.valid is False
    assert any(expected_error in error for error in report.errors)


def test_validation_rejects_invalid_period_and_duplicate_nested_identity(session) -> None:
    payload = _empty_backup()
    instance = _checklist_payload(session)
    instance["period_end"] = instance["period_start"]
    instance["items"].append(deepcopy(instance["items"][0]))
    payload["data"]["checklist_instances"] = [instance, deepcopy(instance)]

    report, _ = validate_user_backup(session, payload)

    assert report.valid is False
    assert any("invalid checklist period range" in error for error in report.errors)
    assert any("duplicate item_seed_key" in error for error in report.errors)
    assert any("duplicate checklist instance" in error for error in report.errors)


def test_validation_rejects_duplicate_material_and_project_stage_identity(session) -> None:
    payload = _empty_backup()
    inventory = {
        "material_key": "moon-vein-flax",
        "quantity": 1,
        "note": None,
        "updated_at": NOW.isoformat(),
    }
    stage = {
        "project_slug": "carrack-advance",
        "stage_seed_key": "carrack-advance.stage.base-ship",
        "completed": False,
        "completed_at": None,
        "note": None,
        "updated_at": NOW.isoformat(),
    }
    payload["data"]["material_inventory"] = [inventory, deepcopy(inventory)]
    payload["data"]["project_stage_states"] = [stage, deepcopy(stage)]

    report, _ = validate_user_backup(session, payload)

    assert report.valid is False
    assert any("duplicate material_key" in error for error in report.errors)
    assert any("duplicate project stage" in error for error in report.errors)


def test_validation_rejects_item_from_a_different_template(session) -> None:
    templates = list(
        session.scalars(
            select(ChecklistTemplate)
            .where(ChecklistTemplate.seed_key.is_not(None))
            .options(selectinload(ChecklistTemplate.items))
            .order_by(ChecklistTemplate.seed_key)
        ).all()
    )
    first = next(item for item in templates if any(child.seed_key for child in item.items))
    foreign_item = next(
        child
        for template in templates
        if template.id != first.id
        for child in template.items
        if child.seed_key
        and all(own.seed_key != child.seed_key for own in first.items)
    )
    payload = _empty_backup()
    instance = _checklist_payload(session)
    instance["template_seed_key"] = first.seed_key
    instance["items"][0]["item_seed_key"] = foreign_item.seed_key
    payload["data"]["checklist_instances"] = [instance]

    report, _ = validate_user_backup(session, payload)

    assert report.valid is False
    assert any("unknown checklist item for template" in error for error in report.errors)


def test_archived_canonical_identity_resolves_without_reactivation(session) -> None:
    content = session.scalar(select(Content).where(Content.slug == "garmoth"))
    assert content is not None
    content.status = "deprecated"
    session.flush()
    payload = _empty_backup()
    payload["data"]["content_states"] = [_content_state("garmoth")]

    report, _ = validate_user_backup(session, payload)
    result = import_user_backup(session, payload, UserBackupImportMode.MERGE)

    assert report.valid is True
    assert report.warnings == ["archived content resolved: garmoth"]
    assert result.content_states_upserted == 1
    assert content.status == "deprecated"


def test_archived_checklist_material_and_project_identities_resolve(session) -> None:
    template = _template_with_item(session)
    assert template is not None
    item = next(value for value in template.items if value.seed_key)
    material = session.scalar(select(Material).where(Material.key == "moon-vein-flax"))
    project = session.scalar(select(Project).where(Project.slug == "carrack-advance"))
    assert material is not None
    assert project is not None
    stage = session.scalar(
        select(ProjectStage).where(
            ProjectStage.project_id == project.id,
            ProjectStage.seed_key == "carrack-advance.stage.base-ship",
        )
    )
    assert stage is not None
    template.active = False
    item.active = False
    material.active = False
    project.active = False
    stage.active = False
    session.flush()
    payload = _empty_backup()
    payload["data"]["checklist_instances"] = [_checklist_payload(session)]
    payload["data"]["material_inventory"] = [{
        "material_key": material.key,
        "quantity": 5,
        "note": None,
        "updated_at": NOW.isoformat(),
    }]
    payload["data"]["project_stage_states"] = [{
        "project_slug": project.slug,
        "stage_seed_key": stage.seed_key,
        "completed": True,
        "completed_at": NOW.isoformat(),
        "note": None,
        "updated_at": NOW.isoformat(),
    }]

    report, _ = validate_user_backup(session, payload)
    import_user_backup(session, payload, UserBackupImportMode.REPLACE)

    assert report.valid is True
    assert any("archived checklist template" in item for item in report.warnings)
    assert any("archived checklist item" in item for item in report.warnings)
    assert any("archived material" in item for item in report.warnings)
    assert any("archived project stage" in item for item in report.warnings)
    assert template.active is False
    assert item.active is False
    assert material.active is False
    assert project.active is False
    assert stage.active is False


def test_replace_round_trip_restores_exact_semantic_data(session) -> None:
    _populate_all_user_state(session)
    original = export_user_backup(session, exported_at=NOW)

    session.query(ChecklistItemState).delete()
    session.query(ChecklistInstance).delete()
    session.query(UserContentState).delete()
    session.query(UserMaterialInventory).delete()
    session.query(UserProjectStageState).delete()
    session.commit()

    result = import_user_backup(
        session,
        original.model_dump(mode="json"),
        UserBackupImportMode.REPLACE,
    )
    restored = export_user_backup(session, exported_at=NOW + timedelta(days=1))

    assert result.mode == UserBackupImportMode.REPLACE
    assert original.data.model_dump(mode="json") == restored.data.model_dump(mode="json")


def test_merge_overwrites_referenced_state_preserves_local_only_and_is_idempotent(session) -> None:
    garmoth = session.scalar(select(Content).where(Content.slug == "garmoth"))
    fishing = session.scalar(
        select(Content).where(Content.slug == "fishing-current-system")
    )
    assert garmoth is not None
    assert fishing is not None
    session.add_all(
        [
            UserContentState(
                content_id=garmoth.id,
                state="not_started",
                note="old",
                updated_at=NOW - timedelta(days=1),
            ),
            UserContentState(
                content_id=fishing.id,
                state="paused",
                note="local-only",
                updated_at=NOW,
            ),
        ]
    )
    session.commit()
    payload = _empty_backup()
    payload["data"]["content_states"] = [
        _content_state("garmoth", state="completed", note="backup-wins")
    ]

    import_user_backup(session, payload, UserBackupImportMode.MERGE)
    import_user_backup(session, payload, UserBackupImportMode.MERGE)

    rows = {
        content.slug: state
        for state, content in session.execute(
            select(UserContentState, Content).join(Content)
        ).all()
    }
    assert len(rows) == 2
    assert rows["garmoth"].state == "completed"
    assert rows["garmoth"].note == "backup-wins"
    assert rows["fishing-current-system"].state == "paused"
    assert rows["fishing-current-system"].note == "local-only"


def test_replace_removes_user_data_missing_from_backup(session) -> None:
    _populate_all_user_state(session)
    payload = _empty_backup()
    payload["data"]["content_states"] = [_content_state("garmoth")]

    result = import_user_backup(session, payload, UserBackupImportMode.REPLACE)

    assert result.deleted_counts.content_states == 2
    assert result.deleted_counts.checklist_instances == 2
    assert session.scalar(select(func.count()).select_from(UserContentState)) == 1
    assert session.scalar(select(func.count()).select_from(ChecklistInstance)) == 0
    assert session.scalar(select(func.count()).select_from(UserMaterialInventory)) == 0
    assert session.scalar(select(func.count()).select_from(UserProjectStageState)) == 0


def test_invalid_import_is_atomic_and_preserves_existing_user_state(session) -> None:
    content = session.scalar(select(Content).where(Content.slug == "garmoth"))
    assert content is not None
    session.add(
        UserContentState(
            content_id=content.id,
            state="paused",
            priority=5,
            note="must survive",
            updated_at=NOW,
        )
    )
    session.commit()
    payload = _empty_backup()
    payload["data"]["content_states"] = [
        _content_state("garmoth", state="completed"),
        _content_state("missing-content"),
    ]

    with pytest.raises(UserBackupValidationError):
        import_user_backup(session, payload, UserBackupImportMode.REPLACE)

    session.expire_all()
    state = session.scalar(
        select(UserContentState).where(UserContentState.content_id == content.id)
    )
    assert state is not None
    assert state.state == "paused"
    assert state.note == "must survive"


def test_import_does_not_mutate_canonical_counts_or_stable_identities(session) -> None:
    before_counts = _canonical_counts(session)
    before_identity = {
        "sources": tuple(session.scalars(select(Source.id).order_by(Source.id)).all()),
        "contents": tuple(session.scalars(select(Content.slug).order_by(Content.slug)).all()),
        "evidence": tuple(session.scalars(select(Evidence.id).order_by(Evidence.id)).all()),
        "templates": tuple(
            session.scalars(
                select(ChecklistTemplate.seed_key).order_by(ChecklistTemplate.id)
            ).all()
        ),
        "projects": tuple(session.scalars(select(Project.slug).order_by(Project.slug)).all()),
        "stages": tuple(
            session.scalars(select(ProjectStage.seed_key).order_by(ProjectStage.id)).all()
        ),
        "materials": tuple(
            session.scalars(select(Material.key).order_by(Material.key)).all()
        ),
    }
    payload = _empty_backup()
    payload["data"]["content_states"] = [_content_state("garmoth")]
    payload["data"]["checklist_instances"] = [_checklist_payload(session)]
    payload["data"]["material_inventory"] = [
        {
            "material_key": "moon-vein-flax",
            "quantity": 7,
            "note": None,
            "updated_at": NOW.isoformat(),
        }
    ]
    payload["data"]["project_stage_states"] = [
        {
            "project_slug": "carrack-advance",
            "stage_seed_key": "carrack-advance.stage.base-ship",
            "completed": True,
            "completed_at": NOW.isoformat(),
            "note": None,
            "updated_at": NOW.isoformat(),
        }
    ]

    import_user_backup(session, payload, UserBackupImportMode.REPLACE)

    after_identity = {
        "sources": tuple(session.scalars(select(Source.id).order_by(Source.id)).all()),
        "contents": tuple(session.scalars(select(Content.slug).order_by(Content.slug)).all()),
        "evidence": tuple(session.scalars(select(Evidence.id).order_by(Evidence.id)).all()),
        "templates": tuple(
            session.scalars(
                select(ChecklistTemplate.seed_key).order_by(ChecklistTemplate.id)
            ).all()
        ),
        "projects": tuple(session.scalars(select(Project.slug).order_by(Project.slug)).all()),
        "stages": tuple(
            session.scalars(select(ProjectStage.seed_key).order_by(ProjectStage.id)).all()
        ),
        "materials": tuple(
            session.scalars(select(Material.key).order_by(Material.key)).all()
        ),
    }
    assert _canonical_counts(session) == before_counts
    assert after_identity == before_identity


def test_backup_api_exports_validates_imports_and_rejects_invalid_payload(session) -> None:
    client = _client(session)
    try:
        exported = client.get("/api/settings/backup")
        valid = client.post(
            "/api/settings/backup/validate",
            json=exported.json(),
        )
        imported = client.post(
            "/api/settings/backup/import",
            json={"backup": exported.json(), "mode": "merge"},
        )
        payload = exported.json()
        payload["data"]["content_states"] = [_content_state("missing-content")]
        invalid = client.post(
            "/api/settings/backup/import",
            json={"backup": payload, "mode": "merge"},
        )
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert exported.status_code == 200
    assert valid.status_code == 200
    assert valid.json()["valid"] is True
    assert imported.status_code == 200
    assert imported.json()["mode"] == "merge"
    assert invalid.status_code == 422
    assert invalid.json()["detail"]["valid"] is False
    assert any(
        "missing-content" in error
        for error in invalid.json()["detail"]["errors"]
    )
