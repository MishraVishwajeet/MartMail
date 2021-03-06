"""empty message

Revision ID: 667065719143
Revises: 5b354e4f5522
Create Date: 2020-02-18 22:21:28.427446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '667065719143'
down_revision = '5b354e4f5522'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('reviewDetails', sa.String(length=1000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reviews', 'reviewDetails')
    # ### end Alembic commands ###
