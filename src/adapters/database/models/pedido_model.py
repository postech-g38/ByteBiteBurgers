from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class PedidoModel(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key=True)
    status_id = Column(Integer, ForeignKey('status_pedido.id'))
    data_mudanca_status = Column(DateTime)
    valor = Column(Float)
    status_pedido_id = Column(Integer, ForeignKey('status_pagamento.id'))
    status = relationship('StatusPedidoModel')
    status_pagamento = relationship('StatusPagamentoModel')