from datetime import datetime

from pydantic import BaseModel


class CreateCarrinhoPayload(BaseModel):
    id: int | None
    valor: float
    usuario_id: int


class UpdateCarrinhoPayload(CreateCarrinhoPayload):
    id: int


class ResponseCarrinhoPayload(CreateCarrinhoPayload):
    created_at: datetime | None
    updated_at: datetime | None
    deleted_at: datetime | None


class ResponsePagination(BaseModel):
    items: list[dict] | None
    quantidade: int
