from datetime import datetime
from typing import Dict

from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.base_model import BaseModel


class CheckoutModel(BaseModel):
    __tablename__ = 'checkout'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, index=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime | None] = mapped_column(onupdate=datetime.utcnow)
    produtos = mapped_column('produtos', JSON)
    status: Mapped[str]
    pagamento: Mapped[str]
    valor: Mapped[float]
    