from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
import socket

from fastapi.testclient import TestClient
from sqlalchemy import select

from app.database import get_session
from app.main import app
from app.models import ChecklistItemState, Evidence, UserProjectStageState
from app.periods import KST
from app.projects import (
    get_project_detail,
    put_material_inventory,
    put_project_stage_state,
)
from app.prompt_bridge import build_context, render_markdown, render_result
from app.schemas import (
    MaterialInventoryUpdate,
    ProjectStageStateUpdate,
    PromptMode,
    PromptRequest,
)


FIXED_NOW = datetime(2026, 9, 2, 23, 0, tzinfo=KST)
GOLDEN_PATH = Path(__file__).with_name('golden') / 'carrack_project_optimizer.md'


def _client(session):
    def override_session():
        yield session

    app.dependency_overrides[get_session] = override_session
    return TestClient(app)


def _request(project_slug: str | None = 'carrack-advance') -> PromptRequest:
    return PromptRequest(
        mode=PromptMode.PROJECT_OPTIMIZER,
        project_slug=project_slug,
        user_question='이번 주 안에 최대한 빨리 끝내는 순서를 짜줘',
        as_of=FIXED_NOW,
    )


def _prepare_project_state(session) -> None:
    put_material_inventory(
        session,
        'moon-vein-flax',
        MaterialInventoryUpdate(quantity=40, note='창고 20, 거래소 예약 20'),
    )
    project = get_project_detail(session, 'carrack-advance')
    put_project_stage_state(
        session,
        project.slug,
        project.stages[0].id,
        ProjectStageStateUpdate(completed=True, note='파란 장비 강화 완료'),
    )
    stage_state = session.scalar(
        select(UserProjectStageState).where(
            UserProjectStageState.stage_id == project.stages[0].id
        )
    )
    stage_state.completed_at = datetime(2026, 9, 1, 0, 0, tzinfo=UTC)
    session.commit()


def test_project_prompt_requires_slug_and_returns_not_found(session) -> None:
    client = _client(session)
    try:
        missing = client.post(
            '/api/prompt/context',
            json={
                'mode': 'project_optimizer',
                'as_of': FIXED_NOW.isoformat(),
            },
        )
        unknown = client.post(
            '/api/prompt/context',
            json={
                'mode': 'project_optimizer',
                'project_slug': 'unknown-project',
                'as_of': FIXED_NOW.isoformat(),
            },
        )
    finally:
        app.dependency_overrides.clear()
        client.close()

    assert missing.status_code == 422
    assert missing.json()['detail'] == 'project_slug is required for project_optimizer'
    assert unknown.status_code == 404
    assert unknown.json()['detail'] == 'Project not found: unknown-project'


def test_project_prompt_is_deterministic_complete_and_golden(session) -> None:
    _prepare_project_state(session)
    initial = build_context(session, _request(), FIXED_NOW)
    first_state_id = session.scalar(select(ChecklistItemState.id).order_by(ChecklistItemState.id))
    first_state = session.get(ChecklistItemState, first_state_id)
    first_state.completed = True
    session.commit()

    first = build_context(session, _request(), FIXED_NOW)
    second = build_context(session, _request(), FIXED_NOW)
    first_markdown = render_markdown(first)
    second_markdown = render_markdown(second)
    project = get_project_detail(session, 'carrack-advance')

    assert first_markdown == second_markdown
    assert len([item for item in first.project_state if item.startswith('stage: ')]) == 4
    assert len([item for item in first.project_state if item.startswith('material: ')]) == 9
    moon = next(item for item in project.materials if item.material_key == 'moon-vein-flax')
    assert (
        f'shortage={moon.shortage:g} {moon.unit}; '
        'inventory_note=창고 20, 거래소 예약 20'
    ) in first_markdown
    assert 'status=completed' in first_markdown
    assert 'note=파란 장비 강화 완료' in first_markdown
    assert any(item.completed for item in first.checklist)
    assert any(not item.completed for item in first.checklist)
    assert len({item.evidence_id for item in first.sources}) == len(first.sources)

    related_names = {
        source.content_name_ko
        for material in project.materials
        for source in material.sources
    }
    assert all(
        any(item.label.startswith(f'[{name}]') for name in related_names)
        for item in first.checklist
    )
    assert any('quantity_per_completion=확인되지 않음' in item for item in first.project_state)
    assert first_markdown == GOLDEN_PATH.read_text(encoding='utf-8')
    assert initial.request_context['page'] == 'project/carrack-advance'


def test_project_prompt_maps_known_quantity_to_reward_evidence(session) -> None:
    bundle = build_context(session, _request(), FIXED_NOW)
    project = get_project_detail(session, 'carrack-advance')
    material, source = next(
        (material, source)
        for material in project.materials
        for source in material.sources
        if source.quantity_per_completion is not None
    )
    expected_claim = (
        f'{source.content_name_ko} acquisition quantity for {material.name_ko}: '
        f'{source.quantity_per_completion:g} {material.unit}'
    )
    facts = [*bundle.canonical_facts, *bundle.open_questions_or_conflicts]
    fact = next(item for item in facts if item.claim == expected_claim)
    assert fact.source_url is not None
    assert fact.source_type is not None


def test_project_prompt_separates_conflicting_lineage(session) -> None:
    project = get_project_detail(session, 'carrack-advance')
    material = project.materials[0]
    evidence = session.scalar(
        select(Evidence).where(
            Evidence.entity_id == material.source_entity_seed_key,
            Evidence.claim_key == 'description',
            Evidence.active.is_(True),
        )
    )
    evidence.verification_status = 'conflict'
    session.commit()

    bundle = build_context(session, _request(), FIXED_NOW)
    target = f'{material.name_ko} project requirement:'
    assert not any(item.claim.startswith(target) for item in bundle.canonical_facts)
    assert any(
        item.claim.startswith(target) and item.verification_status == 'conflict'
        for item in bundle.open_questions_or_conflicts
    )


def test_project_prompt_attempts_no_outbound_network(session, monkeypatch) -> None:
    def blocked_connect(*_args, **_kwargs):
        raise AssertionError('outbound network attempted')

    monkeypatch.setattr(socket.socket, 'connect', blocked_connect)
    result = render_result(build_context(session, _request(), FIXED_NOW))
    assert '## PROJECT_STATE' in result.markdown
    assert result.estimated_tokens > 0
