from unittest.mock import Mock

import pytest

from src.services.produto_service import ProdutoService
from src.services.service_base import NotFoundExcepition
from src.adapters.database.models.produto_model import ProdutoModel
from src.adapters.repositories.produto_repository import ProdutoRepository
from tests.resouces.database.produto_model import PRODUTO_MODEL_BURGUER_MOCK


def test_producto_service_get_all_then_return_produto_list():
    # arrange
    respository = Mock(ProdutoRepository)
    respository.get_all.return_valiue = [ProdutoModel(**PRODUTO_MODEL_BURGUER_MOCK)]
    service = ProdutoService(respository)
    # act
    result = service.get_all()
    # assert
    respository.get_all.assert_called_once()


def test_produto_service_get_by_id_then_return_produto_entity():
    # arrange
    produto_id = 1
    respository = Mock(ProdutoRepository)
    respository.search_by_id.return_value = ProdutoModel(**PRODUTO_MODEL_BURGUER_MOCK)
    service = ProdutoService(respository)
    # act
    result = service.get_by_id(produto_id)
    # assert
    respository.search_by_id.assert_called_once_with(produto_id)


def test_produto_service_get_by_id_then_raise_not_found_exception():
    # arrange
    produto_id = 1
    respository = Mock(ProdutoRepository)
    respository.search_by_id.return_value = None
    service = ProdutoService(respository)
    # act
    with pytest.raises(NotFoundExcepition):
        result = service.get_by_id(produto_id)
    # assert
    respository.search_by_id.assert_called_once_with(produto_id)


def test_produto_service_create_then_return_produto_entity():
    # arrange
    produto_payload = Mock()
    produto_payload.model_dump.return_value = {}
    respository = Mock(ProdutoRepository)
    respository.save.return_value = ProdutoModel(**PRODUTO_MODEL_BURGUER_MOCK)
    service = ProdutoService(respository)
    # act
    result = service.create(produto_payload)
    # assert
    respository.save.assert_called_once()

def test_produto_service_update_then_return_produto_entity():
    # arrange
    produto_id = 1
    produto_payload = Mock()
    produto_payload.model_dump.return_value = {}
    respository = Mock(ProdutoRepository)
    respository.update.return_value = ProdutoModel(**PRODUTO_MODEL_BURGUER_MOCK)
    service = ProdutoService(respository)
    # act
    result = service.update(produto_id, produto_payload)
    # assert
    respository.update.assert_called_once()

def test_produto_service_delete_then_return_produto_entity():
    # arrange
    produto_id = 1
    respository = Mock(ProdutoRepository)
    respository.delete.return_value = ProdutoModel(**PRODUTO_MODEL_BURGUER_MOCK)
    service = ProdutoService(respository)
    # act
    result = service.delete(produto_id)
    # assert
    respository.delete.assert_called_once_with(produto_id)
    

def test_produto_service_get_by_categoria_then_return_produto_list():
    # arrange
    produto_categoria = ''
    respository = Mock(ProdutoRepository)
    respository.get_by_categoria.return_value = [ProdutoModel(**PRODUTO_MODEL_BURGUER_MOCK)]
    service = ProdutoService(respository)
    # act
    result = service.get_by_categoria(produto_categoria)
    # assert
    respository.get_by_categoria.assert_called_once_with(produto_categoria)
    