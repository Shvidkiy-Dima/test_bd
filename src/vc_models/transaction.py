from uuid import uuid4
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, UUID, ForeignKey, DateTime, String, Enum, DECIMAL, JSON
from vc_models.base import BaseModel
from vc_models.choices.transaction import TransactionStatusEnum, \
    TransactionInternalType, TransactionTypeEnum, TransactionCurrency


class Transaction(BaseModel):
    id = mapped_column(Integer, primary_key=True)
    uuid = mapped_column(UUID, unique=True, default=uuid4)
    card_id = mapped_column(Integer, ForeignKey('card.id'), nullable=False)
    internal_type = mapped_column(Enum(TransactionInternalType), nullable=False)
    transaction_date = mapped_column(DateTime, nullable=False)
    cleared_date = mapped_column(DateTime, nullable=False)
    original_transaction_id = mapped_column(String, nullable=False)
    status = mapped_column(Enum(TransactionStatusEnum), nullable=False)
    transaction_type = mapped_column(Enum(TransactionTypeEnum), nullable=False)
    transaction_amount = mapped_column(DECIMAL(12, 2), nullable=False)
    original_transaction_amount = mapped_column(DECIMAL(12, 2), nullable=False)
    original_billing_amount = mapped_column(DECIMAL(12, 2), nullable=False)
    original_billing_currency = mapped_column(Enum(TransactionCurrency), default=TransactionCurrency.USD)
    reserved_amount = mapped_column(DECIMAL(12, 2), nullable=False)
    merchant_name = mapped_column(String, nullable=False)
    mcc = mapped_column(String, nullable=False)
    failure_reason = mapped_column(String, nullable=True)
    cleared_transactions = mapped_column(JSON, nullable=True)
    previous_transactions = mapped_column(JSON, nullable=True)
    charge = mapped_column(DECIMAL(12, 2), nullable=False)
    card = relationship('Card', back_populates='transactions')

    transaction_currency = mapped_column(Enum(TransactionCurrency),
                                         default=TransactionCurrency.USD, nullable=False)

    original_transaction_currency = mapped_column(Enum(TransactionCurrency),
                                                  default=TransactionCurrency.USD, nullable=False)
