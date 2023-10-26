from datetime import datetime
from typing import Any

from pydantic import BaseModel

from src.enums import PedidoStatus


class CreatePedidoPayload(BaseModel):
    data_mudanca_status: datetime | None
    valor: float
    status_pedido: str = PedidoStatus.RECEBIDO.value
    status_pagamento: str
    items: dict[list[dict[str, Any]]]


class UpdatePedidoPayload(CreatePedidoPayload):
    id: str


class ResponsePedidoPayload(UpdatePedidoPayload):
    created_at: datetime | None
    updated_at: datetime | None
    deleted_at: datetime | None


class ResponsePagination(BaseModel):
    items: list[ResponsePedidoPayload] | None
    quantidade: int
