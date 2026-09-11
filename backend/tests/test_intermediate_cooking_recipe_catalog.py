from __future__ import annotations

from datetime import UTC, date, datetime
import json
from pathlib import Path
import shutil

from fastapi.testclient import TestClient
from pydantic import ValidationError
import pytest
from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import Session

from app.database import Base, get_session
from app.knowledge import get_knowledge_recipe
from app.main import app
from app.models import (
    Evidence, IngredientGroup, IngredientGroupMember, Material, Recipe,
    RecipeIngredientOption, RecipeIngredientSlot, Source, UserMaterialInventory,
)
from app.recipe_seed import COOKING_SKILL_TIERS, RecipeSeed
from app.seed import import_seed


DATA = Path(__file__).resolve().parents[2] / "data"

SOURCES = {
    "life-level-experience-guide": ("https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=431", "생활 레벨별 요구 경험치", "Pearl Abyss", "official_guide"),
    "codex-grilled-sausage-9427": ("https://bdocodex.com/kr/item/9427/", "구운 소시지", "BDO Codex", "third_party_database"),
    "weingchicken-grilled-sausage-19": ("https://apps.weingchicken.com/bd/makings/19", "구운 소시지 - 검은사막 제작노트", "위잉치킨", "third_party_database"),
    "codex-steak-9401": ("https://bdocodex.com/kr/item/9401/", "스테이크", "BDO Codex", "third_party_database"),
    "weingchicken-steak-312": ("https://apps.weingchicken.com/bd/makings/312", "스테이크 - 검은사막 제작노트", "위잉치킨", "third_party_database"),
    "codex-sute-tea-117": ("https://bdocodex.com/kr/recipe/117/", "수테차", "BDO Codex", "third_party_database"),
    "codex-sute-tea-special-560": ("https://bdocodex.com/kr/recipe/560/", "수테차", "BDO Codex", "third_party_database"),
    "weingchicken-healthy-sute-tea-222": ("https://apps.weingchicken.com/bd/makings/222", "몸에 좋은 수테차 - 검은사막 제작노트", "위잉치킨", "third_party_database"),
    "weingchicken-meat-sandwich-228": ("https://apps.weingchicken.com/bd/makings/228", "미트 샌드위치 - 검은사막 제작노트", "위잉치킨", "third_party_database"),
    "codex-ham-sandwich-136": ("https://bdocodex.com/kr/recipe/136/", "햄 샌드위치", "BDO Codex", "third_party_database"),
    "weingchicken-ham-sandwich-139": ("https://apps.weingchicken.com/bd/makings/139", "햄 샌드위치 - 검은사막 제작노트", "위잉치킨", "third_party_database"),
    "codex-frank-sandwich-360": ("https://bdocodex.com/kr/recipe/360/", "프랭크 샌드위치", "BDO Codex", "third_party_database"),
    "codex-frank-sandwich-smoked-361": ("https://bdocodex.com/kr/recipe/361/", "프랭크 샌드위치", "BDO Codex", "third_party_database"),
    "weingchicken-frank-sandwich-375": ("https://apps.weingchicken.com/bd/makings/375", "프랭크 샌드위치 - 검은사막 제작노트", "위잉치킨", "third_party_database"),
}

MATERIALS = {
    "grilled-sausage": "구운 소시지", "steak": "스테이크",
    "sute-tea": "수테차", "meat-sandwich": "미트 샌드위치",
    "ham-sandwich": "햄 샌드위치", "frank-sandwich": "프랭크 샌드위치",
    "onion": "양파", "pepper": "후추", "garlic": "마늘", "butter": "버터",
    "tea-with-strong-scent": "향이 진한 차", "soft-bread": "부드러운 빵",
    "cheese": "치즈", "smoked-sausage": "훈연 소시지",
}

