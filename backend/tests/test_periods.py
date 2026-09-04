from datetime import datetime, time

import pytest

from app.periods import KST, SUNDAY, daily_period, next_weekly_occurrence, period_for_rule, weekly_period


def test_daily_period_changes_at_kst_midnight() -> None:
    before = daily_period(datetime(2026, 9, 2, 23, 59, 59, tzinfo=KST))
    boundary = daily_period(datetime(2026, 9, 3, 0, 0, 0, tzinfo=KST))
    assert before.key == "D:2026-09-02"
    assert boundary.key == "D:2026-09-03"
    assert before.end == boundary.start


def test_thursday_weekly_period_changes_at_boundary() -> None:
    before = weekly_period(datetime(2026, 9, 2, 23, 59, 59, tzinfo=KST))
    boundary = weekly_period(datetime(2026, 9, 3, 0, 0, 0, tzinfo=KST))
    assert before.key == "W:2026-08-27T00:00:00+09:00"
    assert boundary.key == "W:2026-09-03T00:00:00+09:00"
    assert before.end == boundary.start


@pytest.mark.parametrize(
    ("moment", "daily_key", "weekly_key"),
    [
        (
            datetime(2026, 12, 31, 23, 59, 59, tzinfo=KST),
            "D:2026-12-31",
            "W:2026-12-31T00:00:00+09:00",
        ),
        (
            datetime(2027, 1, 1, 0, 0, 0, tzinfo=KST),
            "D:2027-01-01",
            "W:2026-12-31T00:00:00+09:00",
        ),
    ],
)
def test_period_keys_cross_year_without_losing_week(moment, daily_key, weekly_key) -> None:
    assert daily_period(moment).key == daily_key
    assert weekly_period(moment).key == weekly_key


def test_sunday_reward_boundary_is_a_schedule_not_weekly_reset() -> None:
    before = datetime(2026, 9, 5, 23, 59, 59, tzinfo=KST)
    boundary = datetime(2026, 9, 6, 0, 0, 0, tzinfo=KST)
    assert next_weekly_occurrence(before, SUNDAY) == boundary
    assert next_weekly_occurrence(boundary, SUNDAY) == boundary
    assert weekly_period(before).key == weekly_period(boundary).key


def test_naive_datetime_is_rejected() -> None:
    with pytest.raises(ValueError, match="timezone-aware"):
        daily_period(datetime(2026, 9, 2))


def test_configurable_daily_boundary() -> None:
    before = daily_period(datetime(2026, 9, 3, 5, 59, 59, tzinfo=KST), time(6, 0))
    boundary = daily_period(datetime(2026, 9, 3, 6, 0, tzinfo=KST), time(6, 0))
    assert before.key == "D:2026-09-02T06:00:00+09:00"
    assert boundary.key == "D:2026-09-03T06:00:00+09:00"


def test_weekly_reset_can_use_another_weekday_and_time() -> None:
    monday = 0
    before = weekly_period(datetime(2026, 9, 7, 5, 59, 59, tzinfo=KST), monday, time(6, 0))
    boundary = weekly_period(datetime(2026, 9, 7, 6, 0, tzinfo=KST), monday, time(6, 0))
    assert before.start == datetime(2026, 8, 31, 6, 0, tzinfo=KST)
    assert boundary.start == datetime(2026, 9, 7, 6, 0, tzinfo=KST)


def test_reward_payout_cannot_drive_checklist_period() -> None:
    with pytest.raises(ValueError, match="cannot drive"):
        period_for_rule(
            rule_type="reward_payout",
            recurrence_type="weekly",
            weekday=SUNDAY,
            now=datetime(2026, 9, 6, 0, 0, tzinfo=KST),
        )
