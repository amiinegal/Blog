"""new additions

Revision ID: d22d78e29a2c
Revises: e61f640e6330
Create Date: 2019-04-30 15:43:40.885341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd22d78e29a2c'
down_revision = 'e61f640e6330'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    op.drop_constraint('user_email_key', 'user', type_='unique')
    op.drop_constraint('user_username_key', 'user', type_='unique')
    op.drop_column('user', 'password')
    op.drop_column('user', 'image_file')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('image_file', sa.VARCHAR(length=20), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('password', sa.VARCHAR(length=60), autoincrement=False, nullable=False))
    op.create_unique_constraint('user_username_key', 'user', ['username'])
    op.create_unique_constraint('user_email_key', 'user', ['email'])
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###