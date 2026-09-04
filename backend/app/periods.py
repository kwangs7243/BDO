from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo


KST = ZoneInfo("Asia/Seoul")
THURSDAY = 3
SUNDAY = 6
RESET_RULE_TYPES = frozenset({"quest_reset", "attempt_reset"})


@dataclass(frozen=True)
class Period:
    key: str
    start: datetime
    end: datetime


def ensure_kst(now: datetime) -> datetime:
    if now.tzinfo is None:
        raise ValueError("now must be timezone-aware")
    return now.astimezone(KST)


def daily_period(now: datetime, at: time = time.min) -> Period:
    local = ensure_kst(now)
    start = datetime.combine(local.date(), at, tzinfo=KST)
    if local < start:
        start -= timedelta(days=1)
    key = f"D:{start.date().isoformat()}" if at == time.min else f"D:{start.isoformat()}"
    return Period(key, start, start + timedelta(days=1))


def weekly_period(now: datetime, weekday: int = THURSDAY, at: time = time.min) -> Period:
    local = ensure_kst(now)
    start_date = local.date() - timedelta(days=(local.weekday() - weekday) % 7)
    start = datetime.combine(start_date, at, tzinfo=KST)
    if local < start:
        start -= timedelta(days=7)
    return Period(f"W:{start.isoformat()}", start, start + timedelta(days=7))


def period_for_rule(
    *,
    rule_type: str,
    recurrence_type: str,
    now: datetime,
    weekday: int | None = None,
    at: time | None = None,
) -> Period:
    """Calculate a checklist period only for reset-like schedule rules."""

    if rule_type not in RESET_RULE_TYPES:
        raise ValueError(f"{rule_type} cannot drive a checklist period")
    boundary_time = at or time.min
    if recurrence_type == "daily":
        return daily_period(now, boundary_time)
    if recurrence_type == "weekly" and weekday is not None:
        return weekly_period(now, weekday, boundary_time)
    raise ValueError(f"Unsupported checklist recurrence: {recurrence_type}")


def next_weekly_occurrence(now: datetime, weekday: int, at: time = time.min) -> datetime:
    """Return the next schedule occurrence, treating an exact boundary as current."""

    local = ensure_kst(now)
    candidate_date: date = local.date() + timedelta(days=(weekday - local.weekday()) % 7)
    candidate = datetime.combine(candidate_date, at, tzinfo=KST)
    if candidate < local:
        candidate += timedelta(days=7)
    return candidate
