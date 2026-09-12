from __future__ import annotations

from datetime import datetime

from fastapi.testclient import TestClient
import pytest
from sqlalchemy import select

from app.database import get_session
from app.knowledge import get_knowledge_content, get_knowledge_project, search_knowledge
from app.main import app
from app.models import (
    ChecklistInstance,
    ChecklistItemState,
    ContentRequirement,
    Project,
    ProjectStage,
    UserContentState,
    UserMaterialInventory,
    UserProjectStageState,
)
from app.periods import KST


FIXED_NOW = datetime(2026, 9, 9, 12, tzinfo=KST)


def _client(session):
    def override_session():
        yield session

    app.dependency_overrides[get_session] = override_session
    return TestClient(app)


def _personal_state_snapshot(session) -> dict[str, list[tuple[object, ...]]]:
    return {
        "checklist_instances": [
            (row.id, row.template_id, row.period_key, row.period_start, row.period_end)
            for row in session.scalars(select(ChecklistInstance).order_by(ChecklistInstance.id))
        ],
        "checklist_items": [
            (row.id, row.completed, row.completed_at, row.note)
            for row in session.scalars(select(ChecklistItemState).order_by(ChecklistItemState.id))
        ],
        "content_state": [
            (row.id, row.content_id, row.state, row.priority, row.note, row.updated_at)
            for row in session.scalars(select(UserContentState).order_by(UserContentState.id))
        ],
        "inventory": [
            (row.id, row.material_id, row.quantity, row.note, row.updated_at)
            for row in session.scalars(
                select(UserMaterialInventory).order_by(UserMaterialInventory.id)
            )
        ],
        "project_stage_state": [
            (row.id, row.stage_id, row.completed, row.completed_at, row.note, row.updated_at)
            for row in session.scalars(
                select(UserProjectStageState).order_by(UserProjectStageState.id)
            )
        ],
    }


def test_content_knowledge_api_returns_canonical_detail_without_personal_state(session) -> None:
    client = _client(session)
    try:
        response = client.get("/api/knowledge/contents/blood-altar")
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert response.status_code == 200
    detail = response.json()
    assert detail["slug"] == "blood-altar"
    assert detail["requirements"]
    assert detail["schedules"]
    assert detail["rewards"]
    assert detail["sources"]
    assert detail["related_contents"]
    assert "user_state" not in detail
    assert "checklists" not in detail


def test_content_knowledge_service_and_api_are_side_effect_free(session) -> None:
    before = _personal_state_snapshot(session)
    detail = get_knowledge_content(session, "blood-altar", FIXED_NOW)
    assert detail is not None

    client = _client(session)
    try:
        assert client.get("/api/knowledge/contents/blood-altar").status_code == 200
        assert client.get("/api/knowledge/projects/carrack-advance").status_code == 200
        assert client.get("/api/knowledge/search", params={"q": "피의 제단"}).status_code == 200
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert _personal_state_snapshot(session) == before


def test_project_knowledge_api_returns_only_canonical_definition(session) -> None:
    client = _client(session)
    try:
        response = client.get("/api/knowledge/projects/carrack-advance")
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert response.status_code == 200
    detail = response.json()
    assert detail["slug"] == "carrack-advance"
    assert detail["stages"][3]["dependencies"] == [
        "carrack-advance.stage.blue-gear",
        "carrack-advance.stage.body-materials",
    ]
    material = next(
        item for item in detail["materials"] if item["material_key"] == "moon-vein-flax"
    )
    assert material["required_quantity"] == 180
    assert material["sources"]
    assert {"owned_quantity", "shortage", "inventory_note", "inventory_updated_at"}.isdisjoint(
        material
    )
    assert all(
        {"id", "completed", "completed_at", "note"}.isdisjoint(stage)
        for stage in detail["stages"]
    )


def test_project_knowledge_is_independent_of_local_inventory_and_stage_state(session) -> None:
    before = get_knowledge_project(session, "carrack-advance")
    assert before is not None
    project = session.scalar(select(Project).where(Project.slug == "carrack-advance"))
    stage = session.scalar(
        select(ProjectStage)
        .where(ProjectStage.project_id == project.id)
        .order_by(ProjectStage.order_no)
    )

    client = _client(session)
    try:
        inventory_response = client.put(
            "/api/materials/moon-vein-flax/inventory",
            json={"quantity": 90, "note": "canonical response must ignore this"},
        )
        stage_response = client.put(
            f"/api/projects/carrack-advance/stages/{stage.id}/state",
            json={"completed": True, "note": "local completion"},
        )
        after_response = client.get("/api/knowledge/projects/carrack-advance")
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert inventory_response.status_code == 200
    assert stage_response.status_code == 200
    assert after_response.status_code == 200
    assert after_response.json() == before.model_dump(mode="json")


