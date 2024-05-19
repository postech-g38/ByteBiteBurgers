

class MercadoPago:
    def __init__(self, host: str, token: str) -> None:
        self._base_url = host
        self._token = token
    
    @property
    def _header(self) -> dict:
        return {
            'Authorization': f"Bearer {self._token}",
            'Content-Type': 'application/json',
            'X-Idempotency-Key': '0d5020ed-1af6-469c-ae06-c3bec19954bb'
        }
