from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.adapters.database.models.base_model import BaseModel


class ProdutoModel(BaseModel):
    __tablename__ = 'produto'

    id:         Mapped[int] = mapped_column(primary_key=True, nullable=False, index=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime | None] = mapped_column(onupdate=datetime.utcnow)
    deleted_at: Mapped[datetime | None]
    nome:       Mapped[str]
    preco:      Mapped[float]
    imagens:    Mapped[str]
    categoria:  Mapped[str]
    