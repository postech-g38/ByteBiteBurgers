from pydantic import BaseModel


class QueryPaginate(BaseModel):
    page: int = 1
    size: int = 50
    order: str = 'created_at:desc'
    