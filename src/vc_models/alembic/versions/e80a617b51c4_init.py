"""init

Revision ID: e80a617b51c4
Revises: 
Create Date: 2023-06-27 21:45:08.951431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e80a617b51c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.UUID(), nullable=True),
    sa.Column('client_uuid', sa.UUID(), nullable=False),
    sa.Column('user_uuid', sa.UUID(), nullable=False),
    sa.Column('card_bank_uuid', sa.UUID(), nullable=False),
    sa.Column('bin_uuid', sa.UUID(), nullable=False),
    sa.Column('form_factor', sa.String(), nullable=False),
    sa.Column('nickname_client', sa.String(), nullable=True),
    sa.Column('nickname_bank', sa.String(), nullable=False),
    sa.Column('status', sa.Enum('ACTIVE', 'INACTIVE', 'CLOSED', name='cardstatus'), nullable=False),
    sa.Column('balance', sa.DECIMAL(precision=12, scale=2), nullable=False),
    sa.Column('limit', sa.DECIMAL(precision=12, scale=2), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('card_bank_uuid'),
    sa.UniqueConstraint('nickname_bank'),
    sa.UniqueConstraint('nickname_client'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('country',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('iso', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bin_uuid', sa.UUID(), nullable=False),
    sa.Column('vendor', sa.Enum('AIRWALLEX', 'SUNRATE', 'WEX', name='binvendorenum'), nullable=False),
    sa.Column('scheme', sa.Enum('VISA', 'MASTERCARD', name='binscheme'), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('product_code', sa.String(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('services', sa.JSON(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('cardhistory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('card_id', sa.Integer(), nullable=False),
    sa.Column('event', sa.Enum('CREATE', 'INACTIVATE', 'ACTIVATE', 'TOP_UP', 'WITHDRAWAL', 'CHANGE_USER', name='cardhistoryeventenum'), nullable=False),
    sa.Column('amount', sa.DECIMAL(precision=12, scale=2), nullable=True),
    sa.Column('initiator', sa.UUID(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['card_id'], ['card.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.UUID(), nullable=True),
    sa.Column('card_id', sa.Integer(), nullable=False),
    sa.Column('internal_type', sa.Enum('PENDING', 'DECLINE', 'SUCCESS', 'REVERSAL', 'PARTIAL_REVERSAL', 'REFUND', 'INCOMING', name='transactioninternaltype'), nullable=False),
    sa.Column('transaction_date', sa.DateTime(), nullable=False),
    sa.Column('cleared_date', sa.DateTime(), nullable=False),
    sa.Column('original_transaction_id', sa.String(), nullable=False),
    sa.Column('status', sa.Enum('PENDING', 'APPROVED', 'FAILED', 'CLEARED', 'REVERSED', name='transactionstatusenum'), nullable=False),
    sa.Column('transaction_type', sa.Enum('AUTHORIZATION', 'CLEARING', 'REVERSAL', 'REFUND', 'ORIGINAL_CREDIT', name='transactiontypeenum'), nullable=False),
    sa.Column('transaction_amount', sa.DECIMAL(precision=12, scale=2), nullable=False),
    sa.Column('original_transaction_amount', sa.DECIMAL(precision=12, scale=2), nullable=False),
    sa.Column('original_billing_amount', sa.DECIMAL(precision=12, scale=2), nullable=False),
    sa.Column('original_billing_currency', sa.Enum('USD', 'RUB', name='transactioncurrency'), nullable=True),
    sa.Column('reserved_amount', sa.DECIMAL(precision=12, scale=2), nullable=False),
    sa.Column('merchant_name', sa.String(), nullable=False),
    sa.Column('mcc', sa.String(), nullable=False),
    sa.Column('failure_reason', sa.String(), nullable=True),
    sa.Column('cleared_transactions', sa.JSON(), nullable=True),
    sa.Column('previous_transactions', sa.JSON(), nullable=True),
    sa.Column('charge', sa.DECIMAL(precision=12, scale=2), nullable=False),
    sa.Column('transaction_currency', sa.Enum('USD', 'RUB', name='transactioncurrency'), nullable=False),
    sa.Column('original_transaction_currency', sa.Enum('USD', 'RUB', name='transactioncurrency'), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['card_id'], ['card.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaction')
    op.drop_table('cardhistory')
    op.drop_table('bin')
    op.drop_table('country')
    op.drop_table('card')
    # ### end Alembic commands ###
