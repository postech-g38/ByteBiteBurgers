from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class TipoProdutoModel(Base):
    __tablename__ = 'tipos_produto'
    id = Column(Integer, primary_key=True)
    nome = Column(String)