FORMULAS = {
    "grilled-sausage": [[("meat", 6)], [("onion", 1)], [("salt", 2)], [("pepper", 2)]],
    "steak": [[("meat", 8)], [("garlic", 2)], [("red-sauce", 2)], [("salt", 2)]],
    "sute-tea": [[("tea-with-fine-scent", 2), ("tea-with-strong-scent", 1)], [("milk", 3)], [("salt", 1)], [("butter", 2)]],
    "meat-sandwich": [[("meat", 7)], [("soft-bread", 1)], [("vegetable", 6)], [("cheese", 3)]],
    "ham-sandwich": [[("grilled-sausage", 2), ("smoked-sausage", 1)], [("soft-bread", 2)], [("vegetable", 5)], [("egg", 4)]],
    "frank-sandwich": [[("grilled-sausage", 2), ("smoked-sausage", 1)], [("soft-bread", 1)], [("cabbage", 2)], [("red-sauce", 1)]],
}
SKILLS = {
    "grilled-sausage": ("beginner", 6), "steak": ("apprentice", 1),
    "sute-tea": ("skilled", 1), "meat-sandwich": ("apprentice", 6),
    "ham-sandwich": ("skilled", 1), "frank-sandwich": ("professional", 1),
}
FORMULA_SOURCES = {
    "grilled-sausage": {"codex-grilled-sausage-9427", "weingchicken-grilled-sausage-19"},
    "steak": {"codex-steak-9401", "weingchicken-steak-312"},
    "sute-tea": {"codex-sute-tea-117", "codex-sute-tea-special-560", "weingchicken-healthy-sute-tea-222"},
    "meat-sandwich": {"weingchicken-meat-sandwich-228", "inven-cooking-recipe-db"},
    "ham-sandwich": {"codex-ham-sandwich-136", "weingchicken-ham-sandwich-139", "inven-cooking-recipe-db"},
    "frank-sandwich": {"codex-frank-sandwich-360", "codex-frank-sandwich-smoked-361", "weingchicken-frank-sandwich-375"},
}
SKILL_SOURCES = {
    "grilled-sausage": FORMULA_SOURCES["grilled-sausage"],
    "steak": FORMULA_SOURCES["steak"], "sute-tea": {"codex-sute-tea-117"},
    "meat-sandwich": {"weingchicken-meat-sandwich-228"},
    "ham-sandwich": {"codex-ham-sandwich-136", "weingchicken-ham-sandwich-139"},
    "frank-sandwich": {"codex-frank-sandwich-360", "weingchicken-frank-sandwich-375"},
}
QUANTITY_SOURCES = {
    "grilled-sausage": {k: FORMULA_SOURCES["grilled-sausage"] for k in ("meat", "onion", "salt", "pepper")},
    "steak": {k: FORMULA_SOURCES["steak"] for k in ("meat", "garlic", "red-sauce", "salt")},
    "sute-tea": {
        "tea-with-fine-scent": {"codex-sute-tea-117", "weingchicken-healthy-sute-tea-222"},
        "tea-with-strong-scent": {"codex-sute-tea-special-560", "weingchicken-healthy-sute-tea-222"},
        **{k: FORMULA_SOURCES["sute-tea"] for k in ("milk", "salt", "butter")},
    },
    "meat-sandwich": {k: FORMULA_SOURCES["meat-sandwich"] for k in ("meat", "soft-bread", "vegetable", "cheese")},
    "ham-sandwich": {
        "grilled-sausage": FORMULA_SOURCES["ham-sandwich"],
        "smoked-sausage": {"weingchicken-ham-sandwich-139"},
        **{k: FORMULA_SOURCES["ham-sandwich"] for k in ("soft-bread", "vegetable", "egg")},
    },
    "frank-sandwich": {
        "grilled-sausage": {"codex-frank-sandwich-360", "weingchicken-frank-sandwich-375"},
        "smoked-sausage": {"codex-frank-sandwich-smoked-361", "weingchicken-frank-sandwich-375"},
        **{k: {"codex-frank-sandwich-360", "weingchicken-frank-sandwich-375"} for k in ("soft-bread", "cabbage", "red-sauce")},
    },
}
TEN_ATTEMPT_TOTALS = {
    slug: {target: quantity * 10 for slot in slots for target, quantity in slot}
    for slug, slots in FORMULAS.items()
}


def _formula(recipe):
    return [[
        (option.material_key or option.ingredient_group.key, option.required_quantity)
        for option in slot.options
    ] for slot in recipe.ingredient_slots]


def _source_ids(session, claim_key):
    return set(session.scalars(select(Evidence.source_id).where(
        Evidence.seed_key.like(f"{claim_key}::%"), Evidence.active.is_(True)
    )))


def _ids(session, model, identity):
    return {getattr(row, identity): row.id for row in session.scalars(select(model))}


