from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.base_model import BaseModel


class CategoriaModel(BaseModel):
    __tablename__ = 'categoria'
    
    id: Mapped[str] = mapped_column(primary_key=True, nullable=False, index=True)
    nome: Mapped[str]
    