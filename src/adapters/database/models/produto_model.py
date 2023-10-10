from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class ProdutoModel(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    tipo_produto_id = Column(Integer, ForeignKey('tipos_produto.id'))
    nome = Column(String)
    valor = Column(Float)
    tipo = relationship('TipoProdutoModel')