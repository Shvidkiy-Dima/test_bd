from enum import Enum


class TransactionTypeEnum(Enum):
    AUTHORIZATION = 'AUTHORIZATION'
    CLEARING = 'CLEARING'
    REVERSAL = 'REVERSAL'
    REFUND = 'REFUND'
    ORIGINAL_CREDIT = 'ORIGINAL_CREDIT'



class TransactionStatusEnum(Enum):
    PENDING = 'PENDING'
    APPROVED = 'APPROVED'
    FAILED = 'FAILED'
    CLEARED = 'CLEARED'
    REVERSED = 'REVERSED'



class TransactionInternalType(Enum):
    PENDING = 'PENDING'
    DECLINE = 'DECLINE'
    SUCCESS = 'SUCCESS'
    REVERSAL = 'REVERSAL'
    PARTIAL_REVERSAL = 'PARTIAL_REVERSAL'
    REFUND = 'REFUND'
    INCOMING = 'INCOMING'


class TransactionCurrency(Enum):
    USD = 'USD'
    RUB = 'RUB'
