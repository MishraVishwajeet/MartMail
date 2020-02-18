"""empty message

Revision ID: 5b354e4f5522
Revises: d2ca877c5098
Create Date: 2020-02-18 22:21:11.959718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b354e4f5522'
down_revision = 'd2ca877c5098'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reviews', 'reviewDetails')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('reviewDetails', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    # ### end Alembic commands ###