from __future__ import annotations

from math import inf, nan

from fastapi.testclient import TestClient
from pydantic import ValidationError
import pytest
from sqlalchemy import select

from app.database import get_session
from app.knowledge import get_knowledge_project
from app.main import app
from app.models import (
    ChecklistInstance,
    ChecklistItemState,
    Material,
    Project,
    ProjectMaterial,
    UserContentState,
    UserMaterialInventory,
    UserProjectStageState,
)
from app.project_calculations import calculate_shortage
from app.projects import get_project_detail, put_material_inventory
from app.schemas import MaterialInventoryUpdate, ProjectCalculationRequest


def _client(session):
    def override_session():
        yield session

    app.dependency_overrides[get_session] = override_session
    return TestClient(app)


def _post(session, payload: dict[str, object], slug: str = "carrack-advance"):
    client = _client(session)
    try:
        return client.post(f"/api/calculations/projects/{slug}", json=payload)
    finally:
        app.dependency_overrides.clear()
        client.close()


def _material(response, material_key: str):
    return next(
        item for item in response.json()["materials"] if item["material_key"] == material_key
    )


def _table_snapshot(session, model):
    return [
        tuple(row.__dict__[column.name] for column in model.__table__.columns)
        for row in session.scalars(select(model))
    ]


@pytest.mark.parametrize(
    ("provided", "expected"),
    [(0, 180), (75, 105), (200, 0)],
)
def test_calculate_shortage_is_pure_and_clamped(provided, expected) -> None:
    assert calculate_shortage(180, provided) == expected


def test_stateless_project_calculation_uses_only_caller_inventory(session) -> None:
    response = _post(
        session,
        {"inventory": [{"material_key": "moon-vein-flax", "quantity": 75}]},
    )

    assert response.status_code == 200
    material = _material(response, "moon-vein-flax")
    assert material["required_quantity"] == 180
    assert material["provided_quantity"] == 75
    assert material["shortage"] == 105
    assert material["satisfied"] is False
    assert response.json()["summary"] == {
        "material_requirement_count": 9,
        "satisfied_requirement_count": 0,
        "shortage_requirement_count": 9,
        "all_requirements_satisfied": False,
    }


def test_stateless_project_calculation_clamps_excess_inventory(session) -> None:
    response = _post(
        session,
        {"inventory": [{"material_key": "moon-vein-flax", "quantity": 200}]},
    )

    material = _material(response, "moon-vein-flax")
    assert material["shortage"] == 0
    assert material["satisfied"] is True


def test_missing_inventory_defaults_every_requirement_to_zero(session) -> None:
    response = _post(session, {"inventory": []})

    assert response.status_code == 200
    for material in response.json()["materials"]:
        assert material["provided_quantity"] == 0
        assert material["shortage"] == material["required_quantity"]


def test_unknown_material_keys_are_rejected_in_sorted_order(session) -> None:
    response = _post(
        session,
        {
            "inventory": [
                {"material_key": "z-not-in-project", "quantity": 1},
                {"material_key": "a-not-in-project", "quantity": 1},
            ]
        },
    )

    assert response.status_code == 422
    assert response.json() == {
        "detail": "Unknown project material keys: a-not-in-project, z-not-in-project"
    }


def test_duplicate_material_keys_are_rejected(session) -> None:
    response = _post(
        session,
        {
            "inventory": [
                {"material_key": "moon-vein-flax", "quantity": 10},
                {"material_key": "moon-vein-flax", "quantity": 20},
            ]
        },
    )

    assert response.status_code == 422
    assert "Duplicate material keys: moon-vein-flax" in response.text


def test_negative_quantity_is_rejected(session) -> None:
    response = _post(
        session,
        {"inventory": [{"material_key": "moon-vein-flax", "quantity": -1}]},
    )
    assert response.status_code == 422


@pytest.mark.parametrize("quantity", [nan, inf, -inf])
def test_non_finite_quantity_is_rejected(quantity) -> None:
    with pytest.raises(ValidationError):
        ProjectCalculationRequest.model_validate(
            {"inventory": [{"material_key": "moon-vein-flax", "quantity": quantity}]}
        )


def test_unknown_project_returns_404(session) -> None:
    response = _post(session, {"inventory": []}, slug="not-found")
    assert response.status_code == 404
    assert response.json() == {"detail": "Project not found"}


