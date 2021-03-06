"""Added html bposts

Revision ID: 3959644eeb14
Revises: 3035f55cbebc
Create Date: 2019-05-06 20:17:28.830855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3959644eeb14'
down_revision = '3035f55cbebc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
