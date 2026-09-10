"""Add V1.9Q cooking canonical definitions without rebuilding Material."""
from alembic import context, op
import sqlalchemy as sa

revision = "20260910_0004"
down_revision = "20260905_0003"
branch_labels = None
depends_on = None


def _create_table_if_missing(name, *columns):
    """Accept existing create_all tables; freeze this revision's historical DDL."""
    if context.is_offline_mode() or not sa.inspect(op.get_bind()).has_table(name):
        op.create_table(name, *columns)


def _id():
    return sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True)


def _active():
    return sa.Column("active", sa.Boolean(), server_default=sa.true(), nullable=False)


def upgrade():
    _create_table_if_missing(
        "ingredient_group", _id(),
        sa.Column("key", sa.String(160), unique=True, nullable=False),
        sa.Column("name_ko", sa.String(255), nullable=False),
        sa.Column("last_verified_at", sa.Date()), _active(),
    )
    _create_table_if_missing(
        "ingredient_group_member", _id(),
        sa.Column("group_id", sa.Integer(), sa.ForeignKey("ingredient_group.id"), nullable=False),
        sa.Column("material_id", sa.Integer(), sa.ForeignKey("material.id"), nullable=False),
        sa.Column("seed_key", sa.String(200), nullable=False),
        sa.Column("order_no", sa.Integer(), nullable=False), _active(),
        sa.UniqueConstraint("group_id", "material_id", name="uq_ingredient_group_material"),
        sa.UniqueConstraint("group_id", "seed_key", name="uq_ingredient_group_member_seed"),
    )
    _create_table_if_missing(
        "recipe", _id(),
        sa.Column("slug", sa.String(120), unique=True, nullable=False),
        sa.Column("name_ko", sa.String(255), nullable=False),
        sa.Column("process_type", sa.String(32), nullable=False),
        sa.Column("result_material_id", sa.Integer(), sa.ForeignKey("material.id"), nullable=False),
        sa.Column("summary", sa.Text()),
        sa.Column("required_skill_tier", sa.String(32)),
        sa.Column("required_skill_level", sa.Integer()),
        sa.Column("last_verified_at", sa.Date()), _active(),
        sa.CheckConstraint("required_skill_level IS NULL OR required_skill_level > 0",
                           name="ck_recipe_skill_positive"),
    )
    _create_table_if_missing(
        "recipe_ingredient_slot", _id(),
        sa.Column("recipe_id", sa.Integer(), sa.ForeignKey("recipe.id"), nullable=False),
        sa.Column("seed_key", sa.String(200), nullable=False),
        sa.Column("label", sa.String(255), nullable=False),
        sa.Column("order_no", sa.Integer(), nullable=False),
        sa.Column("notes", sa.Text()), _active(),
        sa.UniqueConstraint("recipe_id", "seed_key", name="uq_recipe_slot_seed"),
    )
    _create_table_if_missing(
        "recipe_ingredient_option", _id(),
        sa.Column("slot_id", sa.Integer(), sa.ForeignKey("recipe_ingredient_slot.id"), nullable=False),
        sa.Column("seed_key", sa.String(220), nullable=False),
        sa.Column("material_id", sa.Integer(), sa.ForeignKey("material.id")),
        sa.Column("ingredient_group_id", sa.Integer(), sa.ForeignKey("ingredient_group.id")),
        sa.Column("required_quantity", sa.Float(), nullable=False),
        sa.Column("order_no", sa.Integer(), nullable=False),
        sa.Column("notes", sa.Text()), _active(),
        sa.UniqueConstraint("slot_id", "seed_key", name="uq_recipe_option_seed"),
        sa.CheckConstraint("required_quantity > 0", name="ck_recipe_option_quantity_positive"),
        sa.CheckConstraint(
            "(material_id IS NOT NULL AND ingredient_group_id IS NULL) OR "
            "(material_id IS NULL AND ingredient_group_id IS NOT NULL)",
            name="ck_recipe_option_target_xor",
        ),
    )


def downgrade():
    op.drop_table("recipe_ingredient_option")
    op.drop_table("recipe_ingredient_slot")
    op.drop_table("recipe")
    op.drop_table("ingredient_group_member")
    op.drop_table("ingredient_group")