def test_v19u_exact_counts_and_verified_evidence(session):
    for model, expected in (
        (Material, 78), (IngredientGroup, 7), (IngredientGroupMember, 35),
        (Recipe, 15), (RecipeIngredientSlot, 60), (RecipeIngredientOption, 67),
    ):
        assert session.scalar(select(func.count()).select_from(model).where(model.active.is_(True))) == expected
    assert session.scalar(select(func.count()).select_from(Source)) == 213
    catalog = json.loads((DATA / "seed_recipes.json").read_text(encoding="utf-8"))
    claims = [e for owner in [*catalog["ingredient_groups"], *catalog["recipes"]] for e in owner["evidence"]]
    assert len(claims) == len({e["seed_key"] for e in claims}) == 119
    rows = list(session.scalars(select(Evidence).where(
        Evidence.entity_type.in_({"ingredient_group", "recipe", "recipe_ingredient_option"}),
        Evidence.active.is_(True),
    )))
    # Exact packet source sets expand to 91 new rows: 115 + 91 = 206.
    assert len(rows) == 206
    assert all(row.verification_status == "verified" for row in rows)
    assert not any(row.verification_status == "needs_review" for row in rows)


def test_v19u_source_and_material_metadata(session):
    seed = json.loads((DATA / "seed_sources.json").read_text(encoding="utf-8"))
    assert len({row["id"] for row in seed}) == len(seed)
    assert len({row["url"] for row in seed}) == len(seed)
    assert not any("/kr/recipe/591/" in row["url"] for row in seed)
    by_id = {row["id"]: row for row in seed}
    for source_id, expected in SOURCES.items():
        row = by_id[source_id]
        assert (row["url"], row["title"], row["publisher"], row["source_type"]) == expected
        assert row["published_at"] is None
        assert row["retrieved_at"] == "2026-09-11T20:16:00+09:00"
        assert row["region"] == "KR"
        assert row["notes"]
        assert session.get(Source, source_id).source_type == expected[3]
    material_seed = {row["key"]: row for row in json.loads(
        (DATA / "seed_materials.json").read_text(encoding="utf-8")
    )}
    for key, name in MATERIALS.items():
        assert material_seed[key] == {"key": key, "name_ko": name, "unit": "개", "active": True}


def test_v19u_formulas_skills_stable_keys_and_evidence_ownership(session):
    for slug, expected in FORMULAS.items():
        recipe = get_knowledge_recipe(session, slug)
        assert recipe is not None
        assert _formula(recipe) == expected
        assert (recipe.required_skill_tier, recipe.required_skill_level) == SKILLS[slug]
        assert recipe.verification_status == "verified"
        assert _source_ids(session, f"recipe.{slug}.formula") == FORMULA_SOURCES[slug]
        assert _source_ids(session, f"recipe.{slug}.skill") == SKILL_SOURCES[slug]
        assert _source_ids(session, f"recipe.{slug}.attempt") == {"cooking-guide"}
        for slot in recipe.ingredient_slots:
            assert slot.seed_key.startswith(f"{slug}.ingredient.")
            for option in slot.options:
                target = option.material_key or option.ingredient_group.key
                assert option.seed_key.startswith(f"{slot.seed_key}.option.")
                assert _source_ids(session, f"recipe.{option.seed_key}.quantity") == QUANTITY_SOURCES[slug][target]
    assert not session.scalars(select(Evidence).where(
        Evidence.source_id == "life-level-experience-guide"
    )).first()


@pytest.mark.parametrize("tier", sorted(COOKING_SKILL_TIERS))
def test_all_current_cooking_skill_tiers_are_accepted(tier):
    seed = RecipeSeed(
        slug="tier-validation", name_ko="등급 검증", process_type="cooking",
        result_material_key="beer", required_skill_tier=tier,
        required_skill_level=1, last_verified_at=date(2026, 9, 11),
    )
    assert seed.required_skill_tier == tier
    assert COOKING_SKILL_TIERS == {
        "beginner", "apprentice", "skilled", "professional", "artisan", "master", "guru"
    }


@pytest.mark.parametrize("tier", ["novice", "expert", "legend", "숙련", "전문", ""])
def test_unknown_or_localized_cooking_skill_tiers_are_rejected(tier):
    with pytest.raises(ValidationError, match="unsupported cooking skill tier"):
        RecipeSeed(
            slug="tier-validation", name_ko="등급 검증", process_type="cooking",
            result_material_key="beer", required_skill_tier=tier,
            required_skill_level=1, last_verified_at=date(2026, 9, 11),
        )


