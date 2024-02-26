from dataclasses import dataclass
from typing import Any

from fastapi import  HTTPException
from starlette import status


class NotFoundExcepition(HTTPException):
    def __init__(self, model: str = 'values') -> None:
        detail = f"{model} not found"
        super().__init__(status_code=status.HTTP_204_NO_CONTENT, detail=detail)


@dataclass
class BaseController:
    @classmethod
    def query_result(cls, result: list[Any] | dict[str, Any]) -> Any:
        """Return the result if exists or raise exception"""
        if result:
            return result
        raise NotFoundExcepition()
