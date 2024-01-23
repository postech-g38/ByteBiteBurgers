from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.entity_model import EntityModel


class ProdutoModel(EntityModel):
    __tablename__ = 'produto'

    nome:       Mapped[str]
    preco:      Mapped[float]
    imagens:    Mapped[str]
    categoria:  Mapped[str]
    