def test_v19u_keeps_quality_output_and_recursion_out_of_model():
    forbidden = {
        "conversion_ratio", "quantity_multiplier", "quality_multiplier",
        "special_food_multiplier", "special_result_probability", "proc_rate",
        "result_quantity", "expected_output", "recipe_dag",
    }
    columns = set().union(*(
        set(model.__table__.columns.keys()) for model in
        (Recipe, RecipeIngredientOption, IngredientGroup, IngredientGroupMember)
    ))
    assert forbidden.isdisjoint(columns)


@pytest.mark.parametrize("slug", FORMULAS)
def test_v19u_read_search_and_ten_attempt_calculation(session, slug):
    app.dependency_overrides[get_session] = lambda: session
    client = TestClient(app)
    try:
        detail = client.get(f"/api/knowledge/recipes/{slug}")
        assert detail.status_code == 200
        payload = detail.json()
        assert (payload["required_skill_tier"], payload["required_skill_level"]) == SKILLS[slug]
        search = client.get("/api/knowledge/search", params={"q": payload["name_ko"], "limit": 50})
        assert ("recipe", slug) in {
            (item["resource_type"], item["slug"]) for item in search.json()
        }
        calculated = client.post(
            f"/api/calculations/recipes/{slug}", json={"attempt_count": 10}
        )
        assert calculated.status_code == 200
        result = calculated.json()
        options = [o for slot in result["ingredient_slots"] for o in slot["options"]]
        assert {
            o["material_key"] or o["ingredient_group"]["key"]: o["total_required_quantity"]
            for o in options
        } == TEN_ATTEMPT_TOTALS[slug]
        assert "selected_option" not in result
        assert all("combined_quantity" not in slot for slot in result["ingredient_slots"])
    finally:
        app.dependency_overrides.clear()
        client.close()


def test_v19t_ids_semantics_and_inventory_survive_transition(tmp_path):
    baseline = tmp_path / "v19t"
    baseline.mkdir()
    for path in DATA.glob("*.json"):
        shutil.copy(path, baseline / path.name)
    source_rows = json.loads((DATA / "seed_sources.json").read_text(encoding="utf-8"))
    material_rows = json.loads((DATA / "seed_materials.json").read_text(encoding="utf-8"))
    catalog = json.loads((DATA / "seed_recipes.json").read_text(encoding="utf-8"))
    (baseline / "seed_sources.json").write_text(json.dumps(
        [row for row in source_rows if row["id"] not in SOURCES], ensure_ascii=False
    ), encoding="utf-8")
    (baseline / "seed_materials.json").write_text(json.dumps(
        [row for row in material_rows if row["key"] not in MATERIALS], ensure_ascii=False
    ), encoding="utf-8")
    catalog["recipes"] = [row for row in catalog["recipes"] if row["slug"] not in FORMULAS]
    (baseline / "seed_recipes.json").write_text(
        json.dumps(catalog, ensure_ascii=False), encoding="utf-8"
    )

    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    with Session(engine, expire_on_commit=False) as db:
        import_seed(db, baseline)
        old_slugs = {
            "beer", "vinegar", "pickled-vegetables", "grilled-bird-meat",
            "dressing", "red-sauce", "white-sauce", "tea-with-fine-scent", "omelet",
        }
        old_dtos = {slug: get_knowledge_recipe(db, slug).model_dump(mode="json") for slug in old_slugs}
        identity = {
            Material: "key", IngredientGroup: "key", IngredientGroupMember: "seed_key",
            Recipe: "slug", RecipeIngredientSlot: "seed_key",
            RecipeIngredientOption: "seed_key", Evidence: "seed_key",
        }
        ids = {model: _ids(db, model, key) for model, key in identity.items()}
        red_sauce = db.scalar(select(Material).where(Material.key == "red-sauce"))
        db.add(UserMaterialInventory(
            material_id=red_sauce.id,
            quantity=17,
            note="preserve",
            updated_at=datetime(2026, 9, 11, tzinfo=UTC),
        ))
        db.commit()

        import_seed(db, DATA)
        import_seed(db, DATA)

        for model, before in ids.items():
            after = _ids(db, model, identity[model])
            assert {key: after[key] for key in before} == before
        assert {
            slug: get_knowledge_recipe(db, slug).model_dump(mode="json")
            for slug in old_slugs
        } == old_dtos
        inventory = db.scalar(select(UserMaterialInventory).where(
            UserMaterialInventory.material_id == red_sauce.id
        ))
        assert (inventory.quantity, inventory.note) == (17, "preserve")
    engine.dispose()
