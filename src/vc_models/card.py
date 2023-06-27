from uuid import uuid4
from sqlalchemy import Integer, UUID, String, Enum, DECIMAL, ForeignKey, DateTime, JSON
from sqlalchemy.orm import mapped_column, relationship
from vc_models.choices.card import CardStatus, CardHistoryEventEnum, BinVendorEnum, BinScheme
from vc_models.base import BaseModel


class Card(BaseModel):
    id = mapped_column(Integer, primary_key=True)
    uuid = mapped_column(UUID, unique=True, default=uuid4)
    client_uuid = mapped_column(UUID, nullable=False)
    user_uuid = mapped_column(UUID, nullable=False)
    card_bank_uuid = mapped_column(UUID, unique=True, nullable=False)
    bin_uuid = mapped_column(UUID, nullable=False)
    form_factor = mapped_column(String, nullable=False)
    nickname_client = mapped_column(String, nullable=True, unique=True)
    nickname_bank = mapped_column(String, nullable=False, unique=True)
    status = mapped_column(Enum(CardStatus), nullable=False, default=CardStatus.ACTIVE)
    balance = mapped_column(DECIMAL(12, 2), nullable=False)
    limit = mapped_column(DECIMAL(12, 2), nullable=False)

    history = relationship('CardHistory', back_populates='history')
    transactions = relationship('Transaction', back_populates='card')


class CardHistory(BaseModel):
    id = mapped_column(Integer, primary_key=True)
    card_id = mapped_column(Integer, ForeignKey('card.id'), nullable=False)
    event = mapped_column(Enum(CardHistoryEventEnum), nullable=False)
    amount = mapped_column(DECIMAL(12, 2), nullable=True)
    initiator = mapped_column(UUID, nullable=False)
    description = mapped_column(String, nullable=True)

    card = relationship('Card', back_populates='history')


class Bin(BaseModel):
    id = mapped_column(Integer, primary_key=True)
    bin_uuid = mapped_column(UUID, nullable=False)
    vendor = mapped_column(Enum(BinVendorEnum), nullable=False, default=BinVendorEnum.AIRWALLEX)
    scheme = mapped_column(Enum(BinScheme), nullable=False, default=BinScheme.VISA)
    code = mapped_column(String, unique=True, nullable=False)
    product_code = mapped_column(String, nullable=False)
    start_date = mapped_column(DateTime, nullable=False)
    services = mapped_column(JSON, nullable=False)
    country_id = mapped_column(Integer, ForeignKey('country.id'), nullable=False)
    country = relationship('Country', back_populates='bins')


class Country(BaseModel):
    id = mapped_column(Integer, primary_key=True)
    iso = mapped_column(String, nullable=False)
    name = mapped_column(String, nullable=False)

    bins = relationship('Bin', back_populates='country')


