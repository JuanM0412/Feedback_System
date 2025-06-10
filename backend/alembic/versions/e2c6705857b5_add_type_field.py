"""Add type field

Revision ID: e2c6705857b5
Revises: 9a48c9a914a3
Create Date: 2025-06-09 16:50:15.491617

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2c6705857b5'
down_revision: Union[str, None] = '9a48c9a914a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('type', sa.Boolean(), default=False, nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'type')
