from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.entity_model import EntityModel


class ProdutoModel(EntityModel):
    __tablename__ = 'produtos'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, index=True)
    tipo_produto_id: Mapped[int] = mapped_column(ForeignKey('tipos_produto.id'))
    nome: Mapped[str]
    valor: Mapped[float]
    tipo = relationship('TipoProdutoModel')
    