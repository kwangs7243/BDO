from __future__ import annotations

from datetime import date, datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator


class SourceOut(BaseModel):
    evidence_id: int
    evidence_seed_key: str | None
    id: str
    title: str
    url: str
    publisher: str | None
    source_type: str
    published_at: date | None
    retrieved_at: datetime | None
    region: str
    entity_type: str
    entity_id: str
    claim_key: str
    verification_status: str
    last_verified_at: date
    evidence_note: str | None = None
    active: bool
    is_active: bool


class ScheduleOut(BaseModel):
    id: int
    seed_key: str | None
    rule_type: str
    recurrence_type: str
    weekday: int | None
    time_local: str | None
    fixed_datetime: datetime | None
    timezone: str
    notes: str | None
    next_occurrence: datetime | None = None


class ContentRequirementOut(BaseModel):
    seed_key: str
    kind: str
    title: str | None
    description: str
    structured_value: Any | None
    requirement_level: str
    order_no: int


class ContentStepOut(BaseModel):
    seed_key: str
    phase: str
    order_no: int
    title: str
    description: str
    checkable: bool


class RewardOut(BaseModel):
    seed_key: str
    name: str
    reward_type: str
    amount: float | None
    min_amount: float | None
    max_amount: float | None
    unit: str | None
    is_choice: bool
    choice_group: str | None
    recommendation: str | None
    notes: str | None
    order_no: int


class ContentSectionOut(BaseModel):
    seed_key: str
    section_type: str
    title: str
    body_markdown: str
    order_no: int


class ContentRelationOut(BaseModel):
    seed_key: str
    direction: str
    relation_type: str
    note: str | None
    order_no: int
    content_slug: str
    content_name_ko: str
    content_category: str


class UserContentStateValue(StrEnum):
    NOT_STARTED = "not_started"
    FOUNDATION = "foundation"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    PAUSED = "paused"
    IGNORE = "ignore"


class UserContentStateOut(BaseModel):
    state: UserContentStateValue = UserContentStateValue.NOT_STARTED
    priority: int | None = None
    note: str | None = None
    updated_at: datetime | None = None


class UserContentStateUpdate(BaseModel):
    state: UserContentStateValue
    priority: int | None = None
    note: str | None = None


class ProjectSummaryOut(BaseModel):
    slug: str
    name_ko: str
    content_slug: str | None
    active: bool
    completed_stage_count: int
    total_stage_count: int
    shortage_material_count: int


class ProjectMaterialSourceOut(BaseModel):
    seed_key: str
    content_slug: str
    content_name_ko: str
    quantity_per_completion: float | None
    notes: str | None
    order_no: int


class ProjectMaterialOut(BaseModel):
    seed_key: str
    material_key: str
    name_ko: str
    unit: str
    stage_seed_key: str | None
    required_quantity: float
    owned_quantity: float
    shortage: float
    notes: str | None
    order_no: int
    source_entity_type: str | None
    source_entity_seed_key: str | None
    sources: list[ProjectMaterialSourceOut]


class ProjectStageOut(BaseModel):
    id: int
    seed_key: str
    name: str
    description: str | None
    order_no: int
    completed: bool
    completed_at: datetime | None
    note: str | None
    dependencies: list[str]


class ProjectDetailOut(BaseModel):
    slug: str
    name_ko: str
    content_slug: str | None
    summary: str | None
    active: bool
    stages: list[ProjectStageOut]
    materials: list[ProjectMaterialOut]


class MaterialInventoryUpdate(BaseModel):
    quantity: float = Field(ge=0)
    note: str | None = None


class MaterialInventoryOut(BaseModel):
    material_key: str
    quantity: float
    note: str | None
    updated_at: datetime


class ProjectStageStateUpdate(BaseModel):
    completed: bool
    note: str | None = None


class ProjectStageStateOut(BaseModel):
    project_slug: str
    stage_id: int
    completed: bool
    completed_at: datetime | None
    note: str | None
    updated_at: datetime


class ContentSummaryOut(BaseModel):
    slug: str
    name_ko: str
    category: str
    summary: str | None
    status: str
    last_verified_at: date | None
    verification_status: str


class ChecklistStateOut(BaseModel):
    id: int
    template_item_id: int
    seed_key: str | None
    label: str
    details: str | None
    completed: bool
    completed_at: datetime | None
    note: str | None


class ChecklistInstanceOut(BaseModel):
    id: int
    template_id: int
    template_seed_key: str | None
    template_name: str
    content_slug: str | None
    period_key: str
    period_start: datetime
    period_end: datetime
    items: list[ChecklistStateOut]


class ContentDetailOut(ContentSummaryOut):
    purpose: str | None
    party_type: str | None
    difficulty: str | None
    requirements: list[ContentRequirementOut]
    sections: list[ContentSectionOut]
    steps: list[ContentStepOut]
    schedules: list[ScheduleOut]
    rewards: list[RewardOut]
    checklists: list[ChecklistInstanceOut]
    related_contents: list[ContentRelationOut]
    user_state: UserContentStateOut
    sources: list[SourceOut]


class ChecklistStateUpdate(BaseModel):
    completed: bool
    note: str | None = None


class PromptMode(StrEnum):
    CONTENT_ONBOARDING = "content_onboarding"
    WEEKLY_REVIEW = "weekly_review"


class PromptRequest(BaseModel):
    mode: PromptMode
    content_slug: str | None = None
    user_question: str = ""
    as_of: datetime

    @field_validator("as_of")
    @classmethod
    def require_timezone(cls, value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("as_of must be timezone-aware")
        return value


class PromptFact(BaseModel):
    claim: str
    verification_status: str
    last_verified_at: date | None = None
    source_title: str | None = None
    source_url: str | None = None
    source_type: str | None = None


class PromptChecklistItem(BaseModel):
    label: str
    completed: bool
    period_key: str


class PromptContextBundle(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    generated_at: datetime
    region: str = "KR"
    request_context: dict[str, str]
    user_state: list[str] = Field(default_factory=list)
    requirements: list[str] = Field(default_factory=list)
    canonical_facts: list[PromptFact] = Field(default_factory=list)
    steps: list[str] = Field(default_factory=list)
    schedules: list[str] = Field(default_factory=list)
    rewards: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    checklist: list[PromptChecklistItem] = Field(default_factory=list)
    project_state: list[str] = Field(default_factory=list)
    open_questions_or_conflicts: list[PromptFact] = Field(default_factory=list)
    sources: list[SourceOut] = Field(default_factory=list)
    user_question: str = ""


class PromptRenderOut(BaseModel):
    bundle: PromptContextBundle
    markdown: str
    character_count: int
    estimated_tokens: int
    over_budget: bool
