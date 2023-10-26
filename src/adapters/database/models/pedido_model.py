from datetime import datetime
from typing import Dict

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.entity_model import EntityModel


class PedidoModel(EntityModel):
    __tablename__ = 'pedido'

    data_mudanca_status: Mapped[datetime]
    valor: Mapped[float]
    status_pedido: Mapped[str]
    status_pagamento: Mapped[str]
    items: Mapped[Dict]
    