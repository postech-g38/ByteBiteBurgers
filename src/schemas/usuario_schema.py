from datetime import datetime

from pydantic import BaseModel


class CreateUsuarioPayload(BaseModel):
    id: int
    nome: str
    senha: str
    cpf: str | None
    tipo: int


class UpdateUsuarioPayload(CreateUsuarioPayload):
    id: int
    tipo: str


class ResponseUsuarioPayload(CreateUsuarioPayload):
    class Config:
        from_orm = True
        
    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None
