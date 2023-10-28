from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CreateProdutoPayload(BaseModel):
    nome: str
    preco: float
    imagens: str
    categoria: str


class UpdateProdutoPayload(CreateProdutoPayload):
    id: int


class ResponseProdutoPayload(UpdateProdutoPayload):
    model_config: ConfigDict = ConfigDict(from_attributes=True)

    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None


class ResponsePagination(BaseModel):
    items: list[ResponseProdutoPayload] | None
    quantidade: int
    
