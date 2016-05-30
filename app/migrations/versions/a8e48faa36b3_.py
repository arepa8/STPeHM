"""empty message

Revision ID: a8e48faa36b3
Revises: None
Create Date: 2016-05-30 15:37:13.789680

"""

# revision identifiers, used by Alembic.
revision = 'a8e48faa36b3'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('role_name')
    )
    op.create_table('User',
    sa.Column('ci', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=16), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('role', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['role'], ['Role.id'], ),
    sa.PrimaryKeyConstraint('ci'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('Appointment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient', sa.Integer(), nullable=False),
    sa.Column('doctor', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.ForeignKeyConstraint(['doctor'], ['User.ci'], ),
    sa.ForeignKeyConstraint(['patient'], ['User.ci'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Appointment')
    op.drop_table('User')
    op.drop_table('Role')
    ### end Alembic commands ###