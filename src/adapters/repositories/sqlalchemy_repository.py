from typing import Any, Dict, List, Optional, Type

from sqlalchemy import Select, asc, delete, desc, func, update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from src.adapters.database.models.entity_model import EntityModel


class SQLAlchemyRepository:
     def __init__(self, session) -> None:
        self.session_db = session
        self.entity_model = EntityModel

     def get_all(self) -> Type[EntityModel] | None:
        """Get all items
        :return: list of EntityModelBase or None
        :raises ``sqlalchemy.repositories.exc.NoResultFound´´ or ``sqlalchemy.repositories.exc.MultipleResultsFound``
        """
        statement = select(self.entity_model)
        results = self.session_db.execute(statement=statement)
        return results.all()

     def search_by_id(self, model_id: int) -> Type[EntityModel] | None:
        """Get item by id
        :param: model_id: ID of the model
        :return: EntityModelBase or None
        :raises ``sqlalchemy.repositories.exc.NoResultFound´´ or ``sqlalchemy.repositories.exc.MultipleResultsFound``
        """
        statement = select(self.entity_model).where(self.entity_model.id == model_id)
        results = self.session_db.execute(statement=statement)
        result = results.one_or_none()
        if result:
            (result,) = result
        return result

     def save(self, model) -> EntityModel:
        """Save BaseModel into database
        :param: model: Model to save
        :return: Refresh model object
        """
        self.session_db.add(model)

        self.session_db.flush()

        return model

     def update(self, model, values: Dict[str, Any]) -> EntityModel | None:
        """Update BaseModel in database
        :param model_id: ID of the model
        :param values: Dictionary values of the model to be updated
        :return: None
        """
        statement = (
            update(self.entity_model)
            .where(self.entity_model.id == model.id)
            .values(**values)
            .execution_options(synchronize_session='fetch')
        )
        self.session_db.execute(statement=statement)
        self.session_db.flush()
      #   self.session_db.refresh()
        return model

     def delete(self, model_id: Optional[Type[EntityModel]]) -> Type[EntityModel] | None:
        """Delete row from database
        :param model: BaseModel to delete
        :return: None
        """
        statement = delete(self.entity_model).where(self.entity_model.id == model_id)
        self.session_db.execute(statement=statement)
        self.session_db.flush()
