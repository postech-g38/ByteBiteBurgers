from typing import Optional

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.base_model import EntityModel


class UsuarioModel(EntityModel):
    __tablename__ = 'usuario'

    nome:  Mapped[str]
    email: Mapped[str]
    senha: Mapped[str]
    cpf:   Mapped[Optional[str]] = mapped_column(String(11))
    tipo:  Mapped[str]
    