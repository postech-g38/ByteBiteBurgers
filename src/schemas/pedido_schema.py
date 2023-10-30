from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProdudoPedidoSchema(BaseModel):
    produto_id: int
    quantidade: int


class CreatePedidoPayload(BaseModel):
    produtos: list[ProdudoPedidoSchema]



class UpdatePedidoPayload(BaseModel):
    id:               int
    status_pedido:    str


class ResponsePedidoPayload(UpdatePedidoPayload):
    model_config: ConfigDict = ConfigDict(from_attributes=True)

    valor:                  float
    data_mudanca_status: datetime | None
    created_at:          datetime | None
    updated_at:          datetime | None
    deleted_at:          datetime | None


class ResponsePagination(BaseModel):
    items: list[ResponsePedidoPayload] | None
    quantidade: int
