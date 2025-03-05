"""Renaming name to full_name in students table

Revision ID: 3874fa00f058
Revises: 791279dd0760
Create Date: 2025-03-05 10:02:38.257440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3874fa00f058'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='full_name')


def downgrade() -> None:
    op.alter_column('students', 'full_name', new_column_name='name')
