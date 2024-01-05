from typing import Any
from datetime import datetime

from pydantic import BaseModel

from src.enums import PedidoStatus


class ProdudoPedidoSchema(BaseModel):
    produto_id: int
    quantidade: int


class CreateCheckoutPayload(BaseModel):
    produtos: list[ProdudoPedidoSchema]
    valor: float
    pagamento: str
    status: str = PedidoStatus.RECEBIDO.value


class ResponseCheckoutPayload(CreateCheckoutPayload):
    id: int
    created_at: datetime
