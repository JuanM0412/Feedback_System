"""Manually add sheets_id

Revision ID: 1c8b2fab284b
Revises: 2ea227df8380
Create Date: 2025-06-06 20:17:08.968898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c8b2fab284b'
down_revision: Union[str, None] = '2ea227df8380'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
