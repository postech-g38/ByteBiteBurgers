from unittest.mock import Mock

import pytest

from src.services.service_base import BaseService, NotFoundExcepition


def test_base_service_query_result_then_return_result():
    # arrange
    query = Mock()
    # act
    result = BaseService.query_result(query)
    # assert
    assert result is query


def test_base_service_query_result_then_raise_not_found_exception():
    # arrange
    query = None
    # act
    with pytest.raises(NotFoundExcepition) as query_exception:
        result = BaseService.query_result(query)
    # assert
    assert query_exception.type is NotFoundExcepition
    assert query_exception.value.status_code == 204
    assert query_exception.value.detail == 'values not found'
