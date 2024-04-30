# from src.adapters.repositories import 


class PagamentoService:
    def __init__(self, repository) -> None:
        self.repository = repository
    
    def get_pedido_status(self, pedido_id: int) -> dict:
        row = self.repository.pedido.search_by_id(model_id=pedido_id)
        return {'status_pagamento': row.status_pagamento}

    def payment_response(self, payload) -> dict:
        return {'status': 'ok'}
    