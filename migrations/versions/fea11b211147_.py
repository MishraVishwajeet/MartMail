"""empty message

Revision ID: fea11b211147
Revises: a9ad3e26af3f
Create Date: 2020-02-19 15:55:21.063202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fea11b211147'
down_revision = 'a9ad3e26af3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'user_product_list', 'order', ['orderId'], ['id'])
    op.create_foreign_key(None, 'user_product_list', 'customers', ['userId'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_product_list', type_='foreignkey')
    op.drop_constraint(None, 'user_product_list', type_='foreignkey')
    # ### end Alembic commands ###