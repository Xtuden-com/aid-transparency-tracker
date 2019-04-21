"""empty message

Revision ID: 901b6a3b86de
Revises: 873290f6bdb9
Create Date: 2019-04-21 13:20:12.256304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '901b6a3b86de'
down_revision = '873290f6bdb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('organisation', sa.String(length=255), nullable=True))
    op.create_foreign_key(None, 'role', 'organisation', ['organisation'], ['slug'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'role', type_='foreignkey')
    op.drop_column('role', 'organisation')
    # ### end Alembic commands ###
