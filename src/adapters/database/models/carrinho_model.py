from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.base_model import BaseModel
from src.adapters.database.models.entity_model import EntityModel
from src.adapters.database.models.produto_model import ProdutoModel

# Tabela de associação entre Carrinho e Produto
carrinho_produto_association = Table(
    'carrinho_produto', BaseModel.metadata,
    Column('carrinho_id', Integer, ForeignKey('carrinho.id')),
    Column('produto_id', Integer, ForeignKey('produto.id'))
)


class CarrinhoModel(EntityModel):
    __tablename__ = 'carrinho'

    valor: Mapped[float]
    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuario.id'))
    produtos: Mapped[list[ProdutoModel]] = relationship('ProdutoModel',
                                secondary=carrinho_produto_association,
                                primaryjoin="CarrinhoModel.id == carrinho_produto.c.carrinho_id",
                                secondaryjoin="ProdutoModel.id == carrinho_produto.c.produto_id",
                                backref='carrinho_produto_association',
                                lazy='dynamic')


