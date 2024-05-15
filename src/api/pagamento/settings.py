from typing import Dict

import requests


class PagamentoApi:
    
    def __init__(self, host: str) -> None:
        self._base_url = host + '/v1'
    
    def create(self, metodo: str, valor: float, pedido_id: int, usuario_id: int) -> Dict[str, str]:
        payload = {
            'pedido_id': pedido_id,
            'usuario_id': usuario_id,
            'valor': valor,
            'metodo': metodo
        }
        response = requests.post(url=self._base_url + '/', json=payload)
        return response.json()
