from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.adapters.database.models.base_model import BaseModel


class EntityModel(BaseModel):
    __abstract__ = True

    id: Mapped[str] == mapped_column(primary_key=True, nullable=False, index=True)
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime | None]
    deleted_at: Mapped[datetime | None]
