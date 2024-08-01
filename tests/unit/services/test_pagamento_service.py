from unittest.mock import Mock

import pytest

from src.schemas.pagamento_schema import PagamentoPayloadSchema
from src.services.pagamento_service import PagamentoService
from src.adapters.repositories.pagamento_repository import PagamentoRepository
from tests.resouces.database.pagamento_model import PAGAMENTO_CRIADO_MODEL, PAGAMENTO_CRIADO_PAYLOAD


def test_pagamento_service_create_pagamento_then_retur_pagamento_entity():
    # arrange
    payload = Mock(PagamentoPayloadSchema)
    payload.model_dump.return_value = PAGAMENTO_CRIADO_PAYLOAD
    repository = Mock(PagamentoRepository)
    repository.save.return_value = PAGAMENTO_CRIADO_MODEL
    service = PagamentoService(repository)
    # act
    result = service.create(payload)
    # assert
    payload.model_dump.assert_called_once()
    repository.save.assert_called_once()


def test_pagamento_service_get_by_pedido_id_then_return_pagamento_entity():
    # arrange
    pedido_id = 1
    repository = Mock(PagamentoRepository)
    repository.get_by_pedido_id.return_value = PAGAMENTO_CRIADO_MODEL
    service = PagamentoService(repository)
    # act
    result = service.get_by_pedido_id(pedido_id)
    # assert
    repository.get_by_pedido_id.assert_called_once_with(pedido_id)


@pytest.mark.skip
def test_pagamento_service_webhook_then_return():
    pass
