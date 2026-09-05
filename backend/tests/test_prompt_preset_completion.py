from __future__ import annotations

from datetime import datetime
from pathlib import Path
import socket

from fastapi.testclient import TestClient
from sqlalchemy import select

from app.database import get_session
from app.content import get_content_detail
from app.main import app
from app.models import ChecklistItemState, Evidence
from app.periods import KST
from app.projects import get_project_detail
from app.prompt_bridge import build_context, render_markdown, render_result
from app.schemas import PromptMode, PromptRequest


FIXED_NOW = datetime(2026, 9, 2, 23, 0, tzinfo=KST)
WEEKLY_GOLDEN_PATH = Path(__file__).with_name("golden") / "weekly_review.md"


def _client(session) -> TestClient:
    def override_session():
        yield session

    app.dependency_overrides[get_session] = override_session
    return TestClient(app)


def _request(
    mode: PromptMode,
    *,
    content_slug: str | None = None,
    project_slug: str | None = None,
    user_question: str = "",
) -> PromptRequest:
    return PromptRequest(
        mode=mode,
        content_slug=content_slug,
        project_slug=project_slug,
        user_question=user_question,
        as_of=FIXED_NOW,
    )


def test_next_action_global_contains_daily_and_weekly_current_state(session) -> None:
    request = _request(
        PromptMode.NEXT_ACTION,
        user_question="지금 내 상태에서 무엇부터 하면 돼?",
    )
    initial = build_context(session, request, FIXED_NOW)
    first_state = session.scalar(
        select(ChecklistItemState).order_by(ChecklistItemState.id)
    )
    first_state.completed = True
    session.commit()

    bundle = build_context(session, request, FIXED_NOW)
    markdown = render_markdown(bundle)

    assert initial.request_context["page"] == "dashboard"
    assert bundle.request_context["mode"] == "next_action"
    assert any(item.label.startswith("[daily]") for item in bundle.checklist)
    assert any(item.label.startswith("[weekly]") for item in bundle.checklist)
    assert any(item.completed for item in bundle.checklist)
    assert any(not item.completed for item in bundle.checklist)
    assert "매일 00:00 KST" in markdown
    assert "목요일 00:00 KST" in markdown
    assert "- [x]" in markdown
    assert "- [ ]" in markdown


def test_next_action_content_reuses_complete_content_context(session) -> None:
    target = build_context(
        session,
        _request(PromptMode.NEXT_ACTION, content_slug="garmoth"),
        FIXED_NOW,
    )
    onboarding = build_context(
        session,
        _request(PromptMode.CONTENT_ONBOARDING, content_slug="garmoth"),
        FIXED_NOW,
    )

    assert target.request_context["page"] == "content/garmoth"
    assert target.user_state == onboarding.user_state
    assert target.requirements == onboarding.requirements
    assert target.steps == onboarding.steps
    assert target.schedules == onboarding.schedules
    assert target.checklist == onboarding.checklist
    assert target.canonical_facts == onboarding.canonical_facts
    assert target.open_questions_or_conflicts == onboarding.open_questions_or_conflicts
    assert target.sources == onboarding.sources


def test_next_action_project_uses_backend_shortage_without_recalculation(session) -> None:
    project = get_project_detail(session, "carrack-advance")
    material = next(
        item for item in project.materials if item.material_key == "moon-vein-flax"
    )
    bundle = build_context(
        session,
        _request(PromptMode.NEXT_ACTION, project_slug=project.slug),
        FIXED_NOW,
    )

    assert bundle.request_context["page"] == "project/carrack-advance"
    assert any(
        item.startswith(f"material: {material.name_ko} ({material.material_key});")
        and f"shortage={material.shortage:g} {material.unit}" in item
        for item in bundle.project_state
    )


def test_next_action_rejects_two_targets(session) -> None:
    client = _client(session)
    try:
        response = client.post(
            "/api/prompt/context",
            json={
                "mode": "next_action",
                "content_slug": "garmoth",
                "project_slug": "carrack-advance",
                "as_of": FIXED_NOW.isoformat(),
            },
        )
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert response.status_code == 422
    assert response.json()["detail"] == "next_action accepts only one target"


def test_verify_latest_requires_exactly_one_target(session) -> None:
    client = _client(session)
    try:
        missing = client.post(
            "/api/prompt/context",
            json={"mode": "verify_latest", "as_of": FIXED_NOW.isoformat()},
        )
        both = client.post(
            "/api/prompt/context",
            json={
                "mode": "verify_latest",
                "content_slug": "garmoth",
                "project_slug": "carrack-advance",
                "as_of": FIXED_NOW.isoformat(),
            },
        )
    finally:
        app.dependency_overrides.clear()
        client.close()

    expected = "verify_latest requires exactly one content_slug or project_slug"
    assert missing.status_code == 422
    assert missing.json()["detail"] == expected
    assert both.status_code == 422
    assert both.json()["detail"] == expected


