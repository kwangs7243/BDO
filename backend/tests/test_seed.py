from __future__ import annotations

from datetime import datetime
import json
from pathlib import Path
import shutil

from sqlalchemy import func, select

from app.checklists import get_current_checklists
from app.content import get_content_detail
from app.models import (
    ChecklistItemState,
    ChecklistTemplate,
    ChecklistTemplateItem,
    Content,
    ContentRequirement,
    ContentSection,
    ContentStep,
    Evidence,
    Reward,
    ScheduleRule,
    Source,
)
from app.periods import KST
from app.seed import import_seed


DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def _seed_copy(tmp_path: Path) -> Path:
    target = tmp_path / "data"
    shutil.copytree(DATA_DIR, target)
    return target


def _load(path: Path, name: str) -> list[dict]:
    return json.loads((path / name).read_text(encoding="utf-8"))


def _save(path: Path, name: str, rows: list[dict]) -> None:
    (path / name).write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")


def test_seed_import_is_idempotent(session) -> None:
    models = (
        Source,
        Content,
        ScheduleRule,
        ContentRequirement,
        ContentStep,
        Reward,
        ContentSection,
        ChecklistTemplate,
        ChecklistTemplateItem,
        Evidence,
    )
    before = tuple(session.scalar(select(func.count()).select_from(model)) for model in models)
    import_seed(session, DATA_DIR)
    after = tuple(session.scalar(select(func.count()).select_from(model)) for model in models)
    assert after == before


def test_nested_text_update_reuses_item_and_preserves_history(session, tmp_path) -> None:
    now = datetime(2026, 9, 2, 12, tzinfo=KST)
    instances = get_current_checklists(session, "weekly", now)
    original_item = session.scalar(
        select(ChecklistTemplateItem).where(
            ChecklistTemplateItem.seed_key == "garmoth.weekly-reward.status"
        )
    )
    original_id = original_item.id
    original_schedule = session.scalar(
        select(ScheduleRule).where(ScheduleRule.seed_key == "garmoth.attempt-reset")
    )
    original_requirement = session.scalar(
        select(ContentRequirement).where(
            ContentRequirement.seed_key == "blood-altar.party-size"
        )
    )
    schedule_id = original_schedule.id
    requirement_id = original_requirement.id
    state = session.scalar(
        select(ChecklistItemState).where(ChecklistItemState.template_item_id == original_id)
    )
    state.completed = True
    session.commit()

    data_dir = _seed_copy(tmp_path)
    rows = _load(data_dir, "seed_contents.json")
    garmoth = next(row for row in rows if row["slug"] == "garmoth")
    item = garmoth["checklists"][0]["items"][0]
    item["label"] = "변경된 주간 보상 확인 문구"
    item["details"] = "seed update"
    item["reward_hint"] = "updated hint"
    garmoth["schedules"][0]["notes"] = "변경된 초기화 안내"
    blood_altar = next(row for row in rows if row["slug"] == "blood-altar")
    blood_altar["requirements"][0]["description"] = "변경된 파티 조건 설명"
    _save(data_dir, "seed_contents.json", rows)
    import_seed(session, data_dir)

    updated = session.scalar(
        select(ChecklistTemplateItem).where(
            ChecklistTemplateItem.seed_key == "garmoth.weekly-reward.status"
        )
    )
    assert updated.id == original_id
    assert updated.label == "변경된 주간 보상 확인 문구"
    assert updated.reward_hint == "updated hint"
    assert session.get(ScheduleRule, schedule_id).notes == "변경된 초기화 안내"
    assert session.get(ContentRequirement, requirement_id).description == "변경된 파티 조건 설명"
    assert session.get(ChecklistItemState, state.id).completed is True
    assert session.get(ChecklistItemState, state.id).template_item_id == original_id
    assert instances


def test_removed_seed_item_is_archived_without_deleting_history(session, tmp_path) -> None:
    now = datetime(2026, 9, 2, 12, tzinfo=KST)
    get_current_checklists(session, "weekly", now)
    item = session.scalar(
        select(ChecklistTemplateItem).where(
            ChecklistTemplateItem.seed_key == "garmoth.weekly-reward.status"
        )
    )
    state = session.scalar(
        select(ChecklistItemState).where(ChecklistItemState.template_item_id == item.id)
    )
    state.completed = True
    session.commit()

    data_dir = _seed_copy(tmp_path)
    rows = _load(data_dir, "seed_contents.json")
    garmoth = next(row for row in rows if row["slug"] == "garmoth")
    garmoth["checklists"][0]["items"] = []
    _save(data_dir, "seed_contents.json", rows)
    import_seed(session, data_dir)

    session.refresh(item)
    assert item.active is False
    assert session.get(ChecklistItemState, state.id).completed is True
    current = get_current_checklists(session, "weekly", now)
    garmoth_current = next(row for row in current if row.content_slug == "garmoth")
    assert garmoth_current.items == []


def test_evidence_and_source_metadata_update_on_reimport(session, tmp_path) -> None:
    evidence = session.scalar(
        select(Evidence).where(Evidence.seed_key == "garmoth.summary::world-boss-guide")
    )
    evidence_id = evidence.id
    data_dir = _seed_copy(tmp_path)
    sources = _load(data_dir, "seed_sources.json")
    source = next(row for row in sources if row["id"] == "world-boss-guide")
    source["title"] = "갱신된 공식 가이드 제목"
    source["published_at"] = "2026-09-01"
    source["retrieved_at"] = "2026-09-03T09:00:00+09:00"
    source["region"] = "KR"
    _save(data_dir, "seed_sources.json", sources)
    contents = _load(data_dir, "seed_contents.json")
    garmoth = next(row for row in contents if row["slug"] == "garmoth")
    claim = next(row for row in garmoth["evidence"] if row["seed_key"] == "garmoth.summary")
    claim["note"] = "갱신된 evidence note"
    claim["verification_status"] = "needs_review"
    claim["last_verified_at"] = "2026-09-03"
    _save(data_dir, "seed_contents.json", contents)

    import_seed(session, data_dir)
    updated = session.get(Evidence, evidence_id)
    updated_source = session.get(Source, "world-boss-guide")
    assert updated.id == evidence_id
    assert updated.evidence_note == "갱신된 evidence note"
    assert updated.verification_status == "needs_review"
    assert updated.last_verified_at.isoformat() == "2026-09-03"
    assert updated_source.title == "갱신된 공식 가이드 제목"
    assert updated_source.published_at.isoformat() == "2026-09-01"
    assert updated_source.retrieved_at is not None
    assert updated_source.region == "KR"

    detail = get_content_detail(session, "garmoth", datetime(2026, 9, 3, 12, tzinfo=KST))
    exposed = next(row for row in detail.sources if row.id == "world-boss-guide")
    assert exposed.title == "갱신된 공식 가이드 제목"
    assert exposed.published_at.isoformat() == "2026-09-01"
    assert exposed.retrieved_at is not None
    assert exposed.region == "KR"
