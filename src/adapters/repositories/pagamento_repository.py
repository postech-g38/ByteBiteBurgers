from sqlalchemy.orm.session import Session
from sqlalchemy.future import select
from fastapi import Depends

from src.adapters.database import get_database_session
from src.adapters.database.models.pagamento_model import PagamentoModel
from src.adapters.repositories.sqlalchemy_repository import SQLAlchemyRepository


class PagamentoRepository(SQLAlchemyRepository):

    def __init__(self, session: Session = Depends(get_database_session)) -> None:
        super().__init__(session)
        self.entity_model = PagamentoModel

    def get_by_pedido_id(self, pedido_id: str) -> PagamentoModel:
        stmt = select(self.entity_model).where(self.entity_model.pedido_id == pedido_id)
        result = self.session_db.execute(stmt).one_or_none()
        if result:
            result, = result
            return result
        return None
    