from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .entity_model import EntityModel


class TipoUsuarioModel(EntityModel):
    __tablename__ = 'tipo_usuario'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, index=True)
    nome: Mapped[str]
    