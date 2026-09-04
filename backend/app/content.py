from __future__ import annotations

from collections import defaultdict
from datetime import UTC, datetime, time
from zoneinfo import ZoneInfo

from sqlalchemy import or_, select
from sqlalchemy.orm import Session, selectinload

from app.checklists import get_current_checklists
from app.models import Content, ContentRelation, Evidence, ScheduleRule
from app.periods import daily_period, next_weekly_occurrence
from app.schemas import (
    ContentDetailOut,
    ContentRelationOut,
    ContentRequirementOut,
    ContentSectionOut,
    ContentStepOut,
    ContentSummaryOut,
    RewardOut,
    ScheduleOut,
    SourceOut,
    UserContentStateOut,
)


STATUS_PRIORITY = {"conflict": 0, "needs_review": 1, "verified": 2}
PHASE_ORDER = {"unlock": 0, "preparation": 1, "first_time": 2, "repeat": 3, "reward": 4, "maintenance": 5}


def aggregate_verification(evidence: list[Evidence]) -> str:
    active = [item for item in evidence if item.is_active]
    if not active:
        return "unverified"
    return min(
        (item.verification_status for item in active),
        key=lambda status: STATUS_PRIORITY.get(status, 0),
    )


def list_contents(session: Session) -> list[ContentSummaryOut]:
    contents = list(session.scalars(select(Content).order_by(Content.name_ko, Content.slug)).all())
    evidence_by_slug: dict[str, list[Evidence]] = defaultdict(list)
    if contents:
        evidence_rows = session.scalars(
            select(Evidence)
            .where(Evidence.entity_type == "content", Evidence.entity_id.in_([item.slug for item in contents]))
            .order_by(Evidence.entity_id, Evidence.claim_key, Evidence.id)
        ).all()
        for item in evidence_rows:
            evidence_by_slug[item.entity_id].append(item)
    return [
        ContentSummaryOut(
            slug=item.slug,
            name_ko=item.name_ko,
            category=item.category,
            summary=item.summary,
            status=item.status,
            last_verified_at=item.last_verified_at,
            verification_status=aggregate_verification(evidence_by_slug[item.slug]),
        )
        for item in contents
    ]


def _aware(value: datetime | None, timezone: str = "UTC") -> datetime | None:
    if value is None or value.tzinfo is not None:
        return value
    return value.replace(tzinfo=ZoneInfo(timezone))


def _schedule_out(rule: ScheduleRule, now: datetime) -> ScheduleOut:
    next_occurrence = None
    if rule.recurrence_type == "weekly" and rule.weekday is not None:
        next_occurrence = next_weekly_occurrence(now, rule.weekday, rule.time_local or time.min)
    elif rule.recurrence_type == "daily":
        next_occurrence = daily_period(now, rule.time_local or time.min).end
    elif rule.recurrence_type == "fixed_datetime":
        next_occurrence = _aware(rule.fixed_datetime, rule.timezone)
    return ScheduleOut(
        id=rule.id,
        seed_key=rule.seed_key,
        rule_type=rule.rule_type,
        recurrence_type=rule.recurrence_type,
        weekday=rule.weekday,
        time_local=rule.time_local.isoformat(timespec="minutes") if rule.time_local else None,
        fixed_datetime=_aware(rule.fixed_datetime, rule.timezone),
        timezone=rule.timezone,
        notes=rule.notes,
        next_occurrence=next_occurrence,
    )


def _source_out(item: Evidence) -> SourceOut:
    return SourceOut(
        evidence_id=item.id,
        evidence_seed_key=item.seed_key,
        id=item.source.id,
        title=item.source.title,
        url=item.source.url,
        publisher=item.source.publisher,
        source_type=item.source.source_type,
        published_at=item.source.published_at,
        retrieved_at=_aware(item.source.retrieved_at, "UTC"),
        region=item.source.region,
        entity_type=item.entity_type,
        entity_id=item.entity_id,
        claim_key=item.claim_key,
        verification_status=item.verification_status,
        last_verified_at=item.last_verified_at,
        evidence_note=item.evidence_note,
        active=item.active,
        is_active=item.is_active,
    )


