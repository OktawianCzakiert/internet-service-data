"""Rename download_over_limit column

Revision ID: 0918a70859fd
Revises: 598487da0100
Create Date: 2024-07-08 19:54:08.079550

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0918a70859fd'
down_revision: Union[str, None] = '598487da0100'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('prediction', sa.Column('download_over_limit_pred', sa.Integer(), nullable=True))
    op.drop_column('prediction', 'download_over_limit')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('prediction', sa.Column('download_over_limit', sa.INTEGER(), nullable=True))
    op.drop_column('prediction', 'download_over_limit_pred')
    # ### end Alembic commands ###
