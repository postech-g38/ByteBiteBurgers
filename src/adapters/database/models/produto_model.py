from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.entity_model import EntityModel


class ProdutoModel(EntityModel):
    __tablename__ = 'produto'

    categoria_id: Mapped[int] = mapped_column(ForeignKey('categoria.id'))
    nome: Mapped[str]
    preco: Mapped[float]
    imagens: Mapped[str]
    categoria = relationship('CategoriaModel')
    