def test_verify_latest_returns_target_specific_not_found(session) -> None:
    client = _client(session)
    try:
        content = client.post(
            "/api/prompt/context",
            json={
                "mode": "verify_latest",
                "content_slug": "unknown-content",
                "as_of": FIXED_NOW.isoformat(),
            },
        )
        project = client.post(
            "/api/prompt/context",
            json={
                "mode": "verify_latest",
                "project_slug": "unknown-project",
                "as_of": FIXED_NOW.isoformat(),
            },
        )
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert content.status_code == 404
    assert content.json()["detail"] == "Content not found: unknown-content"
    assert project.status_code == 404
    assert project.json()["detail"] == "Project not found: unknown-project"


def test_verify_latest_content_conflict_is_open_not_canonical(session) -> None:
    evidence = session.scalar(
        select(Evidence).where(
            Evidence.entity_id == "garmoth",
            Evidence.active.is_(True),
        )
    )
    evidence.verification_status = "conflict"
    session.commit()
    detail = get_content_detail(session, "garmoth", FIXED_NOW)
    target_claim = (
        detail.summary if evidence.claim_key == "summary" else detail.purpose
    )

    bundle = build_context(
        session,
        _request(PromptMode.VERIFY_LATEST, content_slug="garmoth"),
        FIXED_NOW,
    )

    assert target_claim is not None
    assert not any(item.claim == target_claim for item in bundle.canonical_facts)
    assert any(
        item.claim == target_claim
        and item.verification_status == "conflict"
        for item in bundle.open_questions_or_conflicts
    )


def test_verify_latest_project_structured_conflict_is_open_not_canonical(session) -> None:
    project = get_project_detail(session, "carrack-advance")
    material = next(
        item for item in project.materials if item.material_key == "moon-vein-flax"
    )
    evidence = session.scalar(
        select(Evidence).where(
            Evidence.entity_id == material.source_entity_seed_key,
            Evidence.claim_key == "structured_value",
            Evidence.active.is_(True),
        )
    )
    evidence.verification_status = "conflict"
    session.commit()

    bundle = build_context(
        session,
        _request(PromptMode.VERIFY_LATEST, project_slug=project.slug),
        FIXED_NOW,
    )
    target = f"{material.name_ko} project requirement:"

    assert not any(item.claim.startswith(target) for item in bundle.canonical_facts)
    assert any(
        item.claim.startswith(target) and item.verification_status == "conflict"
        for item in bundle.open_questions_or_conflicts
    )


def test_verify_latest_verified_target_does_not_invent_conflict(session) -> None:
    bundle = build_context(
        session,
        _request(PromptMode.VERIFY_LATEST, content_slug="garmoth"),
        FIXED_NOW,
    )
    markdown = render_markdown(bundle)

    assert bundle.canonical_facts
    assert not any(
        item.verification_status == "conflict"
        for item in bundle.open_questions_or_conflicts
    )
    if not bundle.open_questions_or_conflicts:
        assert "현재 저장된 정보에서 재검증이 필요한 항목이 없다." in markdown


def test_new_presets_attempt_no_outbound_network(session, monkeypatch) -> None:
    def blocked_connect(*_args, **_kwargs):
        raise AssertionError("outbound network attempted")

    monkeypatch.setattr(socket.socket, "connect", blocked_connect)
    requests = [
        _request(PromptMode.NEXT_ACTION),
        _request(PromptMode.NEXT_ACTION, content_slug="garmoth"),
        _request(PromptMode.NEXT_ACTION, project_slug="carrack-advance"),
        _request(PromptMode.VERIFY_LATEST, content_slug="garmoth"),
        _request(PromptMode.VERIFY_LATEST, project_slug="carrack-advance"),
    ]

    for request in requests:
        assert render_result(build_context(session, request, FIXED_NOW)).markdown


def test_weekly_review_matches_fixed_golden(session) -> None:
    request = _request(
        PromptMode.WEEKLY_REVIEW,
        user_question="이번 주 남은 일의 우선순위를 정해줘",
    )
    build_context(session, request, FIXED_NOW)
    first_state = session.scalar(
        select(ChecklistItemState).order_by(ChecklistItemState.id)
    )
    first_state.completed = True
    session.commit()

    markdown = render_markdown(build_context(session, request, FIXED_NOW))

    assert "- mode: weekly_review" in markdown
    assert FIXED_NOW.isoformat() in markdown
    assert "목요일 00:00 KST" in markdown
    assert "- [x]" in markdown
    assert "- [ ]" in markdown
    assert "이번 주 남은 일의 우선순위를 정해줘" in markdown
    assert "## RESPONSE_GUARDRAILS" in markdown
    assert markdown == WEEKLY_GOLDEN_PATH.read_text(encoding="utf-8")
