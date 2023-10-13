from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.entity_model import EntityModel


class CategoriaModel(EntityModel):
    __tablename__ = 'categoria'

    nome: Mapped[str]
    