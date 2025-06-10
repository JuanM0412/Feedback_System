"""Add state to user

Revision ID: c4b90fd42de5
Revises: e2c6705857b5
Create Date: 2025-06-10 16:28:25.499350

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4b90fd42de5'
down_revision: Union[str, None] = 'e2c6705857b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('state', sa.Boolean(), default=True, nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'state')