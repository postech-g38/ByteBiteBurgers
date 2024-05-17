from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, ForeignKey, JSON, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.base_model import EntityModel


class PedidoModel(EntityModel):
    __tablename__ = 'pedido'

    data_mudanca_status: Mapped[Optional[datetime]]
    valor: Mapped[float]
    status_pedido: Mapped[Optional[str]]
    status_pagamento: Mapped[Optional[str]]
    pagamento_id: Mapped[Optional[str]]
    produtos: Mapped[str]  # = mapped_column('produtos', ARRAY(JSON))
