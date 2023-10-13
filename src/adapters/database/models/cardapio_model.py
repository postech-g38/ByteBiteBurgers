from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.entity_model import EntityModel
from src.adapters.database.models.produto_model import ProdutoModel


class CardapioModel(EntityModel):
    __tablename__ = 'cardapio'