def test_result_preserves_canonical_project_material_order_and_row_identity(session) -> None:
    project = get_knowledge_project(session, "carrack-advance")
    response = _post(session, {"inventory": []})

    assert project is not None
    assert response.status_code == 200
    assert [item["project_material_seed_key"] for item in response.json()["materials"]] == [
        item.seed_key for item in project.materials
    ]


def test_calculation_does_not_mutate_personal_or_canonical_tables(session) -> None:
    models = (
        UserMaterialInventory,
        UserProjectStageState,
        UserContentState,
        ChecklistInstance,
        ChecklistItemState,
        Project,
        Material,
        ProjectMaterial,
    )
    before = {model: _table_snapshot(session, model) for model in models}

    response = _post(
        session,
        {"inventory": [{"material_key": "moon-vein-flax", "quantity": 75}]},
    )

    assert response.status_code == 200
    after = {model: _table_snapshot(session, model) for model in models}
    assert after == before


def test_local_inventory_is_never_a_stateless_fallback(session) -> None:
    before = _post(session, {"inventory": []}).json()
    put_material_inventory(
        session,
        "moon-vein-flax",
        MaterialInventoryUpdate(quantity=100, note="local only"),
    )
    after = _post(session, {"inventory": []}).json()

    assert after == before
    assert (
        _material(_post(session, {"inventory": []}), "moon-vein-flax")[
            "provided_quantity"
        ]
        == 0
    )


def test_only_caller_input_changes_stateless_shortage(session) -> None:
    zero = _material(
        _post(
            session,
            {"inventory": [{"material_key": "moon-vein-flax", "quantity": 0}]},
        ),
        "moon-vein-flax",
    )
    seventy_five = _material(
        _post(
            session,
            {"inventory": [{"material_key": "moon-vein-flax", "quantity": 75}]},
        ),
        "moon-vein-flax",
    )

    assert zero["shortage"] == 180
    assert seventy_five["shortage"] == 105


@pytest.mark.parametrize("quantity", [0, 75, 200])
def test_local_tracker_and_stateless_calculator_have_shortage_parity(
    session, quantity
) -> None:
    put_material_inventory(
        session,
        "moon-vein-flax",
        MaterialInventoryUpdate(quantity=quantity, note=None),
    )
    local = get_project_detail(session, "carrack-advance")
    stateless = _post(
        session,
        {"inventory": [{"material_key": "moon-vein-flax", "quantity": quantity}]},
    )

    assert local is not None
    local_material = next(
        item for item in local.materials if item.material_key == "moon-vein-flax"
    )
    assert _material(stateless, "moon-vein-flax")["shortage"] == local_material.shortage


def test_inactive_material_requirements_are_excluded(session) -> None:
    project_material = session.scalar(
        select(ProjectMaterial).where(
            ProjectMaterial.seed_key == "carrack-advance.material.moon-vein-flax"
        )
    )
    assert project_material is not None
    project_material.active = False
    session.commit()

    response = _post(
        session,
        {"inventory": [{"material_key": "moon-vein-flax", "quantity": 1}]},
    )

    assert response.status_code == 422
    assert response.json() == {
        "detail": "Unknown project material keys: moon-vein-flax"
    }


def test_repeated_material_rows_share_caller_quantity_but_keep_row_identity(
    session,
) -> None:
    source_row = session.scalar(
        select(ProjectMaterial).where(
            ProjectMaterial.seed_key == "carrack-advance.material.moon-vein-flax"
        )
    )
    assert source_row is not None
    repeated = ProjectMaterial(
        project_id=source_row.project_id,
        stage_id=source_row.stage_id,
        material_id=source_row.material_id,
        seed_key="carrack-advance.material.moon-vein-flax-repeat",
        required_quantity=50,
        order_no=source_row.order_no + 1,
        active=True,
    )
    session.add(repeated)
    session.commit()

    response = _post(
        session,
        {"inventory": [{"material_key": "moon-vein-flax", "quantity": 20}]},
    )
    matching = [
        item
        for item in response.json()["materials"]
        if item["material_key"] == "moon-vein-flax"
    ]

    assert [item["project_material_seed_key"] for item in matching] == [
        "carrack-advance.material.moon-vein-flax",
        "carrack-advance.material.moon-vein-flax-repeat",
    ]
    assert [item["provided_quantity"] for item in matching] == [20, 20]
    assert [item["shortage"] for item in matching] == [160, 30]
    assert response.json()["summary"]["material_requirement_count"] == 10
