from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.ai_export import (
    DEFAULT_OUTPUT_DIR,
    GENERATED_HEADER,
    build_ai_exports,
    build_ai_exports_from_seed,
    compare_export_tree,
    render_content_markdown,
    write_export_tree,
)
from app.config import seed_dir
from app.database import Base
from app.knowledge import get_knowledge_content
from app.models import (
    Content,
    Material,
    Project,
    ProjectStage,
    UserContentState,
    UserMaterialInventory,
    UserProjectStageState,
)
from app.seed import import_seed


@pytest.fixture(scope="module")
def export_context():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    with Session(engine, expire_on_commit=False) as session:
        import_seed(session, seed_dir())
        exports = build_ai_exports(session)
        yield session, exports
    Base.metadata.drop_all(engine)
    engine.dispose()


def _table_snapshot(session: Session) -> dict[str, tuple[tuple[object, ...], ...]]:
    result = {}
    for table in sorted(Base.metadata.sorted_tables, key=lambda item: item.name):
        rows = session.execute(select(table)).all()
        result[table.name] = tuple(sorted((tuple(row) for row in rows), key=repr))
    return result


def test_build_from_seed_uses_an_isolated_database() -> None:
    exports = build_ai_exports_from_seed()
    manifest = json.loads(exports["manifest.json"])

    assert manifest["content_count"] == 294
    assert manifest["project_count"] == 1
    assert manifest["recipe_count"] == 4
    assert len(exports) == 301


def test_manifest_counts_match_active_canonical_rows(export_context) -> None:
    session, exports = export_context
    manifest = json.loads(exports["manifest.json"])
    active_contents = session.scalars(
        select(Content.slug).where(Content.status == "active")
    ).all()
    active_projects = session.scalars(
        select(Project.slug).where(Project.active.is_(True))
    ).all()

    assert manifest["content_count"] == len(active_contents) == 294
    assert manifest["project_count"] == len(active_projects) == 1
    assert len(manifest["contents"]) == 294
    assert len(manifest["projects"]) == 1


def test_all_markdown_is_marked_generated(export_context) -> None:
    _, exports = export_context
    markdown_files = {
        path: content for path, content in exports.items() if path.endswith(".md")
    }

    assert len(markdown_files) == 300
    assert all(content.startswith(GENERATED_HEADER) for content in markdown_files.values())


def test_blood_altar_contains_canonical_sections(export_context) -> None:
    _, exports = export_context
    page = exports["contents/blood-altar.md"]

    for heading in (
        "# 피의 제단",
        "## Identity",
        "## Overview",
        "## Requirements",
        "## Steps",
        "## Schedules",
        "## Rewards",
        "## Sections",
        "## Related Contents",
        "## Evidence and Sources",
        "### Current evidence",
        "### Historical / inactive evidence",
    ):
        assert heading in page
    assert '- slug: "blood-altar"' in page
    assert "- verification_status:" in page


def test_content_export_is_independent_of_user_content_state(export_context) -> None:
    session, exports = export_context
    before = exports["contents/blood-altar.md"]
    content = session.scalar(select(Content).where(Content.slug == "blood-altar"))
    assert content is not None
    session.add(
        UserContentState(
            content_id=content.id,
            state="in_progress",
            priority=9,
            note="must never enter canonical export",
            updated_at=datetime(2026, 9, 10, tzinfo=UTC),
        )
    )
    session.commit()

    after = build_ai_exports(session)["contents/blood-altar.md"]
    assert after == before
    assert "must never enter canonical export" not in after


def test_carrack_project_contains_canonical_graph_and_contract(export_context) -> None:
    _, exports = export_context
    page = exports["projects/carrack-advance.md"]

    for heading in (
        "## Identity",
        "## Overview",
        "## Stages",
        "## Material Requirements",
        "## Acquisition Sources",
        "## Stateless Calculation Contract",
    ):
        assert heading in page
    assert "carrack-advance.stage.blue-gear" in page
    assert "carrack-advance.material.moon-vein-flax" in page
    assert "quantity_per_completion" in page
    assert "max(required_quantity - provided_quantity, 0)" in page
    assert '- local_inventory_fallback: false' in page
    assert '- persistence: false' in page


def test_project_export_is_independent_of_local_project_state(export_context) -> None:
    session, exports = export_context
    before = exports["projects/carrack-advance.md"]
    material = session.scalar(
        select(Material).where(Material.key == "moon-vein-flax")
    )
    stage = session.scalar(
        select(ProjectStage).where(
            ProjectStage.seed_key == "carrack-advance.stage.blue-gear"
        )
    )
    assert material is not None
    assert stage is not None
    session.add(
        UserMaterialInventory(
            material_id=material.id,
            quantity=123,
            note="must never enter project export",
            updated_at=datetime(2026, 9, 10, tzinfo=UTC),
        )
    )
    session.add(
        UserProjectStageState(
            stage_id=stage.id,
            completed=True,
            completed_at=datetime(2026, 9, 10, tzinfo=UTC),
            note="must never enter project export",
            updated_at=datetime(2026, 9, 10, tzinfo=UTC),
        )
    )
    session.commit()

    after = build_ai_exports(session)["projects/carrack-advance.md"]
    assert after == before
    assert "must never enter project export" not in after
    assert "- owned_quantity:" not in after
    assert "- completed:" not in after


