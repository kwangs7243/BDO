from __future__ import annotations

from datetime import datetime

import pytest
from sqlalchemy import select

from app import prompt_bridge
from app.content import get_content_detail
from app.models import Content, Evidence
from app.periods import KST
from app.prompt_bridge import (
    _content_default_knowledge_role,
    _estimated_tokens,
    build_context,
    render_markdown,
    render_result,
)
from app.schemas import (
    PromptKnowledgeRole,
    PromptMode,
    PromptOutputMode,
    PromptRequest,
    PromptSection,
)


FIXED_NOW = datetime(2026, 9, 6, 12, tzinfo=KST)
V19C_CONTENT_SLUGS = (
    "gathering-onboarding-strategy",
    "fishing-onboarding-strategy",
    "hunting-onboarding-strategy",
)


def _content_request(slug: str) -> PromptRequest:
    return PromptRequest(
        mode=PromptMode.CONTENT_ONBOARDING,
        content_slug=slug,
        as_of=FIXED_NOW,
    )


def _all_knowledge(bundle):
    return [*bundle.canonical_facts, *bundle.open_questions_or_conflicts]


@pytest.mark.parametrize("slug", V19C_CONTENT_SLUGS)
def test_v19c_content_defaults_every_supported_claim_to_strategy(session, slug) -> None:
    detail = get_content_detail(session, slug, FIXED_NOW)
    bundle = build_context(session, _content_request(slug), FIXED_NOW)
    facts = {item.claim: item for item in _all_knowledge(bundle)}

    expected_claims = {
        detail.summary,
        detail.purpose,
        *(item.description for item in detail.requirements),
        *(f"{item.title}: {item.description}" for item in detail.steps),
        *(f"{item.title}: {item.body_markdown}" for item in detail.sections),
    }
    assert expected_claims <= set(facts)
    assert all(
        facts[claim].knowledge_role == PromptKnowledgeRole.STRATEGY
        for claim in expected_claims
    )


def test_factual_content_summary_remains_fact(session) -> None:
    detail = get_content_detail(session, "garmoth", FIXED_NOW)
    evidence = session.scalar(
        select(Evidence).where(
            Evidence.entity_id == "garmoth",
            Evidence.claim_key == "summary",
            Evidence.active.is_(True),
        )
    )
    evidence.source.source_type = "community_strategy"
    session.commit()
    bundle = build_context(session, _content_request("garmoth"), FIXED_NOW)
    fact = next(item for item in _all_knowledge(bundle) if item.claim == detail.summary)
    assert fact.source_type == "community_strategy"
    assert fact.knowledge_role == PromptKnowledgeRole.FACT


def test_measurement_requirement_uses_actual_seed_role(session) -> None:
    slug = "hexe-sanctuary-elvia"
    detail = get_content_detail(session, slug, FIXED_NOW)
    requirement = next(
        item
        for item in detail.requirements
        if item.structured_value.get("knowledge_role") == "measurement"
    )
    bundle = build_context(session, _content_request(slug), FIXED_NOW)
    fact = next(
        item for item in _all_knowledge(bundle) if item.claim == requirement.description
    )
    assert fact.knowledge_role == PromptKnowledgeRole.MEASUREMENT


def test_mixed_requirement_roles_fall_back_to_fact_without_losing_explicit_role(
    session,
) -> None:
    slug = "gathering-onboarding-strategy"
    content = session.scalar(select(Content).where(Content.slug == slug))
    first, second = content.requirements[:2]
    first.structured_value = {**first.structured_value, "knowledge_role": "fact"}
    session.commit()

    detail = get_content_detail(session, slug, FIXED_NOW)
    assert _content_default_knowledge_role(detail.requirements) == PromptKnowledgeRole.FACT
    bundle = build_context(session, _content_request(slug), FIXED_NOW)
    facts = {item.claim: item for item in _all_knowledge(bundle)}
    assert facts[detail.summary].knowledge_role == PromptKnowledgeRole.FACT
    assert facts[first.description].knowledge_role == PromptKnowledgeRole.FACT
    assert facts[second.description].knowledge_role == PromptKnowledgeRole.STRATEGY


def test_unresolved_strategy_claim_preserves_role(session) -> None:
    slug = "gathering-onboarding-strategy"
    detail = get_content_detail(session, slug, FIXED_NOW)
    requirement = detail.requirements[0]
    evidence_rows = list(
        session.scalars(
        select(Evidence).where(
            Evidence.entity_id == requirement.seed_key,
            Evidence.claim_key == "description",
            Evidence.active.is_(True),
        )
        )
    )
    assert evidence_rows
    for evidence in evidence_rows:
        evidence.verification_status = "conflict"
    session.commit()
    session.expire_all()

    bundle = build_context(session, _content_request(slug), FIXED_NOW)
    fact = next(
        item
        for item in bundle.open_questions_or_conflicts
        if item.claim == requirement.description
    )
    assert fact.verification_status == "conflict"
    assert fact.knowledge_role == PromptKnowledgeRole.STRATEGY


