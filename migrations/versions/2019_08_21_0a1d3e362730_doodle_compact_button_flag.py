"""Doodle compact button flag

Revision ID: 0a1d3e362730
Revises: 215dc3cce5c3
Create Date: 2019-08-21 01:37:55.808131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0a1d3e362730"
down_revision = "215dc3cce5c3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "poll",
        sa.Column(
            "compact_doodle_buttons",
            sa.Boolean(),
            server_default="true",
            nullable=False,
        ),
    )
    op.alter_column(
        "poll",
        "permanently_summarized",
        existing_type=sa.BOOLEAN(),
        server_default=None,
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "poll",
        "permanently_summarized",
        existing_type=sa.BOOLEAN(),
        server_default=sa.text("false"),
        existing_nullable=False,
    )
    op.drop_column("poll", "compact_doodle_buttons")
    # ### end Alembic commands ###