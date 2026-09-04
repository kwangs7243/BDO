from __future__ import annotations

from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, inspect, text

from app import models  # noqa: F401
from app.database import Base


@pytest.mark.parametrize("precreate_current_tables", [False, True])
def test_database_migrates_through_project_foundation_without_losing_history(
    tmp_path, monkeypatch, precreate_current_tables
) -> None:
    database_path = tmp_path / "v15-forward.db"
    database_url = f"sqlite:///{database_path.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", database_url)
    config = Config(str(Path(__file__).resolve().parents[1] / "alembic.ini"))

    command.upgrade(config, "20260902_0001")
    engine = create_engine(database_url)
    with engine.begin() as connection:
        connection.execute(
            text(
                "INSERT INTO content "
                "(id, slug, name_ko, category, status, last_verified_at) "
                "VALUES (1, 'history-fixture', '이력 픽스처', 'system', 'active', '2026-09-02')"
            )
        )
        connection.execute(
            text(
                "INSERT INTO checklist_template "
                "(id, content_id, name, recurrence_scope, enabled_default) "
                "VALUES (1, 1, '기존 주간', 'weekly', 1)"
            )
        )
        connection.execute(
            text(
                "INSERT INTO checklist_template_item "
                "(id, template_id, order_no, label) VALUES (1, 1, 1, '기존 항목')"
            )
        )
        connection.execute(
            text(
                "INSERT INTO checklist_instance "
                "(id, template_id, period_key, period_start, period_end, generated_at) "
                "VALUES (1, 1, 'W:2026-08-27T00:00:00+09:00', "
                "'2026-08-27 00:00:00', '2026-09-03 00:00:00', '2026-08-27 00:00:00')"
            )
        )
        connection.execute(
            text(
                "INSERT INTO checklist_item_state "
                "(id, instance_id, template_item_id, completed, completed_at, note) "
                "VALUES (1, 1, 1, 1, '2026-09-01 12:00:00', '보존할 기록')"
            )
        )
    if precreate_current_tables:
        # V1.5 startup create_all may have created only the new tables before
        # Alembic ran; the forward migration must preserve and complete that DB.
        Base.metadata.create_all(engine)

    command.upgrade(config, "20260903_0002")
    with engine.begin() as connection:
        connection.execute(
            text(
                "INSERT INTO user_content_state "
                "(id, content_id, state, priority, note, updated_at) "
                "VALUES (1, 1, 'in_progress', 2, 'preserved user state', '2026-09-04 12:00:00')"
            )
        )
    command.upgrade(config, "head")
    inspector = inspect(engine)
    assert {
        "content_requirement",
        "content_step",
        "reward",
        "content_section",
        "content_relation",
        "user_content_state",
        "project",
        "project_stage",
        "project_stage_dependency",
        "material",
        "project_material",
        "project_material_source",
        "user_material_inventory",
        "user_project_stage_state",
    }.issubset(set(inspector.get_table_names()))
    assert "period_rule_id" in {column["name"] for column in inspector.get_columns("checklist_template")}
    with engine.connect() as connection:
        row = connection.execute(
            text("SELECT completed, note FROM checklist_item_state WHERE id = 1")
        ).one()
        user_state = connection.execute(
            text("SELECT state, priority, note FROM user_content_state WHERE id = 1")
        ).one()
    assert row.completed == 1
    assert user_state.state == "in_progress"
    assert user_state.priority == 2
    assert user_state.note == "preserved user state"
    assert row.note == "보존할 기록"
