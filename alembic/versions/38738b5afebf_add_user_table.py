"""'add_user_table'

Revision ID: 38738b5afebf
Revises: 7197149f41b6
Create Date: 2026-04-17 15:21:43.407877

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '38738b5afebf'
down_revision: Union[str, Sequence[str], None] = '7197149f41b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id",sa.Integer(),nullable=False),
                    sa.Column("email",sa.String,nullable=False),
                    sa.Column("password",sa.String(),nullable=False),
                    sa.Column("created_at",sa.TIMESTAMP(timezone=True),
                              server_default=sa.text("now()"),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint("email"))
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
