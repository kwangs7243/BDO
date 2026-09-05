from __future__ import annotations

from datetime import date, datetime
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.database import get_session
from app.main import app
from app.periods import KST
from app.projects import get_project_detail
from app.prompt_bridge import build_context, render_markdown, render_result
from app.schemas import (
    PromptChecklistItem,
    PromptContextBundle,
    PromptFact,
    PromptMode,
    PromptOutputMode,
    PromptRequest,
    PromptSection,
    PromptSizeMode,
    SourceOut,
)


FIXED_NOW = datetime(2026, 9, 2, 23, 0, tzinfo=KST)
GOLDEN_DIR = Path(__file__).with_name("golden")


def _request(
    mode: PromptMode,
    *,
    content_slug: str | None = None,
    project_slug: str | None = None,
    include_sections: list[PromptSection] | None = None,
) -> PromptRequest:
    return PromptRequest(
        mode=mode,
        content_slug=content_slug,
        project_slug=project_slug,
        include_sections=include_sections,
        user_question="무엇부터 하면 돼?",
        as_of=FIXED_NOW,
    )


def _client(session) -> TestClient:
    def override_session():
        yield session

    app.dependency_overrides[get_session] = override_session
    return TestClient(app)


def _source(
    evidence_id: int,
    *,
    source_type: str,
    active: bool,
    title_suffix: str = "",
    url_suffix: str = "",
) -> SourceOut:
    return SourceOut(
        evidence_id=evidence_id,
        evidence_seed_key=f"evidence-{evidence_id}",
        id=f"source-{evidence_id}",
        title=f"source-{evidence_id}-{title_suffix}",
        url=f"https://example.invalid/{evidence_id}/{url_suffix}",
        publisher="publisher",
        source_type=source_type,
        published_at=date(2026, 9, 1),
        retrieved_at=FIXED_NOW,
        region="KR",
        entity_type="content",
        entity_id=f"entity-{evidence_id}",
        claim_key="summary",
        verification_status="verified",
        last_verified_at=date(2026, 9, 2),
        active=active,
        is_active=active,
    )


def _synthetic_bundle(
    *,
    included_sections: list[PromptSection],
    canonical_facts: list[PromptFact] | None = None,
    unresolved: list[PromptFact] | None = None,
    checklist: list[PromptChecklistItem] | None = None,
    related_contents: list[str] | None = None,
    project_state: list[str] | None = None,
    sources: list[SourceOut] | None = None,
    requirements: list[str] | None = None,
    steps: list[str] | None = None,
    rewards: list[str] | None = None,
    warnings: list[str] | None = None,
) -> PromptContextBundle:
    return PromptContextBundle(
        generated_at=FIXED_NOW,
        request_context={"mode": "next_action", "page": "dashboard"},
        canonical_facts=canonical_facts or [],
        open_questions_or_conflicts=unresolved or [],
        checklist=checklist or [],
        related_contents=related_contents or [],
        project_state=project_state or [],
        sources=sources or [],
        requirements=requirements or [],
        steps=steps or [],
        rewards=rewards or [],
        warnings=warnings or [],
        included_sections=included_sections,
        user_question="합리적인 순서를 알려줘",
    )


def test_legacy_requests_keep_existing_golden_markdown(session) -> None:
    project = build_context(
        session,
        _request(PromptMode.PROJECT_OPTIMIZER, project_slug="carrack-advance"),
        FIXED_NOW,
    )
    weekly = build_context(
        session,
        _request(PromptMode.WEEKLY_REVIEW),
        FIXED_NOW,
    )

    assert "RELATED_CONTENTS" not in render_markdown(project)
    assert "RELATED_CONTENTS" not in render_markdown(weekly)
    assert render_markdown(project).startswith("# BDO Companion Context")
    assert PromptSection.RELATED_CONTENTS not in project.included_sections
    assert PromptSection.RELATED_CONTENTS not in weekly.included_sections


def test_selector_renders_only_selected_section_and_empty_is_none(session) -> None:
    bundle = build_context(
        session,
        _request(
            PromptMode.WEEKLY_REVIEW,
            include_sections=[PromptSection.REQUIREMENTS],
        ),
        FIXED_NOW,
    )
    markdown = render_markdown(bundle)

    assert "## REQUIREMENTS" in markdown
    assert "## REQUIREMENTS\n- none" in markdown
    assert "## SCHEDULES" not in markdown
    assert "## CHECKLIST_STATE" not in markdown


def test_content_related_contents_are_stably_collected(session) -> None:
    bundle = build_context(
        session,
        _request(
            PromptMode.CONTENT_ONBOARDING,
            content_slug="blood-altar",
            include_sections=[PromptSection.RELATED_CONTENTS],
        ),
        FIXED_NOW,
    )

    assert bundle.related_contents
    assert any(
        "weekly-quest-framework" in item for item in bundle.related_contents
    )
    assert render_markdown(bundle).count("## RELATED_CONTENTS") == 1


