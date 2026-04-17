"""create_new_conten_column

Revision ID: 7197149f41b6
Revises: ade1355d03ba
Create Date: 2026-04-17 15:15:36.162730

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7197149f41b6'
down_revision: Union[str, Sequence[str], None] = 'ade1355d03ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_column("posts","content")
    pass
