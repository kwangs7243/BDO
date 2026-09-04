from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import (
    Content,
    ContentRelation,
    ContentRequirement,
    ContentSection,
    Evidence,
    Source,
    UserContentState,
)
from app.seed import import_seed


DATA_DIR = Path(__file__).resolve().parents[2] / "data"

V17B_SOURCE_IDS = {
    "grind-profit-update-2026-06-10",
    "dehkia-party-spots-2026-01-14",
    "dehkia-flow-update-2026-01-28",
    "black-energy-overflow-2026-03-18",
    "gabinya-coastal-cliff-2026-07-29",
    "edania-internal-launch-2026-08-12",
    "edania-internal-hotfix-2026-08-13",
    "edania-internal-balance-2026-08-19",
    "edania-internal-balance-2026-09-02",
    "marni-combat-analyzer-2026-08-05",
    "edania-external-history-2026-09-04",
    "hexe-pet-bottleneck-2026-07-17",
    "hexe-economy-discussion-2026-08-10",
    "orzekea-dsr-tungrad-2026-06-11",
    "silver-at-1600ap-2026-08-14",
    "v17b-provided-measurement-pack-2026-09-04",
}

V17B_SPOT_SLUGS = {
    "hexe-sanctuary-elvia",
    "yzrahid-highlands",
    "city-of-the-dead",
    "tungrad-ruins",
    "dokkebi-forest",
    "darkseekers-retreat",
    "golden-pig-cave",
    "lucky-golden-pig-cave",
    "dehkia-olun-ii",
    "dehkia-ash-ii",
    "dehkia-miru",
    "dehkia-gyfin-upper",
    "black-energy-overflow-zone",
    "gabinya-coastal-cliff",
    "aetherion",
    "nymphamare",
    "orbita",
    "tenebraum",
    "zephyros",
    "aphrodon-temple",
    "hermesia-citadel",
    "magaia-temple",
    "aresion-temple",
    "judgment-scales",
    "event-horizon",
}


def _requirement(session, seed_key: str) -> dict:
    row = session.scalar(
        select(ContentRequirement).where(ContentRequirement.seed_key == seed_key)
    )
    assert row is not None
    assert isinstance(row.structured_value, dict)
    return row.structured_value


def test_v17b_seed_json_is_unique_and_expected_rows_exist() -> None:
    sources = json.loads((DATA_DIR / "seed_sources.json").read_text(encoding="utf-8"))
    contents = json.loads((DATA_DIR / "seed_contents.json").read_text(encoding="utf-8"))
    source_ids = [row["id"] for row in sources]
    source_urls = [row["url"] for row in sources]
    slugs = [row["slug"] for row in contents]

    assert len(source_ids) == len(set(source_ids))
    assert len(source_urls) == len(set(source_urls))
    assert len(slugs) == len(set(slugs))
    assert V17B_SOURCE_IDS <= set(source_ids)
    assert V17B_SPOT_SLUGS <= set(slugs)
    assert "marni-combat-analyzer" in slugs


def test_v17b_current_attack_caps(session) -> None:
    expected = {
        "hexe-sanctuary-elvia": 1130,
        "yzrahid-highlands": 1180,
        "city-of-the-dead": 1295,
        "tungrad-ruins": 1395,
        "dokkebi-forest": 1445,
        "darkseekers-retreat": 1490,
        "golden-pig-cave": 1540,
        "dehkia-olun-ii": 1490,
        "dehkia-ash-ii": 1540,
        "dehkia-miru": 1595,
        "dehkia-gyfin-upper": 1680,
        "black-energy-overflow-zone": 1880,
        "gabinya-coastal-cliff": 2020,
    }
    for slug, cap in expected.items():
        assert _requirement(session, f"{slug}.current-stats")["ap_cap"] == cap

    for slug in {
        "aphrodon-temple",
        "hermesia-citadel",
        "magaia-temple",
        "aresion-temple",
        "judgment-scales",
        "event-horizon",
    }:
        assert _requirement(session, f"{slug}.current-stats")["explicit_ap_cap"] is None


