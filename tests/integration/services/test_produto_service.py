from unittest.mock import Mock

import pytest

from src.adapters.repositories.produto_repository import ProdutoRepository
from src.services.produto_service import ProdutoService
from src.services.service_base import NotFoundExcepition
from src.adapters.database.models.produto_model import ProdutoModel
from tests.resouces.database.produto_model import PRODUTO_MODEL_BURGUER_MOCK
from src.schemas.produto_schema import CreateProdutoPayload


@pytest.mark.integration_test
def test_produto_service_get_all_then_return_produto_list(database):
    # arrange
    repository = ProdutoRepository(database)
    service = ProdutoService(repository)
    database.add(ProdutoModel(**PRODUTO_MODEL_BURGUER_MOCK))
    database.commit()
    # act
    result = service.get_all()
    # assert


@pytest.mark.integration_test
def test_produto_service_get_by_id_then_return_produto_entity(database):
    # arrange
    produto_id = 1
    repository = ProdutoRepository(database)
    service = ProdutoService(repository)
    database.add(ProdutoModel(**PRODUTO_MODEL_BURGUER_MOCK))
    database.commit()
    # act
    result = service.get_by_id(produto_id)
    # assert


@pytest.mark.integration_test
def test_produto_service_get_by_id_then_raise_not_found_exception(database):
    # arrange
    produto_id = 1
    repository = ProdutoRepository(database)
    service = ProdutoService(repository)
    # act
    with pytest.raises(NotFoundExcepition):
        result = service.get_by_id(produto_id)
    # assert


@pytest.mark.integration_test
def test_produto_service_create_then_return_produto_entity(database):
    # arrange
    produto_payload = CreateProdutoPayload(**PRODUTO_MODEL_BURGUER_MOCK)
    repository = ProdutoRepository(database)
    service = ProdutoService(repository)
    # act
    result = service.create(produto_payload)
    # assert


@pytest.mark.integration_test
def test_produto_service_update_then_return_produto_entity(database):
    # arrange
    produto_id = 1
    produto_payload = CreateProdutoPayload(**PRODUTO_MODEL_BURGUER_MOCK)
    repository = ProdutoRepository(database)
    service = ProdutoService(repository)
    database.add(ProdutoModel(**PRODUTO_MODEL_BURGUER_MOCK))
    database.commit()
    # act
    result = service.update(produto_id, produto_payload)
    # assert
    assert result.id == produto_id


@pytest.mark.integration_test
def test_produto_service_delete_then_return_produto_entity(database):
    # arrange
    produto_id = 1
    repository = ProdutoRepository(database)
    service = ProdutoService(repository)
    database.add(ProdutoModel(**PRODUTO_MODEL_BURGUER_MOCK))
    database.commit()
    # act
    result = service.delete(produto_id)
    # assert
    

@pytest.mark.integration_test
def test_produto_service_get_by_categoria_then_return_produto_list(database):
    # arrange
    produto_categoria = 'lanche'
    repository = ProdutoRepository(database)
    service = ProdutoService(repository)
    database.add(ProdutoModel(**PRODUTO_MODEL_BURGUER_MOCK))
    database.commit()
    # act
    result = service.get_by_categoria(produto_categoria)
    # assert
    