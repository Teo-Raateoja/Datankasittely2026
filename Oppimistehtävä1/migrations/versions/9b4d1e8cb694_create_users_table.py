"""add user profile fields

Revision ID: 9b4d1e8cb694
Revises: ad8adb98d2c3
Create Date: 2026-11-05 13:11:45.486680

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b4d1e8cb694'
down_revision: Union[str, Sequence[str], None] = 'ad8adb98d2c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("users") as batch_op:
        batch_op.add_column(sa.Column("city", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("company_name", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("phone", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("website", sa.String(), nullable=True))

    op.execute(
        """
        UPDATE users
        SET city = COALESCE(city, ''),
            company_name = COALESCE(company_name, ''),
            phone = COALESCE(phone, ''),
            website = COALESCE(website, '')
        """
    )

    with op.batch_alter_table("users") as batch_op:
        batch_op.alter_column(
            "city", existing_type=sa.String(), nullable=False
        )
        batch_op.alter_column(
            "company_name", existing_type=sa.String(), nullable=False
        )
        batch_op.alter_column(
            "phone", existing_type=sa.String(), nullable=False
        )
        batch_op.alter_column(
            "website", existing_type=sa.String(), nullable=False
        )


def downgrade() -> None:
    with op.batch_alter_table("users") as batch_op:
        batch_op.drop_column("website")
        batch_op.drop_column("phone")
        batch_op.drop_column("company_name")
        batch_op.drop_column("city")
