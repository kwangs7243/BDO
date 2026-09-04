from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, selectinload

from app.models import ChecklistInstance, ChecklistItemState, ChecklistTemplate
from app.periods import KST, daily_period, period_for_rule, weekly_period
from app.schemas import ChecklistInstanceOut, ChecklistStateOut


def _fallback_period_for_scope(scope: str, now: datetime):
    if scope == "daily":
        return daily_period(now)
    if scope == "weekly":
        return weekly_period(now)
    raise ValueError(f"Unsupported recurrence scope: {scope}")


def _period_for_template(template: ChecklistTemplate, now: datetime):
    if template.period_rule is None:
        return _fallback_period_for_scope(template.recurrence_scope, now)
    rule = template.period_rule
    return period_for_rule(
        rule_type=rule.rule_type,
        recurrence_type=rule.recurrence_type,
        now=now,
        weekday=rule.weekday,
        at=rule.time_local,
    )


def get_current_checklists(
    session: Session,
    scope: str,
    now: datetime,
    content_id: int | None = None,
) -> list[ChecklistInstanceOut]:
    """Get or create this period's instances while preserving all older instances."""

    statement = (
        select(ChecklistTemplate)
        .where(
            ChecklistTemplate.recurrence_scope == scope,
            ChecklistTemplate.enabled_default.is_(True),
            ChecklistTemplate.active.is_(True),
        )
        .options(
            selectinload(ChecklistTemplate.items),
            selectinload(ChecklistTemplate.content),
            selectinload(ChecklistTemplate.period_rule),
        )
        .order_by(ChecklistTemplate.id)
    )
    if content_id is not None:
        statement = statement.where(ChecklistTemplate.content_id == content_id)
    templates = session.scalars(statement).all()

    output: list[ChecklistInstanceOut] = []
    for template in templates:
        period = _period_for_template(template, now)
        active_items = [item for item in template.items if item.active]
        instance = session.scalar(
            select(ChecklistInstance)
            .where(
                ChecklistInstance.template_id == template.id,
                ChecklistInstance.period_key == period.key,
            )
            .options(selectinload(ChecklistInstance.states).selectinload(ChecklistItemState.template_item))
        )
        if instance is None:
            instance = ChecklistInstance(
                template_id=template.id,
                period_key=period.key,
                period_start=period.start,
                period_end=period.end,
                generated_at=datetime.now(UTC),
            )
            try:
                session.add(instance)
                session.flush()
                for item in active_items:
                    session.add(ChecklistItemState(instance_id=instance.id, template_item_id=item.id))
                session.commit()
            except IntegrityError:
                # React development mode can issue the same read twice. The unique
                # period key makes the concurrent winner authoritative.
                session.rollback()
            instance = session.scalar(
                select(ChecklistInstance)
                .where(
                    ChecklistInstance.template_id == template.id,
                    ChecklistInstance.period_key == period.key,
                )
                .options(selectinload(ChecklistInstance.states).selectinload(ChecklistItemState.template_item))
            )
            assert instance is not None

        existing_item_ids = {state.template_item_id for state in instance.states}
        missing_items = [item for item in active_items if item.id not in existing_item_ids]
        if missing_items:
            for item in missing_items:
                session.add(ChecklistItemState(instance_id=instance.id, template_item_id=item.id))
            session.commit()
            instance = session.scalar(
                select(ChecklistInstance)
                .where(ChecklistInstance.id == instance.id)
                .options(selectinload(ChecklistInstance.states).selectinload(ChecklistItemState.template_item))
            )
            assert instance is not None

        states = sorted(
            (state for state in instance.states if state.template_item.active),
            key=lambda state: state.template_item.order_no,
        )
        output.append(
            ChecklistInstanceOut(
                id=instance.id,
                template_id=template.id,
                template_seed_key=template.seed_key,
                template_name=template.name,
                content_slug=template.content.slug if template.content else None,
                period_key=instance.period_key,
                period_start=instance.period_start.replace(tzinfo=KST) if instance.period_start.tzinfo is None else instance.period_start,
                period_end=instance.period_end.replace(tzinfo=KST) if instance.period_end.tzinfo is None else instance.period_end,
                items=[
                    ChecklistStateOut(
                        id=state.id,
                        template_item_id=state.template_item_id,
                        seed_key=state.template_item.seed_key,
                        label=state.template_item.label,
                        details=state.template_item.details,
                        completed=state.completed,
                        completed_at=(
                            state.completed_at.replace(tzinfo=UTC)
                            if state.completed_at is not None and state.completed_at.tzinfo is None
                            else state.completed_at
                        ),
                        note=state.note,
                    )
                    for state in states
                ],
            )
        )
    return output
