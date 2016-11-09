"""add whitelist table

Revision ID: 8736ad38ca31
Revises: adb78f70605d
Create Date: 2016-11-07 10:50:38.168018

"""

# revision identifiers, used by Alembic.
revision = '8736ad38ca31'
down_revision = 'adb78f70605d'
branch_labels = None
depends_on = None

from alembic import context
from alembic import op
import sqlalchemy as sa

from nailgun.db.sqlalchemy.models.fields import JSON
from nailgun.db.sqlalchemy.models.mutable import MutableDict


def upgrade():
    table_prefix = context.config.get_main_option('table_prefix')
    op.create_table(
        table_prefix + 'changes_whitelist',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('env_id', sa.Integer(), nullable=False),
        sa.Column('rule', sa.String(255),
                  server_default='', nullable=False)
    )


def downgrade():
    table_prefix = context.config.get_main_option('table_prefix')
    op.drop_table(table_prefix + 'changes_whitelist')
