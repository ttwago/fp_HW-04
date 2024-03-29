"""Initial migration

Revision ID: a9f9300d844a
Revises: 
Create Date: 2023-06-02 10:51:12.207366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9f9300d844a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('fam', sa.String(), nullable=True),
    sa.Column('otc', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    op.create_table('pereval',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('beautyTitle', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('other_titles', sa.String(), nullable=True),
    sa.Column('connect', sa.String(), nullable=True),
    sa.Column('add_time', sa.DateTime(), nullable=True),
    sa.Column('coord_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Enum('new', 'pending', 'accepted', 'rejected', name='status_enum'), nullable=True),
    sa.Column('user_email', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['coord_id'], ['coords.id'], ),
    sa.ForeignKeyConstraint(['user_email'], ['users.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('level',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('winter', sa.String(), nullable=True),
    sa.Column('summer', sa.String(), nullable=True),
    sa.Column('autumn', sa.String(), nullable=True),
    sa.Column('spring', sa.String(), nullable=True),
    sa.Column('pereval_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pereval_id'], ['pereval.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pereval_images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_name', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('pereval_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pereval_id'], ['pereval.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pereval_images')
    op.drop_table('level')
    op.drop_table('pereval')
    op.drop_table('users')
    op.drop_table('coords')
    # ### end Alembic commands ###
