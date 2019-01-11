"""empty message

Revision ID: 92c39097d93c
Revises: 65cd927613f4
Create Date: 2018-07-28 18:23:27.609996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92c39097d93c'
down_revision = '65cd927613f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_dir_name', table_name='user')
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_password_hash', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('email', sa.VARCHAR(length=64), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=60), nullable=True),
    sa.Column('dir_name', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_user_username', 'user', ['username'], unique=1)
    op.create_index('ix_user_password_hash', 'user', ['password_hash'], unique=1)
    op.create_index('ix_user_email', 'user', ['email'], unique=1)
    op.create_index('ix_user_dir_name', 'user', ['dir_name'], unique=1)
    # ### end Alembic commands ###