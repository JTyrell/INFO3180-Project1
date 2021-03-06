"""empty message

Revision ID: 9ecb1cafe286
Revises: 81bbbf6af1aa
Create Date: 2020-04-11 19:28:05.985249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ecb1cafe286'
down_revision = '81bbbf6af1aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('gender', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('biography', sa.String(length=255), nullable=True),
    sa.Column('upload', sa.String(length=150), nullable=True),
    sa.Column('profile_creation', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user_profiles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profiles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_profiles_pkey'),
    sa.UniqueConstraint('password', name='user_profiles_password_key'),
    sa.UniqueConstraint('username', name='user_profiles_username_key')
    )
    op.drop_table('user_profile')
    # ### end Alembic commands ###