def test_v17b_june_10_overrides_are_current(session) -> None:
    yzrahid = _requirement(session, "yzrahid-highlands.june-2026-current")
    city = _requirement(session, "city-of-the-dead.june-2026-current")

    assert (yzrahid["trash_min"], yzrahid["trash_max"], yzrahid["agris_cost"]) == (
        200,
        240,
        264,
    )
    assert (city["main_trash_min"], city["main_trash_max"]) == (4, 6)
    assert (city["commander_trash_min"], city["commander_trash_max"]) == (220, 250)
    assert city["essence_of_devouring_chance_change_percent"] == 20
    assert city["kabuua_artifact_available"] is True
    assert city["kabuua_fragment_available"] is True


def test_v17b_edania_current_values(session) -> None:
    overflow = _requirement(session, "black-energy-overflow-zone.current-stats")
    gabinya = _requirement(session, "gabinya-coastal-cliff.current-stats")
    gabinya_loot = _requirement(session, "gabinya-coastal-cliff.loot-agris")

    assert overflow == {
        "knowledge_role": "fact",
        "party_size": 3,
        "marni_realm_available": False,
        "sheet_ap_recommended": 385,
        "sheet_dp_recommended": 450,
        "final_ap_recommended": 1850,
        "final_dp_recommended": 760,
        "ap_cap": 1880,
        "crowd_control": ["knockdown", "bound"],
        "initial_regions": ["Orbita", "Zephyros"],
        "launched_at": "2026-03-18",
    }
    assert (
        gabinya["sheet_ap_recommended"],
        gabinya["sheet_dp_recommended"],
        gabinya["final_ap_recommended"],
        gabinya["final_dp_recommended"],
        gabinya["ap_cap"],
    ) == (400, 470, 1990, 820, 2020)
    assert gabinya_loot["trash_npc_price"] == 165508
    assert gabinya_loot["agris_costs"] == {
        "sulfur_volcano_colossus": None,
        "rock_or_stone_colossus": 16,
        "sulfur_stalagmite": 77,
    }

    expected = {
        "aphrodon-temple": (400, 2090, 470, 810),
        "hermesia-citadel": (405, 2220, 485, 830),
        "magaia-temple": (410, 2340, 490, 840),
        "aresion-temple": (415, 2455, 495, 850),
        "judgment-scales": (415, 2455, 500, 860),
        "event-horizon": (420, 2570, 505, 870),
    }
    for slug, values in expected.items():
        row = _requirement(session, f"{slug}.current-stats")
        assert (
            row["sheet_ap_recommended"],
            row["final_ap_recommended"],
            row["sheet_dp_recommended"],
            row["final_dp_recommended"],
        ) == values


def test_event_horizon_uses_september_2_values(session) -> None:
    current = _requirement(session, "event-horizon.current-2026-09-02")
    assert current["trash_ranges"] == {
        "corrupted_edana_or_lost_object": [2, 4],
        "guide_of_despair": [4, 8],
        "ibedor": [25, 35],
        "special_lost_object": [30, 35],
    }
    assert current["agris_costs"] == {
        "base_type": 18,
        "guide_of_despair": 36,
        "ibedor": 180,
        "special_lost_object": 198,
    }
    old = session.scalar(
        select(ContentRequirement).where(
            ContentRequirement.seed_key == "event-horizon.legacy-launch-values"
        )
    )
    evidence = session.scalar(
        select(Evidence).where(
            Evidence.seed_key
            == "event-horizon.claim.legacy-launch-values::edania-internal-launch-2026-08-12"
        )
    )
    assert old is not None and not old.active
    assert evidence is not None
    assert evidence.verification_status == "superseded" and not evidence.active


