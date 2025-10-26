"""create about me for user column

Revision ID: 659318fc2977
Revises: 
Create Date: 2025-10-19 16:55:36.964524

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '659318fc2977'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('about_me', sa.String(), nullable=True))
    


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'about_me')