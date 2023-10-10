from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class SacolaModel(Base):
    __tablename__ = 'sacolas'
    id = Column(Integer, primary_key=True)
    valor = Column(Float)
    produtos = relationship('ProdutoModel', secondary='sacola_produto_association')

# Tabela de associação entre Sacola e Produto
sacola_produto_association = Table(
    'sacola_produto_association', Base.metadata,
    Column('sacola_id', Integer, ForeignKey('sacolas.id')),
    Column('produto_id', Integer, ForeignKey('produtos.id'))
)