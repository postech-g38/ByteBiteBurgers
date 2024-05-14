from dataclasses import dataclass
from typing import Any, List, Dict, ClassVar

from fastapi import  HTTPException
from starlette import status


class NotFoundExcepition(HTTPException):
    def __init__(self, model: str = 'values') -> None:
        detail = f"{model} not found"
        super().__init__(status.HTTP_204_NO_CONTENT, detail)


@dataclass
class BaseService:

    @classmethod
    def query_result(cls, result: List[Any] | Dict[str, Any] | None) -> Any:
        """Return the result if exists or raise exception"""
        if result:
            return result
        