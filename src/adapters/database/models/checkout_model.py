from datetime import datetime
from typing import Dict

from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.base_model import EntityModel


class CheckoutModel(EntityModel):
    __tablename__ = 'checkout'

    produtos = mapped_column('produtos', JSON)
    status: Mapped[str]
    pagamento: Mapped[str]
    valor: Mapped[float]
    