from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CreateProdutoPayload(BaseModel):
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
    items: list[ResponseProdutoPayload] | None
    quantidade: int
    
