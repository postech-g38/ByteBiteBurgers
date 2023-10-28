from datetime import datetime

from src.adapters.repositories import EntityRepository
from src.adapters.database.models.pedido_model import PedidoModel
from src.schemas.pedido_schema import CreatePedidoPayload, ResponsePedidoPayload, UpdatePedidoPayload
from src.services.service_base import BaseService
from src.schemas.checkout_schema import CreateCheckoutPayload
from src.adapters.database.models.checkout_model import CheckoutModel


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
        row = self.repository.pedido.search_by_id(model_id=id)
        if not row:
            return None
        return row.__dict__
    
    def checkout(self, data: CreatePedidoPayload) -> dict | None:
        row = PedidoModel(**dict(data))
        total = 0
        for produto in data.produtos:
            row = self.query_result(self.repository.produto.search_by_id(model_id=produto.produto_id))
            total += (row.preco * produto.quantidade)

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
        self.repository.pedido.update(model=data, values=dict(data))
        row = self.repository.pedido.search_by_id(model_id=data.id)
        return row

    def delete(self, id: int) -> int:
        row = self.repository.pedido.delete(model_id=id)
        return id
    

    # def chekout(self, payload: CreateCheckoutPayload) -> dict:
    #     model = CheckoutModel(**payload.model_dump())
    #     self.repository.checkout.save(model)
    #     self.repository.checkout.model_refresh(model)

    #     return model