def _relation_out(relation: ContentRelation, direction: str) -> ContentRelationOut:
    linked = relation.to_content if direction == "outgoing" else relation.from_content
    return ContentRelationOut(
        seed_key=relation.seed_key,
        direction=direction,
        relation_type=relation.relation_type,
        note=relation.note,
        order_no=relation.order_no,
        content_slug=linked.slug,
        content_name_ko=linked.name_ko,
        content_category=linked.category,
    )


def get_content_detail(session: Session, slug: str, now: datetime) -> ContentDetailOut | None:
    content = session.scalar(
        select(Content)
        .where(Content.slug == slug)
        .options(
            selectinload(Content.schedules),
            selectinload(Content.requirements),
            selectinload(Content.steps),
            selectinload(Content.rewards),
            selectinload(Content.sections),
            selectinload(Content.outgoing_relations).selectinload(ContentRelation.to_content),
            selectinload(Content.incoming_relations).selectinload(ContentRelation.from_content),
            selectinload(Content.user_state),
        )
    )
    if content is None:
        return None

    evidence = list(
        session.scalars(
            select(Evidence)
            .where(or_(Evidence.entity_id == slug, Evidence.entity_id.like(f"{slug}.%")))
            .options(selectinload(Evidence.source))
            .order_by(Evidence.entity_type, Evidence.entity_id, Evidence.claim_key, Evidence.id)
        ).all()
    )
    checklists = []
    for scope in ("daily", "weekly"):
        checklists.extend(get_current_checklists(session, scope, now, content_id=content.id))

    state = content.user_state
    return ContentDetailOut(
        slug=content.slug,
        name_ko=content.name_ko,
        category=content.category,
        summary=content.summary,
        purpose=content.purpose,
        party_type=content.party_type,
        difficulty=content.difficulty,
        status=content.status,
        last_verified_at=content.last_verified_at,
        verification_status=aggregate_verification(evidence),
        requirements=[
            ContentRequirementOut(
                seed_key=item.seed_key,
                kind=item.kind,
                title=item.title,
                description=item.description,
                structured_value=item.structured_value,
                requirement_level=item.requirement_level,
                order_no=item.order_no,
            )
            for item in sorted(
                (row for row in content.requirements if row.active),
                key=lambda row: (row.order_no, row.seed_key),
            )
        ],
        sections=[
            ContentSectionOut(
                seed_key=item.seed_key,
                section_type=item.section_type,
                title=item.title,
                body_markdown=item.body_markdown,
                order_no=item.order_no,
            )
            for item in sorted(
                (row for row in content.sections if row.active),
                key=lambda row: (row.order_no, row.seed_key),
            )
        ],
        steps=[
            ContentStepOut(
                seed_key=item.seed_key,
                phase=item.phase,
                order_no=item.order_no,
                title=item.title,
                description=item.description,
                checkable=item.checkable,
            )
            for item in sorted(
                (row for row in content.steps if row.active),
                key=lambda row: (PHASE_ORDER.get(row.phase, 99), row.order_no, row.seed_key),
            )
        ],
        schedules=[
            _schedule_out(item, now)
            for item in sorted(
                (row for row in content.schedules if row.active),
                key=lambda row: (row.rule_type, row.seed_key or "", row.id),
            )
        ],
        rewards=[
            RewardOut(
                seed_key=item.seed_key,
                name=item.name,
                reward_type=item.reward_type,
                amount=item.amount,
                min_amount=item.min_amount,
                max_amount=item.max_amount,
                unit=item.unit,
                is_choice=item.is_choice,
                choice_group=item.choice_group,
                recommendation=item.recommendation,
                notes=item.notes,
                order_no=item.order_no,
            )
            for item in sorted(
                (row for row in content.rewards if row.active),
                key=lambda row: (row.order_no, row.seed_key),
            )
        ],
        checklists=checklists,
        related_contents=[
            *[
                _relation_out(item, "outgoing")
                for item in sorted(
                    (row for row in content.outgoing_relations if row.active),
                    key=lambda row: (row.order_no, row.seed_key),
                )
            ],
            *[
                _relation_out(item, "incoming")
                for item in sorted(
                    (row for row in content.incoming_relations if row.active),
                    key=lambda row: (row.order_no, row.seed_key),
                )
            ],
        ],
        user_state=UserContentStateOut(
            state=state.state if state else "not_started",
            priority=state.priority if state else None,
            note=state.note if state else None,
            updated_at=_aware(state.updated_at, "UTC") if state else None,
        ),
        sources=[_source_out(item) for item in evidence],
    )