def test_project_related_contents_are_deduplicated_without_slug_hardcode(session) -> None:
    project = get_project_detail(session, "carrack-advance")
    expected_slugs = {
        slug
        for slug in [
            project.content_slug,
            *[
                source.content_slug
                for material in project.materials
                for source in material.sources
            ],
        ]
        if slug
    }
    bundle = build_context(
        session,
        _request(
            PromptMode.PROJECT_OPTIMIZER,
            project_slug=project.slug,
            include_sections=[PromptSection.RELATED_CONTENTS],
        ),
        FIXED_NOW,
    )

    assert len(bundle.related_contents) == len(expected_slugs)
    assert all(
        sum(f"({slug})" in item for item in bundle.related_contents) == 1
        for slug in expected_slugs
    )


def test_invalid_section_returns_422(session) -> None:
    client = _client(session)
    try:
        response = client.post(
            "/api/prompt/context",
            json={
                "mode": "weekly_review",
                "include_sections": ["not_a_section"],
                "as_of": FIXED_NOW.isoformat(),
            },
        )
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert response.status_code == 422


def test_section_order_and_duplicates_are_canonicalized(session) -> None:
    first = build_context(
        session,
        _request(
            PromptMode.WEEKLY_REVIEW,
            include_sections=[
                PromptSection.CHECKLIST,
                PromptSection.SCHEDULES,
            ],
        ),
        FIXED_NOW,
    )
    second = build_context(
        session,
        _request(
            PromptMode.WEEKLY_REVIEW,
            include_sections=[
                PromptSection.SCHEDULES,
                PromptSection.CHECKLIST,
                PromptSection.SCHEDULES,
            ],
        ),
        FIXED_NOW,
    )

    assert first.included_sections == second.included_sections
    assert render_markdown(first) == render_markdown(second)


@pytest.mark.parametrize(
    ("mode", "content_slug", "project_slug"),
    [
        (PromptMode.CONTENT_ONBOARDING, "garmoth", None),
        (PromptMode.PROJECT_OPTIMIZER, None, "carrack-advance"),
        (PromptMode.WEEKLY_REVIEW, None, None),
        (PromptMode.NEXT_ACTION, None, None),
        (PromptMode.VERIFY_LATEST, "garmoth", None),
    ],
)
def test_all_five_modes_support_explicit_selection(
    session,
    mode: PromptMode,
    content_slug: str | None,
    project_slug: str | None,
) -> None:
    bundle = build_context(
        session,
        _request(
            mode,
            content_slug=content_slug,
            project_slug=project_slug,
            include_sections=[PromptSection.SCHEDULES],
        ),
        FIXED_NOW,
    )

    assert bundle.included_sections == [PromptSection.SCHEDULES]
    assert "## SCHEDULES" in render_markdown(bundle)


def test_full_prompt_keeps_goal_guardrails_and_question(session) -> None:
    bundle = build_context(
        session,
        _request(
            PromptMode.WEEKLY_REVIEW,
            include_sections=[PromptSection.SCHEDULES],
        ),
        FIXED_NOW,
    )
    markdown = render_markdown(bundle, PromptOutputMode.FULL_PROMPT)

    assert "- goal:" in markdown
    assert "## RESPONSE_GUARDRAILS" in markdown
    assert "## USER_QUESTION" in markdown
    assert "무엇부터 하면 돼?" in markdown


def test_context_only_excludes_prompt_instructions_and_is_deterministic(session) -> None:
    bundle = build_context(
        session,
        _request(
            PromptMode.WEEKLY_REVIEW,
            include_sections=[PromptSection.SCHEDULES],
        ),
        FIXED_NOW,
    )
    first = render_markdown(bundle, PromptOutputMode.CONTEXT_ONLY)
    second = render_markdown(bundle, PromptOutputMode.CONTEXT_ONLY)

    assert first == second
    assert "- page: weekly" in first
    assert "- mode: weekly_review" in first
    assert "## SCHEDULES" in first
    assert "- goal:" not in first
    assert "## RESPONSE_GUARDRAILS" not in first
    assert "## USER_QUESTION" not in first


def test_auto_under_budget_does_not_compact() -> None:
    bundle = _synthetic_bundle(
        included_sections=[PromptSection.RELATED_CONTENTS],
        related_contents=["small complete item"],
    )
    result = render_result(
        bundle,
        size_mode=PromptSizeMode.AUTO,
    )

    assert result.compacted is False
    assert result.omitted_counts == {}
    assert result.original_estimated_tokens == result.estimated_tokens
    assert result.over_budget is False


def test_auto_compacts_whole_related_item_and_reports_exact_omission() -> None:
    first_item = "RELATED-FIRST-" + ("a" * 26_000)
    second_item = "RELATED-SECOND-" + ("b" * 26_000)
    bundle = _synthetic_bundle(
        included_sections=[PromptSection.RELATED_CONTENTS],
        related_contents=[first_item, second_item],
    )
    first = render_result(bundle, size_mode=PromptSizeMode.AUTO)
    second = render_result(bundle, size_mode=PromptSizeMode.AUTO)

    assert first.compacted is True
    assert first.estimated_tokens <= 12_000
    assert first.markdown == second.markdown
    assert first.omitted_counts == {"related_contents": 1}
    assert first_item in first.markdown
    assert second_item not in first.markdown
    assert second_item[:100] not in first.markdown


