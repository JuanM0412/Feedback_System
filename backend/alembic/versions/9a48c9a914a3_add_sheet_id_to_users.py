"""Add sheet_id to users

Revision ID: 9a48c9a914a3
Revises: 67fab0db96b7
Create Date: 2025-06-06 20:20:08.618662

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a48c9a914a3'
down_revision: Union[str, None] = '67fab0db96b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('sheet_id', sa.Text(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'sheet_id')
