"""Retirando relacionamentos

Revision ID: d6cede7eb551
Revises: 909ffacfb29f
Create Date: 2024-06-17 23:22:11.519842

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd6cede7eb551'
down_revision: Union[str, None] = '909ffacfb29f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
