from __future__ import annotations

from datetime import UTC, datetime

from fastapi.testclient import TestClient
from sqlalchemy import select

from app.database import get_session
from app.life import get_life_hub, get_life_skill
from app.main import app
from app.models import Content, UserContentState


EXPECTED_SKILLS = [
    "gathering",
    "fishing",
    "farming",
    "processing",
    "cooking",
    "alchemy",
    "training",
    "hunting",
    "sailing",
    "barter",
]


def _client(session) -> TestClient:
    def override_session():
        yield session

    app.dependency_overrides[get_session] = override_session
    return TestClient(app)


def _detail_slugs(detail) -> list[str]:
    return [
        item.slug
        for section_name in (
            "foundation_contents",
            "getting_started",
            "equipment",
            "core_systems",
            "recurring_contents",
            "advanced_contents",
            "related_economy",
        )
        for item in getattr(detail, section_name)
    ]


def test_life_hub_discovers_canonical_skills_foundations_and_economy(session) -> None:
    hub = get_life_hub(session)

    assert [skill.key for skill in hub.skills] == EXPECTED_SKILLS
    assert {
        "life-family-levels",
        "life-mastery-foundation",
        "life-common-gear",
        "life-accessory-progression",
        "life-mastery-tools",
        "life-artifacts-lightstones",
        "life-alchemy-stones",
        "cheongmyeong-orb",
        "energy-foundation",
    } == {item.slug for item in hub.foundations}
    economy_slugs = {item.slug for item in hub.economy_contents}
    assert {
        "contribution-economy-foundation",
        "node-network-current-system",
        "production-node-current-system",
        "worker-current-system",
        "storage-current-system",
        "royal-workshop-current-system",
    } <= economy_slugs


def test_gathering_fishing_and_sailing_use_existing_content_taxonomy(session) -> None:
    gathering = get_life_skill(session, "gathering")
    fishing = get_life_skill(session, "fishing")
    sailing = get_life_skill(session, "sailing")

    assert gathering is not None
    assert fishing is not None
    assert sailing is not None
    assert gathering.entry_content_slug == "gathering-current-system"
    assert "gathering-tools" in _detail_slugs(gathering)
    assert fishing.entry_content_slug == "fishing-current-system"
    assert "imperial-fishing-delivery" in _detail_slugs(fishing)
    assert sailing.entry_content_slug == "carrack-types"
    assert {"sailor-hiring-growth", "panokseon", "carrack-advance"} <= set(
        _detail_slugs(sailing)
    )


def test_each_skill_has_unique_active_content_and_preserves_canonical_verification(session) -> None:
    for skill_key in EXPECTED_SKILLS:
        detail = get_life_skill(session, skill_key)
        assert detail is not None
        slugs = _detail_slugs(detail)
        assert len(slugs) == len(set(slugs))
        assert len(slugs) == detail.content_count

    gathering = get_life_skill(session, "gathering")
    assert gathering is not None
    assert gathering.verification_status == "verified"
    assert gathering.last_verified_at.isoformat() == "2026-09-03"


def test_inactive_content_is_excluded_without_creating_an_empty_skill(session) -> None:
    content = session.scalar(
        select(Content).where(Content.slug == "gathering-special-drops")
    )
    assert content is not None
    content.status = "deprecated"
    session.commit()

    gathering = get_life_skill(session, "gathering")

    assert gathering is not None
    assert "gathering-special-drops" not in _detail_slugs(gathering)
    assert gathering.content_count > 0


def test_progress_uses_user_content_state_and_excludes_ignore_from_tracked_total(session) -> None:
    states = {
        "gathering-current-system": "completed",
        "gathering-tools": "in_progress",
        "energy-foundation": "ignore",
    }
    for slug, state in states.items():
        content = session.scalar(select(Content).where(Content.slug == slug))
        assert content is not None
        session.add(
            UserContentState(
                content_id=content.id,
                state=state,
                updated_at=datetime(2026, 9, 5, tzinfo=UTC),
            )
        )
    session.commit()

    hub = get_life_hub(session)
    gathering = next(item for item in hub.skills if item.key == "gathering")

    assert gathering.user_progress.completed == 1
    assert gathering.user_progress.in_progress == 1
    assert gathering.user_progress.ignored == 1
    assert gathering.user_progress.tracked == gathering.user_progress.total - 1
    assert gathering.user_progress.not_started == gathering.user_progress.total - 3


def test_related_projects_follow_active_project_content_relationship(session) -> None:
    sailing = get_life_skill(session, "sailing")
    barter = get_life_skill(session, "barter")

    assert sailing is not None
    assert barter is not None
    assert [project.slug for project in sailing.related_projects] == ["carrack-advance"]
    assert [project.slug for project in barter.related_projects] == ["carrack-advance"]


def test_life_api_returns_hub_detail_and_unknown_skill_404(session) -> None:
    client = _client(session)
    try:
        hub_response = client.get("/api/life")
        detail_response = client.get("/api/life/gathering")
        missing_response = client.get("/api/life/not-a-skill")
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert hub_response.status_code == 200
    assert [item["key"] for item in hub_response.json()["skills"]] == EXPECTED_SKILLS
    assert detail_response.status_code == 200
    assert detail_response.json()["entry_content_slug"] == "gathering-current-system"
    assert missing_response.status_code == 404
    assert missing_response.json()["detail"] == "Life skill not found"
