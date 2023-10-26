from datetime import datetime

from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CreateProdutoPayload(BaseModel):
    nome: str
    categoria_id: str
    preco: float
    imagens: str
    categoria: str


class UpdateProdutoPayload(CreateProdutoPayload):
    id: UUID


class ResponseProdutoPayload(UpdateProdutoPayload):
    model_config: ConfigDict = ConfigDict(from_attributes=True)

    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None


class ResponsePagination(BaseModel):
    items: list[ResponseProdutoPayload] | None
    quantidade: int
    
