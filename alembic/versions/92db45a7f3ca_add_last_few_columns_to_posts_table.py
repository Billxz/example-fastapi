"""add last few columns to posts table

Revision ID: 92db45a7f3ca
Revises: 88be0b555f6b
Create Date: 2026-03-08 20:53:11.921394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92db45a7f3ca'
down_revision: Union[str, Sequence[str], None] = '88be0b555f6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean,
                  nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('post', 'created_at')
    pass
