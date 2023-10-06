from pydantic import BaseModel


class CreateUserPayload(BaseModel):
    nome: str
    senha: str
    documento: str
    tipo_id: str
    