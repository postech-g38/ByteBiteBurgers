from typing import Dict, Any

import requests


class ByteBiteBurguers:
    def __init__(self, host: str) -> None:
        self._base_url = host + '/v1'
    
    def update_pedido(self, pedido_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        response = requests.post(
            url=self._base_url + f"/{pedido_id}/pagamento",
            json=data
        )
        return response.json()
    