from datetime import datetime

from pydantic import BaseModel


class CreatePedidoPayload(BaseModel):
    id: int | None
    data_mudanca_status: datetime | None
    valor: float
    status_pedido: str
    status_pagamento: str


class UpdatePedidoPayload(CreatePedidoPayload):
    id: int


class ResponsePedidoPayload(CreatePedidoPayload):
    created_at: datetime | None
    updated_at: datetime | None
    deleted_at: datetime | None


class ResponsePagination(BaseModel):
    items: list[dict] | None
    quantidade: int
