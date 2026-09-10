"""Shared canonical Material catalog and historical Project fallback."""

from __future__ import annotations

import json
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Material


def sync_materials(session: Session, directory: Path) -> dict[str, Material]:
    """Update stable keys in place; only an explicit shared catalog archives absences.

    Legacy embedded catalogs are partial: they cannot archive another domain's rows.
    Missing optional files preserve the database without claiming catalog authority.
    """
    catalog = directory / "seed_materials.json"
    project_path = directory / "seed_projects.json"
    project = json.loads(project_path.read_text(encoding="utf-8")) if project_path.exists() else {}
    if not isinstance(project, dict):
        raise ValueError("seed_projects.json must contain an object")
    if catalog.exists() and "materials" in project:
        raise ValueError("duplicate Material authority: shared and embedded catalogs")
    authoritative = catalog.exists()
    rows = json.loads(catalog.read_text(encoding="utf-8")) if authoritative else project.get("materials")
    existing = {item.key: item for item in session.scalars(select(Material))}
    if rows is None:
        return existing
    if not isinstance(rows, list):
        raise ValueError("material catalog must be a list")
    seen: set[str] = set()
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("key"), str) or not row["key"].strip():
            raise ValueError("missing Material key")
        key = row["key"]
        if key in seen:
            raise ValueError(f"duplicate Material key: {key}")
        if not row.get("name_ko") or not row.get("unit", "개"):
            raise ValueError(f"missing Material name/unit: {key}")
        seen.add(key)
    for row in rows:
        key = row["key"]
        material = existing.get(key)
        if material is None:
            material = Material(key=key)
            session.add(material)
            existing[key] = material
        material.name_ko = row["name_ko"]
        material.unit = row.get("unit", "개")
        material.active = bool(row.get("active", True))
    if authoritative:
        for key, material in existing.items():
            if key not in seen:
                material.active = False
    session.flush()
    return {key: existing[key] for key in seen}
