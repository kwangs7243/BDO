from __future__ import annotations

from contextlib import asynccontextmanager
from datetime import UTC, datetime

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.checklists import get_current_checklists
from app.content import get_content_detail, list_contents
from app.database import create_schema, get_session
from app.models import ChecklistItemState, Content, UserContentState
from app.periods import KST, SUNDAY, daily_period, next_weekly_occurrence, weekly_period
from app.prompt_bridge import build_context, render_result
from app.projects import (
    get_project_detail,
    list_projects,
    put_material_inventory,
    put_project_stage_state,
)
from app.schemas import (
    ChecklistInstanceOut,
    ChecklistStateOut,
    ChecklistStateUpdate,
    ContentDetailOut,
    ContentSummaryOut,
    PromptContextBundle,
    PromptRenderOut,
    PromptRequest,
    MaterialInventoryOut,
    MaterialInventoryUpdate,
    ProjectDetailOut,
    ProjectStageStateOut,
    ProjectStageStateUpdate,
    ProjectSummaryOut,
    UserContentStateOut,
    UserContentStateUpdate,
)


@asynccontextmanager
async def lifespan(_: FastAPI):
    create_schema()
    yield


app = FastAPI(title="BDO Companion API", version="0.1.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def now_kst() -> datetime:
    return datetime.now(KST)


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok", "timezone": "Asia/Seoul", "llm_transport": "disabled"}


@app.get("/api/contents", response_model=list[ContentSummaryOut])
def contents(session: Session = Depends(get_session)):
    return list_contents(session)


@app.get("/api/contents/{slug}", response_model=ContentDetailOut)
def content_detail(slug: str, session: Session = Depends(get_session)):
    result = get_content_detail(session, slug, now_kst())
    if result is None:
        raise HTTPException(status_code=404, detail="Content not found")
    return result


@app.get("/api/checklists/current", response_model=list[ChecklistInstanceOut])
def current_checklists(
    scope: str = Query(pattern="^(daily|weekly)$"),
    session: Session = Depends(get_session),
):
    return get_current_checklists(session, scope, now_kst())


@app.patch("/api/checklists/states/{state_id}", response_model=ChecklistStateOut)
def update_checklist_state(
    state_id: int,
    update: ChecklistStateUpdate,
    session: Session = Depends(get_session),
):
    state = session.get(ChecklistItemState, state_id)
    if state is None:
        raise HTTPException(status_code=404, detail="Checklist state not found")
    state.completed = update.completed
    state.completed_at = datetime.now(UTC) if update.completed else None
    state.note = update.note
    session.commit()
    session.refresh(state)
    return ChecklistStateOut(
        id=state.id,
        template_item_id=state.template_item_id,
        seed_key=state.template_item.seed_key,
        label=state.template_item.label,
        details=state.template_item.details,
        completed=state.completed,
        completed_at=(
            state.completed_at.replace(tzinfo=UTC)
            if state.completed_at is not None and state.completed_at.tzinfo is None
            else state.completed_at
        ),
        note=state.note,
    )


@app.get("/api/contents/{slug}/state", response_model=UserContentStateOut)
def get_user_content_state(slug: str, session: Session = Depends(get_session)):
    content = session.scalar(select(Content).where(Content.slug == slug))
    if content is None:
        raise HTTPException(status_code=404, detail="Content not found")
    state = session.scalar(select(UserContentState).where(UserContentState.content_id == content.id))
    if state is None:
        return UserContentStateOut()
    return UserContentStateOut(
        state=state.state,
        priority=state.priority,
        note=state.note,
        updated_at=(
            state.updated_at.replace(tzinfo=UTC) if state.updated_at.tzinfo is None else state.updated_at
        ),
    )


@app.put("/api/contents/{slug}/state", response_model=UserContentStateOut)
def put_user_content_state(
    slug: str,
    update: UserContentStateUpdate,
    session: Session = Depends(get_session),
):
    content = session.scalar(select(Content).where(Content.slug == slug))
    if content is None:
        raise HTTPException(status_code=404, detail="Content not found")
    state = session.scalar(select(UserContentState).where(UserContentState.content_id == content.id))
    now = datetime.now(UTC)
    if state is None:
        state = UserContentState(content_id=content.id, updated_at=now)
        session.add(state)
    state.state = update.state.value
    state.priority = update.priority
    state.note = update.note
    state.updated_at = now
    session.commit()
    return UserContentStateOut(
        state=state.state,
        priority=state.priority,
        note=state.note,
        updated_at=state.updated_at.replace(tzinfo=UTC) if state.updated_at.tzinfo is None else state.updated_at,
    )


@app.get("/api/projects", response_model=list[ProjectSummaryOut])
def projects(session: Session = Depends(get_session)):
    return list_projects(session)


@app.get("/api/projects/{slug}", response_model=ProjectDetailOut)
def project_detail(slug: str, session: Session = Depends(get_session)):
    result = get_project_detail(session, slug)
    if result is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return result


@app.put("/api/materials/{material_key}/inventory", response_model=MaterialInventoryOut)
def update_material_inventory(
    material_key: str,
    update: MaterialInventoryUpdate,
    session: Session = Depends(get_session),
):
    try:
        return put_material_inventory(session, material_key, update)
    except LookupError as error:
        raise HTTPException(status_code=404, detail="Material not found") from error


@app.put(
    "/api/projects/{project_slug}/stages/{stage_id}/state",
    response_model=ProjectStageStateOut,
)
def update_project_stage_state(
    project_slug: str,
    stage_id: int,
    update: ProjectStageStateUpdate,
    session: Session = Depends(get_session),
):
    try:
        return put_project_stage_state(session, project_slug, stage_id, update)
    except LookupError as error:
        raise HTTPException(status_code=404, detail="Project stage not found") from error


@app.get("/api/dashboard")
def dashboard(session: Session = Depends(get_session)):
    now = now_kst()
    daily = daily_period(now)
    weekly = weekly_period(now)
    return {
        "now": now,
        "reset_groups": [
            {"kind": "daily", "label": "일일 초기화", "next_at": daily.end},
            {"kind": "weekly", "label": "목요일 주간 초기화", "next_at": weekly.end},
            {
                "kind": "reward_payout",
                "label": "일요일 보상 지급",
                "next_at": next_weekly_occurrence(now, SUNDAY),
            },
        ],
        "daily": get_current_checklists(session, "daily", now),
        "weekly": get_current_checklists(session, "weekly", now),
    }


@app.post("/api/prompt/context", response_model=PromptContextBundle)
def prompt_context(request: PromptRequest, session: Session = Depends(get_session)):
    try:
        return build_context(session, request, request.as_of)
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error
    except LookupError as error:
        raise HTTPException(status_code=404, detail=f"Content not found: {error}") from error


@app.post("/api/prompt/render", response_model=PromptRenderOut)
def prompt_render(request: PromptRequest, session: Session = Depends(get_session)):
    try:
        return render_result(build_context(session, request, request.as_of))
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error
    except LookupError as error:
        raise HTTPException(status_code=404, detail=f"Content not found: {error}") from error
