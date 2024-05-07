from datetime import datetime
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import MetaData

metadata = MetaData()


class BaseModel(DeclarativeBase):
    metadata = metadata


class EntityModel(BaseModel):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, index=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[Optional[datetime]] = mapped_column(onupdate=datetime.now)
    deleted_at: Mapped[Optional[datetime]]
