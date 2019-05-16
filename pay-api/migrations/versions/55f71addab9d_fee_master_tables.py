"""fee_master_tables

Revision ID: 55f71addab9d
Revises: 
Create Date: 2019-05-10 11:04:59.893256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55f71addab9d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('corp_type',
    sa.Column('code', sa.String(length=10), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_table('fee_code',
    sa.Column('code', sa.String(length=10), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_table('filing_type',
    sa.Column('code', sa.String(length=10), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_table('fee_schedule',
    sa.Column('fee_schedule_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('filing_type_code', sa.String(length=10), nullable=False),
    sa.Column('corp_type_code', sa.String(length=10), nullable=False),
    sa.Column('fee_code', sa.String(length=10), nullable=False),
    sa.Column('fee_start_date', sa.Date(), nullable=False),
    sa.Column('fee_end_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['corp_type_code'], ['corp_type.code'], ),
    sa.ForeignKeyConstraint(['fee_code'], ['fee_code.code'], ),
    sa.ForeignKeyConstraint(['filing_type_code'], ['filing_type.code'], ),
    sa.PrimaryKeyConstraint('fee_schedule_id'),
    sa.UniqueConstraint('filing_type_code', 'corp_type_code', 'fee_code', name='unique_fee_sched_1')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fee_schedule')
    op.drop_table('filing_type')
    op.drop_table('fee_code')
    op.drop_table('corp_type')
    # ### end Alembic commands ###