def test_measurements_remain_individual_and_separate_from_facts(session) -> None:
    rows = list(
        session.scalars(
            select(ContentRequirement)
            .join(Content)
            .where(Content.slug.in_(V17B_SPOT_SLUGS))
        )
    )
    roles = {
        row.seed_key: row.structured_value.get("knowledge_role")
        for row in rows
        if isinstance(row.structured_value, dict)
    }
    measurements = [
        row for row in rows if roles.get(row.seed_key) == "measurement"
    ]
    facts = [row for row in rows if roles.get(row.seed_key) == "fact"]

    assert len(measurements) >= 10
    assert {row.structured_value["measurement_grade"] for row in measurements} <= {
        "A",
        "B",
        "C",
    }
    assert all(
        row.structured_value.get("scope") in {
            "individual_session",
            "individual_comparison",
            "individual_reports",
            "limited_aggregate_by_one_reporter",
        }
        for row in measurements
    )
    assert all("measurement_grade" not in row.structured_value for row in facts)
    assert _requirement(session, "hexe-sanctuary-elvia.measurement-h1")[
        "trash_count"
    ] == 18000
    assert _requirement(session, "tungrad-ruins.measurement-t1")[
        "trash_min"
    ] == 30000
    assert _requirement(session, "darkseekers-retreat.measurement-d1-hour")[
        "trash_min"
    ] == 40000

    source = session.get(Source, "v17b-provided-measurement-pack-2026-09-04")
    assert source is not None and source.source_type == "community_measurement"
    evidence = list(
        session.scalars(
            select(Evidence).where(
                Evidence.source_id == "v17b-provided-measurement-pack-2026-09-04"
            )
        )
    )
    measurement_keys = {row.seed_key for row in measurements}
    measurement_evidence = [
        row
        for row in evidence
        if row.entity_id in measurement_keys
    ]
    assert len(measurement_evidence) == len(measurements)
    assert all(row.verification_status == "needs_review" for row in measurement_evidence)


def test_v17b_archive_scope_and_external_progression(session) -> None:
    contents = list(
        session.scalars(select(Content).where(Content.slug.in_(V17B_SPOT_SLUGS)))
    )
    assert len(contents) == len(V17B_SPOT_SLUGS)
    assert all(row.status == "active" for row in contents)

    inactive_requirements = {
        row.seed_key
        for row in session.scalars(
            select(ContentRequirement)
            .join(Content)
            .where(Content.slug.in_(V17B_SPOT_SLUGS), ~ContentRequirement.active)
        )
    }
    assert inactive_requirements == {
        "golden-pig-cave.legacy-release-stats",
        "event-horizon.legacy-launch-values",
    }

    for order, slug in enumerate(
        ["aetherion", "nymphamare", "orbita", "tenebraum", "zephyros"],
        start=1,
    ):
        assert _requirement(session, f"{slug}.progression")["progression_order"] == order


def test_v17b_ids_and_user_state_survive_reimport(session) -> None:
    watched_slugs = V17B_SPOT_SLUGS | {"marni-combat-analyzer"}
    before_content = {
        row.slug: row.id
        for row in session.scalars(select(Content).where(Content.slug.in_(watched_slugs)))
    }
    before_nested = {
        model.__name__: {
            row.seed_key: row.id
            for row in session.scalars(select(model))
            if row.seed_key and row.seed_key.split(".", 1)[0] in watched_slugs
        }
        for model in (ContentRequirement, ContentSection, ContentRelation, Evidence)
    }

    hexe = session.scalar(select(Content).where(Content.slug == "hexe-sanctuary-elvia"))
    state = UserContentState(
        content_id=hexe.id,
        state="in_progress",
        priority=2,
        note="V1.7B preservation marker",
        updated_at=datetime(2026, 9, 4, tzinfo=timezone.utc),
    )
    session.add(state)
    session.commit()

    import_seed(session, DATA_DIR)

    after_content = {
        row.slug: row.id
        for row in session.scalars(select(Content).where(Content.slug.in_(watched_slugs)))
    }
    after_nested = {
        model.__name__: {
            row.seed_key: row.id
            for row in session.scalars(select(model))
            if row.seed_key and row.seed_key.split(".", 1)[0] in watched_slugs
        }
        for model in (ContentRequirement, ContentSection, ContentRelation, Evidence)
    }
    preserved = session.get(UserContentState, state.id)
    assert before_content == after_content
    assert before_nested == after_nested
    assert preserved is not None
    assert (preserved.state, preserved.priority, preserved.note) == (
        "in_progress",
        2,
        "V1.7B preservation marker",
    )


