from unittest.mock import Mock

import pytest

from src.services.pedido_service import PedidoService
from src.adapters.repositories.pedido_repository import PedidoRepository
from src.adapters.database.models.pedido_model import PedidoModel
from src.services.service_base import NotFoundExcepition
from tests.resouces.database.pedido_model import PEDIDO_MODEL_LANCHE_MOCK, PEDIDO_MODEL_COMBO_MAKING_MOCK, PEDIDO_MODEL_REFRIGERANTE_MOCK
from src.schemas.pedido_schema import CreatePedidoPayload


@pytest.mark.integration_test
def test_pedido_service_get_all_then_return_pedido_list(database):
    # arrange
    repository = PedidoRepository(database)
    service = PedidoService(repository)
    database.add(PedidoModel(**PEDIDO_MODEL_LANCHE_MOCK))
    database.commit()
    # act
    result = service.get_all()
    # assert



@pytest.mark.integration_test
def test_pedido_service_get_by_id_then_return_pedido_entity(database):
    # arrange
    pedido_id = 1
    repository = PedidoRepository(database)
    service = PedidoService(repository)
    database.add(PedidoModel(**PEDIDO_MODEL_LANCHE_MOCK))
    database.commit()
    # act
    result = service.get_by_id(pedido_id)
    # assert



@pytest.mark.integration_test
def test_pedido_service_get_by_id_then_raise_not_found_exception(database):
    # arrange
    pedido_id = 1
    repository = PedidoRepository(database)
    service = PedidoService(repository)
    # act
    with pytest.raises(NotFoundExcepition):
        result = service.get_by_id(pedido_id)
    # assert


@pytest.mark.integration_test 
def test_pedido_service_update_then_return_pedido_entity(database):
    # arrange
    pedido_id = 1
    pedido_payload = CreatePedidoPayload(produtos=[{'produto_id': 1, 'quantidade': 1}])
    repository = PedidoRepository(database)
    service = PedidoService(repository)
    database.add(PedidoModel(**PEDIDO_MODEL_LANCHE_MOCK))
    database.commit()
    # act
    result = service.update(pedido_id, pedido_payload)
    # assert



@pytest.mark.integration_test
def test_pedido_service_delete_then_return_pedido_entity(database):
    # arrange
    pedido_id = 1
    repository = PedidoRepository(database)
    service = PedidoService(repository)
    database.add(PedidoModel(**PEDIDO_MODEL_LANCHE_MOCK))
    database.commit()
    # act
    result = service.delete(pedido_id)
    # assert



@pytest.mark.integration_test
def test_pedido_service_pending_orders_then_return_pedidos_list(database):
    # arrange
    repository = PedidoRepository(database)
    service = PedidoService(repository)
    database.add(PedidoModel(**PEDIDO_MODEL_LANCHE_MOCK))
    database.add(PedidoModel(**PEDIDO_MODEL_COMBO_MAKING_MOCK))
    database.add(PedidoModel(**PEDIDO_MODEL_REFRIGERANTE_MOCK))
    database.commit()
    # act
    result = service.pending_orders()
    # assert


@pytest.mark.integration_test
def test_pedido_service_get_by_status_then_return_pedido_list(database):
    # arrange
    pedido_status = 'recebido'
    repository = PedidoRepository(database)
    service = PedidoService(repository)
    database.add(PedidoModel(**PEDIDO_MODEL_LANCHE_MOCK))
    database.commit()
    # act
    result = service.get_by_status(pedido_status)
    # assert



@pytest.mark.skip
@pytest.mark.integration_test
def test_pedido_checkout_then_return(database):
    pass
