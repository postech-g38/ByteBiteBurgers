from datetime import datetime
from uuid import uuid4

from sqlalchemy.orm import Mapped, mapped_column

from src.adapters.database.models.base_model import BaseModel


def generate_uuid() -> str:
    return str(uuid4())


class EntityModel(BaseModel):
    __abstract__ = True

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False, index=True, default=generate_uuid)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime | None] = mapped_column(onupdate=datetime.utcnow)
    deleted_at: Mapped[datetime | None]
