from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.adapters.database.models.base_model import BaseModel


class EntityModel(BaseModel):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, index=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime | None] = mapped_column(onupdate=datetime.utcnow)
    deleted_at: Mapped[datetime | None]