def test_v17b_temp_db_migration_baseline_import_and_idempotence(
    tmp_path, monkeypatch
) -> None:
    db_path = tmp_path / "v17b-validation.db"
    database_url = f"sqlite:///{db_path.as_posix()}"
    monkeypatch.setenv("DATABASE_URL", database_url)

    backend_dir = Path(__file__).resolve().parents[1]
    alembic_config = Config(str(backend_dir / "alembic.ini"))
    alembic_config.set_main_option(
        "script_location", str(backend_dir / "alembic")
    )
    command.upgrade(alembic_config, "20260902_0001")
    command.upgrade(alembic_config, "head")

    source_rows = json.loads(
        (DATA_DIR / "seed_sources.json").read_text(encoding="utf-8")
    )
    content_rows = json.loads(
        (DATA_DIR / "seed_contents.json").read_text(encoding="utf-8")
    )
    baseline_dir = tmp_path / "v17a-seed"
    baseline_dir.mkdir()
    (baseline_dir / "seed_sources.json").write_text(
        json.dumps(
            [row for row in source_rows if row["id"] not in V17B_SOURCE_IDS],
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    (baseline_dir / "seed_contents.json").write_text(
        json.dumps(
            [
                row
                for row in content_rows
                if row["slug"] not in V17B_SPOT_SLUGS
                and row["slug"] != "marni-combat-analyzer"
            ],
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    engine = create_engine(database_url)
    with Session(engine, expire_on_commit=False) as db_session:
        import_seed(db_session, baseline_dir)
        baseline_ids = {
            row.slug: row.id
            for row in db_session.scalars(select(Content))
        }
        watched = db_session.scalar(
            select(Content).where(Content.slug == "grind-zone-attack-cap")
        )
        user_state = UserContentState(
            content_id=watched.id,
            state="in_progress",
            priority=1,
            note="temporary migration preservation marker",
            updated_at=datetime(2026, 9, 4, tzinfo=timezone.utc),
        )
        db_session.add(user_state)
        db_session.commit()

        import_seed(db_session, DATA_DIR)
        first_v17b_ids = {
            row.slug: row.id
            for row in db_session.scalars(
                select(Content).where(
                    Content.slug.in_(
                        V17B_SPOT_SLUGS | {"marni-combat-analyzer"}
                    )
                )
            )
        }
        first_nested_ids = {
            row.seed_key: row.id
            for row in db_session.scalars(select(ContentRequirement))
            if row.seed_key
            and row.seed_key.split(".", 1)[0]
            in V17B_SPOT_SLUGS | {"marni-combat-analyzer"}
        }

        import_seed(db_session, DATA_DIR)

        assert baseline_ids == {
            row.slug: row.id
            for row in db_session.scalars(
                select(Content).where(Content.slug.in_(baseline_ids))
            )
        }
        assert first_v17b_ids == {
            row.slug: row.id
            for row in db_session.scalars(
                select(Content).where(Content.slug.in_(first_v17b_ids))
            )
        }
        assert first_nested_ids == {
            row.seed_key: row.id
            for row in db_session.scalars(
                select(ContentRequirement).where(
                    ContentRequirement.seed_key.in_(first_nested_ids)
                )
            )
        }
        preserved = db_session.get(UserContentState, user_state.id)
        assert preserved is not None
        assert preserved.note == "temporary migration preservation marker"
        assert all(
            row.status == "active"
            for row in db_session.scalars(
                select(Content).where(Content.slug.in_(V17B_SPOT_SLUGS))
            )
        )
