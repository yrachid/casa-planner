"""Removing dimensoes table and adding all attributes on BaseItem

Revision ID: ffd5d6aef5ba
Revises: 34460b24a957
Create Date: 2016-08-22 16:45:06.415303

"""

# revision identifiers, used by Alembic.
revision = 'ffd5d6aef5ba'
down_revision = 'd295d274577a'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fogoes', sa.Column('altura', sa.Float(), nullable=True))
    op.add_column('fogoes', sa.Column('comprimento', sa.Float(), nullable=True))
    op.add_column('fogoes', sa.Column('largura', sa.Float(), nullable=True))
    op.add_column('geladeiras', sa.Column('altura', sa.Float(), nullable=True))
    op.add_column('geladeiras', sa.Column('comprimento', sa.Float(), nullable=True))
    op.add_column('geladeiras', sa.Column('largura', sa.Float(), nullable=True))
    op.add_column('microondas', sa.Column('altura', sa.Float(), nullable=True))
    op.add_column('microondas', sa.Column('comprimento', sa.Float(), nullable=True))
    op.add_column('microondas', sa.Column('largura', sa.Float(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('microondas', 'largura')
    op.drop_column('microondas', 'comprimento')
    op.drop_column('microondas', 'altura')
    op.drop_column('geladeiras', 'largura')
    op.drop_column('geladeiras', 'comprimento')
    op.drop_column('geladeiras', 'altura')
    op.drop_column('fogoes', 'largura')
    op.drop_column('fogoes', 'comprimento')
    op.drop_column('fogoes', 'altura')
    ### end Alembic commands ###