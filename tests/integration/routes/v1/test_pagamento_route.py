from unittest.mock import Mock
from http import HTTPStatus

import pytest

from src.schemas.pagamento_schema import PagamentoPayloadSchema
from src.services.pagamento_service import PagamentoService
from src.adapters.repositories.pagamento_repository import PagamentoRepository
from src.adapters.database.models.pagamento_model import PagamentoModel
from tests.resouces.database.pagamento_model import PAGAMENTO_CRIADO_MODEL, PAGAMENTO_CRIADO_PAYLOAD


@pytest.mark.integration_test
def test_pagamento_route_create_pagamento_then_retur_pagamento_entity(client, database):
    # arrange
    # act
    result = client.post(url='/v1/', json=PAGAMENTO_CRIADO_PAYLOAD)
    # assert
    assert result.status_code == HTTPStatus.CREATED


@pytest.mark.integration_test
def test_pagamento_route_get_by_pedido_id_then_return_pagamento_entity(client, database):
    # arrange
    pedido_id = 1
    database.add(PagamentoModel(**PAGAMENTO_CRIADO_MODEL))
    database.commit()
    # act
    result = client.get(f"/v1/pedido/{pedido_id}")
    # assert
    assert result.status_code == HTTPStatus.OK
    data = result.json()
    assert data['pedido_id'] == pedido_id


@pytest.mark.skip
@pytest.mark.integration_test
def test_pagamento_route_webhook_then_return(client, database):
    # arrange
    webhook_payload = {}
    # act
    result = client.post(url='/v1/webhook', json=webhook_payload)
    # assert
    assert result.status_code == HTTPStatus.OK
    data = result.json()
