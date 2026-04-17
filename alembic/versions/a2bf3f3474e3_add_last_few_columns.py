"""add last few columns

Revision ID: a2bf3f3474e3
Revises: f2438b037d67
Create Date: 2026-04-17 15:49:52.221527

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2bf3f3474e3'
down_revision: Union[str, Sequence[str], None] = 'f2438b037d67'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("created_at",sa.TIMESTAMP(timezone=True),
                                    nullable=False,server_default=sa.text("NOW()")))
    pass


def downgrade() -> None:
    op.drop_column("posts","created_at")
    pass
