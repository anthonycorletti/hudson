"""datasets

Revision ID: 1393566cbef5
Revises: d7fa3f2f4a1b
Create Date: 2022-12-15 07:05:49.154909+00:00

"""
from alembic import op
import sqlalchemy as sa  # noqa
import sqlmodel  # noqa


# revision identifiers, used by Alembic.
revision = "1393566cbef5"
down_revision = "d7fa3f2f4a1b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "datasets",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("description", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("namespace_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["namespace_id"],
            ["namespaces.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("namespace_id", "name"),
    )
    op.create_index(op.f("ix_datasets_id"), "datasets", ["id"], unique=False)
    op.drop_column("subscriptions", "message_retention_duration")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "subscriptions",
        sa.Column(
            "message_retention_duration",
            sa.INTEGER(),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.drop_index(op.f("ix_datasets_id"), table_name="datasets")
    op.drop_table("datasets")
    # ### end Alembic commands ###
