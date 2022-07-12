"""create posts table

Revision ID: 9f1e8c7169f8
Revises: 
Create Date: 2022-07-08 10:08:20.237867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f1e8c7169f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                             sa.Column('title',sa.String(),nullable = False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
