"""removed foreign key restraint from hero table

Revision ID: fe08d18379a1
Revises: d21d39b433ee
Create Date: 2025-02-15 19:08:03.249819

"""
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'fe08d18379a1'
down_revision = 'd21d39b433ee'  # Previous migration ID
branch_labels = None
depends_on = None

def upgrade():
    # Step 1: Create a new table without the foreign key
    op.create_table(
        'new_heroes',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(25), nullable=True),
        sa.Column('rival_id', sa.String(4), nullable=True)  # Changed from Integer to String
    )

    # Step 2: Copy data from old table to new table
    op.execute('INSERT INTO new_heroes (id, name, rival_id) SELECT id, name, rival_id FROM heroes')

    # Step 3: Drop the old table
    op.drop_table('heroes')

    # Step 4: Rename new table to original table name
    op.rename_table('new_heroes', 'heroes')

def downgrade():
    # Step 1: Create the original table with the foreign key constraint
    op.create_table(
        'old_heroes',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(25), nullable=True),
        sa.Column('rival_id', sa.Integer(), sa.ForeignKey("user.id"), nullable=True)  # Restoring foreign key
    )

    # Step 2: Copy data back
    op.execute('INSERT INTO old_heroes (id, name, rival_id) SELECT id, name, rival_id FROM heroes')

    # Step 3: Drop the new table
    op.drop_table('heroes')

    # Step 4: Rename old table back to heroes
    op.rename_table('old_heroes', 'heroes')