@pytest.mark.parametrize(
    ("query", "resource_type", "slug"),
    [
        ("피의 제단", "content", "blood-altar"),
        ("blood-altar", "content", "blood-altar"),
        ("에페리아 중범선 : 점진", "project", "carrack-advance"),
    ],
)
def test_search_resolves_content_and_project_identity(
    session, query, resource_type, slug
) -> None:
    results = search_knowledge(session, query)
    result = next(
        item
        for item in results
        if item.resource_type == resource_type and item.slug == slug
    )
    assert result.matches[0].field in {
        "content.name_ko",
        "content.slug",
        "project.name_ko",
    }

@pytest.mark.parametrize(
    ("query", "field"),
    [
        ("3인 콘텐츠", "requirement.description"),
        ("주간 최고 기록 보상", "reward.name"),
        ("주간 최고 기록 진행", "step.title"),
        ("체크리스트 초기화", "section.body_markdown"),
        ("party_size", "requirement.structured_value"),
    ],
)
def test_search_finds_nested_content_knowledge(session, query, field) -> None:
    result = next(
        item
        for item in search_knowledge(session, query, limit=50)
        if item.slug == "blood-altar"
    )
    assert result.resource_type == "content"
    assert any(match.field == field for match in result.matches)


def test_search_finds_project_by_material_name_and_key(session) -> None:
    by_name = search_knowledge(session, "달의 핏줄이 새겨진 아마포")
    by_key = search_knowledge(session, "moon-vein-flax")

    assert by_name[0].resource_type == "material"
    assert by_name[0].slug == "moon-vein-flax"
    assert by_name[0].matches[0].field == "material.name_ko"
    assert by_key[0].resource_type == "material"
    assert by_key[0].slug == "moon-vein-flax"
    assert by_key[0].matches[0].field == "material.key"
    assert any(
        item.resource_type == "project" and item.slug == "carrack-advance"
        for item in by_key
    )


def test_search_ranking_dedup_and_order_are_deterministic(session) -> None:
    exact_first = search_knowledge(session, "피의 제단", limit=50)
    first = search_knowledge(session, "주간", limit=50)
    second = search_knowledge(session, "주간", limit=50)

    assert exact_first[0].slug == "blood-altar"
    assert first == second
    identities = [(item.resource_type, item.slug) for item in first]
    assert len(identities) == len(set(identities))
    assert identities.count(("content", "blood-altar")) == 1
    blood_altar = next(item for item in first if item.slug == "blood-altar")
    assert len(blood_altar.matches) <= 3

    archived = session.scalar(
        select(ContentRequirement).where(
            ContentRequirement.seed_key == "blood-altar.party-size"
        )
    )
    archived.description = "archive-only-search-needle"
    archived.active = False
    session.commit()
    assert all(
        item.slug != "blood-altar"
        for item in search_knowledge(session, "archive-only-search-needle", limit=50)
    )


@pytest.mark.parametrize(
    ("params", "expected_status"),
    [
        ({}, 422),
        ({"q": ""}, 422),
        ({"q": "   "}, 422),
        ({"q": "피의 제단", "limit": 0}, 422),
        ({"q": "피의 제단", "limit": 51}, 422),
        ({"q": "x" * 201}, 422),
    ],
)
def test_search_api_validation(session, params, expected_status) -> None:
    client = _client(session)
    try:
        response = client.get("/api/knowledge/search", params=params)
    finally:
        app.dependency_overrides.clear()
        client.close()
    assert response.status_code == expected_status


def test_search_service_validates_blank_query_and_limit(session) -> None:
    with pytest.raises(ValueError, match="must not be blank"):
        search_knowledge(session, " \t\n")
    with pytest.raises(ValueError, match="between 1 and 50"):
        search_knowledge(session, "피의 제단", limit=0)


def test_existing_content_and_project_detail_contracts_remain_personal(session) -> None:
    client = _client(session)
    try:
        content_response = client.get("/api/contents/blood-altar")
        project_response = client.get("/api/projects/carrack-advance")
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert content_response.status_code == 200
    assert {"user_state", "checklists"}.issubset(content_response.json())
    project = project_response.json()
    assert project_response.status_code == 200
    assert {"completed", "completed_at", "note"}.issubset(project["stages"][0])
    assert {
        "owned_quantity",
        "shortage",
        "inventory_note",
        "inventory_updated_at",
    }.issubset(project["materials"][0])
