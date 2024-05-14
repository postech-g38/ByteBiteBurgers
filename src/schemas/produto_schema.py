from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, ConfigDict, field_validator, ValidationError

from src.enums import ProdutoCategorias


class CreateProdutoPayload(BaseModel):
    nome: Optional[str]
    preco: Optional[float]
    imagens: Optional[str]
    categoria: Optional[ProdutoCategorias]


class ResponseProduto(CreateProdutoPayload):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


class ResponsePagination(BaseModel):
    items: List[ResponseProduto]
    quantidade: int  
