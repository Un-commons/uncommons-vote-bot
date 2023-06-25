"""User started flag

Revision ID: bd06a9545bc4
Revises: c51526c16e56
Create Date: 2019-08-06 22:32:11.137966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bd06a9545bc4"
down_revision = "c51526c16e56"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user",
        sa.Column("started", sa.Boolean(), server_default="false", nullable=False),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "started")
    # ### end Alembic commands ###