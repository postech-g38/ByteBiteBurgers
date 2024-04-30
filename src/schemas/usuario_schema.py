from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from src.enums import UsuarioTipo


class UsuarioPayload(BaseModel):
    nome: str
    senha: str
    cpf: Optional[str]
    email: str
    tipo: UsuarioTipo = UsuarioTipo.CLIENTE.value


class ResponseUsuarioPayload(UsuarioPayload):
    model_config: ConfigDict = ConfigDict(from_attributes=True)
    
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]


class ResponsePagination(BaseModel):
    items: list[ResponseUsuarioPayload] | None
    quantidade: int
