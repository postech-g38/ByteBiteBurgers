# from typing import List

# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import Mapped, mapped_column, relationship

# from src.adapters.database.models.entity_model import EntityModel
# from src.adapters.database.models.produto_model import ProdutoModel


# class CarrinhoModel(EntityModel):
#     __tablename__ = 'carrinho'

#     valor: Mapped[float]
#     produtos: Mapped[List[ProdutoModel]] = relationship()  # secondary='carrinho_produto_association'


# # Tabela de associação entre Carrinho e Produto
# # carrinho_produto_association = Table(
# #     'carrinho_produto_association', Base.metadata,
# #     Column('carrinho_id', Integer, ForeignKey('carrinho.id')),
# #     Column('produto_id', Integer, ForeignKey('produto.id'))
# # )