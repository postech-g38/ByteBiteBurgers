from typing import Any
from datetime import datetime

from pydantic import BaseModel

from src.enums import PedidoStatus


class CreateCheckoutPayload(BaseModel):
    produtos: list[dict[str, Any]]
    valor: float
    pagamento: str
    status: str = PedidoStatus.RECEBIDO.value


class ResponseCheckoutPayload(CreateCheckoutPayload):
    id: int
    created_at: datetime
