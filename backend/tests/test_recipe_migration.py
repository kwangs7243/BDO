from pathlib import Path

from alembic import command
from alembic.config import Config
import pytest
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.exc import IntegrityError

from app.database import Base


NEW_TABLES = {"ingredient_group", "ingredient_group_member", "recipe",
              "recipe_ingredient_slot", "recipe_ingredient_option"}


def configuration(tmp_path, monkeypatch):
    path = tmp_path / "migration.db"
    url = f"sqlite:///{path.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", url)
    cfg = Config(str(Path(__file__).resolve().parents[1] / "alembic.ini"))
    cfg.set_main_option("script_location", str(Path(__file__).resolve().parents[1] / "alembic"))
    return cfg, create_engine(url)


def test_recipe_migration_upgrade_downgrade_and_constraints(tmp_path, monkeypatch):
    cfg, engine = configuration(tmp_path, monkeypatch)
    command.upgrade(cfg, "20260905_0003")
    before = set(inspect(engine).get_table_names())
    command.upgrade(cfg, "head")
    assert set(inspect(engine).get_table_names()) == before | NEW_TABLES
    constraints = {c["name"] for c in inspect(engine).get_check_constraints("recipe_ingredient_option")}
    assert {"ck_recipe_option_quantity_positive", "ck_recipe_option_target_xor"} <= constraints
    with engine.begin() as c:
        c.execute(text("INSERT INTO material (id, key, name_ko, unit, active) VALUES (1, 'test', 'test', 'unit', 1)"))
        c.execute(text("INSERT INTO recipe (id, slug, name_ko, process_type, result_material_id, active) VALUES (1, 'test', 'test', 'cooking', 1, 1)"))
        c.execute(text("INSERT INTO ingredient_group (id, key, name_ko, active) VALUES (1, 'test', 'test', 1)"))
        c.execute(text("INSERT INTO recipe_ingredient_slot (id, recipe_id, seed_key, label, order_no, active) VALUES (1, 1, 'test.slot', 'test', 1, 1)"))
    for quantity, material, group in [(0, 1, None), (-1, 1, None), (1, None, None), (1, 1, 1)]:
        with pytest.raises(IntegrityError), engine.begin() as c:
            c.execute(text("INSERT INTO recipe_ingredient_option (slot_id, seed_key, material_id, ingredient_group_id, required_quantity, order_no, active) VALUES (1, 'test.option', :m, :g, :q, 1, 1)"),
                      {"m": material, "g": group, "q": quantity})
    command.downgrade(cfg, "20260905_0003")
    assert set(inspect(engine).get_table_names()) == before
    with engine.connect() as c:
        assert c.scalar(text("SELECT key FROM material WHERE id=1")) == "test"
    command.upgrade(cfg, "head")
    assert NEW_TABLES <= set(inspect(engine).get_table_names())
    engine.dispose()


def test_recipe_migration_accepts_create_all_tables(tmp_path, monkeypatch):
    cfg, engine = configuration(tmp_path, monkeypatch)
    command.upgrade(cfg, "20260905_0003")
    Base.metadata.create_all(engine)
    command.upgrade(cfg, "head")
    assert NEW_TABLES <= set(inspect(engine).get_table_names())
    engine.dispose()
