from datetime import datetime

from sqlalchemy import select

from app.content import get_content_detail, list_contents
from app.models import Evidence
from app.periods import KST


def test_source_status_and_last_verified_are_exposed(session) -> None:
    evidence = session.scalar(select(Evidence).where(Evidence.entity_id == "garmoth"))
    evidence.verification_status = "needs_review"
    session.commit()

    detail = get_content_detail(session, "garmoth", datetime(2026, 9, 2, 12, tzinfo=KST))
    assert detail is not None
    assert detail.verification_status == "needs_review"
    assert detail.sources[0].verification_status == "needs_review"
    assert detail.sources[0].last_verified_at.isoformat() == "2026-09-02"
    summary = next(item for item in list_contents(session) if item.slug == "garmoth")
    assert summary.verification_status == "needs_review"


def test_reward_payout_remains_distinct_schedule_type(session) -> None:
    detail = get_content_detail(session, "blood-altar", datetime(2026, 9, 2, 12, tzinfo=KST))
    assert detail is not None
    assert [item.rule_type for item in detail.schedules] == ["reward_payout"]


def test_superseded_source_status_is_exposed(session) -> None:
    evidence = session.scalar(select(Evidence).where(Evidence.entity_id == "garmoth"))
    evidence.verification_status = "superseded"
    session.commit()
    detail = get_content_detail(session, "garmoth", datetime(2026, 9, 2, 12, tzinfo=KST))
    assert detail is not None
    assert detail.verification_status == "verified"
    assert detail.sources[0].verification_status == "superseded"
    assert detail.sources[0].is_active is False


def test_structured_knowledge_and_bidirectional_relations_serialize(session) -> None:
    now = datetime(2026, 9, 2, 12, tzinfo=KST)
    blood_altar = get_content_detail(session, "blood-altar", now)
    assert blood_altar is not None
    assert blood_altar.requirements[0].structured_value == {"party_size": 3}
    assert blood_altar.steps[0].phase == "repeat"
    assert blood_altar.rewards[0].name == "주간 최고 기록 보상"
    assert {section.section_type for section in blood_altar.sections} == {"why", "common_mistakes"}
    assert blood_altar.related_contents[0].content_slug == "weekly-quest-framework"
    assert blood_altar.checklists[0].template_seed_key == "blood-altar.weekly-record-check"
    assert blood_altar.user_state.state.value == "not_started"

    framework = get_content_detail(session, "weekly-quest-framework", now)
    assert framework is not None
    incoming = next(item for item in framework.related_contents if item.direction == "incoming")
    assert incoming.content_slug == "blood-altar"
