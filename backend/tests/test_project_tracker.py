from __future__ import annotations

from fastapi.testclient import TestClient
import pytest

from app.database import get_session
from app.main import app
from app.projects import (
    get_project_detail,
    list_projects,
    put_material_inventory,
    put_project_stage_state,
)
from app.schemas import MaterialInventoryUpdate, ProjectStageStateUpdate


def _client(session):
    def override_session():
        yield session

    app.dependency_overrides[get_session] = override_session
    return TestClient(app)


def test_project_api_lists_carrack_summary_and_deterministic_detail(session) -> None:
    client = _client(session)
    try:
        summaries = client.get("/api/projects")
        detail_response = client.get("/api/projects/carrack-advance")
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert summaries.status_code == 200
    assert summaries.json() == [
        {
            "slug": "carrack-advance",
            "name_ko": "에페리아 중범선 : 점진",
            "content_slug": "carrack-advance",
            "active": True,
            "completed_stage_count": 0,
            "total_stage_count": 4,
            "shortage_material_count": 9,
        }
    ]
    assert detail_response.status_code == 200
    detail = detail_response.json()
    assert [stage["order_no"] for stage in detail["stages"]] == [1, 2, 3, 4]
    assert detail["stages"][3]["dependencies"] == [
        "carrack-advance.stage.blue-gear",
        "carrack-advance.stage.body-materials",
    ]
    assert [material["stage_seed_key"] for material in detail["materials"][:4]] == [
        "carrack-advance.stage.blue-gear"
    ] * 4
    assert [material["stage_seed_key"] for material in detail["materials"][4:]] == [
        "carrack-advance.stage.body-materials"
    ] * 5


@pytest.mark.parametrize(
    ("owned", "expected"),
    [(0, 180), (75, 105), (200, 0)],
)
def test_shortage_is_required_minus_owned_clamped_at_zero(session, owned, expected) -> None:
    put_material_inventory(
        session,
        "moon-vein-flax",
        MaterialInventoryUpdate(quantity=owned, note="shortage fixture"),
    )
    detail = get_project_detail(session, "carrack-advance")
    material = next(item for item in detail.materials if item.material_key == "moon-vein-flax")
    assert material.required_quantity == 180
    assert material.owned_quantity == owned
    assert material.shortage == expected


def test_negative_inventory_returns_api_validation_error(session) -> None:
    client = _client(session)
    try:
        response = client.put(
            "/api/materials/moon-vein-flax/inventory",
            json={"quantity": -1, "note": "invalid"},
        )
    finally:
        app.dependency_overrides.clear()
        client.close()
    assert response.status_code == 422


def test_project_detail_hydrates_persisted_inventory_note(session) -> None:
    client = _client(session)
    try:
        saved = client.put(
            '/api/materials/moon-vein-flax/inventory',
            json={'quantity': 30, 'note': '이번 주 재고'},
        )
        detail_response = client.get('/api/projects/carrack-advance')
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert saved.status_code == 200
    assert detail_response.status_code == 200
    material = next(
        item
        for item in detail_response.json()['materials']
        if item['material_key'] == 'moon-vein-flax'
    )
    assert material['inventory_note'] == '이번 주 재고'
    assert material['inventory_updated_at'] == saved.json()['updated_at']


def test_stage_completion_sets_utc_timestamp_and_reset_clears_it(session) -> None:
    detail = get_project_detail(session, "carrack-advance")
    stage_id = detail.stages[0].id

    completed = put_project_stage_state(
        session,
        "carrack-advance",
        stage_id,
        ProjectStageStateUpdate(completed=True, note="준비 완료"),
    )
    assert completed.completed is True
    assert completed.completed_at is not None
    assert completed.completed_at.utcoffset().total_seconds() == 0
    assert list_projects(session)[0].completed_stage_count == 1

    reset = put_project_stage_state(
        session,
        "carrack-advance",
        stage_id,
        ProjectStageStateUpdate(completed=False, note="재확인 필요"),
    )
    assert reset.completed is False
    assert reset.completed_at is None
    assert reset.note == "재확인 필요"
