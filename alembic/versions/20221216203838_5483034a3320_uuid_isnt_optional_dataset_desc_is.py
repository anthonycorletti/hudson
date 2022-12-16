"""uuid isnt optional dataset desc is

Revision ID: 5483034a3320
Revises: 1393566cbef5
Create Date: 2022-12-16 20:38:38.010900+00:00

"""
from alembic import op
import sqlalchemy as sa  # noqa
import sqlmodel  # noqa


# revision identifiers, used by Alembic.
revision = "5483034a3320"
down_revision = "1393566cbef5"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "datasets", "description", existing_type=sa.VARCHAR(), nullable=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "datasets", "description", existing_type=sa.VARCHAR(), nullable=False
    )
    # ### end Alembic commands ###
