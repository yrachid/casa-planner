"""Removing link attribute from lojas

Revision ID: 6c6848eba943
Revises: ffd5d6aef5ba
Create Date: 2016-08-22 16:54:17.317201

"""

# revision identifiers, used by Alembic.
revision = '6c6848eba943'
down_revision = 'ffd5d6aef5ba'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('lojas', 'link')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lojas', sa.Column('link', sa.VARCHAR(), autoincrement=False, nullable=True))
    ### end Alembic commands ###
