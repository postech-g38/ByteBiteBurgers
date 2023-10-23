from datetime import datetime

from pydantic import BaseModel


class CreateProdutoPayload(BaseModel):
    id: int | None
    nome: str
    preco: float
    categoria_id: int
    imagens: str | None


class UpdateProdutoPayload(CreateProdutoPayload):
    id: int | None


class ResponseProdutoPayload(CreateProdutoPayload):
    created_at: datetime | None
    updated_at: datetime | None
    deleted_at: datetime | None


class ResponsePagination(BaseModel):
    items: list[dict] | None
    quantidade: int
