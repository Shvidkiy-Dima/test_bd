from enum import Enum


class CardHistoryEventEnum(Enum):
    CREATE = 'CREATE'
    INACTIVATE = 'INACTIVATE'
    ACTIVATE = 'ACTIVATE'
    TOP_UP = 'TOP_UP'
    WITHDRAWAL = 'WITHDRAWAL'
    CHANGE_USER = 'CHANGE_USER'


class CardFormFactorEnum(Enum):
    PHYSICAL = 'PHYSICAL'
    VIRTUAL = 'VIRTUAL'


class CardStatus(Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    CLOSED = 'CLOSED'


class BinVendorEnum(Enum):
    AIRWALLEX = 'AIRWALLEX'
    SUNRATE = 'SUNRATE'
    WEX = 'WEX'


class BinScheme(Enum):
    VISA = 'VISA'
    MASTERCARD = 'MASTERCARD'