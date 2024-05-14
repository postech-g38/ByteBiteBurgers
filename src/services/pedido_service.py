from datetime import datetime
from typing import List
import json

from src.adapters.repositories import PedidoRepository
from src.adapters.database.models.pedido_model import PedidoModel
from src.schemas.pedido_schema import CreatePedidoPayload, ResponsePedidoPayload
from src.services.service_base import BaseService
from src.enums import PedidoStatus


class PedidoService(BaseService):
    def __init__(self, repository: PedidoRepository) -> None:
        self.repository = repository

    def get_all(self) -> List[PedidoModel]:
        return self.query_result(self.repository.get_all())

    def get_by_id(self, pedido_id: int) -> PedidoModel:
        return self.query_result(self.repository.search_by_id(pedido_id))

    def get_by_status(self, status: str) -> PedidoModel:
        return self.query_result(self.repository.get_by_status(status.title()))

    def update(self, pedido_id: int, data: CreatePedidoPayload) -> PedidoModel:
        data_dump = data.model_dump()
        data_dump['produtos'] = json.dumps({'data': [i.model_dump() for i in data.produtos]})
        self.repository.update(pedido_id, data_dump)
        return self.repository.search_by_id(pedido_id)

    def delete(self, pedido_id: int) -> PedidoModel:
        data = self.query_result(self.repository.search_by_id(pedido_id))
        data.deleted_at = datetime.now()
        self.repository.delete(pedido_id)
        return data

    def pending_orders(self) -> List[PedidoModel]:
        rows = self.query_result(self.repository.get_pending_orders())
        return (
            sorted([i for i in rows if i.status_pedido == PedidoStatus.RECEBIDO], key=lambda x: x.created_at) +
            sorted([i for i in rows if i.status_pedido == PedidoStatus.EM_PREPARACAO], key=lambda x: x.created_at) +
            sorted([i for i in rows if i.status_pedido == PedidoStatus.PRONTO], key=lambda x: x.created_at)
        )

    def checkout(self, data: CreatePedidoPayload):
        row = PedidoModel(**dict(data))
        total = 0

        for produto in data.produtos:
            produto_info = self.query_result(self.repository.search_by_id(produto.produto_id))
            total += (produto_info.preco * produto.quantidade)

        row.valor = total
        row.status_pedido = PedidoStatus.RECEBIDO
        row.status_pagamento = 'Aguardando'
        row.data_mudanca_status = datetime.now()
        row.produtos = json.dumps({'data': [i.model_dump() for i in data.produtos]})

        self.repository.pedido.save(model=row)
        self.repository.pedido.commit()
        row = self.repository.pedido.model_refresh(model=row)
        return ResponsePedidoPayload.model_validate(row).model_dump()