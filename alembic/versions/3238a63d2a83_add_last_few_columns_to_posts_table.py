"""add last few columns to posts table

Revision ID: 3238a63d2a83
Revises: 5de25a98dac2
Create Date: 2022-07-12 09:20:22.123586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3238a63d2a83'
down_revision = '5de25a98dac2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column(
        'published',sa.Boolean(), nullable=False, server_default='TRUE'),)
    
    op.add_column('posts',sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True) ,nullable=False, server_default=
        sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
