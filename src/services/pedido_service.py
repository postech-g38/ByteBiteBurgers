from datetime import datetime

from src.adapters.repositories import EntityRepository
from src.adapters.database.models.pedido_model import PedidoModel
from src.schemas.pedido_schema import CreatePedidoPayload, ResponsePedidoPayload, UpdatePedidoPayload
from src.services.service_base import BaseService


class PedidoService(BaseService):
    def __init__(self, repository: EntityRepository) -> None:
        self.repository = repository
    
    def get_all(self) -> dict | None:
        rows = self.query_result(self.repository.pedido.get_all())
        rows = [ResponsePedidoPayload.model_validate(i).model_dump() for i in rows]
        return {
            'items': rows,
            'quantidade': len(rows)
        }
     
    def get(self, id: int) -> dict | None:
        row = self.query_result(self.repository.pedido.search_by_id(model_id=id))
        return row.__dict__
    
    def get_by_status(self, status: str) -> dict | None:
        status = status.title()
        rows = self.query_result(self.repository.pedido.get_by_status(status=status))
        rows = [ResponsePedidoPayload.model_validate(i).model_dump() for i in rows]
        return {
            'items': rows,
            'quantidade': len(rows)
        }
        
    def checkout(self, data: CreatePedidoPayload) -> dict | None:
        row = PedidoModel(**dict(data))
        total = 0

        for produto in data.produtos:
            produto_info = self.query_result(self.repository.produto.search_by_id(model_id=produto.produto_id))
            total += (produto_info.preco * produto.quantidade)

        row.valor = total
        row.status_pedido = 'Recebido'
        row.status_pagamento = 'Efetuado'
        row.data_mudanca_status = datetime.now()
        row.produtos = [i.model_dump() for i in data.produtos]

        self.repository.pedido.save(model=row)
        self.repository.pedido.commit()
        row = self.repository.pedido.model_refresh(model=row)
        return ResponsePedidoPayload.model_validate(row).model_dump()

    def update(self, data: UpdatePedidoPayload) -> dict | None:
        self.repository.pedido.update(model_id=data.id, values=data.model_dump())
        self.repository.produto.update(model_id=data.id, values=data.model_dump())
        row = self.repository.produto.model_refresh(model=row)
        return ResponsePedidoPayload.model_validate(row).model_dump()

    def delete(self, id: int) -> dict | None:
        row = self.query_result(self.repository.pedido.search_by_id(model_id=id))
        self.repository.pedido.delete(model_id=id)
        return ResponsePedidoPayload.model_validate(row).model_dump()
    