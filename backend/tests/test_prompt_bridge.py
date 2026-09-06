from datetime import datetime
import socket

from sqlalchemy import select

from app.models import ChecklistItemState, Evidence
from app.main import put_user_content_state
from app.periods import KST
from app.prompt_bridge import build_context, render_markdown, render_result
from app.schemas import PromptMode, PromptRequest, UserContentStateUpdate, UserContentStateValue


FIXED_NOW = datetime(2026, 9, 2, 23, 0, tzinfo=KST)


def test_content_prompt_is_deterministic_and_source_aware(session) -> None:
    request = PromptRequest(
        mode=PromptMode.CONTENT_ONBOARDING,
        content_slug="garmoth",
        user_question="처음 무엇을 준비해야 해?",
        as_of=FIXED_NOW,
    )
    first = render_markdown(build_context(session, request, FIXED_NOW))
    second = render_markdown(build_context(session, request, FIXED_NOW))
    assert first == second
    assert "## VERIFIED_KNOWLEDGE" in first
    assert "## CANONICAL_FACTS" not in first
    assert "verification: verified" in first
    assert "월드 우두머리 레이드" in first
    assert "처음 무엇을 준비해야 해?" in first


def test_unresolved_claim_is_separated_from_verified_facts(session) -> None:
    evidence = session.scalar(select(Evidence).where(Evidence.entity_id == "garmoth"))
    evidence.verification_status = "conflict"
    session.commit()
    request = PromptRequest(mode=PromptMode.CONTENT_ONBOARDING, content_slug="garmoth", as_of=FIXED_NOW)
    bundle = build_context(session, request, FIXED_NOW)
    assert all(item.verification_status == "verified" for item in bundle.canonical_facts)
    assert any(
        item.verification_status == "conflict"
        for item in bundle.open_questions_or_conflicts
    )
    markdown = render_markdown(bundle)
    open_section = markdown.split("## OPEN_QUESTIONS_OR_CONFLICTS", 1)[1].split("## SOURCES", 1)[0]
    assert "verification: conflict" in open_section


def test_weekly_prompt_contains_completed_and_incomplete_state(session) -> None:
    request = PromptRequest(mode=PromptMode.WEEKLY_REVIEW, as_of=FIXED_NOW)
    first_bundle = build_context(session, request, FIXED_NOW)
    state_id = session.scalar(select(ChecklistItemState.id))
    state = session.get(ChecklistItemState, state_id)
    state.completed = True
    session.commit()
    bundle = build_context(session, request, FIXED_NOW)
    assert any(item.completed for item in bundle.checklist)
    assert any(not item.completed for item in bundle.checklist)
    markdown = render_markdown(bundle)
    assert "- [x]" in markdown
    assert "- [ ]" in markdown
    assert len(first_bundle.checklist) == len(bundle.checklist)


def test_prompt_generation_attempts_no_outbound_network(session, monkeypatch) -> None:
    def blocked_connect(*_args, **_kwargs):
        raise AssertionError("outbound network attempted")

    monkeypatch.setattr(socket.socket, "connect", blocked_connect)
    request = PromptRequest(mode=PromptMode.WEEKLY_REVIEW, user_question="무엇부터 할까?", as_of=FIXED_NOW)
    result = render_result(build_context(session, request, FIXED_NOW))
    assert result.markdown.endswith("무엇부터 할까?\n")
    assert result.estimated_tokens > 0
    assert result.over_budget is False


def test_content_onboarding_includes_structured_knowledge_and_personal_state(session) -> None:
    put_user_content_state(
        "blood-altar",
        UserContentStateUpdate(
            state=UserContentStateValue.FOUNDATION,
            priority=1,
            note="파티원 모집 전",
        ),
        session,
    )
    request = PromptRequest(
        mode=PromptMode.CONTENT_ONBOARDING,
        content_slug="blood-altar",
        user_question="이번 주 어떻게 시작할까?",
        as_of=FIXED_NOW,
    )
    markdown = render_markdown(build_context(session, request, FIXED_NOW))
    assert "## REQUIREMENTS" in markdown
    assert "3인 콘텐츠" in markdown
    assert "## STEPS" in markdown
    assert "주간 최고 기록 진행" in markdown
    assert "## REWARDS" in markdown
    assert "주간 최고 기록 보상" in markdown
    assert "[verified] reward_payout" in markdown
    assert "## WARNINGS" in markdown
    assert "보상 지급은 체크리스트 초기화" in markdown
    assert "content_state: foundation" in markdown
    assert "note: 파티원 모집 전" in markdown
