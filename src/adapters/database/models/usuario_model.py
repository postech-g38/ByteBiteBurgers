from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .entity_model import EntityModel

class UsuarioModel(EntityModel):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, index=True)
    nome: Mapped[str]
    senha: Mapped[str]
    cpf: Mapped[str]
    tipo_id: Mapped[int] = mapped_column(ForeignKey('tipo_usuario.id'))
    tipo = relationship('TipoUsuarioModel')