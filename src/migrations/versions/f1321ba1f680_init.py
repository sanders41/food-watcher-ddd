"""init

Revision ID: f1321ba1f680
Revises: 
Create Date: 2023-01-21 10:10:53.224990

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f1321ba1f680'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column('username', sa.Text(), nullable=False),
                    sa.Column('password', sa.Text(), nullable=False),
                    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=False),
                    sa.Column('is_superuser', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###