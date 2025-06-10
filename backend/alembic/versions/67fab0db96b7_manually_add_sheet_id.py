"""Manually add sheet_id

Revision ID: 67fab0db96b7
Revises: 1c8b2fab284b
Create Date: 2025-06-06 20:18:50.034813

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67fab0db96b7'
down_revision: Union[str, None] = '1c8b2fab284b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
