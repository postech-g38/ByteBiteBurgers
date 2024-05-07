from enum import Enum

from pydantic import BaseModel


class OrderBy(Enum):
    CREATED_AT_DESC = 'created_at:desc'
    CREATED_AT_ASC = 'created_at:asc'


class QueryPaginate(BaseModel):
    page: int = 1
    size: int = 50
    order_by: OrderBy = OrderBy.CREATED_AT_DESC.value
