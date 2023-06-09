"""empty message

Revision ID: 858adab40e69
Revises: 0a069b2716d2
Create Date: 2023-05-03 19:50:01.857941

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlmodel # added


# revision identifiers, used by Alembic.
revision = '858adab40e69'
down_revision = '0a069b2716d2'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('phone', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('User', 'phone')
    # ### end Alembic commands ###
