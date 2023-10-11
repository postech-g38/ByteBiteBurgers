from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.entity_model import EntityModel


class SacolaModel(EntityModel):
    __tablename__ = 'sacolas'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, index=True)
    valor: Mapped[float]
    produtos = relationship('ProdutoModel', secondary='sacola_produto_association')


# Tabela de associação entre Sacola e Produto
sacola_produto_association = Table(
    'sacola_produto_association', Base.metadata,
    Column('sacola_id', Integer, ForeignKey('sacolas.id')),
    Column('produto_id', Integer, ForeignKey('produtos.id'))
)