"""add content column to posts table

Revision ID: ce90443dfca4
Revises: 9f1e8c7169f8
Create Date: 2022-07-08 10:27:02.207538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce90443dfca4'
down_revision = '9f1e8c7169f8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
