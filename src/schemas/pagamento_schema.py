from datetime import datetime

from pydantic import BaseModel, ConfigDict

from src.enums import PagamentoStatus


class PagamentoPayloadSchema(BaseModel):
    pedido_id: int
    usuario_id: int
    valor: float
    metodo: str
    status: PagamentoStatus = PagamentoStatus.CRIADO.value


class PagamentoResponseSchema(PagamentoPayloadSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime | None


class PagamentoWebhookSchema(BaseModel):
    pass


class PagamentoWebhookResponse(BaseModel):
    status: str = 'ok'