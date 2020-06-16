"""users table

Revision ID: fb28cd6377a2
Revises: 
Create Date: 2020-06-14 23:52:12.608499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb28cd6377a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('can_delete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(length=60), nullable=True),
    sa.Column('upload_date', sa.DateTime(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('hash_sha', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_file_file_name'), 'file', ['file_name'], unique=True)
    op.create_index(op.f('ix_file_upload_date'), 'file', ['upload_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_file_upload_date'), table_name='file')
    op.drop_index(op.f('ix_file_file_name'), table_name='file')
    op.drop_table('file')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###