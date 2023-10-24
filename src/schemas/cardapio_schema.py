from datetime import datetime

from pydantic import BaseModel


class CreateCardapioPayload(BaseModel):
    id: int | None


class UpdateCardapioPayload(CreateCardapioPayload):
    id: int


class ResponseCardapioPayload(CreateCardapioPayload):
    created_at: datetime | None
    updated_at: datetime | None
    deleted_at: datetime | None


class ResponsePagination(BaseModel):
    items: list[dict] | None
    quantidade: int
