from __future__ import annotations

from copy import deepcopy
from datetime import UTC, datetime, timedelta
import json
from pathlib import Path
import shutil

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session

from app.database import Base, get_session
from app.main import app
from app.models import (Material, ProjectMaterial, UserMaterialInventory, Recipe,
                        IngredientGroup, IngredientGroupMember, RecipeIngredientSlot,
                        RecipeIngredientOption, Evidence, Source, Content, UserContentState,
                        ProjectStage, UserProjectStageState, ChecklistTemplate,
                        ChecklistInstance, ChecklistItemState)
from app.seed import import_seed
from app.recipe_seed import sync_recipes
from app.material_seed import sync_materials
from app.project_seed import sync_projects
from app.knowledge import get_knowledge_recipe, get_knowledge_project, search_knowledge
from app.ai_export import render_recipe_markdown
from app.user_backup import export_user_backup

DATA = Path(__file__).resolve().parents[2] / "data"
DOMAIN = (IngredientGroup, IngredientGroupMember, Recipe, RecipeIngredientSlot, RecipeIngredientOption)


def read(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def write(path, name, payload):
    (path / name).write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")


def material_map(session):
    return {m.key: m for m in session.scalars(select(Material))}


def snapshot(session, models):
    return {m.__tablename__: [tuple(row) for row in session.execute(select(m.__table__).order_by(m.id))]
            for m in models}


def test_recipe_catalog_exact_counts_and_formulas(session):
    for model, count in [(Material, 91), (IngredientGroup, 7), (IngredientGroupMember, 35),
                         (Recipe, 19), (RecipeIngredientSlot, 76), (RecipeIngredientOption, 87)]:
        assert session.scalar(select(func.count()).select_from(model).where(model.active.is_(True))) == count
    assert session.scalar(select(func.count()).select_from(Source)) == 220
    expected = {
        "beer": [[("grain", 5)], [("mineral-water", 6), ("purified-water", 3)],
                 [("leavening-agent", 2)], [("sugar", 1)]],
        "vinegar": [[("grain", 1)], [("fruit", 1)], [("leavening-agent", 1)], [("sugar", 1)]],
        "pickled-vegetables": [[("vegetable", 8)], [("vinegar", 4)],
                               [("leavening-agent", 2)], [("sugar", 2)]],
        "grilled-bird-meat": [[("bird-meat", 2)], [("deep-frying-oil", 6), ("cottonseed-oil", 6)],
                              [("cooking-wine", 2)], [("salt", 1)]],
        "dressing": [[("egg", 1)], [("olive-oil", 1)], [("water", 1)], [("salt", 2)]],
        "red-sauce": [[("base-sauce", 1)], [("meat", 1)],
                      [("mineral-water", 2), ("purified-water", 1)], [("sugar", 2)]],
        "white-sauce": [[("base-sauce", 1)], [("fruit", 1)], [("milk", 1)],
                        [("cooking-wine", 2)]],
        "tea-with-fine-scent": [[("flower", 4)], [("fruit", 4)],
                                [("mineral-water", 7), ("purified-water", 3)],
                                [("edible-honey", 3)]],
        "omelet": [[("grain", 5)], [("olive-oil", 2)], [("egg", 5)], [("salt", 2)]],
    }
    for slug, formula in expected.items():
        recipe = get_knowledge_recipe(session, slug)
        assert recipe.verification_status == "verified"
        assert recipe.required_skill_level == 1
        apprentice = {"pickled-vegetables", "tea-with-fine-scent", "omelet"}
        assert recipe.required_skill_tier == ("apprentice" if slug in apprentice else "beginner")
        assert [[(o.material_key or o.ingredient_group.key, o.required_quantity) for o in s.options]
                for s in recipe.ingredient_slots] == formula
    assert {g.key: len(g.members) for g in session.scalars(select(IngredientGroup))} == {
        "grain": 5, "fruit": 7, "vegetable": 5, "bird-meat": 3,
        "meat": 10, "flower": 3, "water": 2}
    forbidden = {"conversion_ratio", "quantity_multiplier", "quality_multiplier",
                 "white_equivalent", "global_quantity", "global_required_quantity"}
    assert not forbidden & set(IngredientGroup.__table__.columns.keys())
    assert not forbidden & set(IngredientGroupMember.__table__.columns.keys())
    assert "result_quantity" not in Recipe.__table__.columns
    sources = read("seed_sources.json")
    assert len({s["url"] for s in sources}) == len(sources)
    assert "materials" not in read("seed_projects.json")


def test_recipe_evidence_verification_and_source_boundaries(session):
    recipe_entity_types = {"ingredient_group", "recipe", "recipe_ingredient_option"}
    evidence = list(
        session.scalars(
            select(Evidence).where(Evidence.entity_type.in_(recipe_entity_types))
        )
    )
    assert len(evidence) == 292
    assert all(row.verification_status == "verified" for row in evidence)
    assert {row.last_verified_at.isoformat() for row in evidence} == {
        "2026-09-11",
        "2026-09-12",
    }

    official = session.get(Source, "cooking-grilled-bird-meat-official-2018")
    assert official is not None
    assert official.url == (
        "https://www.kr.playblackdesert.com/ko-KR/News/Detail?"
        "countryType=ko-KR&groupContentNo=905"
    )
    assert official.title == "2018년 7월 업데이트 안내"
    assert official.publisher == "Pearl Abyss"
    assert official.source_type == "official_patch"
    assert official.published_at.isoformat() == "2018-07-01"

    assert session.get(Source, "cooking-beer-community-2019").source_type == "community_guide"
    assert session.get(Source, "cooking-vinegar-community-2020").source_type == "community_guide"
    for source_id in (
        "codex-beer-9213",
        "codex-vinegar-9066",
        "codex-pickled-vegetables-9202",
        "codex-grilled-bird-meat-9492",
    ):
        assert session.get(Source, source_id).source_type == "third_party_database"

    def source_ids(seed_key):
        return {
            row.source_id
            for row in evidence
            if row.seed_key.split("::", maxsplit=1)[0] == seed_key
        }

    assert source_ids("recipe.pickled-vegetables.formula") == {
        "cooking-lara-event-2021",
        "cooking-vinegar-community-2020",
        "codex-pickled-vegetables-9202",
    }
    supported_by_official = {
        "recipe.grilled-bird-meat.skill",
        "recipe.grilled-bird-meat.ingredient.bird-meat.option.bird-meat.quantity",
        "recipe.grilled-bird-meat.ingredient.oil.option.deep-frying-oil.quantity",
        "recipe.grilled-bird-meat.ingredient.cooking-wine.option.cooking-wine.quantity",
        "recipe.grilled-bird-meat.ingredient.salt.option.salt.quantity",
    }
    assert {
        row.seed_key.split("::", maxsplit=1)[0]
        for row in evidence
        if row.source_id == official.id
    } == supported_by_official
    assert source_ids(
        "recipe.grilled-bird-meat.ingredient.oil.option.cottonseed-oil.quantity"
    ) == {"codex-grilled-bird-meat-9492"}
    assert source_ids("recipe.grilled-bird-meat.formula") == {
        "codex-grilled-bird-meat-9492"
    }


def test_recipe_reimport_preserves_all_stable_ids(session):
    models = (*DOMAIN, Material, ProjectMaterial, Evidence)
    before = snapshot(session, models)
    import_seed(session, DATA)
    import_seed(session, DATA)
    assert snapshot(session, models) == before


def test_legacy_to_shared_material_transition_preserves_user_inventory(tmp_path):
    directory = tmp_path / "legacy"
    directory.mkdir()
    for name in ("seed_sources.json", "seed_contents.json"):
        shutil.copy(DATA / name, directory / name)
    project = read("seed_projects.json")
    referenced = {r["material_key"] for p in project["projects"] for r in p["project_materials"]}
    project["materials"] = [r for r in read("seed_materials.json") if r["key"] in referenced]
    write(directory, "seed_projects.json", project)
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        import_seed(session, directory)
        old_ids = {m.key: m.id for m in session.scalars(select(Material))}
        assert len(old_ids) == 9
        session.add(UserMaterialInventory(material_id=old_ids["moon-vein-flax"], quantity=37,
                                         note="preserve", updated_at=datetime(2026, 9, 10, tzinfo=UTC)))
        session.commit()
        inventory = snapshot(session, (UserMaterialInventory,))
        project_rows = snapshot(session, (ProjectMaterial,))
        before = get_knowledge_project(session, "carrack-advance")
        import_seed(session, DATA)
        import_seed(session, DATA)
        assert all(material_map(session)[k].id == v for k, v in old_ids.items())
        assert snapshot(session, (UserMaterialInventory,)) == inventory
        assert snapshot(session, (ProjectMaterial,)) == project_rows
        assert get_knowledge_project(session, "carrack-advance") == before
        # Historical embedded catalogs cannot archive unrelated recipe materials.
        import_seed(session, directory)
        assert material_map(session)["beer"].active
        assert snapshot(session, (UserMaterialInventory,)) == inventory
        import_seed(session, DATA)
        assert len(material_map(session)) == 91
    engine.dispose()


def test_project_sync_does_not_archive_recipe_materials(session):
    before = snapshot(session, (Material, UserMaterialInventory))
    sync_projects(session, DATA, material_map(session))
    session.flush()
    assert snapshot(session, (Material, UserMaterialInventory)) == before


def test_shared_catalog_duplicate_authority_is_rejected(session, tmp_path):
    shutil.copy(DATA / "seed_materials.json", tmp_path / "seed_materials.json")
    write(tmp_path, "seed_projects.json", {"materials": [], "projects": []})
    before = snapshot(session, (Material,))
    with pytest.raises(ValueError, match="duplicate Material authority"):
        sync_materials(session, tmp_path)
    assert snapshot(session, (Material,)) == before


def test_missing_catalog_does_not_archive_and_shared_catalog_does(session, tmp_path):
    before = snapshot(session, (Material,))
    sync_materials(session, tmp_path)
    assert snapshot(session, (Material,)) == before
    write(tmp_path, "seed_materials.json", [])
    sync_materials(session, tmp_path)
    assert all(not m.active for m in session.scalars(select(Material)))
    sync_materials(session, DATA)
    assert snapshot(session, (Material,)) == before


@pytest.mark.parametrize("case", ["group-duplicate", "recipe-duplicate", "member-duplicate",
    "unknown-material", "unknown-group", "zero", "negative", "nan", "xor-both", "xor-neither",
    "process", "skill", "result", "source", "target", "slot-duplicate", "option-duplicate"])
def test_recipe_invalid_input_rejected_before_domain_changes(session, tmp_path, case):
    payload = read("seed_recipes.json")
    recipe = next(r for r in payload["recipes"] if r["slug"] == "beer")
    option = recipe["ingredients"][0]["options"][0]
    if case == "group-duplicate":
        payload["ingredient_groups"].append(deepcopy(payload["ingredient_groups"][0]))
    elif case == "recipe-duplicate":
        payload["recipes"].append(deepcopy(recipe))
    elif case == "member-duplicate":
        payload["ingredient_groups"][0]["members"].append(deepcopy(payload["ingredient_groups"][0]["members"][0]))
    elif case == "unknown-material":
        option.pop("ingredient_group_key")
        option["material_key"] = "missing"
    elif case == "unknown-group": option["ingredient_group_key"] = "missing"
    elif case == "zero": option["required_quantity"] = 0
    elif case == "negative": option["required_quantity"] = -1
    elif case == "nan": option["required_quantity"] = float("nan")
    elif case == "xor-both": option["material_key"] = "wheat"
    elif case == "xor-neither": option.pop("ingredient_group_key")
    elif case == "process": recipe["process_type"] = "processing"
    elif case == "skill": recipe["required_skill_level"] = 0
    elif case == "result": recipe["result_material_key"] = "missing"
    elif case == "source": recipe["evidence"][0]["source_ids"] = ["missing"]
    elif case == "target": recipe["evidence"][0]["entity_seed_key"] = "vinegar"
    elif case == "slot-duplicate": recipe["ingredients"].append(deepcopy(recipe["ingredients"][0]))
    elif case == "option-duplicate": recipe["ingredients"][0]["options"].append(deepcopy(option))
    write(tmp_path, "seed_recipes.json", payload)
    before = snapshot(session, DOMAIN)
    with pytest.raises(ValueError):
        sync_recipes(session, tmp_path, material_map(session))
    assert snapshot(session, DOMAIN) == before


def test_recipe_removed_children_and_evidence_archive_then_reactivate(session, tmp_path):
    before = snapshot(session, (*DOMAIN, Evidence))
    payload = read("seed_recipes.json")
    beer = next(r for r in payload["recipes"] if r["slug"] == "beer")
    removed_slot = beer["ingredients"].pop()
    removed_keys = {removed_slot["seed_key"], *[o["seed_key"] for o in removed_slot["options"]]}
    beer["evidence"] = [e for e in beer["evidence"] if e["entity_seed_key"] not in removed_keys]
    group = payload["ingredient_groups"][0]
    removed_member = group["members"].pop()
    write(tmp_path, "seed_recipes.json", payload)
    sync_recipes(session, tmp_path, material_map(session))
    assert session.scalar(select(RecipeIngredientSlot).where(
        RecipeIngredientSlot.seed_key == removed_slot["seed_key"])).active is False
    assert all(not e.active for e in session.scalars(select(Evidence).where(Evidence.entity_id.in_(removed_keys))))
    assert session.scalar(select(IngredientGroupMember).where(
        IngredientGroupMember.seed_key == removed_member["seed_key"])).active is False
    sync_recipes(session, DATA, material_map(session))
    assert snapshot(session, (*DOMAIN, Evidence)) == before


def test_removed_recipe_and_group_cascade_archive_with_same_ids(session, tmp_path):
    before = snapshot(session, (*DOMAIN, Evidence))
    write(tmp_path, "seed_recipes.json", {"ingredient_groups": [], "recipes": []})
    sync_recipes(session, tmp_path, material_map(session))
    assert all(not row.active for m in DOMAIN for row in session.scalars(select(m)))
    assert get_knowledge_recipe(session, "beer") is None
    sync_recipes(session, DATA, material_map(session))
    assert snapshot(session, (*DOMAIN, Evidence)) == before


def test_recipe_knowledge_api_identity_and_404(session):
    app.dependency_overrides[get_session] = lambda: session
    try:
        client = TestClient(app)  # No lifespan startup: dependency override uses the isolated fixture.
        data = client.get("/api/knowledge/recipes/beer").json()
        assert data["slug"] == "beer"
        assert data["result_material_key"] == "beer"
        assert data["ingredient_slots"][0]["options"][0]["ingredient_group"]["verification_status"] == "verified"
        assert data["sources"]
        assert "evidence_id" not in json.dumps(data)
        assert "owned_quantity" not in json.dumps(data)
        response = client.get("/api/knowledge/recipes/missing")
        assert response.status_code == 404
        assert response.json()["detail"] == "Recipe not found"
    finally:
        app.dependency_overrides.clear()


@pytest.mark.parametrize("query,slug", [("맥주", "beer"), ("beer", "beer"), ("감자", "beer"),
    ("식초", "vinegar"), ("새구이", "grilled-bird-meat"), ("곡물", "vinegar")])
def test_recipe_search_discovery_and_stable_ranking(session, query, slug):
    result = search_knowledge(session, query, 50)
    assert ("recipe", slug) in [(r.resource_type, r.slug) for r in result]
    assert len({(r.resource_type, r.slug) for r in result}) == len(result)
    assert all(len(r.matches) <= 3 for r in result)
    assert result == search_knowledge(session, query, 50)
    if query == "식초":
        recipes = [r.slug for r in result if r.resource_type == "recipe"]
        assert recipes.index("vinegar") < recipes.index("pickled-vegetables")


def test_recipe_read_and_export_independent_of_all_personal_state(session):
    before = get_knowledge_recipe(session, "beer")
    page = render_recipe_markdown(before)
    now = datetime(2026, 9, 10, tzinfo=UTC)
    materials = material_map(session)
    for key, quantity in [("beer", 999), ("wheat", 12345)]:
        session.add(UserMaterialInventory(material_id=materials[key].id, quantity=quantity,
                                         note="private recipe note", updated_at=now))
    content = session.scalar(select(Content).where(Content.slug == "cooking-current-system"))
    session.add(UserContentState(content_id=content.id, state="in_progress", note="private", updated_at=now))
    stage = session.scalar(select(ProjectStage))
    session.add(UserProjectStageState(stage_id=stage.id, completed=True, completed_at=now, updated_at=now))
    template = session.scalar(select(ChecklistTemplate).where(ChecklistTemplate.active.is_(True)))
    instance = ChecklistInstance(template_id=template.id, period_key="recipe-isolation",
                                 period_start=now, period_end=now + timedelta(days=7), generated_at=now)
    session.add(instance)
    session.flush()
    session.add(ChecklistItemState(instance_id=instance.id, template_item_id=template.items[0].id,
                                   completed=True, completed_at=now, note="private"))
    session.commit()
    personal = snapshot(session, (UserMaterialInventory, UserContentState, UserProjectStageState,
                                  ChecklistInstance, ChecklistItemState))
    assert get_knowledge_recipe(session, "beer") == before
    assert render_recipe_markdown(get_knowledge_recipe(session, "beer")) == page
    assert snapshot(session, (UserMaterialInventory, UserContentState, UserProjectStageState,
                              ChecklistInstance, ChecklistItemState)) == personal
    backup = export_user_backup(session, exported_at=now)
    assert backup.version == 1
    assert {r.material_key for r in backup.data.material_inventory} == {"beer", "wheat"}
