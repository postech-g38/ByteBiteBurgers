from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.entity_model import EntityModel


class PedidoModel(EntityModel):
    __tablename__ = 'pedido'

    # status_id: Mapped[int] = mapped_column(ForeignKey('status_pedido.id'))
    data_mudanca_status: Mapped[datetime]
    valor: Mapped[float]
    status_pedido: Mapped[str]
    status_pagamento: Mapped[str]
    # status_pedido_id = mapped_column(Integer, ForeignKey('status_pagamento.id'))
    # status = relationship('StatusPedidoModel')
    # status_pagamento = relationship('StatusPagamentoModel')
    