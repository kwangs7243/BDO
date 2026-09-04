"""Add V1.8A project tracker foundation."""

from alembic import context, op
import sqlalchemy as sa


revision = "20260905_0003"
down_revision = "20260903_0002"
branch_labels = None
depends_on = None


def _create_table_if_missing(name: str, *columns: object) -> None:
    """Create new tables while tolerating Base.metadata.create_all() upgrade paths."""

    if context.is_offline_mode() or not sa.inspect(op.get_bind()).has_table(name):
        op.create_table(name, *columns)


def upgrade() -> None:
    _create_table_if_missing(
        "project",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("slug", sa.String(length=120), nullable=False),
        sa.Column("name_ko", sa.String(length=255), nullable=False),
        sa.Column("content_id", sa.Integer(), nullable=True),
        sa.Column("summary", sa.Text(), nullable=True),
        sa.Column("active", sa.Boolean(), server_default=sa.true(), nullable=False),
        sa.ForeignKeyConstraint(["content_id"], ["content.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
    )
    _create_table_if_missing(
        "project_stage",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("seed_key", sa.String(length=200), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("order_no", sa.Integer(), nullable=False),
        sa.Column("active", sa.Boolean(), server_default=sa.true(), nullable=False),
        sa.ForeignKeyConstraint(["project_id"], ["project.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("project_id", "seed_key", name="uq_project_stage_seed_key"),
    )
    _create_table_if_missing(
        "project_stage_dependency",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("stage_id", sa.Integer(), nullable=False),
        sa.Column("depends_on_stage_id", sa.Integer(), nullable=False),
        sa.Column("seed_key", sa.String(length=200), nullable=False),
        sa.Column("active", sa.Boolean(), server_default=sa.true(), nullable=False),
        sa.CheckConstraint("stage_id <> depends_on_stage_id", name="ck_project_stage_dependency_distinct"),
        sa.ForeignKeyConstraint(["depends_on_stage_id"], ["project_stage.id"]),
        sa.ForeignKeyConstraint(["project_id"], ["project.id"]),
        sa.ForeignKeyConstraint(["stage_id"], ["project_stage.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("project_id", "seed_key", name="uq_project_stage_dependency_seed_key"),
    )
    _create_table_if_missing(
        "material",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("key", sa.String(length=160), nullable=False),
        sa.Column("name_ko", sa.String(length=255), nullable=False),
        sa.Column("unit", sa.String(length=64), nullable=False),
        sa.Column("active", sa.Boolean(), server_default=sa.true(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("key"),
    )
    _create_table_if_missing(
        "project_material",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("stage_id", sa.Integer(), nullable=True),
        sa.Column("material_id", sa.Integer(), nullable=False),
        sa.Column("seed_key", sa.String(length=200), nullable=False),
        sa.Column("required_quantity", sa.Float(), nullable=False),
        sa.Column("order_no", sa.Integer(), nullable=False),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("source_entity_type", sa.String(length=64), nullable=True),
        sa.Column("source_entity_seed_key", sa.String(length=200), nullable=True),
        sa.Column("active", sa.Boolean(), server_default=sa.true(), nullable=False),
        sa.CheckConstraint("required_quantity >= 0", name="ck_project_material_required_nonnegative"),
        sa.ForeignKeyConstraint(["material_id"], ["material.id"]),
        sa.ForeignKeyConstraint(["project_id"], ["project.id"]),
        sa.ForeignKeyConstraint(["stage_id"], ["project_stage.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("project_id", "seed_key", name="uq_project_material_seed_key"),
    )
    _create_table_if_missing(
        "project_material_source",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("project_material_id", sa.Integer(), nullable=False),
        sa.Column("content_id", sa.Integer(), nullable=False),
        sa.Column("seed_key", sa.String(length=220), nullable=False),
        sa.Column("quantity_per_completion", sa.Float(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("order_no", sa.Integer(), nullable=False),
        sa.Column("active", sa.Boolean(), server_default=sa.true(), nullable=False),
        sa.CheckConstraint(
            "quantity_per_completion IS NULL OR quantity_per_completion >= 0",
            name="ck_project_material_source_quantity_nonnegative",
        ),
        sa.ForeignKeyConstraint(["content_id"], ["content.id"]),
        sa.ForeignKeyConstraint(["project_material_id"], ["project_material.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "project_material_id", "seed_key", name="uq_project_material_source_seed_key"
        ),
    )
    _create_table_if_missing(
        "user_material_inventory",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("material_id", sa.Integer(), nullable=False),
        sa.Column("quantity", sa.Float(), server_default="0", nullable=False),
        sa.Column("note", sa.Text(), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.CheckConstraint("quantity >= 0", name="ck_user_material_inventory_nonnegative"),
        sa.ForeignKeyConstraint(["material_id"], ["material.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("material_id"),
    )
    _create_table_if_missing(
        "user_project_stage_state",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("stage_id", sa.Integer(), nullable=False),
        sa.Column("completed", sa.Boolean(), server_default=sa.false(), nullable=False),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("note", sa.Text(), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["stage_id"], ["project_stage.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("stage_id"),
    )


def downgrade() -> None:
    op.drop_table("user_project_stage_state")
    op.drop_table("user_material_inventory")
    op.drop_table("project_material_source")
    op.drop_table("project_material")
    op.drop_table("material")
    op.drop_table("project_stage_dependency")
    op.drop_table("project_stage")
    op.drop_table("project")
