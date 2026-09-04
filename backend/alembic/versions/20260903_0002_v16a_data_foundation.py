"""Add V1.6A structured knowledge and stable seed identities."""

from alembic import context, op
import sqlalchemy as sa


revision = "20260903_0002"
down_revision = "20260902_0001"
branch_labels = None
depends_on = None


def _create_table_if_missing(name: str, *columns: object) -> None:
    """Emit full offline DDL, but preserve a table already created in an online DB."""

    if context.is_offline_mode() or not sa.inspect(op.get_bind()).has_table(name):
        op.create_table(name, *columns)


def upgrade() -> None:
    with op.batch_alter_table("schedule_rule") as batch:
        batch.add_column(sa.Column("seed_key", sa.String(length=160), nullable=True))
        batch.add_column(sa.Column("fixed_datetime", sa.DateTime(timezone=True), nullable=True))
        batch.add_column(sa.Column("active", sa.Boolean(), server_default=sa.true(), nullable=False))
        batch.create_unique_constraint("uq_schedule_rule_seed_key", ["content_id", "seed_key"])

    with op.batch_alter_table("evidence") as batch:
        batch.add_column(sa.Column("seed_key", sa.String(length=255), nullable=True))
        batch.add_column(sa.Column("active", sa.Boolean(), server_default=sa.true(), nullable=False))
        batch.create_unique_constraint("uq_evidence_seed_key", ["seed_key"])

    with op.batch_alter_table("checklist_template") as batch:
        batch.add_column(sa.Column("seed_key", sa.String(length=160), nullable=True))
        batch.add_column(sa.Column("period_rule_id", sa.Integer(), nullable=True))
        batch.add_column(sa.Column("active", sa.Boolean(), server_default=sa.true(), nullable=False))
        batch.create_unique_constraint("uq_checklist_template_seed_key", ["content_id", "seed_key"])
        batch.create_foreign_key(
            "fk_checklist_template_period_rule",
            "schedule_rule",
            ["period_rule_id"],
            ["id"],
        )

    with op.batch_alter_table("checklist_template_item") as batch:
        batch.add_column(sa.Column("seed_key", sa.String(length=160), nullable=True))
        batch.add_column(sa.Column("active", sa.Boolean(), server_default=sa.true(), nullable=False))
        batch.create_unique_constraint("uq_checklist_item_seed_key", ["template_id", "seed_key"])

    _create_table_if_missing(
        "content_requirement",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("content_id", sa.Integer(), nullable=False),
        sa.Column("seed_key", sa.String(length=160), nullable=False),
        sa.Column("kind", sa.String(length=32), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=True),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("structured_value", sa.JSON(), nullable=True),
        sa.Column("requirement_level", sa.String(length=32), nullable=False),
        sa.Column("order_no", sa.Integer(), nullable=False),
        sa.Column("active", sa.Boolean(), server_default=sa.true(), nullable=False),
        sa.ForeignKeyConstraint(["content_id"], ["content.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("content_id", "seed_key", name="uq_content_requirement_seed_key"),
    )
    _create_table_if_missing(
        "content_step",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("content_id", sa.Integer(), nullable=False),
        sa.Column("seed_key", sa.String(length=160), nullable=False),
        sa.Column("phase", sa.String(length=32), nullable=False),
        sa.Column("order_no", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("checkable", sa.Boolean(), server_default=sa.false(), nullable=False),
        sa.Column("active", sa.Boolean(), server_default=sa.true(), nullable=False),
        sa.ForeignKeyConstraint(["content_id"], ["content.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("content_id", "seed_key", name="uq_content_step_seed_key"),
    )
    _create_table_if_missing(
        "reward",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("content_id", sa.Integer(), nullable=False),
        sa.Column("seed_key", sa.String(length=160), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("reward_type", sa.String(length=64), nullable=False),
        sa.Column("amount", sa.Float(), nullable=True),
        sa.Column("min_amount", sa.Float(), nullable=True),
        sa.Column("max_amount", sa.Float(), nullable=True),
        sa.Column("unit", sa.String(length=64), nullable=True),
        sa.Column("is_choice", sa.Boolean(), server_default=sa.false(), nullable=False),
        sa.Column("choice_group", sa.String(length=120), nullable=True),
        sa.Column("recommendation", sa.Text(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("order_no", sa.Integer(), nullable=False),
        sa.Column("active", sa.Boolean(), server_default=sa.true(), nullable=False),
        sa.ForeignKeyConstraint(["content_id"], ["content.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("content_id", "seed_key", name="uq_reward_seed_key"),
    )
    _create_table_if_missing(
        "content_section",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("content_id", sa.Integer(), nullable=False),
        sa.Column("seed_key", sa.String(length=160), nullable=False),
        sa.Column("section_type", sa.String(length=32), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("body_markdown", sa.Text(), nullable=False),
        sa.Column("order_no", sa.Integer(), nullable=False),
        sa.Column("active", sa.Boolean(), server_default=sa.true(), nullable=False),
        sa.ForeignKeyConstraint(["content_id"], ["content.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("content_id", "seed_key", name="uq_content_section_seed_key"),
    )
    _create_table_if_missing(
        "content_relation",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("from_content_id", sa.Integer(), nullable=False),
        sa.Column("to_content_id", sa.Integer(), nullable=False),
        sa.Column("seed_key", sa.String(length=160), nullable=False),
        sa.Column("relation_type", sa.String(length=32), nullable=False),
        sa.Column("note", sa.Text(), nullable=True),
        sa.Column("order_no", sa.Integer(), nullable=False),
        sa.Column("active", sa.Boolean(), server_default=sa.true(), nullable=False),
        sa.ForeignKeyConstraint(["from_content_id"], ["content.id"]),
        sa.ForeignKeyConstraint(["to_content_id"], ["content.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("from_content_id", "seed_key", name="uq_content_relation_seed_key"),
    )
    _create_table_if_missing(
        "user_content_state",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("content_id", sa.Integer(), nullable=False),
        sa.Column("state", sa.String(length=32), server_default="not_started", nullable=False),
        sa.Column("priority", sa.Integer(), nullable=True),
        sa.Column("note", sa.Text(), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["content_id"], ["content.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("content_id"),
    )


def downgrade() -> None:
    op.drop_table("user_content_state")
    op.drop_table("content_relation")
    op.drop_table("content_section")
    op.drop_table("reward")
    op.drop_table("content_step")
    op.drop_table("content_requirement")

    with op.batch_alter_table("checklist_template_item") as batch:
        batch.drop_constraint("uq_checklist_item_seed_key", type_="unique")
        batch.drop_column("active")
        batch.drop_column("seed_key")

    with op.batch_alter_table("checklist_template") as batch:
        batch.drop_constraint("fk_checklist_template_period_rule", type_="foreignkey")
        batch.drop_constraint("uq_checklist_template_seed_key", type_="unique")
        batch.drop_column("active")
        batch.drop_column("period_rule_id")
        batch.drop_column("seed_key")

    with op.batch_alter_table("evidence") as batch:
        batch.drop_constraint("uq_evidence_seed_key", type_="unique")
        batch.drop_column("active")
        batch.drop_column("seed_key")

    with op.batch_alter_table("schedule_rule") as batch:
        batch.drop_constraint("uq_schedule_rule_seed_key", type_="unique")
        batch.drop_column("active")
        batch.drop_column("fixed_datetime")
        batch.drop_column("seed_key")
