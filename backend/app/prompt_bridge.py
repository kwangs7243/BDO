from __future__ import annotations

from datetime import date, datetime

from sqlalchemy.orm import Session

from app.checklists import get_current_checklists
from app.content import get_content_detail
from app.schemas import (
    PromptChecklistItem,
    PromptContextBundle,
    PromptFact,
    PromptMode,
    PromptRenderOut,
    PromptRequest,
    SourceOut,
)


PRESET_GOALS = {
    PromptMode.CONTENT_ONBOARDING: "이 콘텐츠를 처음 시작하는 사용자가 진입 순서와 반복 루틴을 이해하도록 설명해 주세요.",
    PromptMode.WEEKLY_REVIEW: "남은 주간 항목을 마감과 가치 기준으로 우선순위화해 주세요.",
}

GUARDRAILS = (
    "제공된 verified 데이터를 우선 사용하세요.",
    "날짜나 패치에 따라 달라지는 정보는 최신 KR 공식 자료를 우선 확인하세요.",
    "미검증 값은 추측하지 마세요.",
    "과거 공략과 최신 공식 자료가 충돌하면 최신 공식 자료를 우선하세요.",
    "정확한 수량, 초기화, 보상은 근거 없이 단정하지 마세요.",
    "이미 완료한 항목을 다시 해야 할 일로 추천하지 마세요.",
)


def _evidence_for(sources: list[SourceOut], entity_id: str, claim_key: str) -> SourceOut | None:
    candidates = [
        item
        for item in sources
        if item.entity_id == entity_id and item.claim_key == claim_key and item.is_active
    ]
    return sorted(candidates, key=lambda item: (item.source_type, item.title, item.id))[0] if candidates else None


def _classify_fact(
    *,
    claim: str,
    entity_id: str,
    claim_key: str,
    sources: list[SourceOut],
    fallback_last_verified: date | None,
    verified: list[PromptFact],
    unresolved: list[PromptFact],
) -> str:
    evidence = _evidence_for(sources, entity_id, claim_key)
    status = evidence.verification_status if evidence else "unverified"
    fact = PromptFact(
        claim=claim,
        verification_status=status,
        last_verified_at=evidence.last_verified_at if evidence else fallback_last_verified,
        source_title=evidence.title if evidence else None,
        source_url=evidence.url if evidence else None,
        source_type=evidence.source_type if evidence else None,
    )
    (verified if status == "verified" else unresolved).append(fact)
    return status


def build_context(session: Session, request: PromptRequest, now: datetime) -> PromptContextBundle:
    facts: list[PromptFact] = []
    unresolved: list[PromptFact] = []
    schedules: list[str] = []
    sources: list[SourceOut] = []
    checklist: list[PromptChecklistItem] = []
    requirements: list[str] = []
    steps: list[str] = []
    rewards: list[str] = []
    warnings: list[str] = []
    user_state: list[str] = []
    request_context = {"mode": request.mode.value, "page": "weekly"}

    if request.mode == PromptMode.CONTENT_ONBOARDING:
        if not request.content_slug:
            raise ValueError("content_slug is required for content_onboarding")
        detail = get_content_detail(session, request.content_slug, now)
        if detail is None:
            raise LookupError(request.content_slug)
        request_context["page"] = f"content/{detail.slug}"
        sources = detail.sources

        if detail.summary:
            _classify_fact(
                claim=detail.summary,
                entity_id=detail.slug,
                claim_key="summary",
                sources=sources,
                fallback_last_verified=detail.last_verified_at,
                verified=facts,
                unresolved=unresolved,
            )
        if detail.purpose:
            _classify_fact(
                claim=detail.purpose,
                entity_id=detail.slug,
                claim_key="purpose",
                sources=sources,
                fallback_last_verified=detail.last_verified_at,
                verified=facts,
                unresolved=unresolved,
            )

        user_state.append(f"content_state: {detail.user_state.state.value}")
        if detail.user_state.priority is not None:
            user_state.append(f"priority: {detail.user_state.priority}")
        if detail.user_state.note:
            user_state.append(f"note: {detail.user_state.note}")

        for item in detail.requirements:
            status = _classify_fact(
                claim=item.description,
                entity_id=item.seed_key,
                claim_key="description",
                sources=sources,
                fallback_last_verified=detail.last_verified_at,
                verified=facts,
                unresolved=unresolved,
            )
            requirements.append(
                f"[{status}] {item.requirement_level}/{item.kind}: "
                f"{item.title + ' — ' if item.title else ''}{item.description}"
            )
        for item in detail.steps:
            status = _classify_fact(
                claim=f"{item.title}: {item.description}",
                entity_id=item.seed_key,
                claim_key="description",
                sources=sources,
                fallback_last_verified=detail.last_verified_at,
                verified=facts,
                unresolved=unresolved,
            )
            steps.append(f"[{status}] {item.phase}: {item.title} — {item.description}")
        for item in detail.rewards:
            reward_text = item.name
            if item.recommendation:
                reward_text += f" (recommendation: {item.recommendation})"
            status = _classify_fact(
                claim=reward_text,
                entity_id=item.seed_key,
                claim_key="reward",
                sources=sources,
                fallback_last_verified=detail.last_verified_at,
                verified=facts,
                unresolved=unresolved,
            )
            rewards.append(f"[{status}] {reward_text}")
        for item in detail.sections:
            status = _classify_fact(
                claim=f"{item.title}: {item.body_markdown}",
                entity_id=item.seed_key,
                claim_key="body",
                sources=sources,
                fallback_last_verified=detail.last_verified_at,
                verified=facts,
                unresolved=unresolved,
            )
            if item.section_type == "common_mistakes":
                warnings.append(f"[{status}] {item.body_markdown}")

        for item in detail.schedules:
            schedule_text = (
                f"{item.rule_type}: {item.notes or item.recurrence_type} ({item.timezone})"
            )
            status = _classify_fact(
                claim=schedule_text,
                entity_id=item.seed_key or detail.slug,
                claim_key=f"schedule.{item.rule_type}",
                sources=sources,
                fallback_last_verified=detail.last_verified_at,
                verified=facts,
                unresolved=unresolved,
            )
            schedules.append(f"[{status}] {schedule_text}")
        for instance in detail.checklists:
            checklist.extend(
                PromptChecklistItem(label=item.label, completed=item.completed, period_key=instance.period_key)
                for item in instance.items
            )
    else:
        for instance in get_current_checklists(session, "weekly", now):
            checklist.extend(
                PromptChecklistItem(label=item.label, completed=item.completed, period_key=instance.period_key)
                for item in instance.items
            )
        schedules.append("일반 주간 체크리스트 기간은 목요일 00:00 KST 경계로 계산됨")

    facts.sort(key=lambda item: (item.claim, item.source_url or ""))
    unresolved.sort(key=lambda item: (item.verification_status, item.claim))
    sources = sorted(
        sources,
        key=lambda item: (
            not item.is_active,
            item.entity_type,
            item.entity_id,
            item.claim_key,
            item.source_type,
            item.title,
            item.evidence_id,
        ),
    )
    checklist.sort(key=lambda item: (item.period_key, item.label))
    return PromptContextBundle(
        generated_at=now,
        request_context=request_context,
        user_state=user_state,
        requirements=requirements,
        canonical_facts=facts,
        steps=steps,
        schedules=schedules,
        rewards=rewards,
        warnings=warnings,
        checklist=checklist,
        open_questions_or_conflicts=unresolved,
        sources=sources,
        user_question=request.user_question.strip(),
    )


