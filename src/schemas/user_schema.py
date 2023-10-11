from datetime import datetime

from pydantic import BaseModel


class CreateUserPayload(BaseModel):
    nome: str
    senha: str
    cpf: str
    tipo_id: str


class UpdateUserPayload(CreateUserPayload):
    id: int
    tipo_id: int
    tipo: str


class ResponseUserPayload(UpdateUserPayload):
    class Config:
        from_orm = True

    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
