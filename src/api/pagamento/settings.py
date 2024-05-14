import requests


class PagamentoApi:
    
    def __init__(self, host: str) -> None:
        self._base_url = host + '/v1'
