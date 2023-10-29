from datetime import datetime
from typing import Dict

from sqlalchemy import Column, Integer, String, ForeignKey, JSON, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.entity_model import EntityModel


class PedidoModel(EntityModel):
    __tablename__ = 'pedido'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, index=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime | None] = mapped_column(onupdate=datetime.utcnow)
    deleted_at: Mapped[datetime | None]
    data_mudanca_status: Mapped[datetime | None]
    valor: Mapped[float]
    status_pedido: Mapped[str | None]
    status_pagamento: Mapped[str | None]
    produtos = mapped_column('produtos', ARRAY(JSON))
