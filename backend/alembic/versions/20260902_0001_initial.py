"""Create the frozen V1.5 vertical-slice tables."""

from alembic import op
import sqlalchemy as sa


revision = "20260902_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "source",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("url", sa.Text(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("publisher", sa.String(length=120), nullable=True),
        sa.Column("source_type", sa.String(length=32), nullable=False),
        sa.Column("published_at", sa.Date(), nullable=True),
        sa.Column("retrieved_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("region", sa.String(length=16), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "content",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("slug", sa.String(length=120), nullable=False),
        sa.Column("name_ko", sa.String(length=255), nullable=False),
        sa.Column("category", sa.String(length=64), nullable=False),
        sa.Column("subcategory", sa.String(length=64), nullable=True),
        sa.Column("summary", sa.Text(), nullable=True),
        sa.Column("purpose", sa.Text(), nullable=True),
        sa.Column("party_type", sa.String(length=32), nullable=True),
        sa.Column("difficulty", sa.String(length=32), nullable=True),
        sa.Column("status", sa.String(length=32), nullable=False),
        sa.Column("last_verified_at", sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
    )
    op.create_table(
        "schedule_rule",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("content_id", sa.Integer(), nullable=False),
        sa.Column("rule_type", sa.String(length=32), nullable=False),
        sa.Column("timezone", sa.String(length=64), nullable=False),
        sa.Column("recurrence_type", sa.String(length=32), nullable=False),
        sa.Column("weekday", sa.Integer(), nullable=True),
        sa.Column("time_local", sa.Time(), nullable=True),
        sa.Column("effective_from", sa.Date(), nullable=True),
        sa.Column("effective_to", sa.Date(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["content_id"], ["content.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "evidence",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("entity_type", sa.String(length=32), nullable=False),
        sa.Column("entity_id", sa.String(length=128), nullable=False),
        sa.Column("claim_key", sa.String(length=128), nullable=False),
        sa.Column("source_id", sa.String(length=64), nullable=False),
        sa.Column("evidence_note", sa.Text(), nullable=True),
        sa.Column("verification_status", sa.String(length=32), nullable=False),
        sa.Column("last_verified_at", sa.Date(), nullable=False),
        sa.Column("superseded_by", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["source_id"], ["source.id"]),
        sa.ForeignKeyConstraint(["superseded_by"], ["evidence.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "checklist_template",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("content_id", sa.Integer(), nullable=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("recurrence_scope", sa.String(length=32), nullable=False),
        sa.Column("enabled_default", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(["content_id"], ["content.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "checklist_template_item",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("template_id", sa.Integer(), nullable=False),
        sa.Column("order_no", sa.Integer(), nullable=False),
        sa.Column("label", sa.String(length=255), nullable=False),
        sa.Column("details", sa.Text(), nullable=True),
        sa.Column("reward_hint", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["template_id"], ["checklist_template.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "checklist_instance",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("template_id", sa.Integer(), nullable=False),
        sa.Column("period_key", sa.String(length=100), nullable=False),
        sa.Column("period_start", sa.DateTime(timezone=True), nullable=False),
        sa.Column("period_end", sa.DateTime(timezone=True), nullable=False),
        sa.Column("generated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["template_id"], ["checklist_template.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("template_id", "period_key", name="uq_checklist_period"),
    )
    op.create_table(
        "checklist_item_state",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("instance_id", sa.Integer(), nullable=False),
        sa.Column("template_item_id", sa.Integer(), nullable=False),
        sa.Column("completed", sa.Boolean(), nullable=False),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("note", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["instance_id"], ["checklist_instance.id"]),
        sa.ForeignKeyConstraint(["template_item_id"], ["checklist_template_item.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("instance_id", "template_item_id", name="uq_checklist_item_state"),
    )


def downgrade() -> None:
    op.drop_table("checklist_item_state")
    op.drop_table("checklist_instance")
    op.drop_table("checklist_template_item")
    op.drop_table("checklist_template")
    op.drop_table("evidence")
    op.drop_table("schedule_rule")
    op.drop_table("content")
    op.drop_table("source")
