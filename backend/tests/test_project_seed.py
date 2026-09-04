from __future__ import annotations

from datetime import UTC, datetime
import json
from pathlib import Path
import shutil

import pytest
from sqlalchemy import func, select

from app.models import (
    Content,
    ContentRelation,
    ContentRequirement,
    Evidence,
    Material,
    Project,
    ProjectMaterial,
    ProjectMaterialSource,
    ProjectStage,
    ProjectStageDependency,
    Reward,
    Source,
    UserMaterialInventory,
    UserProjectStageState,
)
from app.seed import import_seed


DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def _seed_copy(tmp_path: Path) -> Path:
    target = tmp_path / "data"
    shutil.copytree(DATA_DIR, target)
    return target


def _project_payload(path: Path) -> dict:
    return json.loads((path / "seed_projects.json").read_text(encoding="utf-8"))


def _save_project_payload(path: Path, payload: dict) -> None:
    (path / "seed_projects.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def test_carrack_project_seed_shape_and_existing_baseline(session) -> None:
    expected_counts = {
        Project: 1,
        ProjectStage: 4,
        ProjectStageDependency: 4,
        Material: 9,
        ProjectMaterial: 9,
        ProjectMaterialSource: 9,
    }
    for model, expected in expected_counts.items():
        assert session.scalar(select(func.count()).select_from(model)) == expected

    project = session.scalar(select(Project).where(Project.slug == "carrack-advance"))
    assert project.content.slug == "carrack-advance"
    assert project.active is True
    assert session.scalar(select(func.count()).select_from(Source)) == 145
    assert session.scalar(select(func.count()).select_from(Content)) == 259
    assert session.scalar(select(func.count()).select_from(Evidence)) == 1237
    assert session.scalar(select(func.count()).select_from(ContentRelation)) == 401


def test_carrack_material_projection_matches_verified_requirement(session) -> None:
    requirement = session.scalar(
        select(ContentRequirement).where(
            ContentRequirement.seed_key == "carrack-advance.requirement.body-materials"
        )
    )
    body_stage = session.scalar(
        select(ProjectStage).where(
            ProjectStage.seed_key == "carrack-advance.stage.body-materials"
        )
    )
    projected = session.scalars(
        select(ProjectMaterial).where(
            ProjectMaterial.stage_id == body_stage.id,
            ProjectMaterial.active.is_(True),
        )
    ).all()
    assert {item.material.name_ko: item.required_quantity for item in projected} == {
        name: float(quantity) for name, quantity in requirement.structured_value.items()
    }
    assert all(item.source_entity_seed_key == requirement.seed_key for item in projected)
    assert session.scalar(
        select(func.count())
        .select_from(Evidence)
        .where(
            Evidence.entity_id == requirement.seed_key,
            Evidence.verification_status == "verified",
            Evidence.active.is_(True),
        )
    ) >= 1
    for item in projected:
        for source in item.sources:
            if source.quantity_per_completion is None:
                continue
            reward = session.scalar(
                select(Reward).where(
                    Reward.content_id == source.content_id,
                    Reward.name == item.material.name_ko,
                    Reward.active.is_(True),
                )
            )
            assert reward is not None
            assert source.quantity_per_completion == reward.amount

    gear_stage = session.scalar(
        select(ProjectStage).where(ProjectStage.seed_key == "carrack-advance.stage.blue-gear")
    )
    gear_requirement = session.scalar(
        select(ContentRequirement).where(
            ContentRequirement.seed_key == "carrack-advance.requirement.blue-gear-plus10"
        )
    )
    gear_items = session.scalars(
        select(ProjectMaterial).where(
            ProjectMaterial.stage_id == gear_stage.id,
            ProjectMaterial.active.is_(True),
        )
    ).all()
    assert len(gear_items) == gear_requirement.structured_value["count"] == 4
    assert all(item.required_quantity == 1 for item in gear_items)
    assert all(item.source_entity_seed_key == gear_requirement.seed_key for item in gear_items)


def test_three_imports_preserve_ids_and_user_owned_state(session) -> None:
    project = session.scalar(select(Project).where(Project.slug == "carrack-advance"))
    stage = session.scalar(select(ProjectStage).order_by(ProjectStage.order_no))
    material = session.scalar(select(Material).where(Material.key == "moon-vein-flax"))
    canonical_models = (Project, ProjectStage, ProjectStageDependency, Material, ProjectMaterial, ProjectMaterialSource)
    before_counts = tuple(session.scalar(select(func.count()).select_from(model)) for model in canonical_models)
    before_ids = {
        Project: tuple(session.scalars(select(Project.id).order_by(Project.id))),
        ProjectStage: tuple(session.scalars(select(ProjectStage.id).order_by(ProjectStage.id))),
        ProjectStageDependency: tuple(
            session.scalars(select(ProjectStageDependency.id).order_by(ProjectStageDependency.id))
        ),
        Material: tuple(session.scalars(select(Material.id).order_by(Material.id))),
        ProjectMaterial: tuple(session.scalars(select(ProjectMaterial.id).order_by(ProjectMaterial.id))),
        ProjectMaterialSource: tuple(
            session.scalars(select(ProjectMaterialSource.id).order_by(ProjectMaterialSource.id))
        ),
    }
    inventory = UserMaterialInventory(
        material_id=material.id,
        quantity=37,
        note="사용자 재고",
        updated_at=datetime(2026, 9, 5, 1, tzinfo=UTC),
    )
    stage_state = UserProjectStageState(
        stage_id=stage.id,
        completed=True,
        completed_at=datetime(2026, 9, 5, 2, tzinfo=UTC),
        note="사용자 완료",
        updated_at=datetime(2026, 9, 5, 2, tzinfo=UTC),
    )
    session.add_all([inventory, stage_state])
    session.commit()
    user_ids = (inventory.id, stage_state.id)
    completed_at = stage_state.completed_at

    for _ in range(3):
        import_seed(session, DATA_DIR)

    assert tuple(session.scalar(select(func.count()).select_from(model)) for model in canonical_models) == before_counts
    assert tuple(session.scalars(select(Project.id).order_by(Project.id))) == before_ids[Project]
    assert tuple(session.scalars(select(ProjectStage.id).order_by(ProjectStage.id))) == before_ids[ProjectStage]
    assert tuple(
        session.scalars(select(ProjectStageDependency.id).order_by(ProjectStageDependency.id))
    ) == before_ids[ProjectStageDependency]
    assert tuple(session.scalars(select(Material.id).order_by(Material.id))) == before_ids[Material]
    assert tuple(session.scalars(select(ProjectMaterial.id).order_by(ProjectMaterial.id))) == before_ids[ProjectMaterial]
    assert tuple(
        session.scalars(select(ProjectMaterialSource.id).order_by(ProjectMaterialSource.id))
    ) == before_ids[ProjectMaterialSource]
    session.refresh(inventory)
    session.refresh(stage_state)
    assert (inventory.id, stage_state.id) == user_ids
    assert (inventory.quantity, inventory.note) == (37, "사용자 재고")
    assert (stage_state.completed, stage_state.note) == (True, "사용자 완료")
    restored_completed_at = (
        stage_state.completed_at.replace(tzinfo=UTC)
        if stage_state.completed_at.tzinfo is None
        else stage_state.completed_at
    )
    assert restored_completed_at == completed_at
    assert project.active is True


def test_removed_canonical_row_is_archived_without_touching_user_state(session, tmp_path) -> None:
    item = session.scalar(
        select(ProjectMaterial).where(
            ProjectMaterial.seed_key
            == "carrack-advance.material.moon-vein-flax"
        )
    )
    stage = session.get(ProjectStage, item.stage_id)
    inventory = UserMaterialInventory(
        material_id=item.material_id,
        quantity=1,
        note="보존 재고",
        updated_at=datetime(2026, 9, 5, tzinfo=UTC),
    )
    state = UserProjectStageState(
        stage_id=stage.id,
        completed=True,
        completed_at=datetime(2026, 9, 5, tzinfo=UTC),
        note="보존 단계",
        updated_at=datetime(2026, 9, 5, tzinfo=UTC),
    )
    session.add_all([inventory, state])
    session.commit()
    item_id, inventory_id, state_id = item.id, inventory.id, state.id
    source_ids = [source.id for source in item.sources]

    data_dir = _seed_copy(tmp_path)
    payload = _project_payload(data_dir)
    payload["projects"][0]["project_materials"] = [
        row
        for row in payload["projects"][0]["project_materials"]
        if row["seed_key"] != item.seed_key
    ]
    _save_project_payload(data_dir, payload)
    import_seed(session, data_dir)

    assert session.get(ProjectMaterial, item_id).active is False
    assert source_ids
    assert all(session.get(ProjectMaterialSource, source_id).active is False for source_id in source_ids)
    assert session.get(UserMaterialInventory, inventory_id).quantity == 1
    assert session.get(UserMaterialInventory, inventory_id).note == "보존 재고"
    assert session.get(UserProjectStageState, state_id).completed is True
    assert session.get(UserProjectStageState, state_id).note == "보존 단계"


def test_missing_optional_project_file_skips_project_sync(session, tmp_path) -> None:
    data_dir = tmp_path / "legacy-data"
    data_dir.mkdir()
    shutil.copy(DATA_DIR / "seed_sources.json", data_dir / "seed_sources.json")
    shutil.copy(DATA_DIR / "seed_contents.json", data_dir / "seed_contents.json")
    before_id = session.scalar(select(Project.id).where(Project.slug == "carrack-advance"))
    import_seed(session, data_dir)
    project = session.get(Project, before_id)
    assert project.slug == "carrack-advance"
    assert project.active is True


@pytest.mark.parametrize(
    "invalid_case",
    [
        "duplicate-material",
        "duplicate-project",
        "unknown-content",
        "unknown-stage",
        "unknown-source-entity",
        "dag-cycle",
    ],
)
def test_project_seed_rejects_invalid_identity_or_reference(
    session, tmp_path, invalid_case
) -> None:
    data_dir = _seed_copy(tmp_path)
    payload = _project_payload(data_dir)
    project = payload["projects"][0]
    if invalid_case == "duplicate-material":
        payload["materials"].append(dict(payload["materials"][0]))
    elif invalid_case == "duplicate-project":
        payload["projects"].append(dict(project))
    elif invalid_case == "unknown-content":
        project["content_slug"] = "missing-content"
    elif invalid_case == "unknown-stage":
        project["project_materials"][0]["stage_seed_key"] = "carrack-advance.stage.missing"
    elif invalid_case == "unknown-source-entity":
        project["project_materials"][0]["source_entity_seed_key"] = "carrack-advance.missing"
    else:
        project["stage_dependencies"].append(
            {
                "seed_key": "carrack-advance.dependency.base-upgrade",
                "stage_seed_key": "carrack-advance.stage.base-ship",
                "depends_on_stage_seed_key": "carrack-advance.stage.upgrade",
            }
        )
    _save_project_payload(data_dir, payload)

    with pytest.raises(ValueError):
        import_seed(session, data_dir)
    session.rollback()


def test_current_project_seed_has_no_unexpected_archives(session) -> None:
    for model in (
        Project,
        ProjectStage,
        ProjectStageDependency,
        Material,
        ProjectMaterial,
        ProjectMaterialSource,
    ):
        assert session.scalar(
            select(func.count()).select_from(model).where(model.active.is_(False))
        ) == 0