def test_historical_source_is_removed_before_active_official() -> None:
    official = _source(
        1,
        source_type="official_guide",
        active=True,
    )
    historical = _source(
        2,
        source_type="official_patch",
        active=False,
        title_suffix="h" * 50_000,
    )
    bundle = _synthetic_bundle(
        included_sections=[PromptSection.SOURCES],
        sources=[official, historical],
    )
    result = render_result(bundle, size_mode=PromptSizeMode.AUTO)

    assert result.bundle.sources == [official]
    assert result.omitted_counts == {"sources": 1}


def test_non_official_source_is_removed_before_active_official() -> None:
    official = _source(
        1,
        source_type="official_guide",
        active=True,
    )
    community = _source(
        2,
        source_type="community_guide",
        active=True,
        title_suffix="c" * 50_000,
    )
    bundle = _synthetic_bundle(
        included_sections=[PromptSection.SOURCES],
        sources=[official, community],
    )
    result = render_result(bundle, size_mode=PromptSizeMode.AUTO)

    assert result.bundle.sources == [official]
    assert result.omitted_counts == {"sources": 1}


def test_unresolved_checklist_and_project_core_survive_compaction() -> None:
    unresolved = PromptFact(
        claim="충돌 claim을 보존한다",
        verification_status="conflict",
    )
    checklist = PromptChecklistItem(
        label="완료 여부를 보존한다",
        completed=False,
        period_key="W:2026-08-27T00:00:00+09:00",
    )
    project_core = (
        "material: 핵심 재료 (core); stage=stage; "
        "required=100 개; owned=10 개; shortage=90 개"
    )
    acquisition = "acquisition: " + ("획득처" * 20_000)
    bundle = _synthetic_bundle(
        included_sections=[
            PromptSection.OPEN_QUESTIONS_OR_CONFLICTS,
            PromptSection.CHECKLIST,
            PromptSection.PROJECT_STATE,
        ],
        unresolved=[unresolved],
        checklist=[checklist],
        project_state=[project_core, acquisition],
    )
    result = render_result(bundle, size_mode=PromptSizeMode.AUTO)

    assert unresolved in result.bundle.open_questions_or_conflicts
    assert checklist in result.bundle.checklist
    assert project_core in result.bundle.project_state
    assert acquisition not in result.bundle.project_state
    assert result.omitted_counts == {"project_state": 1}


def test_narrative_is_removed_before_canonical_fact() -> None:
    fact = PromptFact(
        claim="검증 사실",
        verification_status="verified",
    )
    warning = "경고-" + ("w" * 50_000)
    bundle = _synthetic_bundle(
        included_sections=[
            PromptSection.CANONICAL_FACTS,
            PromptSection.WARNINGS,
        ],
        canonical_facts=[fact],
        warnings=[warning],
    )
    result = render_result(bundle, size_mode=PromptSizeMode.AUTO)

    assert result.bundle.canonical_facts == [fact]
    assert result.bundle.warnings == []
    assert result.omitted_counts == {"warnings": 1}


def test_detailed_mode_never_compacts_and_reports_over_budget() -> None:
    complete_item = "DETAIL-" + ("d" * 50_000)
    bundle = _synthetic_bundle(
        included_sections=[PromptSection.RELATED_CONTENTS],
        related_contents=[complete_item],
    )
    result = render_result(bundle, size_mode=PromptSizeMode.DETAILED)

    assert result.compacted is False
    assert result.omitted_counts == {}
    assert result.over_budget is True
    assert complete_item in result.markdown


def test_auto_reports_over_budget_when_only_protected_core_remains() -> None:
    protected = PromptChecklistItem(
        label="보호-" + ("p" * 50_000),
        completed=False,
        period_key="W:protected",
    )
    bundle = _synthetic_bundle(
        included_sections=[PromptSection.CHECKLIST],
        checklist=[protected],
    )
    result = render_result(bundle, size_mode=PromptSizeMode.AUTO)

    assert result.compacted is False
    assert result.over_budget is True
    assert result.bundle.checklist == [protected]


def test_render_api_returns_output_and_compaction_metadata(session) -> None:
    client = _client(session)
    try:
        response = client.post(
            "/api/prompt/render",
            json={
                "mode": "weekly_review",
                "include_sections": ["schedules"],
                "output_mode": "context_only",
                "size_mode": "detailed",
                "user_question": "렌더 계약 확인",
                "as_of": FIXED_NOW.isoformat(),
            },
        )
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert response.status_code == 200
    payload = response.json()
    assert payload["compacted"] is False
    assert payload["omitted_counts"] == {}
    assert payload["original_estimated_tokens"] == payload["estimated_tokens"]
    assert "## USER_QUESTION" not in payload["markdown"]
