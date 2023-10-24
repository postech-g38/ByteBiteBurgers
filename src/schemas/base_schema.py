from typing import TypeVar

from pydantic import BaseModel, Field


Item = TypeVar('Item')


class DefaultResponse(BaseModel):
    data: list[Item] = Field(..., 'Objetos Retornados')


class PaginateResponse(DefaultResponse):
    count: int = Field(..., 'Quantidade Total de Objetos')
    