"""Add vote reference and refactor references

Revision ID: 58d240646830
Revises: 2a8262678770
Create Date: 2019-11-15 14:55:46.905786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "58d240646830"
down_revision = "2a8262678770"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("reference", "admin_chat_id", new_column_name="admin_user_id")
    op.add_column(
        "reference", sa.Column("vote_message_id", sa.BigInteger(), nullable=True)
    )
    op.add_column(
        "reference", sa.Column("vote_user_id", sa.BigInteger(), nullable=True)
    )
    op.create_index(
        op.f("ix_reference_admin_user_id"), "reference", ["admin_user_id"], unique=False
    )
    op.create_index(
        op.f("ix_reference_vote_user_id"), "reference", ["vote_user_id"], unique=False
    )
    op.create_foreign_key(
        "admin_user", "reference", "user", ["admin_user_id"], ["id"], ondelete="cascade"
    )
    op.create_foreign_key(
        "vote_user", "reference", "user", ["vote_user_id"], ["id"], ondelete="cascade"
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("reference", "admin_user_id", new_column_name="admin_chat_id")
    op.add_column(
        "reference",
        sa.Column("admin_chat_id", sa.BIGINT(), autoincrement=False, nullable=True),
    )
    op.drop_constraint("vote_user", "reference", type_="foreignkey")
    op.drop_constraint("admin_user", "reference", type_="foreignkey")
    op.drop_index(op.f("ix_reference_vote_user_id"), table_name="reference")
    op.drop_index(op.f("ix_reference_admin_user_id"), table_name="reference")
    op.drop_column("reference", "vote_user_id")
    op.drop_column("reference", "vote_message_id")
    # ### end Alembic commands ###
