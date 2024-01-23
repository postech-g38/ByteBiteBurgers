from typing import Any
from datetime import datetime

from pydantic import BaseModel

from src.enums import PedidoStatus


class PagamentoWebhookSchema(BaseModel):
    user_id: str
    external_pos_id: str
    