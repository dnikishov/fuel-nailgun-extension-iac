"""add unique constaint to whitelist rule-task-env

Revision ID: 954d4c3a76be
Revises: fc4f164a7b6c
Create Date: 2016-11-15 10:36:06.950577

"""

# revision identifiers, used by Alembic.
revision = '954d4c3a76be'
down_revision = 'fc4f164a7b6c'
branch_labels = None
depends_on = None

from alembic import context
from alembic import op
import sqlalchemy as sa


def upgrade():
    table_prefix = context.config.get_main_option('table_prefix')
    op.create_unique_constraint('_env_id_rule_task_unique',
                                table_prefix + 'changes_whitelist',
                                ['env_id', 'rule', 'fuel_task'])


def downgrade():
    pass
