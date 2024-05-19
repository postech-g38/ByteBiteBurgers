from typing import Optional


from pydantic import BaseModel

from src.enums import UsuarioTipo


class UsuarioPayload(BaseModel):
    nome: str
    senha: str
    cpf: Optional[str]
    email: str
    tipo: UsuarioTipo = UsuarioTipo.CLIENTE.value


class ResponseUsuarioPayload(UsuarioPayload):
    pass


class ResponsePagination(BaseModel):
    items: list[ResponseUsuarioPayload] | None
    quantidade: int