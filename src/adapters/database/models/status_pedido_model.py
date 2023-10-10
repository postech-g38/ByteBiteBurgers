from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class StatusPedidoModel(Base):
    __tablename__ = 'status_pedido'
    id = Column(Integer, primary_key=True)
    nome = Column(String)