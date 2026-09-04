from datetime import datetime, timedelta

from sqlalchemy import func, select

from app.checklists import get_current_checklists
from app.models import (
    ChecklistInstance,
    ChecklistItemState,
    ChecklistTemplate,
    ChecklistTemplateItem,
    Content,
    ScheduleRule,
)
from app.periods import KST


def test_new_period_preserves_completed_history(session) -> None:
    first_now = datetime(2026, 9, 2, 12, 0, tzinfo=KST)
    first_instances = get_current_checklists(session, "weekly", first_now)
    first_state_id = first_instances[0].items[0].id
    state = session.get(ChecklistItemState, first_state_id)
    state.completed = True
    state.completed_at = first_now
    session.commit()

    second_instances = get_current_checklists(session, "weekly", first_now + timedelta(days=8))
    assert second_instances[0].period_key != first_instances[0].period_key
    assert second_instances[0].items[0].completed is False
    assert session.get(ChecklistItemState, first_state_id).completed is True
    assert session.scalar(select(func.count()).select_from(ChecklistInstance)) == len(first_instances) * 2
    assert second_instances[0].period_start.tzinfo is not None


def test_same_period_reuses_instance(session) -> None:
    now = datetime(2026, 9, 2, 12, 0, tzinfo=KST)
    first = get_current_checklists(session, "weekly", now)
    second = get_current_checklists(session, "weekly", now)
    assert [item.id for item in first] == [item.id for item in second]


def test_template_uses_its_configured_weekly_period_rule(session) -> None:
    content = session.scalar(select(Content).where(Content.slug == "blood-altar"))
    rule = ScheduleRule(
        content_id=content.id,
        seed_key="blood-altar.test-monday-reset",
        rule_type="quest_reset",
        recurrence_type="weekly",
        weekday=0,
        time_local=datetime.strptime("06:00", "%H:%M").time(),
        timezone="Asia/Seoul",
        active=True,
    )
    session.add(rule)
    session.flush()
    template = ChecklistTemplate(
        content_id=content.id,
        seed_key="blood-altar.test-monday-check",
        name="월요일 오전 체크",
        recurrence_scope="weekly",
        period_rule_id=rule.id,
        enabled_default=True,
        active=True,
    )
    session.add(template)
    session.flush()
    session.add(
        ChecklistTemplateItem(
            template_id=template.id,
            seed_key="blood-altar.test-monday-check.item",
            order_no=1,
            label="확인",
            active=True,
        )
    )
    session.commit()

    now = datetime(2026, 9, 2, 12, tzinfo=KST)
    instances = get_current_checklists(session, "weekly", now, content_id=content.id)
    configured = next(item for item in instances if item.template_seed_key == template.seed_key)
    assert configured.period_key == "W:2026-08-31T06:00:00+09:00"
    assert configured.period_start == datetime(2026, 8, 31, 6, tzinfo=KST)
