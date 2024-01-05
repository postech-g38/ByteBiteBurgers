from datetime import datetime

from pydantic import BaseModel, ConfigDict, field_validator, ValidationError

from src.enums import ProdutoCategorias


class CreateProdutoPayload(BaseModel):
    nome:      str
    preco:     float
    imagens:   str
    categoria: str

    @field_validator('categoria')
    def validate_categoria(cls, categoria: str) -> str:
        categorias = [i.value for i in ProdutoCategorias]
        if categoria.title() not in categorias:
            raise ValueError(f"Categoria deve ser: {'|'.join(categorias)}")
        return categoria.lower()


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
    
