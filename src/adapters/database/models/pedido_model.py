from datetime import datetime
from typing import Dict

from sqlalchemy import Column, Integer, String, ForeignKey, JSON, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.base_model import EntityModel


class PedidoModel(EntityModel):
    __tablename__ = 'pedido'

    data_mudanca_status: Mapped[datetime | None]
    valor: Mapped[float]
    status_pedido: Mapped[str | None]
    status_pagamento: Mapped[str | None]
    pagamento_id: Mapped[str | None]
    # produtos = mapped_column('produtos', ARRAY(JSON))
