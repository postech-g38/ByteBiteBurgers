from datetime import datetime

from pydantic import BaseModel

from src.enums import PagamentoStatus


class PagamentoPayloadSchema(BaseModel):
    pedido_id: str
    usuario_id: str
    valor: float
    metodo: str
    status: PagamentoStatus = PagamentoStatus.CRIADO.value


class PagamentoResponseSchema(PagamentoPayloadSchema):
    id: str
    created_at: datetime
    updated_at: datetime
    