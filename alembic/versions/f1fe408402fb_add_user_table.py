"""Add user table

Revision ID: f1fe408402fb
Revises: ce90443dfca4
Create Date: 2022-07-08 10:33:47.628615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1fe408402fb'
down_revision = 'ce90443dfca4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                     sa.Column('id',sa.Integer(),nullable=False),
                     sa.Column('email',sa.String(),nullable = False),
                     sa.Column('password',sa.String(),nullable=False),
                     sa.Column('created_at',sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'),nullable=False),
                     sa.PrimaryKeyConstraint('id'),
                     sa.UniqueConstraint('email')
                     )


def downgrade() -> None:
    op.drop_table('users')
    pass
