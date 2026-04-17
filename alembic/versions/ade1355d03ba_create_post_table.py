"""create_post_table

Revision ID: ade1355d03ba
Revises: 
Create Date: 2026-04-17 14:51:56.937094

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ade1355d03ba'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts",sa.Column("id",sa.Integer(),nullable=False,primary_key=True),
                    sa.Column("title",sa.String,nullable=False))

def downgrade() -> None:
    """Downgrade schema."""
    pass
