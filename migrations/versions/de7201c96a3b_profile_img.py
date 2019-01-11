"""profile img

Revision ID: de7201c96a3b
Revises: da070c2d86d9
Create Date: 2018-08-11 18:35:15.477273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de7201c96a3b'
down_revision = 'da070c2d86d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_first_name', table_name='user')
    op.drop_index('ix_user_last_name', table_name='user')
    op.drop_index('ix_user_password', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    op.drop_table('user')
    op.drop_table('friends')
    op.drop_table('file_contents')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file_contents',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('data', sa.BLOB(), nullable=True),
    sa.Column('filename', sa.VARCHAR(length=30), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], [u'user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('friends',
    sa.Column('friend_id', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['friend_id'], [u'user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], [u'user.id'], )
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=32), nullable=True),
    sa.Column('password', sa.VARCHAR(length=32), nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=64), nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=64), nullable=True),
    sa.Column('about_me', sa.VARCHAR(length=140), nullable=True),
    sa.Column('location', sa.VARCHAR(length=64), nullable=True),
    sa.Column('last_seen', sa.DATETIME(), nullable=True),
    sa.Column('email', sa.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_user_username', 'user', ['username'], unique=1)
    op.create_index('ix_user_password', 'user', ['password'], unique=1)
    op.create_index('ix_user_last_name', 'user', ['last_name'], unique=1)
    op.create_index('ix_user_first_name', 'user', ['first_name'], unique=1)
    op.create_index('ix_user_email', 'user', ['email'], unique=1)
    # ### end Alembic commands ###
