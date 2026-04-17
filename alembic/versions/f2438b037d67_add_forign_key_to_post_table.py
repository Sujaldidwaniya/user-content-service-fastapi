"""add_forign_key to post_table

Revision ID: f2438b037d67
Revises: 38738b5afebf
Create Date: 2026-04-17 15:35:58.083659

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2438b037d67'
down_revision: Union[str, Sequence[str], None] = '38738b5afebf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("owner_id",sa.Integer(),nullable=False))
    op.create_foreign_key("post_users_fk",source_table="posts",referent_table="users",
                          local_cols=["owner_id"],remote_cols=["id"],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk",table_name="posts")
    op.drop_column("posts","owner_id")
    pass
