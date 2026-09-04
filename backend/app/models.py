from __future__ import annotations

from datetime import date, datetime, time

from sqlalchemy import (
    JSON,
    Boolean,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    Time,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Source(Base):
    __tablename__ = "source"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    url: Mapped[str] = mapped_column(Text, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    publisher: Mapped[str | None] = mapped_column(String(120))
    source_type: Mapped[str] = mapped_column(String(32), nullable=False)
    published_at: Mapped[date | None] = mapped_column(Date)
    retrieved_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    region: Mapped[str] = mapped_column(String(16), default="KR", nullable=False)


class Content(Base):
    __tablename__ = "content"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    slug: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    name_ko: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(64), nullable=False)
    subcategory: Mapped[str | None] = mapped_column(String(64))
    summary: Mapped[str | None] = mapped_column(Text)
    purpose: Mapped[str | None] = mapped_column(Text)
    party_type: Mapped[str | None] = mapped_column(String(32))
    difficulty: Mapped[str | None] = mapped_column(String(32))
    status: Mapped[str] = mapped_column(String(32), default="active", nullable=False)
    last_verified_at: Mapped[date | None] = mapped_column(Date)

    schedules: Mapped[list[ScheduleRule]] = relationship(back_populates="content", cascade="all, delete-orphan")
    requirements: Mapped[list[ContentRequirement]] = relationship(
        back_populates="content", cascade="all, delete-orphan"
    )
    steps: Mapped[list[ContentStep]] = relationship(back_populates="content", cascade="all, delete-orphan")
    rewards: Mapped[list[Reward]] = relationship(back_populates="content", cascade="all, delete-orphan")
    sections: Mapped[list[ContentSection]] = relationship(back_populates="content", cascade="all, delete-orphan")
    checklist_templates: Mapped[list[ChecklistTemplate]] = relationship(
        back_populates="content", cascade="all, delete-orphan"
    )
    outgoing_relations: Mapped[list[ContentRelation]] = relationship(
        back_populates="from_content",
        foreign_keys="ContentRelation.from_content_id",
        cascade="all, delete-orphan",
    )
    incoming_relations: Mapped[list[ContentRelation]] = relationship(
        back_populates="to_content",
        foreign_keys="ContentRelation.to_content_id",
        cascade="all, delete-orphan",
    )
    user_state: Mapped[UserContentState | None] = relationship(
        back_populates="content", cascade="all, delete-orphan", uselist=False
    )


class ScheduleRule(Base):
    __tablename__ = "schedule_rule"
    __table_args__ = (UniqueConstraint("content_id", "seed_key", name="uq_schedule_rule_seed_key"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content_id: Mapped[int] = mapped_column(ForeignKey("content.id"), nullable=False)
    seed_key: Mapped[str | None] = mapped_column(String(160))
    rule_type: Mapped[str] = mapped_column(String(32), nullable=False)
    timezone: Mapped[str] = mapped_column(String(64), default="Asia/Seoul", nullable=False)
    recurrence_type: Mapped[str] = mapped_column(String(32), nullable=False)
    weekday: Mapped[int | None] = mapped_column(Integer)
    time_local: Mapped[time | None] = mapped_column(Time)
    fixed_datetime: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    effective_from: Mapped[date | None] = mapped_column(Date)
    effective_to: Mapped[date | None] = mapped_column(Date)
    notes: Mapped[str | None] = mapped_column(Text)
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    content: Mapped[Content] = relationship(back_populates="schedules")


class Evidence(Base):
    __tablename__ = "evidence"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    seed_key: Mapped[str | None] = mapped_column(String(255), unique=True)
    entity_type: Mapped[str] = mapped_column(String(32), nullable=False)
    entity_id: Mapped[str] = mapped_column(String(128), nullable=False)
    claim_key: Mapped[str] = mapped_column(String(128), nullable=False)
    source_id: Mapped[str] = mapped_column(ForeignKey("source.id"), nullable=False)
    evidence_note: Mapped[str | None] = mapped_column(Text)
    verification_status: Mapped[str] = mapped_column(String(32), nullable=False)
    last_verified_at: Mapped[date] = mapped_column(Date, nullable=False)
    superseded_by: Mapped[int | None] = mapped_column(ForeignKey("evidence.id"))
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    source: Mapped[Source] = relationship(foreign_keys=[source_id])

    @property
    def is_active(self) -> bool:
        """Current aggregation excludes archived or explicitly superseded evidence."""

        return self.active and self.verification_status != "superseded" and self.superseded_by is None


class ContentRequirement(Base):
    __tablename__ = "content_requirement"
    __table_args__ = (UniqueConstraint("content_id", "seed_key", name="uq_content_requirement_seed_key"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content_id: Mapped[int] = mapped_column(ForeignKey("content.id"), nullable=False)
    seed_key: Mapped[str] = mapped_column(String(160), nullable=False)
    kind: Mapped[str] = mapped_column(String(32), nullable=False)
    title: Mapped[str | None] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text, nullable=False)
    structured_value: Mapped[dict[str, object] | list[object] | None] = mapped_column(JSON)
    requirement_level: Mapped[str] = mapped_column(String(32), nullable=False)
    order_no: Mapped[int] = mapped_column(Integer, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    content: Mapped[Content] = relationship(back_populates="requirements")


class ContentStep(Base):
    __tablename__ = "content_step"
    __table_args__ = (UniqueConstraint("content_id", "seed_key", name="uq_content_step_seed_key"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content_id: Mapped[int] = mapped_column(ForeignKey("content.id"), nullable=False)
    seed_key: Mapped[str] = mapped_column(String(160), nullable=False)
    phase: Mapped[str] = mapped_column(String(32), nullable=False)
    order_no: Mapped[int] = mapped_column(Integer, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    checkable: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    content: Mapped[Content] = relationship(back_populates="steps")


class Reward(Base):
    __tablename__ = "reward"
    __table_args__ = (UniqueConstraint("content_id", "seed_key", name="uq_reward_seed_key"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content_id: Mapped[int] = mapped_column(ForeignKey("content.id"), nullable=False)
    seed_key: Mapped[str] = mapped_column(String(160), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    reward_type: Mapped[str] = mapped_column(String(64), nullable=False)
    amount: Mapped[float | None] = mapped_column(Float)
    min_amount: Mapped[float | None] = mapped_column(Float)
    max_amount: Mapped[float | None] = mapped_column(Float)
    unit: Mapped[str | None] = mapped_column(String(64))
    is_choice: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    choice_group: Mapped[str | None] = mapped_column(String(120))
    recommendation: Mapped[str | None] = mapped_column(Text)
    notes: Mapped[str | None] = mapped_column(Text)
    order_no: Mapped[int] = mapped_column(Integer, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    content: Mapped[Content] = relationship(back_populates="rewards")


class ContentSection(Base):
    __tablename__ = "content_section"
    __table_args__ = (UniqueConstraint("content_id", "seed_key", name="uq_content_section_seed_key"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content_id: Mapped[int] = mapped_column(ForeignKey("content.id"), nullable=False)
    seed_key: Mapped[str] = mapped_column(String(160), nullable=False)
    section_type: Mapped[str] = mapped_column(String(32), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    body_markdown: Mapped[str] = mapped_column(Text, nullable=False)
    order_no: Mapped[int] = mapped_column(Integer, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    content: Mapped[Content] = relationship(back_populates="sections")


class ContentRelation(Base):
    __tablename__ = "content_relation"
    __table_args__ = (UniqueConstraint("from_content_id", "seed_key", name="uq_content_relation_seed_key"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    from_content_id: Mapped[int] = mapped_column(ForeignKey("content.id"), nullable=False)
    to_content_id: Mapped[int] = mapped_column(ForeignKey("content.id"), nullable=False)
    seed_key: Mapped[str] = mapped_column(String(160), nullable=False)
    relation_type: Mapped[str] = mapped_column(String(32), nullable=False)
    note: Mapped[str | None] = mapped_column(Text)
    order_no: Mapped[int] = mapped_column(Integer, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    from_content: Mapped[Content] = relationship(
        back_populates="outgoing_relations", foreign_keys=[from_content_id]
    )
    to_content: Mapped[Content] = relationship(back_populates="incoming_relations", foreign_keys=[to_content_id])


class ChecklistTemplate(Base):
    __tablename__ = "checklist_template"
    __table_args__ = (UniqueConstraint("content_id", "seed_key", name="uq_checklist_template_seed_key"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content_id: Mapped[int | None] = mapped_column(ForeignKey("content.id"))
    seed_key: Mapped[str | None] = mapped_column(String(160))
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    recurrence_scope: Mapped[str] = mapped_column(String(32), nullable=False)
    period_rule_id: Mapped[int | None] = mapped_column(ForeignKey("schedule_rule.id"))
    enabled_default: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    content: Mapped[Content | None] = relationship(back_populates="checklist_templates")
    period_rule: Mapped[ScheduleRule | None] = relationship(foreign_keys=[period_rule_id])
    items: Mapped[list[ChecklistTemplateItem]] = relationship(
        back_populates="template", cascade="all, delete-orphan", order_by="ChecklistTemplateItem.order_no"
    )
    instances: Mapped[list[ChecklistInstance]] = relationship(back_populates="template")


class ChecklistTemplateItem(Base):
    __tablename__ = "checklist_template_item"
    __table_args__ = (UniqueConstraint("template_id", "seed_key", name="uq_checklist_item_seed_key"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    template_id: Mapped[int] = mapped_column(ForeignKey("checklist_template.id"), nullable=False)
    seed_key: Mapped[str | None] = mapped_column(String(160))
    order_no: Mapped[int] = mapped_column(Integer, nullable=False)
    label: Mapped[str] = mapped_column(String(255), nullable=False)
    details: Mapped[str | None] = mapped_column(Text)
    reward_hint: Mapped[str | None] = mapped_column(Text)
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    template: Mapped[ChecklistTemplate] = relationship(back_populates="items")


class ChecklistInstance(Base):
    __tablename__ = "checklist_instance"
    __table_args__ = (UniqueConstraint("template_id", "period_key", name="uq_checklist_period"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    template_id: Mapped[int] = mapped_column(ForeignKey("checklist_template.id"), nullable=False)
    period_key: Mapped[str] = mapped_column(String(100), nullable=False)
    period_start: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    period_end: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    generated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    template: Mapped[ChecklistTemplate] = relationship(back_populates="instances")
    states: Mapped[list[ChecklistItemState]] = relationship(
        back_populates="instance", cascade="all, delete-orphan"
    )


class ChecklistItemState(Base):
    __tablename__ = "checklist_item_state"
    __table_args__ = (UniqueConstraint("instance_id", "template_item_id", name="uq_checklist_item_state"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    instance_id: Mapped[int] = mapped_column(ForeignKey("checklist_instance.id"), nullable=False)
    template_item_id: Mapped[int] = mapped_column(ForeignKey("checklist_template_item.id"), nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    note: Mapped[str | None] = mapped_column(Text)

    instance: Mapped[ChecklistInstance] = relationship(back_populates="states")
    template_item: Mapped[ChecklistTemplateItem] = relationship()


class UserContentState(Base):
    __tablename__ = "user_content_state"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content_id: Mapped[int] = mapped_column(ForeignKey("content.id"), unique=True, nullable=False)
    state: Mapped[str] = mapped_column(String(32), default="not_started", nullable=False)
    priority: Mapped[int | None] = mapped_column(Integer)
    note: Mapped[str | None] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    content: Mapped[Content] = relationship(back_populates="user_state")
