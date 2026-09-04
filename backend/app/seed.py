from __future__ import annotations

import json
from datetime import date, datetime, time
from pathlib import Path
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.config import seed_dir
from app.database import SessionLocal, create_schema
from app.models import (
    ChecklistTemplate,
    ChecklistTemplateItem,
    Content,
    ContentRelation,
    ContentRequirement,
    ContentSection,
    ContentStep,
    Evidence,
    Reward,
    ScheduleRule,
    Source,
)
from app.periods import RESET_RULE_TYPES
from app.project_seed import sync_projects


REQUIREMENT_KINDS = {"quest", "level", "gear", "stat", "item", "knowledge", "party", "character", "other"}
REQUIREMENT_LEVELS = {"required", "recommended", "optional"}
STEP_PHASES = {"unlock", "preparation", "first_time", "repeat", "reward", "maintenance"}
SECTION_TYPES = {"overview", "why", "preparation", "start", "strategy", "common_mistakes", "notes"}
RELATION_TYPES = {"prerequisite", "unlocks", "related", "source_for", "part_of", "alternative", "project_link"}


def _read_json(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def _optional_date(value: str | None) -> date | None:
    return date.fromisoformat(value) if value else None


def _optional_datetime(value: str | None) -> datetime | None:
    return datetime.fromisoformat(value) if value else None


def _optional_time(value: str | None) -> time | None:
    return time.fromisoformat(value) if value else None


def _seed_key(slug: str, row: dict[str, Any]) -> str:
    key = str(row.get("seed_key", ""))
    if not key or not key.startswith(f"{slug}."):
        raise ValueError(f"seed_key must start with '{slug}.': {key!r}")
    return key


def _sync_simple_children(
    session: Session,
    *,
    model: type,
    content: Content,
    rows: list[dict[str, Any]],
    values_for: Any,
) -> None:
    existing = list(session.scalars(select(model).where(model.content_id == content.id)).all())
    by_key = {item.seed_key: item for item in existing}
    seen: set[str] = set()
    for index, row in enumerate(rows, start=1):
        key = _seed_key(content.slug, row)
        if key in seen:
            raise ValueError(f"duplicate seed_key for {content.slug}: {key}")
        seen.add(key)
        item = by_key.get(key)
        values = values_for(row, index)
        values["active"] = bool(row.get("active", True))
        if item is None:
            item = model(content_id=content.id, seed_key=key, **values)
            session.add(item)
        else:
            for field, value in values.items():
                setattr(item, field, value)
    for item in existing:
        if item.seed_key not in seen:
            item.active = False


def _sync_schedules(session: Session, content: Content, rows: list[dict[str, Any]]) -> dict[str, ScheduleRule]:
    existing = list(session.scalars(select(ScheduleRule).where(ScheduleRule.content_id == content.id)).all())
    by_key = {item.seed_key: item for item in existing if item.seed_key}
    legacy = [item for item in existing if item.seed_key is None]
    seen: set[str] = set()
    result: dict[str, ScheduleRule] = {}
    for row in rows:
        key = _seed_key(content.slug, row)
        if key in seen:
            raise ValueError(f"duplicate schedule seed_key: {key}")
        seen.add(key)
        rule = by_key.get(key)
        if rule is None:
            rule = next((item for item in legacy if item.rule_type == row["rule_type"]), None)
            if rule is not None:
                legacy.remove(rule)
                rule.seed_key = key
            else:
                rule = ScheduleRule(content_id=content.id, seed_key=key)
                session.add(rule)
        rule.rule_type = row["rule_type"]
        rule.recurrence_type = row["recurrence_type"]
        rule.weekday = row.get("weekday")
        rule.time_local = _optional_time(row.get("time_local"))
        rule.fixed_datetime = _optional_datetime(row.get("fixed_datetime"))
        rule.timezone = row.get("timezone", "Asia/Seoul")
        rule.effective_from = _optional_date(row.get("effective_from"))
        rule.effective_to = _optional_date(row.get("effective_to"))
        rule.notes = row.get("notes")
        rule.active = bool(row.get("active", True))
        result[key] = rule
    for rule in existing:
        if rule.seed_key not in seen:
            rule.active = False
    session.flush()
    return result


def _sync_checklists(
    session: Session,
    content: Content,
    rows: list[dict[str, Any]],
    schedules: dict[str, ScheduleRule],
) -> None:
    existing = list(
        session.scalars(select(ChecklistTemplate).where(ChecklistTemplate.content_id == content.id)).all()
    )
    by_key = {item.seed_key: item for item in existing if item.seed_key}
    legacy = [item for item in existing if item.seed_key is None]
    seen_templates: set[str] = set()
    for row in rows:
        key = _seed_key(content.slug, row)
        if key in seen_templates:
            raise ValueError(f"duplicate checklist seed_key: {key}")
        seen_templates.add(key)
        template = by_key.get(key)
        if template is None:
            template = next((item for item in legacy if item.name == row["name"]), None)
            if template is not None:
                legacy.remove(template)
                template.seed_key = key
            else:
                template = ChecklistTemplate(content_id=content.id, seed_key=key)
                session.add(template)
        template.name = row["name"]
        template.recurrence_scope = row["recurrence_scope"]
        template.enabled_default = bool(row.get("enabled_default", True))
        template.active = bool(row.get("active", True))
        period_rule_key = row.get("period_rule_seed_key")
        if period_rule_key:
            period_rule = schedules.get(period_rule_key)
            if period_rule is None:
                raise ValueError(f"unknown period_rule_seed_key: {period_rule_key}")
            if period_rule.rule_type not in RESET_RULE_TYPES:
                raise ValueError(f"{period_rule.rule_type} cannot drive checklist {key}")
            template.period_rule = period_rule
        else:
            template.period_rule = None
        session.flush()

        existing_items = list(template.items)
        items_by_key = {item.seed_key: item for item in existing_items if item.seed_key}
        legacy_items = [item for item in existing_items if item.seed_key is None]
        seen_items: set[str] = set()
        for index, item_row in enumerate(row.get("items", []), start=1):
            item_key = _seed_key(content.slug, item_row)
            if item_key in seen_items:
                raise ValueError(f"duplicate checklist item seed_key: {item_key}")
            seen_items.add(item_key)
            item = items_by_key.get(item_key)
            if item is None:
                order_no = int(item_row.get("order_no", index))
                item = next((candidate for candidate in legacy_items if candidate.order_no == order_no), None)
                if item is not None:
                    legacy_items.remove(item)
                    item.seed_key = item_key
                else:
                    item = ChecklistTemplateItem(template_id=template.id, seed_key=item_key)
                    session.add(item)
            item.order_no = int(item_row.get("order_no", index))
            item.label = item_row["label"]
            item.details = item_row.get("details")
            item.reward_hint = item_row.get("reward_hint")
            item.active = bool(item_row.get("active", True))
        for item in existing_items:
            if item.seed_key not in seen_items:
                item.active = False

    for template in existing:
        if template.seed_key not in seen_templates:
            template.active = False


def _sync_relations(session: Session, content: Content, rows: list[dict[str, Any]]) -> None:
    existing = list(
        session.scalars(select(ContentRelation).where(ContentRelation.from_content_id == content.id)).all()
    )
    by_key = {item.seed_key: item for item in existing}
    seen: set[str] = set()
    for index, row in enumerate(rows, start=1):
        key = _seed_key(content.slug, row)
        if row["relation_type"] not in RELATION_TYPES:
            raise ValueError(f"unsupported relation_type: {row['relation_type']}")
        target = session.scalar(select(Content).where(Content.slug == row["to_content_slug"]))
        if target is None:
            raise ValueError(f"unknown related content: {row['to_content_slug']}")
        seen.add(key)
        relation = by_key.get(key)
        if relation is None:
            relation = ContentRelation(from_content_id=content.id, seed_key=key, to_content_id=target.id)
            session.add(relation)
        relation.to_content_id = target.id
        relation.relation_type = row["relation_type"]
        relation.note = row.get("note")
        relation.order_no = int(row.get("order_no", index))
        relation.active = bool(row.get("active", True))
    for relation in existing:
        if relation.seed_key not in seen:
            relation.active = False


def _sync_evidence(
    session: Session,
    content: Content,
    rows: list[dict[str, Any]],
    source_rows: dict[str, dict[str, Any]],
) -> None:
    declared_keys: set[str] = set()
    for claim in rows:
        claim_seed_key = _seed_key(content.slug, claim)
        entity_id = claim.get("entity_seed_key", content.slug)
        if entity_id != content.slug and not str(entity_id).startswith(f"{content.slug}."):
            raise ValueError(f"evidence entity key must be scoped to {content.slug}: {entity_id}")
        for source_id in claim["source_ids"]:
            if source_id not in source_rows:
                raise ValueError(f"unknown source_id: {source_id}")
            evidence_key = f"{claim_seed_key}::{source_id}"
            declared_keys.add(evidence_key)
            evidence = session.scalar(select(Evidence).where(Evidence.seed_key == evidence_key))
            if evidence is None:
                evidence = session.scalar(
                    select(Evidence).where(
                        Evidence.seed_key.is_(None),
                        Evidence.entity_type == claim.get("entity_type", "content"),
                        Evidence.entity_id == entity_id,
                        Evidence.claim_key == claim["claim_key"],
                        Evidence.source_id == source_id,
                    )
                )
            if evidence is None:
                evidence = Evidence(seed_key=evidence_key)
                session.add(evidence)
            evidence.seed_key = evidence_key
            evidence.entity_type = claim.get("entity_type", "content")
            evidence.entity_id = entity_id
            evidence.claim_key = claim["claim_key"]
            evidence.source_id = source_id
            evidence.evidence_note = claim.get("note")
            evidence.verification_status = claim.get("verification_status", "unverified")
            evidence.last_verified_at = date.fromisoformat(
                claim.get("last_verified_at", content.last_verified_at.isoformat())
            )
            evidence.active = bool(
                claim.get("active", evidence.verification_status != "superseded")
            )

    existing_seeded = session.scalars(
        select(Evidence).where(Evidence.seed_key.like(f"{content.slug}.%"))
    ).all()
    for evidence in existing_seeded:
        if evidence.seed_key not in declared_keys:
            evidence.active = False


def import_seed(session: Session, directory: Path | None = None) -> None:
    """Synchronize reviewed seed data in place while preserving user history."""

    directory = directory or seed_dir()
    source_data = _read_json(directory / "seed_sources.json")
    content_data = _read_json(directory / "seed_contents.json")
    source_rows = {row["id"]: row for row in source_data}

    for row in source_data:
        source = session.get(Source, row["id"])
        values = {
            "url": row["url"],
            "title": row["title"],
            "publisher": row.get("publisher"),
            "source_type": row["source_type"],
            "published_at": _optional_date(row.get("published_at")),
            "retrieved_at": _optional_datetime(row.get("retrieved_at")),
            "region": row.get("region", "KR"),
        }
        if source is None:
            session.add(Source(id=row["id"], **values))
        else:
            for field, value in values.items():
                setattr(source, field, value)
    session.flush()

    contents: dict[str, Content] = {}
    for row in content_data:
        content = session.scalar(select(Content).where(Content.slug == row["slug"]))
        values = {
            "name_ko": row["name_ko"],
            "category": row["category"],
            "subcategory": row.get("subcategory"),
            "summary": row.get("summary"),
            "purpose": row.get("purpose"),
            "party_type": row.get("party_type"),
            "difficulty": row.get("difficulty"),
            "status": row.get("status", "active"),
            "last_verified_at": date.fromisoformat(row["last_verified_at"]),
        }
        if content is None:
            content = Content(slug=row["slug"], **values)
            session.add(content)
            session.flush()
        else:
            for field, value in values.items():
                setattr(content, field, value)
        contents[content.slug] = content
    session.flush()

    for row in content_data:
        content = contents[row["slug"]]
        schedules = _sync_schedules(session, content, row.get("schedules", []))
        _sync_simple_children(
            session,
            model=ContentRequirement,
            content=content,
            rows=row.get("requirements", []),
            values_for=lambda item, index: {
                "kind": item["kind"],
                "title": item.get("title"),
                "description": item["description"],
                "structured_value": item.get("structured_value"),
                "requirement_level": item["requirement_level"],
                "order_no": int(item.get("order_no", index)),
            },
        )
        _sync_simple_children(
            session,
            model=ContentStep,
            content=content,
            rows=row.get("steps", []),
            values_for=lambda item, index: {
                "phase": item["phase"],
                "order_no": int(item.get("order_no", index)),
                "title": item["title"],
                "description": item["description"],
                "checkable": bool(item.get("checkable", False)),
            },
        )
        _sync_simple_children(
            session,
            model=Reward,
            content=content,
            rows=row.get("rewards", []),
            values_for=lambda item, index: {
                "name": item["name"],
                "reward_type": item["reward_type"],
                "amount": item.get("amount"),
                "min_amount": item.get("min_amount"),
                "max_amount": item.get("max_amount"),
                "unit": item.get("unit"),
                "is_choice": bool(item.get("is_choice", False)),
                "choice_group": item.get("choice_group"),
                "recommendation": item.get("recommendation"),
                "notes": item.get("notes"),
                "order_no": int(item.get("order_no", index)),
            },
        )
        _sync_simple_children(
            session,
            model=ContentSection,
            content=content,
            rows=row.get("sections", []),
            values_for=lambda item, index: {
                "section_type": item["section_type"],
                "title": item["title"],
                "body_markdown": item["body_markdown"],
                "order_no": int(item.get("order_no", index)),
            },
        )
        for requirement in row.get("requirements", []):
            if requirement["kind"] not in REQUIREMENT_KINDS:
                raise ValueError(f"unsupported requirement kind: {requirement['kind']}")
            if requirement["requirement_level"] not in REQUIREMENT_LEVELS:
                raise ValueError(f"unsupported requirement level: {requirement['requirement_level']}")
        for step in row.get("steps", []):
            if step["phase"] not in STEP_PHASES:
                raise ValueError(f"unsupported step phase: {step['phase']}")
        for section in row.get("sections", []):
            if section["section_type"] not in SECTION_TYPES:
                raise ValueError(f"unsupported section type: {section['section_type']}")
        checklist_rows = row.get("checklists")
        if checklist_rows is None and row.get("checklist"):
            checklist_rows = [row["checklist"]]
        _sync_checklists(session, content, checklist_rows or [], schedules)
        session.flush()

    for row in content_data:
        content = contents[row["slug"]]
        _sync_relations(session, content, row.get("relations", []))
        evidence_rows = row.get("evidence", [])
        if not evidence_rows and row.get("source_ids"):
            evidence_rows = [
                {
                    "seed_key": f"{content.slug}.summary",
                    "entity_type": "content",
                    "entity_seed_key": content.slug,
                    "claim_key": "summary",
                    "source_ids": row["source_ids"],
                    "verification_status": row.get("verification_status", "verified"),
                    "last_verified_at": row["last_verified_at"],
                    "note": content.summary,
                }
            ]
        _sync_evidence(session, content, evidence_rows, source_rows)

    sync_projects(session, directory)
    session.commit()


def main() -> None:
    create_schema()
    with SessionLocal() as session:
        import_seed(session)
    print("Seed import complete")


if __name__ == "__main__":
    main()
