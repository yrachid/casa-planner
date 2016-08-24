"""Changing linha onibus field type on imovel

Revision ID: 45c42c821ae0
Revises: bf62ce946645
Create Date: 2016-08-24 01:37:57.091803

"""

# revision identifiers, used by Alembic.
revision = '45c42c821ae0'
down_revision = 'bf62ce946645'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.execute(
        'ALTER TABLE imoveis ALTER COLUMN linha_onibus TYPE VARCHAR'
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.execute(
        'ALTER TABLE imoveis ALTER COLUMN linha_onibus TYPE BOOLEAN USING linha_onibus::boolean'
    )
    ### end Alembic commands ###