def _fact_lines(facts: list[PromptFact]) -> list[str]:
    lines: list[str] = []
    for fact in facts:
        lines.append(f"- {fact.claim}")
        lines.append(f"  - verification: {fact.verification_status}")
        if fact.last_verified_at:
            lines.append(f"  - last_verified: {fact.last_verified_at.isoformat()}")
        if fact.source_title:
            lines.append(f"  - source: {fact.source_title} ({fact.source_type})")
        if fact.source_url:
            lines.append(f"  - url: {fact.source_url}")
    return lines or ["- none"]


def _section(lines: list[str], title: str, values: list[str]) -> None:
    lines.extend(["", f"## {title}", *(f"- {item}" for item in values)])
    if not values:
        lines.append("- none")


def render_markdown(bundle: PromptContextBundle) -> str:
    mode = PromptMode(bundle.request_context["mode"])
    lines = [
        "# BDO Companion Context",
        f"Generated: {bundle.generated_at.isoformat()}",
        f"Region: {bundle.region}",
        "",
        "## REQUEST_CONTEXT",
        f"- page: {bundle.request_context['page']}",
        f"- mode: {mode.value}",
        f"- goal: {PRESET_GOALS[mode]}",
        "",
        "## RESPONSE_GUARDRAILS",
        *[f"- {item}" for item in GUARDRAILS],
    ]
    _section(lines, "USER_STATE", bundle.user_state)
    _section(lines, "REQUIREMENTS", bundle.requirements)
    lines.extend(["", "## CANONICAL_FACTS", *_fact_lines(bundle.canonical_facts)])
    _section(lines, "STEPS", bundle.steps)
    _section(lines, "SCHEDULES", bundle.schedules)
    _section(lines, "REWARDS", bundle.rewards)
    _section(lines, "WARNINGS", bundle.warnings)
    lines.extend(["", "## CHECKLIST_STATE"])
    if bundle.checklist:
        lines.extend(
            f"- [{'x' if item.completed else ' '}] {item.label} ({item.period_key})"
            for item in bundle.checklist
        )
    else:
        lines.append("- none")
    if bundle.project_state:
        _section(lines, "PROJECT_STATE", bundle.project_state)
    lines.extend(["", "## OPEN_QUESTIONS_OR_CONFLICTS", *_fact_lines(bundle.open_questions_or_conflicts)])
    lines.extend(["", "## SOURCES"])
    if bundle.sources:
        lines.extend(
            f"{index}. [{item.title}]({item.url}) — {item.source_type}, "
            f"{item.verification_status}, {'current' if item.is_active else 'historical'}, "
            f"claim {item.entity_id}/{item.claim_key}, verified {item.last_verified_at.isoformat()}"
            for index, item in enumerate(bundle.sources, start=1)
        )
    else:
        lines.append("- none")
    lines.extend(
        [
            "",
            "## USER_QUESTION",
            bundle.user_question or "제공된 컨텍스트를 바탕으로 목적에 맞게 답해 주세요.",
        ]
    )
    return "\n".join(lines).strip() + "\n"


def render_result(bundle: PromptContextBundle) -> PromptRenderOut:
    markdown = render_markdown(bundle)
    characters = len(markdown)
    estimated_tokens = (characters + 3) // 4
    return PromptRenderOut(
        bundle=bundle,
        markdown=markdown,
        character_count=characters,
        estimated_tokens=estimated_tokens,
        over_budget=estimated_tokens > 12_000,
    )
