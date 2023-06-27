from typing import Any
from datetime import datetime

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import DateTime


class Base(DeclarativeBase):
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class BaseModel(Base):
    __abstract__ = True
    _query_property = None

    created = mapped_column(DateTime, default=datetime.utcnow)
    updated = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
