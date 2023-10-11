from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.entity_model import EntityModel


class TipoProdutoModel(EntityModel):
    __tablename__ = 'tipos_produto'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, index=True)
    nome = Column(String)
