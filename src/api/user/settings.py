from typing import Dict

import requests


class UsuarioApi:

    def __init__(self, host: str) -> None:
        self._base_url = host + '/v1'
    
    def get_user(self, documento: str) -> Dict[str, str]:
        response = requests.get(url=self._base_url + f"/cpf/{documento}")
        return response.json()
    