from typing import Optional
from datetime import datetime

from pydantic import BaseModel

from src.enums import UsuarioTipo


class UsuarioPayload(BaseModel):
    nome: str
    senha: str
    cpf: Optional[str]
    email: str
    tipo: UsuarioTipo = UsuarioTipo.CLIENTE.value


class ResponseUsuarioPayload(UsuarioPayload):
    id: str
    created_at: datetime
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


class ResponsePagination(BaseModel):
    items: list[ResponseUsuarioPayload] | None
    quantidade: int