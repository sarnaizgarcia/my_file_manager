"""path field added to File model

Revision ID: 56ec3daddca6
Revises: 7e244aa3067e
Create Date: 2020-06-17 19:26:25.203325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56ec3daddca6'
down_revision = '7e244aa3067e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('file', 'path')
    # ### end Alembic commands ###