def test_schedule_projection_is_clock_independent(export_context) -> None:
    session, exports = export_context
    slugs = {item["slug"] for item in json.loads(exports["manifest.json"])["contents"]}
    first = get_knowledge_content(
        session,
        "blood-altar",
        datetime(2020, 1, 1, tzinfo=UTC),
    )
    second = get_knowledge_content(
        session,
        "blood-altar",
        datetime(2035, 12, 31, tzinfo=UTC),
    )
    assert first is not None
    assert second is not None

    first_page = render_content_markdown(first, slugs)
    second_page = render_content_markdown(second, slugs)
    assert first_page == second_page
    assert "next_occurrence" not in first_page


def test_numeric_database_identity_is_excluded(export_context) -> None:
    _, exports = export_context
    content_page = exports["contents/blood-altar.md"]
    project_page = exports["projects/carrack-advance.md"]

    assert "- evidence_id:" not in content_page
    assert "- id:" not in content_page
    assert "- id:" not in project_page
    assert "- stage_id:" not in project_page


def test_build_is_byte_deterministic(export_context) -> None:
    session, first = export_context
    second = build_ai_exports(session)

    assert {
        path: content.encode("utf-8") for path, content in first.items()
    } == {
        path: content.encode("utf-8") for path, content in second.items()
    }


def test_write_removes_only_stale_files_inside_output(tmp_path: Path) -> None:
    output = tmp_path / "ai_exports"
    stale = output / "contents" / "stale.md"
    stale.parent.mkdir(parents=True)
    stale.write_text("stale", encoding="utf-8")
    outside = tmp_path / "outside.md"
    outside.write_text("preserve", encoding="utf-8")
    expected = {
        "INDEX.md": "index\n",
        "contents/current.md": "current\n",
    }

    write_export_tree(expected, output)

    assert not stale.exists()
    assert outside.read_text(encoding="utf-8") == "preserve"
    assert compare_export_tree(expected, output) == []


def test_check_reports_changed_missing_and_extra_in_deterministic_order(
    tmp_path: Path,
) -> None:
    output = tmp_path / "ai_exports"
    expected = {
        "INDEX.md": "expected\n",
        "contents/a.md": "a\n",
        "contents/b.md": "b\n",
    }
    write_export_tree(expected, output)
    (output / "INDEX.md").write_text("changed\n", encoding="utf-8")
    (output / "contents" / "b.md").unlink()
    (output / "contents" / "z.md").write_text("extra\n", encoding="utf-8")

    assert compare_export_tree(expected, output) == [
        "changed: INDEX.md",
        "missing: contents/b.md",
        "extra: contents/z.md",
    ]


def test_manifest_has_stable_explicit_ordering(export_context) -> None:
    _, exports = export_context
    manifest = json.loads(exports["manifest.json"])

    content_slugs = [item["slug"] for item in manifest["contents"]]
    project_slugs = [item["slug"] for item in manifest["projects"]]
    assert content_slugs == sorted(content_slugs)
    assert project_slugs == sorted(project_slugs)
    assert "generated_at" not in manifest


def test_historical_evidence_is_separate_from_current(export_context) -> None:
    _, exports = export_context
    page = exports["contents/blood-altar.md"]
    historical = page.split("### Historical / inactive evidence", maxsplit=1)[1]

    assert '- is_active: false' in historical
    assert '- verification_status: "superseded"' in historical


def test_export_build_does_not_mutate_any_database_table(export_context) -> None:
    session, _ = export_context
    before = _table_snapshot(session)

    build_ai_exports(session)

    assert _table_snapshot(session) == before


def test_committed_ai_exports_are_current(export_context) -> None:
    _, exports = export_context
    assert compare_export_tree(exports, DEFAULT_OUTPUT_DIR) == []


def test_recipe_export_contract_and_counts(export_context):
    session, exports = export_context
    from app.models import Recipe
    manifest = json.loads(exports["manifest.json"])
    active = list(session.scalars(select(Recipe.slug).where(Recipe.active.is_(True))))
    assert manifest["schema_version"] == 2
    assert manifest["recipe_count"] == len(active) == 4
    assert len(exports) == manifest["content_count"] + manifest["project_count"] + len(active) + 2
    assert len([p for p in exports if p.startswith("recipes/")]) == 4
    assert "## Recipes" in exports["INDEX.md"]
    assert [r["slug"] for r in manifest["recipes"]] == sorted(active)
    beer = exports["recipes/beer.md"]
    for heading in ["Identity", "Result", "Cooking Requirement", "Ingredient Slots",
                    "Substitution Semantics", "Evidence and Sources"]:
        assert f"## {heading}" in beer
    for value in ["verified", "mineral-water", "purified-water",
                  "required_quantity: 6.0", "required_quantity: 3.0", "wheat / 밀", "potato / 감자",
                  "per one cooking attempt", "Mixed option consumption is not inferred",
                  "Result quantity is not guaranteed"]:
        assert value in beer
    assert "needs_review" not in beer
    assert "- evidence_id:" not in beer
    assert "- id:" not in beer
    assert "owned_quantity" not in beer


def test_recipe_export_preserves_historical_evidence(export_context):
    session, _ = export_context
    from app.knowledge import get_knowledge_recipe
    from app.ai_export import render_recipe_markdown
    from app.models import Evidence
    evidence = session.scalar(select(Evidence).where(
        Evidence.entity_type == "recipe", Evidence.entity_id == "beer", Evidence.claim_key == "ingredients"))
    old_status = evidence.verification_status
    try:
        evidence.verification_status = "superseded"
        session.flush()
        page = render_recipe_markdown(get_knowledge_recipe(session, "beer"))
        historical = page.split("### Historical / inactive evidence")[1]
        assert evidence.seed_key in historical
        assert 'verification_status: "superseded"' in historical
    finally:
        evidence.verification_status = old_status
        session.flush()
