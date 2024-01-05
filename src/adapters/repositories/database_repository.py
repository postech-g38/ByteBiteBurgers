from typing import Type, Dict, Any
from abc import ABC, abstractmethod

from src.adapters.database.models.entity_model import EntityModel


class DatabaseRepository(ABC):

    @abstractmethod
    def get_all(self) -> Type[EntityModel] | None:
        raise NotImplementedError
    
    @abstractmethod
    def search_by_id(self, model_id: int) -> Type[EntityModel] | None:
        raise NotImplementedError
    
    @abstractmethod
    def save(self, model) -> EntityModel:
        raise NotImplementedError

    @abstractmethod
    def update(self, model_id: int, values: Dict[str, Any]) -> tuple[Any] | None:
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, model):
        raise NotImplementedError
    