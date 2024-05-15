from unittest.mock import Mock

import pytest

from src.schemas.pagamento_schema import PagamentoPayloadSchema
from src.services.pagamento_service import PagamentoService
from src.adapters.repositories.pagamento_repository import PagamentoRepository
from src.adapters.database.models.pagamento_model import PagamentoModel
from tests.resouces.database.pagamento_model import PAGAMENTO_CRIADO_MODEL


@pytest.mark.integration_test
def test_pagamento_service_create_pagamento_then_retur_pagamento_entity(database):
    # arrange
    payload = PagamentoPayloadSchema(
        pedido_id=1,
        usuario_id=1,
        valor=10.00,
        metodo='cartao_credito',
        status='criado'
    )
    repository = PagamentoRepository(database)
    service = PagamentoService(repository)
    # act
    result = service.create(payload)
    # assert
    assert result.status_code == 201


@pytest.mark.integration_test
def test_pagamento_service_get_by_pedido_id_then_return_pagamento_entity(database):
    # arrange
    pedido_id = 1
    repository = PagamentoRepository(database)
    service = PagamentoService(repository)
    database.add(PagamentoModel(**PAGAMENTO_CRIADO_MODEL))
    database.commit()
    # act
    result = service.get_by_pedido_id(pedido_id)
    # assert
    assert result.status_code == 200


@pytest.mark.skip
@pytest.mark.integration_test
def test_pagamento_service_webhook_then_return(database):
    pass