def test_project_deterministic_knowledge_remains_fact(session) -> None:
    request = PromptRequest(
        mode=PromptMode.PROJECT_OPTIMIZER,
        project_slug="carrack-advance",
        as_of=FIXED_NOW,
    )
    bundle = build_context(session, request, FIXED_NOW)
    knowledge = _all_knowledge(bundle)
    assert knowledge
    assert all(item.knowledge_role == PromptKnowledgeRole.FACT for item in knowledge)


def test_markdown_uses_verified_knowledge_heading_and_role_metadata(session) -> None:
    bundle = build_context(
        session,
        _content_request("gathering-onboarding-strategy"),
        FIXED_NOW,
    )
    markdown = render_markdown(bundle)
    payload = bundle.model_dump(mode="json")
    assert "## VERIFIED_KNOWLEDGE" in markdown
    assert "## CANONICAL_FACTS" not in markdown
    assert "  - knowledge_role: strategy" in markdown
    assert payload["canonical_facts"][0]["knowledge_role"] == "strategy"


def test_structured_sections_render_role_labels(session) -> None:
    markdown = render_markdown(
        build_context(
            session,
            _content_request("gathering-onboarding-strategy"),
            FIXED_NOW,
        )
    )
    requirements = markdown.split("## REQUIREMENTS", 1)[1].split(
        "## VERIFIED_KNOWLEDGE", 1
    )[0]
    steps = markdown.split("## STEPS", 1)[1].split("## SCHEDULES", 1)[0]
    warnings = markdown.split("## WARNINGS", 1)[1].split("## CHECKLIST_STATE", 1)[0]
    assert "[verified][strategy]" in requirements
    assert "[verified][strategy]" in steps
    assert "[verified][strategy]" in warnings


def test_context_only_keeps_roles_without_response_guardrails(session) -> None:
    bundle = build_context(
        session,
        _content_request("gathering-onboarding-strategy"),
        FIXED_NOW,
    )
    markdown = render_markdown(bundle, PromptOutputMode.CONTEXT_ONLY)
    assert "## RESPONSE_GUARDRAILS" not in markdown
    assert "## VERIFIED_KNOWLEDGE" in markdown
    assert "knowledge_role: strategy" in markdown


def test_full_prompt_warns_against_role_conflation(session) -> None:
    markdown = render_markdown(
        build_context(session, _content_request("garmoth"), FIXED_NOW)
    )
    assert "FACT, STRATEGY, MEASUREMENT" in markdown
    assert "공식 사실처럼 단정하지 마세요" in markdown


def test_prompt_selector_contract_remains_unchanged() -> None:
    assert tuple(item.value for item in PromptSection) == (
        "user_state",
        "requirements",
        "canonical_facts",
        "steps",
        "schedules",
        "rewards",
        "warnings",
        "checklist",
        "related_contents",
        "project_state",
        "open_questions_or_conflicts",
        "sources",
    )


def _oversized_related_bundle(session):
    request = _content_request("gathering-onboarding-strategy")
    bundle = build_context(session, request, FIXED_NOW)
    if PromptSection.RELATED_CONTENTS.value not in bundle.included_sections:
        bundle.included_sections.append(PromptSection.RELATED_CONTENTS.value)
    base_budget = _estimated_tokens(render_markdown(bundle)) + 10
    bundle.related_contents.append("oversized: " + ("x" * 20_000))
    return bundle, base_budget


def test_role_aware_compaction_is_deterministic(session, monkeypatch) -> None:
    bundle, base_budget = _oversized_related_bundle(session)
    monkeypatch.setattr(prompt_bridge, "TOKEN_BUDGET", base_budget)
    first = render_result(bundle)
    second = render_result(bundle)
    assert first.markdown == second.markdown
    assert first.compacted is True
    assert first.omitted_counts == {"related_contents": 1}
    assert "knowledge_role: strategy" in first.markdown


def test_compaction_retains_sources_for_visible_role_aware_knowledge(
    session, monkeypatch
) -> None:
    bundle, base_budget = _oversized_related_bundle(session)
    source_url = next(
        item.source_url for item in bundle.canonical_facts if item.source_url
    )
    monkeypatch.setattr(prompt_bridge, "TOKEN_BUDGET", base_budget)
    result = render_result(bundle)
    assert source_url in result.markdown
