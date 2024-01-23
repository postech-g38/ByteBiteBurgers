from datetime import datetime

from pydantic import BaseModel, ConfigDict

from src.enums import UsuarioTipo


class CreateUsuarioPayload(BaseModel):
    nome: str
    senha: str
    cpf: str | None
    email: str
    tipo: str = UsuarioTipo.CLIENTE.value


class UpdateUsuarioPayload(BaseModel):
    id: int
    nome: str | None
    senha: str | None
    cpf: str | None
    email: str | None
    tipo: str | None


class ResponseUsuarioPayload(UpdateUsuarioPayload):
    model_config: ConfigDict = ConfigDict(from_attributes=True)
    
    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None


class ResponsePagination(BaseModel):
    items: list[ResponseUsuarioPayload] | None
    quantidade: int
