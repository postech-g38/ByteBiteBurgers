from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.entity_model import EntityModel


class CarrinhoModel(EntityModel):
    __tablename__ = 'carrinho'

    valor: Mapped[float]
    produtos = relationship('ProdutoModel', secondary='carrinho_produto_association')


# Tabela de associação entre Carrinho e Produto
carrinho_produto_association = Table(
    'carrinho_produto_association', Base.metadata,
    Column('carrinho_id', Integer, ForeignKey('carrinho.id')),
    Column('produto_id', Integer, ForeignKey('produto.id'))
)