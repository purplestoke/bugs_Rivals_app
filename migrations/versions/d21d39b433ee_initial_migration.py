"""Initial migration

Revision ID: d21d39b433ee
Revises: 
Create Date: 2025-02-15 18:50:38.309357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd21d39b433ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=25), nullable=True),
    sa.Column('wallet', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('wallet')
    )
    op.create_table('heroes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=25), nullable=True),
    sa.Column('rival_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['rival_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('heroes')
    op.drop_table('user')
    # ### end Alembic commands ###
